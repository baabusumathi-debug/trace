// Ink on a Flow card: the overlay (write anywhere on either side, this screen's layout only) and rooms under lines.
import { Surface, Toolbar, attachPointer, loadInk, saveInk, settings, INK_ICONS } from './ink.js';

const ROOM_W = 1000;                       // rooms use their own units: 1000 = the room's width
let cur = null;                            // { card, face, rec, overlay, rooms:Map, toolbar, ... }
let writing = false;
const listeners = { changed: null };
export const isWriting = () => writing;

function anchorsOf(box) {
  const els = [...box.querySelectorAll('.c-head, .c-tags, .qh, .qr > *, .c-title, .qrecap, .ans > *, .ans li, .box, .bx > p, .bx li, .hook, .rm')];
  els.forEach((e, i) => { if (!e.dataset.ak) e.dataset.ak = (e.classList.contains('rm') ? 'rm:' + e.dataset.room : 'b' + i); });
  return els;
}
function lineEls(box) {
  const out = [];
  const add = (el, sec, i) => out.push({ el, key: sec + ':' + i });
  box.querySelectorAll('.ans > p, .ans > ul > li, .ans > table').forEach((el, i) => add(el, 'ans', i));
  box.querySelectorAll('.box').forEach(b => {
    const sec = ['why', 'watch', 'qlines', 'qcross', 'note'].find(c => b.classList.contains(c)) || 'box';
    b.querySelectorAll('.bx > p, .bx > ul > li').forEach((el, i) => add(el, sec, i));
  });
  return out;
}

/* ---------- the overlay: absolute coordinates during the session, saved relative to the block above ---------- */
function makeOverlay(box, rec, face) {
  const cv = document.createElement('canvas'); cv.className = 'ink-ov';
  box.appendChild(cv);
  cv.addEventListener('click', e => { if (writing) { e.stopPropagation(); e.preventDefault(); } });
  const cs = getComputedStyle(box).getPropertyValue('--cs') || '1';
  const saved = rec.ov[face];
  const w = box.clientWidth;
  const sameScreen = !saved || (Math.abs((saved.w || w) - w) / w < 0.06 && String(saved.cs || cs).trim() === String(cs).trim());
  let tops = {};
  const measure = () => {
    const r = cv.getBoundingClientRect(), sc = cv.clientWidth / (r.width || 1), t = {};
    anchorsOf(box).forEach(e => { t[e.dataset.ak] = (e.getBoundingClientRect().top - r.top) * sc; });
    t.top = 0; return t;
  };
  const size = () => { cv.style.width = box.scrollWidth + 'px'; cv.style.height = '0px'; cv.style.height = box.scrollHeight + 'px'; };
  size(); tops = measure();
  const toAbs = o => ({ ...o, pts: o.pts.map(q => [q[0], q[1] + (tops[o.a] != null ? tops[o.a] : 0), q[2]]) });
  const objs = sameScreen && saved ? saved.objs.map(toAbs) : [];
  const hiddenFromOther = !sameScreen && saved && saved.objs.length;
  const map = () => ({ X: p => p[0], Y: p => p[1], k: 1 });
  const s = new Surface(cv, objs, { map, changed: () => {} });
  const anchorFor = y => { let best = 'top', by = -Infinity; for (const [k, v] of Object.entries(tops)) if (v <= y + 1 && v > by) { best = k; by = v; } return best; };
  s.relayout = () => {
    const old = tops; size(); tops = measure();
    for (const o of s.objs) { const a = o.a || 'top'; const d = (tops[a] != null && old[a] != null) ? tops[a] - old[a] : 0; if (d) o.pts = o.pts.map(q => [q[0], q[1] + d, q[2]]); }
    s.render();
  };
  s.serialise = () => ({ w: box.clientWidth, cs: String(cs).trim(), objs: s.objs.map(o => { const a = o.a || anchorFor(o.pts[0][1]); return { ...o, a, pts: o.pts.map(q => [q[0], q[1] - (tops[a] || 0), q[2]]) }; }) });
  s.anchorFor = anchorFor; s.hiddenFromOther = hiddenFromOther;
  s.toUnits = (x, y) => { const r = cv.getBoundingClientRect(), sc = cv.clientWidth / (r.width || 1); return [(x - r.left) * sc, (y - r.top) * sc]; };
  s.unitPerPx = () => { const r = cv.getBoundingClientRect(); return cv.clientWidth / (r.width || 1); };
  s.snapLine = e => {
    const pe = cv.style.pointerEvents; cv.style.pointerEvents = 'none';
    const rg = document.caretRangeFromPoint ? document.caretRangeFromPoint(e.clientX, e.clientY) : null;
    cv.style.pointerEvents = pe;
    if (!rg || !box.contains(rg.startContainer)) return null;
    const rects = [...rg.getClientRects()]; const rr = rects[0] || (rg.startContainer.parentElement && rg.startContainer.parentElement.getBoundingClientRect());
    if (!rr || !rr.height || rr.height > 60 || e.clientY < rr.top - 6 || e.clientY > rr.bottom + 6) return null;
    const r = cv.getBoundingClientRect(), sc = cv.clientWidth / (r.width || 1);
    return { y: (rr.top + rr.height / 2 - r.top) * sc, h: rr.height * sc * 0.92 };
  };
  s.scrollBy = dy => { box.scrollTop += dy; };
  return s;
}

/* ---------- rooms ---------- */
function makeRoom(holder, key, data, onChange) {
  const wrap = document.createElement('div'); wrap.className = 'rm'; wrap.dataset.room = key;
  const cv = document.createElement('canvas'); cv.className = 'rm-cv';
  wrap.appendChild(cv); holder.appendChild(wrap);
  wrap.addEventListener('click', e => { if (writing) { e.stopPropagation(); } });
  const kNow = () => cv.clientWidth / ROOM_W;
  const fit = () => { cv.style.height = Math.round((data.h || 180) * kNow()) + 'px'; };
  fit();
  const map = () => { const k = kNow(); return { X: p => p[0] * k, Y: p => p[1] * k, k }; };
  const s = new Surface(cv, data.objs || (data.objs = []), { map, changed: () => {} });
  s.toUnits = (x, y) => { const r = cv.getBoundingClientRect(), sc = cv.clientWidth / (r.width || 1), k = kNow(); return [(x - r.left) * sc / k, (y - r.top) * sc / k]; };
  s.unitPerPx = () => { const r = cv.getBoundingClientRect(); return (cv.clientWidth / (r.width || 1)) / kNow(); };
  s.grow = () => { const maxY = s.objs.reduce((m, o) => Math.max(m, ...o.pts.map(q => q[1])), 0); if (maxY > (data.h || 180) - 70) { data.h = Math.ceil((maxY + 200) / 50) * 50; fit(); s.render(); onChange(true); } };
  s.wrap = wrap; s.data = data; s.fit = fit;
  return s;
}

/* ---------- mount on the current card face ---------- */
export async function mountInk(cardEl, card, face, opts) {
  await flushInk();
  const box = cardEl.querySelector(face === 'q' ? '.c-q' : '.c-a'); if (!box) { cur = null; return; }
  const rec = await loadInk(card);
  if (!document.body.contains(box)) return;
  const st = { card, face, rec, box, rooms: new Map(), open: new Set(Object.keys(rec.rooms || {}).filter(k => rec.rooms[k].objs && rec.rooms[k].objs.length)), last: null, dirty: false, t: null, opts };
  cur = st;
  // chevrons and rooms beside every line (answer side)
  if (face === 'a') for (const { el, key } of lineEls(box)) {
    const has = rec.rooms[key] && rec.rooms[key].objs && rec.rooms[key].objs.length;
    el.classList.add('rm-line');
    const b = document.createElement('button'); b.type = 'button'; b.className = 'rm-chev' + (has ? ' has' : ''); b.dataset.rk = key;
    b.setAttribute('aria-label', has ? 'Show or hide your note under this line' : 'Open room to write under this line');
    b.innerHTML = has ? '<svg viewBox="0 0 24 24"><path d="M4 20l2-6 9.5-9.5a2 2 0 0 1 2.8 0l1.2 1.2a2 2 0 0 1 0 2.8L10 18z"/></svg>' : '<svg viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>';
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
  new ResizeObserver(() => { if (cur === st) { st.rooms.forEach(r => { r.fit(); r.render(); }); st.overlay.relayout(); } }).observe(box);
}
function wireSurface(s) {
  const st = cur;
  attachPointer(s, {
    writing: () => writing, toUnits: s.toUnits, unitPerPx: s.unitPerPx, map: () => s.o.map(), snapLine: s.snapLine || null,
    scrollBy: dy => { st.box.scrollTop += dy; },
    selChanged: () => { st.last = s; if (st.toolbar) st.toolbar.draw(); },
    onDown: () => { if (st.toolbar) st.toolbar.closePop(); },
    textAt: (p, e) => textAt(s, p, e),
    changed: o => { st.last = s; if (o && s === st.overlay && !o.a) o.a = s.anchorFor(o.pts[0][1]); if (s.grow) s.grow(); if (s !== st.overlay) drawChevrons(); markDirty(); }
  });
  s.cv.addEventListener('pointerdown', () => { st.last = s; }, true);
}
function textAt(s, p, e) {
  const S = settings(), inp = document.createElement('textarea');
  inp.className = 'ink-text'; inp.rows = 1; inp.style.left = e.clientX + 'px'; inp.style.top = e.clientY + 'px';
  inp.style.color = S.text.color; inp.style.fontSize = S.text.size + 'px'; inp.style.fontWeight = S.text.bold ? 700 : 400;
  document.body.appendChild(inp); setTimeout(() => inp.focus(), 30);
  const done = () => { const t = inp.value.trim(); inp.remove(); if (!t) return; s.snapshot(); const o = { type: 'text', t, c: S.text.color, s: S.text.size * s.unitPerPx(), b: S.text.bold, pts: [p] }; if (s === cur.overlay) o.a = s.anchorFor(p[1]); s.objs.push(o); s.render(); if (s.grow) s.grow(); markDirty(); };
  inp.addEventListener('keydown', ev => { ev.stopPropagation(); if (ev.key === 'Enter' && !ev.shiftKey) { ev.preventDefault(); inp.blur(); } if (ev.key === 'Escape') { inp.value = ''; inp.blur(); } });
  inp.addEventListener('blur', done, { once: true });
}
function toggleRoom(key) {
  const st = cur; if (!st) return;
  if (st.open.has(key)) {
    const r = st.rooms.get(key);
    if (r && writing) { st.open.delete(key); }                          // writing: close it (ink is kept)
    else if (r && r.wrap.classList.contains('peek')) { r.wrap.classList.remove('peek'); return; }
    else st.open.delete(key);
  } else { st.open.add(key); if (!st.rec.rooms[key]) st.rec.rooms[key] = { h: 180, objs: [] }; }
  drawRooms(); st.overlay.relayout();
}
function drawRooms() {
  const st = cur;
  st.box.querySelectorAll('.rm-hold').forEach(h => {
    const key = h.dataset.for, want = st.open.has(key);
    let r = st.rooms.get(key);
    if (!want) { if (r) { r.wrap.remove(); st.rooms.delete(key); } const d = st.rec.rooms[key]; if (d && !(d.objs && d.objs.length)) delete st.rec.rooms[key]; return; }
    if (!r) { r = makeRoom(h, key, st.rec.rooms[key], () => markDirty()); st.rooms.set(key, r); wireSurface(r); }
    const has = r.objs.length > 0;
    r.wrap.classList.toggle('peek', has && !writing && !r.wrap.dataset.opened);
    r.wrap.onclick = () => { if (!writing && r.wrap.classList.contains('peek')) { r.wrap.classList.remove('peek'); r.wrap.dataset.opened = '1'; st.overlay.relayout(); } };
    r.render();
    const chev = st.box.querySelector(`.rm-chev[data-rk="${CSS.escape(key)}"]`); if (chev) chev.classList.toggle('open', true);
  });
  const PEN = '<svg viewBox="0 0 24 24"><path d="M4 20l2-6 9.5-9.5a2 2 0 0 1 2.8 0l1.2 1.2a2 2 0 0 1 0 2.8L10 18z"/></svg>', CHEV = '<svg viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>';
  st.box.querySelectorAll('.rm-chev').forEach(c => {
    const d = st.rec.rooms[c.dataset.rk], has = !!(d && d.objs && d.objs.length);
    c.classList.toggle('open', st.open.has(c.dataset.rk));
    if (c.classList.contains('has') !== has || !c.innerHTML) { c.classList.toggle('has', has); c.innerHTML = has ? PEN : CHEV; }
  });
}
function drawChevrons() { const st = cur; if (!st) return; const PEN = '<svg viewBox="0 0 24 24"><path d="M4 20l2-6 9.5-9.5a2 2 0 0 1 2.8 0l1.2 1.2a2 2 0 0 1 0 2.8L10 18z"/></svg>', CHEV = '<svg viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>';
  st.box.querySelectorAll('.rm-chev').forEach(c => { const d = st.rec.rooms[c.dataset.rk], has = !!(d && d.objs && d.objs.length); if (c.classList.contains('has') !== has) { c.classList.toggle('has', has); c.innerHTML = has ? PEN : CHEV; } }); }
function applyMode() {
  const st = cur; if (!st) return;
  st.box.classList.toggle('inking', writing);
  [st.overlay, ...st.rooms.values()].forEach(s => { s.cv.style.pointerEvents = writing ? 'auto' : 'none'; s.render(); });
  st.rooms.forEach(r => { r.wrap.classList.toggle('peek', r.objs.length > 0 && !writing && !r.wrap.dataset.opened); r.wrap.classList.toggle('writing', writing); });
  const host = st.opts.toolbarHost();
  if (writing && host) {
    host.hidden = false;
    st.toolbar = new Toolbar(host, {
      undo: () => { const s = st.last || st.overlay; s.doUndo(); markDirty(); },
      redo: () => { const s = st.last || st.overlay; s.doRedo(); markDirty(); },
      done: () => setWriting(false),
      clear: () => { const s = st.last || st.overlay; s.snapshot(); s.objs.splice(0); s.sel = null; s.render(); markDirty(); },
      toolChanged: () => { [st.overlay, ...st.rooms.values()].forEach(s => { s.sel = null; s.render(); }); },
      hasSel: () => !!(st.last && st.last.sel && st.last.sel.ids.length),
      selAction: a => {
        const s = st.last; if (!s || !s.sel) return; const S = settings();
        if (a === 'del') { s.snapshot(); const ids = new Set(s.sel.ids); s.objs.splice(0, s.objs.length, ...s.objs.filter((o, i) => !ids.has(i))); s.sel = null; }
        else if (a === 'copy') { s.snapshot(); const add = s.sel.ids.map(i => { const o = JSON.parse(JSON.stringify(s.objs[i])); o.pts = o.pts.map(q => [q[0] + 14, q[1] + 14, q[2]]); return o; }); s.objs.push(...add); s.sel = { ids: add.map((_, j) => s.objs.length - add.length + j) }; }
        else if (a === 'style') { s.snapshot(); for (const i of s.sel.ids) { const o = s.objs[i]; if (o.type === 'hl') o.c = S.hl.color; else { o.c = S.pen.color; if (o.type === 'pen') { o.pen = S.pen.type; o.s = S.pen.size * s.unitPerPx(); } if (o.type === 'shape') o.s = S.pen.size * s.unitPerPx(); } } }
        else s.sel = null;
        s.render(); markDirty(); st.toolbar.draw();
      }
    });
    if (st.overlay.hiddenFromOther) { const n = document.createElement('div'); n.className = 'ik-note ik-warn'; n.textContent = 'Ink written on another screen size is hidden here. Rooms show on every screen.'; host.appendChild(n); }
  } else if (host) { st.toolbar = null; showFab(host); }
  if (st.opts.modeChanged) st.opts.modeChanged(writing);
}
// not writing: one small round pen button floating at the screen edge (it never sits on the card)
function showFab(host) {
  host.hidden = false; host.classList.add('ik-float'); host.classList.remove('ik-left');
  host.style.left = ''; host.style.top = ''; host.style.right = ''; host.style.transform = '';
  host.innerHTML = `<button class="ik-fab" data-ink-fab aria-label="Write on this card with the S Pen" title="Write on this card (S Pen)">${INK_ICONS.fab}</button>`;
  host.querySelector('[data-ink-fab]').onclick = e => { e.stopPropagation(); setWriting(true); };
}
export function setWriting(on) { writing = !!on; if (cur) { drawRooms(); applyMode(); cur.overlay.relayout(); } else if (listeners.changed) listeners.changed(writing); }
function markDirty() { const st = cur; if (!st) return; st.dirty = true; clearTimeout(st.t); st.t = setTimeout(() => flushInk(), 700); }
export async function flushInk() {
  const st = cur; if (!st || !st.dirty) return;
  st.dirty = false; clearTimeout(st.t);
  st.rec.ov[st.face] = st.overlay.serialise();
  for (const [k, d] of Object.entries(st.rec.rooms)) if (!(d.objs && d.objs.length) && !st.open.has(k)) delete st.rec.rooms[k];
  await saveInk(st.card, st.rec);
}
export function unmountInk() { const st = cur; flushInk(); if (st && st.opts && st.opts.toolbarHost) { const h = st.opts.toolbarHost(); if (h) { h.hidden = true; h.innerHTML = ''; } } cur = null; }
