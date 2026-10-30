# 🚀 14 günə sıfırdan sayt qurmaq

> Bu kurs 10 yaşlı uşağa danışılan kimi yazılıb. Qorxma, hər şey sadə dillə izah olunub.
> 14 gün sonra sən **təkbaşına** sayt qurub, onu internetə çıxarıb, öz domeninə bağlaya biləcəksən.

## 🧠 Əvvəlcə böyük şəkil: sayt nədir?

Saytı **restoran** kimi təsəvvür et:

| Restoranda | Saytda | Nə ilə edirik |
|---|---|---|
| Zal, masalar, menyu (müştəri görür) | **Frontend** | HTML, CSS, JavaScript |
| Mətbəx, aşpaz (müştəri görmür) | **Backend** | Python (Flask) |
| Anbar, soyuducu | **Verilənlər bazası** | SQLite / PostgreSQL |
| Ofisiant (sifarişi mətbəxə aparır) | **API** | HTTP + JSON |
| Restoranın binası | **Hosting (server)** | Render / PythonAnywhere |
| Restoranın ünvanı | **Domen + DNS** | `menimsaytim.az` |
| Kənardan çörək, ət gətirən firmalar | **İnteqrasiyalar** | Hava API-si, Telegram və s. |

Bu cədvəli yadda saxla — 14 gün boyunca hər şey bura bağlanacaq.

## 📅 Plan (gündə 3–5 saat)

| Gün | Mövzu | Nəticə |
|---|---|---|
| [1](gun-01-internet-ve-aletler.md) | İnternet necə işləyir + alətlər | Kompüterin hazırdır |
| [2](gun-02-html.md) | HTML — saytın skeleti | İlk səhifən |
| [3](gun-03-css.md) | CSS — saytın paltarı | Gözəl səhifə |
| [4](gun-04-javascript.md) | JavaScript — saytın əzələləri | Düymə işləyir |
| [5](gun-05-python-esaslar.md) | Python əsasları | Proqram yazırsan |
| [6](gun-06-python-http-json.md) | Python davamı, HTTP, JSON | Ofisiantın dilini bilirsən |
| [7](gun-07-flask-ilk-server.md) | Flask — ilk backend | Öz serverin |
| [8](gun-08-formalar.md) | Formalar, GET/POST, şablonlar | Sayt istifadəçini dinləyir |
| [9](gun-09-verilenler-bazasi.md) | Verilənlər bazası | Sayt yadda saxlayır |
| [10](gun-10-oz-api.md) | Öz API-ni yaratmaq + `fetch` | Frontend ↔ Backend danışır |
| [11](gun-11-inteqrasiyalar.md) | Kənar API-lər, inteqrasiyalar, gizli açarlar | Hava, Telegram |
| [12](gun-12-login-tehlukesizlik.md) | Qeydiyyat, login, təhlükəsizlik | İstifadəçi hesabları |
| [13](gun-13-git-hosting.md) | Git, GitHub, Hosting | Sayt internetdədir |
| [14](gun-14-dns-domen-https.md) | DNS, domen, HTTPS + yekun | `menimsaytim.az` işləyir 🎉 |

## 🏗️ Yekun layihə

[`layihe/`](layihe/) qovluğunda kursun sonunda quracağın **hazır işlək sayt** var:
qeydlər/bloq saytı — qeydiyyat, login, yazılar, öz API-si, hava inteqrasiyası, Telegram bildirişi.

⚠️ **Qayda:** əvvəlcə özün yaz, ilişəndə bax. Kopyalamaq öyrətmir, **yazmaq** öyrədir.

## ✅ Uğurun 5 qızıl qaydası

1. **Hər kodu əlinlə yaz** — copy-paste etmə.
2. **Xəta (error) dostundur.** Qırmızı yazını oxu — o sənə nəyin səhv olduğunu deyir.
3. **Google + rəsmi sənədlər.** Proqramçılar hər gün axtarır. Bu normaldır.
4. **Hər gün kiçik bir şey qur.** Oxumaq 20%, etmək 80%.
5. **Gün sonu yoxlama suallarına cavab ver.** Cavab verə bilmirsənsə — həmin günü təkrarla.
