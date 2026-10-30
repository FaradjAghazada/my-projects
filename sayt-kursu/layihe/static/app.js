const qeydlerEl = document.querySelector("#qeydler");
const suretli = document.querySelector("#suretli");

// Sürətli qeyd: fetch ilə POST, səhifə yenilənmir
if (suretli) {
    suretli.addEventListener("submit", async (e) => {
        e.preventDefault();
        const input = document.querySelector("#suretli-basliq");
        const xeta = document.querySelector("#suretli-xeta");
        const r = await fetch("/api/qeydler", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ basliq: input.value }),
        });
        const data = await r.json();
        if (!r.ok) {
            xeta.textContent = data.xeta;
            return;
        }
        xeta.textContent = "";
        input.value = "";

        const kart = document.createElement("article");
        kart.className = "kart";
        kart.dataset.id = data.id;
        const h2 = document.createElement("h2");
        const a = document.createElement("a");
        a.href = `/qeyd/${data.id}`;
        a.textContent = data.basliq;
        h2.appendChild(a);
        const sil = document.createElement("button");
        sil.className = "sil link-qirmizi";
        sil.textContent = "Sil";
        kart.append(h2, sil);
        qeydlerEl.prepend(kart);
    });
}

// Sil: fetch ilə DELETE, kartı DOM-dan çıxar
qeydlerEl.addEventListener("click", async (e) => {
    if (!e.target.classList.contains("sil")) return;
    const kart = e.target.closest(".kart");
    if (!confirm("Silinsin?")) return;
    const r = await fetch(`/api/qeydler/${kart.dataset.id}`, { method: "DELETE" });
    if (r.ok) kart.remove();
});
