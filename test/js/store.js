// In-memory view of everything in IndexedDB, plus the derived numbers the screens need.
import { db } from './db.js';
import { CONFIG, IS_HT } from './config.js';

export const S = {
  library: null,          // { decks:[...], generated, changes? }
  neet: new Map(),        // 'DECK|CODE' or '*|CODE' -> 'NEET 24·25'
  qb: { version: '', cards: {}, topups: {} },   // QBank/GT layer (data/qbank.json): chips, lines, Crossfire, fixes, Top-up cards
  qmap: { version: '', q: {} },   // DocT question ID -> cards (data/qmap.json)
  doct: [],               // this profile's DocT attempts sent by the recorder, merged per sitting
  decks: new Map(),       // deck -> { deck, version, cards[], verified, downloadedAt }
  edits: new Map(),       // 'DECK|CODE' -> { key, deck, code, fields, ts, dev, synced }
  events: [],             // view events (all devices)
  undone: new Set(),      // ids cancelled by an undo event
  logBase: {},            // deck -> { no: times seen in the old War Map flow }
  chunks: {},             // deck -> [{ id, from, to }]
  logDaily: {},           // 'yyyy-mm-dd' -> { min, cards } from the old War Map flow (not Trace)
  logChron: [],           // recent owner Log rows from the War Map flow: [date, time, deck, from, to, cards, min]
  target: null,
  deckFrom: {},           // deck -> first card number in the War Map's numbering (Decks tab card_from)
  gtDays: {},             // 'yyyy-mm-dd' -> 'GT'           // { date, items:[{ id, deck, label, nos:[], item_id, synced, status }] }
  device: null,
  listeners: new Set()
};

export const emit = () => S.listeners.forEach(f => { try { f(); } catch (e) { console.error(e); } });

export async function loadAll() {
  S.library = (await db.kv.get('library')) || null;
  setNeet((await db.kv.get('neet')) || null);
  setQb((await db.kv.get('qbank')) || null);
  S.qmap = (await db.kv.get('qmap')) || { version: '', q: {} };
  setDoct((await db.kv.get('doctAtt')) || {});
  for (const d of await db.all('decks')) S.decks.set(d.deck, d);
  for (const e of await db.all('edits')) S.edits.set(e.key, e);
  applyTopupDecks();
  const evs = await db.all('events');
  S.events = evs.filter(e => e.kind === 'view');
  S.undone = new Set(evs.filter(e => e.kind === 'undo').map(e => e.ref));
  S.logBase = (await db.kv.get('logBase')) || {};
  S.chunks = (await db.kv.get('chunks')) || {};
  S.logDaily = (await db.kv.get('logDaily')) || {};
  S.logChron = (await db.kv.get('logChron')) || [];
  S.target = (await db.kv.get('target')) || null;
  S.deckFrom = (await db.kv.get('deckFrom')) || {};
  S.gtDays = (await db.kv.get('gtDays')) || {};
  S.gtScores = (await db.kv.get('gtScores')) || {};
  S.device = await db.kv.get('device');
  if (!S.device) {
    const ua = navigator.userAgent;
    const kind = /Mac/.test(ua) && !('ontouchend' in document) ? 'mac' : (Math.min(screen.width, screen.height) >= 700 ? 'tab' : 'phone');
    S.device = (IS_HT ? 'HT-' : '') + kind + '-' + Math.random().toString(36).slice(2, 6);
    await db.kv.set('device', S.device);
  }
  recount();
}

export function setNeet(n) {
  S.neet = new Map();
  if (!n || !n.cards) return;
  for (const c of n.cards) S.neet.set((c.deck || '*') + '|' + c.code, c.tag);
}

/* ---------- cards ---------- */
export function deckMeta(code) { return S.library ? S.library.decks.find(d => d.deck === code) : null; }

export function cardsOf(deck) {
  const d = S.decks.get(deck);
  if (!d) return [];
  return d.cards.map(c => withEdits(c)).concat(topupsOf(deck, d.cards).map(c => withEdits(c)));
}
/* ---------- QBank/GT layer: never changes card text; Top-ups are extra cards at the end of their deck ---------- */
export function setQb(q) { S.qb = q && q.cards ? q : { version: '', cards: {}, topups: {}, decks: [] }; applyTopupDecks(); }
// Top-up decks live in the layer, not in Drive: they are added to the library and to the deck store on every load.
export function applyTopupDecks() {
  const list = (S.qb && S.qb.decks) || [];
  if (S.library) S.library = { ...S.library, decks: S.library.decks.filter(d => !d.topupDeck).concat(list.map(t => ({ deck: t.deck, title: t.title, system: t.system, version: 1, cards: t.cards.length, star: 0, topupDeck: true }))) };
  for (const [k, d] of [...S.decks]) if (d.virtual) S.decks.delete(k);
  for (const t of list) S.decks.set(t.deck, { deck: t.deck, version: 1, verified: true, virtual: true, cards: t.cards.map(c => ({ ...c, deck: t.deck, tdeck: true })) });
}
export const isTopupDeck = deck => { const d = S.decks.get(deck); return !!(d && d.virtual); };
export const hasTopups = deck => !!(S.qb.topups[deck] && S.qb.topups[deck].length);
export function qbOf(c) { return (c && S.qb.cards[c.deck + '|' + c.code]) || null; }
// What hit a card, and how much it is worth. Pools (narrow → wide): NEET ⊂ NEET + GT ⊂ Any hit. Top-ups count by the banks they came from.
const W = { recall: 5, gt: 2, doct: 1, marrow: 1 };
export function hitsOf(c) {
  const h = new Set(); let score = 0;
  if (neetTag(c)) { h.add('neet'); score += 6; }
  const mk = missMap.get(c.deck + '|' + c.code);
  if (mk) for (const k of mk.kinds) h.add(k);
  const recallOnly = k => k === 'recall';   // NEET 2025 recall is part of the NEET tag now, not a separate bank
  if (c.topup || c.tdeck) {
    h.add('topup');
    const b = c.banks || '';
    if (c.recall || /Recall/i.test(b)) { h.add('neet'); score += 5; }
    if (/\bGT\b/.test(b)) h.add('gt');
    if (/\bDocT\b/.test(b)) h.add('doct');
    if (/Marrow/i.test(b)) h.add('marrow');
    score += c.tdeck ? 3 : 1.5 * (c.nq || 1) + (c.tier === 1 ? 3 : 0);
  } else {
    const q = qbOf(c);
    if (q && q.chips) for (const x of q.chips) { if (recallOnly(x.k)) continue; h.add(x.k); score += (W[x.k] || 1) * Math.min(x.n, 6); }
  }
  return { h, score };
}
// Pools are built from components that add up (union): e.g. 'neet+gt', 'doct+marrow', 'doct+marrow+gt'. 'hit' = any component; 'all' = every card.
// The gold ring and the NEET pool are the same set: a real NEET-SS paper tag, or the DocT NEET 2025 recall paper.
export const isNeet = c => !!neetTag(c);
export const COMPONENTS = [['neet', 'NEET'], ['gt', 'DocT GT'], ['doct', 'DocT QBank'], ['marrow', 'Marrow'], ['topup', 'Top-up'], ['missq', 'Missed · QBank'], ['missgt', 'Missed · GT'], ['guess', 'Guessed']];
export const POOLS = [['all', 'All'], ['hit', 'Any hit'], ...COMPONENTS];
const LEGACY = { neetgt: 'neet+gt' };
export const poolParts = p => (!p || p === 'all' || p === 'entire') ? [] : p === 'hit' ? ['hit'] : String(LEGACY[p] || p).split('+').filter(Boolean);
export function inPool(c, p) {
  const parts = poolParts(p);
  if (!parts.length) return true;
  const { h } = hitsOf(c);
  if (parts[0] === 'hit') return h.size > 0;
  return parts.some(k => h.has(k));
}
export function togglePool(cur, k) {
  if (k === 'all' || k === 'hit') return k;
  const set = new Set(poolParts(cur).filter(x => x !== 'hit'));
  set.has(k) ? set.delete(k) : set.add(k);
  return set.size ? COMPONENTS.map(c => c[0]).filter(x => set.has(x)).join('+') : 'all';
}
export const poolName = p => { const parts = poolParts(p); if (!parts.length) return 'All'; if (parts[0] === 'hit') return 'Any hit'; return parts.map(k => (COMPONENTS.find(c => c[0] === k) || [k, k])[1]).join(' + '); };
export function realCount(deck) { const d = S.decks.get(deck); return d ? (d.virtual ? 0 : Math.max(0, ...d.cards.map(c => +c.no || 0))) : Infinity; }
function topupsOf(deck, cards) {
  const list = S.qb.topups[deck];
  if (!list || !list.length) return [];
  const base = Math.max(0, ...cards.map(c => +c.no || 0));
  const lineOf = l => /^\s*([-•]|\w[^|]* \| )/.test(l) ? l : '- ' + l;   // numbered steps become list lines too, so reflow keeps them apart
  return list.map((t, i) => ({ deck, code: 'TU-' + String(i + 1).padStart(2, '0'), no: base + i + 1, section: 'Top-up', topup: true, tier: t.tier, ttype: t.type, tid: t.id,
    q: t.q, a: t.a.map(lineOf).join('\n'), why: '', watch: '', hook: '', banks: t.banks, nq: t.n, recall: t.recall, src: t.src || '' }));
}
// A card's chunk = the War Map Chunks tab range that holds it (card numbers converted with off()). Top-up cards
// form one chunk at the end of their deck; decks with no Chunks rows (e.g. Top-up decks) fall back to section headings.
export function chunkOf(c) {
  if (!c) return { key: '', name: '' };
  if (c.topup) return { key: 'TU', name: 'Top-up' };
  const list = S.chunks[c.deck];
  if (list && list.length && !c.tdeck) {
    const n = +c.no + off(c.deck), ch = list.find(x => n >= x.from && n <= x.to);
    if (ch) return { key: ch.id, name: ch.name || c.section || ch.id };
  }
  return { key: 's:' + (c.section || ''), name: c.section || 'Cards' };
}
export function withEdits(c) {
  const e = S.edits.get(c.deck + '|' + c.code);
  return e && e.fields && Object.keys(e.fields).length ? { ...c, ...e.fields, edited: true } : c;
}
function rawNeetTag(c) {
  return S.neet.get(c.deck + '|' + c.code) || S.neet.get('*|' + c.code) || S.neet.get(c.deck + '|' + (c.section || '')) || '';
}
// NEET tag (gold ring). 2024 = the 2024 recall tags (no full paper exists). 2025 = DocT's full NEET-SS 2025 recall paper
// (the layer's recall chip) plus the Marrow-only 2025 recall items the DocT paper lacks (layer: neet25extra). The old
// merged 2025 tags are no longer used.
export function neetTag(c) {
  if (!c) return '';
  const raw = rawNeetTag(c), has24 = /24/.test(raw);
  const q = qbOf(c), ex = S.qb.neet25extra || {};
  const has25 = !!(q && q.chips && q.chips.some(x => x.k === 'recall')) || !!ex[c.deck + '|' + c.code] || !!c.recall || /Recall/i.test(c.banks || '');
  return has24 && has25 ? 'NEET 24·25' : has24 ? 'NEET 24' : has25 ? 'NEET 25' : '';
}

/* ---------- times seen ---------- */
let seenMap = new Map();      // 'DECK|no' -> count from this app
let deckSeen = new Map();     // deck -> number of distinct cards seen at least once
let lastMap = new Map();      // 'DECK|no' -> last view ts
let deckLast = new Map();     // deck -> last view ts
let traceDaily = {};          // date -> { ms, cards:Set }
let againMap = new Map();     // 'DECK|no' -> last Again view not yet cleared by a later session
let missMap = new Map();      // 'DECK|CODE' -> { kinds:Set(missq|missgt|guess), last:{...} } from DocT attempts
let repairs = [];             // DocT misses still to repair: [{ deck, code, why, label, cohort, ts, kind }]
let unmapped = [];            // DocT misses with no card yet: [{ mcqid, label, deck, ts }]
const dkey = ts => { const d = new Date(ts); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); };
export const today = () => dkey(Date.now());
export { dkey };
// The War Map numbers split decks continuously (HEMO01B = cards 10–22); some converted decks restart at 1.
// off(deck) converts: War Map number = Trace no + off(deck).
const offCache = new Map();
export function off(deck) {
  if (offCache.has(deck)) return offCache.get(deck);
  const d = S.decks.get(deck), f = +S.deckFrom[deck] || 0;
  let o = 0;
  if (d && d.cards.length && f > 1) { const min = Math.min(...d.cards.map(c => c.no)); if (min === 1) o = f - 1; }
  offCache.set(deck, o);
  return o;
}
export function recount() {
  offCache.clear();
  seenMap = new Map(); lastMap = new Map(); deckLast = new Map(); traceDaily = {};
  for (const e of S.events) {
    if (S.undone.has(e.id)) continue;
    const k = e.deck + '|' + e.no;
    seenMap.set(k, (seenMap.get(k) || 0) + 1);
    if (!(lastMap.get(k) > e.ts)) lastMap.set(k, e.ts);
    if (!(deckLast.get(e.deck) > e.ts)) deckLast.set(e.deck, e.ts);
    const dk = dkey(e.ts), t = traceDaily[dk] || (traceDaily[dk] = { ms: 0, cards: new Set() });
    t.ms += Math.min(e.ms || 0, 20 * 60000); t.cards.add(k);
  }
  // Again pile: a card marked Again stays until it is walked without Again in a later session.
  againMap = new Map();
  for (const e of [...S.events].sort((a, b) => a.ts - b.ts)) {
    if (S.undone.has(e.id)) continue;
    const k = e.deck + '|' + e.no, a = againMap.get(k);
    if (e.again) againMap.set(k, { deck: e.deck, no: e.no, code: e.code, ts: e.ts, session: e.session });
    else if (a && e.ts > a.ts && e.session !== a.session) againMap.delete(k);
  }
  buildRepairs();
  deckSeen = new Map();
  if (!S.library) return;
  for (const d of S.library.decks) {
    let n = 0;
    const dd = S.decks.get(d.deck);
    if (dd && dd.cards.length) { for (const c of dd.cards) if (seen(d.deck, c.no) > 0) n++; }
    else for (let i = 1; i <= d.cards; i++) if (seen(d.deck, i) > 0) n++;
    deckSeen.set(d.deck, n);
  }
  recountStars();
}
// ✦ stars = NEET (gold-ring) cards in the deck, from the current NEET set (2024 tags + DocT's 2025 recall paper).
// Decks not on this device yet keep the library's old count until they download.
export function recountStars() {
  if (!S.library) return;
  for (const d of S.library.decks) {
    if (d.topupDeck) continue;
    if (d.star0 === undefined) d.star0 = d.star || 0;
    const dd = S.decks.get(d.deck);
    d.star = dd && dd.cards.length ? cardsOf(d.deck).filter(isNeet).length : d.star0;
  }
}
export function seen(deck, no) {
  return (seenMap.get(deck + '|' + no) || 0) + ((S.logBase[deck] || {})[no + off(deck)] || 0);
}
export const walked = deck => deckSeen.get(deck) || 0;
/** cards in the Again pile, newest first: Trace Again marks + DocT misses due today (from the day after the test) */
export function againList() {
  const out = new Map();
  for (const a of againMap.values()) out.set(a.deck + '|' + a.code, { ...a, why: 'Marked Again in Flow' });
  const t = today();
  for (const r of repairs) if (dkey(r.first || r.ts) < t && !out.has(r.deck + '|' + r.code)) out.set(r.deck + '|' + r.code, r);
  // most urgent first: wrong-and-sure, then guessed wrong, then skipped, then guessed right; within each, misses most of the cohort got right
  const rank = w => /^Wrong and sure/.test(w) ? 0 : /^Guessed wrong/.test(w) ? 1 : /^Skipped/.test(w) ? 2 : /^Guessed right/.test(w) ? 3 : 4;
  return [...out.values()].sort((a, b) => rank(a.why) - rank(b.why) || (+b.cohort || 0) - (+a.cohort || 0) || b.ts - a.ts);
}
export const repairsDueLater = () => repairs.filter(r => dkey(r.first || r.ts) >= today());
export const unmappedMisses = () => unmapped;
export const missOf = c => missMap.get(c.deck + '|' + c.code) || null;
/* ---------- DocT attempts → misses → repair cards ---------- */
// attempts: { fileId: record } as sent by the recorder; one sitting can arrive as attempt + review files (merged here)
export function setDoct(files) {
  const by = new Map();
  for (const r of Object.values(files || {})) {
    if (!r || !r.questions) continue;
    const k = (r.who || '') + '|' + (r.started || '');
    const m = by.get(k) || { ...r, questions: [] , saved_at: r.saved_at };
    const qs = new Map(m.questions.map(q => [q.mcqid, q]));
    for (const q of r.questions) { const o = qs.get(q.mcqid) || {}; const n = { ...o }; for (const [f, v] of Object.entries(q)) if (v != null && v !== '' && !(Array.isArray(v) && !v.length)) n[f] = v; qs.set(q.mcqid, n); }
    m.questions = [...qs.values()];
    if (!m.module && r.module) m.module = r.module;
    if (r.anchor && !m.anchor) m.anchor = r.anchor;
    if (r.lists) { m.lists = { ...(m.lists || {}) }; for (const [f, nos] of Object.entries(r.lists)) m.lists[f] = [...new Set([...(m.lists[f] || []), ...nos])]; }
    if (r.saved_at > (m.saved_at || '')) m.saved_at = r.saved_at;
    by.set(k, m);
  }
  S.doct = [...by.values()].sort((a, b) => String(a.saved_at).localeCompare(String(b.saved_at)));
}
function qStatus(q) {
  const flags = q.flags || [];
  const wrong = !!q.marked_wrong || flags.includes('Wrong') || flags.includes('Guessed Wrong') || !!(q.chosen && q.correct && q.chosen !== q.correct);
  const guessed = !!q.guess || flags.some(f => /^Guessed/.test(f));
  if (wrong) return guessed ? 'Guessed wrong' : 'Wrong and sure';
  if (flags.some(f => /Skipped/.test(f))) return 'Skipped';
  if (guessed && (q.correct || flags.includes('Guessed Right'))) return 'Guessed right';
  return '';
}
// "Module Q7" -> DocT question ID, from the map's labels (for lists read in one tap from the review's question grid)
let labelIdx = null, labelVer = '';
function byLabel(l) {
  if (!labelIdx || labelVer !== S.qmap.version) { labelIdx = new Map(); labelVer = S.qmap.version; for (const [id, e] of Object.entries(S.qmap.q || {})) if (e.l) labelIdx.set(e.l, id); }
  return labelIdx.get(l);
}
// a sitting's questions, plus the Wrong / Guessed lists read from the grid (numbers -> IDs via the anchor question's paper)
function sittingQuestions(a, qm) {
  const qs = new Map((a.questions || []).map(q => [q.mcqid, { ...q }]));
  const an = a.anchor, ae = an && qm[an.mcqid];
  if (an && qs.has(an.mcqid)) qs.get(an.mcqid).qno = an.qno;          // in a filtered review DocT numbers questions 1…n of the list
  if (a.lists && ae && ae.l && ae.l.endsWith(' Q' + an.qno)) {
    const paper = ae.l.slice(0, ae.l.lastIndexOf(' Q'));
    for (const [f, nos] of Object.entries(a.lists)) for (const n of nos) {
      const id = byLabel(paper + ' Q' + n) || ('?' + paper + ' Q' + n);
      const q = qs.get(id) || { mcqid: id, qno: n, flags: [] };
      q.qno = n; q.flags = [...new Set([...(q.flags || []), f])]; if (/^Guessed/.test(f)) q.guess = true;
      qs.set(id, q);
    }
  } else if (a.lists) {                       // paper not in the map: count the misses as "no card yet"
    for (const [f, nos] of Object.entries(a.lists)) for (const n of nos) {
      if (an && an.qno === n && qs.has(an.mcqid)) continue;          // already there as the question on screen
      const id = '?' + (a.module || 'paper') + ' Q' + n;
      if (!qs.has(id)) qs.set(id, { mcqid: id, qno: n, flags: [f], guess: /^Guessed/.test(f) });
    }
  }
  return [...qs.values()];
}
function buildRepairs() {
  missMap = new Map(); unmapped = [];
  const latest = new Map();
  const qm = (S.qmap && S.qmap.q) || {};
  for (const a of S.doct) {
    const ts = Date.parse(a.saved_at || a.started) || 0, kind = a.kind === 'gt' ? 'gt' : 'qbank';
    for (const q of sittingQuestions(a, qm)) {
      const why = qStatus(q);
      if (!why) continue;
      const e = qm[q.mcqid], label = e && e.l ? e.l : (a.module || (kind === 'gt' ? 'GT' : 'QBank')) + ' Q' + (q.qno || '?');
      if (!e || !e.c || !e.c.length) { unmapped.push({ mcqid: q.mcqid, label, deck: e ? e.d : '', why, ts }); continue; }
      for (const key of e.c) {
        const i = key.indexOf('|'), item = { deck: key.slice(0, i), code: key.slice(i + 1), why, label, cohort: q.cohort, ts, kind };
        const mm = missMap.get(key) || { kinds: new Set(), last: null };
        mm.kinds.add(why === 'Guessed right' ? 'guess' : kind === 'gt' ? 'missgt' : 'missq');
        if (/^Guessed/.test(why)) mm.kinds.add('guess');
        mm.last = item; missMap.set(key, mm);
        const prev = latest.get(key);
        item.first = prev ? Math.min(prev.first, ts) : ts;      // due from the day after the earliest miss
        if (!prev || ts >= prev.ts) latest.set(key, item); else prev.first = item.first;
      }
    }
  }
  // a repair is done once the card is walked (without Again) after the test that missed it
  const passed = new Map();
  for (const e of S.events) { if (S.undone.has(e.id) || e.again || !e.code) continue; const k = e.deck + '|' + e.code; if (!(passed.get(k) > e.ts)) passed.set(k, e.ts); }
  repairs = [...latest.entries()].filter(([k, it]) => !(passed.get(k) > it.ts)).map(([, it]) => it);
}
export const lastSeen = (deck, no) => lastMap.get(deck + '|' + no) || 0;
export const deckLastTs = deck => deckLast.get(deck) || 0;
export const seenOn = (deck, no, day) => { const t = traceDaily[day]; return !!(t && t.cards.has(deck + '|' + no)); };
/** minutes and cards per day: War Map flow rows + Trace views */
export function daily(day) {
  const a = S.logDaily[day] || { min: 0, cards: 0 }, t = traceDaily[day];
  return { min: a.min + (t ? t.ms / 60000 : 0), cards: a.cards + (t ? t.cards.size : 0) };
}
export function allDays() { return [...new Set([...Object.keys(S.logDaily), ...Object.keys(traceDaily)])].sort(); }

/* ---------- pace ---------- */
export function avgPace() {
  const ms = [];
  for (let i = S.events.length - 1; i >= 0 && ms.length < CONFIG.avgWindow; i--) {
    const e = S.events[i];
    if (!S.undone.has(e.id) && e.ms > 2000 && e.ms < 20 * 60000) ms.push(e.ms);
  }
  return ms.length ? ms.reduce((a, b) => a + b, 0) / ms.length : 0;
}

/* ---------- presentation helpers ---------- */
export function tier(star) { return star >= 5 ? 'gold' : star >= 3 ? 'silver' : star >= 1 ? 'bronze' : 'plain'; }
export function shade(n) { return Math.min(3, n); }
export function systems() {
  if (!S.library) return [];
  const m = new Map();
  for (const d of S.library.decks) {
    if (!m.has(d.system)) m.set(d.system, []);
    m.get(d.system).push(d);
  }
  return [...m.entries()].sort((a, b) => a[0].localeCompare(b[0], undefined, { numeric: true }))
    .map(([name, decks]) => ({ name, label: name.replace(/^\d+\s+/, ''), decks: decks.sort((a, b) => a.deck.localeCompare(b.deck, undefined, { numeric: true })) }));
}
export const isReady = deck => { const d = S.decks.get(deck), m = deckMeta(deck); return !!(d && d.verified && m && d.version >= m.version); };
