# Gün 13 — Git, GitHub, hosting

**Məqsəd:** kodu versiyalamaq və saytı 24/7 işləyən serverə çıxarmaq.

## 1. Git

Git kodun dəyişiklik tarixçəsini saxlayır. GitHub isə bu tarixçənin onlayn nüsxəsidir. Hosting kodu GitHub-dan götürür.

```bash
git init
git status                    # nə dəyişib
git add .
git commit -m "Login əlavə olundu"
git log --oneline
```

İlk dəfə GitHub-a yükləmək (github.com → **New repository** → boş repo):
```bash
git remote add origin https://github.com/ISTIFADECI/qeydler.git
git branch -M main
git push -u origin main
```
Sonra hər dəfə: `git add . && git commit -m "..." && git push`.

Push etməzdən əvvəl `git status`-a bax: `.env`, `venv/`, `sayt.db` siyahıda olmamalıdır. Əgər `.env` artıq bir dəfə push olunubsa, içindəki açarları **dəyiş**. Faylı silmək kifayət deyil, çünki tarixçədə qalır.

## 2. Hosting növləri

| Növ | Nümunə | Nə vaxt |
|---|---|---|
| Statik | GitHub Pages, Netlify | Yalnız HTML/CSS/JS |
| PaaS | **Render**, PythonAnywhere, Railway | Backend: server idarəsi lazım deyil |
| VPS | Hetzner, DigitalOcean | Linux, Nginx və təhlükəsizliyi özün idarə edirsən |

Biz **Render** istifadə edirik: pulsuz plan var, GitHub-a `push` edəndə avtomatik yenilənir, HTTPS avtomatikdir.

## 3. Saytı hazırlamaq

**a) Production server.** `app.run()` yalnız inkişaf üçündür. Real serverdə `gunicorn` işləyir:
```bash
pip install gunicorn && pip freeze > requirements.txt
```
Start əmri: `gunicorn app:app` (`app.py` faylındakı `app` obyekti). Windows-da gunicorn işləmir, bu normaldır, çünki Render Linux-dadır.

**b) Konfiqurasiya mühitdən gəlsin:**
```python
app.secret_key = os.environ["SECRET_KEY"]

url = os.environ.get("DATABASE_URL", "sqlite:///sayt.db")
app.config["SQLALCHEMY_DATABASE_URI"] = url.replace("postgres://", "postgresql://", 1)
```

**c) Baza.** Render-in pulsuz diski hər deploy-da sıfırlanır, yəni SQLite faylı silinir. Hosting-də PostgreSQL lazımdır:
```bash
pip install psycopg2-binary && pip freeze > requirements.txt
```

## 4. Render-də deploy

1. render.com → GitHub ilə daxil ol.
2. **New → PostgreSQL** → Free → yarat → **Internal Database URL**-i kopyala.
3. **New → Web Service** → reponu seç:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Instance: Free
4. **Environment** bölməsi: `SECRET_KEY`, `DATABASE_URL` (2-ci addımdan), `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.
5. **Create** → **Logs**-a bax → sayt `https://qeydler-xxxx.onrender.com` ünvanında açılır.

Bundan sonra hər `git push` avtomatik deploy edir.

## 5. Deploy xətaları

Həmişə əvvəlcə **Logs**-a bax.

| Logda | Səbəb |
|---|---|
| `ModuleNotFoundError` | Paket `requirements.txt`-də yoxdur, `pip freeze` et |
| `KeyError: 'SECRET_KEY'` | Environment dəyişəni əlavə edilməyib |
| `Failed to find attribute 'app'` | Start Command səhvdir |
| Sayt ilk dəfə 30–50 san gec açılır | Pulsuz plan istifadə olunmayanda yatır. Xəta deyil |

## Tapşırıq

1. Layihəni GitHub-a yüklə. `.env` reponun içində olmamalıdır.
2. Render-də PostgreSQL və Web Service yarat, environment dəyişənlərini əlavə et.
3. Canlı saytda qeydiyyatdan keç, qeyd yarat, Telegram mesajını yoxla.
4. Kiçik bir dəyişiklik et → `push` → avtomatik deploy-u Logs-da izlə.

## Yoxlama

1. `commit` və `push` arasındakı fərq nədir?
2. Niyə `app.run()` yox, `gunicorn`?
3. Render-də SQLite niyə yararsızdır?
4. Deploy uğursuz oldu. İlk nəyə baxırsan?
