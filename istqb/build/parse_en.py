# -*- coding: utf-8 -*-
"""Ingilizce syllabus metni -> _tree_en.json (TR parser'in aynisi, EN kaliplariyla)."""
import re, io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = io.open(os.path.join(HERE, "_syl_en.txt"), encoding="utf-8").read().split("\n")

START, END = 513, 2709          # "1. Fundamentals of Testing" -> "7. References" oncesi
body = RAW[START:END]
for i, l in enumerate(body):    # ch2 basligi iki satira bolunmus
    if l.strip().endswith("Software Development Lifecycle") and "130 minutes" in body[i+1]:
        body[i] = l.rstrip() + " – 130 minutes"; body[i+1] = ""

FOOT = re.compile(r"Page \d+ of 78|International Software Testing Qualifications Board"
                  r"|^\s*Certified Tester\s*$|^\s*Foundation Level\s*$|^\s*v4\.0\.1\s")
def clean(ls): return [l.rstrip() for l in ls if not FOOT.search(l)]

CH  = re.compile(r"^\s{0,8}(\d)\.\s+(.+?)\s+[–-]\s*\d+\s*minutes")
SEC = re.compile(r"^\s{0,16}(\d\.\d)\.?\s+([A-Z].{2,70})\s*$")
SUB = re.compile(r"^\s{0,16}(\d\.\d\.\d)\.\s+([A-Z].{2,70})\s*$")
LO  = re.compile(r"^\s*(FL-\d\.\d\.\d)\s*\((K[123])\)\s*(.+)$")

chapters = []
cur_ch = cur_sec = cur_sub = None
mode = None
for ln in clean(body):
    m = CH.match(ln)
    if m:
        cur_ch = dict(no=m.group(1), title=m.group(2).strip(), kw="", los=[], secs=[])
        chapters.append(cur_ch); cur_sec = cur_sub = None; mode = "pre"
        lo_groups = set(); continue
    if cur_ch is None: continue
    m = LO.match(ln)
    if m:
        cur_ch["los"].append(dict(id=m.group(1), k=m.group(2), text=m.group(3).strip()))
        mode = "lo"; continue
    if mode == "lo" and cur_ch["los"] and re.match(r"^\s{4,}\S", ln) \
       and not SEC.match(ln) and not SUB.match(ln):
        cur_ch["los"][-1]["text"] += " " + ln.strip(); continue
    m = SUB.match(ln)
    if m and cur_sec is not None:
        cur_sub = dict(no=m.group(1), title=m.group(2).strip().rstrip("."), lines=[])
        cur_sec["subs"].append(cur_sub); mode = "body"; continue
    m = SEC.match(ln)
    if m:
        if mode in ("pre", "lo", "kw") and m.group(1) not in lo_groups:
            lo_groups.add(m.group(1)); continue
        if any(s["no"] == m.group(1) for s in cur_ch["secs"]): continue
        cur_sec = dict(no=m.group(1), title=m.group(2).strip().rstrip("."), lines=[], subs=[])
        cur_ch["secs"].append(cur_sec); cur_sub = None; mode = "body"; continue
    if mode in ("pre", "lo"):
        if ln.strip() == "Keywords": mode = "kw"; continue
        if ln.strip().startswith("Learning Objectives for Chapter"): mode = "lo"; continue
        continue
    if mode == "kw":
        if ln.strip().startswith("Learning Objectives for Chapter"): mode = "lo"; continue
        cur_ch["kw"] += " " + ln.strip(); continue
    tgt = cur_sub or cur_sec
    if tgt is not None: tgt["lines"].append(ln)

json.dump(chapters, io.open(os.path.join(HERE, "_tree_en.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
for c in chapters:
    print("C%s %-48s LO:%2d  sec:%d  sub:%d" % (
        c["no"], c["title"][:48], len(c["los"]), len(c["secs"]),
        sum(len(s["subs"]) for s in c["secs"])))
