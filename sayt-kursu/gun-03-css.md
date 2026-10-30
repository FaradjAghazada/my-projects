# Gün 3 — CSS

**Məqsəd:** saytı səliqəli və telefonda işlək etmək. Gözəl dizayn məqsəd deyil.

## 1. Qoşmaq və sintaksis

`style.css` yarat, hər HTML faylın `<head>` hissəsinə əlavə et:
```html
<link rel="stylesheet" href="style.css">
```

```css
selektor {
    xususiyyet: deyer;
}
```

Selektorlar:
```css
p { }          /* bütün <p> */
.kart { }      /* class="kart" */
#esas { }      /* id="esas" */
nav a { }      /* nav içindəki a */
a:hover { }    /* siçan üstündə olanda */
```

## 2. Qutu modeli

Hər element qutudur: `content` → `padding` (daxili boşluq) → `border` → `margin` (xarici boşluq).

```css
* { box-sizing: border-box; }   /* həmişə yaz: ölçüyə padding və border daxil olur */

.kart {
    padding: 16px;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 16px;
}
```

## 3. Düzülüş: Flexbox

Elementləri bir sırada düzmək üçün. Real saytların əksər düzülüşü bununla edilir.

```css
nav {
    display: flex;
    justify-content: space-between;  /* üfüqi düzülüş */
    align-items: center;             /* şaquli düzülüş */
    gap: 16px;                       /* aralarındakı məsafə */
}
```
- `justify-content`: `flex-start | center | flex-end | space-between`
- `flex-direction: column`: sıranı sütuna çevirir.

## 4. Responsiv dizayn

```css
@media (max-width: 700px) {
    nav { flex-direction: column; }
}
```
Yoxla: `F12` → telefon ikonu (Toggle device toolbar).

## 5. Hazır baza

Bunu götür və ehtiyac olduqca dəyiş:
```css
* { box-sizing: border-box; }
body {
    margin: 0;
    font-family: system-ui, sans-serif;
    line-height: 1.6;
    color: #222;
    background: #f5f5f7;
}
main { max-width: 900px; margin: 0 auto; padding: 16px; }
img { max-width: 100%; }
input, textarea, button { font: inherit; padding: 8px; }
button { cursor: pointer; }
```

## Tapşırıq

1. 5-ci bölmədəki bazanı `style.css`-ə əlavə et və 3 səhifəyə qoş.
2. Menyu flex ilə: sayt adı solda, linklər sağda.
3. Qeydlər kart görünüşündə olsun (`.kart`).
4. Formalar şaquli olsun: `form { display: flex; flex-direction: column; max-width: 480px; gap: 8px; }`.
5. 700px-dən dar ekranda menyu sütuna düşsün.

Bu tapşırığa 2 saatdan çox vaxt sərf etmə.

## Yoxlama

1. `padding` və `margin` arasındakı fərq nədir?
2. 3 elementi yan-yana necə düzürsən və aralarını necə bərabər paylayırsan?
3. Yalnız telefon üçün stili necə yazırsan?
