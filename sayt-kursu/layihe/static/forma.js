const metn = document.querySelector("#metn");
const sayac = document.querySelector("#sayac");

function yenile() {
    sayac.textContent = `${metn.value.length} / 500`;
}
metn.addEventListener("input", yenile);
yenile();
