# Gün 14 — DNS, domen, HTTPS + yekun imtahan

**Məqsəd:** saytı öz domeninə bağlamaq və hər şeyi sıfırdan, köməksiz təkrarlamaq.

## 1. Domen

Domen qeydiyyatçıdan (registrar) illik icarəyə alınır.
- `.com`, `.dev` və s.: Namecheap, Porkbun, Cloudflare Registrar (~10–15$/il).
- `.az`: Azərbaycanın akkreditə olunmuş qeydiyyatçıları.

## 2. DNS qeydləri

DNS domen adının hara yönləndiyini təyin edir. Qeydlər domeni aldığın panelin **DNS** bölməsində yazılır.

| Tip | Funksiya | Nümunə |
|---|---|---|
| A | Domen → IPv4 | `@ → 216.24.57.1` |
| CNAME | Domen → başqa domen | `www → qeydler-xxxx.onrender.com` |
| MX | Email hansı serverə gedir | `@ → mx.zoho.com` |
| TXT | Doğrulama, email təhlükəsizliyi | `google-site-verification=...` |
| NS | DNS-i hansı server idarə edir | `ns1.cloudflare.com` |

- `@` domenin özüdür (`site.az`), `www` isə subdomendir.
- **TTL**: qeydin keşdə saxlanma müddəti. Dəyişikliklər adətən bir neçə dəqiqəyə, bəzən 24–48 saata qədər yayılır.

## 3. Domeni Render-ə bağlamaq

1. Render → Web Service → **Settings → Custom Domains** → `site.az` və `www.site.az` əlavə et.
2. Render lazım olan qeydləri göstərir (adətən `@` üçün A, `www` üçün CNAME).
3. Domen panelində bu qeydləri əlavə et. `@` və `www` üçün köhnə, standart qeydlər varsa sil.
4. Render-də **Verify**. Uğurlu olanda HTTPS sertifikatı avtomatik verilir.
5. Yoxla:
```bash
nslookup site.az
```
və ya dnschecker.org.

## 4. HTTPS

HTTPS client ilə server arasındakı trafiki şifrələyir. Bunun üçün TLS sertifikatı lazımdır. Render, Netlify və Cloudflare sertifikatı pulsuz və avtomatik verir və yeniləyir (Let's Encrypt). VPS-də isə sertifikatı özün qurursan (`certbot`).

## 5. Sayt açılmırsa

1. `nslookup site.az`: Render-in göstərdiyi IP qayıdır? Yoxsa DNS qeydi səhvdir və ya hələ yayılmayıb.
2. Render-də domen statusu **Verified**-dir?
3. `onrender.com` ünvanı işləyir? İşləmirsə problem DNS-də yox, tətbiqdədir. Logs-a bax.

---

# Yekun imtahan

Yeni qovluqda, bu fayllara baxmadan, sıfırdan **yeni sayt** qur. Mövzunu özün seç: kitab siyahısı, reseptlər, kiçik mağaza vitrini, portfolio. Limit 1 gün. Yalnız rəsmi sənədlərdən istifadə et:
- Flask: flask.palletsprojects.com
- Flask-SQLAlchemy: flask-sqlalchemy.readthedocs.io
- HTML/CSS/JS: developer.mozilla.org

Tələblər:
- [ ] venv, `requirements.txt`, `.gitignore`, `.env`
- [ ] Flask, `base.html` + ən azı 4 səhifə, telefonda işlək
- [ ] 2 əlaqəli model (foreign key)
- [ ] Tam CRUD (yaratmaq, oxumaq, dəyişmək, silmək)
- [ ] Qeydiyyat, login, çıxış; parollar hash-lənmiş; sahiblik yoxlaması
- [ ] JSON API + səhifədə `fetch` ilə istifadə
- [ ] Ən azı 1 kənar API inteqrasiyası, açar `.env`-də
- [ ] GitHub-da, Render-də, PostgreSQL ilə
- [ ] Öz domenində, HTTPS ilə

Hamısı yerinə yetirilibsə, sən artıq köməksiz sayt qura bilirsən.

## Bundan sonra (bu ardıcıllıqla)

1. **Flask-Migrate**: baza strukturunu məlumat itirmədən dəyişmək. Real layihədə ilk ehtiyac budur.
2. **pytest**: testlər.
3. **Flask-WTF**: CSRF qoruması və formalar.
4. **FastAPI** və ya **Django**: iş elanlarında ən çox tələb olunanlar.
5. **Docker** və **VPS** (Linux, Nginx).
