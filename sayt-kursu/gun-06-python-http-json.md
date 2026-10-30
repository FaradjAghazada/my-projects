# Gün 6 — Python davamı, HTTP və JSON 📨

## 1️⃣ Modullar və pip — hazır alətlər qutusu

Hər şeyi sıfırdan yazmırıq. Başqalarının yazdığı **paketləri** istifadə edirik.

```python
import random
import datetime

print(random.randint(1, 6))           # zər at 🎲
print(datetime.date.today())
```

Kənar paketlər `pip` ilə yüklənir. Amma əvvəlcə **virtual mühit (venv)** yarat.

### 🧺 venv nədir?
Hər layihənin **öz oyuncaq səbəti**. Bir layihənin paketləri digərinə qarışmır.

```bash
python -m venv venv                 # səbət yarat
# aktivləşdir:
venv\Scripts\activate               # Windows
source venv/bin/activate            # Mac/Linux
# Terminalda (venv) yazısı görünəcək ✅

pip install requests                # paket yüklə
pip freeze > requirements.txt       # səbətdə nə var — siyahını yaz
pip install -r requirements.txt     # başqa kompüterdə hamısını birdən yüklə
```
`requirements.txt` hosting-ə yükləyəndə **mütləq** lazım olacaq (13-cü gün).

## 2️⃣ Xətaları tutmaq (try/except)

```python
try:
    reqem = int(input("Rəqəm yaz: "))
    print(10 / reqem)
except ValueError:
    print("Bu rəqəm deyil!")
except ZeroDivisionError:
    print("Sıfıra bölmək olmaz!")
```

## 3️⃣ Fayllar

```python
with open("qeyd.txt", "w", encoding="utf-8") as f:
    f.write("Salam!\n")

with open("qeyd.txt", encoding="utf-8") as f:
    print(f.read())
```

## 4️⃣ HTTP — ofisiantın dili 🧑‍🍳

Hər sorğunun **metodu** var — nə istədiyini deyir:

| Metod | Mənası | Restoranda |
|---|---|---|
| `GET` | Ver, baxım | "Menyunu göstər" |
| `POST` | Yeni şey yarat | "Yeni sifariş verirəm" |
| `PUT/PATCH` | Dəyiş | "Sifarişimi dəyiş" |
| `DELETE` | Sil | "Sifarişi ləğv et" |

Sorğunun hissələri:
- **URL** — hara?
- **Method** — nə etməli?
- **Headers** — əlavə qeydlər (məs. "mən JSON göndərirəm", "bu mənim açarımdır")
- **Body** — göndərilən məlumat (POST-da)

Cavabın hissələri: **status kodu** (200, 404…), **headers**, **body**.

## 5️⃣ JSON — hamının başa düşdüyü dil 🌍

Python Python dilində, JavaScript JS dilində danışır. Bəs bir-birini necə başa düşürlər?
**JSON** — onların ortaq dilidir. Görünüşü Python dict-ə çox bənzəyir:

```json
{
  "ad": "Aysel",
  "yas": 10,
  "telebedir": true,
  "hobbiler": ["rəsm", "üzgüçülük"]
}
```

```python
import json

data = {"ad": "Aysel", "yas": 10}
metn = json.dumps(data, ensure_ascii=False)   # dict → JSON mətni
geri = json.loads(metn)                       # JSON mətni → dict
```

## 6️⃣ İlk API sorğun! 🎉

API = **başqa proqramın menyusu**. Ondan sorğu göndərirsən, JSON qaytarır.

```python
import requests

# Bakının havası (pulsuz API, açar lazım deyil)
url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 40.41, "longitude": 49.87, "current_weather": "true"}

cavab = requests.get(url, params=params, timeout=10)
print(cavab.status_code)                 # 200
data = cavab.json()                      # JSON → dict
print(data["current_weather"]["temperature"], "°C")
```

Bu URL-i brauzerə də yapışdır, JSON-u öz gözünlə gör:
`https://api.open-meteo.com/v1/forecast?latitude=40.41&longitude=49.87&current_weather=true`

## 🎯 Tapşırıq

1. venv yarat, `requests` yüklə, `requirements.txt` yarat.
2. Hava proqramı: istifadəçidən şəhər seçimi soruş (Bakı, Gəncə, Sumqayıt — koordinatları özün tap) və temperaturu göstər.
3. `https://jsonplaceholder.typicode.com/posts` — saxta yazılar API-sidir. İlk 5 yazının başlığını (`title`) çap et.
4. Bonus: `requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "Salam"})` göndər, cavaba bax.

## ✅ Gün sonu yoxlama

1. venv nə üçündür?
2. GET ilə POST fərqi?
3. JSON nədir və niyə lazımdır?
4. `cavab.json()` nə qaytarır?
