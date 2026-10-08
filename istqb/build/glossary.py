# -*- coding: utf-8 -*-
"""ISTQB CTFL v4.0 teknik terim sozlugu  (TR -> EN).

G: (tr, en) ciftleri.  Istege bagli ucuncu eleman, metinde aranacak
   govdeyi (stem) degistirir; varsayilan govde tr teriminin kendisidir.
   Govde, kelime basindan itibaren eslesir ve ardindan en fazla 10 harf
   (Turkce ekleri) gelebilir.
"""

import re

G = [
 # --- 1. Temeller --------------------------------------------------------
 ("test etme", "testing", "test etme"),
 ("test uzmanı", "tester", "test uzman"),
 ("test yöneticisi", "test manager", "test yönetici"),
 ("test nesnesi", "test object", "test nesne"),
 ("test esası", "test basis", "test esas"),
 ("test koşulu", "test condition", "test koşul"),
 ("test senaryosu", "test case", "test senaryo"),
 ("test prosedürü", "test procedure", "test prosedür"),
 ("test verisi", "test data", "test veri"),
 ("test sonucu", "test result", "test sonu"),
 ("test hedefi", "test objective", "test hedef"),
 ("test amacı", "test objective", "test amac"),
 ("test çalışma ürünü", "testware / test work product", "test çalışma ürün"),
 ("test süreci", "test process", "test süreci$|test sürecin|test süreçler|test süreci,$"),
 ("test analizi", "test analysis", "test analiz"),
 ("test tasarımı", "test design", "test tasarım"),
 ("test uyarlama", "test implementation", "test uyarlama"),
 ("test koşumu", "test execution", "test koşum"),
 ("test tamamlama", "test completion", "test tamamlama"),
 ("test planlama", "test planning", "test planlama"),
 ("test gözetimi", "test monitoring", "test gözetim"),
 ("test kontrolü", "test control", "test kontrol"),
 ("test ortamı", "test environment", "test ortam"),
 ("test takımı", "test suite", "test takım"),
 ("insan hatası", "error / mistake", "insan hata"),
 ("hata", "defect / fault / bug", "hata"),
 ("kusur", "defect", "kusur"),
 ("arıza", "failure", "arıza"),
 ("kök neden", "root cause", "kök neden"),
 ("hata ayıklama", "debugging", "hata ayıkla"),
 ("kalite", "quality", "kalite"),
 ("kalite güvence", "quality assurance (QA)", "kalite güvence"),
 ("kalite kontrol", "quality control", "kalite kontrol"),
 ("kapsam", "coverage", "kapsam"),
 ("kapsam öğesi", "coverage item", "kapsam öğe"),
 ("izlenebilirlik", "traceability", "izlenebilirlik"),
 ("doğrulama", "verification", "doğrula"),
 ("sağlama", "validation", "sağlama$|sağlamanın$|sağlamayı$|sağlamaya$|sağlamada$"),
 ("paydaş", "stakeholder", "paydaş"),
 ("gereksinim", "requirement", "gereksinim"),
 ("beklenen sonuç", "expected result", "beklenen sonu"),
 ("gerçek sonuç", "actual result", "gerçek sonu"),
 ("ön koşul", "precondition", "ön koşul"),
 ("hata yoğunluğu", "defect density", "hata yoğunlu"),
 ("hata kümelenmesi", "defect clustering", "kümelen"),
 ("pestisit paradoksu", "pesticide paradox", "pestisit"),
 ("kusursuzluk yanılgısı", "absence-of-defects fallacy", "yanılg"),
 ("ayrıntı düzeyi", "level of detail", "ayrıntı düzey"),
 ("önyargı", "bias", "önyargı"),
 ("bağımsızlık", "independence", "bağımsızlı"),
 ("iş analisti", "business analyst", "iş analist"),
 ("ürün sahibi", "product owner", "ürün sahib"),
 ("alan uzmanı", "domain expert", "alan uzman"),
 ("yaşam döngüsü", "lifecycle", "yaşam döngü"),
 ("yazılım geliştirme yaşam döngüsü", "software development lifecycle (SDLC)",
  "yazılım geliştirme yaşam döngü"),
 ("şelale modeli", "waterfall model", "şelale"),
 ("artımlı geliştirme", "incremental development", "artımlı"),
 ("yinelemeli geliştirme", "iterative development", "yineleme"),
 ("çevik", "agile", "çevik"),
 ("kullanıcı hikayesi", "user story", "kullanıcı hik"),
 ("test güdümlü geliştirme", "test-driven development (TDD)", "test güdümlü"),
 ("davranış güdümlü geliştirme", "behavior-driven development (BDD)", "davranış güdümlü"),
 ("kabul testi güdümlü geliştirme", "acceptance test-driven development (ATDD)",
  "kabul testi güdümlü"),
 ("shift-left", "shift left", "shift"),
 ("retrospektif", "retrospective", "retrospektif"),
 ("sürekli entegrasyon", "continuous integration (CI)", "sürekli entegrasyon"),
 ("sürekli teslimat", "continuous delivery (CD)", "sürekli tesl"),
 ("DevOps", "DevOps", "devops"),

 # --- 2. Test seviyeleri ve cesitleri -----------------------------------
 ("test seviyesi", "test level", "test seviye"),
 ("test çeşidi", "test type", "test çeşid"),
 ("bileşen testi", "component testing / unit testing", "bileşen test"),
 ("birim testi", "unit testing", "birim test"),
 ("bileşen entegrasyon testi", "component integration testing", "bileşen entegrasyon"),
 ("entegrasyon testi", "integration testing", "entegrasyon test"),
 ("sistem testi", "system testing", "sistem test"),
 ("sistem entegrasyon testi", "system integration testing", "sistem entegrasyon"),
 ("kabul testi", "acceptance testing", "kabul test"),
 ("kullanıcı kabul testi", "user acceptance testing (UAT)", "kullanıcı kabul"),
 ("operasyonel kabul testi", "operational acceptance testing", "operasyonel kabul"),
 ("alfa testi", "alpha testing", "alfa test"),
 ("beta testi", "beta testing", "beta test"),
 ("fonksiyonel test", "functional testing", "fonksiyonel test"),
 ("fonksiyonel olmayan test", "non-functional testing", "fonksiyonel olmayan"),
 ("kara kutu testi", "black-box testing", "kara kutu"),
 ("beyaz kutu testi", "white-box testing", "beyaz kutu"),
 ("onaylama testi", "confirmation testing / re-testing", "onaylama test"),
 ("regresyon testi", "regression testing", "regresyon"),
 ("bakım testi", "maintenance testing", "bakım test"),
 ("duman testi", "smoke testing", "duman test"),
 ("etki analizi", "impact analysis", "etki analiz"),
 ("performans verimliliği", "performance efficiency", "performans verimlili"),
 ("kullanılabilirlik", "usability", "kullanılabilirlik"),
 ("güvenilirlik", "reliability", "güvenilirlik"),
 ("taşınabilirlik", "portability", "taşınabilirlik"),
 ("sürdürülebilirlik", "maintainability", "sürdürülebilirlik"),
 ("uyumluluk", "compatibility", "uyumluluk"),
 ("güvenlik", "security", "güvenlik"),
 ("yük testi", "load testing", "yük test"),
 ("sürdürülebilirlik", "maintainability", "sürdürülebilir"),
 ("sürücü", "driver / test driver", "sürücü"),
 ("servis sanallaştırma", "service virtualization", "servis sanal"),
 ("arayüz", "interface", "arayüz"),
 ("sürüm", "release / version", "sürüm"),

 # --- 3. Statik test ----------------------------------------------------
 ("statik test", "static testing", "statik test"),
 ("dinamik test", "dynamic testing", "dinamik test"),
 ("statik analiz", "static analysis", "statik analiz"),
 ("gözden geçirme", "review", "gözden geçir"),
 ("resmi gözden geçirme", "formal review", "resmi gözden"),
 ("gayri resmi gözden geçirme", "informal review", "gayri resmi"),
 ("teknik gözden geçirme", "technical review", "teknik gözden"),
 ("üzerinden geçme", "walkthrough", "üzerinden geçme"),
 ("teftiş", "inspection", "teftiş"),
 ("anomali", "anomaly", "anomali"),
 ("gözden geçiren", "reviewer", "gözden geçiren"),
 ("moderatör", "moderator / facilitator", "moderatör"),
 ("kolaylaştırıcı", "facilitator", "kolaylaştırıcı"),
 ("yazar", "author", "yazar$|yazarı$|yazarın$|yazarlar$|yazarları$|yazarların$|yazarlarının$"),
 ("yazman", "scribe", "yazman"),
 ("gözden geçirme lideri", "review leader", "gözden geçirme lider"),
 ("geri bildirim", "feedback", "geri bildirim"),

 # --- 4. Test teknikleri ------------------------------------------------
 ("test tekniği", "test technique", "test tekni"),
 ("kara kutu test tekniği", "black-box test technique", "kara kutu test tekni"),
 ("beyaz kutu test tekniği", "white-box test technique", "beyaz kutu test tekni"),
 ("tecrübeye dayalı test tekniği", "experience-based test technique", "tecrübeye dayalı"),
 ("denklik paylarına ayırma", "equivalence partitioning (EP)", "denklik pay"),
 ("denklik payı", "equivalence partition", "denklik pay"),
 ("geçerli pay", "valid partition", "geçerli pay"),
 ("geçersiz pay", "invalid partition", "geçersiz pay"),
 ("sınır değer analizi", "boundary value analysis (BVA)", "sınır değer"),
 ("2 değerli SDA", "2-value boundary value analysis", "2 değerli"),
 ("3 değerli SDA", "3-value boundary value analysis", "3 değerli"),
 ("karar tablosu testi", "decision table testing", "karar tablo"),
 ("eylem", "action", "eylem"),
 ("kural", "rule", "kural"),
 ("durum geçişi testi", "state transition testing", "durum geçiş"),
 ("durum geçiş diyagramı", "state transition diagram", "durum geçiş diyagram"),
 ("durum geçiş tablosu", "state transition table", "durum geçiş tablo"),
 ("geçerli geçiş", "valid transition", "geçerli geçiş"),
 ("geçersiz geçiş", "invalid transition", "geçersiz geçiş"),
 ("komut kapsama yüzdesi", "statement coverage", "komut kapsa"),
 ("dal kapsamı", "branch coverage", "dal kapsa"),
 ("hata tahminleme", "error guessing", "hata tahmin"),
 ("keşif testi", "exploratory testing", "keşif test"),
 ("test tüzüğü", "test charter", "test tüzü"),
 ("oturum bazlı test", "session-based testing", "oturum"),
 ("kontrol listesine dayalı test", "checklist-based testing", "kontrol liste"),
 ("iş birliğine dayalı test yaklaşımı", "collaboration-based test approach", "iş birliğine dayalı"),
 ("kabul kriterleri", "acceptance criteria", "kabul kriter"),

 # --- 5. Test yonetimi --------------------------------------------------
 ("test planı", "test plan", "test plan"),
 ("test yaklaşımı", "test approach", "test yaklaşım"),
 ("test stratejisi", "test strategy", "test strateji"),
 ("giriş kriterleri", "entry criteria / definition of ready", "giriş kriter"),
 ("çıkış kriterleri", "exit criteria / definition of done", "çıkış kriter"),
 ("test piramidi", "test pyramid", "test piramid"),
 ("test çeyrekleri", "testing quadrants", "test çeyre"),
 ("risk", "risk", "risk"),
 ("ürün riski", "product risk", "ürün risk"),
 ("proje riski", "project risk", "proje risk"),
 ("risk yönetimi", "risk management", "risk yönetim"),
 ("risk analizi", "risk analysis", "risk analiz"),
 ("risk belirleme", "risk identification", "risk belirleme"),
 ("risk değerlendirmesi", "risk assessment", "risk değerlendir"),
 ("risk kontrolü", "risk control", "risk kontrol"),
 ("risk azaltma", "risk mitigation", "risk azalt"),
 ("risk gözetimi", "risk monitoring", "risk gözetim"),
 ("risk seviyesi", "risk level", "risk seviye"),
 ("risk bazlı test", "risk-based testing", "risk bazlı"),
 ("olasılık", "likelihood / probability", "olasılı"),
 ("etki", "impact", "etki$|etkisi$|etkisini$|etkileri$|etkisinin$|etkiye$"),
 ("etki analizi", "impact analysis", "etki analiz"),
 ("acil durum planı", "contingency plan", "acil durum"),
 ("test ilerleme raporu", "test progress report", "test ilerleme"),
 ("test tamamlama raporu", "test completion report", "test tamamlama rapor"),
 ("ölçüt", "metric", "ölçüt"),
 ("tahminleme", "estimation", "tahminleme"),
 ("ekstrapolasyon", "extrapolation", "ekstrapolasyon"),
 ("Wideband Delphi", "Wideband Delphi (uzman tahmini)", "wideband"),
 ("planlama pokeri", "planning poker", "poker"),
 ("üç noktalı tahmin", "three-point estimation", "üç nokta"),
 ("burndown grafiği", "burndown chart", "burndown"),
 ("kontrol panosu", "dashboard", "pano"),
 ("hata yönetimi", "defect management", "hata yönetim"),
 ("hata raporu", "defect report", "hata rapor"),
 ("yapılandırma yönetimi", "configuration management", "yapılandırma yönetim"),
 ("sürüm kontrolü", "version control", "sürüm kontrol"),
 ("temel çizgi", "baseline", "temel çizgi"),
 ("yapılandırma öğesi", "configuration item", "yapılandırma öğe"),
 ("iş değeri", "business value", "iş değer"),
 ("öncelik", "priority", "öncelik"),
 ("önem derecesi", "severity", "önem derece"),
 ("kalan hata", "residual defect", "kalan hata"),

 # --- 6. Araclar --------------------------------------------------------
 ("SDA", "BVA — boundary value analysis", "sda"),
 ("DPA", "EP — equivalence partitioning", "dpa"),
 ("ifade kapsamı", "statement coverage", "ifade kapsa"),
 ("Tamamlandı Tanımı", "definition of done (DoD)", "tamamlandı tanım"),
 ("sprint", "sprint", "sprint"),
 ("INVEST", "INVEST (kullanıcı hikayesi ölçütü)", "invest"),
 ("test otomasyonu", "test automation", "test otomasyon"),
 ("test aracı", "test tool", "test arac"),
 ("betik", "script", "betik"),
 ("pilot proje", "pilot project", "pilot"),
 ("yatırım getirisi", "return on investment (ROI)", "yatırım"),
]

def tlow(s):
    return s.replace(u"I", u"ı").replace(u"İ", u"i").lower()

def _rx(stem):
    alts = []
    for part in stem.split("|"):
        p = part.strip()
        if p.endswith("$"):
            alts.append(re.escape(p[:-1]) + r"(?![0-9a-zçğıöşü])")
        else:
            alts.append(re.escape(p) + r"[a-zçğıöşü]{0,10}(?![0-9a-zçğıöşü])")
    return re.compile(r"(?<![0-9a-zçğıöşü])(?:" + "|".join(alts) + ")")

TERMS = []
for e in G:
    tr, en = e[0], e[1]
    stem = tlow(e[2] if len(e) > 2 else tr)
    TERMS.append((tr, en, _rx(stem)))

# gozden gecirme rolleri yalnizca 3. konuda anlamli
ONLY_CH = {u"moderatör": "3", u"kolaylaştırıcı": "3", u"yazman": "3",
           u"gözden geçiren": "3", u"gözden geçirme lideri": "3"}

def find(text, ch=None):
    t = tlow(text)
    out = []
    for tr, en, rx in TERMS:
        if ch and tr in ONLY_CH and ONLY_CH[tr] != ch: continue
        if rx.search(t): out.append((tr, en))
    return out
