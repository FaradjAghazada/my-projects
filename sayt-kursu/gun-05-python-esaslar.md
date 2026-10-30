# Gün 5 — Python əsasları

**Məqsəd:** backend kodu yazmaq üçün lazım olan Python: dəyişənlər, şərtlər, `list`, `dict`, döngülər, funksiyalar.

Faylı işə salmaq: `python fayl.py` (Mac/Linux: `python3 fayl.py`).

## 1. Dəyişənlər və tiplər

```python
ad = "Aysel"       # str
yas = 25           # int
qiymet = 9.99      # float
aktiv = True       # bool
yox = None         # dəyər yoxdur

print(f"{ad}, {yas} yaş")   # f-string: mətnə dəyər qoymaq
int("42"), str(42)          # tip çevirmək
```

Python-da bloklar `{}` ilə yox, **girinti (4 boşluq)** ilə ayrılır. Səhv girinti xətadır.

## 2. Şərtlər

```python
if yas >= 18 and aktiv:
    print("icazə var")
elif yas >= 14:
    print("məhdud")
else:
    print("icazə yoxdur")

if not ad:          # boş mətn, 0, None, [] → False sayılır
    print("ad boşdur")
```

## 3. list və dict

Backend-də məlumatın 90%-i bu iki strukturdadır: **dict-lərdən ibarət list**.

```python
qeydler = [
    {"id": 1, "basliq": "Alış-veriş", "metn": "Çörək, süd"},
    {"id": 2, "basliq": "İş", "metn": "Hesabat"},
]

qeydler.append({"id": 3, "basliq": "Yeni", "metn": "..."})
len(qeydler)               # 3
qeydler[0]["basliq"]       # "Alış-veriş"
qeydler[0].get("tarix")    # açar yoxdursa None (xəta vermir)
"id" in qeydler[0]         # True
```

## 4. Döngülər

```python
for q in qeydler:
    print(q["basliq"])

for i in range(3):         # 0, 1, 2
    print(i)

# List comprehension: siyahıdan yeni siyahı
basliqlar = [q["basliq"] for q in qeydler]
uzunlar   = [q for q in qeydler if len(q["metn"]) > 5]
```

## 5. Funksiyalar

```python
def qeyd_tap(qeydler, id):
    for q in qeydler:
        if q["id"] == id:
            return q
    return None

def qeyd_yarat(basliq, metn=""):     # metn-in standart dəyəri var
    return {"basliq": basliq.strip(), "metn": metn.strip()}
```

Flask-da hər səhifə bir funksiyadır. Bu bölməni yaxşı mənimsə.

## Tapşırıq: `qeydler.py`

Saytın məlumat məntiqini terminalda yaz (7-ci gündə Flask-a köçəcək):

1. Yuxarıdakı kimi `qeydler` siyahısı.
2. `qeyd_tap(qeydler, id)`: qeydi id-yə görə qaytarsın, yoxdursa `None`.
3. `qeyd_elave_et(qeydler, basliq, metn)`: yeni id ilə (`max(id) + 1`) əlavə etsin. Başlıq boşdursa əlavə etməsin və `False` qaytarsın.
4. `qeyd_sil(qeydler, id)`: qeydi silsin.
5. `axtar(qeydler, soz)`: başlıqda və ya mətndə sözü olan qeydləri qaytarsın (`soz.lower() in ...lower()`).
6. Faylın sonunda hər funksiyanı `print` ilə yoxla.

## Yoxlama

1. `qeyd["tarix"]` və `qeyd.get("tarix")` arasındakı fərq nədir (açar yoxdursa)?
2. `return` olmayan funksiya nə qaytarır?
3. `[q["id"] for q in qeydler]` nə qaytarır?
