# Qeydlər: yekun layihə

Kursun 14 günü ərzində qurulan saytın hazır nəticəsi. Yalnız ilişəndə bax.

## İşə salmaq

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env              # SECRET_KEY-i doldur
python app.py                     # http://127.0.0.1:5000
```
Windows-da `psycopg2-binary` yüklənməsə, onu `requirements.txt`-dən müvəqqəti sil. Lokalda SQLite işlədilir.

## Render
- Root Directory: `sayt-kursu/layihe`
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:app`
- Environment: `SECRET_KEY`, `DATABASE_URL`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`

## Hansı gün harada

| Gün | Kod |
|---|---|
| 2–3 | `templates/`, `static/style.css` |
| 4 | `static/forma.js` (sayğac) |
| 7–8 | `index`, `qeyd`, `yeni`, `elaqe` route-ları |
| 9 | `Qeyd` modeli, `redakte`, `sil`, axtarış |
| 10 | `/api/qeydler`, `static/app.js` |
| 11 | `hava_al`, `telegram_gonder`, `.env` |
| 12 | `Istifadeci`, `login`, `qeydiyyat`, `oz_qeydi` (403) |
| 13 | `gunicorn`, `DATABASE_URL`, `psycopg2-binary` |
