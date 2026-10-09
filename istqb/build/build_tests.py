# -*- coding: utf-8 -*-
"""Bolum bazli testler:  static/deniz/bolum_testleri/{index,bolum-1,bolum-2}.html

Sorular dogrudan simulator sayfalarindan okunur (gerekce ve ayrintili cozum dahil),
konu baglantilari ders programi sayfasinin capalarina gider."""
import re, json, io, os
from tests_css import TCSS
from qfmt import qhtml, esc

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA = os.path.join(HERE, "..", "data")
OUTD = os.path.join(ROOT, "static/deniz/bolum_testleri")
SIM   = os.path.join(ROOT, "static/deniz/istqub/questions_tr.html")
SIMEN = os.path.join(ROOT, "static/deniz/istqub/questions.html")
REF   = os.path.join(ROOT, "static/deniz/istqub/cozum_yontemleri_tr.html")
DERS  = "../istqub/ders_programi_tr.html"
SIMU  = "../istqub/questions_tr.html"
CHAPTERS = ["1", "2"]                      # hazir olan konular

def jd(n): return json.load(io.open(os.path.join(DATA, n), encoding="utf-8"))
def sim(path):
    s = io.open(path, encoding="utf-8").read()
    m = re.search(r"const DATA\s*=\s*(\{.*?\});\s*\n", s, re.S)
    return json.loads(m.group(1))

TREE, TREE_EN = jd("syllabus_tree.json"), jd("syllabus_tree_en.json")
TITLE, TITLE_EN, CH_T, CH_E = {}, {}, {}, {}
NODES = set()
for c in TREE:
    CH_T[c["no"]] = c["title"]
    for s in c["sections"]:
        TITLE[s["no"]] = s["title"]; NODES.add(s["no"])
        for sb in s["subsections"]: TITLE[sb["no"]] = sb["title"]; NODES.add(sb["no"])
for c in TREE_EN:
    CH_E[c["no"]] = c["title"]
    for s in c["sections"]:
        TITLE_EN[s["no"]] = s["title"]
        for sb in s["subsections"]: TITLE_EN[sb["no"]] = sb["title"]

def node_of(lo):
    a, b, cc = lo[3:].split(".")
    full = "%s.%s.%s" % (a, b, cc)
    return full if full in NODES else "%s.%s" % (a, b)
def sid(no): return "s-" + no.replace(".", "-")

D, DEN = sim(SIM), sim(SIMEN)
TRANS = jd("translations_en.json")
ENQ = {}
for ex, d in DEN.items():
    for q in d["questions"]:
        ENQ["%s%d" % (ex, q["n"])] = {"q": q["q"], "opts": q["opts"], "why": q.get("why", "")}
for k, v in TRANS.items():
    ENQ.setdefault(k, {}).update({"q": v["q"], "opts": v["opts"]})

QS = []
for ex in sorted(D):
    for q in D[ex]["questions"]:
        no = node_of(q["lo"])
        QS.append(dict(ch=no[0], no=no, lo=q["lo"], k=q.get("k", ""), exam=ex, n=q["n"],
                       multi=bool(q.get("multi")), q=q["q"], opts=q["opts"],
                       ans=sorted(q["correct"]), why=q.get("why", ""), deep=q.get("deep", ""),
                       en=ENQ.get("%s%d" % (ex, q["n"]), {})))
QS.sort(key=lambda x: ([int(i) for i in x["no"].split(".")], x["exam"], x["n"]))

def para(t):
    """duz metni paragraf/pre bloklarina cevir (qfmt ile ayni mantik)"""
    return qhtml(t)

def bilingual(tr, en, cls=""):
    c = (" " + cls) if cls else ""
    out = '<div class="s-tr%s">%s</div>' % (c, tr)
    out += '<div class="s-en%s">%s</div>' % (c, en if en else tr)
    return out

def question(q, idx):
    en = q["en"]
    name = "q%d" % idx
    typ = "checkbox" if q["multi"] else "radio"
    lis = []
    for kk in sorted(q["opts"]):
        tr_t = esc(q["opts"][kk])
        en_t = esc(en.get("opts", {}).get(kk, q["opts"][kk]))
        lis.append('<li data-k="%s"><label><input type="%s" name="%s" value="%s">'
                   '<span class="k">%s)</span><span class="t">'
                   '<span class="x-tr">%s</span><span class="x-en">%s</span>'
                   '</span></label></li>' % (kk, typ, name, kk, kk, tr_t, en_t))
    mk = '<span class="mk">çoktan seçmeli</span>' if q["multi"] else ""
    lbl_tr = "%s %s" % (q["no"], TITLE.get(q["no"], ""))
    lbl_en = "%s %s" % (q["no"], TITLE_EN.get(q["no"], TITLE.get(q["no"], "")))
    why_tr = para(q["why"]) if q["why"] else ""
    why_en = para(en["why"]) if en.get("why") else why_tr
    deep = ('<details class="deep"><summary>'
            '<span class="x-tr">Ayrıntılı çözüm</span><span class="x-en">Detailed solution</span>'
            '</summary><div class="deepbody">%s</div></details>' % para(q["deep"])) if q["deep"] else ""
    return (
      '<article class="q" data-i="%d" data-ans="%s" data-multi="%d" data-lang="tr">'
      '<div class="qhead"><span class="num">%d</span>'
      '<span class="ref">Örnek Sınav %s &middot; <span class="x-tr">Soru</span>'
      '<span class="x-en">Question</span> %d</span>'
      '<span class="lo">%s &middot; %s</span>%s'
      '<span class="sw lg"><button type="button" class="on" data-l="tr">TR</button>'
      '<button type="button" data-l="en">EN</button></span></div>'
      '<div class="qtext"><div class="x-tr">%s</div><div class="x-en">%s</div></div>'
      '<ul class="opts">%s</ul>'
      '<div class="qact"><button type="button" class="show">'
      '<span class="x-tr">Cevabı göster</span><span class="x-en">Show answer</span></button></div>'
      '<div class="ansbox">'
      '<a class="tlink" href="%s#%s" target="_blank" rel="noopener">'
      '<span class="x-tr">%s</span><span class="x-en">%s</span></a>'
      '<p class="verdict"></p>'
      '<p class="correct"><span class="x-tr">Doğru cevap:</span>'
      '<span class="x-en">Correct answer:</span> <b>%s</b></p>'
      '<div class="why"><div class="x-tr">%s</div><div class="x-en">%s</div></div>%s'
      '<a class="simlink" href="%s" target="_blank" rel="noopener">'
      '<span class="x-tr">Soruyu simülatörde aç &#8599;</span>'
      '<span class="x-en">Open this question in the simulator &#8599;</span></a>'
      '</div></article>'
      % (idx, ",".join(q["ans"]), 1 if q["multi"] else 0, idx + 1,
         q["exam"], q["n"], q["lo"], q["k"], mk,
         para(q["q"]), para(en.get("q", q["q"])), "".join(lis),
         DERS, sid(q["no"]), esc(lbl_tr), esc(lbl_en),
         ", ".join(a.upper() for a in q["ans"]),
         why_tr, why_en, deep, SIMU))

JS = r"""
(function(){
  var body=document.body, KEY='ctfl-test-'+body.dataset.ch;
  var qs=[].slice.call(document.querySelectorAll('article.q'));
  var sets=[].slice.call(document.querySelectorAll('.qset'));
  var tabs=[].slice.call(document.querySelectorAll('.sets button'));
  var inst=document.getElementById('inst');
  var state={};
  try{ state=JSON.parse(localStorage.getItem(KEY)||'{}') }catch(e){ state={} }
  function save(){ try{ localStorage.setItem(KEY,JSON.stringify(state)) }catch(e){} }

  function picked(q){
    return [].slice.call(q.querySelectorAll('input:checked')).map(function(i){return i.value}).sort();
  }
  function grade(q){
    var want=q.dataset.ans.split(','), got=picked(q);
    return got.length && got.join(',')===want.join(',');
  }
  function reveal(q){
    var want=q.dataset.ans.split(','), got=picked(q);
    q.classList.add('rev');
    q.querySelectorAll('input').forEach(function(i){ i.disabled=true });
    q.querySelectorAll('ul.opts li').forEach(function(li){
      var k=li.dataset.k;
      if(want.indexOf(k)>=0) li.classList.add('right');
      else if(got.indexOf(k)>=0) li.classList.add('wrong');
    });
    var v=q.querySelector('.verdict');
    if(!got.length){ v.className='verdict nt';
      v.innerHTML='<span class="x-tr">Cevaplamadın.</span><span class="x-en">Not answered.</span>'; }
    else if(grade(q)){ v.className='verdict ok'; q.classList.add('ok');
      v.innerHTML='<span class="x-tr">✅ Doğru</span><span class="x-en">✅ Correct</span>'; }
    else { v.className='verdict no'; q.classList.add('no');
      v.innerHTML='<span class="x-tr">❌ Yanlış</span><span class="x-en">❌ Wrong</span>'; }
  }
  function score(){
    var a=0,c=0;
    qs.forEach(function(q){ if(picked(q).length){ a++; if(grade(q)) c++; } });
    var el=document.getElementById('score');
    el.innerHTML=a+'/'+qs.length+' &middot; <b>'+c+'</b> / <i>'+(a-c)+'</i>';
    sets.forEach(function(s,i){
      var all=[].slice.call(s.querySelectorAll('article.q'));
      tabs[i].classList.toggle('done', all.every(function(q){return picked(q).length}));
    });
  }
  function setLang(el,l){
    el.dataset.lang=l;
    el.querySelectorAll(':scope .sw.lg button').forEach(function(b){
      b.classList.toggle('on', b.dataset.l===l);
    });
  }
  function showSet(i){
    sets.forEach(function(s,j){ s.classList.toggle('on', i===j) });
    tabs.forEach(function(t,j){ t.classList.toggle('on', i===j) });
    try{ localStorage.setItem(KEY+'-set', i) }catch(e){}
    window.scrollTo({top:0,behavior:'instant'});
  }

  /* kayitli cevaplar */
  qs.forEach(function(q){
    var v=state[q.dataset.i];
    if(!v) return;
    v.split(',').forEach(function(k){
      var i=q.querySelector('input[value="'+k+'"]'); if(i) i.checked=true;
    });
    q.querySelectorAll('ul.opts li').forEach(function(li){
      li.classList.toggle('sel', v.split(',').indexOf(li.dataset.k)>=0);
    });
    if(state['r'+q.dataset.i]) reveal(q);
  });

  document.addEventListener('change', function(ev){
    var inp=ev.target.closest('article.q input'); if(!inp) return;
    var q=inp.closest('article.q');
    q.querySelectorAll('ul.opts li').forEach(function(li){
      li.classList.toggle('sel', !!li.querySelector('input:checked'));
    });
    state[q.dataset.i]=picked(q).join(',');
    save(); score();
    if(inst.checked){ reveal(q); state['r'+q.dataset.i]=1; save(); }
  });

  document.addEventListener('click', function(ev){
    var b=ev.target.closest('button'); if(!b) return;
    if(b.classList.contains('show')){
      var q=b.closest('article.q'); reveal(q); state['r'+q.dataset.i]=1; save(); return;
    }
    if(b.dataset.l!==undefined){
      var l=b.dataset.l;
      if(b.closest('#glob')){
        document.querySelectorAll('#glob button').forEach(function(x){x.classList.toggle('on',x.dataset.l===l)});
        body.dataset.lang=l; document.documentElement.lang=l;
        qs.forEach(function(q){ setLang(q,l) });
        try{ localStorage.setItem('ctfl-lang',l) }catch(e){}
      } else setLang(b.closest('article.q'), l);
      return;
    }
    if(b.dataset.set!==undefined){ showSet(+b.dataset.set); return; }
    if(b.classList.contains('finish')){
      var s=sets[+b.dataset.i], all=[].slice.call(s.querySelectorAll('article.q')), c=0;
      all.forEach(function(q){ reveal(q); state['r'+q.dataset.i]=1; if(grade(q)) c++; });
      var r=s.parentNode.querySelector('.setfoot[data-i="'+b.dataset.i+'"] .res');
      r.className='res '+(c*2>=all.length?'ok':'no');
      r.innerHTML='<span class="s-tr">Sonuç:</span><span class="s-en">Score:</span> '+c+' / '+all.length;
      save(); score(); return;
    }
    if(b.classList.contains('reset')){
      var s2=sets[+b.dataset.i];
      s2.querySelectorAll('article.q').forEach(function(q){
        q.className='q'; q.dataset.lang=body.dataset.lang;
        q.querySelectorAll('input').forEach(function(i){ i.checked=false; i.disabled=false });
        q.querySelectorAll('ul.opts li').forEach(function(li){ li.className='' });
        delete state[q.dataset.i]; delete state['r'+q.dataset.i];
      });
      var r2=s2.parentNode.querySelector('.setfoot[data-i="'+b.dataset.i+'"] .res');
      r2.className='res'; r2.textContent='';
      save(); score(); window.scrollTo({top:0,behavior:'instant'}); return;
    }
  });

  inst.addEventListener('change', function(){
    try{ localStorage.setItem('ctfl-inst', inst.checked?'1':'0') }catch(e){}
  });
  try{ if(localStorage.getItem('ctfl-inst')==='0') inst.checked=false;
       if(localStorage.getItem('ctfl-lang')==='en'){
         var gb=document.querySelector('#glob button[data-l="en"]'); if(gb) gb.click(); }
       var ss=+(localStorage.getItem(KEY+'-set')||0);
       if(ss>0 && ss<sets.length){ sets.forEach(function(s,j){s.classList.toggle('on',j===ss)});
                                   tabs.forEach(function(t,j){t.classList.toggle('on',j===ss)}); }
  }catch(e){}
  score();
})();
"""

PAGE = u"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<style>%(css)s</style>
</head>
<body%(battr)s>
%(hero)s
%(nav)s
<div class="wrap">%(main)s</div>
<div class="wrap"><footer class="tf">%(foot)s</footer></div>
%(script)s
</body>
</html>
"""

def hero(kick, h1, lede, stats):
    return ('<header class="th"><div class="wrap"><p class="kick">%s</p><h1>%s</h1>'
            '<p>%s</p><div class="stats">%s</div></div></header>'
            % (kick, h1, lede, "".join("<b>%s</b>" % x for x in stats)))

def chapter_page(ch):
    qs = [q for q in QS if q["ch"] == ch]
    nsets = (len(qs) + 9) // 10
    tabs = "".join('<button type="button" data-set="%d"%s>%s%d</button>'
                   % (i, ' class="on"' if i == 0 else '',
                      "Set ", i + 1) for i in range(nsets))
    body = []
    for i in range(nsets):
        chunk = qs[i * 10:(i + 1) * 10]
        items = "".join(question(q, i * 10 + j) for j, q in enumerate(chunk))
        body.append(
          '<section class="qset%s" data-set="%d"><div class="sethead"><h2>Set %d</h2>'
          '<span><span class="s-tr">%d soru &middot; soru %d&ndash;%d</span>'
          '<span class="s-en">%d questions &middot; question %d&ndash;%d</span></span></div>%s'
          '<div class="setfoot" data-i="%d">'
          '<button type="button" class="pri finish" data-i="%d">'
          '<span class="s-tr">Seti bitir ve puanı gör</span>'
          '<span class="s-en">Finish set and see the score</span></button>'
          '<button type="button" class="reset" data-i="%d">'
          '<span class="s-tr">Seti sıfırla</span><span class="s-en">Reset set</span></button>'
          '<span class="res"></span></div></section>'
          % (" on" if i == 0 else "", i, i + 1,
             len(chunk), i * 10 + 1, i * 10 + len(chunk),
             len(chunk), i * 10 + 1, i * 10 + len(chunk),
             items, i, i, i))
    nav = ('<nav class="bar"><div class="in"><div class="sets">%s</div>'
           '<span class="score" id="score"></span>'
           '<label class="chk"><input type="checkbox" id="inst" checked>'
           '<span class="s-tr">anında cevap</span><span class="s-en">instant answer</span></label>'
           '<span class="sw" id="glob"><button type="button" class="on" data-l="tr">TR</button>'
           '<button type="button" data-l="en">EN</button></span></div></nav>' % tabs)
    return PAGE % dict(
        title=u"%s. %s · Bölüm Testi" % (ch, CH_T[ch]),
        css=TCSS, battr=' data-lang="tr" data-ch="%s"' % ch,
        hero=hero(u"ISTQB CTFL v4.0 &middot; Bölüm Bazlı Test",
                  '<span class="s-tr">%s. %s</span><span class="s-en">%s. %s</span>'
                  % (ch, esc(CH_T[ch]), ch, esc(CH_E[ch])),
                  '<span class="s-tr">Bu konunun ders programındaki b&uuml;t&uuml;n sınav soruları, '
                  'onar soruluk setler halinde. İşaretledi&#287;inde cevabı hemen g&ouml;rebilir, '
                  'ya da anında cevabı kapatıp seti sonunda bitirebilirsin.</span>'
                  '<span class="s-en">Every exam question for this chapter, in sets of ten. '
                  'You can see the answer the moment you tick an option, or turn instant answers '
                  'off and finish the set first.</span>',
                  ['<span class="s-tr">%d soru</span><span class="s-en">%d questions</span>' % (len(qs), len(qs)),
                   '<span class="s-tr">%d set</span><span class="s-en">%d sets</span>' % (nsets, nsets),
                   '<span class="s-tr">8 sınavdan</span><span class="s-en">from 8 exams</span>']),
        nav=nav, main="".join(body),
        foot=('<span class="s-tr">Sorular resm&icirc; &ouml;rnek sınavlar A&ndash;D ve pratik setler '
              'E&ndash;H&#39;den alınmıştır. A&ccedil;ıklamalar '
              '<a href="%s" target="_blank" rel="noopener">sınav sim&uuml;lat&ouml;r&uuml;</a> ile aynıdır. '
              '&copy; ISTQB&reg;.</span>'
              '<span class="s-en">Questions are taken from the official sample exams A&ndash;D and the '
              'practice sets E&ndash;H. The explanations are the same as in the '
              '<a href="%s" target="_blank" rel="noopener">exam simulator</a>. &copy; ISTQB&reg;.</span>'
              % (SIMU, SIMU)),
        script="<script>%s</script>" % JS)

def hub_page():
    cards = []
    for ch in CHAPTERS:
        qs = [q for q in QS if q["ch"] == ch]
        nsets = (len(qs) + 9) // 10
        cards.append(
          '<a class="card" href="bolum-%s.html"><div class="n">%s</div>'
          '<h2><span class="s-tr">%s</span><span class="s-en">%s</span></h2>'
          '<p><span class="s-tr">Bu konunun ders programındaki b&uuml;t&uuml;n soruları, '
          'onar soruluk %d set.</span>'
          '<span class="s-en">Every question for this chapter, %d sets of ten.</span></p>'
          '<div class="meta"><span>%d soru</span><span>%d set</span></div></a>'
          % (ch, ch, esc(CH_T[ch]), esc(CH_E[ch]), nsets, nsets, len(qs), nsets))
    return PAGE % dict(
        title=u"Bölüm Bazlı Testler · ISTQB CTFL",
        css=TCSS, battr=' data-lang="tr"',
        hero=hero(u"ISTQB CTFL v4.0",
                  '<span class="s-tr">B&ouml;l&uuml;m Bazlı Testler</span>'
                  '<span class="s-en">Chapter Tests</span>',
                  '<span class="s-tr">Ders programındaki konuların soruları, konu konu ayrılmış halde. '
                  'Bir konuyu bitirdikten sonra yalnızca o konunun sorularıyla kendini sına.</span>'
                  '<span class="s-en">The syllabus questions, split by chapter. '
                  'Finish a chapter, then test yourself on just that chapter.</span>',
                  ['<span class="s-tr">%d konu hazır</span><span class="s-en">%d chapters ready</span>'
                   % (len(CHAPTERS), len(CHAPTERS)),
                   '<span class="s-tr">%d soru</span><span class="s-en">%d questions</span>'
                   % (sum(1 for q in QS if q["ch"] in CHAPTERS),
                      sum(1 for q in QS if q["ch"] in CHAPTERS))]),
        nav='<nav class="bar"><div class="in"><span class="score" id="score"></span>'
            '<span class="sw" id="glob" style="margin-left:auto">'
            '<button type="button" class="on" data-l="tr">TR</button>'
            '<button type="button" data-l="en">EN</button></span></div></nav>',
        main='<div class="cards">%s</div>' % "".join(cards),
        foot='<span class="s-tr">Diğer konular ders programında bitirildik&ccedil;e buraya eklenecek.</span>'
             '<span class="s-en">The remaining chapters will appear here as they are finished.</span>',
        script="""<script>
document.addEventListener('click',function(ev){
  var b=ev.target.closest('#glob button'); if(!b) return;
  var l=b.dataset.l;
  document.querySelectorAll('#glob button').forEach(function(x){x.classList.toggle('on',x.dataset.l===l)});
  document.body.dataset.lang=l; document.documentElement.lang=l;
  try{ localStorage.setItem('ctfl-lang',l) }catch(e){}
});
try{ if(localStorage.getItem('ctfl-lang')==='en')
       document.querySelector('#glob button[data-l=\"en\"]').click() }catch(e){}
</script>""")

# ---------- breadcrumb + sifre kapisi ----------
def block(src, a, b):
    i = src.index(a); j = src.index(b, i) + len(b)
    return src[i:j]
ref   = io.open(REF, encoding="utf-8").read()
HEAD  = block(ref, '<meta name="robots"', '</style>')
CRUMB = block(ref, '<!-- dz-breadcrumb -->', '</style>')
GATE  = block(ref, '<!-- deniz-pw-gate -->', '})();\n</script>')

def wrap(page, trail):
    crumb = re.sub(r'<li><a href="/deniz/">Study Hub</a></li>\s*<li><span aria-current="page">.*?</span></li>',
                   trail, CRUMB, count=1, flags=re.S)
    page = page.replace("</head>", HEAD + "\n</head>", 1)
    i = re.search(r"<body[^>]*>", page, re.I).end()
    return page[:i] + "\n" + crumb + "\n" + GATE + page[i:]

os.makedirs(OUTD, exist_ok=True)
HUB = '<li><a href="/deniz/">Study Hub</a></li><li><span aria-current="page">Bölüm Bazlı Testler</span></li>'
files = [("index.html", wrap(hub_page(), HUB))]
for ch in CHAPTERS:
    trail = ('<li><a href="/deniz/">Study Hub</a></li>'
             '<li><a href="/deniz/bolum_testleri/">Bölüm Bazlı Testler</a></li>'
             '<li><span aria-current="page">%s. %s</span></li>' % (ch, esc(CH_T[ch])))
    files.append(("bolum-%s.html" % ch, wrap(chapter_page(ch), trail)))
for name, html in files:
    io.open(os.path.join(OUTD, name), "w", encoding="utf-8").write(html)
    print("  %-14s %4d KB" % (name, len(html.encode("utf-8")) // 1024))
print("bolum testleri:", ", ".join("%s=%d soru" % (c, sum(1 for q in QS if q["ch"] == c))
                                   for c in CHAPTERS))
