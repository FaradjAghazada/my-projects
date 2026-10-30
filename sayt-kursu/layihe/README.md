# 📝 Yekun layihə: "Qeydlərim"

Kursda öyrəndiyin hər şey bir saytda. **Əvvəlcə özün yaz**, ilişəndə bura bax.

| Xüsusiyyət | Harada | Gün |
|---|---|---|
| HTML şablonlar, `base.html` mirası | `templates/` | 2, 7 |
| Responsiv CSS (flex, grid, media query) | `static/style.css` | 3 |
| JavaScript + `fetch` ilə API | `static/app.js` | 4, 10 |
| Formalar, flash, PRG | `/yeni`, `/elaqe` | 8 |
| SQLAlchemy, 2 əlaqəli cədvəl | `Istifadeci`, `Yazi` | 9 |
| JSON API | `/api/yazilar` | 10 |
| Hava + Telegram inteqrasiyası, `.env` | `hava_al()`, `telegram_gonder()` | 11 |
| Qeydiyyat, login, hash, icazə (403) | `/qeydiyyat`, `/login`, `sil()` | 12 |
| gunicorn, `DATABASE_URL` | `requirements.txt` | 13 |

## Lokalda işə salmaq

```bash
cd layihe
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env              # Windows: copy .env.example .env
python app.py
```
Aç: http://127.0.0.1:5000

## Render-ə yükləmək
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Root Directory: `sayt-kursu/layihe` (əgər bu repo-nu olduğu kimi yükləyirsənsə)
- Environment: `SECRET_KEY`, istəyə bağlı `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`, `DATABASE_URL`

## Özünü sına — təkmilləşdir
1. Yazını **redaktə etmək** səhifəsi əlavə et (UPDATE).
2. API-yə `DELETE /api/yazilar/<id>` əlavə et (yalnız müəllif).
3. Ana səhifəyə axtarış: `/?q=...`
4. Hər yazıya şərh (`Serh` modeli — üçüncü cədvəl).
