# -*- coding: utf-8 -*-
TCSS = """
:root{
  --bg:#f7f7fb; --surface:#fff; --surface2:#fbfbfe; --ink:#1b1b2b; --muted:#60607a; --line:#e6e5f0;
  --shadow:0 1px 2px rgba(28,28,60,.05), 0 10px 30px -16px rgba(28,28,60,.2);
  --c:#4f46e5; --cd:#3730a3; --cs:#eef2ff; --cl:#c7d2fe;
  --good:#059669; --good-s:#e7f6ef; --good-l:#a7e3c9;
  --bad:#dc2626; --bad-s:#fdecec; --bad-l:#f6bcbc;
  --am:#d97706; --am-d:#92400e; --am-s:#fffbeb; --am-l:#fcd98a;
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",sans-serif;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root{
  --bg:#101019; --surface:#1a1a28; --surface2:#15151f; --ink:#ececf4; --muted:#9d9db8; --line:#2b2b3f;
  --shadow:0 1px 2px rgba(0,0,0,.5), 0 10px 30px -16px rgba(0,0,0,.7);
  --c:#818cf8; --cd:#a5b4fc; --cs:#212143; --cl:#39396f;
  --good:#34d399; --good-s:#0e2b20; --good-l:#1d5e46;
  --bad:#f87171; --bad-s:#331416; --bad-l:#6b2529;
  --am:#fbbf24; --am-d:#fcd34d; --am-s:#241c0c; --am-l:#4d3c12;
}}
*{box-sizing:border-box}
html,body{margin:0}
html{scroll-behavior:smooth;scroll-padding-top:14px}
body{font-family:var(--sans);background:var(--bg);color:var(--ink);line-height:1.62;font-size:16px}
a{color:var(--c)}
.wrap{max-width:900px;margin:0 auto;padding:0 1.1rem}

header.th{background:linear-gradient(135deg,#312e81 0%,#4338ca 48%,#0e7490 100%);color:#fff;
  padding:2.1rem 0 1.8rem}
header.th .kick{font-size:.7rem;font-weight:800;letter-spacing:.2em;text-transform:uppercase;
  color:#a5b4fc;margin:0 0 .5rem}
header.th h1{margin:0 0 .5rem;font-size:clamp(1.5rem,4.2vw,2.2rem);font-weight:900;letter-spacing:-.02em;line-height:1.12}
header.th p{margin:0;color:#dbe3ff;font-size:.95rem;max-width:62ch}
header.th .stats{display:flex;flex-wrap:wrap;gap:.45rem;margin-top:1rem}
header.th .stats b{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.22);
  border-radius:99px;padding:.22rem .8rem;font-size:.78rem;font-weight:700}

/* ---- kartlar (hub) ---- */
.cards{display:grid;gap:.9rem;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));margin:1.6rem 0 2.4rem}
a.card{display:block;text-decoration:none;color:inherit;background:var(--surface);border:1px solid var(--line);
  border-radius:17px;padding:1.15rem 1.25rem;box-shadow:var(--shadow);transition:transform .14s,border-color .14s}
a.card:hover{transform:translateY(-2px);border-color:var(--cl)}
a.card .n{width:42px;height:42px;border-radius:13px;background:var(--c);color:#fff;display:flex;
  align-items:center;justify-content:center;font-weight:900;font-size:1.2rem;margin-bottom:.7rem}
a.card h2{margin:0 0 .35rem;font-size:1.08rem;letter-spacing:-.01em;line-height:1.25}
a.card p{margin:0;color:var(--muted);font-size:.86rem}
a.card .meta{margin-top:.75rem;display:flex;flex-wrap:wrap;gap:.35rem}
a.card .meta span{font-family:var(--mono);font-size:.7rem;font-weight:700;color:var(--cd);
  background:var(--cs);border-radius:99px;padding:.1rem .55rem}

/* ---- ust kontrol cubugu ---- */
nav.bar{position:sticky;top:0;z-index:30;background:color-mix(in srgb,var(--bg) 93%,transparent);
  backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
nav.bar .in{max-width:900px;margin:0 auto;padding:.5rem 1.1rem;display:flex;gap:.5rem;align-items:center;flex-wrap:wrap}
.sets{display:flex;gap:.25rem;overflow-x:auto;scrollbar-width:none;flex:1;min-width:0}
.sets::-webkit-scrollbar{display:none}
.sets button{border:1px solid var(--line);background:var(--surface);color:var(--muted);border-radius:9px;
  font-family:var(--mono);font-size:.76rem;font-weight:700;padding:.2rem .6rem;cursor:pointer;white-space:nowrap}
.sets button:hover{color:var(--ink)}
.sets button.on{background:var(--c);border-color:var(--c);color:#fff}
.sets button.done{border-color:var(--good-l);color:var(--good)}
.sets button.on.done{background:var(--good);border-color:var(--good);color:#fff}
.score{font-family:var(--mono);font-size:.76rem;font-weight:800;color:var(--muted);white-space:nowrap}
.score b{color:var(--good)}
.score i{font-style:normal;color:var(--bad)}

.sw{display:inline-flex;border:1px solid var(--line);border-radius:8px;overflow:hidden;flex:none;background:var(--bg)}
.sw button{border:0;background:transparent;color:var(--muted);font-family:var(--sans);font-size:.74rem;
  font-weight:700;padding:.22rem .6rem;cursor:pointer;white-space:nowrap}
.sw button+button{border-left:1px solid var(--line)}
.sw button:hover{color:var(--ink)}
.sw button.on{background:var(--c);color:#fff}
.chk{display:inline-flex;align-items:center;gap:.4rem;font-size:.78rem;font-weight:700;color:var(--muted);
  cursor:pointer;user-select:none;white-space:nowrap}
.chk input{accent-color:var(--c);width:15px;height:15px}

/* ---- soru ---- */
.qset{display:none}
.qset.on{display:block}
.sethead{margin:1.4rem 0 .9rem;display:flex;align-items:baseline;gap:.6rem;flex-wrap:wrap}
.sethead h2{margin:0;font-size:1.15rem;letter-spacing:-.01em}
.sethead span{font-size:.82rem;color:var(--muted)}

article.q{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:1.05rem 1.2rem;
  margin-bottom:.95rem;box-shadow:var(--shadow)}
article.q.ok{border-color:var(--good-l)}
article.q.no{border-color:var(--bad-l)}
.qhead{display:flex;align-items:center;gap:.45rem;flex-wrap:wrap;margin-bottom:.6rem}
.qhead .num{width:26px;height:26px;border-radius:8px;background:var(--cs);color:var(--cd);flex:none;
  display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:.78rem;font-weight:800}
.qhead .ref{font-family:var(--mono);font-size:.7rem;font-weight:700;color:var(--muted)}
.qhead .lo{font-family:var(--mono);font-size:.68rem;font-weight:700;color:var(--cd);background:var(--cs);
  border-radius:99px;padding:.08rem .5rem}
.qhead .mk{font-size:.68rem;font-weight:800;color:var(--am-d);background:var(--am-s);
  border:1px solid var(--am-l);border-radius:99px;padding:.04rem .5rem}
.qhead .sw{margin-left:auto}
.qtext{font-size:.96rem;margin:0 0 .7rem}
.qtext p{margin:.5rem 0}
.qtext p:first-child{margin-top:0}
.qtext .pre{font-family:var(--mono);font-size:.84rem;white-space:pre-wrap;background:var(--surface2);
  border:1px solid var(--line);border-radius:10px;padding:.6rem .75rem;margin:.55rem 0;overflow-x:auto}

ul.opts{list-style:none;margin:0;padding:0;display:grid;gap:.35rem}
ul.opts label{display:grid;grid-template-columns:auto auto minmax(0,1fr);gap:.55rem;align-items:start;
  padding:.5rem .7rem;border:1px solid var(--line);border-radius:11px;cursor:pointer;background:var(--surface2);
  font-size:.92rem;transition:border-color .12s,background .12s}
ul.opts label:hover{border-color:var(--cl)}
ul.opts input{margin:.28rem 0 0;accent-color:var(--c);flex:none}
ul.opts .k{font-family:var(--mono);font-weight:800;color:var(--cd);font-size:.85rem;line-height:1.7}
ul.opts li.sel label{border-color:var(--c);background:var(--cs)}
.q.rev ul.opts label{cursor:default}
.q.rev li.right label{border-color:var(--good);background:var(--good-s)}
.q.rev li.wrong label{border-color:var(--bad);background:var(--bad-s)}
.q.rev li.right .k{color:var(--good)}
.q.rev li.wrong .k{color:var(--bad)}

.qact{margin-top:.7rem;display:flex;gap:.5rem;flex-wrap:wrap;align-items:center}
button.show{border:1px solid var(--cl);background:var(--cs);color:var(--cd);border-radius:9px;
  font-size:.78rem;font-weight:800;padding:.3rem .8rem;cursor:pointer;font-family:var(--sans)}
button.show:hover{background:var(--cl)}
.q.rev button.show{display:none}

.ansbox{display:none;margin-top:.8rem;border-top:1px dashed var(--line);padding-top:.8rem}
.q.rev .ansbox{display:block}
a.tlink{display:inline-flex;align-items:center;gap:.4rem;text-decoration:none;font-size:.82rem;font-weight:800;
  color:var(--cd);background:var(--cs);border:1px solid var(--cl);border-radius:10px;padding:.3rem .7rem;
  margin-bottom:.6rem}
a.tlink:hover{background:var(--cl)}
a.tlink::after{content:"\\2197";font-weight:900}
.verdict{margin:0 0 .45rem;font-size:.9rem;font-weight:800}
.verdict.ok{color:var(--good)}
.verdict.no{color:var(--bad)}
.verdict.nt{color:var(--muted)}
.why{font-size:.9rem;color:var(--ink);margin:.35rem 0}
.why p{margin:.4rem 0}
details.deep{margin-top:.6rem;border:1px solid var(--line);border-radius:11px;background:var(--surface2);overflow:hidden}
details.deep > summary{cursor:pointer;list-style:none;padding:.45rem .8rem;font-size:.8rem;font-weight:800;
  color:var(--muted);display:flex;align-items:center;gap:.45rem}
details.deep > summary::-webkit-details-marker{display:none}
details.deep > summary::before{content:"\\25b8";transition:transform .15s}
details.deep[open] > summary::before{transform:rotate(90deg)}
details.deep[open] > summary{color:var(--ink);border-bottom:1px solid var(--line)}
.deepbody{padding:.65rem .85rem;font-size:.88rem}
.deepbody p{margin:.45rem 0}
.deepbody p:first-child{margin-top:0}
a.simlink{display:inline-block;margin-top:.6rem;font-size:.78rem;font-weight:700}

.setfoot{display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;margin:1.1rem 0 2.6rem}
.setfoot button{border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:10px;
  font-size:.82rem;font-weight:800;padding:.42rem .95rem;cursor:pointer;font-family:var(--sans)}
.setfoot button.pri{background:var(--c);border-color:var(--c);color:#fff}
.setfoot button:hover{border-color:var(--cl)}
.setfoot .res{font-size:.85rem;font-weight:800;margin-left:auto}
.setfoot .res.ok{color:var(--good)}
.setfoot .res.no{color:var(--bad)}

footer.tf{border-top:1px solid var(--line);margin-top:1rem;padding:1.2rem 0 2rem;color:var(--muted);font-size:.8rem}

body[data-lang="tr"] .s-en,body[data-lang="en"] .s-tr{display:none}
article.q[data-lang="tr"] .x-en,article.q[data-lang="en"] .x-tr{display:none}

@media (max-width:620px){
  article.q{padding:.9rem 1rem;border-radius:13px}
  ul.opts label{font-size:.88rem;padding:.45rem .6rem}
  .qhead .sw{margin-left:0}
}
"""
