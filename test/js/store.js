// In-memory view of everything in IndexedDB, plus the derived numbers the screens need.
import { db } from './db.js';
import { CONFIG } from './config.js';

export const S = {
  library: null,          // { decks:[...], generated, changes? }
  neet: new Map(),        // 'DECK|CODE' or '*|CODE' -> 'NEET 24·25'
  qb: { version: '', cards: {}, topups: {} },   // QBank/GT layer (data/qbank.json): chips, lines, Crossfire, fixes, Top-up cards
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
  S.device = await db.kv.get('device');
  if (!S.device) {
    const ua = navigator.userAgent;
    const kind = /Mac/.test(ua) && !('ontouchend' in document) ? 'mac' : (Math.min(screen.width, screen.height) >= 700 ? 'tab' : 'phone');
    S.device = kind + '-' + Math.random().toString(36).slice(2, 6);
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
export const COMPONENTS = [['neet', 'NEET'], ['gt', 'DocT GT'], ['doct', 'DocT QBank'], ['marrow', 'Marrow'], ['topup', 'Top-up']];
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
