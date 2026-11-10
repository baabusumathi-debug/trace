// Card voice (T-099): Gemini audio made by the bridge (backend/Voice.gs), one MP3 per point of a card, the same on every
// device. The app splits a card into points, turns each into speakable text (pronunciation list below), asks the bridge
// to make what is missing, and plays the clips at the chosen speed. Clips are kept on the device after the first play.
import { db } from './db.js';
import { IS_HT } from './config.js';
import { call, batch } from './api.js';
import { splitQ, plain } from './md.js';

export const VOICE = 'Iapetus';
export const PROMPT = 'Read this as a sharp, confident critical care consultant revising high-yield points with a resident. Neutral American English accent. Clear and well paced, every term enunciated, short pauses at full stops.';
// The style note above must never carry text to be spoken: Gemini sometimes reads it out. Pronunciation lives in SAY.
const PV = 'p3';                     // bump when PROMPT or the pronunciation list changes, so clips are made again (p3: American accent, 7 Nov)
export const voiceOn = () => !IS_HT;

/* ---------- pronunciation: symbols and abbreviations the voice would misread ---------- */
// [pattern, spoken]. Applied in order; word boundaries where it matters. Edit freely: a change remakes only the clips it touches.
const SAY = [
  [/cmH2O|cmH₂O|cm H2O|cm H₂O/g, 'centimetres of water'],
  [/mmHg/g, 'millimetres of mercury'],
  [/mL\/kg\/min/g, 'millilitres per kilogram per minute'], [/mL\/kg/g, 'millilitres per kilogram'], [/mL\/cmH2O/g, 'millilitres per centimetre of water'],
  [/µg\/kg\/h/g, 'micrograms per kilogram per hour'], [/µg\/kg\/min/g, 'micrograms per kilogram per minute'], [/mg\/kg\/h/g, 'milligrams per kilogram per hour'],
  [/mg\/kg/g, 'milligrams per kilogram'], [/\bmin\b/g, 'minutes'], [/\bPplat\b/g, 'P plat'], [/\bPIP\b/g, 'P I P'], [/\bPpeak\b/g, 'P peak'],
  [/mg\/dL/g, 'milligrams per decilitre'], [/mmol\/L/g, 'millimoles per litre'], [/J\/min/g, 'joules per minute'], [/L\/min/g, 'litres per minute'], [/L\/s\b/g, 'litres per second'],
  [/\bPEEP\b/g, 'peep'], [/\bARDS\b/g, 'A R D S'], [/\bPBW\b/g, 'predicted body weight'], [/\bP\/F\b/g, 'P to F ratio'], [/\bS\/F\b/g, 'S to F ratio'], [/\bI:E\b/g, 'I to E ratio'],
  [/FiO₂|FiO2/g, 'F I O 2'], [/SpO₂|SpO2/g, 'S P O 2'], [/PaO₂|PaO2/g, 'P A O 2'], [/PaCO₂|PaCO2/g, 'P A C O 2'], [/EtCO₂|EtCO2/g, 'end-tidal C O 2'], [/CO₂|CO2/g, 'C O 2'], [/O₂/g, 'oxygen'],
  [/\bΔP\b|ΔP/g, 'driving pressure'], [/\bVt\b|\bVT\b/g, 'tidal volume'], [/\bRR\b/g, 'respiratory rate'], [/\bHFNO\b|\bHFNC\b/g, 'high-flow nasal oxygen'],
  [/\bNIV\b/g, 'N I V'], [/\bSBT\b/g, 'S B T'], [/\bRSBI\b/g, 'R S B I'], [/\bVILI\b/g, 'villi'], [/\bP-SILI\b/g, 'P sili'], [/\bECMO\b/g, 'eck-mo'], [/\bVV-ECMO\b/g, 'V V eck-mo'],
  [/\bAPRV\b/g, 'A P R V'], [/\bNAVA\b/g, 'nava'], [/\bPAV\b/g, 'P A V'], [/\bICU\b/g, 'I C U'], [/\bARMA\b/g, 'arma'], [/\bPROSEVA\b/g, 'proseva'], [/\bEOLIA\b/g, 'eolia'],
  [/→|⟶|->/g, ', so '], [/≥/g, ' at least '], [/≤/g, ' at most '], [/>/g, ' more than '], [/</g, ' less than '], [/±/g, ' plus or minus '], [/\s\+\s|\s\+$/gm, ' plus '], [/\s=\s/g, ' equals '], [/×/g, ' times '], [/÷/g, ' divided by '],
  [/↑/g, ' rises '], [/↓/g, ' falls '], [/~/g, ' about '], [/≈/g, ' about '], [/°C/g, ' degrees Celsius'], [/%/g, ' percent'],
  [/(\d)\s*[–-]\s*(\d)/g, '$1 to $2'], [/([A-Za-z])[–−]([A-Za-z])/g, '$1 $2'], [/\s*—\s*/g, ', '], [/\s*[–−]\s*/g, ' minus '], [/\be\.g\./g, 'for example'], [/\bi\.e\./g, 'that is'], [/\bvs\.?\b/g, 'versus']
];
export function speakable(t) {
  let s = String(t || '')
    .replace(/\s*\*\*[a-h]\*\*\s*$/gm, '')                                // trailing part letters ("… **a**")
    .replace(/\*\*|__|`/g, '').replace(/(^|\s)\*([^*\n]+)\*/g, '$1$2')     // markdown
    .replace(/^\s*[-•]\s+/gm, '').replace(/^\s*\(?([a-h])\)?\s+/gm, '')     // list marks and part letters
    .replace(/\(standard teaching, not in your notes\)/g, '');
  for (const [re, w] of SAY) s = s.replace(re, w);
  return s.replace(/[ \t]+/g, ' ').replace(/\s+([,.;:])/g, '$1').replace(/([^.:;?!])\n+(?=[a-z(])/g, '$1 ').replace(/\n+/g, '. ').replace(/([:?!.;])\s*\./g, '$1').replace(/\s{2,}/g, ' ').trim();
}

/* ---------- a card → its points ---------- */
const endLetter = l => (String(l).match(/\*\*([a-h])\*\*\s*$/) || [])[1] || '';
const isTable = l => / \| /.test(l) && !/\|\s*\*\*[a-h]\*\*\s*$/.test(l), startsPart = l => /^\s*([-•]\s|\(?[a-h]\)?\s|\d+[.)]\s|\*\*[^*]+\*\*\s*$)/.test(l) || isTable(l);
const row = l => { const c = l.split('|').map(x => x.trim()).filter(Boolean); return c.length > 1 ? c[0] + ': ' + c.slice(1).join(', ') : c.join(''); };
// [{ k, label, t }]: k = part key used for the file name, label = what the ▶ chip shows, t = text to speak
export function partsOf(c, extra) {
  if (!c) return [];
  const out = [], code = String(c.code).replace(/[^\w.\-]/g, '_');
  const { head, rest } = splitQ(c.q || '');
  const qrest = String(rest || '').split('\n').map(l => { const m = l.match(/^(.*?)\s*\|\s*\*\*([a-h])\*\*\s*$/); return m ? m[1] : l; }).join('\n');
  out.push({ k: code + '.q', label: 'Q', t: [plain(head), qrest].filter(Boolean).join('\n') });
  const lines = String(c.a || '').split('\n'), groups = [];
  let inTable = false;
  for (const l of lines) {
    if (!l.trim()) { inTable = false; continue; }
    if (isTable(l)) { if (!inTable) { inTable = true; continue; } groups.push({ t: row(l), letter: '' }); continue; }   // first row of a table is its header
    inTable = false;
    const last = groups[groups.length - 1];
    if (!groups.length || startsPart(l) || (last && last.closed)) groups.push({ t: l, letter: (l.match(/^\s*\(?([a-h])\)?\s/) || [])[1] || endLetter(l), closed: !!endLetter(l) });
    else { last.t += '\n' + l; if (endLetter(l)) { last.letter = last.letter || endLetter(l); last.closed = true; } }
  }
  groups.forEach((g, i) => out.push({ k: code + '.a' + (i + 1), label: g.letter || String(i + 1), t: g.t }));
  if (c.why) out.push({ k: code + '.why', label: 'Why', t: c.why.replace(/^\s*\*\*WHY\*\*\s*/i, '') });
  if (c.watch) out.push({ k: code + '.watch', label: 'Watch', t: c.watch.replace(/^\s*\*\*WATCH\*\*\s*/i, '') });
  return out.concat(extra || []).map(p => ({ ...p, t: speakable(p.t) })).filter(p => p.t.length > 1);
}
export const hash = s => { let h = 5381; for (let i = 0; i < s.length; i++) h = (h * 33 + s.charCodeAt(i)) >>> 0; return h.toString(36); };
export const hOf = p => p.h || hash(PV + '|' + VOICE + '|' + p.t);   // lesson parts carry their own h

/* ---------- index of made clips, per deck ---------- */
const idx = {}, idxAsked = {};
export async function deckIndex(deck, fresh) {
  if (!idx[deck]) idx[deck] = (await db.kv.get('vidx:' + deck)) || {};
  if (fresh || !idxAsked[deck]) {
    idxAsked[deck] = 1;
    try { const r = await call({ op: 'voiceIndex', deck }); if (r && typeof r === 'object') { idx[deck] = r; await db.kv.set('vidx:' + deck, r); } } catch (e) { /* offline: keep the stored index */ }
  }
  return idx[deck];
}
// a clip counts when its text matches and it is in the main voice, or in an OpenAI stand-in voice ("oa-…", used when the
// Google voice limit is reached; remake those with redo keys later to bring them back to the main voice)
export const hasClip = (deck, p) => { const e = idx[deck] && idx[deck][p.k]; return !!(e && e.h === hOf(p) && (e.voice === VOICE || /^oa-/.test(e.voice || ''))); };

/* ---------- making a deck's audio (bridge, in small batches) ---------- */
let making = '';
export const makingDeck = () => making;
// cards = [{ c, extra }] (extra = the card's explanation points)
export async function makeDeck(deck, cards, onStep) {
  if (making) return { done: 0, total: 0, failed: 0, error: 'already making ' + making };
  making = deck;
  try {
  await deckIndex(deck, true);
  const want = cards.flatMap(x => partsOf(x.c, x.extra)).filter(p => !hasClip(deck, p));
  let done = 0, failed = 0, lastErr = '';
  onStep && onStep({ done, total: want.length, failed });
  for (let i = 0; i < want.length; i += 6) {
    const part = want.slice(i, i + 6);
    let r;
    try { const [x] = await batch([{ op: 'voice', deck, voice: VOICE, prompt: PROMPT, items: part.map(p => ({ k: p.k, t: p.t, h: hOf(p) })) }], 330000); if (!x.ok) throw new Error(x.error); r = x.data; }
    catch (e) { lastErr = e.message; failed += part.length; break; }
    done += r.made.length + r.skipped.length; failed += r.failed.length;
    if (r.failed.length) lastErr = r.failed[0].error;
    onStep && onStep({ done, total: want.length, failed, used: r.used, limit: r.limit });
    if (r.failed.some(f => /limit|40[13]/.test(f.error))) break;
  }
  await deckIndex(deck, true);
  return { done, total: want.length, failed, error: lastErr };
  } finally { making = ''; }
}

/* ---------- playback: one timeline over all the clips of a Listen (seek, skip, pause) ---------- */
const audio = typeof Audio !== 'undefined' ? new Audio() : null;
let queue = [], qi = -1, onState = null, playing = '', deckNow = '', urls = [], durs = [], paused = false, gen = 0, cutT = 0;
export const speed = () => { try { return Math.min(2, Math.max(0.8, +localStorage.getItem('trace.vspeed') || 1.2)); } catch (e) { return 1.2; } };
export function setSpeed(v) { try { localStorage.setItem('trace.vspeed', String(v)); } catch (e) { /* */ } if (audio) audio.playbackRate = v; }
async function blobOf(deck, p) {
  const e = idx[deck] && idx[deck][p.k]; if (!e) return null;
  let blob = await db.kv.get('vclip:' + e.id);
  if (!blob) {
    const r = await call({ op: 'readBinary', id: e.id });
    const bin = atob(r.b64), u = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; i++) u[i] = bin.charCodeAt(i);
    blob = new Blob([u], { type: 'audio/mpeg' });
    db.kv.set('vclip:' + e.id, blob).catch(() => {});
  }
  return blob;
}
async function urlAt(i, g) {
  if (urls[i] === undefined) {
    let b = null; try { b = await blobOf(deckNow, queue[i]); } catch (e) { b = null; }
    if (g !== gen) return null;
    urls[i] = b ? URL.createObjectURL(b) : null;
    if (urls[i]) { const m = new Audio(); m.preload = 'metadata'; m.onloadedmetadata = () => { if (isFinite(m.duration)) durs[i] = m.duration; }; m.src = urls[i]; }
  }
  return urls[i];
}
// clip length: the real one once known, else the bridge's estimate
const est = i => queue[i] && queue[i].cut && (durs[i] == null || queue[i].cut < durs[i]) ? queue[i].cut - (queue[i].from || 0) : durs[i] != null ? durs[i] - ((queue[i] && queue[i].from) || 0) : (((idx[deckNow] || {})[queue[i].k] || {}).sec || 5);
export const total = () => queue.reduce((s, _, i) => s + est(i), 0);
export function pos() { if (qi < 0) return 0; let s = 0; for (let i = 0; i < qi; i++) s += est(i); return s + Math.max(0, ((audio && audio.currentTime) || 0) - ((queue[qi] && queue[qi].from) || 0)); }
export const isPaused = () => paused;
const tell = () => onState && onState(playing);
function reset() { gen++; clearInterval(cutT); urls.forEach(u => u && URL.revokeObjectURL(u)); queue = []; urls = []; durs = []; qi = -1; playing = ''; paused = false; if (audio) { audio.onended = null; audio.pause(); audio.removeAttribute('src'); } }
export function stop() { const cb = onState; reset(); onState = null; cb && cb(''); }
export const nowPlaying = () => playing;
async function startAt(i, off, g) {
  if (g !== gen) return;
  if (i >= queue.length) { const cb = onState; reset(); onState = null; cb && cb(''); return; }
  qi = i;
  const url = await urlAt(i, g); if (g !== gen) return;
  if (!url) return startAt(i + 1, 0, g);
  playing = queue[i].k;
  audio.onended = () => setTimeout(() => startAt(i + 1, 0, g), 250);
  const at = Math.max(off || 0, queue[i].from || 0);   // a lesson clip may start past speech that is not in the script
  audio.onloadedmetadata = () => { if (isFinite(audio.duration)) { durs[i] = audio.duration; if (at) audio.currentTime = Math.min(at, Math.max(0, audio.duration - 0.05)); } };
  audio.src = url; audio.playbackRate = speed(); audio.preservesPitch = true;
  // a clip with a cut point (lessons: just after the script's last word) ends there, whatever follows in the file
  clearInterval(cutT);
  const p = queue[i];
  if (p.cut) cutT = setInterval(() => { if (g !== gen || qi !== i) return clearInterval(cutT); if (audio.currentTime >= p.cut) { clearInterval(cutT); audio.pause(); const f = audio.onended; audio.onended = null; f && f(); } }, 50);
  tell();
  if (!paused) await audio.play().catch(() => {});
}
// play these points in order; cb(key) is told which point is playing ('' when done or stopped)
export async function play(deck, parts, cb, from, off) {
  stop();
  queue = parts.filter(p => hasClip(deck, p)); deckNow = deck;
  if (!queue.length) return false;
  onState = cb; const g = gen;
  await startAt(Math.max(0, from ? queue.indexOf(from) : 0), off || 0, g);
  preload(g);
  return true;
}
// fetch the rest so the timeline knows its full length
function preload(g) { (async () => { for (let i = 0; i < queue.length && g === gen; i++) await urlAt(i, g); })(); }
// jump to second t of the whole Listen
export function seek(t) {
  if (!queue.length) return;
  t = Math.max(0, Math.min(t, total() - 0.1));
  let i = 0, s = 0;
  while (i < queue.length - 1 && s + est(i) <= t) { s += est(i); i++; }
  const off = t - s + ((queue[i] && queue[i].from) || 0);
  if (i === qi && audio.src && audio.readyState >= 1) { audio.currentTime = off; if (!paused) audio.play().catch(() => {}); tell(); }
  else { gen++; const g = gen; startAt(i, off, g); preload(g); }
}
export const skip = d => seek(pos() + d);
// the part playing now and the second inside its clip (read-along); jump to a part (object from the list given to play)
export const nowPart = () => (qi >= 0 && queue[qi]) || null;
export const clipTime = () => (audio && audio.currentTime) || 0;
export const clipDur = () => (audio && isFinite(audio.duration) ? audio.duration : 0);
export function seekPart(p, off) {
  const i = queue.indexOf(p); if (i < 0) return false;
  if (i === qi && audio.src && audio.readyState >= 1) { audio.currentTime = off || 0; if (!paused) audio.play().catch(() => {}); tell(); return true; }
  gen++; const g = gen; startAt(i, off || 0, g); preload(g); return true;
}
export const playingList = () => queue;
// phone lock screen: play / pause and ±10 s (lessons are listened to with the eyes closed)
if (typeof navigator !== 'undefined' && navigator.mediaSession) {
  try {
    navigator.mediaSession.setActionHandler('play', () => resume());
    navigator.mediaSession.setActionHandler('pause', () => pause());
    navigator.mediaSession.setActionHandler('seekbackward', () => skip(-10));
    navigator.mediaSession.setActionHandler('seekforward', () => skip(10));
    navigator.mediaSession.setActionHandler('stop', () => stop());
  } catch (e) { /* not supported */ }
}
export function pause() { if (!queue.length) return; paused = true; audio.pause(); tell(); }
export function resume() { if (!queue.length) return; paused = false; audio.play().catch(() => {}); tell(); }
