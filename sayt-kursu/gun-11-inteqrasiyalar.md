# Gün 11 — İnteqrasiyalar və gizli açarlar

**Məqsəd:** kənar servisi sayta qoşmaq və açarları təhlükəsiz saxlamaq. İstənilən yeni API-ni təkbaşına qoşmağın metodu.

İnteqrasiya, saytının başqa servisin API-sinə HTTP sorğusu göndərməsidir. Ödəniş, email, xəritə, SMS, süni intellekt: hamısı eyni qəlibdədir.

## 1. Yeni API-ni qoşmaq üçün metod

1. Rəsmi sənədlərdə **Authentication** bölməsi: açar haradan alınır və necə göndərilir (header, yoxsa URL).
2. Sənəddəki ən sadə nümunəni `curl` ilə işlət.
3. Eyni sorğunu Python `requests` ilə yaz və ayrı funksiyaya çıxar.
4. Açar `.env`-də olsun, `timeout` və `try/except` olsun.
5. Servis cavab verməsə sayt çökməsin.

## 2. Gizli açarlar: `.env`

Açarı koda yazmaq və GitHub-a yükləmək ciddi səhvdir: botlar repoları skan edib açarları dəqiqələr ərzində oğurlayır.

```bash
pip install python-dotenv && pip freeze > requirements.txt
```

`.env`:
```
SECRET_KEY=...
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
```

`.gitignore` (dərhal yarat):
```
.env
venv/
__pycache__/
*.db
```

`app.py`:
```python
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("TELEGRAM_BOT_TOKEN")
```
Hosting-də `.env` faylı olmur. Eyni dəyişənlər panelin **Environment Variables** bölməsinə yazılır (13-cü gün).

## 3. İnteqrasiya 1: hava (açarsız)

6-cı gündəki `hava_al()` funksiyasını `app.py`-yə köçür:
```python
import requests

def hava_al():
    try:
        r = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": 40.41, "longitude": 49.87, "current_weather": "true"},
            timeout=5,
        )
        r.raise_for_status()
        return r.json()["current_weather"]["temperature"]
    except (requests.RequestException, KeyError, ValueError):
        return None

@app.route("/")
def index():
    return render_template("index.html", qeydler=..., temperatur=hava_al())
```
```html
{% if temperatur is not none %}<p>Bakı: {{ temperatur }}°C</p>{% endif %}
```

## 4. İnteqrasiya 2: Telegram bildirişi

1. Telegram-da `@BotFather` → `/newbot` → **token** al.
2. Botuna istənilən mesaj yaz.
3. Brauzerdə `https://api.telegram.org/bot<TOKEN>/getUpdates` aç → `"chat":{"id":...}` sənin `chat_id`-ndir.
4. Kod:
```python
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
```

## 5. Webhook (bilməli olduğun anlayış)

Adi API-də sorğunu sən göndərirsən. **Webhook**-da isə servis hadisə baş verəndə sənin endpoint-inə özü POST göndərir (məs. "ödəniş uğurlu oldu"). Ödəniş sistemləri belə işləyir. Texniki olaraq bu, sənin yazdığın adi `@app.post("/webhook/...")` route-udur.

## Tapşırıq

1. `.env` və `.gitignore` yarat. `SECRET_KEY`-i `.env`-ə köçür.
2. Ana səhifədə hava göstərilsin.
3. Əlaqə forması mesajı Telegram-a göndərsin. Göndərilməsə istifadəçiyə xəta göstərmə, sadəcə terminala yaz.
4. İnterneti söndür və saytı aç. Sayt işləməlidir, sadəcə hava görünməməlidir.

## Yoxlama

1. API açarını niyə koda yazmırıq və hosting-də harada saxlayırıq?
2. Kənar servis çökərsə saytın niyə çökməməlidir və bunu necə təmin edirsən?
3. Webhook adi API sorğusundan nə ilə fərqlənir?
