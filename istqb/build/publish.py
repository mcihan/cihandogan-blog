# -*- coding: utf-8 -*-
"""syllabus.html -> breadcrumb + sifre kapisi -> static/deniz/istqub/ders_programi_tr.html"""
import re, io, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC  = os.path.join(HERE, "syllabus.html")
DST  = os.path.join(ROOT, "static/deniz/istqub/ders_programi_tr.html")
HASH = "2676a34d78a5a52bac7ea209cd8896af7f7eb5554d822d5058987a5ccd427480"   # Munnu123*
REF  = os.path.join(ROOT, "static/deniz/istqub/cozum_yontemleri_tr.html")   # kapi/breadcrumb kaynagi

def block(src, start, end):
    i = src.index(start); j = src.index(end, i) + len(end)
    return src[i:j]

ref = io.open(REF, encoding="utf-8").read()
HEAD  = block(ref, '<meta name="robots"', '</style>')            # noindex + pw-hide
CRUMB = block(ref, '<!-- dz-breadcrumb -->', '</style>')          # breadcrumb + stili
GATE  = block(ref, '<!-- deniz-pw-gate -->', '})();\n</script>')  # kapi + script
assert HASH in GATE, "kapi hash'i eslesmiyor"

page = io.open(SRC, encoding="utf-8").read()
# breadcrumb basligini bu sayfaya gore degistir
CRUMB = re.sub(r'<li><span aria-current="page">.*?</span></li>',
               '<li><span aria-current="page">Ders Programı &middot; T&uuml;rk&ccedil;e</span></li>',
               CRUMB, count=1, flags=re.S)
page = page.replace("</head>", HEAD + "\n</head>", 1)
i = re.search(r"<body[^>]*>", page, re.I).end()
page = page[:i] + "\n" + CRUMB + "\n" + GATE + page[i:]
io.open(DST, "w", encoding="utf-8").write(page)
print("yazildi:", os.path.relpath(DST, ROOT), len(page.encode("utf-8"))//1024, "KB")
