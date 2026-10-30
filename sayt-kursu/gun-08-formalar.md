# Gün 8 — Formalar, GET/POST, redirect, flash 📝

## 📮 Nağıl

Form — **poçt qutusudur**. İstifadəçi məktubu yazır (input), qutuya atır (Göndər),
poçtalyon (brauzer) onu **POST** ilə serverə aparır, server oxuyur və cavab verir.

## 🔁 Bir route — iki metod

```python
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "dev-ucun-gizli-acar"    # flash və session üçün lazımdır (12-ci gündə ətraflı)

@app.route("/elaqe", methods=["GET", "POST"])
def elaqe():
    if request.method == "POST":
        ad = request.form.get("ad", "").strip()
        mesaj = request.form.get("mesaj", "").strip()

        # 🛡️ Yoxlama (validation) — istifadəçiyə HEÇ VAXT kor-koranə inanma
        if not ad or not mesaj:
            flash("Ad və mesaj boş ola bilməz!", "xeta")
            return render_template("elaqe.html", ad=ad, mesaj=mesaj)

        print(f"Yeni mesaj: {ad} → {mesaj}")   # hələlik terminala yazırıq
        flash("Mesajın göndərildi, təşəkkürlər! 🙌", "ugur")
        return redirect(url_for("elaqe"))       # PRG qaydası (aşağıda)

    return render_template("elaqe.html")        # GET → sadəcə formanı göstər
```

`templates/elaqe.html`:
```html
{% extends "base.html" %}
{% block content %}
<h1>Əlaqə</h1>

{% with mesajlar = get_flashed_messages(with_categories=true) %}
  {% for kateqoriya, m in mesajlar %}
    <div class="bildiris {{ kateqoriya }}">{{ m }}</div>
  {% endfor %}
{% endwith %}

<form method="POST">
    <input name="ad" placeholder="Adın" value="{{ ad or '' }}">
    <textarea name="mesaj" placeholder="Mesajın">{{ mesaj or '' }}</textarea>
    <button type="submit">Göndər</button>
</form>
{% endblock %}
```

## 🔄 PRG qaydası: Post → Redirect → Get

Niyə POST-dan sonra `redirect` edirik?
Etməsən, istifadəçi səhifəni yeniləyəndə (F5) brauzer **formanı yenidən göndərir** — məktub iki dəfə gedir!
`redirect` deyir: *"Məktubu aldım, indi təmiz səhifəyə get."*

## 🧾 Məlumat haradan gəlir?

| Harada | Necə oxunur | Nümunə |
|---|---|---|
| URL-in `?` sonrası | `request.args.get("q")` | `/axtar?q=pişik` |
| Form (POST) | `request.form.get("ad")` | `<input name="ad">` |
| JSON body (API) | `request.get_json()` | 10-cu gün |
| URL yolu | funksiya parametri | `/mehsul/<int:id>` |
| Fayl | `request.files["sekil"]` | `<input type="file">` |

## 🛡️ Təhlükəsizlik qeydi

İstifadəçi forma `<script>alert("haha")</script>` yazsa nə olar?
Jinja `{{ }}` bunu **avtomatik zərərsizləşdirir** (escape) — mətn kimi göstərir, işə salmır. 👍
Heç vaxt `|safe` filtrini istifadəçi yazısına tətbiq etmə!

## 🎯 Tapşırıq: "Qonaq kitabı"

1. `/qonaq-kitabi` səhifəsi: ad + mesaj forması.
2. Göndərilən mesajlar Python-da qlobal `mesajlar = []` siyahısına əlavə olunsun.
3. Səhifənin aşağısında bütün mesajlar göstərilsin (ən yenisi yuxarıda).
4. Boş mesaj → qırmızı xəta, uğurlu → yaşıl bildiriş.
5. Serveri dayandırıb yenidən başlat. Mesajlar... **itdi!** 😱
   Sabah bunu verilənlər bazası ilə həll edəcəyik.

## ✅ Gün sonu yoxlama

1. `methods=["GET", "POST"]` nə üçün yazılır?
2. `request.form` və `request.args` fərqi?
3. POST-dan sonra niyə `redirect` edirik?
4. Niyə istifadəçinin göndərdiyini mütləq yoxlamalıyıq?
