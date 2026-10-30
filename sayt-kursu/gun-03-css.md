# Gün 3 — CSS: saytın paltarı 👗

## 🎨 Nağıl

HTML — kukladır, amma çılpaqdır. **CSS** ona paltar geyindirir: rəng, ölçü, yer, şrift.

CSS-in quruluşu: **kimə? → nə etməli?**

```css
h1 {                 /* kimə: bütün h1-lərə (selektor) */
    color: blue;     /* nə: rəngi mavi olsun (xüsusiyyət: dəyər;) */
    font-size: 40px;
}
```

## 🔗 CSS-i HTML-ə qoşmaq

`style.css` faylı yarat və HTML-in `<head>` hissəsinə əlavə et:
```html
<link rel="stylesheet" href="style.css">
```

## 🎯 Selektorlar — kimi geyindiririk?

```css
p { }              /* bütün <p>-lər */
.kart { }          /* class="kart" olan hər kəs (nöqtə ilə) */
#esas { }          /* id="esas" olan tək element (# ilə) */
nav a { }          /* nav-ın İÇİNDƏKİ a-lar */
a:hover { }        /* siçan üstünə gələndə */
```

## 📦 Qutu modeli — ən vacib anlayış

CSS-də **hər şey qutudur**. Hər qutunun 4 qatı var — hədiyyə qutusu kimi:

```
┌─────────── margin (qutu ilə qonşular arasındakı boşluq) ──────────┐
│  ┌──────── border (qutunun kağızı, çərçivəsi) ──────────────────┐  │
│  │  ┌───── padding (hədiyyə ilə kağız arasındakı yumşaq pambıq) ┐│  │
│  │  │            content (hədiyyənin özü — mətn, şəkil)          ││  │
│  │  └───────────────────────────────────────────────────────────┘│  │
│  └───────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

```css
.kart {
    padding: 20px;
    border: 2px solid #ddd;
    margin: 10px;
    border-radius: 12px;     /* künclər yumru */
}

* { box-sizing: border-box; }   /* bunu həmişə yaz — ölçüləri hesablamaq asanlaşır */
```

## 🖌️ Tez-tez lazım olanlar

```css
body {
    font-family: system-ui, Arial, sans-serif;
    background-color: #f5f5f5;
    color: #222;
    margin: 0;
    line-height: 1.6;
}
.duyme {
    background: #4f46e5;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 8px;
    cursor: pointer;          /* siçan əl şəklinə düşür */
}
.duyme:hover { background: #4338ca; }
img { max-width: 100%; }      /* şəkil heç vaxt ekrandan çıxmasın */
```

Rənglər: `red`, `#ff0000`, `rgb(255,0,0)` — hamısı eynidir.
Ölçülər: `px` (piksel), `%` (faiz), `rem` (şriftə görə).

## ↔️ Flexbox — şeyləri yan-yana düzmək

Flexbox — **qatar** kimidir: vaqonları bir sırada düzür.

```css
nav {
    display: flex;                  /* uşaqlarını sıraya düz */
    justify-content: space-between; /* üfüqi: aralarını bərabər payla */
    align-items: center;            /* şaquli: ortaya */
    gap: 16px;                      /* vaqonlar arası məsafə */
}
```
`justify-content` dəyərləri: `flex-start`, `center`, `flex-end`, `space-between`.

## ⊞ Grid — cədvəl kimi düzmək

```css
.kartlar {
    display: grid;
    grid-template-columns: repeat(3, 1fr);  /* 3 bərabər sütun */
    gap: 20px;
}
```

## 📱 Responsiv — telefonda da gözəl olsun

```css
@media (max-width: 700px) {        /* ekran 700px-dən dar olanda */
    .kartlar { grid-template-columns: 1fr; }   /* 1 sütun */
    nav { flex-direction: column; }
}
```
Yoxla: `F12` → telefon ikonu (Toggle device toolbar).

## 🎯 Tapşırıq

Dünənki 3 səhifəli sayta `style.css` qoş:
1. Yuxarıda flex ilə menyu (logo solda, linklər sağda).
2. Hobbilər səhifəsində hər hobbi bir `.kart` olsun, grid ilə 3 sütun.
3. Telefonda 1 sütuna düşsün.
4. Düymələrə `:hover` effekti ver.

💡 Hazır dizayn istəyəndə gələcəkdə **Bootstrap** və ya **Tailwind** kimi kitabxanalara bax — amma əvvəl təmiz CSS-i başa düş.

## ✅ Gün sonu yoxlama

1. `.ad` və `#ad` selektorlarının fərqi?
2. `padding` ilə `margin` fərqi nədir?
3. Üç elementi yan-yana necə düzürsən?
4. Telefon üçün xüsusi stil necə yazılır?
