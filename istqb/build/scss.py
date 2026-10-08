# -*- coding: utf-8 -*-
CSS = """
:root{
  --bg:#f7f7fb; --surface:#fff; --surface2:#fbfbfe; --ink:#1b1b2b; --muted:#60607a; --line:#e6e5f0;
  --shadow:0 1px 2px rgba(28,28,60,.05), 0 10px 30px -16px rgba(28,28,60,.2);
  --c:#4f46e5; --cd:#3730a3; --cs:#eef2ff; --cl:#c7d2fe;
  --good:#059669; --good-s:#e7f6ef; --bad:#dc2626; --bad-s:#fdecec;
  --warn:#b45309; --warn-s:#fdf3e3;
  --am:#d97706; --am-d:#92400e; --am-s:#fffbeb; --am-l:#fcd98a; --am-b:#fef3c7;
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",sans-serif;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  --sbw:290px; --navh:52px;
}
@media (prefers-color-scheme:dark){:root{
  --bg:#101019; --surface:#1a1a28; --surface2:#15151f; --ink:#ececf4; --muted:#9d9db8; --line:#2b2b3f;
  --shadow:0 1px 2px rgba(0,0,0,.5), 0 10px 30px -16px rgba(0,0,0,.7);
  --c:#818cf8; --cd:#a5b4fc; --cs:#212143; --cl:#39396f;
  --good:#34d399; --good-s:#0e2b20; --bad:#f87171; --bad-s:#331416;
  --warn:#fbbf24; --warn-s:#2e2210;
  --am:#fbbf24; --am-d:#fcd34d; --am-s:#241c0c; --am-l:#4d3c12; --am-b:#2f2510;
}}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:calc(var(--navh) + 14px)}
html,body{margin:0}
body{font-family:var(--sans);background:var(--bg);color:var(--ink);line-height:1.65;font-size:16px}
a{color:var(--c)}

/* ---- hero ---- */
header.hero{background:linear-gradient(135deg,#312e81 0%,#4338ca 44%,#0e7490 100%);padding:2.8rem 1.3rem 2.3rem;color:#fff}
.hin{max-width:1320px;margin:0 auto}
.kick{font-size:.72rem;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:#a5b4fc;margin:0 0 .6rem}
.hero h1{font-size:clamp(1.8rem,4.6vw,2.7rem);line-height:1.08;margin:0 0 .6rem;font-weight:900;letter-spacing:-.02em}
.hero p{color:#dbe3ff;max-width:70ch;margin:0 0 1.4rem;font-size:1.02rem}
.stats{display:flex;flex-wrap:wrap;gap:.5rem}
.stats b{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.22);border-radius:99px;
  padding:.26rem .85rem;font-size:.8rem;font-weight:700}
.hnote{color:#b9c4f5;font-size:.82rem;margin:.9rem 0 0;max-width:72ch}

/* ---- nav ---- */
nav.top{position:sticky;top:0;z-index:40;overflow:visible;background:color-mix(in srgb,var(--bg) 92%,transparent);
  backdrop-filter:blur(12px);border-bottom:1px solid var(--line);height:var(--navh)}
nav.top .nin{max-width:1320px;margin:0 auto;display:flex;gap:.5rem;align-items:center;padding:.5rem 1.1rem;height:100%}
.menubtn{display:none;flex:none;border:1px solid var(--line);background:var(--surface);color:var(--ink);
  border-radius:9px;padding:.35rem .6rem;font-size:.85rem;font-weight:700;cursor:pointer;font-family:inherit}
.chips{display:flex;gap:.3rem;overflow-x:auto;scrollbar-width:none;flex:1;min-width:0}
.chips::-webkit-scrollbar{display:none}
.chips a{white-space:nowrap;text-decoration:none;font-size:.82rem;font-weight:700;color:var(--muted);
  border-radius:8px;padding:.3rem .6rem}
.chips a:hover{color:var(--ink);background:color-mix(in srgb,var(--ink) 7%,transparent)}
.srch{flex:none;position:relative}
.srch input{width:210px;max-width:40vw;border:1px solid var(--line);background:var(--surface);color:var(--ink);
  border-radius:9px;padding:.34rem .7rem;font-size:.85rem;font-family:inherit;outline:none}
.srch input:focus{border-color:var(--c);box-shadow:0 0 0 3px color-mix(in srgb,var(--c) 22%,transparent)}

/* ---- layout ---- */
.shell{max-width:1320px;margin:0 auto;display:grid;grid-template-columns:var(--sbw) minmax(0,1fr);
  gap:2rem;padding:1.6rem 1.1rem 4rem;align-items:start}
aside{position:sticky;top:calc(var(--navh) + 12px);max-height:calc(100vh - var(--navh) - 28px);
  overflow-y:auto;border:1px solid var(--line);border-radius:16px;background:var(--surface);
  padding:.9rem .75rem;box-shadow:var(--shadow);scrollbar-width:thin}
aside .grp{margin-bottom:.5rem}
aside .grp > a{display:flex;gap:.5rem;align-items:center;text-decoration:none;color:var(--ink);
  font-weight:800;font-size:.86rem;padding:.4rem .5rem;border-radius:9px}
aside .grp > a:hover{background:var(--cs)}
aside .grp > a i{flex:none;width:22px;height:22px;border-radius:7px;background:var(--c);color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:900;font-style:normal}
aside ul{list-style:none;margin:.15rem 0 .4rem;padding:0 0 0 .5rem;border-left:1px solid var(--line);margin-left:.95rem}
aside li{margin:0}
aside li a{display:block;text-decoration:none;color:var(--muted);font-size:.805rem;padding:.2rem .5rem;
  border-radius:7px;line-height:1.4}
aside li a:hover{color:var(--ink);background:color-mix(in srgb,var(--ink) 6%,transparent)}
aside li a.sub{padding-left:1.1rem;font-size:.78rem}
aside li a.on{color:var(--cd);background:var(--cs);font-weight:700}

main{min-width:0}

/* ---- chapter ---- */
.chap{margin-bottom:3.2rem}
.chead{display:flex;gap:1rem;align-items:flex-start;margin-bottom:1rem;padding-bottom:1rem;border-bottom:2px solid var(--line)}
.chead .n{width:54px;height:54px;flex:none;border-radius:16px;background:linear-gradient(135deg,var(--c),var(--cd));
  color:#fff;display:flex;align-items:center;justify-content:center;font-size:1.5rem;font-weight:900}
.chead h2{margin:0 0 .25rem;font-size:1.6rem;letter-spacing:-.02em;line-height:1.15}
.chead .meta{font-size:.78rem;color:var(--muted);font-family:var(--mono)}
.chead .meta abbr{text-decoration:underline dotted;text-underline-offset:3px;cursor:help}
.kws{display:flex;flex-wrap:wrap;gap:.3rem;margin:.6rem 0 1rem}
.kws span{font-size:.73rem;background:var(--cs);color:var(--cd);border-radius:99px;padding:.14rem .6rem;font-weight:600}
.lobox{background:var(--surface);border:1px solid var(--line);border-radius:15px;padding:.9rem 1.05rem;
  box-shadow:var(--shadow);margin-bottom:1.6rem}
.lobox h3{margin:0 0 .55rem;font-size:.73rem;font-weight:800;letter-spacing:.11em;text-transform:uppercase;color:var(--c)}
.lobox ol{list-style:none;margin:0;padding:0;display:grid;gap:.3rem}
.lobox li{display:grid;grid-template-columns:auto auto minmax(0,1fr);gap:.5rem;align-items:baseline;font-size:.86rem}
.lobox a.loid{font-family:var(--mono);font-size:.74rem;font-weight:700;color:var(--cd);text-decoration:none;
  background:var(--cs);border-radius:6px;padding:.08rem .36rem;white-space:nowrap}
.lobox a.loid:hover{background:var(--cl)}
.kb{font-size:.67rem;font-weight:900;border-radius:5px;padding:.08rem .3rem;letter-spacing:.03em}
.kb.K1{background:var(--good-s);color:var(--good)} .kb.K2{background:var(--cs);color:var(--cd)}
.kb.K3{background:var(--warn-s);color:var(--warn)}

/* ---- section ---- */
section.sec{margin-bottom:1.9rem}
section.sub{margin-left:0;margin-bottom:1.6rem}
.sh{display:flex;gap:.6rem;align-items:baseline;flex-wrap:wrap;margin:0 0 .5rem}
.sh .num{font-family:var(--mono);font-size:.8rem;font-weight:800;color:var(--c);flex:none}
.sh h3{margin:0;font-size:1.22rem;letter-spacing:-.015em;line-height:1.25}
.sh h4{margin:0;font-size:1.04rem;letter-spacing:-.01em;line-height:1.3}
.sh .los{display:flex;gap:.25rem;flex-wrap:wrap}
.sh .pct{margin-left:auto;flex:none;font-family:var(--mono);font-size:.73rem;font-weight:800;
  color:var(--muted);background:color-mix(in srgb,var(--ink) 6%,transparent);
  border-radius:99px;padding:.1rem .5rem;cursor:help}
nav.top .bar{position:absolute;left:0;bottom:-1px;height:3px;width:0;
  background:linear-gradient(90deg,var(--c),var(--cd));transition:width .1s linear;border-radius:0 2px 2px 0}
.sh .los span{font-family:var(--mono);font-size:.68rem;font-weight:700;color:var(--cd);background:var(--cs);
  border-radius:5px;padding:.06rem .34rem}
.body{background:var(--surface);border:1px solid var(--line);border-radius:15px;padding:1rem 1.2rem;
  box-shadow:var(--shadow)}
section.sub .body{background:var(--surface2)}
.body > *:first-child{margin-top:0}
.body > *:last-child{margin-bottom:0}
.body p{margin:.7rem 0}
.body ul,.body ol{margin:.7rem 0;padding-left:1.3rem}
.body li{margin:.3rem 0}
.body ol.prin{list-style:none;counter-reset:pr;padding:0;display:grid;gap:.55rem}
.body ol.prin li{counter-increment:pr;display:grid;grid-template-columns:27px minmax(0,1fr);gap:.65rem;
  padding:.6rem .75rem;border-radius:12px;background:var(--cs);margin:0}
.body ol.prin li::before{content:counter(pr);width:24px;height:24px;border-radius:7px;background:var(--c);
  color:#fff;display:flex;align-items:center;justify-content:center;font-size:.78rem;font-weight:900}
.body code{font-family:var(--mono);font-size:.87em;background:color-mix(in srgb,var(--ink) 8%,transparent);
  padding:.08em .34em;border-radius:5px}
.body a.xref{color:var(--c);text-decoration:none;border-bottom:1px dotted var(--cl);font-weight:600}
.body a.xref:hover{border-bottom-style:solid}
.body b.term{color:var(--cd);font-weight:800}

/* ---- sorular ---- */
/* --- teknik terim sozlugu --- */
details.gl{margin-top:.8rem;border:1px solid var(--am-l);border-radius:13px;background:var(--am-s);overflow:hidden}
details.gl > summary{cursor:pointer;list-style:none;padding:.55rem .9rem;font-size:.84rem;font-weight:800;
  color:var(--am-d);background:var(--am-b);display:flex;align-items:center;gap:.5rem}
details.gl > summary::-webkit-details-marker{display:none}
details.gl > summary::before{content:"\u25b8";font-size:.9rem;transition:transform .15s}
details.gl[open] > summary::before{transform:rotate(90deg)}
details.gl[open] > summary{border-bottom:1px solid var(--am-l)}
details.gl > summary .cnt{margin-left:auto;background:var(--am);color:#fff;border-radius:99px;
  font-family:var(--mono);font-size:.7rem;font-weight:800;padding:.08rem .5rem;flex:none}
.glwrap{padding:.7rem .9rem;display:grid;gap:.1rem .9rem;
  grid-template-columns:repeat(auto-fill,minmax(186px,1fr))}
.glwrap .g{display:block;padding:.26rem 0;border-bottom:1px dotted var(--am-l);min-width:0}
.glwrap .g b{display:block;font-size:.8rem;font-weight:700;color:var(--ink);overflow-wrap:anywhere}
.glwrap .g i{display:block;font-style:normal;font-size:.76rem;font-family:var(--mono);color:var(--am-d);
  overflow-wrap:anywhere}
.glfoot{margin:0;padding:.1rem .9rem .75rem;font-size:.74rem;color:var(--am-d);opacity:.85}
details.qa{margin-top:.8rem;border:1px solid var(--cl);border-radius:13px;background:var(--cs);overflow:hidden}
details.qa > summary{cursor:pointer;list-style:none;padding:.6rem .9rem;font-size:.86rem;font-weight:800;
  color:var(--cd);display:flex;gap:.5rem;align-items:center;user-select:none}
details.qa > summary::-webkit-details-marker{display:none}
details.qa > summary::before{content:"▸";font-size:.9rem;transition:transform .15s}
details.qa[open] > summary::before{transform:rotate(90deg)}
details.qa > summary .cnt{margin-left:auto;background:var(--c);color:#fff;border-radius:99px;
  font-size:.7rem;padding:.08rem .5rem;font-weight:800}
.qwrap{padding:.2rem .7rem .8rem;display:grid;gap:.7rem}
.qitem{background:var(--surface);border:1px solid var(--line);border-radius:11px;padding:.75rem .9rem}
.qref{display:flex;gap:.4rem;align-items:center;flex-wrap:wrap;margin-bottom:.45rem}
.qref .ex{font-size:.7rem;font-weight:800;border-radius:6px;padding:.1rem .45rem;font-family:var(--mono)}
.qref .ex.resmi{background:var(--cs);color:var(--cd)}
.qref .ex.pratik{background:var(--good-s);color:var(--good)}
.qref .kk{font-size:.66rem;font-weight:800;color:var(--muted);font-family:var(--mono)}
.qref .mk{font-size:.66rem;font-weight:800;color:var(--warn);background:var(--warn-s);border-radius:5px;padding:.05rem .32rem}
.qitem p{margin:.4rem 0;font-size:.9rem}
.qitem p.qline{font-family:var(--mono);font-size:.82rem;margin:.15rem 0}
.qopts{list-style:none;margin:.55rem 0 0;padding:0;display:grid;gap:.25rem}
.qopts li{display:grid;grid-template-columns:22px minmax(0,1fr);gap:.5rem;font-size:.88rem;align-items:baseline}
.qopts li b{font-family:var(--mono);font-size:.74rem;font-weight:800;color:var(--muted);text-transform:uppercase}
details.ans{margin-top:.65rem;border-top:1px dashed var(--line);padding-top:.5rem}
details.ans > summary{cursor:pointer;list-style:none;font-size:.78rem;font-weight:700;color:var(--muted);
  display:inline-flex;gap:.35rem;align-items:center;user-select:none}
details.ans > summary::-webkit-details-marker{display:none}
details.ans > summary::before{content:"▸";font-size:.85rem;transition:transform .15s}
details.ans[open] > summary::before{transform:rotate(90deg)}
details.ans[open] > summary{color:var(--good)}
details.ans > summary:hover{color:var(--ink)}
.av{display:inline-flex;align-items:center;margin-top:.45rem;background:var(--good-s);color:var(--good);
  border:1px solid color-mix(in srgb,var(--good) 35%,transparent);border-radius:9px;
  padding:.24rem .65rem;font-size:.86rem;font-weight:800;letter-spacing:.02em}
.lang{display:inline-flex;border:1px solid var(--line);border-radius:7px;overflow:hidden;margin-left:auto;flex:none}
.lang button{border:0;background:var(--surface);color:var(--muted);font-family:var(--mono);
  font-size:.66rem;font-weight:800;padding:.1rem .4rem;cursor:pointer;line-height:1.5;letter-spacing:.03em}
.lang button+button{border-left:1px solid var(--line)}
.lang button:hover{color:var(--ink)}
.lang button.on{background:var(--c);color:#fff}
.lang.glob{margin:0;flex:none}
.lang.glob button{font-size:.72rem;padding:.2rem .5rem;background:var(--bg)}
.lang.glob button.on{background:var(--c);color:#fff}
/* --- sayfa dili (konu metni) --- */
.body > .s-tr,.body > .s-en{display:contents}
.body > .s-tr > *:first-child,.body > .s-en > *:first-child{margin-top:0}
.body > .s-tr > *:last-child,.body > .s-en > *:last-child{margin-bottom:0}
body[data-lang="en"] .s-tr,body[data-lang="tr"] .s-en{display:none}
.qitem[data-lang="tr"] .l-en,.qitem[data-lang="en"] .l-tr{display:none}
details.ans .l-en,details.ans .l-tr{display:inline}
.qitem[data-lang="tr"] details.ans .l-en,.qitem[data-lang="en"] details.ans .l-tr{display:none}
.qscroll{overflow-x:auto;margin:.5rem 0}
table.qtbl{border-collapse:collapse;font-size:.82rem;min-width:320px}
table.qtbl th,table.qtbl td{border:1px solid var(--line);padding:.3rem .55rem;text-align:left;white-space:nowrap}
table.qtbl th{background:var(--cs);color:var(--cd);font-weight:800;font-size:.76rem}
.qfoot{font-size:.78rem;color:var(--muted);padding:0 .25rem}
.qfoot a{font-weight:700}

.nores{display:none;padding:2rem;text-align:center;color:var(--muted);font-size:.95rem}
body.filtering .nores.show{display:block}
footer.ft{border-top:1px solid var(--line);margin-top:2rem;padding:1.3rem 0 0;color:var(--muted);font-size:.82rem}

@media (max-width:1000px){
  .shell{grid-template-columns:minmax(0,1fr);gap:0;padding-top:1rem}
  .menubtn{display:block}
  aside{position:fixed;inset:var(--navh) auto 0 0;width:min(84vw,320px);max-height:none;height:calc(100vh - var(--navh));
    border-radius:0;border-left:0;border-top:0;border-bottom:0;z-index:35;transform:translateX(-102%);
    transition:transform .2s ease;box-shadow:0 0 40px rgba(0,0,0,.3)}
  body.nav-open aside{transform:none}
  body.nav-open::after{content:"";position:fixed;inset:var(--navh) 0 0 0;background:rgba(0,0,0,.45);z-index:34}
  .chead .n{width:44px;height:44px;font-size:1.25rem;border-radius:13px}
  .chead h2{font-size:1.3rem}
  .body{padding:.9rem 1rem;border-radius:13px}
}
@media print{nav.top,aside,.srch,.menubtn{display:none}.shell{display:block}details.qa{break-inside:avoid}}
"""
