# -*- coding: utf-8 -*-
import json, io, re, html, os
from scss import CSS
from qfmt import qhtml, esc
from glossary import find as gfind
from mdlite import render as md

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.environ.get("ISTQB_DATA", os.path.join(HERE, "..", "data"))
OUT  = os.environ.get("ISTQB_OUT",  os.path.join(HERE, "syllabus.html"))
def jd(n): return json.load(io.open(os.path.join(DATA, n), encoding="utf-8"))

TREE = jd("syllabus_tree.json")
BODY = jd("syllabus_body.json")
TREE_EN = jd("syllabus_tree_en.json")
BODY_EN = jd("syllabus_body_en.json")
CH_EN = {c["no"]: c for c in TREE_EN}
SEC_EN = {}
for _c in TREE_EN:
    for _s in _c["sections"]:
        SEC_EN[_s["no"]] = _s["title"]
        for _sb in _s["subsections"]: SEC_EN[_sb["no"]] = _sb["title"]
LO_EN = {l["id"]: l for c in TREE_EN for l in c["los"]}
EASY    = jd("easy_tr.json")
EASY_EN = jd("easy_en.json")
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
RX_SEC_EN  = re.compile(r"((?:see|in)\s+section\s+)(\d\.\d(?:\.\d)?)", re.I)
RX_CHAP_EN = re.compile(r"((?:see|in)\s+chapter\s+)(\d)\b", re.I)
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
    t = RX_SEC_EN.sub(f1, t); t = RX_CHAP_EN.sub(f2, t)
    return t

TERMS = None
def mark(t):                     # anahtar kelimeleri kalinlastir
    for w in TERMS:
        t = re.sub(r"(?<![\w>])(" + re.escape(w) + r")(?![\w<])",
                   r'<b class="term">\1</b>', t, count=1, flags=re.I)
    return t

def bodybi(tr, en):
    if not tr: return en or ""
    if not en: return tr
    return '<div class="x-tr">%s</div><div class="x-en">%s</div>' % (tr, en)

def body_html_en(no):
    b = BODY_EN.get(no)
    return body_html(b["blocks"]) if b else ""

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

def bi(tr, en):
    """iki dilli metin parcasi"""
    return '<span class="s-tr">%s</span><span class="s-en">%s</span>' % (tr, en)

def bx(tr, en):
    """bolum içi iki dilli metin parçasi (section[data-lang] ile değişir)"""
    return '<span class="x-tr">%s</span><span class="x-en">%s</span>' % (tr, en)

def pbadge(key):
    v = PCT.get(key)
    if v is None: return ""
    return ('<span class="pct" title="Bu b&ouml;l&uuml;m&uuml; bitirdiğinde sayfanın '
            '%%%d\'ini okumuş olursun  /  when you finish this section you have read '
            '%d%% of the page">%s</span>' % (v, v, bx("%%%d" % v, "%d%%" % v)))

# ---------- kolay anlatim ----------
def easy(no):
    t, e = EASY.get(no), EASY_EN.get(no)
    if not t and not e: return ""
    inner = ""
    if t: inner += '<div class="x-tr">%s</div>' % md(t)
    if e: inner += '<div class="x-en">%s</div>' % md(e)
    return '<div class="ez">%s</div>' % inner

def vtools(no, has_easy):
    ver = ""
    if has_easy:
        ver = ('<span class="sw vr"><button type="button" class="on" data-v="o">'
               + bx("Orijinal", "Original")
               + '</button><button type="button" data-v="e">'
               + bx("Kolay", "Easy")
               + '</button></span>')
    return ('<div class="vtools">%s<span class="sw lg">'
            '<button type="button" class="on" data-l="tr">TR</button>'
            '<button type="button" data-l="en">EN</button></span></div>' % ver)

# ---------- teknik terim sozlugu ----------
def node_text(no):
    """bolumun turkce govdesi + o bolumun sinav sorulari"""
    out = []
    b = BODY.get(no)
    if b:
        for bl in b["blocks"]:
            out.append(bl.get("text", "")); out += bl.get("items", [])
    for lo in LO_OF.get(no, []):
        for q in BY.get(lo["id"], []):
            out.append(q["q"]); out += list(q["opts"].values())
    return " \n ".join(out)

def gloss(no):
    terms = gfind(node_text(no), no.split(".")[0])
    if len(terms) < 3: return ""
    cells = "".join('<div class="g"><b>%s</b><i>%s</i></div>' % (esc(t), esc(e))
                    for t, e in terms)
    tpl = ('<details class="gl"><summary>'
           + bx("Teknik terimler (T\u00fcrk\u00e7e \u2192 \u0130ngilizce)",
                "Technical terms (Turkish \u2192 English)")
           + '<span class="cnt">%d</span></summary><div class="glwrap">%s</div>'
             '<p class="glfoot">'
           + bx("T\u00fcrk\u00e7e kar\u015f\u0131l\u0131k kafan\u0131 kar\u0131\u015ft\u0131r\u0131rsa "
                "terimin \u0130ngilizce as\u0131l halini buradan kontrol et.",
                "Terms used in this section and in its exam questions.")
           + '</p></details>')
    return tpl % (len(terms), cells)

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
        abox = ('<details class="ans"><summary>'
                '<span class="l-tr">Cevabı göster</span><span class="l-en">Show answer</span>'
                '</summary><div class="av">'
                '<span class="l-tr">Cevap:</span><span class="l-en">Answer:</span>&nbsp;%s'
                '</div></details>' % esc(ans)) if ans else ""
        en = q.get("en")
        if en:
            eopts = "".join('<li><b>%s)</b><span>%s</span></li>' % (k, esc(v))
                            for k, v in sorted(en["opts"].items()))
            bodies = ('<div class="l-tr">%s<ul class="qopts">%s</ul></div>'
                      '<div class="l-en">%s<ul class="qopts">%s</ul></div>'
                      % (qhtml(q["q"]), opts, qhtml(en["q"]), eopts))
            sw = ('<span class="lang"><button type="button" class="on" data-l="tr">TR</button>'
                  '<button type="button" data-l="en">EN</button></span>')
        else:
            bodies = '<div class="l-tr">%s<ul class="qopts">%s</ul></div>' % (qhtml(q["q"]), opts)
            sw = ""
        items.append(
          '<div class="qitem" data-lang="tr"><div class="qref">'
          '<span class="ex %s">%s</span><span class="kk">%s · %s</span>%s%s</div>%s%s</div>'
          % (q["kind"], esc(q["ref"]), esc(q["set"]), q["k"], mk, sw, bodies, abox))
    lolist = ", ".join(l["id"] for l in los)
    tpl = ('<details class="qa"><summary>'
           + bx('Sınavlarda çıkmış sorular', 'Questions asked in the exams')
           + '<span class="cnt">%d</span></summary><div class="qwrap">%s'
             '<p class="qfoot">%s &middot; '
           + bx('Ayrıntılı çözümler için ', 'For detailed solutions see the ')
           + '<a href="https://cihandogan.co.uk/deniz/istqub/questions_tr.html"'
             ' target="_blank" rel="noopener">'
           + bx('sınav simülatörü', 'exam simulator')
           + '</a>.</p></div></details>')
    return tpl % (len(qs), "".join(items), esc(lolist))

def lobadges(no):
    los = LO_OF.get(no, [])
    if not los: return ""
    return '<span class="los">' + "".join(
        '<span title="%s">%s · %s</span>'
        % (esc(l["text"] + "  /  " + LO_EN.get(l["id"], l)["text"]), l["id"], l["k"])
        for l in los) + '</span>'

def nq(no):
    return sum(len(BY.get(l["id"], [])) for l in LO_OF.get(no, []))

# ---------- govde ----------
def render():
    out = []
    for c in T:
        global TERMS
        TERMS = [w.strip() for w in c["kw"].split(",") if 3 < len(w.strip()) < 40]
        cen  = CH_EN.get(c["no"], {})
        kwen = [w.strip() for w in cen.get("keywords", []) if w.strip()]
        kws  = '<div class="kws s-tr">%s</div>' % "".join("<span>%s</span>" % esc(w) for w in TERMS)
        if kwen:
            kws += '<div class="kws s-en">%s</div>' % "".join("<span>%s</span>" % esc(w) for w in kwen)
        los = "".join(
            '<li><a class="loid" href="#%s">%s</a><span class="kb %s">%s</span><span>%s</span></li>'
            % (sid(lo_target(l["id"])), l["id"], l["k"], l["k"],
               bi(esc(l["text"]), esc(LO_EN.get(l["id"], l)["text"]))) for l in c["los"])
        nqc = sum(len(BY.get(l["id"], [])) for l in c["los"])
        lo0, lo1 = CH_RANGE[c["no"]][0], CH_RANGE[c["no"]][1]
        atr = ('<abbr title="ISTQB tarafından akredite eğitim kursları için önerilen asgari ders '
               'süresi — sınav süresi değildir">eğitim süresi %s dk</abbr>' % SURE[c["no"]])
        aen = ('<abbr title="ISTQB&rsquo;s recommended minimum teaching time for accredited '
               'courses — not exam time">teaching time %s min</abbr>' % SURE[c["no"]])
        meta = (bi(atr, aen) + " &middot; "
                + bi("%d öğrenme hedefi" % len(c["los"]), "%d learning objectives" % len(c["los"]))
                + " &middot; " + bi("%d soru" % nqc, "%d questions" % nqc)
                + " &middot; " + bi("sayfanın %%%d&ndash;%%%d aralığı" % (lo0, lo1),
                                    "%d%%&ndash;%d%% of the page" % (lo0, lo1)))
        out.append('<div class="chap" id="c%s"><div class="chead"><div class="n">%s</div><div>'
                   '<h2>%s</h2><div class="meta">%s</div></div></div>%s'
                   '<div class="lobox"><h3>%s</h3><ol>%s</ol></div>'
                   % (c["no"], c["no"], bi(esc(c["title"]), esc(cen.get("title", c["title"]))),
                      meta, kws, bi("Öğrenme hedefleri", "Learning objectives"), los))
        for s in c["secs"]:
            bod = bodybi(body_html(s["blocks"]), body_html_en(s["no"]))
            ez  = easy(s["no"]); a = acc(s["no"]); gl = gloss(s["no"])
            inner = ""
            if bod or ez:
                inner = vtools(s["no"], bool(ez)) + ('<div class="og">%s</div>' % bod if bod else "") + ez
            out.append('<section class="sec" id="%s" data-no="%s" data-lang="tr" data-ver="o">'
                       '<div class="sh">'
                       '<span class="num">%s</span><h3>%s</h3>%s%s</div>%s'
                       % (sid(s["no"]), s["no"], s["no"],
                          bx(esc(s["title"]), esc(SEC_EN.get(s["no"], s["title"]))),
                          lobadges(s["no"]), pbadge(s["no"]),
                          ('<div class="body">%s%s%s</div>' % (inner, gl, a))
                          if (inner or a) else ""))
            out.append("</section>")      # alt bolumler ic ice degil, kardes
            for sb in s["subs"]:
                bod2 = bodybi(body_html(sb["blocks"]), body_html_en(sb["no"]))
                ez2  = easy(sb["no"])
                inner2 = vtools(sb["no"], bool(ez2)) + \
                         ('<div class="og">%s</div>' % bod2 if bod2 else "") + ez2
                out.append('<section class="sub" id="%s" data-no="%s" data-lang="tr" data-ver="o">'
                           '<div class="sh">'
                           '<span class="num">%s</span><h4>%s</h4>%s%s</div>'
                           '<div class="body">%s%s%s</div></section>'
                           % (sid(sb["no"]), sb["no"], sb["no"],
                              bx(esc(sb["title"]), esc(SEC_EN.get(sb["no"], sb["title"]))),
                              lobadges(sb["no"]), pbadge(sb["no"]),
                              inner2, gloss(sb["no"]), acc(sb["no"])))
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
                       % (sid(s["no"]), s["no"],
                          bi(esc(s["title"]), esc(SEC_EN.get(s["no"], s["title"]))),
                          (" · %d" % n) if n else ""))
            for sb in s["subs"]:
                n = nq(sb["no"])
                lis.append('<li><a class="sub" href="#%s">%s %s%s</a></li>'
                           % (sid(sb["no"]), sb["no"],
                              bi(esc(sb["title"]), esc(SEC_EN.get(sb["no"], sb["title"]))),
                              (" · %d" % n) if n else ""))
        out.append('<div class="grp"><a href="#c%s"><i>%s</i>%s</a><ul>%s</ul></div>'
                   % (c["no"], c["no"],
                      bi(esc(c["title"]), esc(CH_EN.get(c["no"], {}).get("title", c["title"]))),
                      "".join(lis)))
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
  /* dil ve surum anahtarlari */
  function mark(scope, attr, v){
    scope.querySelectorAll(':scope > .qref .lang button, :scope > .body > .vtools .sw button,'
      + '#glob button, #gver button').forEach(function(b){
        if(b.dataset[attr]!==undefined) b.classList.toggle('on', b.dataset[attr]===v);
      });
  }
  function qLang(box, l){
    box.dataset.lang = l;
    box.querySelectorAll(':scope > .qref .lang button').forEach(function(b){
      b.classList.toggle('on', b.dataset.l === l);
    });
  }
  function secLang(sec, l){
    sec.dataset.lang = l;
    sec.querySelectorAll(':scope > .body .vtools .sw.lg button').forEach(function(b){
      b.classList.toggle('on', b.dataset.l === l);
    });
    sec.querySelectorAll(':scope > .body .qitem[data-lang]').forEach(function(q){ qLang(q, l) });
  }
  function secVer(sec, v){
    sec.dataset.ver = v;
    sec.querySelectorAll(':scope > .body .vtools .sw.vr button').forEach(function(b){
      b.classList.toggle('on', b.dataset.v === v);
    });
  }
  var SECS = [].slice.call(document.querySelectorAll('main section[data-no]'));
  function allLang(l){
    document.querySelectorAll('#glob button').forEach(function(x){x.classList.toggle('on',x.dataset.l===l)});
    body.dataset.lang = l;
    document.documentElement.lang = l;
    SECS.forEach(function(s){ secLang(s, l) });
    document.querySelectorAll('.qitem[data-lang]').forEach(function(q){ qLang(q, l) });
    inp.placeholder = (l==='en' ? 'Search topics…' : 'Konu ara…');
    try{ localStorage.setItem('ctfl-lang', l) }catch(e){}
    requestAnimationFrame(function(){ sync(); prog(); });
  }
  function allVer(v){
    document.querySelectorAll('#gver button').forEach(function(x){x.classList.toggle('on',x.dataset.v===v)});
    body.dataset.ver = v;
    SECS.forEach(function(s){ secVer(s, v) });
    try{ localStorage.setItem('ctfl-ver', v) }catch(e){}
    requestAnimationFrame(function(){ sync(); prog(); });
  }
  document.addEventListener('click', function(ev){
    var b = ev.target.closest('button[data-l], button[data-v]'); if(!b) return;
    if(b.dataset.v !== undefined){
      if(b.closest('#gver')) allVer(b.dataset.v);
      else { secVer(b.closest('section[data-no]'), b.dataset.v);
             requestAnimationFrame(function(){ sync(); prog(); }); }
      return;
    }
    var l = b.dataset.l;
    if(b.closest('#glob'))        allLang(l);
    else if(b.closest('.vtools')) { secLang(b.closest('section[data-no]'), l);
                                    requestAnimationFrame(function(){ sync(); prog(); }); }
    else                          qLang(b.closest('.qitem'), l);
  });

  /* kayitli tercihler */
  try{ if(localStorage.getItem('ctfl-lang')==='en') allLang('en');
       if(localStorage.getItem('ctfl-ver')==='e')  allVer('e');
  }catch(e){}
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
<body data-lang="tr">

<header class="hero"><div class="hin">
  <p class="kick">ISTQB&reg; Certified Tester &middot; Foundation Level v4.0.1</p>
  <h1><span class="s-tr">CTFL Ders Programı &mdash; konu konu, sorularıyla</span><span class="s-en">CTFL Syllabus &mdash; topic by topic, with its questions</span></h1>
  <p class="s-tr">Resm&icirc; ders programının sadeleştirilmiş s&uuml;r&uuml;m&uuml;: telif, index ve tekrarlar atıldı,
  geriye yalnızca konular kaldı. Her konunun altında, <b>o &ouml;ğrenme hedefinden</b> sekiz &ouml;rnek sınavda
  &ccedil;ıkmış soruları a&ccedil;ılır bir panelde bulacaksın.</p>
  <p class="s-en">A simplified version of the official syllabus: copyright pages, the index and the
  repetition are gone, only the subject matter is left. Under each topic you will find, in a collapsible
  panel, the questions that came up in eight sample exams <b>for that learning objective</b>.</p>
  <div class="stats s-tr"><b>6 konu</b><b>%(nsec)d bölüm</b><b>64 öğrenme hedefi</b><b>%(nq)d soru</b><b>8 sınav</b></div><div class="stats s-en"><b>6 chapters</b><b>%(nsec)d sections</b><b>64 learning objectives</b><b>%(nq)d questions</b><b>8 exams</b></div>
  <p class="hnote s-tr">Konu başlıklarındaki s&uuml;reler, ISTQB'nin <b>akredite eğitim kursları i&ccedil;in &ouml;nerdiği
  asgari ders s&uuml;releridir</b> (toplam 1135 dk &asymp; 19 saat). Sınav s&uuml;resi değildir &mdash; sınav
  40 soru i&ccedil;in 60 dakikadır (ana dili İngilizce olmayan adaylarda 75 dk).</p>
  <p class="hnote s-en">The times on the chapter headings are ISTQB&rsquo;s <b>recommended minimum teaching
  times for accredited training courses</b> (1135 min &asymp; 19 hours in total). They are not exam times
  &mdash; the exam is 40 questions in 60 minutes (75 for candidates who are not native English speakers).</p>
</div></header>

<nav class="top"><div class="nin">
  <button class="menubtn" id="menu" aria-label="İçindekiler">&#9776;</button>
  <div class="chips">%(chips)s</div>
  <span class="sw glob vr" id="gver" title="Tüm konular / all topics"><button type="button" class="on" data-v="o"><span class="s-tr">Orijinal</span><span class="s-en">Original</span></button><button type="button" data-v="e"><span class="s-tr">Kolay</span><span class="s-en">Easy</span></button></span><span class="lang glob" id="glob" title="Sayfanın dili / page language"><button type="button" class="on" data-l="tr">TR</button><button type="button" data-l="en">EN</button></span>
  <div class="srch"><input id="q" type="search" placeholder="Konu ara…" aria-label="Konu ara"></div>
  <div class="bar" id="bar" role="progressbar" aria-label="Okuma ilerlemesi"></div>
</div></nav>

<div class="shell">
  <aside>%(side)s</aside>
  <main>%(body)s
    <div class="nores"><span class="s-tr">Aramanla eşleşen bölüm yok.</span><span class="s-en">No section matches your search.</span></div>
    <footer class="ft"><span class="s-tr">Kaynak: ISTQB&reg; Temel Seviye Ders Programı v4.0.1 (T&uuml;rk&ccedil;e, Yazılım Test ve Kalite Derneği).
    Sorular resm&icirc; &ouml;rnek sınavlar A&ndash;D ve pratik setler E&ndash;H'den alınmıştır.
    Bu sayfa kişisel &ccedil;alışma ama&ccedil;lıdır; &copy; ISTQB&reg;.</span><span class="s-en">Source: ISTQB&reg; Certified Tester
    Foundation Level Syllabus v4.0.1 (English and Turkish editions). The questions are taken from the official
    sample exams A&ndash;D and the practice sets E&ndash;H. This page is for personal study; &copy; ISTQB&reg;.</span></footer>
  </main>
</div>
<script>%(js)s</script>
</body>
</html>
"""

chips = "".join('<a href="#c%s">%s. %s</a>'
                % (c["no"], c["no"],
                   bi(html.escape(c["title"]),
                      html.escape(CH_EN.get(c["no"], {}).get("title", c["title"])))) for c in T)
nsec = len(NODES)
page = HTML % dict(css=CSS, js=JS, chips=chips, side=sidebar(), body=render(),
                   nsec=nsec, nq=QD["meta"]["total"])
io.open(OUT, "w", encoding="utf-8").write(page)
print("bolum dugumu:", nsec, "| LO:", len(ALL_LO), "| boyut:", len(page.encode("utf-8"))//1024, "KB")
eksik = [l for l in ALL_LO if not BY.get(l)]
print("sorusu olmayan LO:", eksik)
