const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1100, height: 1400 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + require('path').resolve(__dirname, 'syllabus.html') + '', { waitUntil: 'load' });
  await p.waitForTimeout(600);

  const info = await p.evaluate(() => {
    const body = document.body;
    body.dataset.lang = 'tr';
    document.querySelectorAll('section[data-no]').forEach(s => { s.dataset.lang='tr'; s.dataset.ver='o'; });

    // ekrana ozgu parcalar
    ['aside', 'nav.top', '.nores', '.vtools', '.qref .lang', '#glob', '#gver', '.srch', '.menubtn']
      .forEach(sel => document.querySelectorAll(sel).forEach(e => e.remove()));
    // resmi metin + kolay anlatim, ikisi de dursun; her birine etiket
    document.querySelectorAll('.body').forEach(bd => {
      const og = bd.querySelector(':scope > .og'), ez = bd.querySelector(':scope > .ez');
      if (og && ez) og.insertAdjacentHTML('beforebegin',
        '<div class="vlabel og-l">Resm\u00ee metin</div>');
      if (ez) ez.insertAdjacentHTML('beforebegin',
        '<div class="vlabel ez-l">Kolay k\u0131s\u0131m</div>');
    });
    document.querySelectorAll('.s-en, .x-en, .l-en').forEach(e => e.remove());  // yalnizca turkce

    // akordiyonlari ac
    document.querySelectorAll('details.qa, details.gl').forEach(d => d.open = true);

    // cevaplari topla, sayfadan cikar
    const key = [];
    document.querySelectorAll('section[data-no]').forEach(sec => {
      const no = sec.dataset.no;
      sec.querySelectorAll('.qitem').forEach(q => {
        const ref = q.querySelector('.qref .ex')?.textContent.trim() || '';
        const av  = q.querySelector('details.ans .av')?.textContent.replace(/\s+/g,' ').replace('Cevap:','').trim() || '';
        if (ref) key.push({ no, ref, av });
      });
      sec.querySelectorAll('details.ans').forEach(d => d.remove());
    });

    // kapak + cevap anahtari icin bilgi
    const secs = [...document.querySelectorAll('section[data-no]')].length;
    const qn   = document.querySelectorAll('.qitem').length;
    const chaps = [...document.querySelectorAll('.chap')].map(c => ({
      no: c.id.slice(1),
      title: c.querySelector('.chead h2')?.textContent.trim() || '',
      secs: [...c.querySelectorAll('section[data-no] > .sh')].map(sh => ({
        no: sh.querySelector('.num')?.textContent.trim() || '',
        t:  (sh.querySelector('h3,h4')?.textContent || '').trim(),
        sub: sh.parentElement.classList.contains('sub')
      }))
    }));
    return { key, secs, qn, chaps };
  });

  // ---- icindekiler ----
  const toc = `
  <div class="tocpage">
    <h2 class="toch">İçindekiler</h2>
    ${info.chaps.map(c => `
      <div class="tocg"><div class="tocc"><b>${c.no}</b>${c.title}</div>
        ${c.secs.map(s2 => `<div class="tocs${s2.sub ? ' sub' : ''}"><i>${s2.no}</i>${s2.t}</div>`).join('')}
      </div>`).join('')}
    <div class="tocg"><div class="tocc"><b>✓</b>Cevap Anahtarı</div></div>
  </div>`;
  await p.evaluate(h => { document.querySelector('main').insertAdjacentHTML('afterbegin', h); }, toc);

  // ---- cevap anahtari ----
  const byCh = {};
  info.key.forEach(k => { const c = k.no[0]; (byCh[c] = byCh[c] || []).push(k); });
  const keyHtml = `
  <div class="chap keypage" id="cevap-anahtari">
    <div class="chead"><div class="n">✓</div><div><h2>Cevap Anahtarı</h2>
      <div class="meta">${info.qn} soru &middot; konu konu</div></div></div>
    ${Object.keys(byCh).sort().map(c => `
      <section class="sec"><div class="sh"><span class="num">${c}</span><h3>${c}. ${(info.chaps.find(x=>x.no===c)||{}).title||''}</h3></div>
        <div class="body"><table class="keyt"><tbody>${
          byCh[c].map(k => `<tr><td class="kno">${k.no}</td><td class="kref">${k.ref}</td><td class="kav">${k.av}</td></tr>`).join('')
        }</tbody></table></div></section>`).join('')}
  </div>`;
  await p.evaluate(h => { document.querySelector('main').insertAdjacentHTML('beforeend', h); }, keyHtml);

  // ---- baski stili ----
  await p.addStyleTag({ content: `
    @page { size: A4; margin: 0.1mm; }
    /* +2px: rem tabanli her sey html'den, duz metin body'den olcekleniyor */
    html { scroll-behavior:auto; font-size:18px; }
    body { background:#fff !important; font-size:16px; }
    .shell { display:block !important; max-width:none !important; padding:2mm 3mm !important; }
    main { min-width:0; }
    header.hero { break-after:page; padding:2.5rem 1.6rem !important; }
    header.hero .hin { max-width:none; }
    .chap { break-before:page; }
    .chap:first-of-type { break-before:auto; }
    section.sec, section.sub { break-inside:auto; }
    .sh { break-after:avoid; }
    .body { box-shadow:none !important; break-inside:auto; }
    .qitem { break-inside:avoid; }
    .lobox, .kws { break-inside:avoid; }
    details.qa > summary, details.gl > summary { break-after:avoid; }
    details.qa, details.gl { break-inside:auto; }
    .glwrap { grid-template-columns:repeat(3,minmax(0,1fr)) !important; }
    .glwrap .g { break-inside:avoid; }
    table.ez-t, .ez-tw { break-inside:auto; }
    a { text-decoration:none; }
    a.xref { border-bottom:0 !important; }
    .qfoot a { color:inherit; }
    /* resmi metin + kolay kisim birlikte */
    section[data-ver="o"] .ez, section[data-ver="e"] .og { display:block !important; }
    .vlabel { display:flex; align-items:center; gap:.5rem; font-size:8.5pt; font-weight:800;
      letter-spacing:.11em; text-transform:uppercase; margin:1rem 0 .55rem; break-after:avoid; }
    .vlabel::after { content:""; flex:1; height:1px; }
    .vlabel.og-l { color:#60607a; margin-top:.1rem; }
    .vlabel.og-l::after { background:#e6e5f0; }
    .vlabel.ez-l { color:#047857; }
    .vlabel.ez-l::before { content:"\u270E"; font-size:11pt; letter-spacing:0; }
    .vlabel.ez-l::after { background:#a7e3c9; }
    .ez { border-left:2px solid #a7e3c9; padding-left:.85rem; }
    /* icindekiler */
    .tocpage { break-after:page; padding-top:.4rem; }
    .toch { font-size:1.5rem; margin:0 0 1.1rem; letter-spacing:-.02em; }
    .tocg { break-inside:avoid; margin-bottom:.85rem; }
    .tocc { font-weight:800; font-size:1rem; margin:.5rem 0 .3rem; display:flex; gap:.5rem; align-items:baseline; }
    .tocc b { font-family:var(--mono); color:#4f46e5; min-width:1.4em; }
    .tocs { font-size:9.5pt; color:#3b3b55; display:flex; gap:.5rem; padding:.07rem 0 .07rem 1.9rem; }
    .tocs.sub { padding-left:3.1rem; color:#60607a; font-size:9pt; }
    .tocs i { font-family:var(--mono); font-style:normal; color:#60607a; min-width:2.6em; }
    /* kapak */
    header.hero { min-height:296.5mm; display:flex; align-items:center; margin:-2mm -3mm 0; }
    /* cevap anahtari */
    .keypage table.keyt { width:100%; border-collapse:collapse; font-size:9.5pt; }
    .keypage table.keyt td { border-bottom:1px solid #e6e5f0; padding:.22rem .4rem; }
    .keypage td.kno { font-family:var(--mono); color:#3730a3; width:4.2em; font-weight:700; }
    .keypage td.kref { font-family:var(--mono); color:#60607a; }
    .keypage td.kav { font-weight:800; color:#059669; text-align:right; width:5em; }
    .keypage .body { break-inside:auto; }
  `});
  await p.emulateMedia({ media: 'print', colorScheme: 'light' });
  await p.waitForTimeout(400);

  await p.pdf({
    path: 'syllabus.pdf',
    format: 'A4', printBackground: true, preferCSSPageSize: true, outline: true, tagged: true,
    displayHeaderFooter: false, margin: { top:'0.1mm', right:'0.1mm', bottom:'0.1mm', left:'0.1mm' },
  });
  console.log('bolum:', info.secs, '| soru:', info.qn, '| cevap:', info.key.length, '| hata:', errs.length);
  await b.close();
})();
