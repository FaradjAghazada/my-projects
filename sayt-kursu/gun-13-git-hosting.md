# Gün 13 — Git, GitHub və Hosting: saytı internetə çıxarmaq 🌍

## 1️⃣ Git — zaman maşını ⏳

Oyunda **save** edirsən ki, ölsən geri qayıdasan. **Git** kodun üçün save sistemidir.
**GitHub** — save-lərin buludda saxlandığı yer (həm də hosting-lər kodu oradan götürür).

```bash
git init                          # bu qovluqda zaman maşınını işə sal
git status                        # nə dəyişib?
git add .                         # bütün dəyişiklikləri "save qutusuna" qoy
git commit -m "Login əlavə etdim" # save et (aydın mesajla!)
git log --oneline                 # bütün save-lər
```

GitHub-a yükləmək:
1. github.com → **New repository** → ad ver (məs. `menim-saytim`) → Create.
2. Göstərilən əmrləri icra et:
```bash
git remote add origin https://github.com/ISTIFADECI/menim-saytim.git
git branch -M main
git push -u origin main
```
Sonrakı dəyişikliklər üçün: `git add . && git commit -m "..." && git push`

⚠️ Push etməzdən əvvəl yoxla: `.env` və `venv/` `.gitignore`-dadır? (`git status`-da görünməməlidir)

## 2️⃣ Hosting nədir? 🏢

İndiyə qədər sayt **sənin kompüterində** idi. Kompüteri söndürsən — sayt da sönür.
**Hosting** = heç vaxt sönməyən, internetə qoşulu başqasının kompüterini **icarəyə götürmək**.

| Növ | Nümunə | Nə vaxt |
|---|---|---|
| **Statik hosting** | GitHub Pages, Netlify, Vercel | Yalnız HTML/CSS/JS (backend yoxdur) |
| **PaaS** (hazır platforma) | **Render**, PythonAnywhere, Railway, Fly.io | Python backend — **başlanğıc üçün ən yaxşısı** |
| **VPS** (boş server) | DigitalOcean, Hetzner, AWS EC2 | Hər şeyi özün qurursan (Linux, Nginx…) — sonrakı səviyyə |

Biz **Render** istifadə edəcəyik (pulsuz plan var, GitHub-dan avtomatik yükləyir).
Alternativ: **PythonAnywhere** — Python üçün çox asan, pulsuz plan var.

## 3️⃣ Saytı hosting-ə hazırlamaq

### a) Gunicorn — əsl ofisiant
`app.run(debug=True)` — **inkişaf üçün** oyuncaq serverdir. Real trafikə dözmür.
Real serverdə **gunicorn** işlədirik:

```bash
pip install gunicorn
pip freeze > requirements.txt     # gunicorn da siyahıda olmalıdır!
```
Yoxla (Mac/Linux): `gunicorn app:app` → `app.py` faylındakı `app` obyektini işə sal.
(Windows-da gunicorn işləmir — narahat olma, Render Linux-dadır.)

### b) Konfiqurasiya mühitdən gəlsin
```python
app.secret_key = os.environ.get("SECRET_KEY", "dev")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///sayt.db")
```

### c) Debug söndürülsün
```python
if __name__ == "__main__":
    app.run(debug=True)           # bu yalnız `python app.py` ilə işləyəndə; gunicorn buna baxmır ✅
```

## 4️⃣ Render-ə yükləmək (addım-addım)

1. https://render.com → **GitHub ilə qeydiyyat**.
2. **New → Web Service** → GitHub repo-nu seç.
3. Doldur:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free
4. **Environment Variables** bölməsi → `.env`-dəki hər şeyi bura əlavə et:
   `SECRET_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` ...
5. **Create Web Service** → loqlara bax (Logs) → bir neçə dəqiqə sonra:
   **`https://menim-saytim.onrender.com`** 🎉🎉🎉

Bundan sonra hər `git push` → Render **avtomatik** yenidən yükləyir (auto-deploy).

### ⚠️ Verilənlər bazası haqqında vacib qeyd
Pulsuz hosting-lərdə disk **müvəqqətidir** — hər yenidən yükləmədə `sayt.db` silinə bilər!
Həll: Render-də **New → PostgreSQL** yarat → onun **Internal Database URL**-ini kopyala →
Web Service-in Environment-ə `DATABASE_URL` kimi əlavə et. Və:
```bash
pip install psycopg2-binary && pip freeze > requirements.txt
```
```python
url = os.environ.get("DATABASE_URL", "sqlite:///sayt.db")
url = url.replace("postgres://", "postgresql://", 1)   # köhnə formatı düzəlt
app.config["SQLALCHEMY_DATABASE_URI"] = url
```
(Alternativlər: Neon, Supabase — pulsuz PostgreSQL.)

## 5️⃣ Xəta olanda nə etməli? 🔧

1. **Logs**-a bax — cavabın 90%-i oradadır.
2. Tez-tez rast gəlinən səhvlər:
   - `ModuleNotFoundError` → paket `requirements.txt`-də yoxdur.
   - `Application failed to respond` → Start Command səhvdir (`gunicorn app:app`).
   - `KeyError: 'SECRET_KEY'` → Environment Variable əlavə etməmisən.
   - Sayt yavaş açılır → pulsuz plan istifadə olunmayanda "yatır", ilk açılış ~30-50 saniyə çəkir. Normaldır.

## 🎯 Tapşırıq

1. Layihəni GitHub-a yüklə (`.env` olmadan!).
2. Render-də Web Service yarat və sayt `onrender.com` ünvanında açılsın.
3. Environment Variables əlavə et, Telegram bildirişi hosting-dən də işləsin.
4. Kiçik dəyişiklik et → `git push` → avtomatik yenilənməni izlə.
5. Bonus: PostgreSQL qoş.

## ✅ Gün sonu yoxlama

1. `git commit` və `git push` fərqi?
2. Statik hosting ilə PaaS fərqi nədir?
3. Niyə `app.run()` yox, `gunicorn` istifadə edirik?
4. Hosting-də API açarları harada saxlanılır?
