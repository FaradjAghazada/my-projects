"""Qeydlər saytı: 14 günlük kursun yekun nəticəsi."""
import os
from datetime import datetime
from functools import wraps

import requests
from dotenv import load_dotenv
from flask import (Flask, abort, flash, jsonify, redirect, render_template,
                   request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

db_url = os.environ.get("DATABASE_URL", "sqlite:///sayt.db")
app.config["SQLALCHEMY_DATABASE_URI"] = db_url.replace("postgres://", "postgresql://", 1)
db = SQLAlchemy(app)


# ── Modellər ──────────────────────────────────────────────
class Istifadeci(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    parol_hash = db.Column(db.String(256), nullable=False)
    qeydler = db.relationship("Qeyd", backref="muellif")


class Qeyd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    basliq = db.Column(db.String(200), nullable=False)
    metn = db.Column(db.Text, nullable=False, default="")
    yaradilib = db.Column(db.DateTime, default=datetime.now)
    muellif_id = db.Column(db.Integer, db.ForeignKey("istifadeci.id"), nullable=False)


with app.app_context():
    db.create_all()


def qeyd_json(q):
    return {"id": q.id, "basliq": q.basliq, "metn": q.metn,
            "yaradilib": q.yaradilib.isoformat(timespec="minutes"),
            "muellif": q.muellif.email}


# ── İnteqrasiyalar ────────────────────────────────────────
def hava_al():
    try:
        r = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": 40.41, "longitude": 49.87, "current_weather": "true"},
            timeout=5,
        )
        r.raise_for_status()
        return r.json()["current_weather"]["temperature"]
    except (requests.RequestException, KeyError, ValueError):
        return None


def telegram_gonder(metn):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return False
    try:
        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": metn},
            timeout=5,
        )
        return r.ok
    except requests.RequestException:
        return False


# ── Login köməkçiləri ─────────────────────────────────────
def login_lazimdir(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper


def oz_qeydi(id):
    """Qeydi qaytarır; yoxdursa 404, başqasınındırsa 403."""
    q = db.get_or_404(Qeyd, id)
    if q.muellif_id != session.get("user_id"):
        abort(403)
    return q


@app.context_processor
def cari_istifadeci():
    uid = session.get("user_id")
    return {"istifadeci": db.session.get(Istifadeci, uid) if uid else None}


# ── Səhifələr ─────────────────────────────────────────────
@app.route("/")
def index():
    soz = request.args.get("q", "").strip()
    sorgu = Qeyd.query
    if soz:
        sorgu = sorgu.filter(Qeyd.basliq.ilike(f"%{soz}%") | Qeyd.metn.ilike(f"%{soz}%"))
    qeydler = sorgu.order_by(Qeyd.yaradilib.desc()).all()
    return render_template("index.html", qeydler=qeydler, soz=soz, temperatur=hava_al())


@app.route("/qeyd/<int:id>")
def qeyd(id):
    return render_template("qeyd.html", q=db.get_or_404(Qeyd, id))


@app.route("/yeni", methods=["GET", "POST"])
@login_lazimdir
def yeni():
    if request.method == "POST":
        basliq = request.form.get("basliq", "").strip()
        metn = request.form.get("metn", "").strip()
        if not basliq:
            flash("Başlıq boş ola bilməz", "xeta")
            return render_template("forma.html", basliq=basliq, metn=metn), 400
        q = Qeyd(basliq=basliq, metn=metn, muellif_id=session["user_id"])
        db.session.add(q)
        db.session.commit()
        flash("Qeyd əlavə olundu", "ugur")
        return redirect(url_for("qeyd", id=q.id))
    return render_template("forma.html")


@app.route("/qeyd/<int:id>/redakte", methods=["GET", "POST"])
@login_lazimdir
def redakte(id):
    q = oz_qeydi(id)
    if request.method == "POST":
        basliq = request.form.get("basliq", "").strip()
        metn = request.form.get("metn", "").strip()
        if not basliq:
            flash("Başlıq boş ola bilməz", "xeta")
            return render_template("forma.html", basliq=basliq, metn=metn), 400
        q.basliq, q.metn = basliq, metn
        db.session.commit()
        flash("Yadda saxlanıldı", "ugur")
        return redirect(url_for("qeyd", id=q.id))
    return render_template("forma.html", basliq=q.basliq, metn=q.metn)


@app.post("/qeyd/<int:id>/sil")
@login_lazimdir
def sil(id):
    db.session.delete(oz_qeydi(id))
    db.session.commit()
    flash("Qeyd silindi", "ugur")
    return redirect(url_for("index"))


@app.route("/elaqe", methods=["GET", "POST"])
def elaqe():
    if request.method == "POST":
        ad = request.form.get("ad", "").strip()
        mesaj = request.form.get("mesaj", "").strip()
        if not ad or not mesaj:
            flash("Ad və mesaj boş ola bilməz", "xeta")
            return render_template("elaqe.html", ad=ad, mesaj=mesaj), 400
        if not telegram_gonder(f"Saytdan mesaj\n{ad}: {mesaj}"):
            print(f"Telegram göndərilmədi: {ad}: {mesaj}")
        flash("Mesajın göndərildi", "ugur")
        return redirect(url_for("elaqe"))
    return render_template("elaqe.html")


@app.route("/qeydiyyat", methods=["GET", "POST"])
def qeydiyyat():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        parol = request.form.get("parol", "")
        if not email or len(parol) < 8:
            flash("Email lazımdır, parol ən az 8 simvol olmalıdır", "xeta")
        elif Istifadeci.query.filter_by(email=email).first():
            flash("Bu email artıq qeydiyyatdadır", "xeta")
        else:
            db.session.add(Istifadeci(email=email, parol_hash=generate_password_hash(parol)))
            db.session.commit()
            flash("Qeydiyyat uğurludur, daxil ol", "ugur")
            return redirect(url_for("login"))
    return render_template("qeydiyyat.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        u = Istifadeci.query.filter_by(email=email).first()
        if u and check_password_hash(u.parol_hash, request.form.get("parol", "")):
            session.clear()
            session["user_id"] = u.id
            return redirect(url_for("index"))
        flash("Email və ya parol səhvdir", "xeta")
    return render_template("login.html")


@app.post("/cixis")
def cixis():
    session.clear()
    return redirect(url_for("index"))


# ── JSON API ──────────────────────────────────────────────
def api_login_lazimdir(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"xeta": "login lazımdır"}), 401
        return f(*args, **kwargs)
    return wrapper


@app.get("/api/qeydler")
def api_siyahi():
    return jsonify([qeyd_json(q) for q in Qeyd.query.order_by(Qeyd.yaradilib.desc())])


@app.get("/api/qeydler/<int:id>")
def api_bir(id):
    return jsonify(qeyd_json(db.get_or_404(Qeyd, id)))


@app.post("/api/qeydler")
@api_login_lazimdir
def api_yarat():
    data = request.get_json(silent=True) or {}
    basliq = (data.get("basliq") or "").strip()
    if not basliq:
        return jsonify({"xeta": "basliq mütləqdir"}), 400
    q = Qeyd(basliq=basliq, metn=(data.get("metn") or "").strip(),
             muellif_id=session["user_id"])
    db.session.add(q)
    db.session.commit()
    return jsonify(qeyd_json(q)), 201


@app.patch("/api/qeydler/<int:id>")
@api_login_lazimdir
def api_deyis(id):
    q = oz_qeydi(id)
    data = request.get_json(silent=True) or {}
    if "basliq" in data:
        basliq = (data["basliq"] or "").strip()
        if not basliq:
            return jsonify({"xeta": "basliq boş ola bilməz"}), 400
        q.basliq = basliq
    if "metn" in data:
        q.metn = (data["metn"] or "").strip()
    db.session.commit()
    return jsonify(qeyd_json(q))


@app.delete("/api/qeydler/<int:id>")
@api_login_lazimdir
def api_sil(id):
    db.session.delete(oz_qeydi(id))
    db.session.commit()
    return "", 204


@app.errorhandler(403)
@app.errorhandler(404)
def xeta_sehifesi(e):
    if request.path.startswith("/api/"):
        return jsonify({"xeta": e.name}), e.code
    return render_template("xeta.html", kod=e.code), e.code


if __name__ == "__main__":
    app.run(debug=True)
