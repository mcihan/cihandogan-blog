#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISTQB calisma materyalinde arama. Kaynak: yayindaki HTML sayfalari.

Kullanim (repo kokunden):
  python3 istqb/tools/lookup.py sec 4.2.2          bolumun tam metni
  python3 istqb/tools/lookup.py lo  FL-4.2.2       ogrenme hedefi + bolum + soru sayisi
  python3 istqb/tools/lookup.py q   FL-4.2.2       o hedeften cikmis tum sorular (cevapsiz)
  python3 istqb/tools/lookup.py q   A21            tek soru (sinav harfi + numara)
  python3 istqb/tools/lookup.py ans A21            cevap + cozum (simulatorden)
  python3 istqb/tools/lookup.py find "karar tablosu"   konu metni + sorularda arama
  python3 istqb/tools/lookup.py toc                tum bolum agaci
"""
import sys, os, re, json, signal
from html.parser import HTMLParser

try:  # head/less ile borulandiginda sessizce bit
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SYL  = os.path.join(ROOT, "static/deniz/istqub/ders_programi_tr.html")
SIM  = os.path.join(ROOT, "static/deniz/istqub/questions_tr.html")
DATA = os.path.join(ROOT, "istqb/data")

def _read(p):
    with open(p, encoding="utf-8") as f: return f.read()

def _jd(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f: return json.load(f)

# ---------- HTML'den eleman cikarma ----------
class Grab(HTMLParser):
    """Verilen id'li elemani ve icerigini duz metne cevirir."""
    def __init__(self, want):
        super().__init__(convert_charrefs=True)
        self.want, self.depth, self.on, self.out, self.skip = want, 0, False, [], 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if not self.on and a.get("id") == self.want:
            self.on, self.depth, self.tag = True, 0, tag
        if self.on:
            if tag == self.tag: self.depth += 1
            if tag in ("script", "style"): self.skip += 1
            if tag in ("p", "li", "tr", "h2", "h3", "h4", "div", "summary", "details"):
                self.out.append("\n")
            if tag == "li": self.out.append("• ")
            if tag in ("td", "th"): self.out.append(" | ")
    def handle_endtag(self, tag):
        if not self.on: return
        if tag in ("script", "style"): self.skip -= 1
        if tag == self.tag:
            self.depth -= 1
            if self.depth == 0: self.on = False
    def handle_data(self, d):
        if self.on and not self.skip: self.out.append(d)
    def text(self):
        t = "".join(self.out)
        t = re.sub(r"[ \t]+", " ", t)
        t = re.sub(r"\n\s*\n+", "\n", t)
        return "\n".join(l.strip(" |") .strip() for l in t.split("\n") if l.strip(" |").strip())

def grab(path, elid):
    g = Grab(elid); g.feed(_read(path)); return g.text()

# ---------- komutlar ----------
def c_sec(no):
    t = grab(SYL, "s-" + no.replace(".", "-"))
    if not t: sys.exit("bolum bulunamadi: %s  (python3 istqb/tools/lookup.py toc)" % no)
    print(t)

def c_toc():
    tree = _jd("syllabus_tree.json")
    for c in tree:
        print("\n%s. %s  (%d dk, %d LO)" % (c["no"], c["title"], c["minutes"], len(c["los"])))
        for s in c["sections"]:
            print("   %-7s %s" % (s["no"], s["title"]))
            for sb in s["subsections"]:
                print("      %-8s %s" % (sb["no"], sb["title"]))

def c_lo(loid):
    loid = loid.upper()
    if not loid.startswith("FL-"): loid = "FL-" + loid
    for c in _jd("syllabus_tree.json"):
        for l in c["los"]:
            if l["id"] == loid:
                print("%s  [%s]  bolum %s" % (l["id"], l["k"], l["section"]))
                print(l["text"])
                print("\n%d soru. Tamami icin:  python3 istqb/tools/lookup.py q %s" % (l["questions"], loid))
                print("Konu metni icin:        python3 istqb/tools/lookup.py sec %s" % l["section"])
                return
    sys.exit("LO bulunamadi: " + loid)

def _print_q(q, n=None):
    print("\n--- %s  [%s %s]%s" % (q["ref"], q["set"], q["k"], "  ÇOKTAN SEÇMELİ" if q["multi"] else ""))
    print(q["q"])
    for k in sorted(q["opts"]): print("   %s) %s" % (k, q["opts"][k]))

def c_q(arg):
    BY = _jd("questions_by_lo.json")["byLo"]
    m = re.fullmatch(r"([A-Ha-h])\s*(\d{1,2})", arg.strip())
    if m:
        ex, n = m.group(1).upper(), int(m.group(2))
        for lo, v in BY.items():
            for q in v:
                if q["exam"] == ex and q["n"] == n:
                    print("ogrenme hedefi: %s" % lo); _print_q(q); return
        sys.exit("soru bulunamadi: " + arg)
    lo = arg.upper()
    if not lo.startswith("FL-"): lo = "FL-" + lo
    if lo not in BY: sys.exit("LO bulunamadi: " + lo)
    print("%s — %d soru" % (lo, len(BY[lo])))
    for q in BY[lo]: _print_q(q)

def c_ans(arg):
    """Cevap ve cozum yalnizca simulator sayfasindadir."""
    m = re.fullmatch(r"([A-Ha-h])\s*(\d{1,2})", arg.strip())
    if not m: sys.exit("kullanim: lookup.py ans A21")
    ex, n = m.group(1).upper(), int(m.group(2))
    src = _read(SIM)
    mm = re.search(r"const DATA\s*=\s*(\{.*?\});\s*\n", src, re.S)
    if not mm: sys.exit("simulator verisi okunamadi: " + SIM)
    D = json.loads(mm.group(1))
    for q in D[ex]["questions"]:
        if q["n"] == n:
            print("%s soru %d  [%s %s]" % (ex, n, q.get("lo"), q.get("k")))
            print("DOGRU: %s" % ", ".join(q["correct"]))
            print("\nGEREKCE:\n%s" % q.get("why", ""))
            if q.get("deep"): print("\nAYRINTILI COZUM:\n%s" % q["deep"])
            return
    sys.exit("soru yok: %s%d" % (ex, n))

def c_find(term):
    t = term.lower()
    print("=== KONULARDA")
    body = _jd("syllabus_body.json")
    for no, s in sorted(body.items(), key=lambda x: [int(y) for y in x[0].split(".")]):
        txt = " ".join(b.get("text", " ".join(b.get("items", []))) for b in s["blocks"])
        if t in txt.lower():
            i = txt.lower().index(t)
            print("  %-8s %-45s …%s…" % (no, s["title"][:45], txt[max(0,i-60):i+80].replace("\n", " ")))
    print("\n=== SORULARDA")
    BY = _jd("questions_by_lo.json")["byLo"]
    hits = [(q["ref"], lo, q["q"]) for lo, v in BY.items() for q in v if t in q["q"].lower()]
    for ref, lo, q in sorted(hits):
        print("  %-24s %-11s %s…" % (ref, lo, q[:70].replace("\n", " ")))
    if not hits: print("  (yok)")

CMD = {"sec": c_sec, "lo": c_lo, "q": c_q, "ans": c_ans, "find": c_find}
if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in CMD and sys.argv[1] != "toc":
        sys.exit(__doc__)
    if sys.argv[1] == "toc": c_toc()
    else: CMD[sys.argv[1]](" ".join(sys.argv[2:]))
