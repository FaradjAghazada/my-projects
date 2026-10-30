# Gün 14 — DNS, domen, HTTPS + yekun 🏁

## 📒 Nağıl: telefon kitabçası

Saytın artıq var: `menim-saytim.onrender.com`. Amma uzun və çirkin adıdır.
Biz istəyirik: **`menimsaytim.az`**.

- **Domen** = ad. Onu **qeydiyyatçıdan (registrar)** illik icarəyə alırsan.
  - `.com`, `.net`, `.dev` — Namecheap, Cloudflare Registrar, Porkbun (~10–15$/il)
  - `.az` — Azərbaycan qeydiyyatçıları (məs. `whois.az`-da göstərilən akkreditə olunmuş qeydiyyatçılar, hostinq şirkətləri)
- **DNS** = telefon kitabçası, deyir: *"menimsaytim.az → filan serverdədir"*.

## 🗂️ DNS qeydləri (records) — kitabçadakı sətirlər

| Növ | Nə deyir | Nümunə |
|---|---|---|
| **A** | Ad → IPv4 ünvanı | `menimsaytim.az → 216.24.57.1` |
| **AAAA** | Ad → IPv6 ünvanı | `→ 2001:db8::1` |
| **CNAME** | Ad → başqa ad (ləqəb) | `www.menimsaytim.az → menim-saytim.onrender.com` |
| **MX** | Bu domenin **poçtu** hara getsin | `→ mail.google.com` |
| **TXT** | Qeyd / sübut ("bu domen mənimdir") | `google-site-verification=...` |
| **NS** | Bu domenin kitabçasını **kim** idarə edir | `→ ns1.cloudflare.com` |

- **`@`** = domenin özü (`menimsaytim.az`)
- **`www`** = subdomen (`www.menimsaytim.az`). Subdomen istədiyin qədər: `api.`, `blog.`...
- **TTL** = "bu məlumatı neçə saniyə yadda saxla". Dəyişiklik dünyaya yayılması bir neçə dəqiqədən 24-48 saata qədər çəkə bilər (adətən tez olur).

## 🔗 Domeni Render-ə bağlamaq (addım-addım)

1. Domen al (məs. Namecheap və ya Cloudflare-dən).
2. Render → sənin Web Service → **Settings → Custom Domains → Add**:
   `menimsaytim.az` və `www.menimsaytim.az` əlavə et.
3. Render sənə hansı DNS qeydlərini yazmağı göstərəcək, təxminən:
   ```
   Type    Name   Value
   A       @      <Render-in göstərdiyi IP>
   CNAME   www    menim-saytim.onrender.com
   ```
4. Domeni aldığın saytın **DNS Management** panelinə gir və bu qeydləri əlavə et.
5. Render-də **Verify** düyməsi → yaşıl ✅ olana qədər gözlə.
6. Yoxla:
   ```bash
   nslookup menimsaytim.az
   ```
   və ya https://dnschecker.org — dünyanın hər yerindən yoxlayır.

## ☁️ Cloudflare (tövsiyə olunur, pulsuz)

Domenin **NS** qeydlərini Cloudflare-ə yönəltsən, əlavə alırsan: sürətli DNS, keş, DDoS qoruması.
1. cloudflare.com → Add site → domenini yaz → Free plan.
2. Cloudflare iki NS göstərəcək (`xxx.ns.cloudflare.com`) → onları domen qeydiyyatçında **Nameservers** bölməsinə yaz.
3. Bundan sonra bütün DNS qeydlərini **Cloudflare panelində** idarə edirsən.
4. Render ilə istifadə edəndə: SSL/TLS rejimini **Full** seç.

## 🔒 HTTPS — zərfli məktub

- **HTTP** = açıqca (postcard) — yolda hamı oxuya bilər.
- **HTTPS** = möhürlü zərf. Parollar, kartlar təhlükəsiz gedir. Brauzerdə 🔒 işarəsi.
- Bunun üçün **SSL/TLS sertifikatı** lazımdır. Yaxşı xəbər: **Render, Netlify, Vercel, Cloudflare bunu avtomatik və pulsuz edir** (Let's Encrypt ilə). Sən heç nə etmirsən!
- VPS-də isə özün `certbot` ilə qurursan (sonrakı səviyyə).

## 📧 Bonus: domen adınla email
`info@menimsaytim.az` istəyirsənsə: Zoho Mail (pulsuz plan), Google Workspace və ya Cloudflare Email Routing (gələn məktubları Gmail-ə yönəldir, pulsuz) — hamısı sənə **MX** və **TXT** qeydləri verəcək, DNS-ə əlavə edirsən.

---

# 🏆 YEKUN İMTAHAN — Mənsiz sayt qur!

Bu gün sıfırdan, **bu fayllara baxmadan** (yalnız ilişəndə) yeni bir sayt qur. Mövzunu özün seç:
"Kitab tövsiyələri", "Resept saytı", "Kiçik mağaza vitrini", "Portfolio + bloq".

### Tələblər siyahısı
- [ ] venv + `requirements.txt` + `.gitignore`
- [ ] Flask, `base.html` + ən az 4 səhifə, responsiv CSS
- [ ] SQLAlchemy ilə ən az 2 cədvəl (əlaqəli)
- [ ] Qeydiyyat / login / çıxış (hash-lənmiş parol)
- [ ] CRUD: yarat, oxu, dəyiş, sil
- [ ] JSON API (`/api/...`) + səhifədə `fetch` ilə istifadə
- [ ] Ən az 1 kənar inteqrasiya (hava, Telegram, email...)
- [ ] Bütün açarlar `.env`-də / Environment Variables-da
- [ ] GitHub-da
- [ ] Render-də işləyir (`debug` söndürülüb, gunicorn)
- [ ] Öz domenində HTTPS ilə açılır 🔒

Hamısı ✅-dirsə — **təbrik edirəm, sən artıq veb proqramçısan!** 🎉

İlişsən: [`layihe/`](layihe/) qovluğunda bütün bunları edən hazır nümunə var.

---

## 🧭 14 gündən sonra nə öyrənməli?

1. **FastAPI** — müasir, çox sürətli API framework (Flask bilən 1-2 günə öyrənir).
2. **Django** — böyük layihələr üçün "hər şey daxil" framework (admin panel hazır gəlir!).
3. **Testlər** — `pytest` ilə kodunu avtomatik yoxlamaq.
4. **Docker** — layihəni "konteynerə" qablaşdırmaq.
5. **Linux + VPS + Nginx** — serveri tam özün idarə etmək.
6. **Frontend framework** — React və ya Vue (daha mürəkkəb interfeyslər üçün).
7. **Alembic / Flask-Migrate** — baza strukturunu itkisiz dəyişmək.

### 📚 Pulsuz mənbələr
- Flask rəsmi sənədləri: https://flask.palletsprojects.com
- MDN (HTML/CSS/JS üçün ən yaxşı): https://developer.mozilla.org
- Python rəsmi tutorial: https://docs.python.org/3/tutorial
- Miguel Grinberg — *Flask Mega-Tutorial* (Flask üzrə ən məşhur dərslik)
- freeCodeCamp: https://www.freecodecamp.org

## ✅ Gün sonu yoxlama

1. A və CNAME qeydinin fərqi?
2. MX qeydi nə üçündür?
3. HTTPS sertifikatını Render-də kim qurur?
4. Saytın `menimsaytim.az`-da açılmırsa, nəyi yoxlayacaqsan? (ipucu: `nslookup`, DNS qeydləri, TTL, Render Verify)
