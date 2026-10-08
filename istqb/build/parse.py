# -*- coding: utf-8 -*-
import re, io, json, unicodedata

import os
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = io.open(os.path.join(HERE, "_syl.txt"), encoding="utf-8").read().split("\n")

FOOT = re.compile(r"turkishtestingboard|Tel:\s*\+90|Versiyon v4\.0|^\s*\d{1,3}\s*$")
def clean(lines):
    return [l.rstrip() for l in lines if not FOOT.search(l)]

# govde: 1. bolum basligindan Ek/Index'e kadar
START, END = 662, 2589          # govde: ilk bolum basligi -> Referanslar oncesi
body = RAW[START:END]
# ch2 basligi iki satira bolunmus: birlestir
for i,l in enumerate(body):
    if l.strip().endswith("Boyunca Test – 130") and body[i+1].strip() == "dakika":
        body[i] = l + " dakika"; body[i+1] = ""
print("govde satir:", len(body), "(%d-%d)" % (START, END))

CH = re.compile(r"^\s{0,8}(\d)\.\s+([^–\-]{4,70})\s*[–-]\s*\d+\s*dakika")
SEC = re.compile(r"^\s{0,16}(\d\.\d)\.?\s+([A-ZÇĞİÖŞÜ].{2,70})\s*$")
SUB = re.compile(r"^\s{0,16}(\d\.\d\.\d)\.\s+([A-ZÇĞİÖŞÜ].{2,70})\s*$")
LO  = re.compile(r"^\s*(FL-\d\.\d\.\d)\s*\((K[123])\)\s*(.+)$")

chapters = []
cur_ch = cur_sec = cur_sub = None
mode = None   # 'lo' | 'body'
for ln in clean(body):
    m = CH.match(ln)
    if m:
        cur_ch = dict(no=m.group(1), title=m.group(2).strip(), kw="", los=[], secs=[])
        chapters.append(cur_ch); cur_sec = cur_sub = None; mode = "lo"
        lo_groups = set(); continue
    if cur_ch is None: continue
    m = LO.match(ln)
    if m:
        cur_ch["los"].append(dict(id=m.group(1), k=m.group(2), text=m.group(3).strip()))
        mode = "lo"; continue
    if mode == "lo" and cur_ch["los"] and re.match(r"^\s{4,}\S", ln) and not SEC.match(ln) and not SUB.match(ln):
        # LO devam satiri
        if cur_ch["los"]: cur_ch["los"][-1]["text"] += " " + ln.strip()
        continue
    m = SUB.match(ln)
    if m and cur_sec is not None:
        cur_sub = dict(no=m.group(1), title=m.group(2).strip().rstrip("."), lines=[])
        cur_sec["subs"].append(cur_sub); mode = "body"; continue
    m = SEC.match(ln)
    if m:
        if mode == "lo" and m.group(1) not in lo_groups:
            # LO listesindeki grup basligi -- bolum degil
            lo_groups.add(m.group(1)); continue
        if any(s["no"] == m.group(1) for s in cur_ch["secs"]): continue
        cur_sec = dict(no=m.group(1), title=m.group(2).strip().rstrip("."), lines=[], subs=[])
        cur_ch["secs"].append(cur_sec); cur_sub = None; mode = "body"; continue
    if mode == "lo":
        if ln.strip().lower().startswith("anahtar kelime"): mode = "kw"; continue
        if ln.strip().startswith("Konu ") and "Hedefleri" in ln: continue
        continue
    if mode == "kw":
        if ln.strip().startswith("Konu ") and "Hedefleri" in ln: mode = "lo"; continue
        cur_ch["kw"] += " " + ln.strip(); continue
    tgt = cur_sub or cur_sec
    if tgt is not None: tgt["lines"].append(ln)

json.dump(chapters, io.open(os.path.join(HERE, "_tree.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=1)
for c in chapters:
    print("B%s %-45s LO:%2d  bolum:%d  altbolum:%d" % (
        c["no"], c["title"][:45], len(c["los"]), len(c["secs"]),
        sum(len(s["subs"]) for s in c["secs"])))
