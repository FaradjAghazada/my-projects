# Gün 4 — JavaScript

**Məqsəd:** brauzerdə işləyən JS əsasları: elementi tapmaq, hadisəyə reaksiya vermək, səhifəni dəyişmək. 10-cu gündə bunu serverlə əlaqə üçün işlədəcəksən.

Bu kursda backend Python-dadır. JS-dən yalnız frontend üçün lazım olan minimum öyrənilir.

## 1. Qoşmaq

`</body>`-dən əvvəl:
```html
<script src="app.js"></script>
```
Nəticəni və xətaları görmək üçün: `F12` → **Console**. Yoxlamaq üçün `console.log(x)` yaz.

## 2. Sintaksis (minimum)

```js
const ad = "Aysel";        // dəyişməyən dəyər (default olaraq bunu işlət)
let say = 0;               // dəyişən dəyər

const siyahi = ["a", "b"];               // array
const qeyd = { basliq: "X", metn: "Y" }; // obyekt
qeyd.basliq;                              // "X"
siyahi.length;                            // 2

if (say > 0) { ... } else { ... }

for (const x of siyahi) {
    console.log(x);
}

function topla(a, b) {
    return a + b;
}

`Salam, ${ad}`             // şablon mətni (backtick ilə)
```

## 3. DOM: tap → qulaq as → dəyiş

```js
const duyme = document.querySelector("#duyme");   // CSS selektoru ilə tap
const metn  = document.querySelector("#metn");

duyme.addEventListener("click", () => {           // hadisəyə qulaq as
    metn.textContent = "Düyməyə basıldı";         // dəyiş
    metn.classList.toggle("gizli");               // class əlavə et / sil
});
```

Element yaratmaq:
```js
const li = document.createElement("li");
li.textContent = "Yeni";
document.querySelector("#siyahi").appendChild(li);
```

Formada input-un dəyərini oxumaq:
```js
const deyer = document.querySelector("#basliq").value;
```

Formanın göndərilməsini dayandırmaq (10-cu gündə lazım olacaq):
```js
form.addEventListener("submit", (e) => {
    e.preventDefault();   // səhifə yenilənmir
    // ...
});
```

Qayda: istifadəçinin yazdığını səhifəyə yazmaq üçün həmişə `textContent` işlət, `innerHTML` yox. `innerHTML` zərərli kodun işə düşməsinə səbəb ola bilər (XSS, 12-ci gün).

## Tapşırıq

`yeni.html` üçün `app.js`:
1. `metn` textarea-sının altında simvol sayğacı olsun: `0 / 500`. Hər yazanda yenilənsin (`input` hadisəsi).
2. Forma göndəriləndə başlıq boşdursa `e.preventDefault()` et və qırmızı xəta mətni göstər.
3. `index.html`: hər kartda "Gizlət" düyməsi kartın mətnini gizlətsin və göstərsin.

## Yoxlama

1. `const` və `let` arasındakı fərq nədir?
2. Düyməyə klik hadisəsini necə tutursan?
3. `e.preventDefault()` nə edir?
4. Niyə `innerHTML` yox, `textContent` işlədirik?
