// Loft numbers: Phase 1 chase, cards per day, study time, best hours, GT trend. Pure calculations, no screens.
import { S, seen, off, cardsOf, inPool, today, dkey, walked, missOf } from './store.js';
import { peekOn, peekViews } from './peek.js';

export const PHASE1_END = '2026-11-30';
export const PHASE1_START = '2026-11-01';
export const WIN_START = '09:30', WIN_END = '21:30';
export const STUDY_GOAL_H = 8;
const DAY = 864e5;
export const winStart = d => new Date(d + 'T' + WIN_START + ':00').getTime();
export const winEnd = d => new Date(d + 'T' + WIN_END + ':00').getTime();
export const addDays = (d, n) => dkey(new Date(d + 'T12:00:00').getTime() + n * DAY);
export const daysBetween = (a, b) => Math.round((new Date(b + 'T12:00:00') - new Date(a + 'T12:00:00')) / DAY);

function views() {
  if (peekOn()) return peekViews().map(e => ({ ...e, no: e.no - off(e.deck) }));
  return S.events.filter(e => e.kind === 'view' && !S.undone.has(e.id)).sort((a, b) => a.ts - b.ts);
}

// When each card was first walked: War Map flow rows (recent, with dates) and Trace views. Cards walked only in old
// War Map history without a date count as walked before the chase began (ts 0).
function firstWalks() {
  const first = new Map();
  for (const r of S.logChron || []) {
    const [day, time, deck, a, b] = r, o = off(deck), ts = Date.parse(day + 'T' + (/^\d{1,2}:\d{2}/.test(time || '') ? String(time).padStart(5, '0') : '12:00') + ':00') || 0;
    for (let n = a; n <= b; n++) { const k = deck + '|' + (n - o); if (!first.has(k) || first.get(k) > ts) first.set(k, ts); }
  }
  for (const e of views()) { const k = e.deck + '|' + e.no; if (!first.has(k) || first.get(k) > e.ts) first.set(k, e.ts); }
  return first;
}

/** Phase 1 chase for a pool: every card walked at least once by 30 Nov. */
export function chase(pool) {
  const first = firstWalks(), td = today(), dates = [];
  let total = 0, walkedNow = 0;
  const pk = peekOn() ? new Set(views().map(e => e.deck + '|' + e.no)) : null;
  for (const d of (S.library ? S.library.decks : [])) {
    const cs = cardsOf(d.deck);
    if (!cs.length) {
      if (!pool || pool === 'all') {
        const pkHere = pk ? [...pk].filter(k => k.startsWith(d.deck + '|')).length : 0, w = Math.max(0, walked(d.deck) - pkHere);
        total += d.cards; walkedNow += w; for (let i = 0; i < w; i++) dates.push(0);
      }
      continue;
    }
    for (const c of cs) {
      if (!inPool(c, pool)) continue;
      total++;
      if (pk && pk.has(c.deck + '|' + c.no)) continue;            // preview: counted below at the peak-week time
      if (seen(c.deck, c.no) > 0) { walkedNow++; const t = first.get(c.deck + '|' + c.no); dates.push(t == null ? 0 : t); }
    }
  }
  if (peekOn()) {                                 // test preview: the peak week's cards count as newly walked
    const done = new Set();
    for (const e of views()) {
      const k = e.deck + '|' + e.no; if (done.has(k)) continue; done.add(k);
      const card = cardsOf(e.deck).find(c => c.no === e.no);
      const deckIn = (S.library ? S.library.decks : []).some(d => d.deck === e.deck);
      if (card ? inPool(card, pool) : deckIn && (!pool || pool === 'all')) { dates.push(e.ts); walkedNow++; }
    }
    walkedNow = Math.min(walkedNow, total);
  }
  const by = day => dates.filter(t => t < winEnd(day) + 3 * 3600e3).length;     // walked by the end of that day (to midnight)
  const startDay = PHASE1_START, nDays = daysBetween(startDay, PHASE1_END) + 1;
  const series = [];
  for (let i = 0; i < nDays; i++) { const day = addDays(startDay, i); if (day > td) break; series.push({ day, walked: by(day) }); }
  const daysLeft = Math.max(1, daysBetween(td, PHASE1_END) + 1);
  const atStartToday = dates.filter(t => t < new Date(td + 'T00:00:00').getTime()).length;
  const doneToday = walkedNow - atStartToday;
  const requiredToday = Math.ceil(Math.max(0, total - atStartToday) / daysLeft);
  const required = Math.ceil(Math.max(0, total - walkedNow) / daysLeft);
  const sevenAgo = dates.filter(t => t < new Date(addDays(td, -6) + 'T00:00:00').getTime()).length;
  const rate = Math.round((walkedNow - sevenAgo) / 7 * 10) / 10;
  const left = Math.max(0, total - walkedNow);
  const finish = left === 0 ? td : rate > 0 ? addDays(td, Math.ceil(left / rate)) : null;
  const late = finish ? daysBetween(PHASE1_END, finish) : null;
  // weekly blocks from 1 Nov with the pace each one needed (from the position at the start of Phase 1)
  const atStart = dates.filter(t => t < new Date(startDay + 'T00:00:00').getTime()).length;
  const perDay0 = (total - atStart) / nDays, weeks = [];
  for (let w = 0; w * 7 < nDays; w++) {
    const a = addDays(startDay, w * 7), b = addDays(startDay, Math.min(nDays - 1, w * 7 + 6));
    const from = new Date(a + 'T00:00:00').getTime(), to = new Date(b + 'T00:00:00').getTime() + DAY;
    weeks.push({ a, b, done: dates.filter(t => t >= from && t < to).length, need: Math.round(perDay0 * (daysBetween(a, b) + 1)), future: a > td });
  }
  return { total, walkedNow, left, daysLeft, required, requiredToday, doneToday, rate, finish, late, series, weeks, startDay, nDays };
}

/** Live pace inside today's window: where you should be by now, and the hourly rate needed from here. */
export function livePace(c, now = Date.now()) {
  const td = today(), a = winStart(td), b = winEnd(td);
  const f = Math.min(1, Math.max(0, (now - a) / (b - a)));
  const should = Math.round(c.requiredToday * f), diff = c.doneToday - should;
  const hoursLeft = Math.max(0, (b - now) / 3600e3);
  const perHour = hoursLeft > 0.1 ? Math.ceil(Math.max(0, c.requiredToday - c.doneToday) / hoursLeft) : null;
  return { should, diff, hoursLeft, perHour, before: now < a, after: now >= b };
}

/** Cards per day, split: new (first walk) · ×2 · ×3+ · repairs; plus War Map flow cards without a split. */
export function cardsPerDay(n) {
  const td = today(), days = [];
  for (let i = n - 1; i >= 0; i--) days.push(addDays(td, -i));
  const want = new Set(days), out = Object.fromEntries(days.map(d => [d, { day: d, new: 0, x2: 0, x3: 0, repair: 0, wm: 0 }]));
  const count = new Map(), lastAgain = new Map(), done = new Set();
  for (const e of views()) {
    const k = e.deck + '|' + e.no, prior = count.get(k) || 0;
    const base = (S.logBase[e.deck] || {})[e.no + off(e.deck)] || 0;
    const nth = base + prior + 1, d = dkey(e.ts), dk = d + '|' + k;
    if (want.has(d) && !done.has(dk)) {
      done.add(dk);
      const o = out[d];
      if (e.first) o.new++; else if (lastAgain.get(k)) o.repair++; else if (nth === 1) o.new++; else if (nth === 2) o.x2++; else o.x3++;
    }
    count.set(k, prior + 1); lastAgain.set(k, !!e.again);
  }
  if (!peekOn()) for (const d of days) { const l = S.logDaily[d]; if (l) out[d].wm = l.cards || 0; }
  return days.map(d => out[d]);
}

/** Study intervals from card views (each view covers its own time, at most 20 min), merged when < 3 min apart. */
export function studyIntervals(day) {
  const a = new Date(day + 'T00:00:00').getTime(), b = a + DAY, iv = [];
  for (const e of views()) {
    if (e.ts < a || e.ts >= b) continue;
    const s = e.ts - Math.min(e.ms || 0, 20 * 60000);
    const last = iv[iv.length - 1];
    if (last && s - last[1] < 3 * 60000) last[1] = Math.max(last[1], e.ts); else iv.push([s, e.ts]);
  }
  return iv;
}
export const studyMs = day => studyIntervals(day).reduce((t, [s, e]) => t + (e - s), 0) + (peekOn() ? 0 : ((S.logDaily[day] || {}).min || 0) * 60000);

/** Cards per hour of the window, averaged over the days with study in the last 14. */
export function bestHours() {
  const td = today(), slots = new Array(12).fill(0); let active = 0;
  const vs = views();
  for (let i = 0; i < 14; i++) {
    const d = addDays(td, -i), a = winStart(d); let any = false;
    for (const e of vs) { if (dkey(e.ts) !== d) continue; const k = Math.floor((e.ts - a) / 3600e3); if (k >= 0 && k < 12) { slots[k]++; any = true; } }
    if (any) active++;
  }
  return slots.map(v => active ? Math.round(v / active * 10) / 10 : 0);
}

/** GT net % per paper for this profile (NEET marking: +4 right, −1 wrong). */
export function gtTrend() {
  return Object.values(S.gtScores || {}).filter(g => g.total).map(g => ({ ...g, pct: Math.round((4 * g.right - g.wrong) / (4 * g.total) * 100) }))
    .sort((a, b) => String(a.date).localeCompare(String(b.date)));
}

/** Today's walks as beads for the Flow thread: 'n' new · 'x2' second walk · 'x3' third or later · 'r' repair. */
export function todayBeads() {
  const td = today(), count = new Map(), lastAgain = new Map(), out = [], seenToday = new Set();
  for (const e of views()) {
    const k = e.deck + '|' + e.no, prior = count.get(k) || 0, base = (S.logBase[e.deck] || {})[e.no + off(e.deck)] || 0;
    if (dkey(e.ts) === td && !seenToday.has(k)) {
      seenToday.add(k);
      const nth = base + prior + 1, c = cardsOf(e.deck).find(x => x.no === e.no);
      out.push(lastAgain.get(k) || (c && missOf(c)) ? 'r' : nth === 1 ? 'n' : nth === 2 ? 'x2' : 'x3');
    }
    count.set(k, prior + 1); lastAgain.set(k, !!e.again);
  }
  return out;
}
