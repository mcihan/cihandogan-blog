function esc(s){
  return String(s).replace(/[&<>"]/g, c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
}

/* Boru (|) ile yazılmış blokları gerçek HTML tablosuna çevirir. */
function looksLikeHeader(cells){
  if(cells[0] === "") return true;
  const rest = cells.slice(1);
  if(!rest.length) return false;
  return rest.every(c => c.length <= 24 && !/[:=]/.test(c));
}
function tableHtml(rows){
  const grid = rows.map(r => r.split("|").map(c => c.trim()));
  const width = Math.max(...grid.map(r => r.length));
  grid.forEach(r => { while(r.length < width) r.push(""); });
  const head = grid.length >= 3 && looksLikeHeader(grid[0]);
  let html = '<div class="tblwrap"><table class="qtbl">';
  if(head){
    html += "<thead><tr>" + grid[0].map(c => `<th>${esc(c)}</th>`).join("") + "</tr></thead>";
  }
  html += "<tbody>";
  for(const r of grid.slice(head ? 1 : 0)){
    html += "<tr>" + r.map(c => `<td>${esc(c)}</td>`).join("") + "</tr>";
  }
  return html + "</tbody></table></div>";
}
function fmtQ(text){
  const lines = String(text).split("\n");
  let out = "", buf = [], tbl = [];
  const flushTxt = () => { if(buf.length){ out += `<span class="ptxt">${esc(buf.join("\n"))}</span>`; buf = []; } };
  const flushTbl = () => {
    if(tbl.length >= 2){ flushTxt(); out += tableHtml(tbl); }
    else if(tbl.length === 1){ buf.push(tbl[0]); }
    tbl = [];
  };
  for(const ln of lines){
    if(ln.includes("|")){ tbl.push(ln); }
    else { flushTbl(); buf.push(ln); }
  }
  flushTbl(); flushTxt();
  return out;
}

