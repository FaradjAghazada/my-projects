# Gün 7 — Flask: ilk backend serverin 🍳

## 🏪 Nağıl

İndiyə qədər sən **müştəri** idin (başqasının API-sinə sorğu göndərirdin).
Bu gün **öz restoranını açırsan** — sorğuları **sən qəbul edib, sən cavab verirsən**.

**Flask** — Python-da kiçik, sadə veb framework-dür. Framework = hazır mətbəx avadanlığı.
(Böyük qardaşları: **Django** — hər şey daxil; **FastAPI** — API-lər üçün çox sürətli. Flask-ı öyrənsən, onlar asan gələcək.)

## ⚙️ Qurulum

```bash
mkdir menim_saytim && cd menim_saytim
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install flask
```

## 🌱 İlk server — `app.py`

```python
from flask import Flask

app = Flask(__name__)          # restoranı açdıq

@app.route("/")                # kimsə "/" ünvanına gələndə...
def ana_sehife():              # ...bu funksiya işləsin
    return "<h1>Salam! Bu mənim serverimdir 🎉</h1>"

@app.route("/haqqimda")
def haqqimda():
    return "Mən Python öyrənirəm."

if __name__ == "__main__":
    app.run(debug=True)        # debug=True: kodu dəyişəndə özü yenilənir
```

```bash
python app.py
```
Brauzerdə aç: **http://127.0.0.1:5000** 🎉

- `127.0.0.1` (və ya `localhost`) = **"bu kompüterin özü"**. Sayt hələ yalnız səndə işləyir.
- `5000` = **port** — binadakı mənzil nömrəsi. Bir kompüterdə çox server ola bilər, hər biri öz portunda.

## 🛣️ Route (yol) — hansı qapı hansı otağa

`@app.route(...)` — **dekorator**. Funksiyanın üstünə "bu funksiya bu ünvana cavabdehdir" yarlığı yapışdırır.

### Dinamik yollar
```python
@app.route("/salam/<ad>")
def salam(ad):
    return f"Salam, {ad}!"
# /salam/Aysel → "Salam, Aysel!"

@app.route("/mehsul/<int:id>")
def mehsul(id):
    return f"Məhsul nömrəsi: {id}"
```

### Query parametrləri (`?` sonrası)
```python
from flask import request

@app.route("/axtar")
def axtar():
    soz = request.args.get("q", "")
    return f"Sən '{soz}' axtardın"
# /axtar?q=pişik
```

## 🖼️ Şablonlar (templates) — HTML-i ayrıca saxlamaq

HTML-i Python-un içində yazmaq çətindir. Ona görə **`templates/`** qovluğu yaradırıq:

```
menim_saytim/
├── app.py
├── templates/
│   ├── base.html
│   └── index.html
└── static/
    ├── style.css
    └── app.js
```

`templates/base.html` — **ana qəlib** (bütün səhifələr üçün ortaq hissə):
```html
<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Saytım{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('ana_sehife') }}">Ana səhifə</a>
        <a href="{{ url_for('haqqimda') }}">Haqqımda</a>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

`templates/index.html` — ana qəlibi **miras alır** və yalnız öz hissəsini doldurur:
```html
{% extends "base.html" %}
{% block title %}Ana səhifə{% endblock %}
{% block content %}
    <h1>Salam, {{ ad }}!</h1>
    <ul>
    {% for h in hobbiler %}
        <li>{{ h }}</li>
    {% endfor %}
    </ul>
{% endblock %}
```

`app.py`:
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ana_sehife():
    return render_template("index.html", ad="Aysel", hobbiler=["rəsm", "kod"])
```

### Jinja dili (şablonun içindəki sehr)
- `{{ dəyişən }}` — dəyəri göstər
- `{% for %} ... {% endfor %}` — döngü
- `{% if %} ... {% endif %}` — şərt
- `{% extends %}` / `{% block %}` — miras

## 🎯 Tapşırıq

2-ci və 3-cü gündə qurduğun 3 səhifəli saytı **Flask-a köçür**:
1. `base.html` yarat, menyu yalnız orada olsun.
2. Hər səhifə `{% extends "base.html" %}` etsin.
3. CSS `static/` qovluğuna köçsün.
4. Hobbilər siyahısı HTML-də yox, **Python-da list** kimi olsun və şablona ötürülsün.
5. `/salam/<ad>` yolu düzəlt.

## ✅ Gün sonu yoxlama

1. `@app.route("/")` nə edir?
2. `localhost:5000` — burada 5000 nədir?
3. `templates` və `static` qovluqlarında nə saxlanılır?
4. `{{ }}` və `{% %}` fərqi?
