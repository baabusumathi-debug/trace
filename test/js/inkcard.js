// Ink on a Flow card: the overlay (write anywhere on either side) and rooms that open under any line.
// The overlay is kept relative to the block it was written on (and highlights snapped to text keep their words),
// so it survives a narrower split-screen window, a bigger text size or a room opening above it.
import { Surface, Toolbar, attachPointer, loadInk, saveInk, settings, INK_ICONS, shiftObj, scaleObj, objBox, placeFloat, dragFloat, railSize } from './ink.js';

const ROOM_W = 1000;                       // rooms use their own units: 1000 = the room's width
const SPACE = 180;                         // one "space" of a room, in room units
const CLIP_KEY = 'trace.ink.clips', OLD_CLIP = 'trace.ink.clip', CLIP_MAX = 12;
let cur = null;
const ovs = st => [st.overlay, st.overlayX].filter(Boolean);            // the answer overlay and the Explain overlay (T-072)
const isOv = (st, s) => s === st.overlay || (st.overlayX && s === st.overlayX);                            // { card, face, rec, overlay, rooms:Map, toolbar, ... }
let writing = false, pasting = null;
// T-078: S Pen side button erases even when the pen tools are closed. The proven side-button signature (pen moves with
// buttons 1, pressure 0, no press) held 70 ms switches writing on quietly (no toolbar); 700 ms after the pen goes quiet it
// switches back off.
let quiet = false, lastPenEv = 0;
addEventListener('pointermove', e => { if (e.pointerType === 'pen') lastPenEv = Date.now(); }, true);
setInterval(() => { if (quiet && writing && Date.now() - lastPenEv > 700) { quiet = false; setWriting(false); } }, 250);
function quietWatch(el) {
  let t0 = null, downAt = 0;
  el.addEventListener('pointerdown', e => {
    if (e.pointerType !== 'pen') return;
    downAt = Date.now(); t0 = null;
    if (quiet && writing) { quiet = false; setWriting(false); e.stopPropagation(); e.preventDefault(); }   // a normal touch ends the quiet eraser; it never draws
  }, true);
  const f = e => {
    if (writing || e.pointerType !== 'pen') return;
    if ((e.buttons & 1) && !(e.pressure > 0) && Date.now() - downAt > 250) { if (!t0) t0 = Date.now(); else if (Date.now() - t0 > 70) { t0 = null; quiet = true; setWriting(true); } }
    else t0 = null;
  };
  el.addEventListener('pointermove', f); if ('onpointerrawupdate' in window) el.addEventListener('pointerrawupdate', f);
}          // pasting = id of the clipboard item waiting to be placed
const listeners = { changed: null };
export const isWriting = () => writing;

function anchorsOf(box) {
  const els = [...box.querySelectorAll('.c-head, .c-tags, .qh, .qr > *, .qr li, .c-title, .qrecap, .ans > *, .ans li, .box, .bx > p, .bx li, .hook, .rm, .xv-sub, .xv > h4, .xv > p, .xv li, .xv-part, .xv-tt, .xp-grid tr, .xv-more, .xp-trapoff')];
  els.forEach((e, i) => { if (!e.dataset.ak) e.dataset.ak = (e.classList.contains('rm') ? 'rm:' + e.dataset.room : 'b' + i); });
  // T-090: the primer and story boxes carry their own fixed keys (arc:…), so they never shift the numbering of the card's own lines
  // (T-091: only while their box is open — a folded box's marks are kept as saved and hidden)
  return els.concat([...box.querySelectorAll('.xp-before [data-ak], .xp-bridge [data-ak]')].filter(e => !e.closest('details:not([open])') && e.getClientRects().length));
}
function lineEls(box) {
  const out = [];
  const add = (el, sec, i) => out.push({ el, key: sec + ':' + i });
  box.querySelectorAll('.ans > p, .ans > ul > li, .ans > ol > li, .ans > table').forEach((el, i) => add(el, 'ans', i));
  // T-086: every table row is its own answer point with its own room (the table's old room is kept for ink already in it)
  box.querySelectorAll('.ans > .tbl').forEach((t, ti) => t.querySelectorAll(':scope > .tr:not(.th)').forEach((tr, ri) => add(tr, 'row' + ti, ri)));
  // T-086: boxes without a known name were all keyed 'box', so two such boxes shared rooms; the second and later now get their own key
  let other = 0;
  box.querySelectorAll('.box').forEach(b => {
    let sec = ['why', 'watch', 'qlines', 'qcross', 'note', 'qfix'].find(c => b.classList.contains(c));
    if (!sec) { sec = other ? 'box' + other : 'box'; other++; }
    b.querySelectorAll('.bx > p, .bx > ul > li').forEach((el, i) => add(el, sec, i));
  });
  return out;
}

/* ---------- text positions (for highlights that hold on to their words) ---------- */
function textOffset(block, node, off) {
  const w = document.createTreeWalker(block, NodeFilter.SHOW_TEXT); let n, t = 0;
  while ((n = w.nextNode())) { if (n === node) return t + off; t += n.length; }
  return null;
}
function rangeOf(block, a, b) {
  const w = document.createTreeWalker(block, NodeFilter.SHOW_TEXT); let n, t = 0, sN = null, sO = 0, eN = null, eO = 0, last = null;
  while ((n = w.nextNode())) { last = n; if (!sN && a <= t + n.length) { sN = n; sO = a - t; } if (!eN && b <= t + n.length) { eN = n; eO = b - t; break; } t += n.length; }
  if (!sN) return null; if (!eN) { eN = last; eO = last.length; }
  const r = document.createRange(); r.setStart(sN, Math.max(0, Math.min(sO, sN.length))); r.setEnd(eN, Math.max(0, Math.min(eO, eN.length))); return r;
}
function caretAt(x, y, hide) {
  const prev = hide.map(el => [el, el.style.pointerEvents]); hide.forEach(el => { el.style.pointerEvents = 'none'; });
  let node = null, off = 0;
  if (document.caretPositionFromPoint) { const c = document.caretPositionFromPoint(x, y); if (c) { node = c.offsetNode; off = c.offset; } }
  else if (document.caretRangeFromPoint) { const r = document.caretRangeFromPoint(x, y); if (r) { node = r.startContainer; off = r.startOffset; } }
  prev.forEach(([el, v]) => { el.style.pointerEvents = v; });
  return node && node.nodeType === 3 ? { node, off } : null;
}
// one band per line of text covered by the range, in the canvas' units
function bandsOf(range, cv) {
  const r = cv.getBoundingClientRect(), sc = cv.clientWidth / (r.width || 1), lines = [];
  for (const q of range.getClientRects()) {
    if (!q.width || q.height > 70) continue;
    const L = lines.find(l => Math.abs(l.top - q.top) < 4 || Math.abs(l.bottom - q.bottom) < 4);
    if (L) { L.left = Math.min(L.left, q.left); L.right = Math.max(L.right, q.right); L.top = Math.min(L.top, q.top); L.bottom = Math.max(L.bottom, q.bottom); }
    else lines.push({ left: q.left, right: q.right, top: q.top, bottom: q.bottom });
  }
  return lines.map(l => [(l.left - r.left) * sc, ((l.top + l.bottom) / 2 - r.top) * sc, (l.right - r.left) * sc, (l.bottom - l.top) * sc * 0.92]);
}

/* ---------- the overlay ---------- */
function makeOverlay(box, rec, face) {
  const cv = document.createElement('canvas'); cv.className = 'ink-ov';
  box.appendChild(cv);
  cv.addEventListener('click', e => { if (writing) { e.stopPropagation(); e.preventDefault(); } });
  const cs = String(getComputedStyle(box).getPropertyValue('--cs') || '1').trim();
  const saved = rec.ov[face];
  const w = box.clientWidth;
  const v1 = !!(saved && saved.v !== 2);
  const sameScreen = !v1 || (Math.abs((saved.w || w) - w) / w < 0.06 && String(saved.cs || cs).trim() === cs);
  let geo = {};
  const blockOf = {};
  const measure = () => {
    const r = cv.getBoundingClientRect(), sc = cv.clientWidth / (r.width || 1), g = {};
    anchorsOf(box).forEach(e => { const q = e.getBoundingClientRect(); g[e.dataset.ak] = [(q.left - r.left) * sc, (q.top - r.top) * sc, q.width * sc, q.height * sc]; blockOf[e.dataset.ak] = e; });
    g.top = [0, 0, cv.clientWidth, 0]; return g;
  };
  const size = () => { cv.style.width = box.scrollWidth + 'px'; cv.style.height = '0px'; cv.style.height = box.scrollHeight + 'px'; };
  size(); geo = measure();
  const map = () => ({ X: p => p[0], Y: p => p[1], k: 1 });
  const s = new Surface(cv, [], { map, changed: () => {}, limits: () => writing });
  const anchorFor = (x, y) => {
    // T-091: a mark made inside a primer/story block belongs to that block (so it folds away with it)
    for (const [k, g] of Object.entries(geo)) if (k.startsWith('arc:') && x >= g[0] - 4 && x <= g[0] + g[2] + 4 && y >= g[1] - 4 && y <= g[1] + g[3] + 4) return k;
    let best = 'top', by = -Infinity;
    for (const [k, g] of Object.entries(geo)) if (k !== 'top' && !k.startsWith('rm:') && g[1] <= y + 1 && g[1] > by) { best = k; by = g[1]; }
    return best;
  };
  // saved form: points relative to the block's top-left, with the block's size at the time
  const toRel = o => {
    if (o._rel) return o._rel;                            // a mark on a story box that is not shown in this flow: kept as saved
    const a = (o.a && geo[o.a]) ? o.a : anchorFor(o.pts[0][0], o.pts[0][1]), g = geo[a];
    const c = { ...o, a, g: [g[2], g[3]], pts: o.pts.map(q => q.length > 2 ? [q[0] - g[0], q[1] - g[1], q[2]] : [q[0] - g[0], q[1] - g[1]]) };
    if (o.rects) c.rects = o.rects.map(r => [r[0] - g[0], r[1] - g[1], r[2] - g[0], r[3]]);
    delete c.hidden; return c;
  };
  // back to this screen: stretch with the block (width) and with its height for marks inside it
  const fx = (o, g) => { const fw = o.g && o.g[0] ? g[2] / o.g[0] : 1, oh = o.g ? o.g[1] : 0; return [v => g[0] + v * fw, v => g[1] + (oh && v <= oh ? v * g[3] / oh : (oh ? v - oh + g[3] : v))]; };
  const toAbs = o => {
    const ak = o.tr && o.tr.ak && o.tr.ak.startsWith('arc:') ? o.tr.ak : o.a;
    if (ak && ak.startsWith('arc:') && !geo[ak]) return { ...o, hidden: true, _rel: o };   // T-090: its story box is not on screen now
    const g = geo[o.a] || geo.top, [X, Y] = fx(o, g);
    const c = { ...o, pts: o.pts.map(q => q.length > 2 ? [X(q[0]), Y(q[1]), q[2]] : [X(q[0]), Y(q[1])]) };
    if (o.rects) c.rects = o.rects.map(r => [X(r[0]), Y(r[1]), X(r[2]), r[3]]);
    delete c.g; return c;
  };
  const resnap = o => {                                   // highlights tied to words follow the words
    if (!(o.type === 'hl' && o.snap && o.tr)) return;
    const el = blockOf[o.tr.ak]; if (!el) return;
    const rg = rangeOf(el, Math.min(o.tr.s, o.tr.e), Math.max(o.tr.s, o.tr.e)); if (!rg) return;
    const b = bandsOf(rg, cv); if (!b.length) return;
    const bb = o.ul ? ulBands(b, o.ulw || 2) : b;
    o.rects = bb; o.pts = [[bb[0][0], bb[0][1]], [bb[bb.length - 1][2], bb[bb.length - 1][1]]]; o.h = bb[0][3];
  };
  let initial = [];
  if (saved && saved.objs) {
    if (!v1) initial = saved.objs.map(toAbs);
    else if (sameScreen) initial = saved.objs.map(o => ({ ...o, pts: o.pts.map(q => [q[0], q[1] + (geo[o.a] ? geo[o.a][1] : 0), q[2]]) }));
  }
  initial.forEach(resnap);
  s.objs.push(...initial);
  s.relayout = () => {
    const rel = s.objs.map(toRel);
    size(); geo = measure();
    const abs = rel.map(toAbs); abs.forEach(resnap);
    s.objs.splice(0, s.objs.length, ...abs);
    s.render();
  };
  s.serialise = () => ({ v: 2, w: box.clientWidth, cs, objs: s.objs.map(toRel) });
  s.anchorFor = p => anchorFor(p[0], p[1]); s.hiddenFromOther = v1 && !sameScreen && saved.objs.length;
  s.toUnits = (x, y) => { const r = cv.getBoundingClientRect(), sc = cv.clientWidth / (r.width || 1); return [(x - r.left) * sc, (y - r.top) * sc]; };
  s.unitPerPx = () => { const r = cv.getBoundingClientRect(); return cv.clientWidth / (r.width || 1); };
  const hide = () => [cv, ...box.querySelectorAll('.rm-cv, .ink-tx')];
  s.snapLine = e => {
    const c = caretAt(e.clientX, e.clientY, hide());
    if (!c || !box.contains(c.node)) return null;
    const el = c.node.parentElement && c.node.parentElement.closest('[data-ak]');
    if (!el || !box.contains(el) || el.classList.contains('rm')) return null;
    const rg = document.createRange(); rg.setStart(c.node, c.off); rg.setEnd(c.node, Math.min(c.node.length, c.off + 1));
    const rr = rg.getClientRects()[0] || c.node.parentElement.getBoundingClientRect();
    if (!rr || !rr.height || rr.height > 70 || e.clientY < rr.top - 8 || e.clientY > rr.bottom + 8) return null;
    if (e.clientX < rr.left - 14 || e.clientX > rr.right + 14) return null;   // beside the words (margin, end of a line): draw freely
    const r = cv.getBoundingClientRect(), sc = cv.clientWidth / (r.width || 1);
    const off = textOffset(el, c.node, c.off);
    return { y: (rr.top + rr.height / 2 - r.top) * sc, h: rr.height * sc * 0.92, el, off, tr: null, rects: null };
  };
  s.snapUpdate = (line, e) => {
    if (!line || line.off == null) return null;
    const c = caretAt(e.clientX, e.clientY, hide());
    const off2 = c && line.el.contains(c.node) ? textOffset(line.el, c.node, c.off) : null;
    if (off2 == null) return line.last || null;
    const a = Math.min(line.off, off2), b = Math.max(line.off, off2); if (a === b) return line.last || null;
    const rg = rangeOf(line.el, a, b); if (!rg) return line.last || null;
    const rects = bandsOf(rg, cv); if (!rects.length) return line.last || null;
    line.last = { rects, tr: { ak: line.el.dataset.ak, s: a, e: b } };
    return line.last;
  };
  s.scrollBy = dy => { box.scrollTop += dy; };
  s.parentEl = box; s.toCss = p => [p[0], p[1]]; s.cssScale = () => 1;
  return s;
}

/* ---------- rooms ---------- */
function makeRoom(holder, key, data, onChange) {
  const wrap = document.createElement('div'); wrap.className = 'rm'; wrap.dataset.room = key;
  const cv = document.createElement('canvas'); cv.className = 'rm-cv';
  const more = document.createElement('button'); more.type = 'button'; more.className = 'rm-more'; more.setAttribute('aria-label', 'One more space'); more.title = 'One more space';
  more.innerHTML = '<svg viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>';
  // T-086: ⌃ takes one empty space back (never below the ink already written)
  const less = document.createElement('button'); less.type = 'button'; less.className = 'rm-more rm-less'; less.setAttribute('aria-label', 'One space less'); less.title = 'One space less';
  less.innerHTML = '<svg viewBox="0 0 24 24"><path d="M6 15l6-6 6 6"/></svg>';
  wrap.appendChild(cv); wrap.appendChild(less); wrap.appendChild(more); holder.appendChild(wrap);
  wrap.addEventListener('click', e => { if (writing) { e.stopPropagation(); } });
  const kNow = () => (cv.clientWidth || wrap.clientWidth || ROOM_W) / ROOM_W;
  // the room grows with the text when the side is zoomed (its height follows the zoom; its ink keeps the room's width)
  const zf = () => { const r = cv.getBoundingClientRect().width, c = cv.clientWidth; return r && c ? Math.max(0.5, Math.min(3, r / c)) : 1; };
  const fit = () => {
    const used = (data.objs || []).reduce((m, o) => Math.max(m, objBox(o)[3]), 0);
    if (used + 10 > (data.h || SPACE)) data.h = Math.ceil((used + 20) / (SPACE / 2)) * (SPACE / 2);
    cv.style.height = Math.round((data.h || SPACE) * kNow() * zf()) + 'px';
  };
  fit();
  const map = () => { const k = kNow(); return { X: p => p[0] * k, Y: p => p[1] * k, k }; };
  const s = new Surface(cv, data.objs || (data.objs = []), { map, changed: () => {}, limits: () => writing });
  s.toUnits = (x, y) => { const r = cv.getBoundingClientRect(), sc = cv.clientWidth / (r.width || 1), k = kNow(); return [(x - r.left) * sc / k, (y - r.top) * sc / k]; };
  s.unitPerPx = () => { const r = cv.getBoundingClientRect(); return (cv.clientWidth / (r.width || 1)) / kNow(); };
  // ⌄ at the end of the room: one more full space. After writing, the room trims to what was used (in half spaces).
  more.onpointerdown = e => e.stopPropagation();
  more.onclick = e => { e.stopPropagation(); e.preventDefault(); data.h = (data.h || SPACE) + SPACE; fit(); s.render(); showLess(); onChange(true); if (cur) { cur.last = s; cur.overlay.relayout(); } };
  const usedH = () => s.objs.reduce((m, o) => { const b = objBox(o); return Math.max(m, b[3] + (o.type === 'text' ? 0 : (o.s || o.h || 0) / 2)); }, 0);
  const showLess = () => { less.hidden = (data.h || SPACE) - SPACE < Math.max(SPACE / 2, usedH() + 6); };
  less.onpointerdown = e => e.stopPropagation();
  less.onclick = e => { e.stopPropagation(); e.preventDefault(); const min = Math.max(SPACE / 2, Math.ceil((usedH() + 6) / (SPACE / 2)) * (SPACE / 2)); data.h = Math.max(min, (data.h || SPACE) - SPACE); fit(); s.render(); showLess(); onChange(true); if (cur) cur.overlay.relayout(); };
  s.showLess = showLess; showLess();
  s.trim = () => {
    if (!s.objs.length) return false;
    const used = s.objs.reduce((m, o) => { const b = objBox(o); return Math.max(m, b[3] + (o.type === 'text' ? 0 : (o.s || o.h || 0) / 2)); }, 0);
    const h = Math.max(SPACE / 2, Math.ceil((used + 6) / (SPACE / 2)) * (SPACE / 2));
    if (h === data.h) return false;
    data.h = h; fit(); s.render(); showLess(); onChange(true); return true;
  };
  s.wrap = wrap; s.data = data; s.fit = fit; s.parentEl = wrap; s.toCss = p => [p[0] * kNow(), p[1] * kNow()]; s.cssScale = kNow;
  return s;
}

/* ---------- clipboard: kept by the app, so it pastes on this card, the next card, any card, or another window ---------- */
// clipboard history: the last 12 copies, newest first; each can be pasted any number of times on any card
function readClips() {
  try {
    let a = JSON.parse(localStorage.getItem(CLIP_KEY) || 'null');
    if (!Array.isArray(a)) { const old = JSON.parse(localStorage.getItem(OLD_CLIP) || 'null'); a = old ? [{ id: 'c' + old.ts, ...old }] : []; }
    return a;
  } catch (e) { return []; }
}
function saveClips(a) { try { localStorage.setItem(CLIP_KEY, JSON.stringify(a.slice(0, CLIP_MAX))); localStorage.removeItem(OLD_CLIP); } catch (e) { /* private mode or full */ } }
function writeClip(c) { const a = readClips(); a.unshift({ id: 'c' + c.ts + Math.random().toString(36).slice(2, 5), ...c }); saveClips(a); }
// while writing, no browser text selection or long-press menu anywhere on the card (the S Pen button triggers both on the Tab)
document.addEventListener('contextmenu', e => {
  const st = cur; if (!st) return;
  if (writing && st.box.contains(e.target)) { e.preventDefault(); return; }
  // T-136: mouse (DeX / desktop): select words, right-click → the marking menu instead of the browser's
  const ws = getSelection(); if (!ws || ws.isCollapsed || !ws.rangeCount) return;
  const s = st.xbox && st.overlayX && st.xbox.contains(e.target) ? st.overlayX : st.box.contains(e.target) ? st.overlay : null;
  if (!s || !s.parentEl) return;
  const sel = selFromRange(s, ws.getRangeAt(0)); if (!sel.length) return;
  e.preventDefault(); ws.removeAllRanges(); textBar(s, sel, e.clientX, e.clientY);
}, true);
document.addEventListener('selectstart', e => { if (writing && cur && cur.box.contains(e.target) && !e.target.closest('.ink-tx')) e.preventDefault(); }, true);
addEventListener('storage', e => { if (e.key === CLIP_KEY && cur && cur.toolbar) cur.toolbar.draw(); });
function copySel(s) {
  const objs = s.sel.ids.filter(i => s.objs[i]).map(i => JSON.parse(JSON.stringify(s.objs[i])));
  if (!objs.length) return;
  const bb = objs.map(objBox).reduce((a, b) => [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[2], b[2]), Math.max(a[3], b[3])]);
  const f = 1 / s.unitPerPx();                                     // stored in screen pixels
  objs.forEach(o => { delete o.a; delete o.hidden; shiftObj(o, -bb[0], -bb[1]); scaleObj(o, f); });
  writeClip({ n: objs.length, objs, ts: Date.now() });
}
function pasteInto(s, p) {
  const c = readClips().find(x => x.id === pasting) || readClips()[0]; if (!c || !cur) return;
  s.snapshot();
  const f = s.unitPerPx(), start = s.objs.length;
  for (const src of c.objs) { const o = JSON.parse(JSON.stringify(src)); scaleObj(o, f); shiftObj(o, p[0], p[1]); if (isOv(cur, s)) o.a = s.anchorFor(o.pts[0]); s.objs.push(o); }
  s.sel = { ids: c.objs.map((_, j) => start + j) };
  pasting = null;
  if (s.data) { const b = s.objs.slice(start).map(objBox).reduce((m, q) => Math.max(m, q[3]), 0); if (b > (s.data.h || SPACE) - 10) { s.data.h = Math.ceil((b + 20) / (SPACE / 2)) * (SPACE / 2); s.fit(); } }
  s.render();
  settings().tool = 'lasso'; cur.last = s; markDirty(); if (cur.toolbar) { cur.toolbar.clipOpen = false; cur.toolbar.draw(); }
}

/* ---------- mount on the current card face ---------- */
export async function mountInk(cardEl, card, face, opts) {
  await flushInk();
  const box = cardEl.querySelector(face === 'q' ? '.c-q' : '.c-a'); if (!box) { cur = null; return; }
  const rec = await loadInk(card);
  if (!document.body.contains(box)) return;
  // T-086: mounting again on the same face (e.g. after Learn/Revise) must not leave the old rooms, chevrons and canvases behind —
  // they showed the same ink several times over (Naven, 5 Nov)
  box.querySelectorAll('.rm-hold, .rm-chev, canvas.ink-ov, .ink-tx').forEach(n => n.remove());
  const xb0 = face === 'a' ? cardEl.querySelector('.xp-pane') : null; if (xb0) xb0.querySelectorAll('canvas.ink-ov, .ink-tx').forEach(n => n.remove());
  const st = { card, face, rec, box, rooms: new Map(), open: new Set(Object.keys(rec.rooms || {}).filter(k => rec.rooms[k].objs && rec.rooms[k].objs.length)), last: null, dirty: false, t: null, opts };
  if (cur && cur.toolbar) cur.toolbar.destroy();
  cur = st;
  // chevrons and rooms beside every line (answer side)
  if (face === 'a') for (const { el, key } of lineEls(box)) {
    const has = rec.rooms[key] && rec.rooms[key].objs && rec.rooms[key].objs.length;
    el.classList.add('rm-line');
    // T-072: a lettered part opens its room from its own circled letter (no chevron beside it)
    const sp = el.querySelector(':scope > .sp');
    if (sp) {
      sp.classList.add('rm-l'); sp.dataset.rk = key; sp.classList.toggle('has', !!has); sp.setAttribute('role', 'button'); sp.tabIndex = 0;
      sp.setAttribute('aria-label', has ? 'Show or hide your note under this part' : 'Open room to write under this part');
      const holder = document.createElement('div'); holder.className = 'rm-hold'; holder.dataset.for = key;
      if (el.tagName === 'LI') el.appendChild(holder); else el.after(holder);
      sp.addEventListener('pointerdown', e => e.stopPropagation(), true);
      sp.onclick = e => { e.stopPropagation(); e.preventDefault(); toggleRoom(key); };
      continue;
    }
    const holder = document.createElement('div'); holder.className = 'rm-hold'; holder.dataset.for = key;
    const b = document.createElement('button'); b.type = 'button'; b.className = 'rm-chev' + (has ? ' has' : ''); b.dataset.rk = key;
    b.setAttribute('aria-label', has ? 'Show or hide your note under this line' : 'Open room to write under this line');
    b.innerHTML = has ? PEN : CHEV;
    el.appendChild(b); if (el.tagName === 'LI') el.appendChild(holder); else el.after(holder);
    b.onclick = e => { e.stopPropagation(); e.preventDefault(); toggleRoom(key); };
  }
  st.overlay = makeOverlay(box, rec, face);
  wireSurface(st.overlay);
  // Explain pane (answer side): its own ink layer, saved per depth (Learn and Revise lay out differently)
  const xbox = face === 'a' ? cardEl.querySelector('.xp-pane') : null;
  if (xbox) {
    const xp = xbox.querySelector('.xp'); st.xface = 'x:' + ((xp && xp.dataset.depth) || 'learn'); st.xbox = xbox;
    st.overlayX = makeOverlay(xbox, rec, st.xface); wireSurface(st.overlayX);
    xbox.addEventListener('toggle', () => { if (cur === st) st.overlayX.relayout(); }, true);
    new ResizeObserver(() => { if (cur === st && st.overlayX) st.overlayX.relayout(); }).observe(xbox);
  }
  drawRooms();
  ovs(st).forEach(o => o.relayout());
  box.querySelectorAll('details').forEach(d => d.addEventListener('toggle', () => { if (cur === st) { st.overlay.relayout(); drawChevrons(); } }));   // T-091: primer/story folded or opened
  // T-090: a face drawn during the flip/turn animation is measured while transformed, so marks landed off the text (question-face
  // highlights seemed lost after Reveal → Question). Measure again once the animation has finished.
  [260, 520].forEach(t => setTimeout(() => { if (cur === st && !writing) ovs(st).forEach(o => o.relayout()); }, t));
  quietWatch(box); if (st.xbox) quietWatch(st.xbox);
  applyMode();
  box.addEventListener('toggle', () => { if (cur === st) { st.rooms.forEach(r => { r.fit(); r.render(); }); st.overlay.relayout(); } }, true);
  let lastW = box.clientWidth;
  new ResizeObserver(() => { if (cur !== st) return; st.rooms.forEach(r => { r.fit(); r.render(); }); st.overlay.relayout(); if (Math.abs(box.clientWidth - lastW) > 2) lastW = box.clientWidth; }).observe(box);
}
const PEN = '<svg viewBox="0 0 24 24"><path d="M14.6 4.6l4.8 4.8L9 19.8l-5.3.9.9-5.3z"/></svg>', CHEV = '<svg viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>';
function wireSurface(s) {
  const st = cur;
  attachPointer(s, {
    writing: () => writing, toUnits: s.toUnits, unitPerPx: s.unitPerPx, map: () => s.o.map(), snapLine: s.snapLine || null, snapUpdate: s.snapUpdate || null,
    scrollBy: dy => { (s.parentEl || st.box).scrollTop += dy; },
    selChanged: () => { if (st.last && st.last !== s && st.last.sel) { st.last.sel = null; st.last.render(); } st.last = s; if (st.toolbar) st.toolbar.draw(); },
    onDown: surf => {
      if (st.toolbar) st.toolbar.closePop();
      // moving to another writing area: the room just left trims to the space it used
      if (st.last && st.last !== surf && st.last.trim && st.last.trim()) st.overlay.relayout();
      st.last = surf;
    },
    pasting: () => !!pasting, pasteAt: p => pasteInto(s, p),
    armChanged: on => { const h = st.opts.toolbarHost && st.opts.toolbarHost(); if (h) h.classList.toggle('ik-armed', on); },
    textAt: (p, e, hit) => textAt(s, p, hit),
    lassoText: poly => lassoText(s, poly),
    textSel: (act, e, phase) => textSelect(s, act, e, phase),
    dropOut: e => dropOut(s, e),
    changed: o => { st.last = s; if (o && isOv(st, s) && !o.a) o.a = s.anchorFor(o.pts[0]); if (!isOv(st, s)) { drawChevrons(); if (s.showLess) s.showLess(); } markDirty(); }
  });
}

/* ---------- T-072/T-074: choosing words ----------
   Select-text tool: drag from the first word to the last (whole words), or tap a part to take all of it.
   Lasso drawn over words with no ink inside: only the lines whose middle lies inside the loop are taken. */
const leafBlocks = box => [...box.querySelectorAll('[data-ak]')].filter(el => !el.classList.contains('rm') && !el.querySelector('[data-ak]') && el.textContent.trim());
const hideOf = s => [s.cv, ...s.parentEl.querySelectorAll('.rm-cv, .ink-tx')];
function caretIn(s, x, y) {
  const c = caretAt(x, y, hideOf(s)); if (!c) return null;
  const el = c.node.parentElement && c.node.parentElement.closest('[data-ak]');
  if (!el || !s.parentEl.contains(el) || el.classList.contains('rm')) return null;
  const off = textOffset(el, c.node, c.off); return off == null ? null : { el, off };
}
function wordSnap(t, a, b) { while (a > 0 && /\S/.test(t[a - 1])) a--; while (b < t.length && /\S/.test(t[b])) b++; return [a, b]; }
function selBetween(s, c0, c1) {
  const blocks = leafBlocks(s.parentEl); let i0 = blocks.indexOf(c0.el), i1 = blocks.indexOf(c1.el); if (i0 < 0 || i1 < 0) return [];
  if (i1 < i0 || (i1 === i0 && c1.off < c0.off)) { [c0, c1] = [c1, c0]; [i0, i1] = [i1, i0]; }
  const out = [];
  for (let i = i0; i <= i1; i++) {
    const el = blocks[i], t = el.textContent; let a = i === i0 ? c0.off : 0, b = i === i1 ? c1.off : t.length;
    [a, b] = wordSnap(t, a, b); if (b - a < 1) continue;
    out.push({ el, a, b, text: t.slice(a, b).replace(/\s+/g, ' ').trim().replace(/^[a-h](?=[A-Z(“"])/, '') });
  }
  return out;
}
let tmarks = [];
function drawMarks(sel) {
  tmarks.forEach(m => m.remove()); tmarks = [];
  sel.forEach(t => { const rg = rangeOf(t.el, t.a, t.b); if (rg) for (const q of rg.getClientRects()) { if (q.width < 1) continue; const m = document.createElement('div'); m.className = 'ik-tmark'; Object.assign(m.style, { left: q.left + 'px', top: q.top + 'px', width: q.width + 'px', height: q.height + 'px' }); document.body.appendChild(m); tmarks.push(m); } });
}
function textSelect(s, act, e, phase) {
  if (!s.parentEl) return;
  if (phase === 'start') { document.querySelectorAll('.ik-tsel').forEach(n => n.remove()); act.c0 = caretIn(s, e.clientX, e.clientY); act.sel = []; drawMarks([]); return; }
  if (!act.c0) { const c = caretIn(s, e.clientX, e.clientY); if (c) act.c0 = c; else return; }
  const tap = Math.hypot(e.clientX - act.sx, e.clientY - act.sy) < 8;
  if (phase === 'move') { if (tap) return; const c1 = caretIn(s, e.clientX, e.clientY); if (c1) { act.sel = selBetween(s, act.c0, c1); drawMarks(act.sel); } return; }
  let sel = act.sel || [];
  if (tap) { const el = act.c0.el, t = el.textContent; sel = [{ el, a: 0, b: t.length, text: t.replace(/\s+/g, ' ').trim().replace(/^[a-h](?=[A-Z(“"])/, '') }]; }
  if (!sel.length) { drawMarks([]); return; }
  textBar(s, sel, e.clientX, e.clientY);
}
const inPolyS = (pt, poly) => { let c = false; for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) { const [xi, yi] = poly[i], [xj, yj] = poly[j]; if ((yi > pt[1]) !== (yj > pt[1]) && pt[0] < (xj - xi) * (pt[1] - yi) / (yj - yi) + xi) c = !c; } return c; };
function lassoText(s, poly) {
  const st = cur; if (!st || !s.parentEl) return;
  const r0 = s.cv.getBoundingClientRect(), k = r0.width / (s.cv.clientWidth || 1);
  const P = poly.map(p => [r0.left + p[0] * k, r0.top + p[1] * k]);
  const sel = [];
  for (const el of leafBlocks(s.parentEl)) {
    const t = el.textContent, rg = rangeOf(el, 0, t.length); if (!rg) continue;
    const lines = [...rg.getClientRects()].filter(q => q.width > 2 && inPolyS([q.left + Math.min(q.width / 2, 40), q.top + q.height / 2], P) || (q.width > 2 && inPolyS([q.left + q.width / 2, q.top + q.height / 2], P)));
    if (!lines.length) continue;
    const f = lines[0], l = lines[lines.length - 1];
    const a = caretIn(s, f.left + 2, f.top + f.height / 2), b = caretIn(s, l.right - 2, l.top + l.height / 2);
    let A = a && a.el === el ? a.off : 0, B = b && b.el === el ? b.off + 1 : t.length;
    [A, B] = wordSnap(t, A, Math.min(B, t.length)); if (B - A < 1) continue;
    sel.push({ el, a: A, b: B, text: t.slice(A, B).replace(/\s+/g, ' ').trim().replace(/^[a-h](?=[A-Z(“"])/, '') });
  }
  if (!sel.length) return;
  const last = P.reduce((m, p) => p[1] > m[1] ? p : m, P[0]);
  textBar(s, sel, Math.min(...P.map(p => p[0])), last[1]);
}
// T-136: marking colours: [highlighter, ink for underline / box / circle / bold]
const MK = [['#ffcc00', '#b98a00'], ['#7ee07e', '#1f8f3a'], ['#ff8fc8', '#c81f6e'], ['#8fd0ff', '#1f4fd8'], ['#ffb066', '#d75f00']];
const MK_KEY = 'trace.mk';
const mkNow = () => { try { const i = +localStorage.getItem(MK_KEY); return MK[i] ? i : 0; } catch (e) { return 0; } };
export const ulBands = (b, w) => b.map(r => [r[0], r[1] + r[3] / 2 + w / 2, r[2], w]);
function selFromRange(s, rg) {
  const out = [];
  for (const el of leafBlocks(s.parentEl)) {
    if (!rg.intersectsNode(el)) continue;
    const t = el.textContent, off = (n, o) => { const r = document.createRange(); r.setStart(el, 0); r.setEnd(n, o); return r.toString().length; };
    let a = el.contains(rg.startContainer) ? off(rg.startContainer, rg.startOffset) : 0, b = el.contains(rg.endContainer) ? off(rg.endContainer, rg.endOffset) : t.length;
    [a, b] = wordSnap(t, a, b); if (b - a < 1) continue;
    out.push({ el, a, b, text: t.slice(a, b).replace(/\s+/g, ' ').trim().replace(/^[a-h](?=[A-Z(“"])/, '') });
  }
  return out;
}
function textBar(s, sel, x, y) {
  document.querySelectorAll('.ik-tsel').forEach(n => n.remove());
  drawMarks(sel); const marks = tmarks;
  const bar = document.createElement('div'); bar.className = 'ik-tsel';
  const sw = () => MK.map((m, i) => `<button data-sw="${i}" class="ik-sw${i === mkNow() ? ' on' : ''}" style="background:${m[0]}" aria-label="Colour ${i + 1}"></button>`).join('');
  bar.innerHTML = `<div class="ik-tsr">${sw()}</div><div class="ik-tsr"><button data-t="hl">Highlight</button><button data-t="ul">Underline</button><button data-t="box">Box</button><button data-t="circ">Circle</button><button data-t="bold">Bold</button></div><div class="ik-tsr"><button data-t="move">Select &amp; move</button><button data-t="copy">Copy text</button>${s === (cur && cur.overlayX) ? '<button data-t="tocard">→ Move to card</button><button data-t="unclear" class="ik-unclear">? Still unclear</button>' : ''}${cur && cur.opts.onAsk ? '<button data-t="ask" class="ik-ask">Ask ▸</button>' : ''}<button data-t="x" aria-label="Close">✕</button></div>`;
  Object.assign(bar.style, { left: Math.max(8, Math.min(innerWidth - 470, x)) + 'px', top: Math.max(8, Math.min(innerHeight - 150, y + 8)) + 'px' });
  document.body.appendChild(bar);
  const made = [];
  const close = () => { bar.remove(); drawMarks([]); removeEventListener('scroll', close, true); removeEventListener('pointerdown', away, true); };
  const away = e => { if (!bar.contains(e.target)) close(); };
  addEventListener('scroll', close, true); setTimeout(() => addEventListener('pointerdown', away, true), 0);
  bar.addEventListener('pointerdown', e => e.stopPropagation());
  bar.addEventListener('contextmenu', e => e.preventDefault());
  bar.querySelectorAll('[data-sw]').forEach(b => b.onclick = e => { e.stopPropagation(); try { localStorage.setItem(MK_KEY, b.dataset.sw); } catch (er) { /* */ } bar.querySelectorAll('[data-sw]').forEach(n => n.classList.toggle('on', n === b)); });
  const mark = k => {
    s.snapshot(); const S = settings(), m = MK[mkNow()], u = s.unitPerPx ? s.unitPerPx() : 1, n0 = s.objs.length, all = [];
    for (const t of sel) { const rg = rangeOf(t.el, t.a, t.b); if (!rg) continue; const rects = bandsOf(rg, s.cv); if (!rects.length) continue;
      all.push(...rects); const tr = { ak: t.el.dataset.ak, s: t.a, e: t.b };
      if (k === 'hl' || k === 'ul' || k === 'bold') {
        const w = (k === 'bold' ? 3.6 : 1.8) * u, rr = k === 'hl' ? rects : ulBands(rects, w);
        const o = { type: 'hl', snap: true, c: k === 'hl' ? m[0] : m[1], o: k === 'hl' ? S.hl.op / 100 : 1, h: rr[0][3], rects: rr, pts: [[rr[0][0], rr[0][1]], [rr[rr.length - 1][2], rr[rr.length - 1][1]]], tr };
        if (k !== 'hl') { o.ul = 1; o.ulw = w; }
        o.a = s.anchorFor(o.pts[0]); s.objs.push(o);
      } }
    if ((k === 'box' || k === 'circ') && all.length) {
      const x0 = Math.min(...all.map(r => r[0])), x1 = Math.max(...all.map(r => r[2])), y0 = Math.min(...all.map(r => r[1] - r[3] / 2)), y1 = Math.max(...all.map(r => r[1] + r[3] / 2));
      const px = (k === 'circ' ? 10 : 4) * u, py = (k === 'circ' ? 7 : 3) * u;
      const o = { type: 'shape', kind: k === 'box' ? 'rect' : 'ellipse', c: m[1], s: 2 * u, pts: [[x0 - px, y0 - py], [x1 + px, y1 + py]] };
      o.a = s.anchorFor(o.pts[0]); s.objs.push(o);
    }
    for (let i = n0; i < s.objs.length; i++) made.push(i);
    s.render(); markDirty(); drawMarks([]);
  };
  bar.querySelectorAll('[data-t]').forEach(b => b.onclick = async e => {
    e.stopPropagation(); const k = b.dataset.t, st = cur;
    if (['hl', 'ul', 'box', 'circ', 'bold'].includes(k) && st) { mark(k); return; }   // the menu stays: add a box to a highlight, or pick Select & move
    if (k === 'move' && st) {
      if (!made.length) mark('hl');
      close(); quiet = false; setWriting(true); settings().tool = 'lasso';
      s.sel = { ids: made.filter(i => s.objs[i]) }; st.last = s; s.render(); if (st.toolbar) st.toolbar.draw();
      toast('Selected · drag it to move it'); return;
    }
    if (k === 'copy') { const txt = sel.map(t => t.text).join('\n'); try { await navigator.clipboard.writeText(txt); toast('Text copied'); } catch (er) { toast('Copy was blocked by the browser'); } }
    else if (k === 'ask' && st && st.opts.onAsk) { const r = b.getBoundingClientRect(); close(); st.opts.onAsk(sel.map(t => t.text).filter(Boolean), s === st.overlayX ? 'Explain' : 'card', r); return; }
    else if (k === 'tocard' && st) { close(); textToCard(st, sel.map(t => t.text).filter(Boolean).join(' ')); return; }
    else if (k === 'unclear' && st && st.opts.onUnclear) { st.opts.onUnclear(sel.map(t => t.text).filter(Boolean)); toast('Saved to “Still unclear” · the next rewrite of this deck expands it'); }
    close();
  });
}
// T-086: selected Explain words become a typed note on the card: selected, so it drags straight away; tap it with the Text tool to add words
function wrapWords(t, n = 46) { const out = []; let line = ''; for (const w of t.split(/\s+/)) { if (line && (line + ' ' + w).length > n) { out.push(line); line = w; } else line = line ? line + ' ' + w : w; } if (line) out.push(line); return out.join('\n'); }
function textToCard(st, text) {
  const to = st.overlay; if (!to || !text) return;
  const pr = to.parentEl.getBoundingClientRect(), y = Math.max(pr.top, 70) + 40, S = settings();
  const at = to.toUnits(pr.left + 36, y);
  to.snapshot();
  const o = { type: 'text', t: wrapWords(text), c: S.text.color, s: S.text.size * to.unitPerPx(), b: false, bg: '#fff6c4', pts: [at] };
  o.a = to.anchorFor(at); to.objs.push(o);
  [...ovs(st), ...st.rooms.values()].forEach(x => { if (x !== to && x.sel) { x.sel = null; x.render(); } });
  to.sel = { ids: [to.objs.length - 1] }; st.last = to; S.tool = 'lasso';
  to.render(); markDirty(); if (st.toolbar) st.toolbar.draw();
  toast('On the card · drag it where you want · to add words, pick the Text tool (T) and tap it');
}
/* ---------- T-072: marks dragged out of one writing area land in the area under the pen (Explain ↔ card) ---------- */
function dropOut(s, e) {
  const st = cur; if (!st || !s.parentEl || !isOv(st, s)) return false;
  const inside = el => { const q = el.getBoundingClientRect(); return e.clientX >= q.left && e.clientX <= q.right && e.clientY >= q.top && e.clientY <= q.bottom; };
  if (inside(s.parentEl)) return false;
  const to = ovs(st).find(o => o !== s && inside(o.parentEl)); if (!to || !s.sel) return false;
  const r1 = s.cv.getBoundingClientRect(), k1 = r1.width / (s.cv.clientWidth || 1);
  const conv = q => { const u = to.toUnits(r1.left + q[0] * k1, r1.top + q[1] * k1); return q.length > 2 ? [u[0], u[1], q[2]] : u; };
  const f = to.unitPerPx() * k1;
  const ids = s.sel.ids.filter(i => s.objs[i]), moved = ids.map(i => JSON.parse(JSON.stringify(s.objs[i])));
  to.snapshot();
  for (const o of moved) {
    o.pts = o.pts.map(conv);
    if (o.rects) o.rects = o.rects.map(r => { const a = conv([r[0], r[1]]), b = conv([r[2], r[1]]); return [a[0], a[1], b[0], r[3] * f]; });
    if (o.s) o.s *= f; if (o.h) o.h *= f; if (o.r) o.r *= f;
    delete o.tr; delete o.a; o.a = to.anchorFor(o.pts[0]); to.objs.push(o);
  }
  const gone = new Set(ids); s.objs.splice(0, s.objs.length, ...s.objs.filter((o, i) => !gone.has(i)));
  s.sel = null; to.sel = { ids: moved.map((_, j) => to.objs.length - moved.length + j) }; st.last = to;
  s.render(); to.render(); markDirty(); if (st.toolbar) st.toolbar.draw();
  return true;
}

/* ---------- text: an editor right where the pen tapped, inside the card ---------- */
function textAt(s, p, hit) {
  const st = cur, S = settings(), host = s.parentEl;
  st.box.querySelectorAll('.ink-tx').forEach(n => n.remove());
  const old = hit >= 0 ? s.objs[hit] : null;
  const k = s.cssScale();
  const style = { c: old ? old.c : S.text.color, b: old ? !!old.b : S.text.bold, size: old ? old.s / s.unitPerPx() : S.text.size };
  if (old) { old.hidden = true; s.render(); }
  const at = old ? old.pts[0] : p, css = s.toCss(at);
  const wrap = document.createElement('div'); wrap.className = 'ink-tx';
  wrap.style.left = Math.max(0, Math.min(css[0], host.clientWidth - 300)) + 'px'; wrap.style.top = Math.max(0, css[1]) + 'px';
  wrap.innerHTML = `<div class="ink-txbar">
      <button data-tz="-1" aria-label="Smaller">A−</button><button data-tz="1" aria-label="Bigger">A+</button><button data-tb aria-label="Bold"><b>B</b></button>
      ${['#1c1c1e', '#1f4fd8', '#e0312b', '#2e9d4f', '#8e44ad'].map(c => `<span class="ik-dot sm" data-tc="${c}" style="background:${c}"></span>`).join('')}
      ${old ? '<button data-tdel aria-label="Delete this text">Delete</button>' : ''}<button data-tok class="ok" aria-label="Done">✓</button></div>
    <textarea class="ink-text" rows="1" spellcheck="false" placeholder="Type, or write with the keyboard's handwriting"></textarea>`;
  host.appendChild(wrap);
  const ta = wrap.querySelector('textarea');
  const look = () => { ta.style.color = style.c; ta.style.fontWeight = style.b ? 700 : 400; ta.style.fontSize = (style.size * s.unitPerPx() * k) + 'px'; ta.style.height = 'auto'; ta.style.height = ta.scrollHeight + 'px'; ta.style.width = '0px'; ta.style.width = Math.max(200, Math.min(Math.max(220, host.clientWidth - css[0] - 16), ta.scrollWidth + 28)) + 'px'; };
  ta.value = old ? old.t : ''; look();
  setTimeout(() => { ta.focus({ preventScroll: true }); ta.setSelectionRange(ta.value.length, ta.value.length); }, 30);
  let closed = false;
  const finish = (keep = true, del = false) => {
    if (closed) return; closed = true;
    const t = ta.value.replace(/\s+$/, ''); wrap.remove();
    const i = old ? s.objs.indexOf(old) : -1;
    if (old && !keep) { delete old.hidden; s.render(); return; }
    if (old && (del || !t)) { s.snapshot(); s.objs.splice(i, 1); }
    else if (old) { s.snapshot(); old.t = t; old.c = style.c; old.b = style.b; old.s = style.size * s.unitPerPx(); delete old.hidden; }
    else if (keep && t) { s.snapshot(); const o = { type: 'text', t, c: style.c, s: style.size * s.unitPerPx(), b: style.b, pts: [at] }; if (isOv(st, s)) o.a = s.anchorFor(at); s.objs.push(o); }
    if (s.data && s.trim) { const b = s.objs.reduce((m, o) => Math.max(m, objBox(o)[3]), 0); if (b > (s.data.h || SPACE) - 6) { s.data.h = Math.ceil((b + 20) / (SPACE / 2)) * (SPACE / 2); s.fit(); } }
    s.render(); if (!isOv(st, s)) drawChevrons(); markDirty();
  };
  wrap.querySelectorAll('.ink-txbar button, .ink-txbar .ik-dot').forEach(b => b.addEventListener('pointerdown', e => { e.preventDefault(); e.stopPropagation(); }));
  wrap.querySelectorAll('[data-tz]').forEach(b => b.onclick = () => { style.size = Math.max(9, Math.min(48, style.size + 2 * +b.dataset.tz)); look(); ta.focus(); });
  wrap.querySelector('[data-tb]').onclick = () => { style.b = !style.b; look(); ta.focus(); };
  wrap.querySelectorAll('[data-tc]').forEach(d => d.onclick = () => { style.c = d.dataset.tc; look(); ta.focus(); });
  wrap.querySelector('[data-tok]').onclick = () => finish(true);
  const td = wrap.querySelector('[data-tdel]'); if (td) td.onclick = () => finish(true, true);
  ta.addEventListener('input', look);
  ta.addEventListener('keydown', ev => { ev.stopPropagation(); if (ev.key === 'Escape') finish(false); });
  ta.addEventListener('blur', () => setTimeout(() => { if (!wrap.contains(document.activeElement)) finish(true); }, 150));
  wrap.addEventListener('click', e => e.stopPropagation());
  wrap.addEventListener('pointerdown', e => e.stopPropagation());
}

function toggleRoom(key) {
  const st = cur; if (!st) return;
  if (st.open.has(key)) {
    const r = st.rooms.get(key);
    if (r && writing) { r.trim(); st.open.delete(key); }
    else if (r && r.wrap.classList.contains('peek')) { r.wrap.classList.remove('peek'); r.wrap.dataset.opened = '1'; st.overlay.relayout(); return; }
    else st.open.delete(key);
  } else { st.open.add(key); if (!st.rec.rooms[key]) st.rec.rooms[key] = { h: SPACE, objs: [] }; }
  drawRooms(); st.overlay.relayout();
}
function drawRooms() {
  const st = cur;
  st.box.querySelectorAll('.rm-hold').forEach(h => {
    const key = h.dataset.for, want = st.open.has(key);
    let r = st.rooms.get(key);
    if (!want) { if (r) { r.wrap.remove(); st.rooms.delete(key); if (st.last === r) st.last = null; } const d = st.rec.rooms[key]; if (d && !(d.objs && d.objs.length)) delete st.rec.rooms[key]; return; }
    if (!r) { r = makeRoom(h, key, st.rec.rooms[key], () => markDirty()); st.rooms.set(key, r); wireSurface(r); }
    const has = r.objs.length > 0;
    r.wrap.classList.toggle('peek', has && !writing && !r.wrap.dataset.opened); r.wrap.classList.toggle('writing', writing); r.cv.style.pointerEvents = writing ? 'auto' : 'none';
    r.wrap.onclick = () => { if (!writing && r.wrap.classList.contains('peek')) { r.wrap.classList.remove('peek'); r.wrap.dataset.opened = '1'; st.overlay.relayout(); } };
    r.render(); r.showLess();
  });
  drawChevrons();
}
function drawChevrons() {
  const st = cur; if (!st) return;
  st.box.querySelectorAll('.sp.rm-l').forEach(c => { const d = st.rec.rooms[c.dataset.rk]; c.classList.toggle('open', st.open.has(c.dataset.rk)); c.classList.toggle('has', !!(d && d.objs && d.objs.length)); });
  st.box.querySelectorAll('.rm-chev').forEach(c => {
    const d = st.rec.rooms[c.dataset.rk], has = !!(d && d.objs && d.objs.length);
    c.classList.toggle('open', st.open.has(c.dataset.rk));
    if (c.classList.contains('has') !== has || !c.innerHTML) { c.classList.toggle('has', has); c.innerHTML = has ? PEN : CHEV; }
  });
}
function selAction(a, v) {
  const st = cur, s = st && st.last; if (!s || !s.sel) return;
  const ids = s.sel.ids.filter(i => s.objs[i]);
  if (a === 'del' || a === 'cut') { if (a === 'cut') copySel(s); s.snapshot(); const set = new Set(ids); s.objs.splice(0, s.objs.length, ...s.objs.filter((o, i) => !set.has(i))); s.sel = null; if (a === 'cut') toast('Cut to the clipboard · open it from the strip, pick the item, then tap where it goes'); }
  else if (a === 'xfer') {
    // move the selected marks to the other side, keeping their shape; they land at the top of what that side shows now
    const to = ovs(st).find(o => o !== s); if (!to || !isOv(st, s)) return;
    const bb = ids.map(i => objBox(s.objs[i])).reduce((m, q) => [Math.min(m[0], q[0]), Math.min(m[1], q[1]), Math.max(m[2], q[2]), Math.max(m[3], q[3])]);
    const r1 = s.cv.getBoundingClientRect(), k1 = r1.width / (s.cv.clientWidth || 1), pr = to.parentEl.getBoundingClientRect();
    const dx = pr.left + 40 - (r1.left + bb[0] * k1), dy = pr.top + 60 - (r1.top + bb[1] * k1);
    const conv = q => { const u = to.toUnits(r1.left + q[0] * k1 + dx, r1.top + q[1] * k1 + dy); return q.length > 2 ? [u[0], u[1], q[2]] : u; };
    const f = to.unitPerPx() * k1, moved = ids.map(i => JSON.parse(JSON.stringify(s.objs[i])));
    to.snapshot(); s.snapshot();
    for (const o of moved) { o.pts = o.pts.map(conv); if (o.rects) o.rects = o.rects.map(r => { const p0 = conv([r[0], r[1]]), p1 = conv([r[2], r[1]]); return [p0[0], p0[1], p1[0], r[3] * f]; }); if (o.s) o.s *= f; if (o.h) o.h *= f; if (o.r) o.r *= f; delete o.tr; delete o.a; o.a = to.anchorFor(o.pts[0]); to.objs.push(o); }
    const gone = new Set(ids); s.objs.splice(0, s.objs.length, ...s.objs.filter((o, i) => !gone.has(i)));
    s.sel = null; to.sel = { ids: moved.map((_, j) => to.objs.length - moved.length + j) }; st.last = to; to.render();
    toast(to === st.overlayX ? 'Moved to Explain' : 'Moved to the card · drag it where you want');
  }
  else if (a === 'unclear') {
    // the words under the selected marks: snapped highlights keep their exact words; other marks take the lines they touch
    const r0 = s.cv.getBoundingClientRect(), sc = s.cv.clientWidth / (r0.width || 1), out = new Set();
    for (const i of ids) {
      const o = s.objs[i];
      if (o.tr) { const el = s.parentEl.querySelector(`[data-ak="${o.tr.ak}"]`); if (el) out.add(el.textContent.slice(Math.min(o.tr.s, o.tr.e), Math.max(o.tr.s, o.tr.e)).replace(/\s+/g, ' ').trim()); continue; }
      const bb = objBox(o);
      s.parentEl.querySelectorAll('.xv > p, .xv li, .xv-part').forEach(el => { const q = el.getBoundingClientRect(), y0 = (q.top - r0.top) * sc, y1 = (q.bottom - r0.top) * sc; if (y1 > bb[1] && y0 < bb[3]) out.add(el.textContent.replace(/\s+/g, ' ').trim()); });
    }
    const texts = [...out].filter(Boolean);
    if (texts.length && st.opts.onUnclear) { st.opts.onUnclear(texts); toast('Saved to “Still unclear” · the next rewrite of this deck expands it'); } else toast('Select a highlight or a mark over the explanation first.');
    s.sel = null;
  }
  else if (a === 'copy') { copySel(s); toast('Copied to the clipboard · open it from the strip, pick the item, then tap where it goes'); }
  else if (a === 'colour') { s.snapshot(); for (const i of ids) s.objs[i].c = v; }
  else if (a === 'width') { s.snapshot(); for (const i of ids) { const o = s.objs[i]; if (o.type === 'hl' && o.snap) { o.h *= v; if (o.rects) o.rects = o.rects.map(r => [r[0], r[1], r[2], r[3] * v]); } else if (o.s) o.s = Math.max(0.3, o.s * v); } }
  else s.sel = null;
  s.render(); if (!isOv(st, s)) drawChevrons(); markDirty(); if (st.toolbar) st.toolbar.draw();
}
function toast(msg) {
  const t = document.createElement('div'); t.className = 'ik-toast'; t.textContent = msg; document.body.appendChild(t);
  setTimeout(() => t.classList.add('out'), 2600); setTimeout(() => t.remove(), 3100);
}
function applyMode() {
  const st = cur; if (!st) return;
  st.box.classList.toggle('inking', writing); if (st.xbox) st.xbox.classList.toggle('inking', writing);
  [...ovs(st), ...st.rooms.values()].forEach(s => { s.cv.style.pointerEvents = writing ? 'auto' : 'none'; s.render(); });
  st.rooms.forEach(r => { r.wrap.classList.toggle('peek', r.objs.length > 0 && !writing && !r.wrap.dataset.opened); r.wrap.classList.toggle('writing', writing); });
  const host = st.opts.toolbarHost();
  if (st.toolbar) { st.toolbar.destroy(); st.toolbar = null; }
  if (writing && host && !quiet) {
    host.hidden = false;
    st.toolbar = new Toolbar(host, {
      undo: () => { const s = st.last || st.overlay; s.doUndo(); markDirty(); },
      redo: () => { const s = st.last || st.overlay; s.doRedo(); markDirty(); },
      done: () => setWriting(false),
      clear: () => { const s = st.last || st.overlay; s.snapshot(); s.objs.splice(0); s.sel = null; s.render(); markDirty(); },
      toolChanged: () => { pasting = null; [...ovs(st), ...st.rooms.values()].forEach(s => { s.sel = null; s.render(); }); },
      hasSel: () => !!(st.last && st.last.sel && st.last.sel.ids.length),
      selOnExplain: () => !!(st.overlayX && st.last === st.overlayX),
      canXfer: () => !!(st.overlayX && isOv(st, st.last)), xferLabel: () => st.last === st.overlayX ? '→ Move to card' : '→ Move to Explain',
      pin: st.opts.pin || null, docked: st.opts.docked || null,
      clips: () => readClips(), pasting: () => pasting, setPasting: v => { pasting = v || null; },
      removeClip: id => { saveClips(readClips().filter(c => c.id !== id)); if (pasting === id) pasting = null; },
      clearClips: () => { saveClips([]); pasting = null; },
      selAction
    });
    if (st.overlay.hiddenFromOther) toast('Ink written before this update on another screen size is hidden here. New ink and rooms show on every screen.');
  } else if (host) { showFab(host); }
  if (st.opts.modeChanged) st.opts.modeChanged(writing);
}
// not writing: one small round pen button floating at the screen edge (drag it anywhere; it never sits in the card's layout)
function showFab(host) {
  host.hidden = false; host.classList.add('ik-float');
  host.innerHTML = `<button class="ik-fab" data-ink-fab aria-label="Write on this card with the S Pen" title="Write on this card (drag to move)">${INK_ICONS.fab}</button>`;
  placeFloat(host, railSize());
  dragFloat(host, host.querySelector('[data-ink-fab]'), () => { quiet = false; setWriting(true); });
}
export function setWriting(on) {
  const was = writing; writing = !!on; if (!writing) pasting = null;
  if (cur) {
    if (was && !writing) { cur.box.querySelectorAll('.ink-tx textarea').forEach(t => t.blur()); cur.rooms.forEach(r => r.trim()); }  // done: every room shrinks to what it uses
    [...ovs(cur), ...cur.rooms.values()].forEach(s => { s.sel = null; });
    drawRooms(); applyMode(); ovs(cur).forEach(o => o.relayout());
  } else if (listeners.changed) listeners.changed(writing);
}
function markDirty() { const st = cur; if (!st) return; st.dirty = true; clearTimeout(st.t); st.t = setTimeout(() => flushInk(), 700); }
export async function flushInk() {
  const st = cur; if (!st || !st.dirty) return;
  st.dirty = false; clearTimeout(st.t);
  st.rec.ov[st.face] = st.overlay.serialise();
  if (st.overlayX) st.rec.ov[st.xface] = st.overlayX.serialise();
  for (const [k, d] of Object.entries(st.rec.rooms)) if (!(d.objs && d.objs.length) && !st.open.has(k)) delete st.rec.rooms[k];
  await saveInk(st.card, st.rec);
}
export function unmountInk() {
  const st = cur;
  if (st) { st.rooms.forEach(r => r.trim()); if (st.toolbar) st.toolbar.destroy(); const h = st.opts && st.opts.toolbarHost && st.opts.toolbarHost(); if (h) { h.hidden = true; h.innerHTML = ''; } }
  flushInk(); cur = null;
}
