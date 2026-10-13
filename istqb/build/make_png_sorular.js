const { chromium } = require('playwright');
const path = require('path');
const NAME = process.argv[2] || 'durum';
const SRC = 'file://' + path.resolve(process.env.KONUDIR, NAME + '.html');

(async () => {
  const b = await chromium.launch({ args: ['--force-device-scale-factor=2'] });
  const p = await b.newPage({ viewport: { width: 980, height: 1200 }, deviceScaleFactor: 2 });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto(SRC, { waitUntil: 'load' });
  await p.waitForTimeout(500);

  const list = await p.evaluate(() => {
    document.getElementById('pw-hide')?.remove();
    document.getElementById('pw-gate')?.remove();
    document.querySelector('nav.sticky')?.remove();
    document.querySelector('nav.dz-bc')?.remove();
    document.querySelector('header.hero')?.remove();
    const out = [];
    document.querySelectorAll('main section').forEach(sec => {
      const h2 = sec.querySelector('.shead h2');
      if (!h2 || !/^\s*Soru\s+(\d+)/.test(h2.textContent)) { sec.remove(); return; }
      const n = h2.textContent.match(/^\s*Soru\s+(\d+)/)[1];
      const lo = sec.querySelector('.shead .lo')?.textContent.trim() || '';
      const ref = (lo.match(/sınav\s*([A-H]).*?Soru\s*(\d+)/i) || []).slice(1).join('');
      // sadece baslik + soru kalsin
      const keep = new Set([sec.querySelector(':scope > .shead'),
                            sec.querySelector(':scope > .card.q')]);
      [...sec.children].forEach(el => { if (!keep.has(el)) el.remove(); });
      sec.style.margin = '0';
      out.push({ id: sec.id, n, ref });
    });
    document.querySelector('main').style.padding = '18px 20px';
    return out;
  });

  for (const q of list) {
    const f = `${NAME}-soru-${String(q.n).padStart(2,'0')}${q.ref ? '-' + q.ref : ''}.png`;
    await p.locator('#' + q.id).screenshot({ path: f });
    console.log('  ' + f);
  }
  console.log('toplam:', list.length, '| hata:', errs.length);
  await b.close();
})();
