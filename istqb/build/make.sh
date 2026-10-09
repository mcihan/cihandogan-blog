#!/bin/sh
# Ders programi sayfasini bastan uretir. Repo kokunden ya da buradan calistirilabilir.
set -e
cd "$(dirname "$0")"
PDF="../docs/ISTQB_CTFL_Syllabus-v4.0.1-TR.pdf"
PDFEN="../docs/ISTQB_CTFL_Syllabus-v4.0.1-EN.pdf"

echo "1/7  PDF -> metin"          ; pdftotext -layout "$PDF" _syl.txt
                                   pdftotext -layout "$PDFEN" _syl_en.txt
echo "2/7  metin -> bolum agaci"  ; python3 parse.py >/dev/null; python3 parse_en.py >/dev/null
echo "3/7  sorular (simulatorden)"; python3 extract_questions.py
echo "4/7  agac -> data/*.json"   ; python3 blocks.py; python3 blocks.py en
echo "5/7  data -> syllabus.html" ; python3 build_site.py
echo "6/7  -> yayin kopyasi"      ; python3 publish.py
echo "7/7  bolum bazli testler"   ; python3 build_tests.py
rm -f _syl.txt _syl_en.txt _tree.json _tree_en.json
echo "bitti."
