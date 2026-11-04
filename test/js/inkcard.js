// Ink on a Flow card: the overlay (write anywhere on either side) and rooms that open under any line.
// The overlay is kept relative to the block it was written on (and highlights snapped to text keep their words),
// so it survives a narrower split-screen window, a bigger text size or a room opening above it.
import { Surface, Toolbar, attachPointer, loadInk, saveInk, settings, INK_ICONS, shiftObj, scaleObj, objBox, placeFloat, dragFloat, railSize } from './ink.js';

const ROOM_W = 1000;                       // rooms use their own units: 1000 = the room's width
const SPACE = 180;                         // one "space" of a room, in room units
const CLIP_KEY = 'trace.ink.clips', OLD_CLIP = 'trace.ink.clip', CLIP_MAX = 12;
let cur = null;                            // { card, face, rec, overlay, rooms:Map, toolbar, ... }
let writing = false, pasting = null;          // pasting = id of the clipboard item waiting to be placed
const listeners = { changed: null };
export const isWriting = () => writing;

function anchorsOf(box) {
  const els = [...box.querySelectorAll('.c-head, .c-tags, .qh, .qr > *, .qr li, .c-title, .qrecap, .ans > *, .ans li, .box, .bx > p, .bx li, .hook, .rm')];
  els.forEach((e, i) => { if (!e.dataset.ak) e.dataset.ak = (e.classList.contains('rm') ? 'rm:' + e.dataset.room : 'b' + i); });
  return els;
}
function lineEls(box) {
  const out = [];
  const add = (el, sec, i) => out.push({ el, key: sec + ':' + i });
  box.querySelectorAll('.ans > p, .ans > ul > li, .ans > ol > li, .ans > table').forEach((el, i) => add(el, 'ans', i));
  box.querySelectorAll('.box').forEach(b => {
    const sec = ['why', 'watch', 'qlines', 'qcross', 'note'].find(c => b.classList.contains(c)) || 'box';
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
    let best = 'top', by = -Infinity;
    for (const [k, g] of Object.entries(geo)) if (k !== 'top' && !k.startsWith('rm:') && g[1] <= y + 1 && g[1] > by) { best = k; by = g[1]; }
    return best;
  };
  // saved form: points relative to the block's top-left, with the block's size at the time
  const toRel = o => {
    const a = (o.a && geo[o.a]) ? o.a : anchorFor(o.pts[0][0], o.pts[0][1]), g = geo[a];
    const c = { ...o, a, g: [g[2], g[3]], pts: o.pts.map(q => q.length > 2 ? [q[0] - g[0], q[1] - g[1], q[2]] : [q[0] - g[0], q[1] - g[1]]) };
    if (o.rects) c.rects = o.rects.map(r => [r[0] - g[0], r[1] - g[1], r[2] - g[0], r[3]]);
    delete c.hidden; return c;
  };
  // back to this screen: stretch with the block (width) and with its height for marks inside it
  const fx = (o, g) => { const fw = o.g && o.g[0] ? g[2] / o.g[0] : 1, oh = o.g ? o.g[1] : 0; return [v => g[0] + v * fw, v => g[1] + (oh && v <= oh ? v * g[3] / oh : (oh ? v - oh + g[3] : v))]; };
  const toAbs = o => {
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
    o.rects = b; o.pts = [[b[0][0], b[0][1]], [b[b.length - 1][2], b[b.length - 1][1]]]; o.h = b[0][3];
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
  wrap.appendChild(cv); wrap.appendChild(more); holder.appendChild(wrap);
  wrap.addEventListener('click', e => { if (writing) { e.stopPropagation(); } });
  const kNow = () => (cv.clientWidth || wrap.clientWidth || ROOM_W) / ROOM_W;
  const fit = () => { cv.style.height = Math.round((data.h || SPACE) * kNow()) + 'px'; };
  fit();
  const map = () => { const k = kNow(); return { X: p => p[0] * k, Y: p => p[1] * k, k }; };
  const s = new Surface(cv, data.objs || (data.objs = []), { map, changed: () => {}, limits: () => writing });
  s.toUnits = (x, y) => { const r = cv.getBoundingClientRect(), sc = cv.clientWidth / (r.width || 1), k = kNow(); return [(x - r.left) * sc / k, (y - r.top) * sc / k]; };
  s.unitPerPx = () => { const r = cv.getBoundingClientRect(); return (cv.clientWidth / (r.width || 1)) / kNow(); };
  // ⌄ at the end of the room: one more full space. After writing, the room trims to what was used (in half spaces).
  more.onpointerdown = e => e.stopPropagation();
  more.onclick = e => { e.stopPropagation(); e.preventDefault(); data.h = (data.h || SPACE) + SPACE; fit(); s.render(); onChange(true); if (cur) { cur.last = s; cur.overlay.relayout(); } };
  s.trim = () => {
    if (!s.objs.length) return false;
    const used = s.objs.reduce((m, o) => { const b = objBox(o); return Math.max(m, b[3] + (o.type === 'text' ? 0 : (o.s || o.h || 0) / 2)); }, 0);
    const h = Math.max(SPACE / 2, Math.ceil((used + 6) / (SPACE / 2)) * (SPACE / 2));
    if (h === data.h) return false;
    data.h = h; fit(); s.render(); onChange(true); return true;
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
document.addEventListener('contextmenu', e => { if (writing && cur && cur.box.contains(e.target)) e.preventDefault(); }, true);
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
  for (const src of c.objs) { const o = JSON.parse(JSON.stringify(src)); scaleObj(o, f); shiftObj(o, p[0], p[1]); if (s === cur.overlay) o.a = s.anchorFor(o.pts[0]); s.objs.push(o); }
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
  const st = { card, face, rec, box, rooms: new Map(), open: new Set(Object.keys(rec.rooms || {}).filter(k => rec.rooms[k].objs && rec.rooms[k].objs.length)), last: null, dirty: false, t: null, opts };
  if (cur && cur.toolbar) cur.toolbar.destroy();
  cur = st;
  // chevrons and rooms beside every line (answer side)
  if (face === 'a') for (const { el, key } of lineEls(box)) {
    const has = rec.rooms[key] && rec.rooms[key].objs && rec.rooms[key].objs.length;
    el.classList.add('rm-line');
    const b = document.createElement('button'); b.type = 'button'; b.className = 'rm-chev' + (has ? ' has' : ''); b.dataset.rk = key;
    b.setAttribute('aria-label', has ? 'Show or hide your note under this line' : 'Open room to write under this line');
    b.innerHTML = has ? PEN : CHEV;
    el.appendChild(b);
    const holder = document.createElement('div'); holder.className = 'rm-hold'; holder.dataset.for = key;
    if (el.tagName === 'LI') el.appendChild(holder); else el.after(holder);
    b.onclick = e => { e.stopPropagation(); e.preventDefault(); toggleRoom(key); };
  }
  st.overlay = makeOverlay(box, rec, face);
  wireSurface(st.overlay);
  drawRooms();
  st.overlay.relayout();
  applyMode();
  let lastW = box.clientWidth;
  new ResizeObserver(() => { if (cur !== st) return; st.rooms.forEach(r => { r.fit(); r.render(); }); st.overlay.relayout(); if (Math.abs(box.clientWidth - lastW) > 2) lastW = box.clientWidth; }).observe(box);
}
const PEN = '<svg viewBox="0 0 24 24"><path d="M14.6 4.6l4.8 4.8L9 19.8l-5.3.9.9-5.3z"/></svg>', CHEV = '<svg viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>';
function wireSurface(s) {
  const st = cur;
  attachPointer(s, {
    writing: () => writing, toUnits: s.toUnits, unitPerPx: s.unitPerPx, map: () => s.o.map(), snapLine: s.snapLine || null, snapUpdate: s.snapUpdate || null,
    scrollBy: dy => { st.box.scrollTop += dy; },
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
    changed: o => { st.last = s; if (o && s === st.overlay && !o.a) o.a = s.anchorFor(o.pts[0]); if (s !== st.overlay) drawChevrons(); markDirty(); }
  });
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
    else if (keep && t) { s.snapshot(); const o = { type: 'text', t, c: style.c, s: style.size * s.unitPerPx(), b: style.b, pts: [at] }; if (s === st.overlay) o.a = s.anchorFor(at); s.objs.push(o); }
    if (s.data && s.trim) { const b = s.objs.reduce((m, o) => Math.max(m, objBox(o)[3]), 0); if (b > (s.data.h || SPACE) - 6) { s.data.h = Math.ceil((b + 20) / (SPACE / 2)) * (SPACE / 2); s.fit(); } }
    s.render(); if (s !== st.overlay) drawChevrons(); markDirty();
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
    r.render();
  });
  drawChevrons();
}
function drawChevrons() {
  const st = cur; if (!st) return;
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
  else if (a === 'copy') { copySel(s); toast('Copied to the clipboard · open it from the strip, pick the item, then tap where it goes'); }
  else if (a === 'colour') { s.snapshot(); for (const i of ids) s.objs[i].c = v; }
  else if (a === 'width') { s.snapshot(); for (const i of ids) { const o = s.objs[i]; if (o.type === 'hl' && o.snap) { o.h *= v; if (o.rects) o.rects = o.rects.map(r => [r[0], r[1], r[2], r[3] * v]); } else if (o.s) o.s = Math.max(0.3, o.s * v); } }
  else s.sel = null;
  s.render(); if (s !== st.overlay) drawChevrons(); markDirty(); if (st.toolbar) st.toolbar.draw();
}
function toast(msg) {
  const t = document.createElement('div'); t.className = 'ik-toast'; t.textContent = msg; document.body.appendChild(t);
  setTimeout(() => t.classList.add('out'), 2600); setTimeout(() => t.remove(), 3100);
}
function applyMode() {
  const st = cur; if (!st) return;
  st.box.classList.toggle('inking', writing);
  [st.overlay, ...st.rooms.values()].forEach(s => { s.cv.style.pointerEvents = writing ? 'auto' : 'none'; s.render(); });
  st.rooms.forEach(r => { r.wrap.classList.toggle('peek', r.objs.length > 0 && !writing && !r.wrap.dataset.opened); r.wrap.classList.toggle('writing', writing); });
  const host = st.opts.toolbarHost();
  if (st.toolbar) { st.toolbar.destroy(); st.toolbar = null; }
  if (writing && host) {
    host.hidden = false;
    st.toolbar = new Toolbar(host, {
      undo: () => { const s = st.last || st.overlay; s.doUndo(); markDirty(); },
      redo: () => { const s = st.last || st.overlay; s.doRedo(); markDirty(); },
      done: () => setWriting(false),
      clear: () => { const s = st.last || st.overlay; s.snapshot(); s.objs.splice(0); s.sel = null; s.render(); markDirty(); },
      toolChanged: () => { pasting = null; [st.overlay, ...st.rooms.values()].forEach(s => { s.sel = null; s.render(); }); },
      hasSel: () => !!(st.last && st.last.sel && st.last.sel.ids.length),
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
  dragFloat(host, host.querySelector('[data-ink-fab]'), () => setWriting(true));
}
export function setWriting(on) {
  const was = writing; writing = !!on; if (!writing) pasting = null;
  if (cur) {
    if (was && !writing) { cur.box.querySelectorAll('.ink-tx textarea').forEach(t => t.blur()); cur.rooms.forEach(r => r.trim()); }  // done: every room shrinks to what it uses
    [cur.overlay, ...cur.rooms.values()].forEach(s => { s.sel = null; });
    drawRooms(); applyMode(); cur.overlay.relayout();
  } else if (listeners.changed) listeners.changed(writing);
}
function markDirty() { const st = cur; if (!st) return; st.dirty = true; clearTimeout(st.t); st.t = setTimeout(() => flushInk(), 700); }
export async function flushInk() {
  const st = cur; if (!st || !st.dirty) return;
  st.dirty = false; clearTimeout(st.t);
  st.rec.ov[st.face] = st.overlay.serialise();
  for (const [k, d] of Object.entries(st.rec.rooms)) if (!(d.objs && d.objs.length) && !st.open.has(k)) delete st.rec.rooms[k];
  await saveInk(st.card, st.rec);
}
export function unmountInk() {
  const st = cur;
  if (st) { st.rooms.forEach(r => r.trim()); if (st.toolbar) st.toolbar.destroy(); const h = st.opts && st.opts.toolbarHost && st.opts.toolbarHost(); if (h) { h.hidden = true; h.innerHTML = ''; } }
  flushInk(); cur = null;
}
