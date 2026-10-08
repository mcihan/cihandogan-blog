# -*- coding: utf-8 -*-
"""_tree[_en].json -> data/syllabus_tree[_en].json + data/syllabus_body[_en].json

Kullanim: python3 blocks.py [en]"""
import re, json, io, os, sys

LANG = "_en" if len(sys.argv) > 1 and sys.argv[1] == "en" else ""

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
SURE = {"1":180,"2":130,"3":80,"4":390,"5":335,"6":20}

BUL = re.compile(r"^\s*[•▪]\s*(.*)$")
NUM = re.compile(r"^\s*(\d{1,2})\.\s+([A-ZÇĞİÖŞÜ].*)$" if not LANG else r"^\s*(\d{1,2})\.\s+([A-Z].*)$")

def to_blocks(lines):
    blocks, cur = [], None
    def flush():
        nonlocal cur
        if cur: blocks.append(cur); cur = None
    for raw in lines:
        ln = raw.rstrip()
        if not ln.strip():
            if cur and cur["t"] == "p": flush()
            continue
        m = BUL.match(ln)
        if m:
            if not cur or cur["t"] != "ul": flush(); cur = {"t":"ul","items":[]}
            cur["items"].append(m.group(1).strip()); continue
        m = NUM.match(ln)
        if m and len(ln) - len(ln.lstrip()) <= 6:
            if not cur or cur["t"] != "ol": flush(); cur = {"t":"ol","items":[]}
            cur["items"].append(m.group(2).strip()); continue
        if cur and cur["t"] in ("ul","ol"):
            if len(ln) - len(ln.lstrip()) >= 8:
                cur["items"][-1] += " " + ln.strip(); continue
            flush()
        if not cur: cur = {"t":"p","text":""}
        cur["text"] = (cur["text"] + " " + ln.strip()).strip()
    flush()
    return [b for b in blocks if b["t"] != "p" or len(b["text"]) > 25]

T = json.load(io.open(os.path.join(HERE, "_tree%s.json" % LANG), encoding="utf-8"))
NODES = {}
for c in T:
    for s in c["secs"]:
        s["blocks"] = to_blocks(s.pop("lines")); NODES[s["no"]] = s
        for sb in s["subs"]:
            sb["blocks"] = to_blocks(sb.pop("lines")); NODES[sb["no"]] = sb

def tgt(lo):
    a,b,cc = lo[3:].split(".")
    return "%s.%s.%s" % (a,b,cc) if "%s.%s.%s" % (a,b,cc) in NODES else "%s.%s" % (a,b)

QF = os.path.join(DATA, "questions_by_lo.json")
BY = json.load(io.open(QF, encoding="utf-8"))["byLo"] if os.path.exists(QF) else {}

tree = []
for c in T:
    tree.append(dict(no=c["no"], title=c["title"], minutes=SURE[c["no"]],
        keywords=[w.strip() for w in c["kw"].split(",") if w.strip()],
        los=[dict(id=l["id"], k=l["k"], text=l["text"], section=tgt(l["id"]),
                  questions=len(BY.get(l["id"], []))) for l in c["los"]],
        sections=[dict(no=s["no"], title=s["title"],
                       subsections=[dict(no=sb["no"], title=sb["title"]) for sb in s["subs"]])
                  for s in c["secs"]]))
body = {}
for c in T:
    for s in c["secs"]:
        body[s["no"]] = dict(title=s["title"], chapter=c["no"], blocks=s["blocks"])
        for sb in s["subs"]:
            body[sb["no"]] = dict(title=sb["title"], chapter=c["no"], blocks=sb["blocks"])

os.makedirs(DATA, exist_ok=True)
json.dump(tree, io.open(os.path.join(DATA,"syllabus_tree%s.json" % LANG),"w",encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(body, io.open(os.path.join(DATA,"syllabus_body%s.json" % LANG),"w",encoding="utf-8"), ensure_ascii=False, indent=1)
print("syllabus_tree%s.json + syllabus_body%s.json:" % (LANG, LANG), len(tree), "konu,", len(body), "bolum")
