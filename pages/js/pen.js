// S Pen on the study pages. Same engine as the cards (ink.js): pen, highlighter, eraser,
// lasso, shapes, undo/redo, side button erases. Pen writes, fingers scroll.
// Marks are kept per screen, on this device, in its own database.
import { db, useDbName } from './db.js';
import { Surface, Toolbar, attachPointer, settings, INK_ICONS, placeFloat, dragFloat, railSize } from './ink.js';
useDbName('trace-pages');

const PAGE = (location.pathname.split('/').pop() || 'page').replace('.html', '') || 'page';
let writing = false, cur = null, host = null, bar = null, dirty = false, timer = 0;

const viewNow = () => [...document.querySelectorAll('section.view')].find(v => !v.hidden) || null;
const bucket = () => Math.round((document.querySelector('main') || document.body).clientWidth / 40) * 40;
const keyOf = v => 'pen:' + PAGE + ':' + v.id + ':' + bucket();

function markDirty() { dirty = true; clearTimeout(timer); timer = setTimeout(flush, 700); }
async function flush() {
  if (!dirty || !cur) return;
  dirty = false; clearTimeout(timer);
  try { await db.kv.set(cur.key, { objs: cur.s.objs, ts: Date.now() }); } catch (e) { /* private mode */ }
}

function sizeTo(view, cv) {
  cv.style.width = view.clientWidth + 'px';
  cv.style.height = '0px';
  cv.style.height = Math.max(view.scrollHeight, view.clientHeight) + 'px';
}

async function mount(view) {
  if (cur && cur.view === view) return;
  await unmount();
  const cv = document.createElement('canvas');
  cv.className = 'pen-cv';
  view.style.position = 'relative';
  view.appendChild(cv);
  sizeTo(view, cv);
  const map = () => ({ X: p => p[0], Y: p => p[1], k: 1 });
  const s = new Surface(cv, [], { map, changed: () => {}, limits: () => writing });
  s.toUnits = (x, y) => { const r = cv.getBoundingClientRect(), sc = cv.clientWidth / (r.width || 1); return [(x - r.left) * sc, (y - r.top) * sc]; };
  s.unitPerPx = () => { const r = cv.getBoundingClientRect(); return cv.clientWidth / (r.width || 1); };
  const key = keyOf(view);
  cur = { view, cv, s, key };
  try { const rec = await db.kv.get(key); if (rec && rec.objs) s.objs.push(...rec.objs); } catch (e) { /* */ }
  attachPointer(s, {
    writing: () => writing,
    toUnits: s.toUnits, unitPerPx: s.unitPerPx, map: () => s.o.map(),
    scrollBy: dy => { window.scrollBy(0, dy); },
    selChanged: () => { if (bar) bar.draw(); },
    onDown: () => { if (bar) bar.closePop(); },
    pasting: () => null, clips: () => [],
    changed: () => markDirty()
  });
  const ro = new ResizeObserver(() => { if (cur && cur.view === view) { sizeTo(view, cv); s.render(); } });
  ro.observe(view); cur.ro = ro;
  applyMode();
  s.render();
}
async function unmount() {
  if (!cur) return;
  await flush();
  if (cur.ro) cur.ro.disconnect();
  cur.cv.remove();
  cur = null;
}

function applyMode() {
  if (cur) cur.cv.classList.toggle('on', writing);
  document.body.classList.toggle('pen-on', writing);
  if (!host) return;
  if (bar) { bar.destroy(); bar = null; }
  host.hidden = false;
  if (writing) {
    host.classList.add('ik-float');
    bar = new Toolbar(host, {
      undo: () => { if (cur) { cur.s.doUndo(); markDirty(); } },
      redo: () => { if (cur) { cur.s.doRedo(); markDirty(); } },
      done: () => setWriting(false),
      clear: () => { if (!cur) return; const s = cur.s; s.snapshot(); s.objs.splice(0); s.sel = null; s.render(); markDirty(); },
      toolChanged: () => { if (cur) { cur.s.sel = null; cur.s.render(); } },
      hasSel: () => !!(cur && cur.s.sel && cur.s.sel.ids.length),
      selOnExplain: () => false, canXfer: () => false, xferLabel: () => '',
      pin: null, docked: null,
      clips: () => [], pasting: () => null, setPasting: () => {}, removeClip: () => {}, clearClips: () => {},
      selAction: (a, v) => {
        if (!cur || !cur.s.sel) return;
        const s = cur.s, ids = s.sel.ids.filter(i => s.objs[i]);
        if (a === 'del' || a === 'cut') { s.snapshot(); const set = new Set(ids); s.objs.splice(0, s.objs.length, ...s.objs.filter((o, i) => !set.has(i))); s.sel = null; }
        else if (a === 'colour') { s.snapshot(); for (const i of ids) s.objs[i].c = v; }
        else if (a === 'width') { s.snapshot(); for (const i of ids) { const o = s.objs[i]; if (o.type === 'hl' && o.snap) { o.h *= v; if (o.rects) o.rects = o.rects.map(r => [r[0], r[1], r[2], r[3] * v]); } else if (o.s) o.s = Math.max(0.3, o.s * v); } }
        else s.sel = null;
        s.render(); markDirty(); if (bar) bar.draw();
      }
    });
  } else {
    host.classList.add('ik-float');
    host.innerHTML = '<button class="ik-fab" data-pen-fab aria-label="Write on this screen with the S Pen" title="Write on this screen (drag to move)">' + INK_ICONS.fab + '</button>';
    placeFloat(host, railSize());
    dragFloat(host, host.querySelector('[data-pen-fab]'), () => setWriting(true));
  }
}
function setWriting(on) {
  writing = !!on;
  if (!writing && cur) { cur.s.sel = null; cur.s.render(); flush(); }
  applyMode();
}

function start() {
  host = document.createElement('div');
  host.className = 'ik-host ik-float';
  host.hidden = true;
  document.body.appendChild(host);
  const v = viewNow(); if (v) mount(v);
  applyMode();
  new MutationObserver(() => { const n = viewNow(); if (n && (!cur || cur.view !== n)) mount(n); })
    .observe(document.querySelector('main') || document.body, { attributes: true, attributeFilter: ['hidden'], subtree: true });
  addEventListener('beforeunload', () => { flush(); });
  addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden') flush(); });
}
if (document.readyState === 'loading') addEventListener('DOMContentLoaded', start); else start();
