// Card text -> HTML. Supports **bold**, *italic*, "- " bullets, "a | b" tables, and lettered sub-parts.
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

export function inline(s) {
  return esc(s)
    .replace(/\*\*([^*]+?)\*\*/g, '<b>$1</b>')
    .replace(/(^|[^*\w])\*([^*\n]+?)\*(?![*\w])/g, '$1<i>$2</i>')
    .replace(/\u2028/g, '<br>');
}

export function plain(s) { return (s || '').replace(/\*\*/g, '').replace(/(^|[^*])\*([^*]+)\*/g, '$1$2'); }

// "**a** text", "a text", "**a.** text" -> letter + rest
const SUB_B = /^\s*\*\*([a-h])[.)]?\*\*\s+(.*)$/;            // **a** text
const SUB_P = /^\s*([a-h])[.)]?\s+(?=[A-Z0-9*(“"'≥≤<>])(.*)$/;  // a Text  (not "a patient…")
const SUB = { test: l => SUB_B.test(l) || SUB_P.test(l) };
const subMatch = l => l.match(SUB_B) || l.match(SUB_P);

// T-131: "1. text" numbered steps keep their own lines and numbers
const NUM = /^\s*(\d{1,2})[.)]\s+(?=\S)(.*)$/;
function line(l, noSub) {
  const m = !noSub && subMatch(l);
  if (m && m[2]) return `<p class="sub"><span class="sp">${m[1]}</span><span>${inline(m[2])}</span></p>`;
  const n = l.match(NUM);
  if (n) return `<p class="sub num"><span class="sp np">${n[1]}</span><span>${inline(n[2])}</span></p>`;
  return `<p>${inline(l)}</p>`;
}
// T-131: a lone "a" (no "b" in the same field) that starts with bold text, or follows an unfinished line, is the article
// "a", not a part letter: "… induction dose and / a **full paralytic dose**"
function falseParts(lines) {
  const letters = new Set(lines.map(l => { const m = subMatch(l); return m ? m[1] : null; }).filter(Boolean));
  const bad = new Set();
  if (letters.has('b')) return bad;
  lines.forEach((l, i) => {
    const m = l.match(SUB_P); if (!m || m[1] !== 'a') return;
    const prev = i ? plain(lines[i - 1]).trim() : '';
    if (/^\*\*/.test(m[2]) || (prev && !/[.:!?]$/.test(prev))) bad.add(i);
  });
  return bad;
}

// T-130: a row is any line with a | between cells ("a | b", "a| b", " | b" for an empty first cell, "a |"); a bullet
// at the start of a cell is kept as "• "; a row group whose first row starts with a part letter ("b B. LOW | C. HIGH")
// shows that letter above the table
const ROW = /(^\s*\|\s*\S)|(\S\s*\|\s*\S)|(\S\s*\|\s*$)/;
export const isRow = l => ROW.test(plain(l || ''));
const cellsOf = r => r.replace(/^\s+|\s+$/g, '').split(/\s*\|\s*/).map(c => c.trim().replace(/^[-•]\s+/, '• '));
function table(rows) {
  let pre = '';
  const m = subMatch(rows[0]);
  if (m && m[2] && isRow(m[2])) { pre = `<p class="sub tlab"><span class="sp">${m[1]}</span></p>`; rows = [m[2], ...rows.slice(1)]; }
  const cells = rows.map(cellsOf);
  const n = Math.max(...cells.map(c => c.length));
  cells.forEach(r => { while (r.length < n) r.push(''); });
  // the first row is a header only when its cells are short labels; a long first row is data like the rest
  const hasHead = cells.length > 1 && cells[0].every(c => plain(c).length <= 45);
  const head = hasHead ? cells[0] : null, body = hasHead ? cells.slice(1) : cells;
  const labels = head ? head.map(plain) : [];
  let h = pre + `<div class="tbl c${n}${head ? '' : ' nohead'}" style="--gtc:minmax(0,.75fr) repeat(${Math.max(1, n - 1)},minmax(0,1.25fr))">` + (head ? '<div class="tr th">' + head.map(c => `<div class="td">${inline(c)}</div>`).join('') + '</div>' : '');
  for (const r of body) {
    h += '<div class="tr">' + r.map((c, j) => `<div class="td${j === 0 && !/^• /.test(c) ? ' t0' : ''}${c ? '' : ' empty'}"${j ? ` data-label="${esc(labels[j] || '')}"` : ''}>${inline(c)}</div>`).join('') + '</div>';
  }
  return h + '</div>';
}

// The cards keep the PDF's line wrapping. Rejoin wrapped lines:
//  - sub-parts, bullets and table rows always start a new line;
//  - a line that clearly continues the previous one (starts lower-case, with a digit, an arrow, a bracket,
//    an ALL-CAPS word, or the previous line ends on "and", "the", a comma…) is joined with a space;
//  - an open line followed by a capitalised one keeps a soft line break (likely a list without markers);
//  - otherwise a new paragraph.
const CONT_START = /^[a-z0-9(\[→←↑↓–\-\/,;:%+×=<>≥≤~&·]/;
const CAPS_WORD = /^[A-Z]{2,}[A-Z0-9'\-]*\b/;
const OPEN_END = /([,(\-–/+&→←]|\b(the|a|an|and|or|of|to|with|for|in|on|by|at|from|than|as|is|are|be|if|vs|via|per|not|no|THE|OF|AND|OR|TO|WITH|FOR|IN|ON|BY|AT|AS|IS|NOT|NO))$/;
export const SOFT = '\u2028';
export function reflow(md) {
  const out = [], src = (md || '').split('\n'), bad = falseParts(src);
  for (let li = 0; li < src.length; li++) {
    const raw = src[li];
    let l = raw.replace(/\s+$/, '');
    if (/\s\|$/.test(l)) l += ' ';            // "cell |" = row with an empty last cell
    if (!l.trim()) { out.push(''); continue; }
    const bare = plain(l).trim();
    const prev = out.length ? out[out.length - 1] : null;
    const startsCont = CONT_START.test(bare);
    const marker = (subMatch(l) && !bad.has(li)) || NUM.test(l) || /^\s*[-•]\s+/.test(l) || (isRow(l) && !startsCont);
    if (bad.has(li) && prev && prev.trim()) { out[out.length - 1] = prev.replace(/\s+$/, '') + ' ' + l.trim(); continue; }
    if (prev && !marker && prev.trim()) {
      const pb = plain(prev.split(SOFT).pop()).trim();
      const prevOpen = !/[.:!?]$/.test(pb);
      if (startsCont || (prevOpen && (CAPS_WORD.test(bare) || OPEN_END.test(pb)))) { out[out.length - 1] = prev.replace(/\s+$/, '') + ' ' + l.trim(); continue; }
      if (prevOpen && !isRow(prev)) { out[out.length - 1] = prev + SOFT + l.trim(); continue; }
    }
    out.push(l);
  }
  return out.join('\n');
}

export function render(md) {
  if (!md) return '';
  const lines = reflow(md).split('\n');
  let out = '', tbl = [], ul = [];
  const flush = () => {
    if (tbl.length) { out += tbl.length > 1 ? table(tbl) : line(tbl[0]); tbl = []; }
    if (ul.length) { out += '<ul>' + ul.map(x => `<li>${inline(x)}</li>`).join('') + '</ul>'; ul = []; }
  };
  for (const raw of lines) {
    const l = raw.replace(/\s+$/, '');
    if (isRow(l)) { if (ul.length) flush(); tbl.push(l); continue; }
    if (/^\s*[-•]\s+/.test(l)) { if (tbl.length) flush(); ul.push(l.replace(/^\s*[-•]\s+/, '')); continue; }
    flush();
    if (l.trim()) out += line(l);
  }
  flush();
  return out;
}

// Question: first line(s) before the first sub-part are the heading.
export function splitQ(q) {
  const lines = (q || '').split('\n');
  const head = [], rest = [];
  let inRest = false;
  for (const l of lines) {
    if (!inRest && (SUB.test(l) || isRow(l) || /^\s*[-•]\s/.test(l))) inRest = true;
    (inRest ? rest : head).push(l);
  }
  return { head: head.join(' ').replace(/\s+/g, ' ').trim(), rest: reflow(rest.join('\n')) };
}
