// Mounts Trace's ink engine (../../js/ink.js, the same file the app uses) on any element:
// a study screen or a note page. One toolbar serves them all; the last surface written on owns undo.
import { Surface, Toolbar, attachPointer, settings, INK_ICONS, placeFloat, dragFloat, railSize, shiftObj, scaleObj, objBox } from '../../js/ink.js';

// The clipboard is Trace's own (same key, same shape), so a cut on a study page pastes in the card app and back.
const CLIP_KEY = 'trace.ink.clips', CLIP_MAX = 12;
let pasting = null;                           // id of the clipboard item waiting to be placed
function readClips() { try { const a = JSON.parse(localStorage.getItem(CLIP_KEY) || 'null'); return Array.isArray(a) ? a : []; } catch (e) { return []; } }
function saveClips(a) { try { localStorage.setItem(CLIP_KEY, JSON.stringify(a.slice(0, CLIP_MAX))); } catch (e) { /* full */ } }
function writeClip(c) { const a = readClips(); a.unshift({ id: 'c' + c.ts + Math.random().toString(36).slice(2, 5), ...c }); saveClips(a); }
function copySel(s) {
  const objs = s.sel.ids.filter(i => s.objs[i]).map(i => JSON.parse(JSON.stringify(s.objs[i])));
  if (!objs.length) return 0;
  const bb = objs.map(objBox).reduce((a, b) => [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[2], b[2]), Math.max(a[3], b[3])]);
  const f = 1 / s.unitPerPx();                // stored in screen pixels, as the app does
  objs.forEach(o => { delete o.a; delete o.hidden; shiftObj(o, -bb[0], -bb[1]); scaleObj(o, f); });
  writeClip({ n: objs.length, objs, ts: Date.now() });
  return objs.length;
}
function pasteInto(h, p) {
  const c = readClips().find(x => x.id === pasting) || readClips()[0]; if (!c) return;
  const s = h.s; s.snapshot();
  const f = s.unitPerPx(), start = s.objs.length;
  for (const src of c.objs) { const o = JSON.parse(JSON.stringify(src)); scaleObj(o, f); shiftObj(o, p[0], p[1]); delete o.a; s.objs.push(o); }
  s.sel = { ids: c.objs.map((_, j) => start + j) };
  pasting = null; last = h;
  settings().tool = 'lasso';
  s.render(); fire(h);
  if (bar) { bar.clipOpen = false; bar.draw(); }
  toast('Pasted · drag it where you want');
}
addEventListener('storage', e => { if (e.key === CLIP_KEY && bar) bar.draw(); });

// one quiet line at the foot of the screen, gone in a few seconds
let toastEl = null, toastT = 0;
export function toast(text) {
  if (!toastEl) { toastEl = document.createElement('div'); toastEl.className = 'dk-toast'; document.body.appendChild(toastEl); }
  toastEl.textContent = text; toastEl.classList.add('on');
  clearTimeout(toastT); toastT = setTimeout(() => toastEl.classList.remove('on'), 3200);
}

let writing = false, host = null, bar = null, last = null;
const surfaces = new Set();
const watchers = new Set();
export const isWriting = () => writing;
export const onWriting = fn => { watchers.add(fn); fn(writing); };

export function mountInk(el, opts) {
  const cv = document.createElement('canvas');
  cv.className = 'ink-ov';
  if (getComputedStyle(el).position === 'static') el.style.position = 'relative';
  el.appendChild(cv);
  const map = () => ({ X: p => p[0], Y: p => p[1], k: 1 });
  const s = new Surface(cv, [], { map, changed: () => {}, limits: () => writing });
  s.toUnits = (x, y) => { const r = cv.getBoundingClientRect(), sc = cv.clientWidth / (r.width || 1); return [(x - r.left) * sc, (y - r.top) * sc]; };
  s.unitPerPx = () => { const r = cv.getBoundingClientRect(); return cv.clientWidth / (r.width || 1); };
  const h = {
    el, cv, s, opts,
    size() {
      const w = opts.width ? opts.width() : el.clientWidth;
      const ht = opts.height ? opts.height() : Math.max(el.scrollHeight, el.clientHeight);
      cv.style.width = w + 'px'; cv.style.height = ht + 'px'; s.render();
    },
    load(objs) { s.objs.splice(0, s.objs.length, ...(objs || [])); s.undo.length = 0; s.redo.length = 0; s.sel = null; s.render(); },
    objs: () => s.objs,
    destroy() { surfaces.delete(h); if (last === h) last = null; cv.remove(); }
  };
  attachPointer(s, {
    writing: () => writing,
    toUnits: s.toUnits, unitPerPx: s.unitPerPx, map: () => s.o.map(),
    scrollBy: dy => { const p = opts.scroller && opts.scroller(); if (p) p.scrollTop += dy; else window.scrollBy(0, dy); },
    selChanged: () => { if (last && last !== h && last.s.sel) { last.s.sel = null; last.s.render(); } last = h; if (bar) bar.draw(); },
    onDown: () => { last = h; if (bar) bar.closePop(); },
    pasting: () => !!pasting, pasteAt: p => pasteInto(h, p), clips: () => [],
    changed: () => { last = h; if (opts.changed) opts.changed(); },
    grew: () => { if (opts.grew) opts.grew(); }
  });
  // the page must not scroll while the pen is down (the side button reports as a mouse on the Tab)
  ['pointerdown', 'pointermove'].forEach(t => cv.addEventListener(t, e => {
    if (writing && (e.pointerType === 'pen' || e.pointerType === 'mouse')) e.preventDefault();
  }, { passive: false }));
  // a finger still works the page while the pen is writing: a short tap goes through to whatever is under it
  let tap = null;
  cv.addEventListener('pointerdown', e => { if (e.pointerType === 'touch') tap = { x: e.clientX, y: e.clientY, t: Date.now() }; }, true);
  cv.addEventListener('pointerup', e => {
    if (e.pointerType !== 'touch' || !tap) return;
    const moved = Math.hypot(e.clientX - tap.x, e.clientY - tap.y), held = Date.now() - tap.t; tap = null;
    if (moved > 9 || held > 420) return;
    const was = cv.style.pointerEvents; cv.style.pointerEvents = 'none';
    const under = document.elementFromPoint(e.clientX, e.clientY);
    cv.style.pointerEvents = was;
    const hit = under && under.closest('button, a, [data-go], summary, input, label');
    if (hit) { e.preventDefault(); hit.click(); }
  }, true);
  surfaces.add(h); h.size();
  return h;
}

function apply() {
  document.body.classList.toggle('ink-on', writing);
  surfaces.forEach(h => h.cv.classList.toggle('on', writing));
  watchers.forEach(f => f(writing));
  if (!host) return;
  if (bar) { bar.destroy(); bar = null; }
  host.hidden = !writing && !host.dataset.fab;
  host.innerHTML = '';
  if (!writing) { host.hidden = true; return; }
  host.className = 'ik-host ik-float';
  const S = () => last || [...surfaces][0];
  bar = new Toolbar(host, {
    undo: () => { const h = S(); if (h) { h.s.doUndo(); fire(h); } },
    redo: () => { const h = S(); if (h) { h.s.doRedo(); fire(h); } },
    done: () => setWriting(false),
    clear: () => { const h = S(); if (!h) return; h.s.snapshot(); h.s.objs.splice(0); h.s.sel = null; h.s.render(); fire(h); },
    toolChanged: () => { pasting = null; surfaces.forEach(h => { h.s.sel = null; h.s.render(); }); },
    hasSel: () => { const h = S(); return !!(h && h.s.sel && h.s.sel.ids.length); },
    selOnExplain: () => false, canXfer: () => false, xferLabel: () => '',
    pin: null, docked: null,
    clips: () => readClips(), pasting: () => pasting, setPasting: v => { pasting = v || null; if (pasting) toast('Now tap with the pen where it should go'); },
    removeClip: id => { saveClips(readClips().filter(c => c.id !== id)); if (pasting === id) pasting = null; },
    clearClips: () => { saveClips([]); pasting = null; },
    selAction: (a, v) => {
      const h = S(); if (!h || !h.s.sel) return;
      const s = h.s, ids = s.sel.ids.filter(i => s.objs[i]);
      if (a === 'copy') { copySel(s); s.sel = null; s.render(); if (bar) bar.draw(); toast('Copied · open the clipboard in the pen bar, pick it, then tap where it goes'); return; }
      if (a === 'cut') copySel(s);
      if (a === 'del' || a === 'cut') { s.snapshot(); const set = new Set(ids); s.objs.splice(0, s.objs.length, ...s.objs.filter((o, i) => !set.has(i))); s.sel = null; }
      else if (a === 'colour') { s.snapshot(); for (const i of ids) s.objs[i].c = v; }
      else if (a === 'width') { s.snapshot(); for (const i of ids) { const o = s.objs[i]; if (o.type === 'hl' && o.snap) { o.h *= v; if (o.rects) o.rects = o.rects.map(r => [r[0], r[1], r[2], r[3] * v]); } else if (o.s) o.s = Math.max(0.3, o.s * v); } }
      else s.sel = null;
      s.render(); fire(h); if (bar) bar.draw();
      if (a === 'cut') toast('Cut · open the clipboard in the pen bar, pick it, then tap where it goes');
    }
  });
}
function fire(h) { if (h && h.opts && h.opts.changed) h.opts.changed(); }

export function setWriting(on) {
  writing = !!on; if (!writing) pasting = null;
  if (!writing) surfaces.forEach(h => { if (h.s.sel) { h.s.sel = null; h.s.render(); } });
  apply();
}
export function startInk() {
  host = document.createElement('div');
  host.className = 'ik-host ik-float'; host.hidden = true;
  document.body.appendChild(host);
  apply();
}
export const sizeAll = () => surfaces.forEach(h => h.size());
