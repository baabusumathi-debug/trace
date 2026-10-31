// In-memory view of everything in IndexedDB, plus the derived numbers the screens need.
import { db } from './db.js';
import { CONFIG } from './config.js';

export const S = {
  library: null,          // { decks:[...], generated, changes? }
  neet: new Map(),        // 'DECK|CODE' or '*|CODE' -> 'NEET 24·25'
  decks: new Map(),       // deck -> { deck, version, cards[], verified, downloadedAt }
  edits: new Map(),       // 'DECK|CODE' -> { key, deck, code, fields, ts, dev, synced }
  events: [],             // view events (all devices)
  undone: new Set(),      // ids cancelled by an undo event
  logBase: {},            // deck -> { no: times seen in the old War Map flow }
  chunks: {},             // deck -> [{ id, from, to }]
  logDaily: {},           // 'yyyy-mm-dd' -> { min, cards } from the old War Map flow (not Trace)
  logChron: [],           // recent owner Log rows from the War Map flow: [date, time, deck, from, to, cards, min]
  target: null,           // { date, items:[{ id, deck, label, nos:[], item_id, synced, status }] }
  device: null,
  listeners: new Set()
};

export const emit = () => S.listeners.forEach(f => { try { f(); } catch (e) { console.error(e); } });

export async function loadAll() {
  S.library = (await db.kv.get('library')) || null;
  setNeet((await db.kv.get('neet')) || null);
  for (const d of await db.all('decks')) S.decks.set(d.deck, d);
  for (const e of await db.all('edits')) S.edits.set(e.key, e);
  const evs = await db.all('events');
  S.events = evs.filter(e => e.kind === 'view');
  S.undone = new Set(evs.filter(e => e.kind === 'undo').map(e => e.ref));
  S.logBase = (await db.kv.get('logBase')) || {};
  S.chunks = (await db.kv.get('chunks')) || {};
  S.logDaily = (await db.kv.get('logDaily')) || {};
  S.logChron = (await db.kv.get('logChron')) || [];
  S.target = (await db.kv.get('target')) || null;
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
  return d.cards.map(c => withEdits(c));
}
export function withEdits(c) {
  const e = S.edits.get(c.deck + '|' + c.code);
  return e && e.fields && Object.keys(e.fields).length ? { ...c, ...e.fields, edited: true } : c;
}
export function neetTag(c) {
  return S.neet.get(c.deck + '|' + c.code) || S.neet.get('*|' + c.code) || S.neet.get(c.deck + '|' + (c.section || '')) || '';
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
export function recount() {
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
    for (let i = 1; i <= d.cards; i++) if (seen(d.deck, i) > 0) n++;
    deckSeen.set(d.deck, n);
  }
}
export function seen(deck, no) {
  return (seenMap.get(deck + '|' + no) || 0) + ((S.logBase[deck] || {})[no] || 0);
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
