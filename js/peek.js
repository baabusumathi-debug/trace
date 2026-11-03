// Test-only preview: Naven's peak week before INI-SS (17–23 Oct, from the War Map Log) laid onto the last 7 days,
// so the Loft can be seen with real-shaped data. Study times are real Log start times and minutes; break reasons are
// assumed from the gaps. Nothing is saved; it only changes what the Loft draws while the switch is on.
import { PEAK } from './peakdata.js';
import { CHANNEL } from './config.js';

const KEY = 'trace-test.peekPeak';
const DAY = 864e5;
const SRC_END = '2026-10-23';
let cache = null;

export function peekOn() {
  if (CHANNEL !== 'test') return false;
  if (!/^#\/loft/.test(location.hash)) return false;
  try { return localStorage.getItem(KEY) === '1'; } catch (e) { return false; }
}
export function setPeek(on) { try { localStorage.setItem(KEY, on ? '1' : '0'); } catch (e) { /* private mode */ } cache = null; }
export const PEAK_LABEL = '17–23 Oct, the week before INI';

const dkey = t => { const d = new Date(t); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); };

function build() {
  const td = dkey(Date.now());
  const shift = Math.round((new Date(td + 'T12:00:00') - new Date(SRC_END + 'T12:00:00')) / DAY);
  const at = (mmdd, hm) => {                      // real date + time, moved forward by `shift` days
    const d = new Date('2026-' + mmdd + 'T' + hm.padStart(5, '0') + ':00');
    d.setDate(d.getDate() + shift); return d.getTime();
  };
  const events = [], sessions = {};
  for (const [mmdd, hm, deck, a, b, min] of PEAK) {
    const s = at(mmdd, hm), n = b - a + 1, per = min * 60000 / n;
    for (let i = 0; i < n; i++) events.push({ id: 'pk' + events.length, kind: 'view', deck, no: a + i, ts: Math.round(s + per * (i + 1)), ms: Math.round(per), first: true, peek: true });
    const day = dkey(s); (sessions[day] = sessions[day] || []).push([s, s + min * 60000]);
  }
  events.sort((x, y) => x.ts - y.ts);
  // assumed breaks: the gaps between sessions inside 9:30–21:30, named by the time they began
  const breaks = {};
  for (const [day, ss] of Object.entries(sessions)) {
    ss.sort((x, y) => x[0] - y[0]);
    const w0 = new Date(day + 'T09:30:00').getTime(), w1 = new Date(day + 'T21:30:00').getTime();
    const used = new Set(), out = [];
    const name = (s, len) => {
      const h = new Date(s).getHours() + new Date(s).getMinutes() / 60, m = len / 60000;
      const once = k => (used.has(k) ? null : (used.add(k), k));
      if (s <= w0 + 60000 && m >= 20) return once('breakfast') || 'rest';
      if (h >= 12.5 && h < 15.5 && m >= 25) return once('lunch') || 'rest';
      if (h >= 16 && h < 18 && m >= 15) return once('eveningtea') || 'tea';
      if (h >= 19 && h < 21.5 && m >= 25) return once('dinner') || 'rest';
      if (m < 8) return 'restroom';
      if (m <= 20) return 'tea';
      return 'rest';
    };
    let prev = w0;
    for (const [s, e] of ss) {
      const gs = Math.max(prev, w0), ge = Math.min(s, w1);
      if (ge - gs >= 5 * 60000) {
        // assumed: a meal or tea took up to twice its allowance, a rest up to 30 min; the rest of a long gap stays unexplained
        const reason = name(gs, ge - gs), allowed = { breakfast: 30, lunch: 30, dinner: 30, eveningtea: 30, tea: 15 }[reason] || 0;
        const cap = (allowed ? allowed * 2 : reason === 'rest' ? 30 : 10) * 60000, len = Math.min(ge - gs, cap);
        const st = reason === 'breakfast' ? ge - len : gs;            // breakfast sits just before the first session
        out.push({ reason, start: st, end: st + len, allowed, peek: true });
      }
      prev = Math.max(prev, e);
    }
    breaks[day] = out;
  }
  return { events, breaks, td };
}
function data() { if (!cache || cache.td !== dkey(Date.now())) cache = build(); return cache; }
export const peekViews = () => data().events;
export const peekBreaks = day => data().breaks[day] || [];
