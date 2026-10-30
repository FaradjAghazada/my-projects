# Gün 9 — Verilənlər bazası

**Məqsəd:** məlumatı server yenidən başlayanda itməyəcək şəkildə saxlamaq.

## 1. Relyasiya bazası

Məlumat cədvəllərdə saxlanılır:

**`qeyd` cədvəli**
| id | basliq | metn | yaradilib |
|---|---|---|---|
| 1 | Alış-veriş | Çörək, süd | 2026-10-30 10:00 |

- **Sütun**: sahə (tipi var: mətn, ədəd, tarix).
- **Sətir**: bir qeyd.
- **Primary key (`id`)**: sətrin unikal identifikatoru.
- **Foreign key**: başqa cədvəlin sətrinə istinad (məs. qeydin müəllifi, 12-ci gün).

İnkişaf zamanı **SQLite** (bir fayl, quraşdırma tələb etmir), hosting-də **PostgreSQL** işlədirik. Kod eyni qalır.

## 2. SQL: əsası bil

Bazaya bu 4 əmr ilə müraciət olunur (CRUD):
```sql
INSERT INTO qeyd (basliq, metn) VALUES ('X', 'Y');   -- Create
SELECT * FROM qeyd WHERE id = 1;                      -- Read
UPDATE qeyd SET basliq = 'Z' WHERE id = 1;            -- Update
DELETE FROM qeyd WHERE id = 1;                        -- Delete
```
SQL-i ORM vasitəsilə yazacaqsan, amma arxada nə baş verdiyini bilməlisən.

**SQL injection:** istifadəçi daxil etdiyini SQL mətninə birləşdirmək ən təhlükəli səhvdir:
```python
f"SELECT * FROM user WHERE email = '{email}'"       # QADAĞANDIR
```
ORM bunu avtomatik olaraq təhlükəsiz edir. Xam SQL yazanda isə parametr işlət: `execute("... WHERE email = ?", (email,))`.

## 3. Flask-SQLAlchemy

```bash
pip install flask-sqlalchemy && pip freeze > requirements.txt
```

```python
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sayt.db"
db = SQLAlchemy(app)

class Qeyd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    basliq = db.Column(db.String(200), nullable=False)
    metn = db.Column(db.Text, nullable=False, default="")
    yaradilib = db.Column(db.DateTime, default=datetime.now)

with app.app_context():
    db.create_all()      # cədvəllər yoxdursa yaradır
```

## 4. CRUD əməliyyatları

```python
# Create
q = Qeyd(basliq="X", metn="Y")
db.session.add(q)
db.session.commit()           # commit olmadan heç nə yazılmır

# Read
Qeyd.query.order_by(Qeyd.yaradilib.desc()).all()       # hamısı
db.get_or_404(Qeyd, id)                                 # biri, yoxdursa 404
Qeyd.query.filter(Qeyd.basliq.ilike(f"%{soz}%")).all()  # axtarış (təhlükəsizdir)

# Update
q.basliq = "Yeni"
db.session.commit()

# Delete
db.session.delete(q)
db.session.commit()
```

Şablonda `q["basliq"]` əvəzinə `q.basliq` yazılır (Jinja hər ikisini qəbul edir).

## 5. Struktur dəyişəndə

`db.create_all()` mövcud cədvəli dəyişmir. Modelə yeni sütun əlavə etdinsə, inkişaf zamanı `sayt.db` faylını sil və serveri yenidən başlat. Real layihədə bunun üçün `Flask-Migrate` istifadə olunur, amma 14 gündən sonra.

## Tapşırıq

1. Python siyahısını `Qeyd` modeli ilə əvəz et. 5-ci gündəki funksiyalar artıq lazım deyil.
2. Ana səhifə, qeyd səhifəsi, yeni qeyd, silmə və axtarış bazadan işləsin.
3. Redaktə: `/qeyd/<id>/redakte` (GET forma, POST yadda saxla). Forma `yeni.html` ilə eyni olsun, şablonu təkrar istifadə et.
4. Serveri yenidən başlat. Qeydlər yerində qalmalıdır.

## Yoxlama

1. `db.session.commit()` olmasa nə olur?
2. Primary key və foreign key nədir?
3. SQL injection nədir və necə qarşısı alınır?
