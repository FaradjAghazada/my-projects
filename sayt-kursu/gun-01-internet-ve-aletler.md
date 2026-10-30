# Gün 1 — İnternet necə işləyir, alətlər

**Məqsəd:** brauzerlə server arasında nə baş verdiyini başa düşmək və işləyən mühit qurmaq.

## 1. Saytı açanda nə baş verir

1. Brauzerə `site.az` yazırsan.
2. Brauzer **DNS**-dən soruşur: "site.az-ın IP ünvanı nədir?" DNS cavab verir: `185.12.34.56`.
3. Brauzer həmin IP-dəki **serverə** **HTTP sorğusu (request)** göndərir: `GET /`.
4. Server **cavab (response)** qaytarır: status kodu və HTML.
5. Brauzer HTML-i səhifə kimi göstərir, sonra CSS, JS və şəkilləri ayrı sorğularla yükləyir.

Bütün kurs bu sxem üzərindədir. Frontend brauzerdə işləyir, backend serverdə. DNS və hosting saytı bu ikisinin arasında əlçatan edir.

## 2. Terminlər

| Termin | Mənası |
|---|---|
| Client | Sorğu göndərən (brauzer, mobil tətbiq) |
| Server | Sorğuya cavab verən proqram/kompüter |
| IP | Serverin şəbəkə ünvanı |
| Domen | IP-nin insan üçün adı |
| DNS | Domeni IP-yə çevirən sistem |
| HTTP/HTTPS | Client və server arasındakı protokol. HTTPS şifrələnmişdir |
| Port | Bir kompüterdə hansı proqrama müraciət edildiyi (`:5000`, `:443`) |

URL-in hissələri:
```
https://site.az/yazilar?sehife=2
protokol  domen   yol    parametr
```

Status kodları: `200` uğurlu, `301/302` yönləndirmə, `400` səhv sorğu, `401/403` icazə yoxdur, `404` tapılmadı, `500` server xətası.

## 3. Quraşdır

1. **VS Code** (code.visualstudio.com). Əlavələr: `Python`, `Live Server`.
2. **Python 3.12+** (python.org). Windows-da **"Add Python to PATH"** seç.
3. **Git** (git-scm.com).
4. **GitHub** hesabı.

Yoxla (VS Code → Terminal → New Terminal):
```bash
python --version     # Mac/Linux: python3 --version
git --version
```

## 4. Lazım olan terminal əmrləri

```bash
pwd              # hansı qovluqdayam (Windows: cd)
ls               # içində nə var (Windows cmd: dir)
mkdir qeydler    # qovluq yarat
cd qeydler       # qovluğa gir
cd ..            # geri çıx
```

## Tapşırıq

1. `qeydler` qovluğunu yarat və VS Code-da aç (`File → Open Folder`). 14 gün bu qovluqda işləyəcəksən.
2. Brauzerdə istənilən saytı aç → `F12` → **Network** → səhifəni yenilə. Sorğulara, metodlarına və status kodlarına bax.
3. Terminalda `nslookup google.com` yaz və IP ünvanını tap.

## Yoxlama

1. Brauzer `site.az` yazılandan HTML görənə qədər hansı addımları keçir?
2. `404` və `500` arasındakı fərq nədir? Hansı serverin günahıdır?
3. `https://shop.az/mehsul?id=5` URL-də domen, yol və parametr hansıdır?
