// The Plan: stretches of days, subjects (rows) spread over them at a pace, re-planned every day from what was walked.
// Pure numbers and storage; the screens live in app.js. Colour is never needed to read a plan: every cell is a number.
import { S, today, dkey, cardsOf, againList, repairsDueLater, missOf } from './store.js';
import { CHANNEL, IS_HT } from './config.js';

const KEY = (CHANNEL === 'test' ? 'trace-test.' : 'trace.') + (IS_HT ? 'ht.' : '') + 'plan';
const DAY = 864e5;
export const DAY_TYPES = [['normal', 'Normal', null], ['gt', 'GT day', 20], ['half', 'Half day', 30], ['off', 'Off', 0]];
export const addDays = (d, n) => dkey(new Date(d + 'T12:00:00').getTime() + n * DAY);
export const between = (a, b) => Math.round((new Date(b + 'T12:00:00') - new Date(a + 'T12:00:00')) / DAY);
const dayStart = d => new Date(d + 'T00:00:00').getTime();
const rid = () => Math.random().toString(36).slice(2, 9);

/* ---------- storage (this device; synced to Drive by sync.js on the live app) ---------- */
let P = null, lastJson = null;
// T-081/T-086: undo — the plan as it was before each change (last 40), kept on this device so it survives closing the app
const HKEY = KEY + '.undo';
const hist = (() => { try { const a = JSON.parse(localStorage.getItem(HKEY) || '[]'); return Array.isArray(a) ? a : []; } catch (e) { return []; } })();
const saveHist = () => { try { localStorage.setItem(HKEY, JSON.stringify(hist)); } catch (e) { hist.splice(0, Math.max(0, hist.length - 10)); try { localStorage.setItem(HKEY, JSON.stringify(hist)); } catch (er) { /* full */ } } };
export function loadPlan() {
  if (P) return P;
  try { P = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { P = null; }
  if (!P || !Array.isArray(P.stretches)) P = { v: 1, stretches: [], current: null, updated: 0 };
  lastJson = JSON.stringify(P);
  return P;
}
export function savePlan(touch = true) {
  if (touch) P.updated = Date.now();
  const j = JSON.stringify(P);
  if (touch && lastJson && lastJson !== j) { hist.push(lastJson); if (hist.length > 40) hist.shift(); saveHist(); }
  lastJson = j;
  try { localStorage.setItem(KEY, j); } catch (e) { /* private mode */ }
}
export const canUndoPlan = () => hist.length > 0;
export function undoPlan() {
  if (!hist.length) return false;
  P = JSON.parse(hist.pop()); saveHist(); P.updated = Date.now(); lastJson = JSON.stringify(P);
  try { localStorage.setItem(KEY, lastJson); } catch (e) { /* */ }
  return true;
}
export function replacePlan(next) { if (next && Array.isArray(next.stretches)) { P = next; savePlan(false); } }
export const planJson = () => loadPlan();
export function currentStretch() {
  const p = loadPlan(), td = today();
  let st = p.stretches.find(s => s.id === p.current);
  if (!st) st = p.stretches.find(s => td >= s.start && td <= addDays(s.start, s.days - 1)) || p.stretches[p.stretches.length - 1] || null;
  return st;
}
export function newStretch({ start, days, pace } = {}) {
  const p = loadPlan(), last = p.stretches[p.stretches.length - 1];
  const s = { id: rid(), name: 'Stretch ' + (p.stretches.length + 1), start: start || (last ? addDays(last.start, last.days) : today()), days: days || 10,
    pace: pace || (last ? last.pace : 65), ceiling: last ? last.ceiling : 75, dayType: {}, subjects: [], pins: {}, repair: { on: true, cap: 20, pos: 'first', spread: 'even' }, order: {}, created: Date.now() };
  p.stretches.push(s); p.current = s.id; savePlan();
  return s;
}
export function deleteStretch(id) { const p = loadPlan(); p.stretches = p.stretches.filter(s => s.id !== id); if (p.current === id) p.current = null; savePlan(); }
export function addSubject(st, { name, sub, keys, from }) {
  const s = { id: rid(), name, sub: sub || '', keys: [...new Set(keys)], mode: 'seq', daily: null, from: from && from > st.start ? from : null, addedAt: Date.now() };
  st.subjects.push(s); savePlan(); return s;
}
export const dayList = st => [...Array(st.days)].map((_, i) => addDays(st.start, i));
export const dayType = (st, d) => st.dayType[d] || 'normal';

/* ---------- what has been walked ---------- */
// first view of each card at or after a given time
let idx = null, idxN = -1;
function viewIndex() {
  if (idx && idxN === S.events.length + S.undone.size) return idx;
  idx = new Map();
  for (const e of S.events) {
    if (e.kind !== 'view' || S.undone.has(e.id) || !e.code) continue;
    const k = e.deck + '|' + e.code; (idx.get(k) || idx.set(k, []).get(k)).push(e.ts);
  }
  for (const a of idx.values()) a.sort((x, y) => x - y);
  idxN = S.events.length + S.undone.size;
  return idx;
}
function walkedAfter(key, t0) { const a = viewIndex().get(key); if (!a) return null; for (const t of a) if (t >= t0) return t; return null; }
export const subjectDone = (s, before = Infinity) => s.keys.filter(k => { const t = walkedAfter(k, s.addedAt); return t != null && t < before; }).length;
function cardOf(key) { const i = key.indexOf('|'), deck = key.slice(0, i), code = key.slice(i + 1); return cardsOf(deck).find(c => c.code === code) || null; }

/* ---------- the plan for a stretch ---------- */
export function compute(st) {
  const td = today(), days = dayList(st), t0 = dayStart(td), now = Date.now();
  const cap = d => { const t = DAY_TYPES.find(x => x[0] === dayType(st, d)); return t && t[2] != null ? t[2] : st.pace; };
  const isFuture = d => d >= td;
  const R = repairOpts(st);
  const subs = st.subjects;
  const cells = {}, actual = {}, overflow = {};
  for (const s of subs.concat([{ id: 'repair' }])) { cells[s.id] = {}; actual[s.id] = {}; overflow[s.id] = 0; }
  // what was actually walked, day by day (past days and today)
  for (const s of subs) for (const k of s.keys) { const t = walkedAfter(k, s.addedAt); if (t != null) { const d = dkey(t); if (days.includes(d)) actual[s.id][d] = (actual[s.id][d] || 0) + 1; } }
  const repairWalks = {};
  for (const e of S.events) {
    if (e.kind !== 'view' || S.undone.has(e.id) || !e.code) continue;
    const d = dkey(e.ts); if (!days.includes(d)) continue;
    const c = cardOf(e.deck + '|' + e.code); if (c && missOf(c)) repairWalks[d] = (repairWalks[d] || 0) + 1;
  }
  Object.assign(actual.repair, repairWalks);
  // what is left at the start of today
  const left = {}; for (const s of subs) left[s.id] = s.keys.length - subjectDone(s, t0);
  for (const s of subs) if (s.once && s.to && s.to < td) left[s.id] = 0;   // a today-only subject from an earlier day is finished with
  const leftStart = { ...left };
  const future = days.filter(isFuture);
  const repairTotal = R.on ? againList().length + repairsDueLater().filter(r => dkey(r.first || r.ts) <= days[days.length - 1]).length + (actual.repair[td] || 0) : 0;
  const workDays = future.filter(d => cap(d) > 0);
  // effective pace: raise normal days (up to the ceiling) when the work left needs it
  const demand = repairTotal + subs.reduce((t, s) => t + Math.max(0, left[s.id]), 0);
  const fixedCap = future.filter(d => dayType(st, d) !== 'normal').reduce((t, d) => t + cap(d), 0);
  const normalDays = future.filter(d => dayType(st, d) === 'normal').length;
  const needPace = normalDays ? Math.ceil(Math.max(0, demand - fixedCap) / normalDays) : 0;
  const effPace = Math.max(st.pace, Math.min(st.ceiling || st.pace, needPace));
  const capOf = d => dayType(st, d) === 'normal' ? effPace : cap(d);
  const room = {}; future.forEach(d => room[d] = capOf(d));
  // 1. repair pile: its share is kept for it each day (where it sits in the walk is its row position, used by todayCards).
  //    even = spread over the working days left; by = spread to a date; fixed = a set number a day. Never more than cap (even/by).
  let rep = repairTotal;
  const rDays = (R.spread === 'by' && R.by && workDays.some(d => d <= R.by)) ? workDays.filter(d => d <= R.by) : workDays;
  rDays.forEach((d, i) => {
    const pin = st.pins['repair|' + d];
    const want = pin != null ? pin : R.spread === 'fixed' ? R.fixed : Math.min(R.cap, Math.ceil(rep / (rDays.length - i)));
    const share = Math.max(0, Math.min(want, rep, pin != null ? Infinity : room[d]));
    if (share > 0) { cells.repair[d] = share; room[d] -= share; rep -= share; }
  });
  overflow.repair = Math.max(0, rep);
  // 2. pinned cells (a fixed number may go over the day's room: "go deep" today)
  for (const s of subs) for (const d of future) {
    const pin = st.pins[s.id + '|' + d];
    if (pin == null) continue;
    const v = Math.max(0, Math.min(pin, left[s.id])); cells[s.id][d] = v; room[d] -= v; left[s.id] -= v;
  }
  // 3. daily lanes (a number a day, or spread to their last day)
  for (const s of subs.filter(x => x.mode === 'daily')) {
    const fromD = s.from && s.from > td ? s.from : td, toD = s.to || days[days.length - 1];
    const span = future.filter(d => d >= fromD && d <= toD && room[d] > 0 && st.pins[s.id + '|' + d] == null);
    span.forEach((d, i) => {
      const want = s.daily ? s.daily : Math.ceil(left[s.id] / (span.length - i));
      const v = Math.max(0, Math.min(want, left[s.id], room[d])); if (v) { cells[s.id][d] = (cells[s.id][d] || 0) + v; room[d] -= v; left[s.id] -= v; }
    });
  }
  // 4. subjects in order, filling what is left of each day
  for (const s of subs.filter(x => x.mode !== 'daily')) {
    for (const d of future) {
      if (left[s.id] <= 0) break;
      if (st.pins[s.id + '|' + d] != null || room[d] <= 0 || (s.from && d < s.from)) continue;
      const v = Math.min(left[s.id], room[d]); cells[s.id][d] = (cells[s.id][d] || 0) + v; room[d] -= v; left[s.id] -= v;
    }
  }
  for (const s of subs) overflow[s.id] += Math.max(0, left[s.id]);
  // totals
  const total = {}; days.forEach(d => { total[d] = Object.values(cells).reduce((t, c) => t + (c[d] || 0), 0); });
  const done = {}; days.forEach(d => { done[d] = Object.values(actual).reduce((t, c) => t + (c[d] || 0), 0); });
  const over = Object.values(overflow).reduce((t, v) => t + v, 0);
  const cards = repairTotal + subs.reduce((t, s) => t + Math.max(0, leftStart[s.id]), 0);
  const roomAll = future.reduce((t, d) => t + capOf(d), 0);
  return { days, td, cap: capOf, cells, actual, overflow, over, total, done, effPace, needPace, raised: effPace > st.pace, cards, room: roomAll,
    spare: Math.max(0, roomAll - cards), repairTotal, leftStart, repairOpts: R, todayPlan: days.includes(td) ? total[td] || 0 : 0, active: days.includes(td), future };
}

/* ---------- repair options (older plans have only on + cap) ---------- */
export function repairOpts(st) {
  const r = st.repair || (st.repair = { on: true, cap: 20 });
  const n = st.subjects.length, at = r.at != null ? Math.max(0, Math.min(n, r.at)) : r.pos === 'last' ? n : 0;
  return { on: !!r.on, cap: r.cap == null ? 20 : r.cap, at, spread: ['even', 'by', 'fixed'].includes(r.spread) ? r.spread : 'even', by: r.by || null, fixed: r.fixed == null ? 10 : r.fixed };
}
/* ---------- the order of a day's walk: st.order[d] (ids), else repair first/last around the subjects ---------- */
export function dayOrder(st, d) {
  const base = rowOrder(st);
  const saved = (st.order && st.order[d]) || [];
  const out = saved.filter(id => base.includes(id));
  base.forEach(id => { if (!out.includes(id)) { const j = base.indexOf(id); const after = base.slice(0, j).reverse().find(x => out.includes(x)); out.splice(after ? out.indexOf(after) + 1 : 0, 0, id); } });
  return out;
}
// the rows in plan order: the subjects, with the repair pile placed among them like any other row
export function rowOrder(st) { const ids = st.subjects.map(s => s.id); ids.splice(repairOpts(st).at, 0, 'repair'); return ids; }
export function moveRow(st, id, k) {
  const rows = rowOrder(st), i = rows.indexOf(id), j = i + k; if (i < 0 || j < 0 || j >= rows.length) return;
  rows.splice(i, 1); rows.splice(j, 0, id);
  st.subjects = rows.filter(x => x !== 'repair').map(x => st.subjects.find(s => s.id === x));
  st.repair.at = rows.indexOf('repair'); delete st.repair.pos; savePlan();
}
export function setDayOrder(st, d, ids) { st.order = st.order || {}; st.order[d] = ids; Object.keys(st.order).forEach(k => { if (k < addDays(today(), -2)) delete st.order[k]; }); savePlan(); }

/* ---------- today's cards, in plan order ---------- */
export function todayCards(st, r = compute(st)) {
  if (!r.active) return [];
  const td = r.td, out = [], seenK = new Set();
  const doneToday = id => r.actual[id][td] || 0;
  const add = c => { const k = c.deck + '|' + c.code; if (!seenK.has(k)) { seenK.add(k); out.push(c); } };
  for (const id of dayOrder(st, td)) {
    if (id === 'repair') { againList().slice(0, Math.max(0, (r.cells.repair[td] || 0) - doneToday('repair'))).forEach(a => { const c = cardOf(a.deck + '|' + a.code); if (c) add(c); }); continue; }
    const s = st.subjects.find(x => x.id === id); if (!s) continue;
    let n = (r.cells[s.id][td] || 0) - doneToday(s.id);
    for (const k of s.keys) { if (n <= 0) break; if (walkedAfter(k, s.addedAt) != null) continue; const c = cardOf(k); if (c) { add(c); n--; } }
  }
  return out;
}
export function todayParts(st, r = compute(st)) {
  if (!r.active) return [];
  const td = r.td, parts = [];
  for (const id of dayOrder(st, td)) {
    if (!r.cells[id] || !r.cells[id][td]) continue;
    const s = st.subjects.find(x => x.id === id);
    parts.push({ id, name: id === 'repair' ? 'Repair' : s.name, n: r.cells[id][td], done: r.actual[id][td] || 0 });
  }
  return parts;
}
