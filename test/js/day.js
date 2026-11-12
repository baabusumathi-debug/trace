// T-141: the day plan — blocks of the day (study, break, rest, meal, out) and earned breaks.
// Meals and Out are fixed anchors. Breaks are earned while studying (1 min for every `ratio` min) and fall due at the
// end of a question, never in the middle of one; a break taken late moves the blocks after it, up to the next anchor.
// Kept on this device, per profile. Times are minutes from midnight.
import { CHANNEL, IS_HT } from './config.js';
import { today, dkey } from './store.js';
import { studyIntervals } from './loftx.js';
import { breaksOn, current as curBreak, MEALS } from './breaks.js';

const KEY = (CHANNEL === 'test' ? 'trace-test.' : 'trace.') + (IS_HT ? 'ht.' : '') + 'day';
export const TYPES = [['study', 'Study'], ['break', 'Break'], ['rest', 'Rest'], ['meal', 'Meal'], ['out', 'Out']];
export const FIXED = new Set(['meal', 'out']);
export const typeName = t => (TYPES.find(x => x[0] === t) || [t, t])[1];
const rid = () => Math.random().toString(36).slice(2, 8);

let D = null;
function load() {
  if (D) return D;
  try { D = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { D = null; }
  if (!D || typeof D !== 'object') D = {};
  D.days = D.days || {}; D.ratio = D.ratio || 5; D.size = D.size || 10; D.zoom = D.zoom || 15; D.gap = D.gap || 45;
  return D;
}
function save() {
  const d = load(), keep = Object.keys(d.days).sort().slice(-21), out = {}; keep.forEach(k => out[k] = d.days[k]); d.days = out;
  try { localStorage.setItem(KEY, JSON.stringify(d)); } catch (e) { /* private mode */ }
}
export const settingsDay = () => load();
export function setSetting(k, v) { load()[k] = v; save(); }
export const nowMin = (t = Date.now()) => { const d = new Date(t); return d.getHours() * 60 + d.getMinutes() + d.getSeconds() / 60; };
export const hm = m => { m = Math.round(m); const h = Math.floor(m / 60) % 24, mm = m % 60, hh = ((h + 11) % 12) + 1; return hh + ':' + String(mm).padStart(2, '0') + (h < 12 ? ' AM' : ' PM'); };
export const dur = m => { m = Math.max(0, Math.round(m)); const h = Math.floor(m / 60); return h ? h + 'h ' + String(m % 60).padStart(2, '0') + 'm' : m + ' min'; };

export function blocksOf(day = today()) { const d = load(); return (d.days[day] || []).slice().sort((a, b) => a.a - b.a); }
function put(day, list) { load().days[day] = list.sort((a, b) => a.a - b.a); save(); }
// a new block cuts into whatever it overlaps (the new one wins)
export function addBlock(day, { type, a, b, label }) {
  a = Math.max(0, Math.round(a)); b = Math.min(24 * 60, Math.round(b)); if (b <= a) return null;
  const out = [];
  for (const x of blocksOf(day)) {
    if (x.b <= a || x.a >= b) { out.push(x); continue; }
    if (x.a < a) out.push({ ...x, b: a });
    if (x.b > b) out.push({ ...x, id: x.a < a ? rid() : x.id, a: b });
  }
  const nb = { id: rid(), type, a, b, label: label || '' }; out.push(nb); put(day, out); return nb;
}
export function updateBlock(day, id, ch) {
  const list = blocksOf(day), x = list.find(y => y.id === id); if (!x) return;
  load().days[day] = list.filter(y => y.id !== id); save();
  const nb = addBlock(day, { ...x, ...ch }); if (nb) { nb.id = id; if (x.done) nb.done = true; put(day, blocksOf(day).map(y => y === nb ? nb : y)); }
}
export function removeBlock(day, id) { put(day, blocksOf(day).filter(x => x.id !== id)); }
export function clearDay(day) { put(day, []); }
// a rhythm fills the empty time between two times with study, breaks every `every` minutes
export function fillRhythm(day, from, to, every, brk) {
  const taken = blocksOf(day);
  let t = Math.max(from, 0);
  while (t < to) {
    const nextFixed = taken.filter(x => x.a >= t).reduce((m, x) => Math.min(m, x.a), to);
    const inside = taken.find(x => x.a <= t && x.b > t);
    if (inside) { t = inside.b; continue; }
    const end = Math.min(nextFixed, to);
    let s = t;
    while (s < end) {
      const se = Math.min(end, s + every); addBlock(day, { type: 'study', a: s, b: se }); s = se;
      if (s < end) { const be = Math.min(end, s + brk); addBlock(day, { type: 'break', a: s, b: be }); s = be; }
    }
    t = end;
  }
}

/* ---------- now: the block you are in, what comes next, how long this session runs ---------- */
export function nowInfo(t = Date.now()) {
  const day = dkey(t), m = nowMin(t), list = blocksOf(day);
  const cur = list.find(x => x.a <= m && x.b > m) || null;
  const next = list.find(x => x.a > m) || null;
  // the session: this study block and the study blocks joined to it (a break in between ends it)
  let end = null;
  if (cur && cur.type === 'study') { end = cur.b; for (const x of list) if (x.a === end && x.type === 'study') end = x.b; }
  const nextBreak = list.find(x => x.a >= m && !['study'].includes(x.type)) || null;
  return { day, m, list, cur, next, sessionEnd: end, left: end != null ? end - m : null, nextBreak };
}

/* ---------- earned breaks ---------- */
const BREAKY = r => !MEALS.includes(r) && r !== 'duty';
export function bank(t = Date.now()) {
  const day = dkey(t), s = load();
  const iv = studyIntervals(day), studied = iv.reduce((a, [x, y]) => a + (y - x), 0) / 60000;
  const brs = breaksOn(day).filter(b => BREAKY(b.reason)), taken = brs.reduce((a, b) => a + ((b.end || t) - b.start), 0) / 60000;
  const cb = curBreak(), onNow = cb && dkey(cb.start) === day && BREAKY(cb.reason) ? (t - cb.start) / 60000 : 0;
  const lastEnd = Math.max(0, ...breaksOn(day).map(b => b.end || 0), cb ? t : 0);
  const sinceIv = iv.filter(([x, y]) => y > lastEnd).reduce((a, [x, y]) => a + (y - Math.max(x, lastEnd)), 0) / 60000;
  return { studied, earned: studied / s.ratio, taken: taken + onNow, left: Math.max(0, studied / s.ratio - taken - onNow), since: sinceIv, ratio: s.ratio, size: s.size };
}
// is a break due now? a planned break has started, or enough is earned after a long stretch
let snoozeAt = 0;
export function snooze() { snoozeAt = Date.now(); }
export function breakDue(t = Date.now()) {
  if (curBreak()) return null;
  if (Date.now() - snoozeAt < 8 * 60000) return null;        // "one more question" holds it for a while
  const n = nowInfo(t), b = bank(t), s = load();
  if (n.cur && n.cur.type === 'break' && !n.cur.done) return { why: 'planned', mins: Math.round(n.cur.b - n.cur.a), block: n.cur, bank: b };
  if (n.cur && n.cur.type === 'study' && n.sessionEnd != null && n.left <= 0.5) return { why: 'end', mins: s.size, bank: b };
  if (b.left >= s.size && b.since >= s.gap) return { why: 'earned', mins: Math.min(30, Math.round(b.left)), bank: b };
  return null;
}
// a break starting now: a planned break that should have started earlier moves here, and the blocks after it
// (not meals or Out) move by the same amount, never past the next fixed block
export function onBreakStart(t = Date.now()) {
  const day = dkey(t), m = nowMin(t), list = blocksOf(day);
  const pb = list.find(x => x.type === 'break' && !x.done && x.a <= m && x.b > m - 60) || list.find(x => x.type === 'break' && !x.done && x.a > m && x.a - m < 20);
  if (!pb) return;
  const delta = Math.round(m - pb.a); pb.done = true;
  if (delta <= 0) { put(day, list); return; }
  const fixedNext = list.filter(x => FIXED.has(x.type) && x.a >= pb.a).reduce((mm, x) => Math.min(mm, x.a), 24 * 60);
  const study = list.find(x => x.type === 'study' && x.b === pb.a);
  for (const x of list) {
    if (x.a < pb.a || FIXED.has(x.type) || x.a >= fixedNext) continue;
    x.a = Math.min(fixedNext, x.a + delta); x.b = Math.min(fixedNext, x.b + delta);
  }
  if (study) study.b = pb.a;                         // the study before it ran on to now
  put(day, list.filter(x => x.b > x.a));
}
