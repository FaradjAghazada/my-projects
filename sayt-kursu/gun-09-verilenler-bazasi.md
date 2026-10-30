# Gün 9 — Verilənlər bazası: saytın yaddaşı 🗄️

## 📚 Nağıl

Python siyahısı — **qumun üstünə yazılmış yazı**: server söndü, dalğa gəldi, silindi.
**Verilənlər bazası (database)** — **daşa həkk olunmuş yazı**: server min dəfə sönsə də qalır.

Baza **Excel cədvəlinə** bənzəyir:

**`yazilar` cədvəli:**
| id | basliq | metn | yaradilib |
|---|---|---|---|
| 1 | İlk yazım | Salam dünya | 2026-10-30 |
| 2 | Python | Çox maraqlıdır | 2026-10-31 |

- **Cədvəl (table)** = vərəq
- **Sütun (column)** = başlıq (`basliq`, `metn`)
- **Sətir (row)** = bir qeyd
- **id (primary key)** = hər sətrin unikal nömrəsi, pasport kimi

## 🗣️ SQL — baza ilə danışmaq dili

CRUD = bazada edə biləcəyin 4 şey:

```sql
-- Create (yarat)
INSERT INTO yazilar (basliq, metn) VALUES ('İlk yazım', 'Salam dünya');
-- Read (oxu)
SELECT * FROM yazilar WHERE id = 1;
-- Update (dəyiş)
UPDATE yazilar SET basliq = 'Yeni başlıq' WHERE id = 1;
-- Delete (sil)
DELETE FROM yazilar WHERE id = 1;
```
⚠️ `UPDATE` və `DELETE`-də `WHERE` unutsan — **bütün** sətirlər dəyişər/silinər!

## 🐍 Python ilə: SQLite (heç nə quraşdırmaq lazım deyil)

SQLite — bütün baza **bir fayldadır**. Öyrənmək üçün ideal.

```python
import sqlite3

conn = sqlite3.connect("sayt.db")
conn.execute("""
    CREATE TABLE IF NOT EXISTS yazilar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        basliq TEXT NOT NULL,
        metn TEXT NOT NULL
    )
""")
conn.execute("INSERT INTO yazilar (basliq, metn) VALUES (?, ?)", ("Salam", "İlk yazı"))
conn.commit()     # dəyişiklikləri yadda saxla!

for setir in conn.execute("SELECT id, basliq FROM yazilar"):
    print(setir)
conn.close()
```

### 💉 SQL Injection — ən təhlükəli səhv

```python
# ❌ HEÇ VAXT BELƏ ETMƏ:
conn.execute(f"SELECT * FROM users WHERE ad = '{ad}'")
# İstifadəçi ad yerinə  ' OR '1'='1  yazsa — bütün istifadəçiləri oğurlayar!

# ✅ HƏMİŞƏ ? işarəsi ilə:
conn.execute("SELECT * FROM users WHERE ad = ?", (ad,))
```

## 🪄 ORM: SQLAlchemy — SQL-i Python kimi yazmaq

Hər dəfə SQL yazmaq yorucudur. **ORM** cədvəlləri **Python class**-larına çevirir.

```bash
pip install flask-sqlalchemy
```

```python
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sayt.db"
db = SQLAlchemy(app)

class Yazi(db.Model):                                  # bu class = cədvəl
    id = db.Column(db.Integer, primary_key=True)
    basliq = db.Column(db.String(200), nullable=False)
    metn = db.Column(db.Text, nullable=False)
    yaradilib = db.Column(db.DateTime, default=datetime.now)

with app.app_context():
    db.create_all()                                    # cədvəli yarat (yoxdursa)

@app.route("/")
def index():
    yazilar = Yazi.query.order_by(Yazi.yaradilib.desc()).all()   # SELECT
    return render_template("index.html", yazilar=yazilar)

@app.route("/yeni", methods=["POST"])
def yeni():
    yazi = Yazi(basliq=request.form["basliq"], metn=request.form["metn"])
    db.session.add(yazi)                               # INSERT
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/sil/<int:id>", methods=["POST"])
def sil(id):
    yazi = db.get_or_404(Yazi, id)                     # tapılmasa → 404
    db.session.delete(yazi)                            # DELETE
    db.session.commit()
    return redirect(url_for("index"))
```

## 🔗 Cədvəllər arası əlaqə (bir istifadəçi → çox yazı)

```python
class Istifadeci(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad = db.Column(db.String(80), unique=True)
    yazilar = db.relationship("Yazi", backref="muellif")

class Yazi(db.Model):
    # ...
    istifadeci_id = db.Column(db.Integer, db.ForeignKey("istifadeci.id"))
```
`ForeignKey` = "bu yazı **o** istifadəçiyə aiddir" deyən ip.

> 🌐 Real saytda (hosting-də) adətən **PostgreSQL** istifadə olunur. Yaxşı xəbər: SQLAlchemy ilə
> yalnız `DATABASE_URI` sətrini dəyişirsən, qalan kod eyni qalır!

## 🎯 Tapşırıq

Dünənki "Qonaq kitabı"nı SQLAlchemy ilə yenidən yaz:
1. `Mesaj` modeli: `id`, `ad`, `metn`, `tarix`.
2. Mesajlar bazaya yazılsın. Serveri söndür-yandır — mesajlar **qalmalıdır** ✅.
3. Hər mesajın yanında "Sil" düyməsi (`POST` forması ilə).
4. Bonus: "Redaktə et" — `/redakte/<id>` səhifəsi (UPDATE).
5. Bonus: VS Code-a **SQLite Viewer** əlavəsini qoy, `sayt.db`-nin içinə bax.

## ✅ Gün sonu yoxlama

1. CRUD-un 4 hərfi nə deməkdir?
2. Primary key nədir?
3. SQL injection nədir və necə qorunuruq?
4. `db.session.commit()` yazmasan nə olar?
