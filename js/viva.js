// Viva layer (T-095): one package file per INI viva package (data/viva/P4.json …), written by the content chat.
// New viva cards sit at the end of their deck (store.js vivaCardsOf); the package's question order drives a viva walk:
// a question card, its steps with a bridge under each answer, then the spine card (60 s timer, Fluent / Patchy / Blank).
// Card text is never changed here; the viva explanation is its own layer, beside the NEET one.
import { db } from './db.js';
import { IS_HT } from './config.js';
import { S, emit, recount, cardsOf } from './store.js';

export const VIVA_PKGS = ['P4', 'P1', 'P3', 'P6', 'P7'];
const IMG = pkg => `./data/viva/img/${pkg}/`;
const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ch]));
const md = s => esc(s).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/(^|[^*])\*([^*]+)\*/g, '$1<i>$2</i>');

// Viva is Naven's only (INI interview): HT's profile never loads a package, so no tile, chip, cards or explain appear
export async function initViva() { S.viva = IS_HT ? {} : (await db.kv.get('viva')) || {}; }
export async function loadViva() {
  if (IS_HT) return;
  let changed = false;
  for (const pkg of VIVA_PKGS) {
    try {
      const r = await fetch(`./data/viva/${pkg}.json`, { cache: 'no-cache' });
      if (!r.ok) continue;
      const p = await r.json();
      if (p && p.version && p.version !== (S.viva[pkg] && S.viva[pkg].version)) { S.viva = { ...S.viva, [pkg]: p }; changed = true; }
    } catch (e) { /* offline: keep the stored copy */ }
  }
  if (changed) { await db.kv.set('viva', S.viva); recount(); emit(); }
}
export const pkgs = () => VIVA_PKGS.filter(p => S.viva && S.viva[p]).map(p => S.viva[p]);
export const pkgOf = p => (S.viva && S.viva[p]) || null;

// a step key ("DECK|CODE" or "V4-001") → the card as Trace shows it (null if its deck is not on this device)
export function cardOfKey(pkg, key) {
  const P = pkgOf(pkg); if (!P) return null;
  if (/^V\d+-\d{3}$/.test(key)) { const v = P.cards[key]; return v ? cardsOf(v.deck).find(c => c.code === key) || null : null; }
  const [deck, code] = key.split('|');
  return cardsOf(deck).find(c => c.code === code) || null;
}
export const keyOf = c => c.vcard ? c.code : c.deck + '|' + c.code;

// The walk: every question in file order; a card under several questions comes back as a slim "seen above" step
export function vivaQueue(pkg, onlyQ) {
  const P = pkgOf(pkg); if (!P) return { list: [], missing: [] };
  const list = [], missing = [], first = new Map();
  for (const q of P.questions) {
    const steps = q.steps.map(s => ({ s, c: cardOfKey(pkg, s.card) }));
    steps.filter(x => !x.c).forEach(x => missing.push(x.s.card));
    const ok = steps.filter(x => x.c);
    if (onlyQ && q.q !== onlyQ) continue;          // one question alone: only repeats inside it count
    ok.forEach((x, i) => {
      const k = x.s.card, rep = first.has(k) ? first.get(k) : null;
      if (!rep) first.set(k, q.q);
      list.push({ ...x.c, vq: { pkg, q: q.q, i, j: q.steps.indexOf(x.s), n: ok.length, bridge: i === ok.length - 1 ? null : x.s.bridge, rep, key: k } });
    });
  }
  return { list, missing: [...new Set(missing)] };
}
// unique keys lit by a package (for the Mosaic)
export function vivaKeys(pkg) {
  const P = pkgOf(pkg); if (!P) return new Set();
  return new Set(P.questions.flatMap(q => q.steps.map(s => /^V/.test(s.card) ? (P.cards[s.card] || {}).deck + '|' + s.card : s.card)));
}
export const qOf = (pkg, qid) => { const P = pkgOf(pkg); return P ? P.questions.find(q => q.q === qid) : null; };

// the viva explanation of a card, from whichever package has one
export function vivaX(c) {
  if (!c) return null;
  const k = keyOf(c);
  for (const P of pkgs()) if (P.explain && P.explain[k]) return { x: P.explain[k], pkg: P.package };
  return null;
}
export const vivaLines = c => { const k = keyOf(c); return pkgs().flatMap(P => (P.lines && P.lines[k]) || []); };

/* ---------- html ---------- */
const TIER = { S: 'Tier S', A: 'Tier A', B: 'Tier B' };
const KIND = { direct: 'Direct', xvy: 'X vs Y', scenario: 'Scenario', spotter: 'Spotter', trial: 'Trial' };
export function vivaPanelHtml(vx, sw) {
  const x = vx.x, intro = String(x.intro || '').split('\n');
  const see = intro.filter(l => /^See it:/i.test(l)), body = intro.filter(l => !/^See it:/i.test(l));
  const why = (x.why || []).map(([l, t]) => `<p class="xv-part"><b class="xl">${esc(l || '•')}</b><span>${md(t)}</span></p>`).join('');
  const pic = x.pic ? `<figure class="vx-fig"><img src="${IMG(vx.pkg)}${esc(x.pic)}" alt="${esc(x.cap || 'Diagram')}" loading="lazy"><figcaption>${md(x.cap || '')}</figcaption></figure>` : '';
  return `<div class="xp v2 vx open" data-depth="learn">
    <div class="xp-bar"><button class="xp-tog" data-xp-tog aria-expanded="true"><span>Viva explain</span></button>${sw || ''}</div>
    <div class="xp-body">
      <section class="xv xv-ctx"><h4 class="mono">HOW IT WORKS</h4>${body.map(l => `<p>${md(l)}</p>`).join('')}${see.map(l => `<p class="vx-see">${md(l)}</p>`).join('')}</section>
      ${pic}
      ${why ? `<section class="xv xv-why"><h4 class="mono">WHY EACH PART</h4>${why}</section>` : ''}
      <p class="vx-v mono">VIVA ${esc(vx.pkg)} · v${esc(x.v)}</p>
    </div></div>`;
}
export const xpSwitch = tab => `<span class="xv-seg vx-sw" role="group" aria-label="Which explanation"><button class="${tab === 'neet' ? 'on' : ''}" data-xtab="neet" aria-pressed="${tab === 'neet'}">NEET</button><button class="${tab === 'viva' ? 'on' : ''}" data-xtab="viva" aria-pressed="${tab === 'viva'}">Viva</button></span>`;

export function qHeadHtml(pkg, qid, at) {
  const P = pkgOf(pkg), q = qOf(pkg, qid); if (!q) return '';
  const no = P.questions.indexOf(q) + 1;
  return `<div class="c-done vq-head">
    <span class="mono kick dark">VIVA ${esc(pkg)} · QUESTION ${no} OF ${P.questions.length}</span>
    <p class="vq-tags mono"><span class="vt vt-${esc(q.tier)}">${TIER[q.tier] || esc(q.tier)}</span><span>${esc(q.gen)}${q.handle ? ' ' + esc(q.handle) : ''}</span>${q.kind ? `<span>${KIND[q.kind] || esc(q.kind)}</span>` : ''}<span>${esc(q.q)}</span></p>
    <h2 class="vq-t">${md(q.text)}</h2>
    <p class="muted-d">Say your answer out loud first. Then walk the ${at.n} card${at.n === 1 ? '' : 's'} behind it${at.reps ? ` (${at.reps} seen above)` : ''}; the spine card comes last.</p>
  </div>`;
}
const MARKS = [['fluent', 'Fluent'], ['patchy', 'Patchy'], ['blank', 'Blank']];
export function spineHtml(pkg, qid, mark) {
  const q = qOf(pkg, qid); if (!q) return '';
  return `<div class="c-done vq-spine">
    <span class="mono kick dark">SPINE · ${esc(q.q)} · SAY IT IN 60 SECONDS</span>
    <h2 class="vq-t">${md(q.text)}</h2>
    <div class="vq-timer"><button class="pillbtn" data-vtimer>Start 60 s</button><span class="mono vq-clock" data-vclock>1:00</span></div>
    <details class="vq-lines" data-vspine><summary class="mono">SHOW THE SPINE · ${q.spine.length} lines</summary><ol>${q.spine.map(l => `<li>${md(l)}</li>`).join('')}</ol>${q.say60 ? `<p class="vq-say">${md(q.say60)}</p>` : ''}</details>
    <div class="vq-marks" role="group" aria-label="How did it go">${MARKS.map(([k, l]) => `<button class="chip${mark === k ? ' on' : ''}" data-vmark="${k}">${l}</button>`).join('')}</div>
    <p class="muted-d small">Marks stay on this device for now.</p>
  </div>`;
}

/* ---------- self-marks: kept per profile on this device ---------- */
export async function marks() { return (await db.kv.get('vivaMarks')) || {}; }
export async function setMark(pkg, qid, mark) {
  const m = await marks(), k = pkg + '|' + qid;
  m[k] = (m[k] || []).concat({ ts: Date.now(), mark });
  await db.kv.set('vivaMarks', m);
}
export const lastMark = (m, pkg, qid) => { const l = m[pkg + '|' + qid]; return l && l.length ? l[l.length - 1].mark : ''; };
