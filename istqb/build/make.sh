#!/bin/sh
# Ders programi sayfasini bastan uretir. Repo kokunden ya da buradan calistirilabilir.
set -e
cd "$(dirname "$0")"
PDF="../docs/ISTQB_CTFL_Syllabus-v4.0.1-TR.pdf"
PDFEN="../docs/ISTQB_CTFL_Syllabus-v4.0.1-EN.pdf"

echo "1/6  PDF -> metin"          ; pdftotext -layout "$PDF" _syl.txt
                                   pdftotext -layout "$PDFEN" _syl_en.txt
echo "2/6  metin -> bolum agaci"  ; python3 parse.py >/dev/null; python3 parse_en.py >/dev/null
echo "3/6  sorular (simulatorden)"; python3 extract_questions.py
echo "4/6  agac -> data/*.json"   ; python3 blocks.py; python3 blocks.py en
echo "5/6  data -> syllabus.html" ; python3 build_site.py
echo "6/6  -> yayin kopyasi"      ; python3 publish.py
rm -f _syl.txt _syl_en.txt _tree.json _tree_en.json
echo "bitti."
