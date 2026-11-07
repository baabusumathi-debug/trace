// Narrated lessons (T-102; spec: docs/Trace_Lesson_Spec_7Nov.md). A viva question has an opening lesson, a micro-lesson per
// card and a closing lesson, written by the content chat in the package file. Each paragraph is cut at its [[takeaways]]
// into runs; each run is one clip (takeaways get the slower, stressed style). The Lesson tab shows the full text and lights
// the word being spoken, using word timings from Whisper saved beside each clip (approximate timings when there are none).
import { db } from './db.js';
import { call, batch } from './api.js';
import { pkgOf, qOf } from './viva.js';
import { VOICE, hash, speakable, deckIndex, hasClip, play, stop, nowPart, clipTime, clipDur, seekPart, pause, resume, isPaused, skip, pos, total, seek, speed, setSpeed, nowPlaying } from './voice.js';

const LV = 'L1';                      // bump when the lesson style notes change, so lesson clips are made again
export const LPROMPT = 'Speak as a calm, composed senior consultant teaching one aspirant. Neutral American English accent. Unhurried, measured pace. Enunciate every word and medical term clearly; say numbers and units in full. Pause briefly after each sentence.';
export const KPROMPT = LPROMPT + ' This line is a key takeaway. Say it a little slower, with a clear, natural stress on the important words, and a short pause after it. Do not exaggerate or sound dramatic.';
export const lessonDeck = pkg => 'VIVA-' + pkg;
const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ch]));
const md = s => esc(s).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');

/* ---------- where lessons are ---------- */
// slot: 'o' (open), 'c' (close), 's<j>' (step j of the question). "same" points to another question's lesson for this card.
export function lessonOf(pkg, qid, slot) {
  const q = qOf(pkg, qid); if (!q) return null;
  let L = slot === 'o' ? q.open : slot === 'c' ? q.close : (q.steps[+slot.slice(1)] || {}).lesson, owner = qid, oslot = slot;
  if (L && L.same) {
    const card = (q.steps[+slot.slice(1)] || {}).card, q2 = qOf(pkg, L.same), j = q2 ? q2.steps.findIndex(s => s.card === card) : -1;
    const L2 = j >= 0 ? q2.steps[j].lesson : null;
    if (!L2 || L2.same) return null;
    L = L2; owner = q2.q; oslot = 's' + j;
  }
  return L && L.text ? { L, pkg, q: owner, slot: oslot } : null;
}
export const hasLessons = pkg => { const P = pkgOf(pkg); return !!P && P.questions.some(q => q.open || q.close || q.steps.some(s => s.lesson)); };

/* ---------- a lesson → paragraphs → runs (clips) and words ---------- */
// [{ type: 'p', runs: [{ key, text, words, part }] } | { type: 'box', md } | { type: 'pic' }]
export function parse(x) {
  const out = [];
  for (const raw of String(x.L.text).split(/\n\s*\n/)) {
    const t = raw.trim(); if (!t) continue;
    if (t === '{{pic}}') { out.push({ type: 'pic' }); continue; }
    const bx = t.match(/^\{\{([\s\S]*)\}\}$/); if (bx) { out.push({ type: 'box', md: bx[1].trim() }); continue; }
    const runs = t.split(/(\[\[[\s\S]+?\]\])/).map(r => r.trim()).filter(Boolean).map(r => {
      const key = /^\[\[/.test(r), text = key ? r.slice(2, -2).trim() : r;
      return { key, text, words: text.split(/\s+/).filter(Boolean) };
    });
    out.push({ type: 'p', runs });
  }
  for (const p of out) for (const r of p.runs || []) {
    const t = speakable(r.text), h = hash(LV + '|' + VOICE + '|' + (r.key ? 'K' : 'N') + '|' + t);
    r.part = { k: `L-${x.q}-${x.slot}-${h}`.replace(/[^\w.\-]/g, '_'), t, h, key: r.key, prompt: r.key ? KPROMPT : LPROMPT, label: r.key ? 'Key' : '' };
  }
  return out;
}
export const partsOfLesson = paras => paras.flatMap(p => (p.runs || []).map(r => r.part));
const spokenLen = paras => partsOfLesson(paras).reduce((s, p) => s + p.t.length, 0);

/* ---------- word timings ---------- */
const norm = s => String(s).toLowerCase().replace(/[’']/g, '').replace(/[^a-z0-9]/g, '');
const tim = {};
async function whisperWords(deck, p) {
  const e = ((await deckIndex(deck)) || {})[p.k]; if (!e || !e.tid) return null;
  if (tim[e.tid]) return tim[e.tid];
  let t = await db.kv.get('vtim:' + e.tid);
  if (!t) { try { const r = await call({ op: 'readFile', id: e.tid }); t = JSON.parse(r.text); db.kv.set('vtim:' + e.tid, t).catch(() => {}); } catch (x) { return null; } }
  return (tim[e.tid] = t);
}
// starts[i] (seconds) for each display word of a run: Whisper's words matched to the script's words (longest common run),
// words Whisper heard differently placed between their matched neighbours by length
export function alignRun(words, W, dur) {
  const n = words.length, m = W.length, D = words.map(w => { const a = norm(w), b = norm(speakable(w)); return [a, b]; }), Wn = W.map(w => norm(w[0]));
  const eq = (i, j) => { const [a, b] = D[i], w = Wn[j]; if (!w) return false; return w === a || w === b || (w.length >= 4 && (a.startsWith(w) || w.startsWith(a) || b.startsWith(w))); };
  const L = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
  for (let i = n - 1; i >= 0; i--) for (let j = m - 1; j >= 0; j--) L[i][j] = eq(i, j) ? L[i + 1][j + 1] + 1 : Math.max(L[i + 1][j], L[i][j + 1]);
  const st = new Array(n).fill(null);
  for (let i = 0, j = 0; i < n && j < m;) { if (eq(i, j)) { st[i] = W[j][1] / 1000; i++; j++; } else if (L[i + 1][j] >= L[i][j + 1]) i++; else j++; }
  const end = dur || (m ? W[m - 1][2] / 1000 : 0);
  return fill(words, st, 0, end);
}
// approximate: spread the words over the clip by length, with a little extra after commas and full stops
export function approxRun(words, dur) { return fill(words, new Array(words.length).fill(null), 0, dur || words.length * 0.35); }
function fill(words, st, t0, t1) {
  const wt = words.map(w => w.length + 1 + (/[,;:]$/.test(w) ? 3 : /[.?!]$/.test(w) ? 6 : 0));
  const n = words.length;
  for (let i = 0; i < n;) {
    if (st[i] != null) { i++; continue; }
    let j = i; while (j < n && st[j] == null) j++;
    const a = i ? st[i - 1] : t0, b = j < n ? st[j] : t1, prevW = i ? wt[i - 1] : 0;
    const tot = wt.slice(i, j).reduce((s, x) => s + x, 0) + prevW;
    let acc = prevW; for (let k = i; k < j; k++) { st[k] = a + (b - a) * (i ? acc / tot : (acc - prevW) / Math.max(1, tot - prevW)); acc += wt[k]; }
    i = j;
  }
  return st;
}

/* ---------- making a package's lesson audio (bridge, small batches, with word timings) ---------- */
let making = '';
export const makingLessons = () => making;
export function allLessonParts(pkg) {
  const P = pkgOf(pkg); if (!P) return [];
  const seen = new Set(), out = [];
  for (const q of P.questions) for (const slot of ['o', ...q.steps.map((_, j) => 's' + j), 'c']) {
    const x = lessonOf(pkg, q.q, slot); if (!x) continue;
    for (const p of partsOfLesson(parse(x))) if (!seen.has(p.k)) { seen.add(p.k); out.push(p); }
  }
  return out;
}
export const estMin = parts => Math.round(parts.reduce((s, p) => s + p.t.length, 0) / 14 / 60);   // about 14 spoken characters a second
export async function makeLessons(pkg, onStep, onlyQ) {
  if (making) return { error: 'already making ' + making };
  making = pkg;
  const deck = lessonDeck(pkg);
  try {
    await deckIndex(deck, true);
    let want = allLessonParts(pkg).filter(p => !hasClip(deck, p));
    if (onlyQ) want = want.filter(p => p.k.startsWith('L-' + onlyQ + '-'));
    let done = 0, failed = 0, lastErr = '';
    onStep && onStep({ done, total: want.length, failed });
    for (let i = 0; i < want.length;) {
      const pr = want[i].prompt, part = [];
      while (i < want.length && part.length < 5 && want[i].prompt === pr) part.push(want[i++]);
      let r;
      try { const [x] = await batch([{ op: 'voice', deck, voice: VOICE, prompt: pr, align: true, items: part.map(p => ({ k: p.k, t: p.t, h: p.h })) }], 330000); if (!x.ok) throw new Error(x.error); r = x.data; }
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

/* ---------- the read-along ---------- */
const mmss = t => { t = Math.max(0, Math.round(t || 0)); return Math.floor(t / 60) + ':' + String(t % 60).padStart(2, '0'); };
// html for a lesson; mountLesson() wires it once it is in the page
export function lessonHtml(x, picHtml, extra) {
  const paras = parse(x); let pi = 0;
  const body = paras.map(p => {
    if (p.type === 'pic') return picHtml || '';
    if (p.type === 'box') return `<div class="ls-box"><small class="mono">ON SCREEN</small>${p.md.split('\n').map(l => /\|/.test(l) ? `<div class="ls-row">${l.split('|').map(c => c.trim()).filter(Boolean).map(c => `<span>${md(c)}</span>`).join('')}</div>` : `<div>${md(l)}</div>`).join('')}</div>`;
    const html = p.runs.map(r => { const ri = pi++; const ws = r.words.map((w, wi) => `<span class="lw" data-r="${ri}" data-w="${wi}">${esc(w)}</span>`).join(' '); return r.key ? `<b class="kp">${ws}</b>` : ws; }).join(' ');
    return `<p class="ls-p${p.runs.every(r => r.key) ? ' allkey' : ''}">${html}</p>`;
  }).join('');
  const top = !paras.some(p => p.type === 'pic') ? (picHtml || '') : '';
  return `<div class="lesson" data-lesson>
    <div class="ls-bar"><button class="ls-pp" data-lpp aria-label="Play">▶</button><button class="mono" data-lj="-10" aria-label="Back 10 seconds">−10</button><button class="mono" data-lj="-5" aria-label="Back 5 seconds">−5</button><button class="mono" data-lj="5" aria-label="Forward 5 seconds">+5</button><button class="mono" data-lj="10" aria-label="Forward 10 seconds">+10</button>${extra || ''}<span class="ls-spd mono"><button data-ls="-1" aria-label="Slower">−</button><b>${speed().toFixed(1)}×</b><button data-ls="1" aria-label="Faster">+</button></span>
      <input type="range" class="ls-seek" min="0" max="1000" value="0" aria-label="Position"><span class="ls-time mono"><span>0:00</span><span>${mmss(spokenLen(paras) / 14)}</span></span><span class="ls-msg mono"></span></div>
    <div class="ls-text">${top}${body}</div>
    <button class="ls-follow mono" data-lfollow hidden>↓ Follow the voice</button>
  </div>`;
}
// opts: { auto: start at once, onEnd: called when the lesson finishes on its own }
export function mountLesson(root, x, opts = {}) {
  const el = root.querySelector('[data-lesson]'); if (!el) return null;
  const deck = lessonDeck(x.pkg), paras = parse(x), runs = paras.flatMap(p => p.runs || []), parts = runs.map(r => r.part);
  const spans = runs.map((_, ri) => [...el.querySelectorAll(`.lw[data-r="${ri}"]`)]);
  const pp = el.querySelector('[data-lpp]'), rng = el.querySelector('.ls-seek'), tm = el.querySelector('.ls-time'), msg = el.querySelector('.ls-msg'), fol = el.querySelector('[data-lfollow]');
  ['pointerdown', 'click', 'touchstart', 'input', 'change', 'keydown'].forEach(t => el.addEventListener(t, e => e.stopPropagation()));
  const starts = new Map();        // run index → word starts (seconds)
  let follow = true, lit = null, raf = 0, drag = false, mine = false, ended = false;
  const timingsFor = async ri => {
    if (starts.has(ri)) return starts.get(ri);
    const W = await whisperWords(deck, parts[ri]);
    const s = W && W.words && W.words.length ? alignRun(runs[ri].words, W.words, (W.dur || 0) / 1000) : null;
    if (s) starts.set(ri, s);
    return s;
  };
  const playing = () => mine && !!nowPlaying() && parts.includes(nowPart());
  const light = sp => { if (lit === sp) return; if (lit) lit.classList.remove('on'); lit = sp; if (sp) { sp.classList.add('on'); if (follow) { const r = sp.getBoundingClientRect(), vh = innerHeight; if (r.top < vh * 0.25 || r.bottom > vh * 0.7) sp.scrollIntoView({ block: 'center', behavior: 'smooth' }); } } };
  const frame = () => {
    raf = 0;
    if (!el.isConnected) return;
    if (playing()) {
      const ri = parts.indexOf(nowPart()), t = clipTime();
      let s = starts.get(ri);
      if (!s) { timingsFor(ri); const d = clipDur(); s = d ? approxRun(runs[ri].words, d) : null; }
      if (s) { let w = 0; while (w + 1 < s.length && s[w + 1] <= t + 0.04) w++; light(spans[ri][w]); }
      const T = total(); if (!drag) rng.value = T ? Math.round(pos() / T * 1000) : 0;
      tm.firstChild.textContent = mmss(drag ? rng.value / 1000 * T : pos()); tm.lastChild.textContent = mmss(T);
    }
    pp.textContent = playing() && !isPaused() ? '❚❚' : '▶'; pp.setAttribute('aria-label', playing() && !isPaused() ? 'Pause' : 'Play');
    if (playing()) raf = requestAnimationFrame(frame);
  };
  const tick = () => { if (!raf) raf = requestAnimationFrame(frame); };
  const cb = k => { if (!k) { mine = false; light(null); if (!ended && opts.onEnd && !isPaused()) { ended = true; opts.onEnd(); } } tick(); };
  const start = async (ri, off) => {
    await deckIndex(deck);
    if (!parts.some(p => hasClip(deck, p))) { msg.textContent = 'no voice yet · make it on the Viva page'; return false; }
    ended = false; mine = true; follow = true; fol.hidden = true;
    const ok = await play(deck, parts, cb, ri != null ? parts[ri] : null, off);
    if (!ok) { mine = false; msg.textContent = 'no voice yet'; }
    parts.forEach((_, i) => timingsFor(i));
    tick(); return ok;
  };
  pp.onclick = () => { if (playing()) { if (isPaused()) { resume(); follow = true; fol.hidden = true; } else pause(); tick(); } else start(); };
  el.querySelectorAll('[data-lj]').forEach(b => b.onclick = () => { if (playing()) { skip(+b.dataset.lj); tick(); } });
  el.querySelectorAll('[data-ls]').forEach(b => b.onclick = () => { const v = Math.round(Math.min(2, Math.max(0.8, speed() + 0.1 * +b.dataset.ls)) * 10) / 10; setSpeed(v); el.querySelector('.ls-spd b').textContent = v.toFixed(1) + '×'; });
  rng.addEventListener('input', () => { drag = true; tick(); });
  rng.addEventListener('change', () => { if (playing()) seek(rng.value / 1000 * total()); drag = false; tick(); });
  fol.onclick = () => { follow = true; fol.hidden = true; if (lit) lit.scrollIntoView({ block: 'center', behavior: 'smooth' }); };
  // tap a word: jump there; tap a paragraph's empty space: its first word
  el.querySelector('.ls-text').addEventListener('click', async e => {
    if (e.target.closest('.ls-box, figure, a, button')) return;
    const w = e.target.closest('.lw'), p = e.target.closest('.ls-p');
    const sp = w || (p && p.querySelector('.lw')); if (!sp) return;
    const ri = +sp.dataset.r, wi = +sp.dataset.w;
    const s = await timingsFor(ri), off = s ? Math.max(0, s[wi] - 0.05) : 0;
    follow = true; fol.hidden = true;
    if (playing()) { seekPart(parts[ri], off); if (isPaused()) resume(); } else start(ri, off);
    light(spans[ri][wi]); tick();
  });
  // a hand scroll stops the auto-scroll; ▶ or "Follow the voice" brings it back
  const hand = () => { if (!el.isConnected) { ['wheel', 'touchmove'].forEach(t => document.removeEventListener(t, hand)); return; } if (playing() && follow) { follow = false; fol.hidden = false; } };
  ['wheel', 'touchmove'].forEach(t => document.addEventListener(t, hand, { passive: true }));
  deckIndex(deck).then(() => {
    if (!el.isConnected) return;
    const have = parts.filter(p => hasClip(deck, p)).length;
    if (!have) { msg.textContent = 'no voice yet · make it on the Viva page'; el.classList.add('novoice'); }
    else if (have < parts.length) msg.textContent = `${parts.length - have} of ${parts.length} pieces not made yet`;
    if (opts.auto && have) start();
  });
  return { start, stop };
}
