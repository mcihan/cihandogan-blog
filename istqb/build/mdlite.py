# -*- coding: utf-8 -*-
"""Kolay anlatim markdown'u -> HTML.  Kucuk ve amaca ozel bir donusturucu:
basliklar, tablolar, listeler, alinti, kod blogu, yatay cizgi, kalin, kod."""
import re, html as _h

def esc(s):
    return _h.escape(s, quote=False)

_B  = re.compile(r"\*\*(.+?)\*\*", re.S)
_C  = re.compile(r"`([^`]+)`")
_I  = re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])")

def inline(s):
    s = esc(s)
    out, last = [], 0
    for m in _C.finditer(s):                     # once kod: icinde ** islenmesin
        seg = s[last:m.start()]
        out.append(_I.sub(r"<em>\1</em>", _B.sub(r"<strong>\1</strong>", seg)))
        out.append("<code>%s</code>" % m.group(1))
        last = m.end()
    seg = s[last:]
    out.append(_I.sub(r"<em>\1</em>", _B.sub(r"<strong>\1</strong>", seg)))
    return "".join(out)

_SEP = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")

def _cells(line):
    t = line.strip()
    if t.startswith("|"): t = t[1:]
    if t.endswith("|"):   t = t[:-1]
    return [c.strip() for c in t.split("|")]

def render(md):
    lines = md.replace("\r\n", "\n").split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        ln = lines[i]
        s  = ln.strip()

        if not s:
            i += 1; continue

        if s.startswith("```"):                             # kod blogu
            lang = s[3:].strip()
            i += 1; buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            out.append('<pre class="ez-pre"%s><code>%s</code></pre>'
                       % (' data-lang="%s"' % esc(lang) if lang else "",
                          esc("\n".join(buf))))
            continue

        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):          # yatay cizgi
            out.append('<hr class="ez-hr">'); i += 1; continue

        m = re.match(r"^(#{2,6})\s+(.*)$", s)               # baslik
        if m:
            lv = min(len(m.group(1)) + 1, 6)                # ## -> h3
            out.append('<h%d class="ez-h">%s</h%d>' % (lv, inline(m.group(2)), lv))
            i += 1; continue

        if s.startswith("|") and i + 1 < n and _SEP.match(lines[i + 1]):
            head = _cells(ln); i += 2; rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(_cells(lines[i])); i += 1
            w = len(head)
            th = "".join("<th>%s</th>" % inline(c) for c in head)
            tb = "".join("<tr>%s</tr>" % "".join(
                    "<td>%s</td>" % inline(r[j] if j < len(r) else "") for j in range(w))
                 for r in rows)
            out.append('<div class="ez-tw"><table class="ez-t"><thead><tr>%s</tr></thead>'
                       '<tbody>%s</tbody></table></div>' % (th, tb))
            continue

        if s.startswith("> "):                              # alinti / altin kural
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip()); i += 1
            out.append('<blockquote class="ez-q">%s</blockquote>'
                       % "<br>".join(inline(x) for x in buf if x))
            continue

        if re.match(r"^[-*+]\s+", s):                       # madde listesi
            items = []
            while i < n and re.match(r"^\s*[-*+]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*+]\s+", "", lines[i])); i += 1
            out.append('<ul class="ez-ul">%s</ul>'
                       % "".join("<li>%s</li>" % inline(x) for x in items))
            continue

        if re.match(r"^\d+[.)]\s+", s):                     # numarali liste
            items = []
            while i < n and re.match(r"^\s*\d+[.)]\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+[.)]\s+", "", lines[i])); i += 1
            out.append('<ol class="ez-ol">%s</ol>'
                       % "".join("<li>%s</li>" % inline(x) for x in items))
            continue

        buf = []                                            # paragraf
        while i < n and lines[i].strip() and not re.match(
                r"^\s*([-*+]\s|\d+[.)]\s|>|\||#{2,6}\s|```|-{3,}$)", lines[i]):
            buf.append(lines[i].strip()); i += 1
        out.append("<p>%s</p>" % inline(" ".join(buf)))
    return "".join(out)
