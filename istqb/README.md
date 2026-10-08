# istqb/ — ISTQB CTFL v4.0.1 çalışma kaynakları

Bu klasör yayınlanmaz (Hugo yalnızca `content/` ve `static/` altını yayımlar).
Yayındaki sayfalar `static/deniz/` altındadır; burası onların **kaynağı ve indeksi**.

| Yol | Ne |
|---|---|
| `docs/ISTQB_CTFL_Syllabus-v4.0.1-TR.pdf` | Resmî ders programı, Türkçe (79 sayfa) |
| `data/syllabus_tree.json` | 6 konu → 22 bölüm → 42 alt bölüm → 64 öğrenme hedefi |
| `data/syllabus_body.json` | Her bölümün gövde metni, paragraf/madde blokları hâlinde |
| `data/questions_by_lo.json` | 8 sınavdaki 320 sorunun tamamı, LO'ya göre gruplanmış (cevapsız) |
| `tools/lookup.py` | Yayındaki HTML'lerde arama aracı |

## Arama aracı

Repo kökünden çalıştır:

```bash
python3 istqb/tools/lookup.py toc              # tüm bölüm ağacı
python3 istqb/tools/lookup.py sec 4.2.2        # bölümün tam metni
python3 istqb/tools/lookup.py lo  FL-4.2.2     # öğrenme hedefi + K seviyesi + soru sayısı
python3 istqb/tools/lookup.py q   FL-4.2.2     # o hedeften çıkmış tüm sorular
python3 istqb/tools/lookup.py q   A21          # tek soru
python3 istqb/tools/lookup.py ans A21          # cevap + gerekçe + ayrıntılı çözüm
python3 istqb/tools/lookup.py find "karar tablosu"
```

`sec` doğrudan `static/deniz/istqub/ders_programi_tr.html` içinden, `ans` ise
`static/deniz/istqub/questions_tr.html` içindeki `const DATA` nesnesinden okur —
sayfalar değişince araç da güncel kalır.

## Skill'ler

`.claude/skills/ctfl-syllabus` ve `.claude/skills/deniz-question-bank`, bu repoda Claude
ile çalışırken otomatik devreye girer ve ikisi de önce yukarıdaki HTML sayfalarına bakar.

## Telif

Ders programı © International Software Testing Qualifications Board (ISTQB®);
Türkçe çeviri Yazılım Test ve Kalite Derneği. Sorular resmî örnek sınavlardan (A–D) ve
syllabus'a göre hazırlanmış pratik setlerden (E–H). Kişisel çalışma amaçlıdır.
