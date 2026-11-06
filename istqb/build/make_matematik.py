# -*- coding: utf-8 -*-
"""deniz/konular/matematik.html — ISTQB sinavinda cikan aritmetik calisma sayfasi"""
import io, re
from fractions import Fraction

CSS   = io.open("css.txt", encoding="utf-8").read()
HEAD  = io.open("head.txt", encoding="utf-8").read()
GATE  = io.open("gate.txt", encoding="utf-8").read()
CRUMB = io.open("crumb.txt", encoding="utf-8").read()
CRUMB = re.sub(r'<li><span aria-current="page">.*?</span></li>',
               '<li><span aria-current="page">Sınav Matematiği</span></li>',
               CRUMB, count=1, flags=re.S)

def pc(num, den, nd=1):
    """yuzdeyi sinavdaki gibi yaz: tam sayiysa tam, degilse virgullu"""
    v = 100.0 * num / den
    r = round(v, nd)
    return ("%d" % r) if abs(r - round(r)) < 1e-9 else (("%.*f" % (nd, r)).replace(".", ","))

# ---------------- 1. kesir -> yuzde tablosu ----------------
DENS = [2, 3, 4, 5, 6, 8, 10, 12]
def fractable():
    rows = []
    for d in DENS:
        cells = []
        for n in range(1, d):
            f = Fraction(n, d)
            cells.append('<td><b>%d/%d</b><span>%%%s</span></td>' % (n, d, pc(n, d)))
        rows.append('<tr><th>/%d</th>%s</tr>' % (d, "".join(cells)))
    return ('<div class="scroll"><table class="dt frk"><tbody>%s</tbody></table></div>'
            % "".join(rows))

# ---------------- alistirmalar ----------------
A = [(4,6),(3,8),(6,8),(4,5),(5,8),(2,4),(3,5),(7,8),(2,3),(5,6),
     (3,12),(9,12),(2,5),(1,6),(7,10),(4,8),(1,3),(5,12)]
B = [("a × 3/9 = 200", "a = 200 × 9/3", 600, "Payla böl, paydayla çarp — kesri ters çevirip geçir."),
     ("a × 2/5 = 80",  "a = 80 × 5/2",  200, "Aynı kural: 80 ÷ 2 = 40, 40 × 5 = 200."),
     ("a × 4/7 = 28",  "a = 28 × 7/4",  49,  "28 ÷ 4 = 7, 7 × 7 = 49."),
     ("3/4 × a = 150", "a = 150 × 4/3", 200, "Sıra önemli değil, çarpma yer değiştirir."),
     ("a / 6 = 7,5",   "a = 7,5 × 6",   45,  "Bölmenin tersi çarpma."),
     ("%25 × a = 90",  "a = 90 × 4",    360, "%25 = 1/4, tersi ×4."),
     ("%60 × a = 120", "a = 120 ÷ 0,6", 200, "Ya da 120 × 100/60."),
     ("a × 5/8 = 250", "a = 250 × 8/5", 400, "250 ÷ 5 = 50, 50 × 8 = 400.")]
C = [("8 sınırın 6'sı test edildi", 6, 8),
     ("5 payın 4'ü kapsandı",       4, 5),
     ("12 sütunun 3'ü çalıştırıldı",3,12),
     ("20 geçişin 7'si denendi",    7,20),
     ("6 komutun 4'ü yürütüldü",    4, 6),
     ("8 dalın 5'i alındı",         5, 8)]

def ans_pc(n, d): return "%%%s  (%d/%d)" % (pc(n, d), n, d)

def drillA():
    return ('<div class="scroll"><table class="dt drill"><thead><tr>'
            '<th>#</th><th>Kesir</th><th class="ctr">Yüzde</th>'
            '<th>#</th><th>Kesir</th><th class="ctr">Yüzde</th></tr></thead><tbody>'
            + "".join('<tr><td class="qn">%d</td><td><b>%d / %d</b></td><td class="ctr bl"></td>'
                      '<td class="qn">%d</td><td><b>%d / %d</b></td><td class="ctr bl"></td></tr>'
                      % (i+1, A[i][0], A[i][1], i+1+len(A)//2, A[i+len(A)//2][0], A[i+len(A)//2][1])
                      for i in range(len(A)//2))
            + '</tbody></table></div>')

def drillB():
    return ('<ol class="dr">' + "".join(
        '<li><code>%s</code><span class="bl w"></span></li>' % q for q, _, _, _ in B) + '</ol>')

def drillC():
    return ('<ol class="dr">' + "".join(
        '<li>%s &rarr; kapsam?<span class="bl w"></span></li>' % t for t, _, _ in C) + '</ol>')

D = [("Üç noktalı tahmin", "En iyi 2, en olası 5, en kötü 14 saat. Tek test için tahmin?",
      "(2 + 4×5 + 14) / 6 = 36/6", "6 saat"),
     ("Üç noktalı + adet", "En iyi 1, en olası 3, en kötü 8 saat. <b>Dört</b> test için?",
      "(1 + 12 + 8)/6 = 3,5 → 3,5 × 4", "14 saat"),
     ("Orana dayalı tahmin", "Geçmiş: toplam geliştirme 3.600.000 $, toplam test 360.000 $. "
      "Yeni projenin geliştirmesi 800.000 $. Test eforu?",
      "oran = 360.000/3.600.000 = 0,10 → 800.000 × 0,10", "80.000 $"),
     ("Ekstrapolasyon", "E(n) = (3×A(n−1) + A(n−2)) / 4. A(4)=6, A(3)=8. E(5)?",
      "(3×6 + 8)/4 = 26/4", "6,5"),
     ("Risk seviyesi", "Olasılık %50, etki 2.000 $. Risk seviyesi?",
      "0,50 × 2.000", "1.000 $"),
     ("Risk — ters hesap", "Risk seviyesi 1.000 $, olasılık %50. Etki?",
      "1.000 ÷ 0,50", "2.000 $"),
     ("Karar tablosu", "3 evet/hayır koşulu. Tam tabloda kaç sütun?",
      "2³", "8 sütun"),
     ("Karar tablosu kapsamı", "8 sütunlu tabloda 3 farklı sütun çalıştırıldı.",
      "3/8", "%37,5"),
     ("Sınır sayısı", "4 bitişik pay, iki uç da kapalı. 2-değerli sınır sayısı?",
      "4 × 2 − 0", "8 sınır"),
     ("Durum geçişi", "5 durum, 4 olay. Tüm geçiş kapsamının paydası?",
      "5 × 4", "20 hücre"),
     ("Geçerli geçiş kapsamı", "6 geçerli geçişin 4'ü denendi.",
      "4/6", "%66,7"),
     ("Each Choice", "Paylar 3, 2 ve 4. %100 için en az kaç test?",
      "max(3, 2, 4)", "4 test")]

def drillD():
    return ('<ol class="dr big">' + "".join(
        '<li><b>%s</b><span class="qq">%s</span><span class="bl w"></span></li>' % (t, q)
        for t, q, _, _ in D) + '</ol>')

def keyA():
    return ('<div class="kg">' + "".join(
        '<span><i>%d.</i> %s</span>' % (i+1, ans_pc(n, d)) for i, (n, d) in enumerate(A)) + '</div>')
def keyB():
    return ('<div class="kg wide">' + "".join(
        '<span><i>%d.</i> <b>%s</b> &nbsp;%s &nbsp;<em>%s</em></span>' % (i+1, r, w, note)
        for i, (q, w, r, note) in enumerate(B)) + '</div>')
def keyC():
    return ('<div class="kg">' + "".join(
        '<span><i>%d.</i> %s</span>' % (i+1, ans_pc(n, d)) for i, (t, n, d) in enumerate(C)) + '</div>')
def keyD():
    return ('<div class="kg wide">' + "".join(
        '<span><i>%d.</i> <b>%s</b> &nbsp;<em>%s</em></span>' % (i+1, r, w)
        for i, (t, q, w, r) in enumerate(D)) + '</div>')

SEC = [("Neden bu sayfa", "320 sorunun 69'unda aritmetik var"),
       ("Kesir &rarr; y&uuml;zde", "Ezberlenecek tablo &middot; sınavda çıkan paydalar"),
       ("B&ouml;lme ve yuvarlama", "Hesap makinesi yok &middot; uzun bölme"),
       ("Bilinmeyeni bulma", "a × 3/9 = 200 tipinde denklemler"),
       ("Oran ve orantı", "FL-5.1.4 &middot; orana dayalı tahmin"),
       ("Sınavın altı form&uuml;l&uuml;", "Kapsam, sınır, sütun, geçiş, efor, risk"),
       ("Alıştırma A &mdash; kesirler", "18 soru &middot; kafadan"),
       ("Alıştırma B &mdash; denklemler", "8 soru &middot; bilinmeyeni çek"),
       ("Alıştırma C &mdash; kapsam", "6 soru &middot; payda + bölme"),
       ("Alıştırma D &mdash; form&uuml;ller", "12 soru &middot; sınav biçiminde"),
       ("Cevap anahtarı", "Önce çöz, sonra bak")]
IDS = ["s%d" % (i+1) for i in range(len(SEC))]
JUMP = "".join('<a href="#%s"><span class="n">%d</span><b>%s</b></a>' % (IDS[i], i+1, t)
               for i, (t, _) in enumerate(SEC))
NAV  = "".join('<a href="#%s">%d. %s</a>' % (IDS[i], i+1, t) for i, (t, _) in enumerate(SEC))

def sec(i, title, lo, body):
    return ('<section id="%s"><div class="shead"><div class="num">%d</div>'
            '<div><h2>%s</h2><div class="lo">%s</div></div></div>%s</section>'
            % (IDS[i], i+1, title, lo, body))

# ---------------- bolum govdeleri ----------------
S1 = """
<p class="lead">320 sorunun <b>69'unda</b> bir aritmetik adım var — payı paydaya bölmek, yüzdeye
çevirmek, bilinmeyeni çekmek ya da bir oranı uygulamak. Konuyu bilip işlemde kaybetmek
sınavda en can sıkıcı puan kaybı.</p>
<div class="recog"><b>Sınavda hesap makinesi yok.</b> Ama ihtiyacın olan matematik ilkokul
seviyesinde: dört işlem, kesir, yüzde, basit orantı. Zor olan tarafı, bunları <i>hızlı</i> ve
<i>hatasız</i> yapmak. Bu sayfa tam olarak sınavda çıkan sayıları çalıştırıyor.</div>
<div class="scroll"><table class="dt"><thead><tr><th>Hangi hesap</th><th class="ctr">Kaç soruda</th><th>Nerede çıkıyor</th></tr></thead><tbody>
<tr><td>Kapsam yüzdesi (pay / payda)</td><td class="ctr"><b>38</b></td><td>4.2 · 4.3 — denklik payı, sınır değer, karar tablosu, durum geçişi, komut/dal</td></tr>
<tr><td>Efor tahmini (adam-gün, $)</td><td class="ctr"><b>15</b></td><td>5.1.4 — üç noktalı, orana dayalı, ekstrapolasyon</td></tr>
<tr><td>Oran ve orantı</td><td class="ctr"><b>9</b></td><td>5.1.4 · 4.2 — geçmiş projeden yeni projeye</td></tr>
<tr><td>Risk seviyesi (olasılık × etki)</td><td class="ctr"><b>5</b></td><td>5.2.1</td></tr>
<tr><td>Sayma: sınır, pay, geçiş, sütun</td><td class="ctr"><b>5</b></td><td>4.2 — paydayı kurmak</td></tr>
</tbody></table></div>
<div class="card key"><h3>Altın kural</h3><p>Sınavdaki her yüzde sorusu aynı iki adımdan oluşur:
<b>paydayı kur</b>, sonra <b>payı say</b>. Hata neredeyse her zaman birinci adımda olur —
aritmetikte değil. Önce "kaç tane var?" sorusunu doğru cevapla.</p></div>
"""

S2 = """
<p class="lead">Aşağıdaki tablo sınavda gerçekten çıkan paydaları kapsıyor. Sınav sorularındaki
şıklar bu kümeden geliyor: %12,5 · %25 · %33,3 · %37,5 · %50 · %60 · %62,5 · %66,7 · %75 · %80 · %87,5.
Bunları ezberlersen bölme yapmana çoğu zaman gerek kalmaz.</p>
""" + fractable() + """
<div class="fgrid">
  <div class="fbox"><h4>/2 ve /4 ve /8</h4><p>Hepsi yarıya bölmekten çıkar:
  <code>1/2 = %50</code> → yarısı <code>1/4 = %25</code> → yarısı <code>1/8 = %12,5</code>.
  Gerisi toplama: <code>3/8 = 25 + 12,5 = %37,5</code>, <code>5/8 = 50 + 12,5 = %62,5</code>.</p></div>
  <div class="fbox"><h4>/5 ve /10</h4><p>En kolayı: <code>1/5 = %20</code>, say git —
  40, 60, 80. <code>1/10 = %10</code>.</p></div>
  <div class="fbox"><h4>/3 ve /6</h4><p>Devirli: <code>1/3 = %33,3</code>, <code>2/3 = %66,7</code>.
  Altıda birler bunun yarısı: <code>1/6 = %16,7</code>, <code>5/6 = %83,3</code>.</p></div>
  <div class="fbox"><h4>/12</h4><p>Karar tablolarında çıkar. <code>1/12 = %8,3</code>,
  <code>3/12 = 1/4 = %25</code>, <code>6/12 = %50</code>, <code>9/12 = %75</code>. Önce sadeleştir.</p></div>
</div>
<div class="card trap"><h3>Tuzak</h3><p>Şıklarda <b>%66,7 ve %67 birlikte</b> bulunabilir;
ikisi de doğrudur, soru hangisini yazdıysa o. Aynı şekilde %33,3 / %33 ve %83,3 / %83.
Hesabın doğruysa en yakın şıkkı seç, ikinci bir hesap yapma.</p></div>
"""

S3 = """
<p class="lead">Elinde hesap makinesi yokken <code>2/7</code> gibi bir bölmeyi yapmanın yolu
uzun bölme. Yüzdeye çevirmek için paya <b>önce 100 ekle</b>, sonra böl — ondalıkla uğraşmazsın.</p>
<pre class="fx">yüzde = pay × 100 ÷ payda        (ters sıra daha zor: 2 ÷ 7 = 0,2857… → ×100)

2/7  →  2 × 100 = 200  →  200 ÷ 7
        7 × 20 = 140   kalan 60
        7 × 8  = 56    kalan 4      →  28, kalan 4
        4 → 40,  7 × 5 = 35          →  28,5…
                                      2/7 ≈ %28,6</pre>
<div class="card"><h3>Uzun bölmeyi adım adım</h3>
<ol class="steps">
  <li><b>Payı 100 ile çarp</b><div>Virgülle hiç uğraşma. <code>3/8</code> → <code>300 ÷ 8</code>.</div></li>
  <li><b>Paydanın katlarını çıkar</b><div><code>8 × 30 = 240</code>, kalan 60. <code>8 × 7 = 56</code>, kalan 4.
    Buraya kadar <b>37</b>.</div></li>
  <li><b>Kalan varsa virgülden sonrasına geç</b><div>Kalan 4'ü 40 yap: <code>8 × 5 = 40</code>, tam bölündü.
    Sonuç <b>%37,5</b>.</div></li>
  <li><b>Kalan devrediyorsa dur</b><div><code>200 ÷ 3 = 66,66…</code> → üçüncü haneye bakma,
    <b>%66,7</b> yaz. Şıklar zaten bir ondalıktan fazlasını vermez.</div></li>
</ol></div>
<div class="card warnc"><h3>Yuvarlama</h3><p>Virgülden sonraki ikinci hane 5 ve üzeriyse yukarı:
<code>66,66 → 66,7</code>. Sınav şıkları genelde bir ondalık basamak kullanır; iki şık arasında
0,1'lik fark varsa hesabını bir kez daha kontrol et, çünkü biri yuvarlamadan değil
<b>yanlış paydadan</b> gelmiştir.</p></div>
"""

S4 = """
<p class="lead">"<code>a × 3/9 = 200</code>, a kaçtır?" tipindeki sorular. Tek kural var:
<b>kesri karşı tarafa ters çevirerek geçir.</b></p>
<pre class="fx">a × 3/9 = 200
        ↓   kesri ters çevirip sağa geçir
a = 200 × 9/3  =  200 × 3  =  600

kontrol:  600 × 3/9 = 600 ÷ 9 × 3 = 66,67 × 3 ≈ 200  ✔</pre>
<div class="scroll"><table class="dt"><thead><tr><th>Denklem</th><th>Ne yaparsın</th><th class="ctr">Sonuç</th></tr></thead><tbody>
<tr><td><code>a × 3/9 = 200</code></td><td>×<b>9/3</b> ile geçir</td><td class="ctr"><b>600</b></td></tr>
<tr><td><code>a / 4 = 25</code></td><td>Bölmenin tersi <b>çarpma</b></td><td class="ctr"><b>100</b></td></tr>
<tr><td><code>a × 0,25 = 90</code></td><td>0,25 = 1/4 → <b>×4</b></td><td class="ctr"><b>360</b></td></tr>
<tr><td><code>%40 × a = 120</code></td><td><b>÷0,4</b> ya da ×100/40</td><td class="ctr"><b>300</b></td></tr>
<tr><td><code>a/8 = %37,5</code></td><td>Yüzdeyi kesre çevir: 3/8 → <b>a = 3</b></td><td class="ctr"><b>3</b></td></tr>
</tbody></table></div>
<div class="card key"><h3>Sadeleştir, sonra çarp</h3><p><code>200 × 9/3</code> işleminde önce
<b>9/3 = 3</b> yap, sonra <code>200 × 3</code>. Büyük sayıyı 9 ile çarpıp 3'e bölmek
daha çok hata üretir. Her zaman önce kesri sadeleştir.</p></div>
<div class="card trap"><h3>Sınavdaki gerçek hâli</h3><p>Bu hesap karşına "risk seviyesi 1.000 $,
olasılık %50, etki nedir?" diye çıkar. Formül <code>risk = olasılık × etki</code>; bilinmeyen
etki olduğunda <code>etki = risk ÷ olasılık = 1.000 ÷ 0,5 = 2.000 $</code>.</p></div>
"""

S5 = """
<p class="lead">Orana dayalı tahminde (5.1.4) bütün mesele <b>hangi iki sayının oranı</b>
alınacağını doğru seçmek. İşlem zaten tek bölme.</p>
<pre class="fx">oran        = toplam test eforu ÷ toplam geliştirme eforu
yeni tahmin = yeni geliştirme eforu × oran</pre>
<div class="scroll"><table class="dt"><thead><tr><th>Proje</th><th class="ctr">Geliştirme</th><th class="ctr">Test</th><th class="ctr">Oranı</th></tr></thead><tbody>
<tr><td>P1</td><td class="ctr">800.000</td><td class="ctr">40.000</td><td class="ctr">%5</td></tr>
<tr><td>P2</td><td class="ctr">1.200.000</td><td class="ctr">130.000</td><td class="ctr">%10,8</td></tr>
<tr><td>P3</td><td class="ctr">600.000</td><td class="ctr">70.000</td><td class="ctr">%11,7</td></tr>
<tr><td>P4</td><td class="ctr">1.000.000</td><td class="ctr">120.000</td><td class="ctr">%12</td></tr>
<tr><td><b>Toplam</b></td><td class="ctr"><b>3.600.000</b></td><td class="ctr"><b>360.000</b></td><td class="ctr"><b>%10</b></td></tr>
</tbody></table></div>
<pre class="fx">ortalamaların oranı : 90.000 / 900.000 = 0,10   →  800.000 × 0,10 = 80.000 $   ✔
oranların ortalaması: (5 + 10,8 + 11,7 + 12)/4 = %9,875 → 79.000 $            ✘</pre>
<div class="card trap"><h3>İki farklı sonuç veren iki yol</h3><p>Soru "<b>ortalamaları kullanarak</b>"
diyorsa toplamı toplama bölersin. "Her projenin oranını" deseydi oranların ortalamasını alırdın.
Sayılar birbirine yakın çıktığı için yanlış yolu seçtiğini fark etmeyebilirsin —
<b>soruda hangi ortalamanın istendiğini işaretle.</b></p></div>
<div class="card key"><h3>Kısayol</h3><p>Toplam/toplam oranı çoğu soruda <b>yuvarlak bir sayı</b>
çıkacak şekilde kurulmuştur (%10, %12,5, %20). Hesabın küsuratlıysa büyük ihtimalle
yanlış sütunları topladın.</p></div>
"""

S6 = """
<p class="lead">Sınavda hesap gerektiren her şey şu altı formülden birine iner.
Hepsini bir karta yazıp ezberle.</p>
<div class="fgrid">
  <div class="fbox"><h4>Kapsam yüzdesi</h4>
    <pre class="fx">% = çalıştırılan kapsam öğesi
    ────────────────── × 100
      toplam kapsam öğesi</pre>
    <p>Kapsam öğesi tekniğe göre değişir: <b>pay</b> (EP), <b>sınır değer</b> (BVA),
    <b>sütun</b> (karar tablosu), <b>geçiş</b> (durum geçişi), <b>komut/dal</b> (beyaz kutu).</p></div>
  <div class="fbox"><h4>Sınır sayısı — 2 değerli</h4>
    <pre class="fx">sınır = pay sayısı × 2 − açık uç sayısı</pre>
    <p>Dört bitişik pay, iki uç kapalı → <code>4×2 − 0 = 8</code>. Üst uç açıksa 7.</p></div>
  <div class="fbox"><h4>Karar tablosu</h4>
    <pre class="fx">tam tablo sütunu = 2ⁿ   (n = evet/hayır koşulu)</pre>
    <p>2³ = 8, 2⁴ = 16. <b>Ama</b> sadeleştirilmiş tabloda payda tablonun kendi sütun sayısıdır — say.</p></div>
  <div class="fbox"><h4>Durum geçişi</h4>
    <pre class="fx">tüm geçiş = durum sayısı × olay sayısı
geçerli geçiş = tablodaki dolu hücreler</pre>
    <p>5 durum × 4 olay = 20 hücre. Soru hangisini istiyorsa onun paydasını kullan.</p></div>
  <div class="fbox"><h4>Üç noktalı tahmin</h4>
    <pre class="fx">E = (a + 4m + b) / 6
a = en iyi, m = en olası, b = en kötü</pre>
    <p>Birden çok test isteniyorsa <b>sonucu adetle çarpmayı unutma</b>.</p></div>
  <div class="fbox"><h4>Risk seviyesi</h4>
    <pre class="fx">risk = olasılık × etki</pre>
    <p>Bilinmeyen etkiyse böl. Olasılık yüzdeyse önce ondalığa çevir: %50 → 0,5.</p></div>
</div>
<div class="card warnc"><h3>Ekstrapolasyon</h3><p>Soruda formül <b>verilir</b>, ezberlemene gerek yok.
Tek iş indisleri doğru okumak: <code>E(5) = (3×A(4) + A(3)) / 4</code> — <b>A</b> gerçekleşen,
<b>E</b> tahmin. Tabloda iki sütun da vardır; yanlış sütunu okumak hazır bir çeldiriciye düşürür.</p></div>
"""

S7 = '<p class="lead">Kafadan yap, yanına yaz. Hepsi sınavda çıkan paydalar.</p>' + drillA()
S8 = ('<p class="lead">Bilinmeyeni çek. Yanına hem sonucu hem işlemi yaz.</p>' + drillB()
      + '<div class="card"><h3>Hatırlatma</h3><p>Kesri karşıya ters çevirerek geçir, '
        'sonra <b>önce sadeleştir</b>, sonra çarp.</p></div>')
S9 = ('<p class="lead">Önce paydayı söyle, sonra böl. Her biri tek satır.</p>' + drillC())
S10 = ('<p class="lead">Sınavdaki hâliyle. İşlemi de yaz, sadece sonucu değil.</p>' + drillD())

S11 = ('<p class="lead">Önce kendin çöz, sonra bak.</p>'
       '<div class="card key"><h3>A &middot; Kesir &rarr; yüzde</h3>' + keyA() + '</div>'
       '<div class="card key"><h3>B &middot; Bilinmeyeni bulma</h3>' + keyB() + '</div>'
       '<div class="card key"><h3>C &middot; Kapsam</h3>' + keyC() + '</div>'
       '<div class="card key"><h3>D &middot; Formüller</h3>' + keyD() + '</div>'
       '<div class="next">'
       '<a href="bva.html"><b>Sınır Değer Analizi</b><span>Kapsam yüzdesinin en çok çıktığı yer</span></a>'
       '<a href="ep.html"><b>Denklik Payları</b><span>Payda nasıl kurulur</span></a>'
       '<a href="../istqub/questions_tr.html"><b>Sınav simülatörü</b><span>Hesabı gerçek soruda dene</span></a>'
       '</div>')

BODY = "".join(sec(i, t, lo, b) for i, ((t, lo), b) in enumerate(zip(
    SEC, [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11])))

EXTRA = """
/* ---- matematik sayfasina ozel ---- */
table.dt.frk{font-size:.8rem}
table.dt.frk th{width:3.2em;text-align:center;font-family:var(--mono)}
table.dt.frk td{text-align:center;padding:.3rem .25rem;min-width:4.1em}
table.dt.frk td b{display:block;font-family:var(--mono);font-size:.82rem;color:var(--ink)}
table.dt.frk td span{display:block;font-size:.74rem;font-weight:700;color:var(--cd)}
table.dt.drill td{vertical-align:middle}
table.dt.drill td.qn{font-family:var(--mono);color:var(--muted);width:2.4em;font-size:.78rem}
table.dt.drill td b{font-family:var(--mono);font-size:.95rem}
td.bl{min-width:5.5em;border-bottom:1px solid var(--line)}
ol.dr{list-style:none;counter-reset:d;margin:.6rem 0 0;padding:0;display:grid;gap:.45rem}
ol.dr li{counter-increment:d;display:grid;grid-template-columns:26px minmax(0,1fr) 8.5em;gap:.6rem;
  align-items:center;padding:.5rem .7rem;border:1px solid var(--line);border-radius:12px;
  background:var(--surface)}
ol.dr li::before{content:counter(d);width:23px;height:23px;border-radius:7px;display:flex;
  align-items:center;justify-content:center;font-size:.75rem;font-weight:900;color:#fff;background:var(--c)}
ol.dr li code{font-size:.95rem}
ol.dr .bl.w{height:1.6rem;border-bottom:1.5px dashed var(--line);border-radius:0}
ol.dr.big li{grid-template-columns:26px minmax(0,1fr);row-gap:.25rem}
ol.dr.big li > b{font-size:.9rem}
ol.dr.big li .qq{grid-column:2;font-size:.88rem;color:var(--muted)}
ol.dr.big li .bl.w{grid-column:2;height:1.5rem;max-width:12em}
.kg{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,150px),1fr));gap:.25rem .9rem;
  font-size:.86rem}
.kg.wide{grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:.3rem 1rem}
.kg span{display:block;padding:.12rem 0;border-bottom:1px dotted var(--line)}
.kg i{font-style:normal;font-family:var(--mono);font-size:.76rem;color:var(--muted);margin-right:.35rem}
.kg b{font-family:var(--mono);color:var(--good)}
.kg em{font-style:normal;font-size:.8rem;color:var(--muted)}
@media(max-width:620px){ ol.dr li{grid-template-columns:26px minmax(0,1fr);row-gap:.3rem}
  ol.dr li .bl.w{grid-column:2;max-width:10em} }
"""

PAGE = """<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sınav Matematiği &middot; CTFL</title>
<style>
%(css)s%(extra)s</style>
%(head)s
</head>
<body>
%(crumb)s
%(gate)s
<header class="hero"><div class="in">
  <p class="kicker">Konular &middot; CTFL v4.0 &middot; Sınav aritmetiği</p>
  <h1>Sınav Matematiği</h1>
  <p class="lede">Kesri yüzdeye çevirmek, bilinmeyeni çekmek, oran uygulamak ve sınavın altı
  formülünü hatasız kullanmak. Sekiz sınavdaki <b>69 soruda</b> bir hesap adımı var; bu sayfa
  tam olarak o hesapları çalıştırıyor. Sonunda 44 alıştırma ve cevap anahtarı.</p>
  <div class="jump">%(jump)s</div>
</div></header>

<nav class="sticky"><div class="in">%(nav)s</div></nav>

<main>
%(body)s
<footer class="ft">Sayılar ve örnekler ISTQB&reg; CTFL v4.0 &ouml;rnek sınavları A&ndash;D ile
pratik setler E&ndash;H'deki sorulardan &ccedil;ıkarıldı. Kişisel &ccedil;alışma i&ccedil;indir.</footer>
</main>
</body>
</html>
""" % dict(css=CSS, extra=EXTRA, head=HEAD, crumb=CRUMB, gate=GATE, jump=JUMP, nav=NAV, body=BODY)

io.open("matematik.html", "w", encoding="utf-8").write(PAGE)
print("matematik.html:", len(PAGE.encode("utf-8")) // 1024, "KB")
