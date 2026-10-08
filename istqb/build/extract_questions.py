# -*- coding: utf-8 -*-
"""static/deniz/istqub/questions_tr.html -> data/questions_by_lo.json  (cevapsiz)"""
import re, json, io, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SIM  = os.path.join(ROOT, "static/deniz/istqub/questions_tr.html")
DATA = os.path.join(HERE, "..", "data")

META = {"A":("Resmî Set v1.5","resmi"), "B":("Resmî Set v1.6","resmi"),
        "C":("Resmî Set v1.6","resmi"), "D":("Resmî Set v1.5","resmi"),
        "E":("Pratik Set v1.0","pratik"), "F":("Pratik Set v1.0","pratik"),
        "G":("Pratik Set v1.0","pratik"), "H":("Pratik Set v1.0","pratik")}

src = io.open(SIM, encoding="utf-8").read()
m = re.search(r"const DATA\s*=\s*(\{.*?\});\s*\n", src, re.S)
if not m: raise SystemExit("simulator verisi bulunamadi: " + SIM)
D = json.loads(m.group(1))

out = collections.defaultdict(list)
for ex in sorted(D):
    for q in D[ex]["questions"]:
        out[q["lo"]].append(dict(
            exam=ex, n=q["n"], k=q.get("k",""), multi=bool(q.get("multi")),
            q=q["q"], opts=q["opts"], set=META[ex][0], kind=META[ex][1],
            ref=u"Örnek Sınav %s · Soru %d" % (ex, q["n"])))
for lo in out: out[lo].sort(key=lambda x: (x["exam"], x["n"]))

payload = {"meta": {"exams": {e: {"label": u"Örnek Sınav "+e, "set": META[e][0],
                                  "kind": META[e][1]} for e in sorted(D)},
                    "total": sum(len(v) for v in out.values()), "los": len(out)},
           "byLo": dict(out)}
os.makedirs(DATA, exist_ok=True)
io.open(os.path.join(DATA,"questions_by_lo.json"),"w",encoding="utf-8").write(
    json.dumps(payload, ensure_ascii=False, separators=(",",":")))
print("questions_by_lo.json:", payload["meta"]["total"], "soru,", payload["meta"]["los"], "LO")
