const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1100, height: 1400 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + require('path').resolve(__dirname, 'syllabus.html') + '', { waitUntil: 'load' });
  await p.waitForTimeout(600);

  const info = await p.evaluate(() => {
    const body = document.body;
    body.dataset.lang = 'tr';
    document.querySelectorAll('section[data-no]').forEach(s => { s.dataset.lang='tr'; s.dataset.ver='e'; });

    // ekrana ozgu parcalar
    ['aside', 'nav.top', '.nores', '.vtools', '.qref .lang', '#glob', '#gver', '.srch', '.menubtn']
      .forEach(sel => document.querySelectorAll(sel).forEach(e => e.remove()));
    // yalnizca kolay anlatim kalsin; resmi metin tamamen cikar
    document.querySelectorAll('.og').forEach(e => e.remove());
    document.querySelectorAll('.s-en, .x-en, .l-en').forEach(e => e.remove());  // yalnizca turkce

    // akordiyonlari ac
    document.querySelectorAll('details.qa').forEach(d => d.open = true);

    // teknik terimler: hepsi bir arada, en basta; bolum ici kopyalari gitsin
    const terms = new Map();
    document.querySelectorAll('details.gl .glwrap .g').forEach(g => {
      const tr = g.querySelector('b')?.textContent.trim();
      const en = g.querySelector('i')?.textContent.trim();
      if (tr && !terms.has(tr)) terms.set(tr, en);
    });
    document.querySelectorAll('details.gl').forEach(d => d.remove());

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
    return { key, secs, qn, chaps, terms: [...terms.entries()] };
  });

  // ---- icindekiler ----
  const toc = `
  <div class="tocpage">
    <h2 class="toch">İçindekiler</h2>
    ${info.chaps.map(c => `
      <div class="tocg"><div class="tocc"><b>${c.no}</b>${c.title}</div>
        ${c.secs.map(s2 => `<div class="tocs${s2.sub ? ' sub' : ''}"><i>${s2.no}</i>${s2.t}</div>`).join('')}
      </div>`).join('')}
    <div class="tocg"><div class="tocc"><b>§</b>Teknik Terimler (Türkçe → İngilizce)</div></div>
    <div class="tocg"><div class="tocc"><b>✓</b>Cevap Anahtarı</div></div>
  </div>`;
  await p.evaluate(h => { document.querySelector('main').insertAdjacentHTML('afterbegin', h); }, toc);

  // ---- teknik terimler sozlugu (tek yerde) ----
  const coll = new Intl.Collator('tr');
  const terms = info.terms.slice().sort((a, b) => coll.compare(a[0], b[0]));
  const glHtml = `
  <div class="glpage">
    <h2 class="toch">Teknik Terimler · Türkçe &rarr; İngilizce</h2>
    <p class="glnote">Ders programının tamamında ve sınav sorularında geçen ${terms.length} terim,
      alfabetik sırayla. Türkçe karşılık kafanı karıştırırsa terimin İngilizce aslını buradan kontrol et.</p>
    <div class="glall">${terms.map(([tr, en]) =>
      `<div class="g"><b>${tr}</b><i>${en}</i></div>`).join('')}</div>
  </div>`;
  await p.evaluate(h => {
    document.querySelector('.tocpage').insertAdjacentHTML('afterend', h);
  }, glHtml);

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
    /* --- A4 baski: yalnizca kolay anlatim --- */
    @page { size: A4; margin: 10mm 9mm; }
    html { scroll-behavior:auto; font-size:17px; }
    body { background:#fff !important; font-size:15px; orphans:3; widows:3; }
    .shell { display:block !important; max-width:none !important; padding:0 !important; }
    main { min-width:0; }

    /* sayfayi doldur: yalnizca konu baslari yeni sayfada baslasin */
    .chap { break-before:page; }
    .chap:first-of-type { break-before:auto; }
    section.sec, section.sub, .body, details.qa, .ez, .ez-tw, table.ez-t,
    .qitem, .qopts, ol.prin { break-inside:auto; }
    .sh, .chead, details.qa > summary, .ez .ez-h { break-after:avoid; }
    .qitem .qref { break-after:avoid; }
    .ez .ez-q, .ez .ez-pre, .ez .ez-tw, .lobox, .kws, .glall .g,
    .qopts li, .ez .ez-ul li, .ez .ez-ol li { break-inside:avoid; }
    tr, .ez .ez-h { break-inside:avoid; }

    /* dikey ritmi sikistir */
    .chap { margin-bottom:0 }
    .chead { margin-bottom:.5rem }
    section.sec { margin-bottom:.9rem }
    section.sub { margin-bottom:.8rem }
    .sh { margin-bottom:.35rem }
    .body { box-shadow:none !important; padding:.55rem .7rem; border-radius:9px; margin:0 }
    .lobox { padding:.55rem .75rem; margin-bottom:.6rem }
    .kws { margin:.35rem 0 .6rem }
    .ez { border-left:0; padding-left:0; font-size:.95rem }
    .ez .ez-h { margin:.75rem 0 .3rem }
    .ez p { margin:.35rem 0 }
    .ez .ez-ul, .ez .ez-ol { margin:.3rem 0 }
    .ez .ez-ul li, .ez .ez-ol li { margin:.14rem 0 }
    .ez .ez-hr { margin:.6rem 0 }
    .ez .ez-q { margin:.45rem 0; padding:.4rem .7rem }
    .ez .ez-pre { margin:.45rem 0; padding:.5rem .7rem }
    .ez .ez-tw { margin:.45rem 0 }
    .ez table.ez-t th, .ez table.ez-t td { padding:.26rem .5rem }
    details.qa { margin-top:.6rem }
    .qwrap { padding:.15rem .5rem .5rem; gap:.45rem }
    .qitem { padding:.4rem .55rem }
    .qopts { gap:.15rem }

    a { text-decoration:none; }
    a.xref { border-bottom:0 !important; }
    .qfoot a { color:inherit; }

    /* kapak */
    header.hero { break-after:page; padding:2rem 1.4rem !important;
      min-height:275mm; display:flex; align-items:center; }
    header.hero .hin { max-width:none; }

    /* icindekiler */
    .tocpage { break-after:page; }
    .toch { font-size:1.45rem; margin:0 0 .9rem; letter-spacing:-.02em; }
    .tocg { break-inside:avoid; margin-bottom:.6rem; }
    .tocc { font-weight:800; font-size:.98rem; margin:.4rem 0 .22rem; display:flex; gap:.5rem; align-items:baseline; }
    .tocc b { font-family:var(--mono); color:#4f46e5; min-width:1.4em; }
    .tocs { font-size:9pt; color:#3b3b55; display:flex; gap:.5rem; padding:.04rem 0 .04rem 1.9rem; }
    .tocs.sub { padding-left:3.1rem; color:#60607a; font-size:8.6pt; }
    .tocs i { font-family:var(--mono); font-style:normal; color:#60607a; min-width:2.6em; }

    /* toplu teknik terimler */
    .glpage { break-before:page; break-after:page; }
    .glnote { font-size:9pt; color:#60607a; margin:0 0 .8rem; max-width:62ch; }
    .glall { column-count:3; column-gap:1rem; }
    .glall .g { padding:.2rem 0; border-bottom:1px dotted #e6e5f0; -webkit-column-break-inside:avoid; }
    .glall .g b { display:block; font-size:9pt; font-weight:700; color:#1b1b2b; }
    .glall .g i { display:block; font-style:normal; font-size:8.6pt; font-family:var(--mono); color:#92400e; }

    /* cevap anahtari */
    .keypage { break-before:page }
    .keypage .body { columns:2; column-gap:1.2rem }
    .keypage table.keyt { width:100%; border-collapse:collapse; font-size:9pt; }
    .keypage table.keyt td { border-bottom:1px solid #e6e5f0; padding:.18rem .35rem; }
    .keypage td.kno { font-family:var(--mono); color:#3730a3; width:4.2em; font-weight:700; }
    .keypage td.kref { font-family:var(--mono); color:#60607a; }
    .keypage td.kav { font-weight:800; color:#059669; text-align:right; width:4em; }
  `});
  await p.emulateMedia({ media: 'print', colorScheme: 'light' });
  await p.waitForTimeout(400);

  await p.pdf({
    path: 'syllabus-kolay-a4.pdf',
    format: 'A4', printBackground: true, preferCSSPageSize: true,
    outline: true, tagged: true,
    displayHeaderFooter: false,
    margin: { top:'10mm', right:'9mm', bottom:'10mm', left:'9mm' },
  });
  console.log('bolum:', info.secs, '| soru:', info.qn, '| cevap:', info.key.length, '| hata:', errs.length);
  await b.close();
})();
