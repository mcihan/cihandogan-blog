# -*- coding: utf-8 -*-
"""Soru metnini HTML'e cevir: satir sonlari, pipe tablolari, kod bloklari."""
import re, html

def esc(s): return html.escape(s, quote=False)

def _table(rows):
    cells = [[c.strip() for c in r.split("|")] for r in rows]
    w = max(len(r) for r in cells)
    out = ['<div class="qscroll"><table class="qtbl">']
    for i, r in enumerate(cells):
        r = r + [""] * (w - len(r))
        tag = "th" if i == 0 else "td"
        out.append("<tr>" + "".join(
            '<%s>%s</%s>' % (tag, esc(c) or "&nbsp;", tag) for c in r) + "</tr>")
    out.append("</table></div>")
    return "".join(out)

def qhtml(q):
    lines = q.split("\n")
    out, para, tbl = [], [], []
    def flush_p():
        if para: out.append("<p>" + esc(" ".join(para)) + "</p>"); para.clear()
    def flush_t():
        if tbl: out.append(_table(tbl)); tbl.clear()
    for ln in lines:
        s = ln.rstrip()
        if "|" in s and s.strip():
            flush_p(); tbl.append(s.strip()); continue
        flush_t()
        if not s.strip(): flush_p(); continue
        if re.match(r"^\s*[-•]\s+", s) or re.match(r"^\s*(TC|AC|R|S|T)\d+\s*[:.)]", s):
            flush_p(); out.append("<p class=\"qline\">" + esc(s.strip()) + "</p>"); continue
        para.append(s.strip())
    flush_p(); flush_t()
    return "".join(out) or "<p>" + esc(q) + "</p>"
