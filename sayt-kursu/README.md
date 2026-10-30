# 14 günə sıfırdan sayt qurmaq

**Nəticə:** 14 gün sonra Python backend-li saytı təkbaşına qurub, internetə çıxarıb, öz domeninə bağlayacaqsan.

## Metod

- **Bir layihə.** 14 gün boyunca eyni saytı qurursan: "Qeydlər" saytı. Hər gün ona bir hissə əlavə olunur. Ayrı-ayrı məşq tapşırıqları yoxdur.
- **Gündə 4 saat:** 1 saat oxu, 3 saat kod. Oxumaq yox, yazmaq öyrədir.
- **Yalnız lazım olan.** Hər mövzudan saytı qurmaq üçün lazım olan 20% verilir. Qalanını ehtiyac yaranda axtarıb tapacaqsan. Bu da öyrəniləcək bacarıqdır.
- **Gün sonu yoxlama.** Hər günün sonunda bir neçə sual var. Cavab verə bilmirsənsə, növbəti günə keçmə.

## Plan

| Gün | Mövzu | Gün sonunda saytda |
|---|---|---|
| [1](gun-01-internet-ve-aletler.md) | İnternet necə işləyir, alətlər | Alətlər quruludur |
| [2](gun-02-html.md) | HTML | Səhifələrin skeleti |
| [3](gun-03-css.md) | CSS | Dizayn, telefon versiyası |
| [4](gun-04-javascript.md) | JavaScript | İnteraktiv elementlər |
| [5](gun-05-python-esaslar.md) | Python əsasları | Məlumatlarla işləmək |
| [6](gun-06-python-http-json.md) | venv, HTTP, JSON, `requests` | Kənar API-dən məlumat |
| [7](gun-07-flask-ilk-server.md) | Flask, şablonlar | Sayt Python serverində |
| [8](gun-08-formalar.md) | Formalar, POST | Sayt məlumat qəbul edir |
| [9](gun-09-verilenler-bazasi.md) | Verilənlər bazası | Məlumat yadda qalır |
| [10](gun-10-oz-api.md) | Öz JSON API-n + `fetch` | Frontend ↔ backend |
| [11](gun-11-inteqrasiyalar.md) | İnteqrasiyalar, gizli açarlar | Hava, Telegram |
| [12](gun-12-login-tehlukesizlik.md) | Login, təhlükəsizlik | İstifadəçi hesabları |
| [13](gun-13-git-hosting.md) | Git, GitHub, hosting | Sayt internetdədir |
| [14](gun-14-dns-domen-https.md) | DNS, domen, HTTPS + imtahan | Sayt öz domenində |

Hazır nəticə [`layihe/`](layihe/) qovluğundadır. Yalnız ilişəndə bax.

## Bu 14 gündə nəyə vaxt itirmə

Başlayanların vaxtının çoxu bunlara gedir. Hamısını sonraya saxla:

- **Dil, framework və ya "ən yaxşı yol" seçimi.** Seçim edilib: Python + Flask + SQLite/PostgreSQL + Render. Müqayisə videolarına baxma.
- **Uzun video kurslar.** Videoya baxmaq öyrənmək hissi verir, amma öyrətmir. Oxu və yaz.
- **Hər şeyi əzbərləmək.** Peşəkarlar da sənədlərə baxır. Nəyin mövcud olduğunu bil, necə yazıldığını axtar.
- **CSS ilə saatlarla oynamaq.** Səliqəli olsun, kifayətdir. Dizayn sonra.
- **Redaktoru, terminalı bəzəmək.** VS Code və 2 əlavə yetər.
- **React, Docker, Kubernetes, mikroservislər, Django.** 14 gündən sonra.
- **Mükəmməl kod.** İşləyən kod > gözəl kod. Əvvəl işlət, sonra təmizlə.
- **Xətanı oxumadan Google-a qaçmaq.** Xəta mesajının son sətrini oxu. Cavab adətən oradadır.

## Xəta zamanı qayda (15 dəqiqə qaydası)

1. Xəta mesajının **son sətrini** oxu və hansı fayl, hansı sətir olduğunu tap.
2. Həmin sətrə `print()` qoy və dəyişənlərin nə olduğunu gör.
3. Xəta mətnini olduğu kimi Google-da axtar.
4. **15 dəqiqədən çox ilişdinsə**, `layihe/` qovluğuna bax və ya soruş. Saatlarla ilişib qalmaq öyrətmir.
