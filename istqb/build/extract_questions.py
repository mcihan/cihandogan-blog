# -*- coding: utf-8 -*-
"""static/deniz/istqub/questions_tr.html -> data/questions_by_lo.json

Soru metni, siklar ve dogru sikkin HARFI alinir; gerekce ve ayrintili cozum alinmaz
(onlar yalnizca simulator sayfasinda durur)."""
import re, json, io, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SIM  = os.path.join(ROOT, "static/deniz/istqub/questions_tr.html")
SIMEN= os.path.join(ROOT, "static/deniz/istqub/questions.html")       # resmi A-D, ingilizce
TRANS= os.path.join(HERE, "..", "data", "translations_en.json")       # E-H, cevrilmis
DATA = os.path.join(HERE, "..", "data")

META = {"A":("Resmî Set v1.5","resmi"), "B":("Resmî Set v1.6","resmi"),
        "C":("Resmî Set v1.6","resmi"), "D":("Resmî Set v1.5","resmi"),
        "E":("Pratik Set v1.0","pratik"), "F":("Pratik Set v1.0","pratik"),
        "G":("Pratik Set v1.0","pratik"), "H":("Pratik Set v1.0","pratik")}

def _data(path):
    src = io.open(path, encoding="utf-8").read()
    m = re.search(r"const DATA\s*=\s*(\{.*?\});\s*\n", src, re.S)
    if not m: raise SystemExit("simulator verisi bulunamadi: " + path)
    return json.loads(m.group(1))

D  = _data(SIM)
# ingilizce metin: A-D resmi simulatorden, E-H cevrilmis dosyadan
ENQ = {}
for _ex, _d in _data(SIMEN).items():
    for _q in _d["questions"]:
        ENQ["%s%d" % (_ex, _q["n"])] = {"q": _q["q"], "opts": _q["opts"]}
ENQ.update(json.load(io.open(TRANS, encoding="utf-8")))

out = collections.defaultdict(list)
for ex in sorted(D):
    for q in D[ex]["questions"]:
        out[q["lo"]].append(dict(
            exam=ex, n=q["n"], k=q.get("k",""), multi=bool(q.get("multi")),
            q=q["q"], opts=q["opts"], ans=sorted(q["correct"]),
            en=ENQ.get("%s%d" % (ex, q["n"])),
            set=META[ex][0], kind=META[ex][1],
            ref=u"Örnek Sınav %s · Soru %d" % (ex, q["n"])))
for lo in out: out[lo].sort(key=lambda x: (x["exam"], x["n"]))

payload = {"meta": {"exams": {e: {"label": u"Örnek Sınav "+e, "set": META[e][0],
                                  "kind": META[e][1]} for e in sorted(D)},
                    "total": sum(len(v) for v in out.values()), "los": len(out)},
           "byLo": dict(out)}
os.makedirs(DATA, exist_ok=True)
io.open(os.path.join(DATA,"questions_by_lo.json"),"w",encoding="utf-8").write(
    json.dumps(payload, ensure_ascii=False, separators=(",",":")))
ne = sum(1 for v in out.values() for q in v if q.get("en"))
print("questions_by_lo.json:", payload["meta"]["total"], "soru,", payload["meta"]["los"], "LO,", ne, "ingilizce")
