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

function line(l) {
  const m = subMatch(l);
  if (m && m[2]) return `<p class="sub"><span class="sp">${m[1]}</span><span>${inline(m[2])}</span></p>`;
  return `<p>${inline(l)}</p>`;
}

function table(rows) {
  const cells = rows.map(r => r.split(' | ').map(c => c.trim()));
  cells.forEach(r => { if (r.length > 1 && r[r.length - 1] === '') r[r.length - 1] = ''; });
  const head = cells[0], body = cells.slice(1);
  const n = Math.max(...cells.map(c => c.length));
  const labels = head.map(plain);
  let h = `<div class="tbl c${n}" style="--gtc:minmax(0,.75fr) repeat(${Math.max(1, n - 1)},minmax(0,1.25fr))"><div class="tr th">` + head.map(c => `<div class="td">${inline(c)}</div>`).join('') + '</div>';
  for (const r of body) {
    h += '<div class="tr">' + r.map((c, j) => `<div class="td${j === 0 ? ' t0' : ''}"${j ? ` data-label="${esc(labels[j] || '')}"` : ''}>${inline(c)}</div>`).join('') + '</div>';
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
const isRow = l => l.includes(' | ') || /\s\|$/.test(l);
export function reflow(md) {
  const out = [];
  for (const raw of (md || '').split('\n')) {
    let l = raw.replace(/\s+$/, '');
    if (/\s\|$/.test(l)) l += ' ';            // "cell |" = row with an empty last cell
    if (!l.trim()) { out.push(''); continue; }
    const bare = plain(l).trim();
    const prev = out.length ? out[out.length - 1] : null;
    const startsCont = CONT_START.test(bare);
    const marker = subMatch(l) || /^\s*[-•]\s+/.test(l) || (isRow(l) && !startsCont);
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
    if (/^\s*[-•]\s+/.test(l)) { if (tbl.length) flush(); ul.push(l.replace(/^\s*[-•]\s+/, '')); continue; }
    if (l.includes(' | ')) { if (ul.length) flush(); tbl.push(l); continue; }
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
    if (!inRest && (SUB.test(l) || / \| /.test(l) || /^\s*[-•]\s/.test(l))) inRest = true;
    (inRest ? rest : head).push(l);
  }
  return { head: head.join(' ').replace(/\s+/g, ' ').trim(), rest: reflow(rest.join('\n')) };
}
