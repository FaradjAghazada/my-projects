# Gün 2 — HTML: saytın skeleti 🦴

## 🏠 Nağıl

Ev tikirsən. Əvvəlcə **divarlar, otaqlar, qapılar** lazımdır — rəng, mebel sonra.
**HTML** = evin divarları. O deyir: *"burada başlıq var, burada şəkil, burada düymə"*.

HTML **teqlərdən** (tag) ibarətdir. Teq — qutudur. Açırsan, içinə nəsə qoyursan, bağlayırsan:

```html
<p>Salam, mən paraqrafam!</p>
 ↑ açılış                 ↑ bağlanış (/ işarəsi ilə)
```

## 📄 İlk səhifən

`sayt` qovluğunda `index.html` yarat və **əlinlə** yaz:

```html
<!DOCTYPE html>
<html lang="az">
<head>
    <!-- head: brauzer üçün gizli məlumatlar (görünmür) -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mənim ilk saytım</title>
</head>
<body>
    <!-- body: görünən hər şey -->
    <h1>Salam, dünya!</h1>
    <p>Bu mənim <strong>ilk</strong> saytımdır.</p>
</body>
</html>
```

Faylı brauzerdə aç (iki dəfə kliklə) və ya VS Code-da sağ klik → **Open with Live Server**.

> `<meta charset="UTF-8">` olmasa `ə, ş, ğ` hərfləri qarışıq görünə bilər!

## 🧱 Ən vacib teqlər

```html
<h1>Ən böyük başlıq</h1>  ... <h6>ən kiçik</h6>
<p>Paraqraf — adi mətn</p>
<a href="https://google.com">Link — başqa yerə qapı</a>
<img src="pisik.jpg" alt="Pişik şəkli">       <!-- bağlanış teqi yoxdur -->
<br>                                          <!-- yeni sətir -->

<ul>                     <!-- nöqtəli siyahı -->
    <li>Alma</li>
    <li>Armud</li>
</ul>
<ol>                     <!-- nömrəli siyahı -->
    <li>Birinci</li>
</ol>

<button>Bas məni</button>
<div>Qutu — hər şeyi qruplaşdırmaq üçün</div>
<span>Sətir içində kiçik qutu</span>
```

## 🏷️ Atributlar — teqin xüsusiyyətləri

```html
<a href="haqqimda.html" target="_blank">Haqqımda</a>
<img src="logo.png" alt="Logo" width="200">
<div id="esas" class="kart">...</div>
```
- `id` — **unikal ad** (pasport kimi, yalnız bir dənə)
- `class` — **qrup adı** (məktəb forması kimi, çoxları geyinə bilər)

## 🗂️ Semantik teqlər — otaqlara ad vermək

`div` hər şeydir, amma bunlar daha aydındır (Google da sevir):

```html
<header>Saytın başı: logo, menyu</header>
<nav>Menyu linkləri</nav>
<main>Əsas məzmun</main>
<section>Bölmə</section>
<article>Yazı / məqalə</article>
<footer>Saytın ayağı: © 2026</footer>
```

## 📝 Formalar — sayt səndən soruşur

Bu, backend günlərində çox lazım olacaq:

```html
<form action="/elaqe" method="POST">
    <label for="ad">Adın:</label>
    <input type="text" id="ad" name="ad" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email">

    <label for="mesaj">Mesaj:</label>
    <textarea id="mesaj" name="mesaj"></textarea>

    <button type="submit">Göndər</button>
</form>
```
`name` atributu çox vacibdir — backend məlumatı **bu adla** tanıyacaq.

## 🎯 Tapşırıq

3 səhifəli sayt qur:
1. `index.html` — Ana səhifə: başlıq, özün haqqında 2 paraqraf, şəkil.
2. `hobbilerim.html` — sevdiyin 5 şeyin siyahısı.
3. `elaqe.html` — əlaqə forması (ad, email, mesaj).
4. Hər səhifənin yuxarısında `<nav>` olsun və 3 səhifəyə link versin.

## ✅ Gün sonu yoxlama

1. `<head>` və `<body>` arasındakı fərq nədir?
2. `id` ilə `class` fərqi nədir?
3. Linki yeni pəncərədə necə açırsan?
4. Formada `name` atributu niyə lazımdır?
5. `alt` atributu nə üçündür? (ipucu: kor insanlar və şəkil yüklənməyəndə)
