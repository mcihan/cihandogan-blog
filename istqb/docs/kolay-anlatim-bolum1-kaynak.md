# ISTQB Temel Kavramlar Özeti

---

## 1️⃣ Hata / Arıza / Hata Ayıklama

| Kavram | Ne demek? | Örnek |
|---|---|---|
| **Hata (Bug/Error)** | Geliştirici kodda yanlış yapar | `a - b` yazması gerekirken `a + b` yazdı |
| **Arıza (Failure)** | Hatanın çalışırken ortaya çıkması | Uygulama çöktü, yanlış sonuç verdi |
| **Hata Ayıklama (Debugging)** | Hatanın nedenini bulup düzeltme | Kodu inceleyip yanlış satırı düzeltmek |

> 🔑 **Hata** → sebep, **Arıza** → sonuç, **Hata Ayıklama** → çözüm

---

## 2️⃣ Test Etme vs Kalite Güvence (KG)

| | **Test Etme** | **Kalite Güvence** |
|---|---|---|
| **Odak** | Ürün | Süreç |
| **Yaklaşım** | Düzeltici | Önleyici |
| **Soru** | Ürün doğru mu? | Süreç doğru mu? |
| **Kim?** | Test ekibi | Herkes |
| **Örnek** | Story 24 saatte silindi mi? | Neden hep zamanlayıcı hataları çıkıyor? |

> 🔑 **Test** yangını söndürür, **KG** yangın çıkmaması için tedbir alır

---

## 3️⃣ Statik Test vs Dinamik Test

| | **Statik Test** | **Dinamik Test** |
|---|---|---|
| **Nasıl?** | Kodu çalıştırmadan | Kodu çalıştırarak |
| **Ne zaman?** | Erken aşamada | Kod yazıldıktan sonra |
| **Hata bulma** | Daha erken ve ucuz | Daha geç ve pahalı |
| **Örnek** | Kod inceleme, gereksinim gözden geçirme | Birim testi, sistem testi |

> 🔑 Statik test hataları **daha erken** ve **daha ucuza** bulur

---

## 4️⃣ Tipik Test Amaçları (ISTQB)

### ✅ Bunlar test amacıdır:
- Hataları bulmak ve arızaları tetiklemek
- Gereksinimlerin karşılandığını doğrulamak
- Paydaşlara sürüm kararı için bilgi sağlamak
- Kullanıcı beklentilerinin karşılandığını doğrulamak
- Yasal/sözleşmesel gereklilikleri karşılamak
- Kalan risk seviyesini düşürmek

### ❌ Bunlar test amacı DEĞİLdir:
- Kök nedeni bulmak → Debugging'in işi
- Hiç hata kalmadığını kanıtlamak → İmkansız! (ISTQB 1. Prensip)
- Kalite süreçlerini yönetmek → KG'nin işi
- Kodu düzeltip sürüme almak → Geliştirici + Debugging işi

---

## 5️⃣ Testin Başarıya Katkısı

- 💰 Hataları **ucuz ve erken** bulmayı sağlar
- 📊 Ürün kalitesini **ölçer** → sürüm kararlarına katkı sağlar
- 👤 **Kullanıcıyı temsil eder** → gerçek kullanıcıları dahil etmek pahalıdır
- ⚖️ **Yasal zorunlulukları** karşılar

---

## 6️⃣ Sınav İçin Kritik Kurallar

| Kural | Açıklama |
|---|---|
| **Test ≠ Debugging** | Test hata bulur, Debugging kök nedeni çözer |
| **Test ≠ KG** | Test ürüne bakar, KG sürece bakar |
| **Statik ≠ Dinamik** | Statik okur, Dinamik çalıştırır |
| **%100 test imkansız** | ISTQB 2. Prensibi |
| **Hiç hata yok ispatlanamaz** | ISTQB 1. Prensibi |
| **Erken test = ucuz test** | ISTQB 3. Prensibi |

---

## 🧠 Her Şeyi Tek Tabloda:

| Kavram | Kısaca |
|---|---|
| **Hata (Error/Bug)** | Kodda yapılan yanlışlık |
| **Arıza (Failure)** | Hatanın çalışırken görünmesi |
| **Hata Ayıklama (Debugging)** | Hatayı bulup düzeltme süreci |
| **Test Etme** | Ürün doğru mu? diye kontrol etmek |
| **Kalite Güvence (KG)** | Süreç doğru mu? diye kontrol etmek |
| **Statik Test** | Kodu okuyarak/inceleyerek hata bulmak |
| **Dinamik Test** | Kodu çalıştırarak hata bulmak |




-------------

<br/>


# İnsan Hataları, Yazılım Hataları ve Arızalar

---

## 👤 İnsanlar Neden Hata Yapar?

* ⏰ **Zaman baskısı** → Aceleci davranmak
* 🧩 **Karmaşık iş** → Zor gereksinimler, karmaşık kod
* 😴 **Yorgunluk** → Dikkat dağınıklığı
* 📚 **Yetersiz eğitim** → Konuyu tam bilmemek
* 🗣️ **İletişim eksikliği** → Yanlış anlaşılmalar
* 🏗️ **Kötü altyapı/süreç** → Çalışmayı zorlaştıran ortam

---

## 📍 Hatalar Nerede Bulunur?

* 📋 **Gereksinim belgelerinde** → Yanlış/eksik yazılmış gereksinim
* 💻 **Kaynak kodda** → Yanlış yazılmış kod satırı
* 🧪 **Test betiklerinde** → Hatalı yazılmış test senaryosu
* 📦 **Derleme/yapılandırma dosyalarında** → Yanlış ayarlar

---

## 🔁 Hata Nasıl Yayılır?

* Erken aşamada yapılan hata **tespit edilmezse** →
* Sonraki aşamalarda da hatalı ürünler çıkar →
* Hata giderek **büyür ve pahalılaşır** 💸

> Örnek: Gereksinim yanlış yazıldı → Kod yanlış yazıldı → Test yanlış yapıldı → Kullanıcıya hatalı ürün gitti

---

## ⚡ Her Hata Her Zaman Arızaya Neden Olmaz!

* 🔴 **Her zaman arızaya neden olan hatalar** → Kod çalışınca hep çöker
* 🟡 **Bazen arızaya neden olan hatalar** → Sadece belirli koşullarda çöker
* 🟢 **Hiç arızaya neden olmayan hatalar** → Kodda var ama hiç tetiklenmez

> Örnek: Sadece 29 Şubat'ta çalışan bir kod → Yılda 1 kez arıza çıkarır!

---

## 🌍 Arızanın Sebebi Sadece İnsan Hatası Değildir!

* ☢️ **Radyasyon** → Donanım yazılımını bozabilir
* 📡 **Elektromanyetik alan** → Sistemi etkileyebilir
* 🌡️ **Çevresel koşullar** → Aşırı sıcak, nem vb.

> Yani bazen kimse hata yapmamış olsa bile arıza çıkabilir!

---

## 🔍 Kök Neden Nedir?

* Bir problemin **temel sebebidir**
* Arıza çıkınca veya hata bulununca **kök neden analizi** yapılır
* Kök neden bulunup **ortadan kaldırılırsa** → Benzer hatalar tekrar çıkmaz

> Örnek:
> ```
> Arıza: Uygulama çöktü
> Hata: Kod yanlış yazılmış
> Kök Neden: Geliştirici eğitim almamış
> Çözüm: Eğitim ver → Benzer hatalar bir daha çıkmaz
> ```

---

## 🧠 Özet Zinciri:

```
İnsan hatası yapar
    ↓
Kodda/belgede hata oluşur
    ↓
Kod çalışınca arıza çıkar
    ↓
Kök neden analizi yapılır
    ↓
Kök neden düzeltilir → Benzer hatalar önlenir

```

<br/>

# Hata / Kusur / Arıza / Kök Neden — Kavramlar ve Örnekler

---

## 🧠 Temel Tanımlar

| Kavram | Ne demek? |
|---|---|
| **Kök Neden** | Hatanın ortaya çıkmasının **temel sebebi** (insan, süreç, ortam) |
| **Hata (Error)** | İnsanın yaptığı **yanlış eylem veya karar** |
| **Kusur (Defect/Bug)** | Hatanın **koda veya belgeye yansımış hali** |
| **Arıza (Failure)** | Kusurlu kodun **çalışınca yanlış davranması** |

> 🔑 Zincir: **Kök Neden → Hata → Kusur → Arıza**

---

## 📌 Örnek 1 — Bonus Hesaplama & Engelli Kullanıcı

### Senaryo:
- Tasarımcı yorgun olduğu için engelli kullanıcıları dikkate almayan arayüz tasarladı
- Programcı zaman baskısı altında bonus hesaplamalarına hata yönetimi eklemedi
- Engelli kullanıcılar şikayet etti → Şirkete para cezası kesildi
- Bonus hesaplamalarının bazen yanlış olduğu fark edilmedi

### Sınıflandırma:
| Kavram | Bu örnekte |
|---|---|
| **Kök Neden** | Programcının **zaman baskısı altında** çalışması ✅ |
| **Hata (Error)** | Tasarımcının engelli kullanıcıları **dikkate almama kararı** |
| **Kusur (Defect)** | Bonusların **bazen yanlış hesaplanması** (kodda var ama tetiklenmedi) |
| **Arıza (Failure)** | Şirketin **para cezası alması** (sistem yanlış davrandı) |

### Neden C doğru?
> - A ❌ → Bonus hatası "zaman zaman" değil, kodda **sürekli var** ama tetiklenmedi → bu bir **kusurdur**
> - B ❌ → Para cezası bir **arızanın sonucu**, arızanın kendisi değil
> - C ✅ → Zaman baskısı → **kök nedendir**, hataya yol açan temel sebep
> - D ❌ → Arayüz tasarımı hata **içerir** doğru ama soru "doğru ifade" soruyor, C daha kesin

---

## 📌 Örnek 2 — Çevrimiçi Sınav Gözetim Sistemi

### Senaryo:
- Sınav süresi dolunca oturum kapanması gerekirken açık kaldı
- Geliştirici yanlış operatör kullandı
- Ekipte zaman birimleri konusunda **hiç eğitim verilmemiş**

### Sınıflandırma:
| Kavram | Bu örnekte |
|---|---|
| **Kök Neden** | Ekibe **eğitim verilmemiş** olması ✅ |
| **Hata (Error)** | Geliştiricinin **yanlış operatörü yazması** (insan eylemi) |
| **Kusur (Defect)** | **Koddaki yanlış operatör** (hatanın koda yansıması) |
| **Arıza (Failure)** | **Oturumun açık kalması** (sistemin yanlış davranması) |

### Zincir:
```
Eğitim yok (Kök Neden)
    ↓
Geliştirici yanlış operatör yazdı (Hata)
    ↓
Kodda yanlış operatör kaldı (Kusur)
    ↓
Oturum kapanmadı (Arıza)
```

---

## 📌 Örnek 3 — Otel Fiyatlandırma Motoru

### Senaryo:
- İndirim SADECE 3 geceden FAZLA rezervasyonlara uygulanmalı
- Geliştirici kuralı yanlış anladı → "3 gece ve üzeri" diye kodladı
- 3 gecelik rezervasyona yanlışlıkla indirim uygulandı

### Sınıflandırma:
| Kavram | Bu örnekte |
|---|---|
| **Hata (Error)** | Geliştiricinin kuralı **yanlış anlaması** (insan eylemi) ✅ |
| **Kusur (Defect)** | Koddaki **yanlış koşul** `>=3` yerine `>3` olmalıydı ✅ |
| **Arıza (Failure)** | 3 gecelik rezervasyona **indirimin yanlış uygulanması** ✅ |

### Zincir:
```
Kuralı yanlış anladı (Hata)
    ↓
Koda yanlış koşul yazdı (Kusur)
    ↓
Müşteriye yanlış indirim uygulandı (Arıza)
```

---

## 🧠 Hepsini Birleştiren Özet Tablo

| Kavram | Tanım | Örnek 1 | Örnek 2 | Örnek 3 |
|---|---|---|---|---|
| **Kök Neden** | Temel sebep | Zaman baskısı | Eğitim verilmemesi | — |
| **Hata (Error)** | İnsanın yanlış eylemi | Arayüzde engellileri atlamak | Yanlış operatör yazmak | Kuralı yanlış anlamak |
| **Kusur (Defect)** | Hatanın koda yansıması | Bonus hesaplama hatası | Koddaki yanlış operatör | Koddaki yanlış koşul |
| **Arıza (Failure)** | Sistemin yanlış davranması | Para cezası alınması | Oturumun açık kalması | Yanlış indirim uygulanması |

---

## 🔑 Altın Kural:

```
Kök Neden  → "Neden hata yapıldı?"        → Eğitimsizlik, yorgunluk, baskı
Hata       → "İnsan ne yaptı?"            → Yanlış anladı, yanlış yazdı
Kusur      → "Kodda ne var?"              → Yanlış operatör, yanlış koşul
Arıza      → "Sistem ne yaptı?"           → Çöktü, yanlış sonuç verdi
```


# ISTQB 7 Test Prensibi — Basit Açıklama

---

## 1️⃣ Test, hata olmadığını ispatlayamaz

* Test yaparak **"hata var"** diyebilirsin ✅
* Ama **"hiç hata yok"** diyemezsin ❌
* Test sadece **keşfedilmemiş hata olasılığını azaltır**
* Tüm testler geçse bile yazılım kullanıcı ihtiyaçlarını karşılamıyor olabilir

> 💡 Örnek: Instagram'ı test ettin, hata bulamadın → Bu "Instagram mükemmel" demek değil, sadece "bulamadın" demek

---

## 2️⃣ %100 Test Etmek İmkansızdır

* Her şeyi test etmeye kalkarsan **zaman ve para biter**
* Bunun yerine şunları kullan:
  * 🎯 **Risk bazlı test** → En riskli yerleri önce test et
  * 📋 **Test önceliklendirme** → Önemli testleri öne al
  * 🔧 **Test teknikleri** → Akıllıca test et

> 💡 Örnek: WhatsApp'ta mesaj gönderme özelliği, karanlık mod renginden çok daha kritiktir → Önce onu test et

---

## 3️⃣ Erken Test = Zaman ve Para Tasarrufu

* Hata **ne kadar erken** bulunursa düzeltmesi **o kadar ucuz**
* Gereksinimde bulunan hata → **En ucuz**
* Canlı sistemde bulunan hata → **En pahalı** 💸
* Hem statik hem dinamik test **mümkün olduğunca erken** başlamalı

> 💡 Örnek:
> ```
> Gereksinim aşamasında hata → 1 saatte düzeltilir
> Canlıya çıktıktan sonra hata → Haftalarca sürer, müşteri kaybedilir
> ```

---

## 4️⃣ Hatalar Belirli Yerlerde Yoğunlaşır (Pareto Prensibi)

* Hataların **%80'i** genellikle kodun **%20'sinde** bulunur
* Yani bazı modüller/özellikler **sürekli hata üretir**
* Bu bilgi → **risk bazlı testte** kullanılır, sorunlu alanlara odaklanılır

> 💡 Örnek: Instagram'da ödeme modülü, profil fotoğrafı değiştirmekten çok daha fazla hata üretir → Oraya odaklan

---

## 5️⃣ Antibiyotik Direnci — Aynı Test Hep İşe Yaramaz

* Aynı testleri **tekrar tekrar** çalıştırırsan → Yeni hata **bulamazsın**
* Yazılım testlere "alışır", gizli hatalar ortaya çıkmaz
* Çözüm: **Yeni testler yaz, test verilerini değiştir**
* ⚠️ İstisna: Regresyon testleri aynı kalabilir (eski hataların geri gelmediğini kontrol eder)

> 💡 Örnek:
> ```
> Hep aynı kullanıcıyla, aynı şifreyle, aynı tarayıcıda test ediyorsun
> → Farklı kullanıcı, farklı cihaz, farklı senaryo dene!
> ```

---

## 6️⃣ Test Bağlama Göre Değişir

* Her proje için **tek tip test yaklaşımı yoktur**
* Banka uygulaması ≠ Oyun uygulaması ≠ Hastane sistemi
* Projenin türüne, riskine, bütçesine göre test **farklılaşır**

> 💡 Örnek:
> ```
> Hastane yazılımı → Çok sıkı, kapsamlı test (hayat riski var!)
> Basit not alma uygulaması → Daha hafif test yeterli
> ```

---

## 7️⃣ "Hata Bulamadık = Başarılı Yazılım" Yanılgısı

* Tüm testler geçti + Tüm hatalar düzeltildi → **Yine de kötü yazılım olabilir!**
* Çünkü:
  * Kullanıcı ihtiyaçlarını karşılamıyor olabilir
  * Rakip ürünlerden zayıf olabilir
  * Müşterinin iş hedeflerine ulaşmıyor olabilir
* Test sadece **doğrulama** değil, **sağlama** da yapmalıdır

> 💡 Örnek:
> ```
> Uygulama tüm gereksinimleri karşılıyor ✅
> Ama kullanıcılar kullanmayı zor buluyor 😤
> → Testler geçti ama yazılım başarısız!
> ```

---

## 🧠 7 Prensibi Tek Tabloda:

| # | Prensip | Kısaca |
|---|---|---|
| 1 | Hata olmadığı ispatlanamaz | "Hata yok" diyemezsin |
| 2 | %100 test imkansız | Akıllıca, öncelikli test et |
| 3 | Erken test ucuzdur | Erken bul, ucuza düzelt |
| 4 | Hatalar yoğunlaşır | %80 hata, %20 kodda |
| 5 | Antibiyotik direnci | Aynı test hep işe yaramaz |
| 6 | Bağlama göre değişir | Her proje farklı test ister |
| 7 | Hata yok ≠ Başarı | Testler geçse de yazılım kötü olabilir |



# Test Aktiviteleri ve Görevleri — Örneklerle Açıklama

---

## 🔄 Genel Bilgi

> Aktiviteler sırayla gibi görünse de **paralel veya tekrarlı** olarak uygulanır.
> Her proje ve sisteme göre **uyarlanması** gerekir.

---

## 1️⃣ Test Planlama
**"Ne yapacağız, nasıl yapacağız?"**

* Test hedefleri, kapsamı ve yaklaşımı belirlenir
* Kaynaklar, zaman ve bütçe planlanır

> 💡 **Örnek — Instagram DM Özelliği:**
> - Hangi özellikler test edilecek? → Mesaj gönderme, silme, iletme
> - Kim test edecek? → 3 kişilik test ekibi
> - Ne zaman? → 2 hafta
> - Otomasyon mu, manuel mi? → Kritik akışlar otomatik

---

## 2️⃣ Test Gözetimi ve Kontrolü
**"Her şey planlandığı gibi gidiyor mu?"**

* Testler sürekli izlenir
* Planlanan ile gerçekleşen karşılaştırılır
* Sapma varsa aksiyon alınır

> 💡 **Örnek:**
> - Plan: Haftada 50 test senaryosu koşulacak
> - Gerçek: 30 koşulabildi
> - Kontrol: Neden? → Test ortamı çöktü → Ortam düzeltildi, takvim güncellendi

---

## 3️⃣ Test Analizi
**"Ne test edilecek?"**

* Gereksinimler, kullanıcı hikayeleri incelenir
* Test koşulları belirlenir ve önceliklendirilir

> 💡 **Örnek — Instagram Story:**
> - Gereksinim: "Story 24 saat sonra silinmeli"
> - Test koşulları çıkarılır:
>   - Story yüklendi mi?
>   - 24 saat sonra silindi mi?
>   - Silmeden önce görüntülenebiliyor mu?
>   - Birden fazla story yüklenebiliyor mu?

---

## 4️⃣ Test Tasarımı
**"Nasıl test edilecek?"**

* Test koşulları → Detaylı test senaryolarına dönüştürülür
* Test verisi, ortam ve araçlar belirlenir

> 💡 **Örnek — Story Silme Senaryosu:**
> ```
> Senaryo: Story 24 saat sonra silinmeli
> Adımlar:
>   1. Kullanıcı story paylaşır
>   2. 24 saat beklenir (test ortamında simüle edilir)
>   3. Story'nin silindiği kontrol edilir
> Beklenen Sonuç: Story görünmüyor ✅
> ```

---

## 5️⃣ Test Uyarlama
**"Testler çalıştırmaya hazır mı?"**

* Test senaryoları → Çalıştırılabilir test betiklerine dönüştürülür
* Test ortamı kurulur ve doğrulanır
* Testler önceliklendirilip sıraya konur

> 💡 **Örnek:**
> - Selenium ile otomatik test betiği yazıldı
> - Test veritabanı hazırlandı (sahte kullanıcılar oluşturuldu)
> - Test ortamı kontrol edildi → "Ortam hazır" onayı alındı
> - Önce kritik testler, sonra diğerleri sıraya kondu

---

## 6️⃣ Test Koşumu
**"Sonuçlar ne?"**

* Testler çalıştırılır (manuel veya otomatik)
* Gerçek sonuçlar → Beklenen sonuçlarla karşılaştırılır
* Hatalar raporlanır

> 💡 **Örnek:**
> - Story silme testi çalıştırıldı
> - Beklenen: 24 saat sonra silinmeli
> - Gerçekleşen: Story hâlâ görünüyor ❌
> - Hata raporu oluşturuldu → Geliştiriciye iletildi

---

## 7️⃣ Test Tamamlama
**"Ne öğrendik, ne arşivleyelim?"**

* Faydalı test ürünleri arşivlenir
* Test ortamı kapatılır
* Tecrübeler analiz edilir → İyileştirme önerileri çıkarılır
* Test tamamlama raporu hazırlanır

> 💡 **Örnek:**
> - Bu sürümde 120 test koşuldu, 8 hata bulundu, 7'si düzeltildi
> - 1 hata bir sonraki sürüme ertelendi
> - Öğrenilen: "Zamanlayıcı içeren özellikler daha fazla test gerektiriyor"
> - Rapor yöneticiye iletildi ✅

---

## 🧠 Özet Tablo:

| Aktivite | Soru | Örnek Çıktı |
|---|---|---|
| **Planlama** | Ne yapacağız? | Test planı belgesi |
| **Gözetim/Kontrol** | Plan yürüyor mu? | Haftalık durum raporu |
| **Analiz** | Ne test edilecek? | Test koşulları listesi |
| **Tasarım** | Nasıl test edilecek? | Test senaryoları |
| **Uyarlama** | Testler hazır mı? | Otomatik test betikleri |
| **Koşum** | Sonuçlar ne? | Hata raporları |
| **Tamamlama** | Ne öğrendik? | Tamamlama raporu |



# Test Süreci Bağlama Bağlıdır

---

## 📌 Temel Fikir:

> Test **izole yapılmaz!**
> Test, yazılım geliştirme sürecinin **ayrılmaz bir parçasıdır**
> ve her projede **farklı şekilde** uygulanır.

---

## 🤔 Neden Farklı Uygulanır?

Çünkü her projenin **bağlamı farklıdır.** Şu faktörler testi doğrudan etkiler:

---

### 👥 1. Paydaşlar
* Müşteri ne istiyor?
* Beklentiler neler?
* Ne kadar iş birliği yapılabilir?

> 💡 Örnek: Müşteri "sadece giriş ekranı test edilsin" diyorsa kapsam daralır

---

### 👨‍💻 2. Ekip Üyeleri
* Test uzmanlarının deneyimi ne kadar?
* Otomasyon biliyor mu?
* Eğitime ihtiyaç var mı?

> 💡 Örnek: Ekipte otomasyon bilen kimse yoksa → Manuel test yapılır

---

### 🏢 3. Kurumun Faaliyet Alanı
* Yazılım ne kadar kritik?
* Yasal zorunluluklar var mı?

> 💡 Örnek:
> Hastane yazılımı → Çok sıkı test (hayat riski!)
> Yemek sipariş uygulaması → Daha esnek test

---

### 💻 4. Teknik Faktörler
* Hangi teknoloji kullanılıyor?
* Mimari nasıl?
* Web mi, mobil mi, API mi?

> 💡 Örnek: Mobil uygulama → Farklı cihazlarda test gerekir
> Web uygulaması → Farklı tarayıcılarda test gerekir

---

### ⏰ 5. Proje Kısıtları
* Zaman yeterli mi?
* Bütçe ne kadar?
* Kapsam ne?

> 💡 Örnek: 1 hafta kaldıysa → Sadece kritik özellikler test edilir
> 3 ay varsa → Kapsamlı test yapılabilir

---

### 🏗️ 6. Organizasyonel Faktörler
* Şirketin test politikası ne?
* Hangi süreçler kullanılıyor?

> 💡 Örnek: Şirket "her kod değişikliğinde regresyon testi zorunlu" diyorsa → Otomasyon şart

---

### 🔄 7. Yazılım Geliştirme Yaşam Döngüsü
* Agile mi, Waterfall mı?
* Scrum mu, Kanban mı?

> 💡 Örnek:
> Agile → Her sprint sonunda test
> Waterfall → Geliştirme bitince test

---

### 🔧 8. Araçlar
* Hangi test araçları mevcut?
* Lisans var mı?
* Ekip kullanabiliyor mu?

> 💡 Örnek: Selenium lisansı varsa → Web otomasyonu yapılır
> Yoksa → Manuel test

---

## 🎯 Bu Faktörler Neyi Etkiler?

| Faktör Değişince | Etkilenen Alan |
|---|---|
| Bütçe azalırsa | Test kapsamı daralır |
| Ekip deneyimliyse | Otomasyon artar |
| Kritik yazılımsa | Test detayı artar |
| Agile kullanılıyorsa | Test hızlanır, hafifler |
| Araç yoksa | Manuel test yapılır |

---

## 🧠 Tek Cümleyle:

> **Test evrensel değildir.**
> Her projede **bağlama göre şekillenir** →
> Kim yapıyor, ne zaman, hangi araçla, ne kadar detaylı → hepsi **bağlama göre değişir!**






============================


# Test Çalışma Ürünleri (Testware)

> Her test aktivitesinin bir **çıktısı** vardır. Bu çıktılara **test çalışma ürünleri** denir.

---

## 📋 1. Test Planlama Ürünleri

* 📄 **Test planı** → Tüm test sürecinin belgesi
* 📅 **Test zaman çizelgesi** → Ne zaman ne yapılacak
* ⚠️ **Risk kaydı** → Riskler, olasılıkları ve etkileri
* 🚦 **Giriş/Çıkış kriterleri** → Testin ne zaman başlayıp biteceği

---

## 👁️ 2. Test Gözetimi ve Kontrolü Ürünleri

* 📊 **Test ilerleme raporları** → Testler ne durumda?
* 📌 **Kontrol direktifleri** → Sapma varsa alınan aksiyonlar
* ⚠️ **Güncel risk bilgisi** → Riskler değişti mi?

---

## 🔍 3. Test Analizi Ürünleri

* ✅ **Test koşulları listesi** → Ne test edilecek? (önceliklendirilmiş)
* 🐛 **Hata raporu** → Gereksinim/belgelerde bulunan hatalar

---

## ✏️ 4. Test Tasarımı Ürünleri

* 📝 **Test senaryoları** → Adım adım test akışları (önceliklendirilmiş)
* 📂 **Test başlatma belgeleri** → Testi başlatmak için gerekli bilgiler
* 🎯 **Kapsam öğeleri** → Neyin kapsandığının listesi
* 🗃️ **Test verisi gereksinimleri** → Hangi verilerle test edilecek?
* 🖥️ **Test ortamı gereksinimleri** → Hangi ortam gerekli?

---

## 🔧 5. Test Uyarlama Ürünleri

* 📋 **Test prosedürleri** → Senaryoların adım adım uygulanma rehberi
* 🤖 **Otomatik test betikleri** → Selenium, Appium vb. ile yazılan kodlar
* 🖐️ **Manuel test betikleri** → Elle yapılan test adımları
* 📦 **Test grupları** → Bir arada çalıştırılan test setleri
* 🗄️ **Test verisi** → Gerçek test için hazırlanan veriler
* ⏱️ **Test koşum çizelgesi** → Hangi test ne zaman koşulacak?
* 🌐 **Test ortamı öğeleri** → Taklit uygulamalar, simülatörler, sürücüler

---

## ▶️ 6. Test Koşumu Ürünleri

* 📒 **Test kayıtları** → Hangi test koşuldu, sonuç ne oldu?
* 🐛 **Hata raporları** → Bulunan hatalar ve detayları

---

## ✅ 7. Test Tamamlama Ürünleri

* 📄 **Test tamamlama raporu** → Tüm sürecin özeti
* 💡 **İyileştirme önerileri** → Bir sonraki proje için dersler
* 📝 **Değişiklik talepleri** → Düzeltilmesi istenen maddeler

---

## 🧠 Özet Tablo:

| Aktivite | Üretilen Ürünler |
|---|---|
| **Planlama** | Test planı, risk kaydı, zaman çizelgesi |
| **Gözetim/Kontrol** | İlerleme raporları, kontrol direktifleri |
| **Analiz** | Test koşulları, hata raporu |
| **Tasarım** | Test senaryoları, test verisi gereksinimleri |
| **Uyarlama** | Test betikleri, test verisi, ortam |
| **Koşum** | Test kayıtları, hata raporları |
| **Tamamlama** | Tamamlama raporu, iyileştirme önerileri |

---

## 🏪 Gerçek Hayat Örneği — Trendyol "Sepete Ekle" Özelliği

> **Senaryo:** Bir e-ticaret şirketinde (Trendyol gibi) **"Sepete Ekle"** özelliği test ediliyor

---

### 📋 1. Test Planlama Ürünleri

Proje başladı, test ekibi oturup plan yapıyor:

* 📄 **Test Planı** → Confluence'a yazılan belge: "Sepete ekle özelliği 2 hafta test edilecek, 3 test uzmanı çalışacak"
* 📅 **Zaman Çizelgesi** → Jira'da oluşturulan takvim: "1. hafta manuel, 2. hafta otomasyon"
* ⚠️ **Risk Kaydı** → "Stok sıfırken ürün sepete eklenebilir mi? → Yüksek risk"
* 🚦 **Giriş Kriteri** → "Geliştirici kodu teslim etmeden test başlamaz"
* 🚦 **Çıkış Kriteri** → "Kritik hataların %100'ü kapatılmadan yayına alınmaz"

---

### 👁️ 2. Test Gözetimi ve Kontrolü Ürünleri

Test başladı, yönetici takip ediyor:

* 📊 **İlerleme Raporu** → Jira dashboard'unda: "50 senaryodan 30'u tamamlandı, 3 hata açık"
* 📌 **Kontrol Direktifi** → "Stok hatası kritik, diğer testleri bırak önce bunu çöz"
* ⚠️ **Güncel Risk** → "Mobil tarayıcıda da sorun çıktı, risk seviyesi yükseldi"

---

### 🔍 3. Test Analizi Ürünleri

Gereksinimler okunuyor, ne test edileceği belirleniyor:

* ✅ **Test Koşulları** → Confluence'a yazılan liste:
  * Ürün sepete eklendi mi?
  * Stok 0 iken eklenebiliyor mu?
  * Aynı ürün 2 kez eklenince adet artıyor mu?
  * Maksimum kaç adet eklenebilir?
* 🐛 **Hata Raporu** → "Gereksinimde maksimum adet yazılmamış!" → Jira'da açıldı

---

### ✏️ 4. Test Tasarımı Ürünleri

Test koşulları → Detaylı senaryolara dönüştürülüyor:

* 📝 **Test Senaryosu** → TestRail'e yazılan senaryo:
```
Senaryo: Stok 0 iken sepete ekle
Adım 1: Stoku 0 olan ürüne git
Adım 2: "Sepete Ekle" butonuna tıkla
Beklenen: "Stokta yok" uyarısı çıkmalı
```
* 🗃️ **Test Verisi Gereksinimleri** → "Stoku 0 olan 5 farklı ürün lazım"
* 🖥️ **Ortam Gereksinimleri** → "Chrome, Safari ve Android'de test edilmeli"

---

### 🔧 5. Test Uyarlama Ürünleri

Testler çalıştırmaya hazırlanıyor:

* 🤖 **Otomatik Test Betiği** → Selenium ile yazılan Python kodu:
```python
def test_add_to_cart():
    driver.find_element("sepete_ekle_btn").click()
    assert "Sepetim (1)" in driver.title
```
* 🗄️ **Test Verisi** → Excel'de hazırlanan liste: "Ürün ID: 1234, Stok: 0"
* 🌐 **Test Ortamı** → "test.trendyol.com" adresi ayarlandı, sahte kullanıcılar oluşturuldu
* ⏱️ **Koşum Çizelgesi** → "Önce stok testleri, sonra ödeme testleri"

---

### ▶️ 6. Test Koşumu Ürünleri

Testler çalıştırılıyor:

* 📒 **Test Kayıtları** → TestRail'de: "Senaryo #12 → ❌ BAŞARISIZ, Senaryo #13 → ✅ BAŞARILI"
* 🐛 **Hata Raporu** → Jira'da açılan ticket:
```
Başlık: Stok 0 iken ürün sepete eklenebiliyor
Öncelik: Kritik 🔴
Adımlar: Stoku 0 olan ürüne git → Sepete ekle
Beklenen: "Stokta yok" uyarısı
Gerçekleşen: Ürün sepete eklendi!
Ekran görüntüsü: screenshot.png
```

---

### ✅ 7. Test Tamamlama Ürünleri

Özellik yayına alındı, süreç kapatılıyor:

* 📄 **Tamamlama Raporu** → Confluence'a yazılan özet:
  * 50 senaryo koşuldu
  * 7 hata bulundu, 6'sı kapatıldı
  * 1 düşük öncelikli hata sonraki sprint'e ertelendi
* 💡 **İyileştirme Önerisi** → "Stok kontrolleri her zaman önce test edilmeli"
* 📝 **Değişiklik Talebi** → Jira'da yeni ticket: "Maksimum sepet adedi gereksinime eklenmeli"

---

## 🧠 Hangi Tool Ne İçin Kullanıldı?

| Tool | Ne İçin? |
|---|---|
| **Jira** | Hata raporları, proje takibi, zaman çizelgesi |
| **Confluence** | Test planı, tamamlama raporu, koşul listesi |
| **TestRail** | Test senaryoları, test kayıtları |
| **Selenium** | Otomatik test betikleri |
| **Excel** | Test verisi |



<br/>
<br/>
<br/>

-------------------
-------------------
-------------------
-------------------
-------------------
-------------------
-------------------
-------------------
-------------------
-------------------
-------------------
-------------------
-------------------
-------------------
-------------------
-------------------

-------------------

# SOZLUK

- **Kapsam öğeleri** (coverage items)= "Hangi alanları test edeceğiz?"