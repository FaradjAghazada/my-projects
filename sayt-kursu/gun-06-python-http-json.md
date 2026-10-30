# Gün 6 — venv, xətalar, HTTP, JSON

**Məqsəd:** paket idarəetməsi və HTTP/JSON-u başa düşmək. Sabahdan backend yazacaqsan və hər şey bunun üzərində qurulub.

## 1. Virtual mühit və paketlər

Hər layihənin öz paket mühiti olur, layihələr bir-birinə qarışmır.

```bash
cd qeydler
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
# terminalda (venv) görünməlidir

pip install requests
pip freeze > requirements.txt     # paketlərin siyahısı (hosting-də lazım olacaq)
pip install -r requirements.txt   # siyahıdan hamısını yüklə
```
Hər dəfə terminalı açanda venv-i aktivləşdir. VS Code-da `Python: Select Interpreter` → `venv` seç.

## 2. Xətaları tutmaq

```python
try:
    n = int(deyer)
except ValueError:
    n = 0
```
Qayda: yalnız gözlədiyin xətanı tut (`ValueError`, `requests.RequestException`). Boş `except:` yazma, çünki səhvləri gizlədir.

## 3. HTTP

Sorğu bunlardan ibarətdir: **metod + URL + headers + body**. Cavab isə: **status kodu + headers + body**.

| Metod | Mənası | Nümunə |
|---|---|---|
| GET | Oxu | Qeydlər siyahısını al |
| POST | Yarat | Yeni qeyd göndər |
| PUT/PATCH | Dəyiş | Qeydi redaktə et |
| DELETE | Sil | Qeydi sil |

- GET məlumatı URL-də göndərir (`?q=...`). Brauzerdə linkə keçmək GET-dir.
- POST məlumatı body-də göndərir. Forma göndərmək POST-dur.
- **Headers**: əlavə məlumat. Məsələn `Content-Type: application/json` (body-nin formatı), `Authorization: Bearer <açar>`.

## 4. JSON

Proqramlar arasında məlumat ötürmək üçün mətn formatı. Python `dict`/`list` ilə demək olar eynidir:

```json
{"id": 1, "basliq": "Alış-veriş", "aktiv": true, "teqler": ["ev"]}
```
Python-dan fərqi: `true/false/null` (Python-da `True/False/None`), həmişə qoşa dırnaq.

```python
import json
metn = json.dumps({"a": 1}, ensure_ascii=False)   # dict → JSON mətni
data = json.loads(metn)                          # JSON mətni → dict
```

## 5. `requests` ilə API-yə sorğu

```python
import requests

r = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": 40.41, "longitude": 49.87, "current_weather": "true"},
    timeout=5,                 # həmişə timeout qoy
)
print(r.status_code)           # 200
data = r.json()                # JSON → dict
print(data["current_weather"]["temperature"])

r = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "Test"},    # dict → JSON body + Content-Type header
    timeout=5,
)
print(r.status_code, r.json())  # 201
```

## Tapşırıq

1. `qeydler/` qovluğunda venv yarat, `requests` yüklə, `requirements.txt` yarat.
2. `hava.py`: Bakının temperaturunu qaytaran `hava_al()` funksiyası. İnternet yoxdursa və ya xəta varsa `None` qaytarsın (`try/except requests.RequestException`). 11-ci gündə sayta qoşulacaq.
3. `https://jsonplaceholder.typicode.com/posts` ünvanına GET sorğusu göndər və ilk 5 yazının `title`-ını çap et.
4. Eyni URL-i brauzerdə aç, JSON-u gör. Sonra `F12 → Network`-də sorğunun metoduna və status koduna bax.

## Yoxlama

1. venv nəyə lazımdır və `requirements.txt` nə üçündür?
2. GET və POST: məlumat hər birində harada gedir?
3. `requests.post(url, json=...)` hansı header-i avtomatik qoyur?
4. Kənar API-yə sorğuda niyə `timeout` lazımdır?
