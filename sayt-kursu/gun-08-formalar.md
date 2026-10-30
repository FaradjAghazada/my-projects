# Gün 8 — Formalar, POST, yönləndirmə

**Məqsəd:** istifadəçidən məlumat qəbul etmək, yoxlamaq və cavab vermək.

## 1. GET və POST bir route-da

```python
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "dev"     # flash üçün lazımdır (12-ci gündə ətraflı)

@app.route("/yeni", methods=["GET", "POST"])
def yeni():
    if request.method == "POST":
        basliq = request.form.get("basliq", "").strip()
        metn = request.form.get("metn", "").strip()

        if not basliq:
            flash("Başlıq boş ola bilməz", "xeta")
            return render_template("yeni.html", basliq=basliq, metn=metn), 400

        qeyd_elave_et(qeydler, basliq, metn)
        flash("Qeyd əlavə olundu", "ugur")
        return redirect(url_for("index"))

    return render_template("yeni.html")
```

Ardıcıllıq: **oxu → yoxla → saxla → yönləndir**.

## 2. Məlumat haradan oxunur

| Mənbə | Kod |
|---|---|
| Forma (POST) | `request.form.get("ad")` |
| URL parametri `?q=` | `request.args.get("q")` |
| URL yolu `/qeyd/5` | funksiya parametri |
| JSON body | `request.get_json()` (10-cu gün) |

## 3. Post → Redirect → Get

Uğurlu POST-dan sonra həmişə `redirect` et. Etməsən, istifadəçi F5 basanda brauzer formanı təkrar göndərir və eyni qeyd iki dəfə yaranır.

Xəta olanda isə redirect etmə. Formanı yazılmış dəyərlərlə yenidən göstər ki, istifadəçi hər şeyi təkrar yazmasın:
```html
<input name="basliq" value="{{ basliq or '' }}">
<textarea name="metn">{{ metn or '' }}</textarea>
```

## 4. Flash mesajları

`base.html`-də, `<main>`-in əvvəlində:
```html
{% for kat, m in get_flashed_messages(with_categories=true) %}
    <div class="bildiris {{ kat }}">{{ m }}</div>
{% endfor %}
```

## 5. Yoxlama (validation) qaydaları

- Server tərəfində **həmişə** yoxla. HTML-dəki `required` və JS yoxlaması asanlıqla keçilir. Onlar yalnız istifadəçi rahatlığı üçündür.
- `.strip()` ilə boşluqları sil, uzunluğu yoxla.
- Məlumatı dəyişən əməliyyatlar (yaratmaq, silmək) yalnız **POST** ilə olsun, GET linki ilə yox:
```html
<form action="{{ url_for('sil', id=q.id) }}" method="POST">
    <button>Sil</button>
</form>
```

## Tapşırıq

1. `/yeni`: forma işləsin, boş başlıq xəta versin, uğurlu olanda ana səhifəyə yönləndirsin.
2. `/qeyd/<id>/sil` (yalnız POST): qeydi silsin və yönləndirsin.
3. `/elaqe`: ad və mesaj tələb olunsun. Hələlik mesajı `print()` ilə terminala yaz (11-ci gündə Telegram-a gedəcək).
4. Flash mesajları `base.html`-də göstərilsin, uğur yaşıl, xəta qırmızı.
5. Serveri yenidən başlat. Qeydlər itəcək, çünki siyahı yaddaşdadır. Sabah bunu həll edəcəksən.

## Yoxlama

1. Uğurlu POST-dan sonra niyə `redirect` edirik?
2. HTML-də `required` varsa, server tərəfində yoxlama yenə də niyə lazımdır?
3. Silmə əməliyyatı niyə GET linki ilə edilmir?
