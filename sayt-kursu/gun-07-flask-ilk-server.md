# Gün 7 — Flask: ilk server, şablonlar

**Məqsəd:** HTML səhifələrini Python serverindən vermək və məlumatı Python-dan HTML-ə ötürmək.

Flask Python-da veb server yazmaq üçün framework-dür: sorğunu qəbul edir, hansı funksiyanın işləyəcəyini seçir, cavabı qaytarır.

## 1. Minimal server

```bash
pip install flask && pip freeze > requirements.txt
```

`app.py`:
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Salam"

if __name__ == "__main__":
    app.run(debug=True)
```
```bash
python app.py
```
Aç: `http://127.0.0.1:5000`. `127.0.0.1` sənin kompüterindir, `5000` isə port.
`debug=True` kodu dəyişəndə serveri yenidən başladır və xətaları göstərir. Yalnız lokalda işlət.

## 2. Route-lar

```python
from flask import request

@app.route("/qeyd/<int:id>")          # URL-dən dəyər götürmək
def qeyd(id):
    return f"Qeyd {id}"

@app.route("/axtar")
def axtar():
    soz = request.args.get("q", "")   # /axtar?q=süd
    return f"Axtarış: {soz}"
```

## 3. Layihə strukturu

```
qeydler/
├── app.py
├── requirements.txt
├── templates/        ← HTML (Jinja şablonları)
│   ├── base.html
│   └── index.html
└── static/           ← CSS, JS, şəkillər
    ├── style.css
    └── app.js
```

## 4. Şablonlar (Jinja)

`templates/base.html` (ortaq hissə, bir dəfə yazılır):
```html
<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Qeydlər{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('index') }}">Qeydlər</a>
        <a href="{{ url_for('elaqe') }}">Əlaqə</a>
    </nav>
    <main>{% block content %}{% endblock %}</main>
</body>
</html>
```

`templates/index.html`:
```html
{% extends "base.html" %}
{% block content %}
    {% for q in qeydler %}
        <article class="kart">
            <h2><a href="{{ url_for('qeyd', id=q.id) }}">{{ q.basliq }}</a></h2>
            <p>{{ q.metn }}</p>
        </article>
    {% else %}
        <p>Qeyd yoxdur.</p>
    {% endfor %}
{% endblock %}
```

`app.py`:
```python
from flask import Flask, render_template, abort

app = Flask(__name__)

qeydler = [
    {"id": 1, "basliq": "Alış-veriş", "metn": "Çörək, süd"},
    {"id": 2, "basliq": "İş", "metn": "Hesabat"},
]

@app.route("/")
def index():
    return render_template("index.html", qeydler=qeydler)

@app.route("/qeyd/<int:id>")
def qeyd(id):
    q = next((q for q in qeydler if q["id"] == id), None)
    if q is None:
        abort(404)
    return render_template("qeyd.html", q=q)
```

Jinja sintaksisi:
- `{{ x }}`: dəyəri göstər (avtomatik escape olunur, yəni təhlükəsizdir).
- `{% if %}…{% endif %}`, `{% for %}…{% endfor %}`: məntiq.
- `{% extends %}`, `{% block %}`: şablon mirası.
- `url_for('funksiya_adı')`: linki əl ilə yazma, funksiya adından yarat.

## Tapşırıq

2–4-cü günlərdəki saytı Flask-a köçür:
1. Yuxarıdakı struktur. CSS və JS `static/` qovluğuna.
2. `base.html` + `index.html`, `qeyd.html`, `yeni.html`, `elaqe.html`. Hamısı `extends "base.html"` etsin.
3. Qeydlər HTML-də yox, `app.py`-dəki siyahıdan gəlsin (5-ci gündəki funksiyaları istifadə et).
4. `/qeyd/<id>` ünvanı mövcud olmayan id üçün 404 versin.
5. `/axtar?q=...`: nəticəni `index.html` ilə göstər.

## Yoxlama

1. `templates` və `static` qovluqlarında nə saxlanılır?
2. Linki niyə `url_for` ilə yaradırıq?
3. `{{ }}` və `{% %}` arasındakı fərq nədir?
4. `/qeyd/<int:id>`-də `int:` nə edir?
