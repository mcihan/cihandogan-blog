const { chromium } = require('playwright');
const path = require('path');
// kullanim:  node make_pdf_konu.js karar        (konular/<ad>.html -> <Ad>.pdf)
const NAME = process.argv[2] || 'karar';
const SRC  = 'file://' + path.resolve(__dirname, '../../static/deniz/konular/' + NAME + '.html');
// Galaxy Tab A: 1200x2000 => 3:5.  Sayfa: 150mm x 250mm
const W = '150mm', H = '250mm';

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 600, height: 1000 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto(SRC, { waitUntil: 'load' });
  await p.waitForTimeout(400);

  await p.evaluate(() => {
    document.getElementById('pw-hide')?.remove();
    document.getElementById('pw-gate')?.remove();
    document.querySelector('nav.sticky')?.remove();   // yapisik menu baskida ise yaramaz
    document.querySelector('nav.dz-bc')?.remove();

    // Soru bolumleri: sorunun hemen altina cozum alani + bir tam bos sayfa koy,
    // cozum ondan sonra gelsin
    let n = 0;
    document.querySelectorAll('main section').forEach(sec => {
      const h2 = sec.querySelector('.shead h2');
      if (!h2 || !/^\s*Soru\s+\d/.test(h2.textContent)) return;
      const q = sec.querySelector(':scope > .card.q');
      if (!q) return;
      n++;
      const t = h2.textContent.trim().split('\u2014')[0].trim();
      q.insertAdjacentHTML('afterend',
        '<div class="slvrest"></div>' +
        '<div class="slvpage"><p class="slvlbl">\u270E &nbsp;\u00c7\u00f6z\u00fcm alan\u0131 &middot; '
        + t + '</p></div>' +
        '<p class="slvafter">\u00c7\u00f6z\u00fcm</p>');
    });
    window.__nq = n;
  });
  console.log('soru bolumu:', await p.evaluate(() => window.__nq));

  await p.addStyleTag({ content: `
    @page { size: ${W} ${H}; margin: 0.1mm; }
    html { scroll-behavior:auto; font-size:16px; }
    body { background:#fff !important; }
    .in, main { max-width:none !important; }
    main { padding: 3mm 3.5mm 6mm !important; }
    header.hero { padding: 7mm 3.5mm 6mm !important; break-after:page; min-height:238mm;
      display:flex; flex-direction:column; justify-content:center; }
    .hero h1 { font-size:2rem !important; }
    .jump { grid-template-columns:repeat(2,minmax(0,1fr)) !important; }

    /* baskida yatay kaydirma yok -> her sey sigmali */
    .scroll { overflow:visible !important; margin:.55rem 0 !important; }
    .scroll table.dt { min-width:0 !important; }
    table.dt { font-size:.72rem; table-layout:auto; }
    table.dt th, table.dt td { padding:.26rem .34rem; }
    table.dt th { font-size:.66rem; }
    pre { white-space:pre-wrap; overflow-wrap:anywhere; font-size:.74rem; padding:.55rem .65rem; }
    .shint { display:none !important; }

    section { margin-bottom:1.6rem; break-before:auto; }
    .shead { break-after:avoid; }
    .card, ol.steps li, .fbox, .opts li { break-inside:avoid; }
    .card { padding:.8rem .9rem; margin-bottom:.7rem; }
    ol.steps li { padding:.5rem .6rem; }
    .next { display:none }

    /* --- cozum alani: sorudan sonra bos sayfa(lar) --- */
    .slvrest { break-after:page; }
    .slvpage { break-after:page; height:235mm; }
    .slvlbl { margin:0; font-size:.72rem; font-weight:800; letter-spacing:.1em;
      text-transform:uppercase; color:#b9b7c9; }
    .slvafter { margin:0 0 .7rem; font-size:.72rem; font-weight:800; letter-spacing:.11em;
      text-transform:uppercase; color:var(--c); }
    section:has(.slvpage) > .card.q { break-after:avoid; }
    a { text-decoration:none; color:inherit }
  `});
  await p.emulateMedia({ media: 'print', colorScheme: 'light' });
  await p.waitForTimeout(300);

  // tasan ogeler var mi? (baski genisligi ~ 150mm = 567px)
  const over = await p.evaluate(() => {
    const lim = document.querySelector('main').getBoundingClientRect().width + 2;
    const out = [];
    document.querySelectorAll('main *').forEach(e => {
      const w = e.getBoundingClientRect().width;
      if (w > lim) out.push(e.tagName + '.' + (e.className||'').toString().slice(0,26) + ' w=' + Math.round(w));
    });
    return { lim: Math.round(lim), over: out.slice(0, 12), n: out.length };
  });
  console.log('tasma:', JSON.stringify(over));

  await p.pdf({ path: NAME + '.pdf', width: W, height: H,
                printBackground: true, preferCSSPageSize: true, outline: true,
                margin: { top:'0.1mm', right:'0.1mm', bottom:'0.1mm', left:'0.1mm' } });
  console.log('hata:', errs.length);
  await b.close();
})();
