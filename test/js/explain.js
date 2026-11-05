// Explain layer (T-069 pilot): ready-made explanations, deck maps, bridges and rebuilt Top-up cards, shipped with the
// app as data/explain.json (same origin, offline once fetched). Card text is never changed; this sits beside it.
import { db } from './db.js';
import { S, emit } from './store.js';

export const X = { v: '', decks: {}, patterns: {} };
const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ch]));
// **bold** and *italic* only — the explain text is our own data, so this is all the markup it uses
const md = s => esc(s).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/(^|[^*])\*([^*]+)\*/g, '$1<i>$2</i>');

function apply(x) {
  if (!x || !x.decks) return;
  X.v = x.version || ''; X.decks = x.decks; X.patterns = x.patterns || {};
  // rebuilt Top-up cards replace the old dense ones for these decks, and their explanations are keyed TU-nn like the cards
  S.xtopups = {};
  for (const [deck, d] of Object.entries(X.decks)) {
    if (!d.topups || !d.topups.length) continue;
    S.xtopups[deck] = d.topups.map(t => ({ id: t.id, topic: t.topic, type: t.type, q: t.q, a: t.a, tier: t.tier, n: t.n, banks: t.banks, recall: /recall/i.test(t.banks || ''), src: t.banks || '', raw: true }));
    d.topups.forEach((t, i) => { if (t.x) d.cards['TU-' + String(i + 1).padStart(2, '0')] = { ...t.x, topup: true }; });
  }
}
export async function initExplain() { apply(await db.kv.get('explain')); }
export async function loadExplain() {
  try {
    const r = await fetch('./data/explain.json', { cache: 'no-cache' });
    if (!r.ok) return;
    const x = await r.json();
    if (x && x.version && x.version !== X.v) { apply(x); await db.kv.set('explain', x); emit(); }
  } catch (e) { /* offline: keep the stored copy */ }
}
export const xOf = c => (c && X.decks[c.deck] && X.decks[c.deck].cards[c.code]) || null;
export const mapOf = deck => (X.decks[deck] && X.decks[deck].map) || null;
export const spineOf = deck => (X.decks[deck] && X.decks[deck].spine) || null;
// T-088: the deck's story. "Step n of N" on the explanation; on the question face, the primer the first time a deck appears
// in a flow, and the takeaways of the steps you skipped when cards were left out (any-hit flows)
export function stepHtml(c, x) {
  const sp = spineOf(c.deck); if (!sp || !x || !x.step || !sp[x.step - 1]) return '';
  return `<p class="xv-step mono"><span>STEP ${x.step} OF ${sp.length}</span> ${md(sp[x.step - 1][0])}</p>`;
}
export function arcHtml(c, x, prevStep, first) {
  const d = X.decks[c.deck]; if (!d || !d.spine || !x || !x.step) return '';
  const from = first ? 1 : (prevStep || 0) + 1, gap = [];
  for (let k = from; k < x.step; k++) if (d.spine[k - 1]) gap.push(d.spine[k - 1]);
  let h = '';
  if (first && d.primer) h += `<div class="xp-before xp-primer"><span class="mono">STARTING ${esc(c.deck)} · WHAT YOU NEED FIRST</span><p>${md(d.primer)}</p></div>`;
  if (gap.length) h += `<div class="xp-before"><span class="mono">BEFORE THIS · ${gap.length === 1 ? 'THE STEP' : 'THE STEPS'} YOU SKIPPED</span><ul>${gap.map(([t, w]) => `<li><b>${md(t)}.</b> ${md(w)}</li>`).join('')}</ul></div>`;
  return h;
}
export const closeOf = deck => (X.decks[deck] && X.decks[deck].close) || null;
export const hasExplain = c => !!xOf(c);

/* ---------- pictures: small, fixed set; drawn by the app so every deck looks the same ---------- */
export function picture(p) {
  if (!p) return '';
  if (p.t === 'chain') return chainHtml(p.steps);
  if (p.t === 'grid') return `<div class="xp-grid"><table><thead><tr>${p.head.map(h => `<th>${md(h)}</th>`).join('')}</tr></thead><tbody>${p.rows.map(r => `<tr>${r.map((c, i) => i ? `<td>${md(c)}</td>` : `<th>${md(c)}</th>`).join('')}</tr>`).join('')}</tbody></table></div>`;
  if (p.t === 'fork') return `<div class="xp-fork"><div class="xf-q">${md(p.q)}</div>${p.branches.map(([a, b]) => `<div class="xf-row"><span class="xf-if">${md(a)}</span><span class="xf-ar" aria-hidden="true">→</span><span class="xf-then">${md(b)}</span></div>`).join('')}</div>`;
  if (p.t === 'trio') return `<div class="xp-trio">${p.items.map(([n, l]) => `<div><b>${md(n)}</b><span>${md(l)}</span></div>`).join('')}</div>`;
  if (p.t === 'steps') return `<ol class="xp-steps">${p.items.map(([a, b]) => `<li><b>${md(a)}</b><span>${md(b)}</span></li>`).join('')}</ol>`;
  if (p.t === 'scale') {
    // ticks and values on the line; the meaning of each mark in a list underneath (labels never collide)
    const W = 520, H = 52, x0 = 20, x1 = W - 20, X = v => x0 + (v - p.min) / (p.max - p.min) * (x1 - x0);
    const marks = p.marks.map(([v]) => `<g><line x1="${X(v)}" y1="26" x2="${X(v)}" y2="44" class="xs-tick"/><text x="${X(v)}" y="18" text-anchor="middle" class="xs-v">${v}</text></g>`).join('');
    return `<figure class="xp-scale"><figcaption class="mono">${esc(p.label)}</figcaption><svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(p.label)}"><line x1="${x0}" y1="35" x2="${x1}" y2="35" class="xs-axis"/>${marks}</svg><ul class="xs-key">${p.marks.map(([v, l]) => `<li><b>${v}</b> ${md(l)}</li>`).join('')}</ul></figure>`;
  }
  return '';
}
function chainHtml(steps) {
  return `<ol class="xp-chain">${steps.map((s, i) => `<li class="${i === steps.length - 1 ? 'end' : ''}">${md(s)}</li>`).join('')}</ol>`;
}

/* ---------- the Explain panel (answer side) ---------- */
// opts: { open, traps, note }
export function gistHtml(x) { return x && x.gist ? `<div class="xp-gist"><span class="mono">WHY</span><p>${md(x.gist)}</p></div>` : ''; }
export function panelHtml(c, x, opts) {
  if (!x) return '';
  if (x.v === 2) return learnHtml(c, x, opts);
  const blk = (cls, lab, body) => body ? `<div class="xp-b ${cls}"><span class="xp-lab mono">${lab}</span><div>${body}</div></div>` : '';
  const pats = (x.pat || []).filter(k => X.patterns[k]).map(k => `<button class="xp-pat mono" data-pat="${esc(k)}">▦ ${esc(X.patterns[k].name)}</button>`).join('');
  const traps = [x.trap, x.trap2].filter(Boolean);
  return `<div class="xp${opts.open ? ' open' : ''}">
    <button class="xp-tog" data-xp-tog aria-expanded="${opts.open}"><span>Explain</span><span class="mono xp-hint">${opts.open ? 'hide' : 'mechanism · context · what the exam tempts you with'}</span></button>
    <div class="xp-body"${opts.open ? '' : ' hidden'}>
      ${x.chain ? chainHtml(x.chain) : ''}
      ${picture(x.pic)}
      ${blk('xb-tempt', 'TEMPTING, BUT', x.tempt ? md(x.tempt) : '')}
      ${blk('xb-nbr', 'DON’T CONFUSE', x.nbr ? md(x.nbr) : '')}
      ${blk('xb-rule', 'RULE', x.rule ? `<b>${md(x.rule)}</b>` : '')}
      ${blk('xb-num', 'NUMBERS', x.nums ? md(x.nums) : '')}
      ${blk('xb-sits', 'WHERE IT SITS', x.sits ? md(x.sits) : '')}
      ${traps.length ? (opts.traps ? blk('xb-trap', 'EXAM TRAP', traps.map(t => `<p>${md(t)}</p>`).join('')) : `<p class="xp-trapoff mono">${traps.length} exam trap${traps.length > 1 ? 's' : ''} hidden · turn traps on in the Flow panel</p>`) : ''}
      ${pats ? `<div class="xp-pats">${pats}</div>` : ''}
      ${x.deeper ? `<details class="xp-deep"><summary>Deeper</summary><p>${md(x.deeper)}</p></details>` : ''}
      <label class="xp-note"><span class="mono">YOUR ANALOGY</span><textarea rows="2" data-xp-note placeholder="Your own picture for this — write or type">${esc(opts.note || '')}</textarea></label>
      <div class="xp-fb mono"><span>Was this useful?</span><button data-xp-fb="up" aria-label="Useful">👍</button><button data-xp-fb="down" aria-label="Not useful">👎</button><button data-xp-fb="long">too long</button><span class="xp-src">${x.topup ? 'Top-up · ' : ''}explain v${esc(X.v.slice(0, 4))}</span></div>
    </div></div>`;
}
/* ---------- Explain v2 (T-070): Learn on first sight, Revise afterwards ----------
   Learn  = what's going on → part by part (why) → table → close mimics → traps → how it is asked → punchline (last).
   Revise = how it is asked → traps → punchline, with a way back to the full explanation. */
export const depthOf = (x, n, pref) => !x || x.v !== 2 ? 'learn' : pref === 'learn' || pref === 'revise' ? pref : (n > 0 ? 'revise' : 'learn');
function learnHtml(c, x, opts) {
  const depth = opts.depth || 'learn', learn = depth === 'learn';
  const sec = (cls, lab, body) => body ? `<section class="xv ${cls}"><h4 class="mono">${lab}</h4>${body}</section>` : '';
  const why = (x.why || []).map(([l, t]) => `<p class="xv-part"><b class="xl">${esc(l)}</b><span>${md(t)}</span></p>`).join('');
  const tbl = x.table ? `<div class="xp-grid">${x.table.title ? `<p class="xv-tt">${md(x.table.title)}</p>` : ''}<table><thead><tr>${x.table.head.map(h => `<th>${md(h)}</th>`).join('')}</tr></thead><tbody>${x.table.rows.map(r => `<tr>${r.map((v, i) => i ? `<td>${md(v)}</td>` : `<th>${md(v)}</th>`).join('')}</tr>`).join('')}</tbody></table></div>` : '';
  const mim = (x.mimic || []).map(([a, b]) => `<li><b>${md(a)}</b> — ${md(b)}</li>`).join('');
  const trp = (x.traps || []).map(([a, b], i) => `<li><b>${md(a)}</b> is wrong. ${md(b)}</li>`).join('');
  const dec = (x.decode || []).map(([a, b]) => `<li><span class="xv-stem">${md(a)}</span><span class="xv-ar" aria-hidden="true">→</span><b>${md(b)}</b></li>`).join('');
  // T-084: approved corrections to the card text (the card itself is not edited)
  const fix = (x.fix || []).map(([a, b]) => `<li><span class="xv-was">Card: ${md(a)}</span><b>${md(b)}</b></li>`).join('');
  const fixSec = fix ? sec('xv-fix', 'CORRECTION TO YOUR CARD', `<ul>${fix}</ul>`) : '';
  const traps = trp ? (opts.traps ? sec('xv-trap', 'THE TRAPS', `<ul>${trp}</ul>`) : `<p class="xp-trapoff mono">${x.traps.length} exam trap${x.traps.length > 1 ? 's' : ''} hidden · turn traps on in the Flow panel</p>`) : '';
  const body = learn
    ? `${stepHtml(c, x)}${x.sub ? `<p class="xv-sub mono">${md(x.sub)}</p>` : ''}
       ${sec('xv-ctx', 'WHAT’S GOING ON', x.intro ? `<p>${md(x.intro)}</p>` : '')}
       ${fixSec}
       ${sec('xv-why', 'PART BY PART', why)}
       ${tbl}
       ${sec('xv-mim', 'CLOSE MIMICS', mim ? `<ul>${mim}</ul>` : '')}
       ${traps}
       ${sec('xv-dec', 'HOW IT IS ASKED', dec ? `<ul>${dec}</ul>` : '')}
       ${sec('xv-punch', 'PUNCHLINE', x.punch ? `<p>${md(x.punch)}</p>` : '')}`
    : `${stepHtml(c, x)}${fixSec}${sec('xv-dec', 'HOW IT IS ASKED', dec ? `<ul>${dec}</ul>` : '')}
       ${traps}
       ${sec('xv-punch', 'PUNCHLINE', x.punch ? `<p>${md(x.punch)}</p>` : '')}
       <button class="xv-more" data-xp-depth="learn">Read the full explanation</button>`;
  return `<div class="xp v2${opts.open ? ' open' : ''}" data-depth="${depth}">
    <div class="xp-bar"><button class="xp-tog" data-xp-tog aria-expanded="${opts.open}"><span>Explain</span></button>
      <span class="xv-seg" role="group" aria-label="Explanation depth"><button class="${learn ? 'on' : ''}" data-xp-depth="learn" aria-pressed="${learn}">Learn</button><button class="${learn ? '' : 'on'}" data-xp-depth="revise" aria-pressed="${!learn}">Revise</button></span></div>
    <div class="xp-body"${opts.open ? '' : ' hidden'}>${body}
      <div class="xp-fb mono"><span>Was this useful?</span><button data-xp-fb="up" aria-label="Useful">👍</button><button data-xp-fb="down" aria-label="Not useful">👎</button><button data-xp-fb="long">too long</button><button data-xp-fb="short">too short</button></div>
    </div></div>`;
}
// extra lettered parts (the rebuilt Top-up lines), shown from the second time a card is seen
export function partLetters(q, n) {
  const used = (String(q).match(/^\s*\**([a-h])\**\s/gm) || []).length;
  return [...Array(n)].map((_, i) => String.fromCharCode(97 + used + i));
}
export function partsQHtml(c, x) {
  if (!x || !x.parts || !x.parts.length) return '';
  const L = partLetters(c.q, x.parts.length);
  return `<div class="xp-qparts"><span class="mono">EXAM ADD-ONS</span>${x.parts.map((p, i) => `<p><b class="xl">${L[i]}</b> ${md(p.q)}</p>`).join('')}</div>`;
}
export function partsAHtml(c, x) {
  if (!x || !x.parts || !x.parts.length) return '';
  const L = partLetters(c.q, x.parts.length);
  return `<div class="box xp-aparts"><span class="mono">EXAM ADD-ONS</span><div class="bx">${x.parts.map((p, i) => `<p><b class="xl">${L[i]}</b> <span class="xq">${md(p.q)}</span><br>${md(p.a)}</p>`).join('')}</div></div>`;
}
// bridge from skipped cards (question side)
export function bridgeHtml(c, x, skipped) {
  if (!x) return '';
  let h = '';
  if (x.before && skipped) h += `<div class="xp-before"><span class="mono">BEFORE THIS · FROM CARDS YOU SKIPPED</span><p>${md(x.before)}</p></div>`;
  if (x.bridge && skipped) h += `<div class="xp-bridge"><span class="mono">BRIDGE · ${esc(x.bridge.code)}</span><p>${md(x.bridge.q)}</p><button class="xp-bshow" data-xp-bridge>Show answer</button><p class="xp-ba" hidden>${md(x.bridge.a)}</p></div>`;
  return h;
}
export function mapHtml(deck, title, walking) {
  const m = mapOf(deck); if (!m) return '';
  const sk = m.skipped || {};
  return `<div class="xp-map"><span class="mono kick dark">DECK MAP · ${esc(deck)}</span><h2>${md(m.title || title || deck)}</h2>
    <p class="muted-d small">Try to say the ideas before you read them. Numbered cards are the ones in this flow; the rest are one line each.</p>
    <ol class="xm-ideas">${m.ideas.map(it => `<li><b>${md(it.t)}</b><div class="xm-cards">${it.cards.map(code => walking.has(code) ? `<span class="xm-c on mono">${esc(code)}</span>` : `<span class="xm-c mono" title="${esc(sk[code] || '')}">${esc(code)}</span>${sk[code] ? `<span class="xm-sk">${md(sk[code])}</span>` : ''}`).join('')}</div></li>`).join('')}</ol>
    ${m.recall ? `<p class="xm-recall"><span class="mono">THE DECK IN ONE LINE</span>${md(m.recall)}</p>` : ''}</div>`;
}
export function closeHtml(deck) {
  const c = closeOf(deck); if (!c) return '';
  return `<div class="xp-map xp-close"><span class="mono kick dark">DECK CLOSE · ${esc(deck)}</span><h2>How it fits together</h2>
    <ul>${c.wrap.map(w => `<li>${md(w)}</li>`).join('')}</ul>
    ${c.q ? `<div class="xp-bridge"><span class="mono">ONE RECALL</span><p>${md(c.q.q)}</p><button class="xp-bshow" data-xp-bridge>Show answer</button><p class="xp-ba" hidden>${md(c.q.a)}</p></div>` : ''}</div>`;
}
export function patternHtml(k) {
  const p = X.patterns[k]; if (!p) return '';
  return `<p class="xp-patline"><b>${md(p.line)}</b></p><div class="xp-grid"><table><thead><tr>${p.head.map(h => `<th>${md(h)}</th>`).join('')}</tr></thead><tbody>${p.rows.map(r => `<tr>${r.map((c, i) => i ? `<td>${md(c)}</td>` : `<th>${md(c)}</th>`).join('')}</tr>`).join('')}</tbody></table></div>`;
}
// small per-device stores for notes and feedback
export async function getNote(c) { return (await db.kv.get('xpnote|' + c.deck + '|' + c.code)) || ''; }
export async function setNote(c, v) { await db.kv.set('xpnote|' + c.deck + '|' + c.code, v); }
export async function feedback(c, v) { const k = 'xpfb'; const all = (await db.kv.get(k)) || {}; all[c.deck + '|' + c.code] = { v, ts: Date.now(), ver: X.v }; await db.kv.set(k, all); }
