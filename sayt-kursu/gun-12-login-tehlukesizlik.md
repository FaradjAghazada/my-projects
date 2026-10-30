# Gün 12 — Qeydiyyat, login, təhlükəsizlik

**Məqsəd:** istifadəçi hesabları və hər istifadəçinin yalnız öz qeydlərini idarə etməsi.

- **Authentication**: istifadəçinin kim olduğunu müəyyən etmək (login).
- **Authorization**: həmin istifadəçiyə nəyə icazə olduğunu yoxlamaq.

## 1. Parol hash-i

Parol bazada heç vaxt açıq saxlanmır. Geri çevrilə bilməyən **hash** saxlanılır:
```python
from werkzeug.security import generate_password_hash, check_password_hash

h = generate_password_hash("parol123")   # bazaya bu yazılır
check_password_hash(h, "parol123")       # True
```

## 2. Session

Login olandan sonra Flask istifadəçinin id-sini imzalanmış **cookie**-də saxlayır. `SECRET_KEY` bu imzanın açarıdır: kim onu bilirsə, istənilən istifadəçinin adından cookie düzəldə bilər. Ona görə uzun və təsadüfi olmalı və `.env`-də saxlanmalıdır:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
```python
from flask import session
app.secret_key = os.environ["SECRET_KEY"]
session["user_id"] = 5        # yaz
session.get("user_id")        # oxu
session.clear()               # çıxış
```

## 3. Modellər

```python
class Istifadeci(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    parol_hash = db.Column(db.String(256), nullable=False)
    qeydler = db.relationship("Qeyd", backref="muellif")

class Qeyd(db.Model):
    # ... əvvəlki sütunlar
    muellif_id = db.Column(db.Integer, db.ForeignKey("istifadeci.id"), nullable=False)
```
Strukturu dəyişdin, ona görə `sayt.db` faylını sil.

## 4. Qeydiyyat, login, çıxış

```python
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
            return redirect(url_for("login"))
    return render_template("qeydiyyat.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = Istifadeci.query.filter_by(email=request.form.get("email", "").strip().lower()).first()
        if u and check_password_hash(u.parol_hash, request.form.get("parol", "")):
            session.clear()
            session["user_id"] = u.id
            return redirect(url_for("index"))
        flash("Email və ya parol səhvdir", "xeta")   # hansının səhv olduğunu demə
    return render_template("login.html")

@app.post("/cixis")
def cixis():
    session.clear()
    return redirect(url_for("index"))
```

## 5. Səhifəni qorumaq

```python
from functools import wraps
from flask import abort

def login_lazimdir(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper

@app.route("/qeyd/<int:id>/sil", methods=["POST"])
@login_lazimdir
def sil(id):
    q = db.get_or_404(Qeyd, id)
    if q.muellif_id != session["user_id"]:
        abort(403)                      # authorization
    db.session.delete(q)
    db.session.commit()
    return redirect(url_for("index"))
```

Cari istifadəçini bütün şablonlarda əlçatan etmək (menyuda "Daxil ol" və ya "Çıxış" göstərmək üçün):
```python
@app.context_processor
def cari_istifadeci():
    uid = session.get("user_id")
    return {"istifadeci": db.session.get(Istifadeci, uid) if uid else None}
```

## 6. Təhlükəsizlik minimumu

| Risk | Qoruma |
|---|---|
| SQL injection | ORM / parametrli sorğu |
| XSS (səhifəyə skript yeritmək) | Jinja `{{ }}` escape edir; `\|safe` və `innerHTML` istifadəçi məlumatına işlətmə |
| Parol sızması | Hash |
| Açar sızması | `.env`, `.gitignore` |
| Başqasının resursunu dəyişmək | Hər dəyişiklikdə sahibliyi yoxla (403) |
| Debug səhifəsinin açıq qalması | Hosting-də `debug` söndürülü |
| Trafikin oxunması | HTTPS (14-cü gün) |
| CSRF | Silmə və dəyişmə yalnız POST ilə; real layihədə `Flask-WTF` |

## Tapşırıq

1. Qeydiyyat, login, çıxış səhifələri.
2. Menyu login vəziyyətinə görə dəyişsin.
3. Qeyd yaratmaq, redaktə və silmə yalnız login olmuş istifadəçiyə açıq olsun. Redaktə və silmə yalnız müəllifə.
4. API-də də eyni qaydalar: login yoxdursa `401`, müəllif deyilsə `403` JSON cavabı.
5. İki ayrı hesabla (ikincisi üçün brauzerin gizli pəncərəsini aç) birinin qeydini o birindən silməyə çalış. `403` almalısan.

## Yoxlama

1. Authentication və authorization arasındakı fərq nədir?
2. `SECRET_KEY` sızarsa nə olar?
3. Login uğursuz olanda niyə "email səhvdir" yox, "email və ya parol səhvdir" deyirik?
4. Qeydi silməzdən əvvəl hansı iki yoxlama aparılır?
