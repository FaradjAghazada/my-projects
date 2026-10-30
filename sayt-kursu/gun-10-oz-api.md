# Gün 10 — Öz API-ni yaratmaq + frontend ilə birləşdirmək 🔌

## 🍽️ Nağıl

İndiyə qədər serverin **hazır yemək** (HTML səhifə) verirdi.
Bəzən müştəri deyir: *"Mənə hazır yemək yox, **xammal** ver, özüm bişirəcəm."*
Bu xammal — **JSON**-dur. JSON qaytaran ünvanlar toplusu — **API**-dir.

Kimlər istifadə edir? Mobil tətbiqlər, başqa saytlar, öz JavaScript-in.

## 📐 REST — API-lərin "yaxşı tərbiyə" qaydaları

Bir resurs (məs. `yazilar`) üçün standart ünvanlar:

| Metod | URL | Nə edir | Uğurlu status |
|---|---|---|---|
| GET | `/api/yazilar` | Hamısını ver | 200 |
| GET | `/api/yazilar/5` | 5 nömrəlini ver | 200 (yoxdursa 404) |
| POST | `/api/yazilar` | Yenisini yarat | 201 Created |
| PUT | `/api/yazilar/5` | 5-i dəyiş | 200 |
| DELETE | `/api/yazilar/5` | 5-i sil | 204 No Content |

Qayda: URL-də **isim** (yazilar), metodda **fel** (GET, POST). `/api/yaziSil?id=5` kimi yazma!

## 🐍 Flask-da API

```python
from flask import jsonify, request

def yazi_dict(y):
    return {"id": y.id, "basliq": y.basliq, "metn": y.metn,
            "yaradilib": y.yaradilib.isoformat()}

@app.get("/api/yazilar")                       # @app.route(..., methods=["GET"]) qısası
def api_yazilar():
    yazilar = Yazi.query.order_by(Yazi.id.desc()).all()
    return jsonify([yazi_dict(y) for y in yazilar])

@app.get("/api/yazilar/<int:id>")
def api_yazi(id):
    return jsonify(yazi_dict(db.get_or_404(Yazi, id)))

@app.post("/api/yazilar")
def api_yazi_yarat():
    data = request.get_json(silent=True) or {}
    basliq = (data.get("basliq") or "").strip()
    metn = (data.get("metn") or "").strip()
    if not basliq or not metn:
        return jsonify({"xeta": "basliq və metn mütləqdir"}), 400   # 400 = səhv sorğu
    y = Yazi(basliq=basliq, metn=metn)
    db.session.add(y)
    db.session.commit()
    return jsonify(yazi_dict(y)), 201

@app.delete("/api/yazilar/<int:id>")
def api_yazi_sil(id):
    db.session.delete(db.get_or_404(Yazi, id))
    db.session.commit()
    return "", 204
```

## 🧪 API-ni yoxlamaq

1. **Brauzer** — yalnız GET üçün: `http://127.0.0.1:5000/api/yazilar`
2. **curl** (terminal):
   ```bash
   curl http://127.0.0.1:5000/api/yazilar
   curl -X POST http://127.0.0.1:5000/api/yazilar \
        -H "Content-Type: application/json" \
        -d '{"basliq": "API-dən", "metn": "Salam!"}'
   curl -X DELETE http://127.0.0.1:5000/api/yazilar/1
   ```
3. **Postman** və ya VS Code-da **Thunder Client** əlavəsi — düymələrlə rahat yoxlama.
4. Python `requests` ilə (6-cı gündən bildiyin kimi).

## 🌉 Frontend ↔ Backend: `fetch`

JavaScript səhifəni **yeniləmədən** serverdən məlumat ala bilir. Bu, müasir saytların sirridir.

```js
// Oxu (GET)
async function yazilariGetir() {
    const cavab = await fetch("/api/yazilar");
    const yazilar = await cavab.json();
    const ul = document.querySelector("#siyahi");
    ul.innerHTML = "";
    for (const y of yazilar) {
        const li = document.createElement("li");
        li.textContent = `${y.basliq} — ${y.metn}`;
        ul.appendChild(li);
    }
}

// Yarat (POST)
async function yaziElaveEt(basliq, metn) {
    const cavab = await fetch("/api/yazilar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ basliq, metn }),
    });
    if (!cavab.ok) {
        const xeta = await cavab.json();
        alert(xeta.xeta);
        return;
    }
    yazilariGetir();      // siyahını yenilə
}

yazilariGetir();
```

`async/await` nədir? İnternet sorğusu vaxt aparır. `await` deyir: *"cavab gələnə qədər gözlə, sonra davam et"* — amma səhifə donmur.

## 🧭 CORS — qısaca

Əgər frontend **başqa domendə** olsa (məs. `site.az` → `api.site.az`), brauzer sorğunu bloklaya bilər.
Həll: `pip install flask-cors` → `CORS(app)`. Bizim layihədə frontend və backend eyni yerdədir — problem yoxdur.

## 🎯 Tapşırıq

4-cü gündəki **To-Do** siyahısını backend-ə bağla:
1. `Is` modeli: `id`, `metn`, `bitib` (Boolean).
2. API: `GET /api/isler`, `POST /api/isler`, `PATCH /api/isler/<id>` (bitib=True/False), `DELETE /api/isler/<id>`.
3. Frontend `fetch` ilə işləsin — səhifə **heç vaxt yenilənməsin**.
4. Səhifəni yenilə — işlər **qalmalıdır** ✅. Təbriklər, bu artıq tam (full-stack) tətbiqdir! 🎉

## ✅ Gün sonu yoxlama

1. HTML səhifə qaytaran route ilə API route-un fərqi?
2. Yeni resurs yaradılanda hansı status kodu qaytarılır?
3. `fetch`-də `body: JSON.stringify(...)` niyə lazımdır?
4. `400` və `404` fərqi?
