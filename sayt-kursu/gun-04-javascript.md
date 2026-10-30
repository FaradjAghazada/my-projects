# Gün 4 — JavaScript: saytın əzələləri 💪

## 🤖 Nağıl

- HTML — robotun **skeleti**
- CSS — robotun **paltarı**
- **JavaScript** — robotun **əzələləri və beyni**: düyməyə basanda nəsə etsin, məlumat gətirsin.

JavaScript **brauzerdə** (istifadəçinin kompüterində) işləyir. Python isə **serverdə** işləyəcək.

## 🔗 Qoşmaq

`</body>`-dən **dərhal əvvəl**:
```html
<script src="app.js"></script>
```
Yoxlamaq üçün: `F12` → **Console**. `console.log(...)` yazdığın hər şey orada görünür.

## 📦 Əsaslar

```js
// Dəyişən — adı olan qutu
let yas = 10;              // dəyişə bilər
const ad = "Aysel";        // dəyişməz (const = sabit)

// Növlər
let reqem = 5;
let metn = "salam";
let dogru = true;
let siyahi = ["alma", "armud"];          // massiv (array)
let adam = { ad: "Aysel", yas: 10 };     // obyekt — Python-da dict olacaq

console.log(adam.ad);         // Aysel
console.log(siyahi[0]);       // alma  (sayma 0-dan başlayır!)
console.log(`Salam, ${ad}!`); // şablon mətni: `` işarəsi ilə

// Şərt
if (yas >= 18) {
    console.log("Böyüksən");
} else {
    console.log("Uşaqsan");
}

// Döngü
for (const meyve of siyahi) {
    console.log(meyve);
}

// Funksiya — təkrar istifadə olunan resept
function topla(a, b) {
    return a + b;
}
const vur = (a, b) => a * b;   // qısa yazılış (arrow function)
```

## 🖱️ DOM — səhifəni idarə etmək

**DOM** = brauzerin HTML-dən qurduğu **ağac**. JS bu ağacın budaqlarını tapıb dəyişə bilir.

```html
<h1 id="basliq">Salam</h1>
<button id="duyme">Bas</button>
<p id="sayac">0</p>
```

```js
// 1. Tap
const basliq = document.querySelector("#basliq");
const duyme  = document.querySelector("#duyme");
const sayac  = document.querySelector("#sayac");

// 2. Dəyiş
basliq.textContent = "Salam, JavaScript!";
basliq.style.color = "purple";

// 3. Hadisəyə (event) qulaq as
let say = 0;
duyme.addEventListener("click", () => {
    say = say + 1;
    sayac.textContent = say;
});
```

**Tap → Qulaq as → Dəyiş.** Frontend JS-in 80%-i budur.

## ➕ Element yaratmaq

```js
const siyahiEl = document.querySelector("#siyahi");   // <ul id="siyahi">
const yeni = document.createElement("li");
yeni.textContent = "Yeni element";
siyahiEl.appendChild(yeni);
```

## 🎯 Tapşırıq: "Görüləcək işlər" (To-Do) siyahısı

```html
<input id="is" placeholder="Nə etməliyəm?">
<button id="elave">Əlavə et</button>
<ul id="siyahi"></ul>
```
1. Düyməyə basanda input-dakı mətn siyahıya `<li>` kimi əlavə olunsun.
2. Boş mətn əlavə olunmasın (`if (metn === "") return;`).
3. Əlavə edəndən sonra input təmizlənsin (`input.value = ""`).
4. Bonus: `<li>`-yə kliklədikdə üstündən xətt çəkilsin (`li.style.textDecoration = "line-through"`).

> Bu siyahı səhifəni yeniləyəndə **itir**. Niyə? Çünki yadda saxlayan yoxdur!
> 9-cu gündə **verilənlər bazası** ilə bu problemi həll edəcəyik. 😉

## ✅ Gün sonu yoxlama

1. JavaScript harada işləyir: brauzerdə, yoxsa serverdə?
2. `let` ilə `const` fərqi?
3. Düyməyə klik hadisəsini necə tutursan?
4. DOM nədir?
