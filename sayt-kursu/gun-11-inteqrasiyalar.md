# Gün 11 — İnteqrasiyalar: başqa xidmətləri saytına qoşmaq 🧩

## 🧱 Nağıl

LEGO evi qurursan. Pəncərəni, təkəri özün düzəltmirsən — **hazır hissə** götürüb taxırsan.
**İnteqrasiya** = başqa şirkətin hazır xidmətini (API-sini) öz saytına taxmaq.

Nümunələr:
| Ehtiyac | Xidmət |
|---|---|
| Hava | Open-Meteo (pulsuz, açarsız) |
| Bildiriş göndərmək | Telegram Bot API (pulsuz) |
| Email göndərmək | Resend, SendGrid, Mailgun, Gmail SMTP |
| Ödəniş | Stripe, PayPal; Azərbaycanda bankların ödəniş şlüzləri (Kapital Bank, PASHA Bank və s.) |
| Xəritə | Google Maps, OpenStreetMap/Leaflet |
| Süni intellekt | Claude API, OpenAI API |
| Login | "Google ilə daxil ol" (OAuth) |

Hamısının işləmə prinsipi **eynidir**: sənədləri (docs) oxu → açar (API key) al → HTTP sorğusu göndər → JSON cavabı oxu.

## 🔑 API açarı və `.env` — evin açarını qapının üstündə qoyma!

Çox xidmət səndən **API key** istəyir — bu sənin pasportun və pul kisəndir.
Açarı **heç vaxt** koda yazma və GitHub-a yükləmə! Botlar GitHub-u dəqiqələr içində skan edib oğurlayır.

Həll: **mühit dəyişənləri (environment variables)** və `.env` faylı.

```bash
pip install python-dotenv
```

`.env` (layihənin kökündə):
```
TELEGRAM_BOT_TOKEN=123456:ABC-sənin-tokenin
TELEGRAM_CHAT_ID=987654321
SECRET_KEY=uzun-tesadufi-metn
```

`.gitignore` (bu faylı **mütləq** yarat):
```
.env
venv/
__pycache__/
*.db
```

Python-da:
```python
import os
from dotenv import load_dotenv

load_dotenv()                                   # .env-i oxu
token = os.environ.get("TELEGRAM_BOT_TOKEN")    # açarı götür
```
Hosting-də isə `.env` faylı olmur — açarları panelin **Environment Variables** bölməsinə yazırsan (13-cü gün).

## 🌤️ İnteqrasiya 1: Hava (açarsız)

```python
import requests

def hava_al(enlik=40.41, uzunluq=49.87):
    try:
        r = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": enlik, "longitude": uzunluq, "current_weather": "true"},
            timeout=5,
        )
        r.raise_for_status()                       # 4xx/5xx olsa xəta at
        return r.json()["current_weather"]["temperature"]
    except requests.RequestException:
        return None                                # xidmət çöksə, saytımız çökməsin!

@app.route("/")
def index():
    return render_template("index.html", temperatur=hava_al())
```
```html
{% if temperatur is not none %}<p>Bakıda indi: {{ temperatur }}°C</p>{% endif %}
```

🔑 **Qızıl qayda:** kənar xidmət **həmişə** çökə bilər. `timeout` qoy və `try/except` ilə tut.

## 📲 İnteqrasiya 2: Telegram bildirişi

Kimsə əlaqə formasını dolduranda telefonuna mesaj gəlsin!

1. Telegram-da **@BotFather**-a yaz → `/newbot` → ad ver → **token** alacaqsan.
2. Yeni botuna istənilən mesaj yaz.
3. Brauzerdə aç: `https://api.telegram.org/bot<TOKEN>/getUpdates` → cavabda `"chat":{"id": ...}` — bu sənin **chat_id**-dir.
4. Kod:

```python
def telegram_gonder(metn):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return False                              # açar yoxdursa sakitcə keç
    try:
        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": metn},
            timeout=5,
        )
        return r.ok
    except requests.RequestException:
        return False
```
Əlaqə formasının POST hissəsində: `telegram_gonder(f"📩 {ad}: {mesaj}")`.

## 📧 İnteqrasiya 3: Email (SMTP ilə, qısaca)

```python
import smtplib
from email.message import EmailMessage

def email_gonder(kime, movzu, metn):
    msg = EmailMessage()
    msg["From"] = os.environ["EMAIL_USER"]
    msg["To"] = kime
    msg["Subject"] = movzu
    msg.set_content(metn)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(os.environ["EMAIL_USER"], os.environ["EMAIL_PASSWORD"])   # Gmail-də "App Password"
        s.send_message(msg)
```
Real layihədə **Resend / SendGrid** kimi xidmətlər daha etibarlıdır (spam-a düşmür).

## 🪝 Webhook — "mənə zəng vur" xidməti

Adi API: **sən** soruşursan → "Ödəniş oldu?" "Yox." "İndi?" "Yox." 😩
**Webhook**: xidmət **özü** sənə xəbər verir → "Ödəniş oldu!" ✅
Yəni sən bir route açırsan (`POST /webhook/odenis`) və xidmət hadisə baş verəndə ora sorğu göndərir.
Ödəniş sistemləri, GitHub, Telegram botlar — hamısı webhook istifadə edir.

## 📖 Yeni API-ni necə öyrənmək (bunu təkbaşına edəcəksən)

1. Rəsmi **docs** səhifəsini tap ("X API documentation").
2. **Authentication** bölməsi: açar haradan alınır, harada göndərilir (header? URL?).
3. **Quickstart** nümunəsini curl ilə yoxla.
4. Python-da `requests` ilə təkrarla.
5. `timeout`, `try/except`, açar `.env`-də.

## 🎯 Tapşırıq

1. Saytının ana səhifəsində Bakının havasını göstər.
2. Telegram bot yarat, əlaqə formasından gələn mesajlar telefonuna gəlsin.
3. Bütün açarlar `.env`-də olsun, `.gitignore` yaradılsın.
4. İnterneti söndür və saytı aç — sayt **çökməməlidir**, sadəcə hava görünməməlidir.

## ✅ Gün sonu yoxlama

1. API açarını niyə koda yazmırıq?
2. `.gitignore` nə edir?
3. Kənar API-yə sorğuda niyə `timeout` qoyuruq?
4. Webhook adi API sorğusundan nə ilə fərqlənir?
