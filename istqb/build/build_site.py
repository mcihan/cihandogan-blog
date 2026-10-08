# -*- coding: utf-8 -*-
import json, io, re, html, os
from scss import CSS
from qfmt import qhtml, esc

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.environ.get("ISTQB_DATA", os.path.join(HERE, "..", "data"))
OUT  = os.environ.get("ISTQB_OUT",  os.path.join(HERE, "syllabus.html"))
def jd(n): return json.load(io.open(os.path.join(DATA, n), encoding="utf-8"))

TREE = jd("syllabus_tree.json")
BODY = jd("syllabus_body.json")
QD   = jd("questions_by_lo.json")
BY   = QD["byLo"]

SURE = {c["no"]: str(c["minutes"]) for c in TREE}

# data/*.json -> eski ic yapi (bolum agaci + bloklar)
T = []
for c in TREE:
    ch = dict(no=c["no"], title=c["title"], kw=", ".join(c["keywords"]),
              los=[dict(id=l["id"], k=l["k"], text=l["text"]) for l in c["los"]], secs=[])
    for s_ in c["sections"]:
        sec = dict(no=s_["no"], title=s_["title"], blocks=BODY[s_["no"]]["blocks"], subs=[])
        for sb in s_["subsections"]:
            sec["subs"].append(dict(no=sb["no"], title=sb["title"], blocks=BODY[sb["no"]]["blocks"]))
        ch["secs"].append(sec)
    T.append(ch)

# ---------- dugum indeksi ----------
NODES = {}                       # "1.1.1" -> node
for c in T:
    for s in c["secs"]:
        NODES[s["no"]] = s
        for sb in s["subs"]: NODES[sb["no"]] = sb
def sid(no): return "s-" + no.replace(".", "-")

def lo_target(loid):             # FL-1.3.1 -> 1.3 (alt bolum yoksa)
    a, b, cc = loid[3:].split(".")
    return "%s.%s.%s" % (a, b, cc) if "%s.%s.%s" % (a, b, cc) in NODES else "%s.%s" % (a, b)

LO_OF = {}                       # node no -> [lo,...]
ALL_LO = {}
for c in T:
    for lo in c["los"]:
        ALL_LO[lo["id"]] = lo
        LO_OF.setdefault(lo_target(lo["id"]), []).append(lo)

# ---------- capraz referans linkleri ----------
RX_SEC  = re.compile(r"(bkz\.?\s*bölüm\s*)(\d\.\d(?:\.\d)?)", re.I)
RX_CHAP = re.compile(r"(bkz\.?\s*konu\s*)(\d)", re.I)
RX_SEC2 = re.compile(r"(bölüm\s*)(\d\.\d(?:\.\d)?)('[dt]e|'da|'ta|’de|’da)", re.I)

def xref(t):
    def f1(m):
        no = m.group(2)
        return m.group(1) + ('<a class="xref" href="#%s">%s</a>' % (sid(no), no) if no in NODES else no)
    def f2(m):
        return m.group(1) + '<a class="xref" href="#c%s">%s</a>' % (m.group(2), m.group(2))
    def f3(m):
        no = m.group(2)
        return m.group(1) + ('<a class="xref" href="#%s">%s</a>' % (sid(no), no) if no in NODES else no) + m.group(3)
    t = RX_SEC.sub(f1, t); t = RX_SEC2.sub(f3, t); t = RX_CHAP.sub(f2, t)
    return t

TERMS = None
def mark(t):                     # anahtar kelimeleri kalinlastir
    for w in TERMS:
        t = re.sub(r"(?<![\w>])(" + re.escape(w) + r")(?![\w<])",
                   r'<b class="term">\1</b>', t, count=1, flags=re.I)
    return t

def body_html(blocks, terms_on=True):
    global TERMS
    out = []
    for b in blocks:
        if b["t"] == "p":
            out.append("<p>" + xref(esc(b["text"])) + "</p>")
        elif b["t"] == "ul":
            out.append("<ul>" + "".join("<li>" + xref(esc(x)) + "</li>" for x in b["items"]) + "</ul>")
        else:
            cls = ' class="prin"' if len(b["items"]) >= 5 else ""
            out.append("<ol%s>" % cls + "".join("<li>" + xref(esc(x)) + "</li>" for x in b["items"]) + "</ol>")
    return "".join(out)

# ---------- ilerleme yuzdesi (kelime agirligina gore, belge sirasinda) ----------
def _w(blocks):
    n = 0
    for b in blocks:
        n += len(b.get("text", "").split())
        for x in b.get("items", []): n += len(x.split())
    return n

_order = []                      # [(anahtar, agirlik, konu_no)] belge sirasinda
for _c in T:
    _order.append(("c" + _c["no"],
                   sum(len(l["text"].split()) for l in _c["los"])
                   + len([k for k in _c["kw"].split(",") if k.strip()]), _c["no"]))
    for _s in _c["secs"]:
        _order.append((_s["no"], _w(_s["blocks"]), _c["no"]))
        for _sb in _s["subs"]:
            _order.append((_sb["no"], _w(_sb["blocks"]), _c["no"]))

_total = sum(w for _, w, _c2 in _order) or 1
PCT, CH_RANGE, _cum = {}, {}, 0
for _k, _w2, _ch in _order:
    if _ch not in CH_RANGE:
        CH_RANGE[_ch] = [int(round(_cum * 100.0 / _total)), 0]
    _cum += _w2
    PCT[_k] = max(1, min(100, int(round(_cum * 100.0 / _total))))
    CH_RANGE[_ch][1] = PCT[_k]

def pbadge(key):
    v = PCT.get(key)
    if v is None: return ""
    return ('<span class="pct" title="Bu b&ouml;l&uuml;m&uuml; bitirdiğinde sayfanın '
            '%%%d\'ini okumuş olursun">%%%d</span>' % (v, v))

# ---------- soru akordiyonu ----------
def acc(node_no):
    los = LO_OF.get(node_no, [])
    qs = []
    for lo in los: qs += BY.get(lo["id"], [])
    qs.sort(key=lambda x: (x["exam"], x["n"]))
    if not qs: return ""
    items = []
    for q in qs:
        opts = "".join('<li><b>%s)</b><span>%s</span></li>' % (k, esc(v))
                       for k, v in sorted(q["opts"].items()))
        mk = '<span class="mk">çoktan seçmeli</span>' if q["multi"] else ""
        ans = ", ".join(a.upper() for a in q.get("ans", []))
        abox = ('<details class="ans"><summary>Cevabı göster</summary>'
                '<div class="av">Cevap: %s</div></details>' % esc(ans)) if ans else ""
        items.append(
          '<div class="qitem"><div class="qref">'
          '<span class="ex %s">%s</span><span class="kk">%s · %s</span>%s</div>%s'
          '<ul class="qopts">%s</ul>%s</div>'
          % (q["kind"], esc(q["ref"]), esc(q["set"]), q["k"], mk, qhtml(q["q"]), opts, abox))
    lolist = ", ".join(l["id"] for l in los)
    return ('<details class="qa"><summary>Sınavlarda çıkmış sorular'
            '<span class="cnt">%d</span></summary><div class="qwrap">%s'
            '<p class="qfoot">%s · Ayrıntılı çözümler için '
            '<a href="https://cihandogan.co.uk/deniz/istqub/questions_tr.html" target="_blank" rel="noopener">'
            'sınav simülatörü</a>.</p></div></details>'
            % (len(qs), "".join(items), esc(lolist)))

def lobadges(no):
    los = LO_OF.get(no, [])
    if not los: return ""
    return '<span class="los">' + "".join(
        '<span title="%s">%s · %s</span>' % (esc(l["text"]), l["id"], l["k"]) for l in los) + "</span>"

def nq(no):
    return sum(len(BY.get(l["id"], [])) for l in LO_OF.get(no, []))

# ---------- govde ----------
def render():
    out = []
    for c in T:
        global TERMS
        TERMS = [w.strip() for w in c["kw"].split(",") if 3 < len(w.strip()) < 40]
        kws = "".join("<span>%s</span>" % esc(w) for w in TERMS)
        los = "".join(
            '<li><a class="loid" href="#%s">%s</a><span class="kb %s">%s</span><span>%s</span></li>'
            % (sid(lo_target(l["id"])), l["id"], l["k"], l["k"], esc(l["text"])) for l in c["los"])
        out.append('<div class="chap" id="c%s"><div class="chead"><div class="n">%s</div><div>'
                   '<h2>%s</h2><div class="meta"><abbr title="ISTQB taraf&#305;ndan akredite e&#287;itim '
                   'kurslar&#305; i&ccedil;in &ouml;nerilen asgari ders s&uuml;resi &mdash; '
                   's&#305;nav s&uuml;resi de&#287;ildir">e&#287;itim s&uuml;resi %s dk</abbr> &middot; %d &ouml;&#287;renme hedefi &middot; %d soru'
                   ' &middot; sayfanın %%%d&ndash;%%%d aralığı'
                   '</div></div></div>'
                   '<div class="kws">%s</div>'
                   '<div class="lobox"><h3>Öğrenme hedefleri</h3><ol>%s</ol></div>'
                   % (c["no"], c["no"], esc(c["title"]), SURE[c["no"]], len(c["los"]),
                      sum(len(BY.get(l["id"], [])) for l in c["los"]),
                      CH_RANGE[c["no"]][0], CH_RANGE[c["no"]][1], kws, los))
        for s in c["secs"]:
            inner = body_html(s["blocks"])
            out.append('<section class="sec" id="%s" data-no="%s"><div class="sh">'
                       '<span class="num">%s</span><h3>%s</h3>%s%s</div>%s'
                       % (sid(s["no"]), s["no"], s["no"], esc(s["title"]), lobadges(s["no"]), pbadge(s["no"]),
                          ('<div class="body">%s%s</div>' % (inner, acc(s["no"]))) if (inner or acc(s["no"])) else ""))
            for sb in s["subs"]:
                out.append('<section class="sub" id="%s" data-no="%s"><div class="sh">'
                           '<span class="num">%s</span><h4>%s</h4>%s%s</div>'
                           '<div class="body">%s%s</div></section>'
                           % (sid(sb["no"]), sb["no"], sb["no"], esc(sb["title"]), lobadges(sb["no"]), pbadge(sb["no"]),
                              body_html(sb["blocks"]), acc(sb["no"])))
            out.append("</section>")
        out.append("</div>")
    return "".join(out)

# ---------- kenar cubugu ----------
def sidebar():
    out = []
    for c in T:
        lis = []
        for s in c["secs"]:
            n = nq(s["no"])
            lis.append('<li><a href="#%s">%s %s%s</a></li>'
                       % (sid(s["no"]), s["no"], esc(s["title"]), (" · %d" % n) if n else ""))
            for sb in s["subs"]:
                n = nq(sb["no"])
                lis.append('<li><a class="sub" href="#%s">%s %s%s</a></li>'
                           % (sid(sb["no"]), sb["no"], esc(sb["title"]), (" · %d" % n) if n else ""))
        out.append('<div class="grp"><a href="#c%s"><i>%s</i>%s</a><ul>%s</ul></div>'
                   % (c["no"], c["no"], esc(c["title"]), "".join(lis)))
    return "".join(out)

JS = """
(function(){
  var body=document.body;
  document.getElementById('menu').onclick=function(){body.classList.toggle('nav-open')};
  document.querySelectorAll('aside a').forEach(function(a){
    a.addEventListener('click',function(){body.classList.remove('nav-open')});
  });
  /* scrollspy — tiklamayla gelen kaydirmaya karismaz:
     yalnizca kenar cubugunun kendi scrollTop'u degisir, sayfa asla oynatilmaz. */
  var aside=document.querySelector('aside'), items=[], cur=null, tick=false;
  document.querySelectorAll('aside li a').forEach(function(a){
    var el=document.getElementById(a.getAttribute('href').slice(1));
    if(el) items.push({a:a, el:el});
  });
  function sync(){
    tick=false;
    if(!items.length) return;
    var line=document.querySelector('nav.top').getBoundingClientRect().bottom+24, best=null;
    for(var i=0;i<items.length;i++){
      if(items[i].el.getBoundingClientRect().top<=line) best=items[i]; else break;
    }
    if(!best||best.a===cur) return;
    if(cur) cur.classList.remove('on');
    best.a.classList.add('on'); cur=best.a;
    if(getComputedStyle(aside).position==='fixed' && !body.classList.contains('nav-open')) return;
    var r=best.a.getBoundingClientRect(), p=aside.getBoundingClientRect();
    if(r.top<p.top+24)         aside.scrollTop += r.top-p.top-24;
    else if(r.bottom>p.bottom-24) aside.scrollTop += r.bottom-p.bottom+24;
  }
  /* okuma ilerleme cubugu */
  var bar=document.getElementById('bar');
  function prog(){
    var d=document.documentElement, h=d.scrollHeight-d.clientHeight;
    bar.style.width = (h>0 ? Math.min(100, Math.max(0, d.scrollTop/h*100)) : 0) + '%';
  }
  addEventListener('scroll',function(){ if(!tick){tick=true;requestAnimationFrame(function(){sync();prog();});} },{passive:true});
  addEventListener('resize',prog,{passive:true});
  prog();
  addEventListener('hashchange',function(){ requestAnimationFrame(sync); });
  sync();

  /* arama */
  var inp=document.getElementById('q'), nores=document.querySelector('.nores');
  var nodes=[].slice.call(document.querySelectorAll('main section[data-no]'));
  var chaps=[].slice.call(document.querySelectorAll('main .chap'));
  var side=[].slice.call(document.querySelectorAll('aside li'));
  function norm(s){return s.toLocaleLowerCase('tr').replace(/[ıİ]/g,'i').replace(/[şŞ]/g,'s')
    .replace(/[ğĞ]/g,'g').replace(/[üÜ]/g,'u').replace(/[öÖ]/g,'o').replace(/[çÇ]/g,'c')}
  nodes.forEach(function(n){n._t=norm(n.textContent)});
  side.forEach(function(l){l._t=norm(l.textContent)});
  var t;
  inp.addEventListener('input',function(){
    clearTimeout(t); t=setTimeout(function(){
      var v=norm(inp.value.trim());
      if(!v){ body.classList.remove('filtering');
        nodes.forEach(function(n){n.style.display=''}); chaps.forEach(function(c){c.style.display=''});
        side.forEach(function(l){l.style.display=''}); nores.classList.remove('show'); return; }
      body.classList.add('filtering');
      var hit=0;
      chaps.forEach(function(c){
        var any=0;
        c.querySelectorAll('section[data-no]').forEach(function(n){
          var ok=n._t.indexOf(v)>=0; n.style.display=ok?'':'none'; if(ok){any++;hit++}
        });
        c.style.display=any?'':'none';
      });
      side.forEach(function(l){l.style.display=l._t.indexOf(v)>=0?'':'none'});
      nores.classList.toggle('show',hit===0);
    },140);
  });
})();
"""

HTML = u"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ISTQB CTFL v4.0 · Konu Anlatımı ve Soru Bankası</title>
<meta name="description" content="ISTQB Temel Seviye Ders Programı v4.0.1'in sadeleştirilmiş, yapılandırılmış HTML sürümü. Her konunun altında o öğrenme hedefinden çıkmış sınav soruları.">
<style>%(css)s</style>
</head>
<body>

<header class="hero"><div class="hin">
  <p class="kick">ISTQB&reg; Certified Tester &middot; Foundation Level v4.0.1</p>
  <h1>CTFL Ders Programı &mdash; konu konu, sorularıyla</h1>
  <p>Resm&icirc; ders programının sadeleştirilmiş s&uuml;r&uuml;m&uuml;: telif, index ve tekrarlar atıldı,
  geriye yalnızca konular kaldı. Her konunun altında, <b>o &ouml;ğrenme hedefinden</b> sekiz &ouml;rnek sınavda
  &ccedil;ıkmış soruları a&ccedil;ılır bir panelde bulacaksın.</p>
  <div class="stats"><b>6 konu</b><b>%(nsec)d bölüm</b><b>64 öğrenme hedefi</b><b>%(nq)d soru</b><b>8 sınav</b></div>
  <p class="hnote">Konu başlıklarındaki s&uuml;reler, ISTQB'nin <b>akredite eğitim kursları i&ccedil;in &ouml;nerdiği
  asgari ders s&uuml;releridir</b> (toplam 1135 dk &asymp; 19 saat). Sınav s&uuml;resi değildir &mdash; sınav
  40 soru i&ccedil;in 60 dakikadır (ana dili İngilizce olmayan adaylarda 75 dk).</p>
</div></header>

<nav class="top"><div class="nin">
  <button class="menubtn" id="menu" aria-label="İçindekiler">&#9776;</button>
  <div class="chips">%(chips)s</div>
  <div class="srch"><input id="q" type="search" placeholder="Konu ara…" aria-label="Konu ara"></div>
  <div class="bar" id="bar" role="progressbar" aria-label="Okuma ilerlemesi"></div>
</div></nav>

<div class="shell">
  <aside>%(side)s</aside>
  <main>%(body)s
    <div class="nores">Aramanla eşleşen bölüm yok.</div>
    <footer class="ft">Kaynak: ISTQB&reg; Temel Seviye Ders Programı v4.0.1 (T&uuml;rk&ccedil;e, Yazılım Test ve Kalite Derneği).
    Sorular resm&icirc; &ouml;rnek sınavlar A&ndash;D ve pratik setler E&ndash;H'den alınmıştır.
    Bu sayfa kişisel &ccedil;alışma ama&ccedil;lıdır; &copy; ISTQB&reg;.</footer>
  </main>
</div>
<script>%(js)s</script>
</body>
</html>
"""

chips = "".join('<a href="#c%s">%s. %s</a>' % (c["no"], c["no"], html.escape(c["title"])) for c in T)
nsec = len(NODES)
page = HTML % dict(css=CSS, js=JS, chips=chips, side=sidebar(), body=render(),
                   nsec=nsec, nq=QD["meta"]["total"])
io.open(OUT, "w", encoding="utf-8").write(page)
print("bolum dugumu:", nsec, "| LO:", len(ALL_LO), "| boyut:", len(page.encode("utf-8"))//1024, "KB")
eksik = [l for l in ALL_LO if not BY.get(l)]
print("sorusu olmayan LO:", eksik)
