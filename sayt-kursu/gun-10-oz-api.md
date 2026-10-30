# Gün 10 — Öz JSON API-n + `fetch`

**Məqsəd:** HTML əvəzinə JSON qaytaran endpoint-lər yazmaq və frontend-dən səhifəni yeniləmədən onlara müraciət etmək.

İndiyə qədər server hazır HTML qaytarırdı. API isə xam məlumat (JSON) qaytarır. Onu öz JS kodun, mobil tətbiq və ya başqa servis istifadə edir.

## 1. REST qaydaları

| Metod | URL | Əməliyyat | Uğurlu status |
|---|---|---|---|
| GET | `/api/qeydler` | Siyahı | 200 |
| GET | `/api/qeydler/5` | Bir qeyd | 200 / 404 |
| POST | `/api/qeydler` | Yarat | 201 |
| PATCH | `/api/qeydler/5` | Dəyiş | 200 |
| DELETE | `/api/qeydler/5` | Sil | 204 |

URL resursu (isim), metod isə əməliyyatı bildirir. `/api/qeydSil?id=5` kimi yazma.
Xəta olanda düzgün status və JSON qaytar: `{"xeta": "..."}`, `400` (səhv məlumat), `401` (login yoxdur), `403` (icazə yoxdur), `404` (tapılmadı).

## 2. Flask-da API

```python
from flask import jsonify, request

def qeyd_json(q):
    return {"id": q.id, "basliq": q.basliq, "metn": q.metn,
            "yaradilib": q.yaradilib.isoformat()}

@app.get("/api/qeydler")
def api_siyahi():
    return jsonify([qeyd_json(q) for q in Qeyd.query.order_by(Qeyd.id.desc())])

@app.post("/api/qeydler")
def api_yarat():
    data = request.get_json(silent=True) or {}
    basliq = (data.get("basliq") or "").strip()
    if not basliq:
        return jsonify({"xeta": "basliq mütləqdir"}), 400
    q = Qeyd(basliq=basliq, metn=(data.get("metn") or "").strip())
    db.session.add(q)
    db.session.commit()
    return jsonify(qeyd_json(q)), 201

@app.delete("/api/qeydler/<int:id>")
def api_sil(id):
    db.session.delete(db.get_or_404(Qeyd, id))
    db.session.commit()
    return "", 204
```

## 3. API-ni yoxlamaq

GET üçün brauzer kifayətdir. Digər metodlar üçün `curl` istifadə et:
```bash
curl http://127.0.0.1:5000/api/qeydler
curl -X POST http://127.0.0.1:5000/api/qeydler \
     -H "Content-Type: application/json" \
     -d '{"basliq": "API-dən", "metn": "test"}'
curl -X DELETE http://127.0.0.1:5000/api/qeydler/1
```
Windows PowerShell-də `curl.exe` yaz. Daha rahat alternativ: VS Code-da **Thunder Client** əlavəsi.

## 4. Frontend-dən `fetch`

```js
async function qeydleriYukle() {
    const r = await fetch("/api/qeydler");
    const qeydler = await r.json();
    const ul = document.querySelector("#siyahi");
    ul.replaceChildren();
    for (const q of qeydler) {
        const li = document.createElement("li");
        li.textContent = q.basliq;
        ul.appendChild(li);
    }
}

async function qeydYarat(basliq, metn) {
    const r = await fetch("/api/qeydler", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ basliq, metn }),
    });
    if (!r.ok) {
        const x = await r.json();
        alert(x.xeta);
        return;
    }
    await qeydleriYukle();
}
```
`await` cavabı gözləyir, amma səhifəni dondurmur. `await` işlədilən funksiya `async` olmalıdır.

Frontend və backend eyni domendədir, ona görə CORS problemi yoxdur. Fərqli domenlər olanda `flask-cors` lazım olur.

## Tapşırıq

1. 5 endpoint-in hamısını yaz: GET siyahı, GET bir, POST, PATCH, DELETE.
2. Hər birini curl və ya Thunder Client ilə yoxla, səhv məlumatla da (boş başlıq, mövcud olmayan id).
3. Ana səhifəyə "Sürətli qeyd" forması əlavə et: `submit` zamanı `e.preventDefault()` et, `fetch` ilə POST göndər, siyahını yenilə. Səhifə yenilənməməlidir.
4. Kartlardakı "Sil" düyməsi `fetch` ilə DELETE göndərsin və kartı DOM-dan silsin.

## Yoxlama

1. HTML qaytaran route ilə API endpoint-in fərqi nədir?
2. `201`, `204`, `400`, `404` statusları nə vaxt qaytarılır?
3. `fetch`-də `headers` və `JSON.stringify` niyə lazımdır?
