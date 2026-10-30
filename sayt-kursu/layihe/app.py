"""Yekun layihə: "Qeydlərim" — kursda öyrəndiyin hər şey bir yerdə.

İşə salmaq:
    python -m venv venv
    source venv/bin/activate        # Windows: venv\\Scripts\\activate
    pip install -r requirements.txt
    cp .env.example .env            # və içini doldur
    python app.py                   # http://127.0.0.1:5000
"""
import os
from datetime import datetime
from functools import wraps

import requests
from dotenv import load_dotenv
from flask import (Flask, abort, flash, jsonify, redirect, render_template,
                   request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()  # .env faylını oxu (Gün 11)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-acar-hostingde-deyis")

# Hosting-də DATABASE_URL (PostgreSQL), lokalda SQLite (Gün 13)
db_url = os.environ.get("DATABASE_URL", "sqlite:///sayt.db")
app.config["SQLALCHEMY_DATABASE_URI"] = db_url.replace("postgres://", "postgresql://", 1)
db = SQLAlchemy(app)


# ───────────── Modellər (Gün 9) ─────────────
class Istifadeci(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    parol_hash = db.Column(db.String(256), nullable=False)
    yazilar = db.relationship("Yazi", backref="muellif", lazy=True)


class Yazi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    basliq = db.Column(db.String(200), nullable=False)
    metn = db.Column(db.Text, nullable=False)
    yaradilib = db.Column(db.DateTime, default=datetime.now)
    muellif_id = db.Column(db.Integer, db.ForeignKey("istifadeci.id"), nullable=False)

    def dict(self):
        return {
            "id": self.id,
            "basliq": self.basliq,
            "metn": self.metn,
            "yaradilib": self.yaradilib.isoformat(timespec="minutes"),
            "muellif": self.muellif.email,
        }


with app.app_context():
    db.create_all()


# ───────────── İnteqrasiyalar (Gün 11) ─────────────
def hava_al(enlik=40.41, uzunluq=49.87):
    """Bakının havası. Xidmət çöksə None qaytarır — saytımız çökmür."""
    try:
        r = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": enlik, "longitude": uzunluq, "current_weather": "true"},
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


# ───────────── Login köməkçiləri (Gün 12) ─────────────
def login_lazimdir(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            flash("Əvvəlcə daxil ol", "xeta")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper


@app.context_processor
def cari_istifadeci():
    """Bütün şablonlarda `istifadeci` dəyişəni olsun."""
    uid = session.get("user_id")
    return {"istifadeci": db.session.get(Istifadeci, uid) if uid else None}


# ───────────── Səhifələr (Gün 7-8) ─────────────
@app.route("/")
def index():
    yazilar = Yazi.query.order_by(Yazi.yaradilib.desc()).all()
    return render_template("index.html", yazilar=yazilar, temperatur=hava_al())


@app.route("/yazi/<int:id>")
def yazi(id):
    return render_template("yazi.html", yazi=db.get_or_404(Yazi, id))


@app.route("/yeni", methods=["GET", "POST"])
@login_lazimdir
def yeni():
    if request.method == "POST":
        basliq = request.form.get("basliq", "").strip()
        metn = request.form.get("metn", "").strip()
        if not basliq or not metn:
            flash("Başlıq və mətn boş ola bilməz", "xeta")
            return render_template("yeni.html", basliq=basliq, metn=metn)
        y = Yazi(basliq=basliq, metn=metn, muellif_id=session["user_id"])
        db.session.add(y)
        db.session.commit()
        flash("Yazı əlavə olundu ✅", "ugur")
        return redirect(url_for("yazi", id=y.id))
    return render_template("yeni.html")


@app.route("/yazi/<int:id>/sil", methods=["POST"])
@login_lazimdir
def sil(id):
    y = db.get_or_404(Yazi, id)
    if y.muellif_id != session["user_id"]:
        abort(403)  # yalnız müəllif silə bilər (authorization)
    db.session.delete(y)
    db.session.commit()
    flash("Yazı silindi", "ugur")
    return redirect(url_for("index"))


@app.route("/elaqe", methods=["GET", "POST"])
def elaqe():
    if request.method == "POST":
        ad = request.form.get("ad", "").strip()
        mesaj = request.form.get("mesaj", "").strip()
        if not ad or not mesaj:
            flash("Ad və mesaj boş ola bilməz", "xeta")
            return render_template("elaqe.html", ad=ad, mesaj=mesaj)
        telegram_gonder(f"📩 Saytdan mesaj\n{ad}: {mesaj}")
        flash("Mesajın göndərildi, təşəkkürlər! 🙌", "ugur")
        return redirect(url_for("elaqe"))  # Post → Redirect → Get
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
            flash("Qeydiyyat uğurludur, indi daxil ol", "ugur")
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
            flash("Xoş gəldin! 👋", "ugur")
            return redirect(url_for("index"))
        flash("Email və ya parol səhvdir", "xeta")
    return render_template("login.html")


@app.route("/cixis", methods=["POST"])
def cixis():
    session.clear()
    return redirect(url_for("index"))


# ───────────── JSON API (Gün 10) ─────────────
@app.get("/api/yazilar")
def api_yazilar():
    yazilar = Yazi.query.order_by(Yazi.yaradilib.desc()).all()
    return jsonify([y.dict() for y in yazilar])


@app.get("/api/yazilar/<int:id>")
def api_yazi(id):
    return jsonify(db.get_or_404(Yazi, id).dict())


@app.post("/api/yazilar")
def api_yazi_yarat():
    if "user_id" not in session:
        return jsonify({"xeta": "əvvəlcə daxil ol"}), 401
    data = request.get_json(silent=True) or {}
    basliq = (data.get("basliq") or "").strip()
    metn = (data.get("metn") or "").strip()
    if not basliq or not metn:
        return jsonify({"xeta": "basliq və metn mütləqdir"}), 400
    y = Yazi(basliq=basliq, metn=metn, muellif_id=session["user_id"])
    db.session.add(y)
    db.session.commit()
    return jsonify(y.dict()), 201


@app.errorhandler(404)
def tapilmadi(e):
    if request.path.startswith("/api/"):
        return jsonify({"xeta": "tapılmadı"}), 404
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)  # yalnız lokalda; hosting-də gunicorn işlədir
