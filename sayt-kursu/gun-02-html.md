# Gün 2 — HTML

**Məqsəd:** saytın səhifələrinin strukturunu yazmaq.

HTML məzmunu və onun rolunu təsvir edir: bu başlıqdır, bu linkdir, bu formadır. Görünüş CSS-in işidir.

## 1. Səhifənin skeleti

`qeydler/index.html`:
```html
<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Qeydlər</title>
</head>
<body>
    <h1>Qeydlər</h1>
    <p>Mənim ilk saytım.</p>
</body>
</html>
```
- `<head>` brauzer üçündür, görünmür. `charset="UTF-8"` olmasa `ə, ş, ğ` pozulur. `viewport` olmasa telefonda kiçik görünür.
- `<body>` görünən hissədir.

Aç: VS Code-da fayla sağ klik → **Open with Live Server**.

## 2. Lazım olan teqlər

```html
<h1>...</h1> <h2>...</h2>            <!-- başlıqlar -->
<p>Paraqraf</p>
<a href="/haqqinda.html">Link</a>
<img src="sekil.jpg" alt="Şəklin təsviri">
<ul><li>Siyahı elementi</li></ul>
<button>Düymə</button>
<div>Qrup (blok)</div>
<span>Qrup (sətir içində)</span>

<header> <nav> <main> <article> <footer>   <!-- səhifə hissələri -->
```

Atributlar:
- `id="..."`: unikal ad, səhifədə yalnız bir dəfə.
- `class="..."`: qrup adı, çox elementdə ola bilər. CSS və JS ilə bu adlara müraciət olunur.

## 3. Formalar (backend üçün ən vacib hissə)

```html
<form action="/elaqe" method="POST">
    <label for="ad">Ad</label>
    <input id="ad" name="ad" type="text" required>

    <label for="email">Email</label>
    <input id="email" name="email" type="email">

    <label for="mesaj">Mesaj</label>
    <textarea id="mesaj" name="mesaj"></textarea>

    <button type="submit">Göndər</button>
</form>
```
- `action`: məlumat hansı ünvana göndərilir.
- `method`: `GET` və ya `POST` (6-cı gün).
- `name`: serverin məlumatı tanıdığı açar. `name` olmayan sahə göndərilmir.

## Tapşırıq: saytın səhifələri

`qeydler/` qovluğunda 3 fayl:
1. `index.html`: `<header>` içində `<nav>` (3 səhifəyə link), `<main>` içində 3 qeyd. Hər qeyd `<article class="kart">` içində başlıq və mətndir.
2. `yeni.html`: yeni qeyd forması (`basliq` input, `metn` textarea, düymə).
3. `elaqe.html`: əlaqə forması (`ad`, `mesaj`).

Menyu hər 3 səhifədə eyni olsun. Hələ dizayn etmə.

## Yoxlama

1. `id` ilə `class` arasındakı fərq nədir?
2. Formada `name` atributu niyə vacibdir?
3. `<head>` içindəki iki `meta` teqi nə edir?
