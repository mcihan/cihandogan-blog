---
name: ctfl-syllabus
description: ISTQB CTFL v4.0.1 ders programının kendisine dair her soru için kullan — bir öğrenme hedefinin (FL-x.y.z) tam metni, bir bölümün kapsamı, bir terimin resmî tanımı, K seviyeleri, bölüm süreleri, anahtar kelimeler, bölümler arası çapraz referanslar. Syllabus'un ne dediğini doğrulaman gerektiğinde bunu kullan.
---

# CTFL v4.0.1 Ders Programı Uzmanı

## Önce HTML'e bak

Bu reponun ISTQB materyali iki yerde yaşar ve **yayındaki HTML sayfaları doğruluk
kaynağıdır**. `istqb/data/*.json` yalnızca aynı içeriğin hızlı aranabilir indeksidir.

| Soru türü | Bakılacak dosya |
|---|---|
| Syllabus ne diyor, bir konunun tam metni | `static/deniz/istqub/ders_programi_tr.html` |
| Bir sorunun metni, şıkları, kaynağı | aynı sayfa — konunun altındaki akordiyon |
| Bir sorunun **cevabı ve çözümü** | `static/deniz/istqub/questions_tr.html` (`const DATA`) |
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


## Yapı: 6 konu, 22 bölüm, 42 alt bölüm, 64 öğrenme hedefi


**1. Yazılım Testinin Temelleri** — 180 dk · 14 LO

| LO | K | Bölüm | Konu | Soru |
|---|---|---|---|---|
| `FL-1.1.1` | K1 | 1.1.1 | Test Hedefleri | 5 |
| `FL-1.1.2` | K2 | 1.1.2 | Yazılım Testi ve Hata Ayıklama | 4 |
| `FL-1.2.1` | K2 | 1.2.1 | Yazılım Testinin Başarıya Katkısı | 5 |
| `FL-1.2.2` | K1 | 1.2.2 | Test Etme ve Kalite Güvence (KG) | 3 |
| `FL-1.2.3` | K2 | 1.2.3 | İnsan Hataları, Hatalar, Arızalar ve Kök Nedenler | 3 |
| `FL-1.3.1` | K2 | 1.3 | Test Prensipleri | 6 |
| `FL-1.4.1` | K2 | 1.4.1 | Test Aktiviteleri ve Görevleri | 6 |
| `FL-1.4.2` | K2 | 1.4.2 | Proje Bağlamında Test Süreci | 4 |
| `FL-1.4.3` | K2 | 1.4.3 | Test Çalışma Ürünleri | 4 |
| `FL-1.4.4` | K2 | 1.4.4 | Test Esası ve Test Çalışma Ürünleri Arasında İzlenebilirlik | 4 |
| `FL-1.4.5` | K2 | 1.4.5 | Test Etme Sürecindeki Roller | 5 |
| `FL-1.5.1` | K2 | 1.5.1 | Test Etme Sürecinde Gerekli Genel Beceriler | 4 |
| `FL-1.5.2` | K1 | 1.5.2 | Tüm Ekip Yaklaşımı | 6 |
| `FL-1.5.3` | K2 | 1.5.3 | Testin Bağımsızlığı | 5 |

**2. Yazılım Geliştirme Yaşam Döngüsü Boyunca Test** — 130 dk · 10 LO

| LO | K | Bölüm | Konu | Soru |
|---|---|---|---|---|
| `FL-2.1.1` | K2 | 2.1.1 | Yazılım Geliştirme Yaşam Döngüsünün Test Üzerindeki Etkisi | 4 |
| `FL-2.1.2` | K1 | 2.1.2 | Yazılım Geliştirme Yaşam Döngüsü ve İyi Test Etme Uygulamaları | 6 |
| `FL-2.1.3` | K1 | 2.1.3 | Yazılım Geliştirme Faktörü Olarak Test | 6 |
| `FL-2.1.4` | K2 | 2.1.4 | DevOps ve Test Etme | 5 |
| `FL-2.1.5` | K2 | 2.1.5 | Shift-Left Yaklaşımı | 4 |
| `FL-2.1.6` | K2 | 2.1.6 | Geçmişe Dönük Öğeler ve Süreç İyileştirmesi | 6 |
| `FL-2.2.1` | K2 | 2.2.1 | Test Seviyeleri | 4 |
| `FL-2.2.2` | K2 | 2.2.2 | Test Çeşitleri | 4 |
| `FL-2.2.3` | K2 | 2.2.3 | Onaylama Testleri ve Regresyon Testleri | 5 |
| `FL-2.3.1` | K2 | 2.3 | Bakım Testleri | 4 |

**3. Statik Testler** — 80 dk · 8 LO

| LO | K | Bölüm | Konu | Soru |
|---|---|---|---|---|
| `FL-3.1.1` | K1 | 3.1.1 | Statik Testlerle İncelenebilen İş Ürünleri | 3 |
| `FL-3.1.2` | K2 | 3.1.2 | Statik Testin Önemi | 4 |
| `FL-3.1.3` | K2 | 3.1.3 | Statik Test ve Dinamik Test Arasındaki Farklar | 5 |
| `FL-3.2.1` | K1 | 3.2.1 | Erken ve Sık Paydaş Geri Bildiriminin Faydaları | 5 |
| `FL-3.2.2` | K2 | 3.2.2 | Gözden Geçirme Süreci Faaliyetleri | 4 |
| `FL-3.2.3` | K1 | 3.2.3 | Gözden Geçirmede Roller ve Sorumluluklar | 4 |
| `FL-3.2.4` | K2 | 3.2.4 | Gözden Geçirme Çeşitleri | 3 |
| `FL-3.2.5` | K1 | 3.2.5 | Gözden Geçirmelerin Başarı Faktörleri | 4 |

**4. Test Analizi ve Tasarımı** — 390 dk · 14 LO

| LO | K | Bölüm | Konu | Soru |
|---|---|---|---|---|
| `FL-4.1.1` | K2 | 4.1 | Test Tekniklerine Genel Bakış | 6 |
| `FL-4.2.1` | K3 | 4.2.1 | Denklik Paylarına Ayırma | 8 |
| `FL-4.2.2` | K3 | 4.2.2 | Sınır Değer Analizi | 8 |
| `FL-4.2.3` | K3 | 4.2.3 | Karar Tablosu Testleri | 8 |
| `FL-4.2.4` | K3 | 4.2.4 | Durum Geçişi Testleri | 8 |
| `FL-4.3.1` | K2 | 4.3.1 | Komut Testleri ve Komut Kapsama Yüzdesi | 5 |
| `FL-4.3.2` | K2 | 4.3.2 | Dal Testi ve Dal Kapsamı | 5 |
| `FL-4.3.3` | K2 | 4.3.3 | Beyaz Kutu Testinin Önemi | 6 |
| `FL-4.4.1` | K2 | 4.4.1 | Hata Tahminleme | 5 |
| `FL-4.4.2` | K2 | 4.4.2 | Keşif Testi | 6 |
| `FL-4.4.3` | K2 | 4.4.3 | Kontrol Listesine Dayalı Testler | 5 |
| `FL-4.5.1` | K2 | 4.5.1 | İş Birliğine Dayalı Kullanıcı Hikayesi Yazımı | 4 |
| `FL-4.5.2` | K2 | 4.5.2 | Kabul Kriterleri | 6 |
| `FL-4.5.3` | K3 | 4.5.3 | Kabul Testi Güdümlü Yazılım Geliştirme (ATDD) | 8 |

**5. Test Aktivitelerini Yönetme** — 335 dk · 16 LO

| LO | K | Bölüm | Konu | Soru |
|---|---|---|---|---|
| `FL-5.1.1` | K2 | 5.1.1 | Test Planının Amacı ve İçeriği | 3 |
| `FL-5.1.2` | K1 | 5.1.2 | Test Uzmanının Döngü ve Sürüm Planlamasına Katkısı | 3 |
| `FL-5.1.3` | K2 | 5.1.3 | Giriş Kriterleri ve Çıkış Kriterleri | 4 |
| `FL-5.1.4` | K3 | 5.1.4 | Tahminleme Teknikleri | 8 |
| `FL-5.1.5` | K3 | 5.1.5 | Test Senaryosu Önceliklendirme | 8 |
| `FL-5.1.6` | K1 | 5.1.6 | Test Piramidi | 4 |
| `FL-5.1.7` | K2 | 5.1.7 | Test Çeyrekleri | 5 |
| `FL-5.2.1` | K1 | 5.2.1 | Risk Tanımı ve Risk Özellikleri | 4 |
| `FL-5.2.2` | K2 | 5.2.2 | Proje Riskleri ve Ürün Riskleri | 3 |
| `FL-5.2.3` | K2 | 5.2.3 | Ürün Riski Analizi | 5 |
| `FL-5.2.4` | K2 | 5.2.4 | Ürün Risk Kontrolü | 3 |
| `FL-5.3.1` | K1 | 5.3.1 | Yazılım Testlerinde Kullanılan Metrikler | 3 |
| `FL-5.3.2` | K2 | 5.3.2 | Test Raporlarının Amacı, İçeriği ve Hedef Kitlesi | 3 |
| `FL-5.3.3` | K2 | 5.3.3 | Testin Durumunun Bildirilmesi | 3 |
| `FL-5.4.1` | K2 | 5.4 | Yapılandırma Yönetimi | 5 |
| `FL-5.5.1` | K3 | 5.5 | Hata Yönetimi | 8 |

**6. Test Araçları** — 20 dk · 2 LO

| LO | K | Bölüm | Konu | Soru |
|---|---|---|---|---|
| `FL-6.1.1` | K2 | 6.1 | Yazılım Testleri için Araç Desteği | 8 |
| `FL-6.2.1` | K1 | 6.2 | Test Otomasyonunun Faydaları ve Riskleri | 8 |

## Bilmen gereken kurallar

**K seviyeleri.** K1 = hatırlama, K2 = anlama, K3 = uygulama. Sınavda K3 soruları hesap
ister ve daha çok puan eder. Yalnızca şu LO'lar K3'tür: `FL-4.2.1`, `FL-4.2.2`, `FL-4.2.3`,
`FL-4.2.4`, `FL-4.5.3`, `FL-5.1.4`, `FL-5.1.5`, `FL-5.5.1`. Bir soru hesap istiyorsa
neredeyse kesin bu sekizden biridir.

**Sınav.** 40 soru, 60 dakika (ana dili İngilizce olmayan adaylar için 75 dk), geçme notu
26/40 (%65). Puanlama K seviyesine göre değişir.

**Numaralandırma.** `FL-a.b.c` öğrenme hedefi, `a.b.c` bölüm numarası. Çoğu LO aynı
numaralı alt bölüme karşılık gelir; alt bölüm yoksa üst bölüme düşer
(`FL-1.3.1` → bölüm `1.3`, `FL-6.1.1` → bölüm `6.1`). HTML'de bölüm ankoru `#s-4-2-2`.

## Nasıl cevap verirsin

1. `lookup.py lo <LO>` ile hedefi ve bölümünü bul.
2. `lookup.py sec <bölüm>` ile konunun tam metnini oku.
3. Cevabı **syllabus'un kendi terminolojisiyle** ver; Türkçe terimi kullan, ilk geçişte
   İngilizcesini parantezde ekle (ör. "sınır değer analizi (boundary value analysis)").
4. Kaynağı belirt: bölüm numarası ve LO (ör. "§4.2.2, FL-4.2.2 · K3").
5. Syllabus'ta olmayan bir şey soruluyorsa bunu açıkça söyle — uydurma. CTFL kapsamı
   dışındaki konular (indirgenmiş karar tablosu algoritmaları, MC/DC, nöron kapsamı gibi)
   syllabus'ta açıkça kapsam dışı ilan edilmiştir.

## Sık karıştırılanlar

- **Hata ayıklama test değildir.** Test arızayı tetikler; hata ayıklama nedeni bulur ve giderir.
- **Kalite güvence ≠ test.** KG süreç odaklı ve önleyici; test ürün odaklı ve düzeltici,
  kalite kontrolün bir biçimidir.
- **Doğrulama (verification) ≠ sağlama (validation).** Doğrulama "gereksinimi karşılıyor mu",
  sağlama "gerçek ihtiyacı karşılıyor mu".
- **Onaylama testi ≠ regresyon testi.** Onaylama: düzeltme işe yaradı mı. Regresyon:
  değişiklik başka yeri bozdu mu.
- **Test seviyesi ≠ test çeşidi.** Seviye: bileşen, bileşen entegrasyon, sistem, sistem
  entegrasyon, kabul. Çeşit: fonksiyonel, fonksiyonel olmayan, kara kutu, beyaz kutu.
- **Dal kapsamı komut kapsamını içerir**, tersi değil.
