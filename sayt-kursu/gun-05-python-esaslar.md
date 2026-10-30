# Gün 5 — Python əsasları 🐍

## 👨‍🍳 Nağıl

Backend — **mətbəxdir**. Aşpazımız **Python**-dur. Bu gün aşpaza danışmağı öyrənirik.
Python ingilis dilinə ən çox bənzəyən proqramlaşdırma dilidir — ona görə başlamaq asandır.

`dersler.py` faylı yarat, kodu yaz və terminalda işə sal:
```bash
python dersler.py      # Mac/Linux: python3 dersler.py
```

## 📦 Dəyişənlər və növlər

```python
ad = "Aysel"          # str   — mətn
yas = 10              # int   — tam ədəd
boy = 1.42            # float — kəsr ədəd
telebedir = True      # bool  — True / False

print(ad, yas)
print(f"Salam, {ad}! Sənin {yas} yaşın var.")   # f-string: ən rahat yol
print(type(yas))      # <class 'int'>
```

⚠️ Python-da **boşluqlar (girinti) vacibdir!** JS-dəki `{ }` əvəzinə 4 boşluq istifadə olunur.

## 🔀 Şərtlər

```python
bal = 85
if bal >= 90:
    print("Əla")
elif bal >= 70:
    print("Yaxşı")
else:
    print("Çalışmaq lazımdır")

# and, or, not
if yas > 7 and yas < 18:
    print("Məktəblisən")
```

## 📋 Siyahı (list)

```python
meyveler = ["alma", "armud", "gilas"]
print(meyveler[0])        # alma
meyveler.append("nar")    # sona əlavə et
meyveler.remove("armud")  # sil
print(len(meyveler))      # neçə dənə? → 3
print("alma" in meyveler) # var? → True
```

## 📖 Lüğət (dict) — backend-in ən sevimli qutusu

Dict — **etiketli qutular** kimidir: hər qutunun adı (açar, key) və içi (dəyər, value) var.

```python
sagird = {
    "ad": "Aysel",
    "yas": 10,
    "hobbiler": ["rəsm", "üzgüçülük"],
}
print(sagird["ad"])              # Aysel
print(sagird.get("seher", "?"))  # açar yoxdursa xəta yox, "?" qaytarır
sagird["seher"] = "Bakı"         # yeni açar əlavə et
```
Yadda saxla: JS-dəki obyekt `{ad: "Aysel"}` ↔ Python-dakı dict `{"ad": "Aysel"}`.
Sabah görəcəksən ki, bunlar **JSON** vasitəsilə bir-birinə çevrilir.

## 🔁 Döngülər

```python
for meyve in meyveler:
    print(meyve)

for i in range(5):        # 0,1,2,3,4
    print(i)

for acar, deyer in sagird.items():
    print(acar, "→", deyer)

say = 3
while say > 0:
    print(say)
    say -= 1
print("Start! 🚀")
```

## 🧰 Funksiyalar — resept kartları

```python
def salamla(ad, dil="az"):        # dil-in standart dəyəri var
    if dil == "en":
        return f"Hello, {ad}!"
    return f"Salam, {ad}!"

print(salamla("Murad"))
print(salamla("Murad", dil="en"))
```

Backend-də **hər səhifə bir funksiya olacaq**. Ona görə funksiyaları yaxşı başa düş!

## 🎯 Tapşırıq: "Mini mağaza"

```python
mehsullar = [
    {"ad": "Qələm", "qiymet": 0.5, "say": 100},
    {"ad": "Dəftər", "qiymet": 1.2, "say": 0},
    {"ad": "Çanta", "qiymet": 25, "say": 3},
]
```
1. Bütün məhsulları belə çap et: `Qələm — 0.5 AZN (100 ədəd)`.
2. `stokda_olanlar(mehsullar)` funksiyası yaz — yalnız `say > 0` olanları qaytarsın.
3. `umumi_deyer(mehsullar)` — anbardakı bütün malların ümumi qiymətini hesablasın (`qiymet * say`).
4. Bonus: `input()` ilə istifadəçidən məhsul adı soruş və onun qiymətini göstər.

## ✅ Gün sonu yoxlama

1. list ilə dict fərqi nədir?
2. Python-da `{ }` əvəzinə nə istifadə olunur?
3. `return` nə edir?
4. `sagird["telefon"]` və `sagird.get("telefon")` fərqi nədir (açar yoxdursa)?
