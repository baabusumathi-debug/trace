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
let P = null;
export function loadPlan() {
  if (P) return P;
  try { P = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { P = null; }
  if (!P || !Array.isArray(P.stretches)) P = { v: 1, stretches: [], current: null, updated: 0 };
  return P;
}
export function savePlan(touch = true) {
  if (touch) P.updated = Date.now();
  try { localStorage.setItem(KEY, JSON.stringify(P)); } catch (e) { /* private mode */ }
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
    pace: pace || (last ? last.pace : 65), ceiling: last ? last.ceiling : 75, dayType: {}, subjects: [], pins: {}, repair: { on: true, cap: 20 }, created: Date.now() };
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
  const future = days.filter(isFuture);
  const repairTotal = st.repair && st.repair.on ? againList().length + repairsDueLater().filter(r => dkey(r.first || r.ts) <= days[days.length - 1]).length + (actual.repair[td] || 0) : 0;
  const workDays = future.filter(d => cap(d) > 0);
  // effective pace: raise normal days (up to the ceiling) when the work left needs it
  const demand = repairTotal + subs.reduce((t, s) => t + Math.max(0, left[s.id]), 0);
  const fixedCap = future.filter(d => dayType(st, d) !== 'normal').reduce((t, d) => t + cap(d), 0);
  const normalDays = future.filter(d => dayType(st, d) === 'normal').length;
  const needPace = normalDays ? Math.ceil(Math.max(0, demand - fixedCap) / normalDays) : 0;
  const effPace = Math.max(st.pace, Math.min(st.ceiling || st.pace, needPace));
  const capOf = d => dayType(st, d) === 'normal' ? effPace : cap(d);
  const room = {}; future.forEach(d => room[d] = capOf(d));
  // 1. repair pile first, spread over the working days left, at most `cap` a day
  let rep = repairTotal;
  workDays.forEach((d, i) => { const share = Math.min(st.repair.cap || 20, Math.ceil(rep / (workDays.length - i)), room[d]); if (share > 0) { cells.repair[d] = share; room[d] -= share; rep -= share; } });
  overflow.repair = Math.max(0, rep);
  // 2. pinned cells
  for (const s of subs) for (const d of future) {
    const pin = st.pins[s.id + '|' + d];
    if (pin == null) continue;
    const v = Math.max(0, Math.min(pin, left[s.id], room[d])); cells[s.id][d] = v; room[d] -= v; left[s.id] -= v;
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
  const cards = repairTotal + subs.reduce((t, s) => t + s.keys.length - subjectDone(s, t0), 0);
  const roomAll = future.reduce((t, d) => t + capOf(d), 0);
  return { days, td, cap: capOf, cells, actual, overflow, over, total, done, effPace, needPace, raised: effPace > st.pace, cards, room: roomAll,
    spare: Math.max(0, roomAll - cards), repairTotal, todayPlan: days.includes(td) ? total[td] || 0 : 0, active: days.includes(td), future };
}

/* ---------- today's cards, in plan order ---------- */
export function todayCards(st, r = compute(st)) {
  if (!r.active) return [];
  const td = r.td, out = [], seenK = new Set();
  const doneToday = id => r.actual[id][td] || 0;
  const add = c => { const k = c.deck + '|' + c.code; if (!seenK.has(k)) { seenK.add(k); out.push(c); } };
  againList().slice(0, Math.max(0, (r.cells.repair[td] || 0) - doneToday('repair'))).forEach(a => { const c = cardOf(a.deck + '|' + a.code); if (c) add(c); });
  for (const s of st.subjects) {
    let n = (r.cells[s.id][td] || 0) - doneToday(s.id);
    for (const k of s.keys) { if (n <= 0) break; if (walkedAfter(k, s.addedAt) != null) continue; const c = cardOf(k); if (c) { add(c); n--; } }
  }
  return out;
}
export function todayParts(st, r = compute(st)) {
  if (!r.active) return [];
  const td = r.td, parts = [];
  if (r.cells.repair[td]) parts.push({ name: 'Repair', n: r.cells.repair[td], done: r.actual.repair[td] || 0 });
  for (const s of st.subjects) if (r.cells[s.id][td]) parts.push({ name: s.name, n: r.cells[s.id][td], done: r.actual[s.id][td] || 0 });
  return parts;
}
