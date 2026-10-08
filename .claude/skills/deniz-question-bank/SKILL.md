---
name: deniz-question-bank
description: /deniz altındaki ISTQB çalışma materyaline dair her iş için kullan — 8 örnek sınavdaki 320 soru, hangi sorunun hangi öğrenme hedefinden geldiği, cevaplar ve çözümler, konu pratikleri, çözüm yöntemleri, BVA konu sayfası. Soru bulmak, soru üretmek, bir konunun hangi sorularda geçtiğini çıkarmak veya /deniz sayfalarını güncellemek gerektiğinde bunu kullan.
---

# Deniz Soru Bankası ve /deniz Çalışma Sitesi Uzmanı

## Önce HTML'e bak

Bu reponun ISTQB materyali iki yerde yaşar ve **yayındaki HTML sayfaları doğruluk
kaynağıdır**. `istqb/data/*.json` yalnızca aynı içeriğin hızlı aranabilir indeksidir.

| Soru türü | Bakılacak dosya |
|---|---|
| Syllabus ne diyor, bir konunun tam metni | `static/deniz/istqub/ders_programi_tr.html` |
| Bir sorunun metni, şıkları, kaynağı | aynı sayfa — konunun altındaki akordiyon |
| Bir sorunun **doğru şık harfi** | aynı sayfa — sorunun altındaki kapalı `details.ans` paneli |
| Bir sorunun **gerekçesi ve ayrıntılı çözümü** | `static/deniz/istqub/questions_tr.html` (`const DATA`) |
| Bir tekniğin adım adım çözüm reçetesi | `static/deniz/istqub/cozum_yontemleri_tr.html` |
| Sınır değer analizi, derinlemesine | `static/deniz/konular/bva.html` |
| Konu pratik testleri | `static/deniz/istqub/pratik_testler_tr.html` |
| Resmî PDF (son başvuru mercii) | `istqb/docs/ISTQB_CTFL_Syllabus-v4.0.1-TR.pdf` |

## Arama aracı

Bu sayfaları elle grep'lemek yerine repo kökünden şunu kullan:

```bash
python3 istqb/tools/lookup.py toc              # tüm bölüm ağacı
python3 istqb/tools/lookup.py sec 4.2.2        # bölümün tam metni (HTML'den okur)
python3 istqb/tools/lookup.py lo  FL-4.2.2     # öğrenme hedefi, K seviyesi, bölümü, soru sayısı
python3 istqb/tools/lookup.py q   FL-4.2.2     # o hedeften çıkmış tüm sorular (cevapsız)
python3 istqb/tools/lookup.py q   A21          # tek soru
python3 istqb/tools/lookup.py ans A21          # cevap + gerekçe + ayrıntılı çözüm (simülatörden)
python3 istqb/tools/lookup.py find "karar tablosu"   # konularda ve sorularda metin arama
```

`sec` komutu doğrudan `ders_programi_tr.html` içindeki `id="s-4-2-2"` elemanını okur;
`ans` komutu `questions_tr.html` içindeki `const DATA` nesnesini ayrıştırır. Yani sayfalar
değişince araç da otomatik güncel kalır. Hafızadan cevap verme — önce bu aracı çalıştır.


`istqb/data/questions_by_lo.json` her soruyu `ans` alanıyla tutar: **yalnızca doğru şıkkın
harfi** (çoktan seçmelide birden çok harf). Gerekçe ve ayrıntılı çözüm o dosyada yoktur,
yalnızca simülatör sayfasındadır. Ders programı sayfasında her sorunun altında, varsayılan
olarak kapalı bir `details.ans` paneli sadece bu harfi gösterir — öğrenci önce kendi
çözsün diye.

## /deniz sayfa haritası

Hepsi `static/deniz/` altında, hepsi **`Munnu123*`** şifresiyle korunur (istemci tarafı
SHA-256 kapısı, `#pw-gate`), hepsinin en üstünde `nav.dz-bc` breadcrumb çubuğu vardır.

| Yol | Ne |
|---|---|
| `index.html` | Hub, kart listesi |
| `istqub/ders_programi_tr.html` | Ders programı + her konunun altında o LO'nun soruları |
| `istqub/questions_tr.html` | Simülatör — 8 sınav × 40 soru, **cevaplar ve çözümler burada** |
| `istqub/pratik_testler_tr.html` | 10 karma test × 5 soru + 4 EP testi × 4 soru |
| `istqub/cozum_yontemleri_tr.html` | Beş hesaplı konunun adım adım reçetesi |
| `konular/index.html` | Konu anlatımları hub'ı |
| `konular/bva.html` | Sınır değer analizi — 11 bölüm, A/B/C/D 21. soruları tam çözümlü |
| `istqub/istqb_study_guide_tr.html` | Görsel çalışma rehberi |
| `java_brushup.html` | Java tazeleme |

## Sınavlar

| Sınav | Set | Tür |
|---|---|---|
| A, D | Resmî Set v1.5 | resmî ISTQB örnek sınavı |
| B, C | Resmî Set v1.6 | resmî ISTQB örnek sınavı |
| E, F, G, H | Pratik Set v1.0 | syllabus'a göre hazırlanmış ek set |

Her sınav 40 soru. **Soru sırası sabittir ve LO sırasını izler** — 20. soru denklik payları,
21. soru sınır değer analizi gibi. E ve H birer kayık (19/20/21/22). Bu yüzden "A21"
demek neredeyse her zaman "BVA sorusu" demektir. **A21 ile B21 aynı soru değildir:**
A21 not hesaplama (kapsam yüzdesi), B21 parola uzunluğu (2→3 değerli fark).

### K3 (hesap isteyen) soruların konumu

| Sınav | Soru no → LO (yalnızca K3 hesap soruları) |
|---|---|
| **A** | 20→`FL-4.2.1`, 21→`FL-4.2.2`, 22→`FL-4.2.3`, 23→`FL-4.2.4`, 29→`FL-4.5.3`, 32→`FL-5.1.4`, 33→`FL-5.1.5`, 38→`FL-5.5.1` |
| **B** | 20→`FL-4.2.1`, 21→`FL-4.2.2`, 22→`FL-4.2.3`, 23→`FL-4.2.4`, 29→`FL-4.5.3`, 31→`FL-5.1.4`, 32→`FL-5.1.5`, 38→`FL-5.5.1` |
| **C** | 20→`FL-4.2.1`, 21→`FL-4.2.2`, 22→`FL-4.2.3`, 23→`FL-4.2.4`, 29→`FL-4.5.3`, 31→`FL-5.1.4`, 32→`FL-5.1.5`, 38→`FL-5.5.1` |
| **D** | 20→`FL-4.2.1`, 21→`FL-4.2.2`, 22→`FL-4.2.3`, 23→`FL-4.2.4`, 29→`FL-4.5.3`, 31→`FL-5.1.4`, 32→`FL-5.1.5`, 38→`FL-5.5.1` |
| **E** | 19→`FL-4.2.1`, 20→`FL-4.2.2`, 21→`FL-4.2.3`, 22→`FL-4.2.4`, 29→`FL-4.5.3`, 32→`FL-5.1.4`, 33→`FL-5.1.5`, 38→`FL-5.5.1` |
| **F** | 20→`FL-4.2.1`, 21→`FL-4.2.2`, 22→`FL-4.2.3`, 23→`FL-4.2.4`, 29→`FL-4.5.3`, 31→`FL-5.1.4`, 32→`FL-5.1.5`, 38→`FL-5.5.1` |
| **G** | 20→`FL-4.2.1`, 21→`FL-4.2.2`, 22→`FL-4.2.3`, 23→`FL-4.2.4`, 29→`FL-4.5.3`, 32→`FL-5.1.4`, 33→`FL-5.1.5`, 38→`FL-5.5.1` |
| **H** | 19→`FL-4.2.1`, 20→`FL-4.2.2`, 21→`FL-4.2.3`, 22→`FL-4.2.4`, 29→`FL-4.5.3`, 30→`FL-5.1.4`, 31→`FL-5.1.5`, 38→`FL-5.5.1` |

### Öğrenme hedefi → soru dizini (tamamı)

| LO | Bölüm | K | Sorular |
|---|---|---|---|
| `FL-1.1.1` | 1.1.1 Test Hedefleri | K1 | A1, C1, D1, E1, G1 |
| `FL-1.1.2` | 1.1.2 Yazılım Testi ve Hata Ayıklama | K2 | C2, E2, F1, H1 |
| `FL-1.2.1` | 1.2.1 Yazılım Testinin Başarıya Katkısı | K2 | A2, B1, F2, G2, H2 |
| `FL-1.2.2` | 1.2.2 Test Etme ve Kalite Güvence (KG) | K1 | B2, E3, F3 |
| `FL-1.2.3` | 1.2.3 İnsan Hataları, Hatalar, Arızalar ve Kök Nedenler | K2 | D2, F4, H3 |
| `FL-1.3.1` | 1.3 Test Prensipleri | K2 | A3, B3, C3, D3, E4, F5 |
| `FL-1.4.1` | 1.4.1 Test Aktiviteleri ve Görevleri | K2 | A4, B4, C4, D4, F6, G3 |
| `FL-1.4.2` | 1.4.2 Proje Bağlamında Test Süreci | K2 | A5, B5, F7, H4 |
| `FL-1.4.3` | 1.4.3 Test Çalışma Ürünleri | K2 | C5, D5, E5, G4 |
| `FL-1.4.4` | 1.4.4 Test Esası ve Test Çalışma Ürünleri Arasında İzlenebilirlik | K2 | B6, E6, G5, H5 |
| `FL-1.4.5` | 1.4.5 Test Etme Sürecindeki Roller | K2 | A6, C6, D6, G6, H6 |
| `FL-1.5.1` | 1.5.1 Test Etme Sürecinde Gerekli Genel Beceriler | K2 | A7, B7, E7, G7 |
| `FL-1.5.2` | 1.5.2 Tüm Ekip Yaklaşımı | K1 | A8, B8, C7, D7, G8, H7 |
| `FL-1.5.3` | 1.5.3 Testin Bağımsızlığı | K2 | C8, D8, E8, F8, H8 |
| `FL-2.1.1` | 2.1.1 Yazılım Geliştirme Yaşam Döngüsünün Test Üzerindeki Etkisi | K2 | B9, E9, F9, G9 |
| `FL-2.1.2` | 2.1.2 Yazılım Geliştirme Yaşam Döngüsü ve İyi Test Etme Uygulamaları | K1 | A9, B10, C9, D9, F10, H9 |
| `FL-2.1.3` | 2.1.3 Yazılım Geliştirme Faktörü Olarak Test | K1 | A10, B11, C10, D10, G10, H10 |
| `FL-2.1.4` | 2.1.4 DevOps ve Test Etme | K2 | B12, D11, F11, G11, H11 |
| `FL-2.1.5` | 2.1.5 Shift-Left Yaklaşımı | K2 | A11, C11, E10, G12 |
| `FL-2.1.6` | 2.1.6 Geçmişe Dönük Öğeler ve Süreç İyileştirmesi | K2 | A12, C12, D12, E11, F12, G13 |
| `FL-2.2.1` | 2.2.1 Test Seviyeleri | K2 | A13, B13, C13, E12 |
| `FL-2.2.2` | 2.2.2 Test Çeşitleri | K2 | D13, E13, F13, H12 |
| `FL-2.2.3` | 2.2.3 Onaylama Testleri ve Regresyon Testleri | K2 | A14, B14, C14, E14, H13 |
| `FL-2.3.1` | 2.3 Bakım Testleri | K2 | D14, F14, G14, H14 |
| `FL-3.1.1` | 3.1.1 Statik Testlerle İncelenebilen İş Ürünleri | K1 | D15, F15, G15 |
| `FL-3.1.2` | 3.1.2 Statik Testin Önemi | K2 | A15, D16, F16, H15 |
| `FL-3.1.3` | 3.1.3 Statik Test ve Dinamik Test Arasındaki Farklar | K2 | B15, C15, E15, G16, H16 |
| `FL-3.2.1` | 3.2.1 Erken ve Sık Paydaş Geri Bildiriminin Faydaları | K1 | A16, B16, C16, F17, G17 |
| `FL-3.2.2` | 3.2.2 Gözden Geçirme Süreci Faaliyetleri | K2 | B17, D17, G18, H17 |
| `FL-3.2.3` | 3.2.3 Gözden Geçirmede Roller ve Sorumluluklar | K1 | B18, D18, E16, H18 |
| `FL-3.2.4` | 3.2.4 Gözden Geçirme Çeşitleri | K2 | A17, C17, E17 |
| `FL-3.2.5` | 3.2.5 Gözden Geçirmelerin Başarı Faktörleri | K1 | A18, C18, E18, F18 |
| `FL-4.1.1` | 4.1 Test Tekniklerine Genel Bakış | K2 | A19, B19, C19, D19, F19, G19 |
| `FL-4.2.1` | 4.2.1 Denklik Paylarına Ayırma | K3 | A20, B20, C20, D20, E19, F20, G20, H19 |
| `FL-4.2.2` | 4.2.2 Sınır Değer Analizi | K3 | A21, B21, C21, D21, E20, F21, G21, H20 |
| `FL-4.2.3` | 4.2.3 Karar Tablosu Testleri | K3 | A22, B22, C22, D22, E21, F22, G22, H21 |
| `FL-4.2.4` | 4.2.4 Durum Geçişi Testleri | K3 | A23, B23, C23, D23, E22, F23, G23, H22 |
| `FL-4.3.1` | 4.3.1 Komut Testleri ve Komut Kapsama Yüzdesi | K2 | A24, B24, D24, F24, G24 |
| `FL-4.3.2` | 4.3.2 Dal Testi ve Dal Kapsamı | K2 | B25, C24, E23, G25, H23 |
| `FL-4.3.3` | 4.3.3 Beyaz Kutu Testinin Önemi | K2 | A25, C25, D25, E24, F25, H24 |
| `FL-4.4.1` | 4.4.1 Hata Tahminleme | K2 | A26, C26, D26, E25, F26 |
| `FL-4.4.2` | 4.4.2 Keşif Testi | K2 | A27, B26, D27, E26, G26, H25 |
| `FL-4.4.3` | 4.4.3 Kontrol Listesine Dayalı Testler | K2 | B27, C27, E27, G27, H26 |
| `FL-4.5.1` | 4.5.1 İş Birliğine Dayalı Kullanıcı Hikayesi Yazımı | K2 | D28, E28, F27, H27 |
| `FL-4.5.2` | 4.5.2 Kabul Kriterleri | K2 | A28, B28, C28, F28, G28, H28 |
| `FL-4.5.3` | 4.5.3 Kabul Testi Güdümlü Yazılım Geliştirme (ATDD) | K3 | A29, B29, C29, D29, E29, F29, G29, H29 |
| `FL-5.1.1` | 5.1.1 Test Planının Amacı ve İçeriği | K2 | C30, E30, F30 |
| `FL-5.1.2` | 5.1.2 Test Uzmanının Döngü ve Sürüm Planlamasına Katkısı | K1 | A30, E31, G30 |
| `FL-5.1.3` | 5.1.3 Giriş Kriterleri ve Çıkış Kriterleri | K2 | A31, B30, D30, G31 |
| `FL-5.1.4` | 5.1.4 Tahminleme Teknikleri | K3 | A32, B31, C31, D31, E32, F31, G32, H30 |
| `FL-5.1.5` | 5.1.5 Test Senaryosu Önceliklendirme | K3 | A33, B32, C32, D32, E33, F32, G33, H31 |
| `FL-5.1.6` | 5.1.6 Test Piramidi | K1 | C33, E34, G34, H32 |
| `FL-5.1.7` | 5.1.7 Test Çeyrekleri | K2 | A34, B33, C34, D33, F33 |
| `FL-5.2.1` | 5.2.1 Risk Tanımı ve Risk Özellikleri | K1 | D34, E35, F34, H33 |
| `FL-5.2.2` | 5.2.2 Proje Riskleri ve Ürün Riskleri | K2 | D35, F35, H34 |
| `FL-5.2.3` | 5.2.3 Ürün Riski Analizi | K2 | C35, E36, F36, G35, H35 |
| `FL-5.2.4` | 5.2.4 Ürün Risk Kontrolü | K2 | A35, B34, G36 |
| `FL-5.3.1` | 5.3.1 Yazılım Testlerinde Kullanılan Metrikler | K1 | B35, F37, H36 |
| `FL-5.3.2` | 5.3.2 Test Raporlarının Amacı, İçeriği ve Hedef Kitlesi | K2 | C36, D36, E37 |
| `FL-5.3.3` | 5.3.3 Testin Durumunun Bildirilmesi | K2 | A36, B36, G37 |
| `FL-5.4.1` | 5.4 Yapılandırma Yönetimi | K2 | A37, B37, C37, D37, H37 |
| `FL-5.5.1` | 5.5 Hata Yönetimi | K3 | A38, B38, C38, D38, E38, F38, G38, H38 |
| `FL-6.1.1` | 6.1 Yazılım Testleri için Araç Desteği | K2 | A39, B39, C39, D39, E39, F39, G39, H39 |
| `FL-6.2.1` | 6.2 Test Otomasyonunun Faydaları ve Riskleri | K1 | A40, B40, C40, D40, E40, F40, G40, H40 |

## Not defteri — `istqb/note.html`

Cihan sohbette bir kavramı açıklattığında sık sık **"bunu nota ekle"** der. Hedef dosya
`istqb/note.html`. Yayınlanmaz (Hugo yalnızca `content/` ve `static/` altını yayımlar).

Ekleme şekli: dosyadaki `YENİ NOT BURAYA EKLENİR` yorumunun **hemen üstüne** bir
`<article>` koy. İçindekiler listesi makalelerden JavaScript ile üretilir, elle
güncellemek gerekmez.

```html
<article class="note" id="n-kisa-slug" data-title="Kısa başlık">
  <header><h2>Başlık</h2>
  <span class="src">Syllabus §x.y · FL-x.y.z · ingilizce terim</span></header>
  ... içerik ...
</article>
```

Hazır bileşenler: `div.box.key` (ana fikir), `div.box.trap` (tuzak/sınav notu),
`div.box.warn` (dikkat), `table.t` (`div.scroll` içinde), `div.chain` (zincir rozetleri),
`b.k` (vurgulu terim), `pre > code`.

Notun biçimi, sohbette anlattığım biçimin aynısı olmalı: tek cümlelik tanım, somut
örnek(ler), karıştırılan kavramla farkı, pratik ayırt etme kuralı, sınavda nereden
çıktığı. Uzatma — not tek kavramı anlatır.

## Yeni soru üretirken uyulan kurallar

Cihan bu kuralları net koydu (kardeşi Deniz için hazırlıyor):

- **Türkçe**, sınav konseptinde, kolaydan ortaya. **Asla gerçek sınavdan daha zor olmasın.**
- Mevcut soruları **birebir tekrarlama** — benzeri olsun, aynısı olmasın. Üretmeden önce
  `lookup.py find "<anahtar>"` ile ara.
- **Durum geçişi sorularında diyagramı soruda verme.** Geçiş listesini metin olarak ver,
  öğrenci kendi çizsin; renkli diyagramı yalnızca çözümde göster.
- **Regresyon/onaylama soruları** resmî formatta olmalı: numaralı koşum geçmişi tablosu
  (TC × Koşum, hücrelerde `(n) Başarılı/Başarısız`).
- Cevap şıklarını **a/b/c/d arasında dengeli dağıt** — hepsi (a) veya (b) olmasın.
- Her soruda **LO ve K seviyesi** etiketlenir.

## Hesap konularının formülleri

Bunlar `cozum_yontemleri_tr.html` ve `konular/bva.html` ile birebir tutarlı olmalı:

| Konu | Formül |
|---|---|
| Denklik payları (`FL-4.2.1`) | Each Choice: `min test = max(satır, sütun)`; kısıt varsa `toplam pay − m` |
| Sınır değer (`FL-4.2.2`) | `sınır sayısı = pay × 2 − açık uç sayısı`; 2-değerli = sınırların kendisi; 3-değerli = her sınıra ±1 |
| Karar tablosu (`FL-4.2.3`) | `2ⁿ` kural; kapsam = denenen sütun / uygulanabilir sütun |
| Durum geçişi (`FL-4.2.4`) | 0-anahtar (geçerli geçişler); `min test = max(başlangıçtan çıkan ok, bitişe giren ok)` |
| Onaylama/regresyon (`FL-2.2.3`) | Önceki sonuç **Başarısız → onaylama**, **Başarılı → regresyon**, yoksa ilk koşum |

Kapsam yüzdesinde **payda her zaman kapsam öğesi sayısıdır, test sayısı değil.**

## Bu repoda çalışma şekli

1. Kullanıcı başka bir dalda olabilir (`web-site-version-1`, tema dosyaları değişik).
   **Çalışma ağacına ve açık dalına dokunma**; `git commit-tree` ile `istqb-tr-pratik`
   dalına, `origin/main` üstüne commit kur.
2. **Push'u kullanıcı yapar** — sandbox'ta GitHub kimliği yok:
   `git push origin istqb-tr-pratik:main`
3. HTML değiştirdiysen Playwright ile doğrula: konsol hatası yok, mobilde (390px) yatay
   taşma yok, şifre kapısı `Munnu123*` ile açılıyor, breadcrumb yerinde.
4. Yeni bir /deniz sayfası eklediysen: breadcrumb + şifre kapısı ekle, hub'a kart koy.
