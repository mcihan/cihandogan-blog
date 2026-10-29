const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const SRC = '/home/claude/repo/static/deniz/istqub/questions_tr.html';
const OUT = '/home/claude/sinavpdf/ISTQB-TR-Sinavlar.pdf';
const src = fs.readFileSync(SRC, 'utf8');
const DATA = JSON.parse(src.match(/const DATA\s*=\s*(\{[\s\S]*?\});\s*\n/)[1]);
const SECTIONS = JSON.parse(src.match(/const SECTIONS\s*=\s*(\{[\s\S]*?\});\s*\n/)[1]);
eval(fs.readFileSync(path.join(__dirname, 'fmt.js'), 'utf8'));   // esc, fmtQ, tableHtml

const EXC = {A:'#818cf8',B:'#38bdf8',C:'#c084fc',D:'#f472b6',
             E:'#34d399',F:'#fbbf24',G:'#fb7185',H:'#2dd4bf'};
const SETNAME = ex => DATA[ex].version;

/* ---------------- icerik ---------------- */
let body = '';

// kapak
body += `<section class="cover">
  <p class="kick">ISTQB&reg; CTFL v4.0 &middot; T&uuml;rk&ccedil;e</p>
  <h1>Sekiz Sınav<br>320 Soru</h1>
  <p class="lede">A&ndash;D ISTQB'nin resm&icirc; &ouml;rnek sınavları, E&ndash;H aynı yapıya g&ouml;re
    hazırlanmış pratik setler. Her sınav 40 soru; ger&ccedil;eğinde 60 dakika, ana dili İngilizce
    olmayan adaylarda 75 dakika. Ge&ccedil;me notu 26/40.</p>
  <div class="cov-ex">${Object.keys(DATA).map(ex =>
    `<span style="--ec:${EXC[ex]}"><b>${ex}</b>${DATA[ex].questions.length} soru</span>`).join('')}</div>
  <p class="covnote">Cevap anahtarı ve gerek&ccedil;eler en sonda. &Ccedil;&ouml;zerken oraya bakma.</p>
</section>`;

// icindekiler
body += `<section class="toc">
  <h2>İ&ccedil;indekiler</h2>
  <div class="tocg">${Object.keys(DATA).map(ex =>
    `<a href="#ex-${ex}" style="--ec:${EXC[ex]}"><b>${ex}</b><span>&Ouml;rnek Sınav ${ex}</span>
      <i>${DATA[ex].questions.length} soru</i></a>`).join('')}</div>
  <h2 class="k">Cevap anahtarı</h2>
  <div class="tocg">${Object.keys(DATA).map(ex =>
    `<a href="#key-${ex}" style="--ec:${EXC[ex]}"><b>${ex}</b><span>Cevaplar ${ex}</span>
      <i>gerek&ccedil;eli</i></a>`).join('')}</div>
</section>`;

// sinavlar
for (const ex of Object.keys(DATA)) {
  const qs = DATA[ex].questions;
  body += `<section class="exam" id="ex-${ex}" style="--ec:${EXC[ex]}">
    <div class="exhead"><div class="exn">${ex}</div>
      <div><h2>&Ouml;rnek Sınav ${ex}</h2>
      <p>${qs.length} soru &middot; ${esc(SETNAME(ex))} &middot; 26/40 ge&ccedil;me notu</p></div></div>`;
  for (const q of qs) {
    const multi = q.multi ? `<span class="mc">İKİ şık se&ccedil;in</span>` : '';
    body += `<article class="q">
      <div class="qh"><span class="qn">${q.n}</span>${multi}
        <span class="lo">${q.lo} &middot; ${q.k}</span></div>
      <div class="qt">${fmtQ(q.q)}</div>
      <ul class="op">${Object.keys(q.opts).map(L =>
        `<li><b>${L}</b><span>${esc(q.opts[L])}</span></li>`).join('')}</ul>
    </article>`;
  }
  body += `</section>`;
}

// cevap anahtari
body += `<section class="keyhead"><h2>Cevap Anahtarı</h2>
  <p>Her sınav i&ccedil;in doğru şık ve tek paragraflık gerek&ccedil;e. Ayrıntılı &ccedil;&ouml;z&uuml;mler
     sim&uuml;lat&ouml;rde.</p></section>`;
for (const ex of Object.keys(DATA)) {
  body += `<section class="key" id="key-${ex}" style="--ec:${EXC[ex]}">
    <h3><span class="exn sm">${ex}</span>&Ouml;rnek Sınav ${ex}</h3>
    <div class="kgrid">${DATA[ex].questions.map(q =>
      `<div class="kr"><span class="kn">${q.n}</span>
        <span class="ka">${q.correct.map(c=>c.toUpperCase()).join(', ')}</span>
        <span class="kw">${esc(q.why||'')}</span></div>`).join('')}</div></section>`;
}

/* ---------------- stil: koyu, goz yormayan ---------------- */
const CSS = `
:root{
  --bg:#14161d;            /* sicak koyu gri, saf siyah degil */
  --surface:#1b1e27;
  --surface2:#20242f;
  --ink:#d7dae3;           /* saf beyaz degil, kontrast ~11:1 */
  --dim:#9aa0b0;
  --line:#2c313e;
  --acc:#9aa6ff;
  --good:#5fd3a6;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",sans-serif;
}
@page{ size:150mm 250mm; margin:0; }
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg)}
body{font-family:var(--sans);color:var(--ink);font-size:11.2pt;line-height:1.55;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}

/* kapak */
.cover{min-height:250mm;padding:18mm 11mm;display:flex;flex-direction:column;justify-content:center;
  break-after:page;background:linear-gradient(160deg,#1b2040 0%,#171a28 55%,#13201f 100%)}
.cover .kick{margin:0 0 .7rem;font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;
  font-weight:800;color:var(--acc)}
.cover h1{margin:0 0 .9rem;font-size:2.5rem;line-height:1.05;font-weight:900;letter-spacing:-.02em;color:#e9ebf2}
.cover .lede{margin:0 0 1.6rem;color:var(--dim);font-size:.95rem;max-width:46ch}
.cov-ex{display:grid;grid-template-columns:repeat(4,1fr);gap:.5rem}
.cov-ex span{border:1px solid var(--line);border-radius:11px;padding:.5rem .3rem;text-align:center;
  font-size:.7rem;color:var(--dim);background:rgba(255,255,255,.03)}
.cov-ex b{display:block;font-size:1.15rem;font-weight:900;color:var(--ec);margin-bottom:.1rem}
.covnote{margin:1.7rem 0 0;font-size:.8rem;color:var(--dim);border-left:2px solid var(--acc);padding-left:.7rem}

/* icindekiler */
.toc{break-after:page;padding:10mm 8mm}
.toc h2{margin:0 0 .7rem;font-size:1.35rem;font-weight:900;color:#e9ebf2}
.toc h2.k{margin-top:1.5rem}
.tocg{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.45rem}
.tocg a{display:grid;grid-template-columns:28px minmax(0,1fr);gap:.55rem;align-items:center;
  text-decoration:none;color:var(--ink);border:1px solid var(--line);border-radius:11px;
  padding:.45rem .55rem;background:var(--surface)}
.tocg b{width:28px;height:28px;border-radius:8px;display:flex;align-items:center;justify-content:center;
  font-size:.9rem;font-weight:900;color:#12141b;background:var(--ec)}
.tocg span{font-size:.84rem;font-weight:700;line-height:1.2}
.tocg i{grid-column:2;font-style:normal;font-size:.7rem;color:var(--dim);font-family:var(--mono)}

/* sinav basligi */
.exam{break-before:page;padding:6mm 7mm 8mm}
.exhead{display:flex;gap:.7rem;align-items:center;margin-bottom:1rem;break-after:avoid}
.exn{width:40px;height:40px;flex:none;border-radius:12px;display:flex;align-items:center;justify-content:center;
  font-size:1.3rem;font-weight:900;color:#12141b;background:var(--ec)}
.exn.sm{width:26px;height:26px;font-size:.9rem;border-radius:8px;margin-right:.5rem}
.exhead h2{margin:0;font-size:1.3rem;font-weight:900;letter-spacing:-.015em;color:#e9ebf2}
.exhead p{margin:.1rem 0 0;font-size:.78rem;color:var(--dim);font-family:var(--mono)}

/* soru */
.q{background:var(--surface);border:1px solid var(--line);border-radius:13px;
  padding:.65rem .8rem .7rem;margin-bottom:.6rem;break-inside:avoid}
.qh{display:flex;align-items:center;gap:.45rem;margin-bottom:.35rem;flex-wrap:wrap}
.qn{min-width:24px;height:22px;padding:0 .35rem;border-radius:7px;display:flex;align-items:center;
  justify-content:center;font-family:var(--mono);font-size:.76rem;font-weight:800;
  color:var(--ec);background:color-mix(in srgb,var(--ec) 16%,transparent)}
.qh .lo{margin-left:auto;font-family:var(--mono);font-size:.66rem;color:var(--dim)}
.mc{font-size:.66rem;font-weight:800;color:#f0b86e;background:rgba(240,184,110,.14);
  border-radius:99px;padding:.04rem .5rem}
.qt{font-size:.93rem;margin-bottom:.45rem}
.qt .ptxt{white-space:pre-wrap;display:block}
.tblwrap{overflow:hidden;margin:.4rem 0;border:1px solid var(--line);border-radius:9px}
table.qtbl{border-collapse:collapse;width:100%;font-size:.78rem;font-family:var(--mono)}
table.qtbl th{background:var(--surface2);color:var(--acc);font-weight:800;text-align:left;
  padding:.24rem .45rem;border-bottom:1px solid var(--line)}
table.qtbl td{padding:.22rem .45rem;border-bottom:1px solid var(--line);color:var(--ink)}
table.qtbl tr:last-child td{border-bottom:0}
ul.op{list-style:none;margin:0;padding:0;display:grid;gap:.22rem}
ul.op li{display:grid;grid-template-columns:20px minmax(0,1fr);gap:.5rem;align-items:start;
  background:var(--surface2);border:1px solid var(--line);border-radius:9px;
  padding:.33rem .5rem;font-size:.88rem;break-inside:avoid}
ul.op b{font-family:var(--mono);font-size:.76rem;font-weight:800;color:var(--dim);
  text-align:center;line-height:1.5;text-transform:uppercase}

/* cevap anahtari */
.keyhead{break-before:page;padding:8mm 7mm 2mm}
.keyhead h2{margin:0 0 .3rem;font-size:1.6rem;font-weight:900;color:#e9ebf2}
.keyhead p{margin:0;color:var(--dim);font-size:.85rem;max-width:48ch}
.key{padding:2mm 7mm 5mm;break-before:page}
.key h3{display:flex;align-items:center;margin:0 0 .55rem;font-size:1.05rem;font-weight:900;
  color:#e9ebf2;break-after:avoid}
.kgrid{display:grid;gap:.26rem}
.kr{display:grid;grid-template-columns:22px 30px minmax(0,1fr);gap:.5rem;align-items:start;
  border-bottom:1px solid var(--line);padding:.26rem 0;break-inside:avoid}
.kn{font-family:var(--mono);font-size:.74rem;color:var(--dim);text-align:right;line-height:1.5}
.ka{font-family:var(--mono);font-size:.8rem;font-weight:900;color:var(--good);line-height:1.45}
.kw{font-size:.76rem;color:var(--dim);line-height:1.45}
`;

const html = `<!doctype html><html lang="tr"><head><meta charset="utf-8">
<title>ISTQB CTFL · Türkçe Sınavlar</title><style>${CSS}</style></head><body>${body}</body></html>`;
fs.writeFileSync('/home/claude/sinavpdf/_doc.html', html);

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 600, height: 1000 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file:///home/claude/sinavpdf/_doc.html', { waitUntil: 'load' });
  await p.emulateMedia({ media: 'print', colorScheme: 'dark' });
  await p.waitForTimeout(400);
  const over = await p.evaluate(() => {
    const lim = document.body.clientWidth + 2, out = [];
    document.querySelectorAll('body *').forEach(e => {
      if (e.getBoundingClientRect().width > lim) out.push(e.tagName + '.' + (e.className||'').toString().slice(0,24));
    });
    return out.slice(0, 8);
  });
  await p.pdf({ path: OUT, width: '150mm', height: '250mm', printBackground: true,
                preferCSSPageSize: true, outline: true, tagged: true,
                margin: { top:'0mm', right:'0mm', bottom:'0mm', left:'0mm' } });
  console.log('soru:', Object.values(DATA).reduce((a,d)=>a+d.questions.length,0),
              '| tasma:', over.length ? over : 'yok', '| hata:', errs.length);
  await b.close();
})();
