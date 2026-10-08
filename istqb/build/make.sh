#!/bin/sh
# Ders programi sayfasini bastan uretir. Repo kokunden ya da buradan calistirilabilir.
set -e
cd "$(dirname "$0")"
PDF="../docs/ISTQB_CTFL_Syllabus-v4.0.1-TR.pdf"

echo "1/5  PDF -> metin"          ; pdftotext -layout "$PDF" _syl.txt
echo "2/5  metin -> bolum agaci"  ; python3 parse.py
echo "3/5  sorular (simulatorden)"; python3 extract_questions.py
echo "4/5  agac -> data/*.json"   ; python3 blocks.py
echo "5/5  data -> syllabus.html" ; python3 build_site.py
echo "      -> yayin kopyasi"     ; python3 publish.py
rm -f _syl.txt _tree.json
echo "bitti."
