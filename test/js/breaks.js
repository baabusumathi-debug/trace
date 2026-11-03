// Breaks and time away: "Going out" before leaving, or "where were you?" after coming back. Kept on this device,
// per profile. Reminders at the end of a break go to the profile's own Google Calendar ("Trace" / "Trace · HT").
import { CHANNEL, IS_HT } from './config.js';
import { batch, hasBackend, isDemo } from './api.js';
import { dkey } from './store.js';

const PK = (CHANNEL === 'test' ? 'trace-test.' : 'trace.') + (IS_HT ? 'ht.' : '');
const get = (k, d) => { try { const v = localStorage.getItem(PK + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } };
const set = (k, v) => { try { localStorage.setItem(PK + k, JSON.stringify(v)); } catch (e) { /* private mode */ } };

// minutes allowed (0 = not timed, only counted); remind = calendar nudge after that many minutes
export const REASONS = [
  ['breakfast', 'Breakfast', 30], ['lunch', 'Lunch', 30], ['dinner', 'Dinner', 30],
  ['eveningtea', 'Evening tea (4–6 pm)', 30], ['tea', 'Tea', 15],
  ['restroom', 'Restroom', 0], ['rest', 'Rest', 0, 20], ['duty', 'Duty / ward', 0], ['phone', 'Phone / distraction', 0], ['other', 'Other', 0]
];
export const reasonOf = k => REASONS.find(r => r[0] === k) || [k, k, 0];
export const MEALS = ['breakfast', 'lunch', 'dinner'], TEAS = ['eveningtea', 'tea'];
export const AWAY_MIN = 5;           // minutes away before "where were you?"

export const current = () => get('onBreak', null);
export function breaksOn(day) { return (get('breaks', {})[day] || []); }
function save(rec) {
  const all = get('breaks', {}), d = dkey(rec.start);
  (all[d] = all[d] || []).push(rec);
  const keep = Object.keys(all).sort().slice(-45); const out = {}; keep.forEach(k => out[k] = all[k]);
  set('breaks', out);
}
const who = () => IS_HT ? 'HT' : 'Trace';
const calOk = () => hasBackend() && !isDemo();

export async function startBreak(reason) {
  if (current()) return current();
  const [k, label, allowed, remind] = reasonOf(reason), start = Date.now();
  const rec = { id: 'b' + start.toString(36), reason: k, start, allowed: allowed || 0, cal: null };
  set('onBreak', rec);
  const mins = allowed || remind || 0;
  if (mins && calOk()) {
    try {
      const [r] = await batch([{ op: 'calendar', action: 'add', who: who(), at: new Date(start + mins * 60000).toISOString(), title: `${label} ${allowed ? 'ends' : 'reminder'} · back to Trace`, note: 'Set by Trace when you went out.' }]);
      if (r && r.ok) { rec.cal = r.data.id; set('onBreak', rec); }
    } catch (e) { /* offline: the in-app timer still runs */ }
  }
  return rec;
}
export async function endBreak() {
  const rec = current(); if (!rec) return null;
  rec.end = Date.now(); set('onBreak', null); save(rec);
  if (rec.cal && calOk() && rec.end < rec.start + Math.max(rec.allowed, 20) * 60000) {
    try { await batch([{ op: 'calendar', action: 'remove', who: who(), id: rec.cal }]); } catch (e) { /* the reminder just rings */ }
  }
  return rec;
}
export function logAway(reason, start, end) { const rec = { id: 'a' + start.toString(36), reason, start, end, allowed: reasonOf(reason)[2] || 0, away: true }; save(rec); return rec; }

// leaving and coming back (tab hidden / app in the background)
export const hiddenAt = () => get('hiddenAt', null);
export const markHidden = t => set('hiddenAt', t);
export const pendingAway = () => get('pendingAway', null);     // an away gap the person chose to leave open ("just checking")
export const setPendingAway = v => set('pendingAway', v);
