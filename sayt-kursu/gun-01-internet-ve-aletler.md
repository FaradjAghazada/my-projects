# Gün 1 — İnternet necə işləyir + alətləri quraşdırmaq

## 🍕 Nağıl: pizza sifarişi

Sən telefonda `google.com` yazırsan. Nə baş verir?

1. **Brauzer** (Chrome) — bu sənsən, ac müştəri.
2. Sən "Google" deyirsən, amma kompüter adları başa düşmür, yalnız **rəqəmləri** başa düşür.
   Hər kompüterin internetdə ünvanı var: **IP ünvanı**, məsələn `142.250.185.78`.
3. Kompüter **DNS**-dən soruşur: *"google.com-un ünvanı nədir?"*
   DNS — **telefon kitabçasıdır**: adı verirsən, nömrəni qaytarır.
4. Brauzer həmin IP-yə **sorğu (request)** göndərir: *"Mənə ana səhifəni ver"*.
5. O ünvandakı kompüter — **server** — **cavab (response)** qaytarır: HTML, şəkillər və s.
6. Brauzer bunları gözəl səhifəyə çevirib göstərir.

```
Sən (brauzer) ──"google.com?"──▶ DNS ──"142.250.185.78"──▶ Sən
Sən ──── REQUEST: "GET /" ──────▶ Server
Sən ◀─── RESPONSE: HTML ───────── Server
```

Bu **request → response** oyunu internetin hər şeyidir. 14 gün boyunca biz bu oyunun hər iki tərəfini öyrənəcəyik.

## 🔤 Bugünkü sözlər

| Söz | Uşaq dili ilə |
|---|---|
| **Server** | Heç vaxt yatmayan, sorğulara cavab verən kompüter |
| **Client (müştəri)** | Sorğu göndərən — adətən brauzer |
| **IP** | Kompüterin ev ünvanı (rəqəmlərlə) |
| **Domen** | Ünvanın gözəl adı (`google.com`) |
| **DNS** | Adı rəqəmə çevirən telefon kitabçası |
| **HTTP / HTTPS** | Brauzerlə serverin danışdığı dil. **S** = Secure (məktub zərfdə, kimsə oxuya bilmir) |
| **URL** | Tam ünvan: `https://site.az/haqqimizda?dil=az` |

URL-in hissələri:
```
https://   menimsaytim.az   /yazilar   ?sehife=2
protokol   domen            yol (path)  parametrlər (query)
```

## 🛠️ Alətləri quraşdır (praktika)

1. **VS Code** — kod yazmaq üçün dəftər: https://code.visualstudio.com
   - Əlavələr (Extensions): `Python`, `Live Server`.
2. **Python 3.12+**: https://www.python.org/downloads
   - ⚠️ Windows-da quraşdıranda **"Add Python to PATH"** işarəsini qoy!
3. **Git**: https://git-scm.com/downloads
4. **GitHub hesabı**: https://github.com (pulsuzdur)

## 💻 Terminal — kompüterlə yazışmaq

Terminal kompüterə **sözlə əmr vermək** yeridir. VS Code-da: `Terminal → New Terminal`.

```bash
python --version      # Windows-da (Mac/Linux-da: python3 --version)
git --version
mkdir sayt            # "sayt" adlı qovluq yarat
cd sayt               # o qovluğun içinə gir
ls                    # içində nə var? (Windows cmd-də: dir)
cd ..                 # bir qovluq geri çıx
```

## 🔍 Təcrübə: interneti öz gözünlə gör

1. Chrome-da istənilən sayta gir → `F12` bas → **Network** bölməsi → səhifəni yenilə.
   Gördüyün hər sətir bir **request**-dir! Birinə kliklə: `Status 200` = "hər şey yaxşıdır".
2. Terminalda yaz:
   ```bash
   nslookup google.com
   ```
   Bu, DNS-dən ünvan soruşmaqdır. Gördüyün rəqəmlər — IP.

## 🎯 Status kodları (yadda saxla)

- `200` — Oldu ✅
- `301/302` — Başqa yerə köçüb, ora get ➡️
- `404` — Belə şey yoxdur 🤷
- `500` — Serverdə (mətbəxdə) nəsə yandı 🔥
- `401/403` — İcazən yoxdur 🚫

## ✅ Gün sonu yoxlama

1. DNS nə edir? (bir cümlə ilə)
2. Client ilə server arasındakı fərq nədir?
3. `404` nə deməkdir?
4. `https://shop.az/mehsullar?reng=qirmizi` URL-də domen, yol və parametr hansıdır?
5. Terminalda `python --version` işləyirmi?
