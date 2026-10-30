// Gün 10: frontend səhifəni yeniləmədən backend API-dən məlumat alır
const duyme = document.querySelector("#yukle");
const siyahi = document.querySelector("#api-siyahi");

async function yazilariGetir() {
    const cavab = await fetch("/api/yazilar");
    const yazilar = await cavab.json();
    siyahi.innerHTML = "";
    for (const y of yazilar) {
        const li = document.createElement("li");
        li.textContent = `${y.basliq} — ${y.muellif}`;   // textContent: XSS-dən qorunma
        siyahi.appendChild(li);
    }
    if (yazilar.length === 0) siyahi.textContent = "API boş siyahı qaytardı.";
}

duyme.addEventListener("click", yazilariGetir);
