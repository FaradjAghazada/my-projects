# Gün 12 — Qeydiyyat, login və təhlükəsizlik 🔐

## 🎟️ Nağıl

Əyləncə parkına girirsən. Kassada bilet alırsan (**login**), qoluna **bilərzik** taxırlar (**session/cookie**).
Hər attraksionda bilet soruşmurlar — bilərziyinə baxırlar. Bilərzik yoxdursa — "Kassaya get!" (**redirect to login**).

- **Authentication (kimlik)** — "Sən kimsən?" (login)
- **Authorization (icazə)** — "Sənə bu icazəlidir?" (məs. yalnız öz yazını silə bilərsən)

## 🧂 Parolu HEÇ VAXT açıq saxlama!

Baza oğurlansa, parollar açıq görünməməlidir. Parolu **hash** edirik:
hash = **qiymə maşını**. Ətdən qiymə olur, qiymədən ət geri olmur. 🥩➡️🍖

```python
from werkzeug.security import generate_password_hash, check_password_hash
# (werkzeug Flask ilə birlikdə gəlir)

h = generate_password_hash("gizli123")
print(h)   # scrypt:32768:8:1$....  — oxunmaz
check_password_hash(h, "gizli123")   # True
check_password_hash(h, "sehv")       # False
```

## 🍪 Session — Flask-ın bilərziyi

```python
from flask import session

app.secret_key = os.environ.get("SECRET_KEY", "dev")   # bilərziyi saxtalaşdırmamaq üçün möhür
```
`SECRET_KEY` yaratmaq: `python -c "import secrets; print(secrets.token_hex(32))"`

## 👤 Tam nümunə

```python
from functools import wraps
from flask import session, flash, redirect, url_for, request, render_template, g

class Istifadeci(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    parol_hash = db.Column(db.String(256), nullable=False)

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
            u = Istifadeci(email=email, parol_hash=generate_password_hash(parol))
            db.session.add(u)
            db.session.commit()
            flash("Qeydiyyat uğurludur, indi daxil ol", "ugur")
            return redirect(url_for("login"))
    return render_template("qeydiyyat.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = Istifadeci.query.filter_by(email=request.form.get("email", "").strip().lower()).first()
        if u and check_password_hash(u.parol_hash, request.form.get("parol", "")):
            session.clear()
            session["user_id"] = u.id                  # 🎟️ bilərziyi taxdıq
            return redirect(url_for("index"))
        flash("Email və ya parol səhvdir", "xeta")      # hansının səhv olduğunu demirik!
    return render_template("login.html")

@app.route("/cixis", methods=["POST"])
def cixis():
    session.clear()                                     # bilərziyi çıxardıq
    return redirect(url_for("index"))

# 🛂 Mühafizəçi dekorator — yalnız login olanlar keçsin
def login_lazimdir(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper

@app.route("/panel")
@login_lazimdir
def panel():
    return "Bura yalnız daxil olanlar üçündür 🔒"
```

Avtorizasiya nümunəsi (yalnız müəllif silə bilər):
```python
if yazi.muellif_id != session["user_id"]:
    abort(403)
```

> Böyük layihələrdə **Flask-Login** paketi bu işləri daha rahat edir. Amma əvvəl prinsipi başa düşmək üçün özün yaz.

## 🛡️ Təhlükəsizlik yoxlama siyahısı

| Təhlükə | Nədir | Qoruma |
|---|---|---|
| **SQL Injection** | Formadan SQL kodu yeritmək | ORM və ya `?` parametrləri (9-cu gün) |
| **XSS** | Formadan `<script>` yeritmək | Jinja `{{ }}` avtomatik escape; `\|safe` istifadə etmə |
| **CSRF** | Başqa sayt sənin adından forma göndərir | `Flask-WTF` CSRF tokenləri; silmə/dəyişmə yalnız POST ilə |
| **Parol oğurluğu** | Baza sızır | Hash (`generate_password_hash`) |
| **Açar sızması** | API key GitHub-da | `.env` + `.gitignore` |
| **Brute force** | Milyon parol yoxlamaq | `Flask-Limiter` ilə sorğu limiti |
| **Debug rejimi** | Xəta səhifəsi kodu göstərir | Hosting-də `debug=False`! |
| **HTTP** | Məlumat açıq gedir | Həmişə HTTPS (14-cü gün) |

## 🎯 Tapşırıq

1. Qeydiyyat, login, çıxış səhifələri.
2. Menyu: login olmayana "Daxil ol / Qeydiyyat", olana "Çıxış" göstərsin.
3. Yazı yaratmaq yalnız login olanlara icazəli olsun.
4. Hər yazı müəllifinə bağlansın (`ForeignKey`), yalnız müəllif silə bilsin.
5. `sayt.db`-yə bax: parollar oxunmaz olmalıdır ✅.

## ✅ Gün sonu yoxlama

1. Authentication və authorization fərqi?
2. Parolu niyə hash edirik?
3. Session nədir və `SECRET_KEY` nə üçündür?
4. Login səhv olanda niyə "email səhvdir" demirik?
