// The study desk: the page on one side, a notebook on the other, a divider between them,
// each side with its own zoom, and the S Pen over both. Controls live in the header strip.
import { useDbName } from '../../js/db.js';
useDbName('trace-pages');
import { mountInk, startInk, setWriting, isWriting, onWriting, sizeAll, toast } from './ink-mount.js';
import { Notebook, PW } from './notes.js';
import { PAPERS, COLOURS, LAYOUTS } from './paper.js';
import { localGet, localSet, cloudGet, makeSaver, onState, markSynced, NOTES_FILE, INK_FILE } from './store.js';

const PAGE = (location.pathname.split('/').pop() || 'page').replace('.html', '') || 'page';
const P = {
  get: (k, d) => { try { const v = localStorage.getItem('desk.' + PAGE + '.' + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
  set: (k, v) => { try { localStorage.setItem('desk.' + PAGE + '.' + k, JSON.stringify(v)); } catch (e) { /* */ } }
};
const land = () => matchMedia('(orientation:landscape) and (min-width:900px)').matches;
const el = (t, c, h) => { const n = document.createElement(t); if (c) n.className = c; if (h != null) n.innerHTML = h; return n; };

let study, zwrap, zw, orient, notesPane, divider, nb, saver, inkSaver, inks = new Map(), base = 0;
let ink = { v: 1, views: {}, ts: 0 };        // every mark on the study screens: views["S1-CS-02@790"] = { objs, ts }

/* ---------- layout ---------- */
function build() {
  const header = document.querySelector('header'), main = document.querySelector('main');
  document.body.classList.add('desk-on');
  const desk = el('div', 'desk');
  study = el('div', 'pane pane-study');
  orient = el('div', 'orient'); orient.hidden = true;
  zwrap = el('div', 'zwrap'); zw = el('div', 'zw');
  zwrap.appendChild(zw); zw.appendChild(main); study.append(orient, zwrap);
  divider = el('div', 'a-div', '<i></i>');
  notesPane = el('div', 'pane pane-notes');
  desk.append(study, divider, notesPane);
  header.after(desk);
  header.appendChild(strip());
  desk.style.setProperty('--split', (P.get(land() ? 'splitL' : 'splitP', 50)) + '%');
  return desk;
}
function strip() {
  const s = el('div', 'strip');
  s.innerHTML =
    '<button class="sbtn" data-s="pen" aria-pressed="false"><span class="ic">✎</span> Pen</button>' +
    '<button class="sbtn" data-s="notes" aria-pressed="false"><span class="ic">▤</span> Notes</button>' +
    '<span class="zgrp" role="group" aria-label="Size">' +
      '<button class="sbtn tiny" data-s="zout" aria-label="Smaller">−</button>' +
      '<span class="zlab"><b data-z-who>Study</b> <span data-z-val>100%</span></span>' +
      '<button class="sbtn tiny" data-s="zin" aria-label="Bigger">+</button>' +
      '<input type="range" min="40" max="250" step="5" value="100" data-z-range aria-label="Size">' +
      '<button class="sbtn tiny" data-s="fit" aria-label="Fit this side to its width">⇔ Fit</button>' +
    '</span>' +
    '<button class="sbtn" data-s="set" aria-label="Settings">⚙</button>' +
    '<button class="sbtn tiny bk" data-s="dot" data-dot aria-label="Backup">▢</button>' +
    '<a class="sbtn" href="./" data-s="home">← Pages</a>';
  return s;
}

/* ---------- zoom: the whole side scales, so writing stays exactly on the words ---------- */
let zStudy = 1, zWho = 'study', zH = 0;
function baseWidth() {
  const k = land() ? 'baseL' : 'baseP';
  let b = P.get(k, 0);
  if (!b) { b = Math.max(360, Math.round((land() ? Math.min(innerWidth * 0.52, 900) : innerWidth) - 8)); P.set(k, b); }
  return b;
}
// Sticky bars (tabs, headers) inside a scaled page move by scroll x zoom and drift down the page,
// so while the study side is zoomed they sit in place like ordinary content.
function markSticky() {
  zw.querySelectorAll('*').forEach(e => { if (!e.dataset.stk && getComputedStyle(e).position === 'sticky') e.dataset.stk = '1'; });
}
function unstick(z) { zw.classList.toggle('unstick', Math.abs(z - 1) > 0.005); }
function applyStudyZoom() {
  base = baseWidth();
  unstick(zStudy);
  zw.style.width = base + 'px';
  zw.style.transform = 'scale(' + zStudy.toFixed(3) + ')';
  zH = zw.offsetHeight || zw.scrollHeight;
  zwrap.style.width = Math.round(base * zStudy) + 'px';
  zwrap.style.height = Math.round(zH * zStudy) + 'px';
  sizeAll();
  paintZoom();
}
// live zoom: only the transform and the box change, around the point given, once a frame
let sp = null;
function studyPinchTo(z, fx, fy) {
  z = Math.max(0.4, Math.min(2.5, z));
  if (!sp) sp = { cx: (study.scrollLeft + fx - zwrap.offsetLeft) / zStudy, cy: (study.scrollTop + fy - zwrap.offsetTop) / zStudy };
  zStudy = z; unstick(z);
  zw.style.transform = 'scale(' + z.toFixed(4) + ')';
  zwrap.style.width = Math.round(base * z) + 'px';
  zwrap.style.height = Math.round(zH * z) + 'px';
  study.scrollLeft = sp.cx * z + zwrap.offsetLeft - fx;
  study.scrollTop = sp.cy * z + zwrap.offsetTop - fy;
  paintZoom();
}
function studyPinchEnd() { sp = null; P.set('zStudy', zStudy); applyStudyZoom(); }
function fitNotes() {
  const w = (notesPane.clientWidth || innerWidth) - 34;
  if (w > 80) { nb.setZoom(w / PW); P.set('zNotes', nb.getZoom()); paintZoom(); }
}
function fitStudy() { zStudy = Math.max(0.4, Math.min(2.5, (study.clientWidth - 6) / baseWidth())); applyStudyZoom(); P.set('zStudy', zStudy); }
const paneOf = who => who === 'study' ? study : nb.scroll;
const zNow = who => who === 'study' ? zStudy : nb.getZoom();
function liveZoom(who, z, fx, fy) {
  const p = paneOf(who);
  if (fx == null) { fx = p.clientWidth / 2; fy = p.clientHeight / 3; }
  if (who === 'study') studyPinchTo(z, fx, fy); else { nb.pinchTo(z, fx, fy); paintZoom(); }
}
function endZoom(who) {
  if (who === 'study') studyPinchEnd();
  else { nb.pinchEnd(); P.set('zNotes', nb.getZoom()); paintZoom(); }
}
function setZoom(who, z) { liveZoom(who, z); endZoom(who); }
function paintZoom() {
  const z = zNow(zWho === 'notes' && nb ? 'notes' : 'study');
  const w = document.querySelector('[data-z-who]'), v = document.querySelector('[data-z-val]'), r = document.querySelector('[data-z-range]');
  if (w) w.textContent = zWho === 'study' ? 'Study' : 'Notes';
  if (v) v.textContent = Math.round(z * 100) + '%';
  if (r && document.activeElement !== r) r.value = Math.round(z * 100);
}
function pinch(pane, who) {
  let g = null, raf = 0, want = null;
  const mid = e => { const r = paneOf(who).getBoundingClientRect(), a = e.touches[0], b = e.touches[1]; return [(a.clientX + b.clientX) / 2 - r.left, (a.clientY + b.clientY) / 2 - r.top]; };
  const dist = e => Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
  const frame = () => { raf = 0; if (want) liveZoom(who, want[0], want[1], want[2]); };
  pane.addEventListener('touchstart', e => {
    if (e.touches.length !== 2) return;
    zWho = who; paintZoom();
    g = { d0: dist(e), z0: zNow(who), on: false }; e.preventDefault();
  }, { passive: false });
  pane.addEventListener('touchmove', e => {
    if (!g || e.touches.length !== 2) return; e.preventDefault();
    const r = dist(e) / g.d0; if (!g.on && Math.abs(r - 1) < 0.04) return;
    const m = mid(e);
    if (!g.on) { g.on = true; if (who === 'study') sp = null; else nb.pinchStart(m[0], m[1]); }   // the point under the fingers is fixed here
    want = [g.z0 * r, m[0], m[1]];
    if (!raf) raf = requestAnimationFrame(frame);
  }, { passive: false });
  const done = e => {
    if (!g || (e.touches && e.touches.length >= 2)) return;
    if (raf) { cancelAnimationFrame(raf); frame(); }
    const was = g.on; g = null; want = null;
    if (was) endZoom(who);
  };
  pane.addEventListener('touchend', done); pane.addEventListener('touchcancel', done);
}

/* ---------- the divider ---------- */
function setupSplit(desk) {
  divider.addEventListener('pointerdown', e => {
    if (e.pointerType === 'pen' && isWriting()) return;
    e.preventDefault(); divider.setPointerCapture(e.pointerId); desk.classList.add('dragging');
    const r = desk.getBoundingClientRect();
    const mv = ev => {
      const v = land() ? (ev.clientX - r.left) / r.width * 100 : (ev.clientY - r.top) / r.height * 100;
      desk.style.setProperty('--split', Math.max(12, Math.min(88, v)).toFixed(1) + '%');
    };
    const up = () => {
      divider.removeEventListener('pointermove', mv); divider.removeEventListener('pointerup', up); divider.removeEventListener('pointercancel', up);
      desk.classList.remove('dragging');
      const v = parseFloat(desk.style.getPropertyValue('--split')) || 50;
      P.set(land() ? 'splitL' : 'splitP', v);
      if (v <= 14) showNotes(false);
      fitStudy();
      if (nb.getZoom() * PW > nb.scroll.clientWidth - 10) fitNotes(); else nb.fit();
    };
    divider.addEventListener('pointermove', mv); divider.addEventListener('pointerup', up); divider.addEventListener('pointercancel', up);
  });
}
function showNotes(on) {
  const desk = document.querySelector('.desk');
  desk.classList.toggle('notes-on', on);
  const b = document.querySelector('[data-s="notes"]'); if (b) b.setAttribute('aria-pressed', on ? 'true' : 'false');
  P.set('notes', on);
  if (on && parseFloat(desk.style.getPropertyValue('--split')) <= 14) desk.style.setProperty('--split', '50%');
  zWho = on ? 'notes' : 'study';
  requestAnimationFrame(() => {
    fitStudy();
    if (on) { if (!P.get('zNotes', 0) || nb.getZoom() * PW > nb.scroll.clientWidth) fitNotes(); nb.paint(); nb.scrollToPage(nb.idx); }
    paintZoom();
  });
}

/* ---------- ink on the study side: kept on the tablet and backed up to Drive ---------- */
const viewNow = () => [...document.querySelectorAll('section.view')].find(v => !v.hidden) || null;
const ikey = (id, w) => id + '@' + w;
async function adopt(id, w) {                  // marks saved before the Drive backup existed
  const k = ikey(id, w);
  if (ink.views[k]) return ink.views[k];
  const old = await localGet('pen:' + PAGE + ':' + id + ':' + w);
  if (old && old.objs && old.objs.length && !ink.views[k]) { ink.views[k] = { objs: old.objs, ts: old.ts || 1 }; inkSaver.touch(); }
  return ink.views[k];
}
function inkFor(view) {
  const k = ikey(view.id, base);
  if (inks.has(k)) return inks.get(k);
  for (const [key, o] of inks) if (o.el === view) { o.destroy(); inks.delete(key); }   // the other orientation's layer
  const h = mountInk(view, {
    width: () => base, height: () => Math.max(view.scrollHeight, view.clientHeight),
    scroller: () => study,
    changed: () => { ink.views[k] = { objs: h.objs().slice(), ts: Date.now() }; ink.ts = Date.now(); inkSaver.touch(); orientNote(view); }
  });
  h.key = k;
  inks.set(k, h);
  adopt(view.id, base).then(r => { if (r && r.objs) h.load(r.objs); });
  return h;
}
// writing made in the other orientation sits at a different width, so it is not drawn here: say so
async function orientNote(view) {
  if (!view) return;
  const other = P.get(land() ? 'baseP' : 'baseL', 0);
  let has = false;
  if (other && other !== base) { const r = await adopt(view.id, other); has = !!(r && r.objs && r.objs.length); }
  const here = ink.views[ikey(view.id, base)];
  orient.hidden = !has;
  if (has) orient.textContent = '✎ You also have writing on this screen in ' + (land() ? 'portrait' : 'landscape') + ' — turn the tablet to see it' + (here && here.objs.length ? '' : '.');
}

/* ---------- settings ---------- */
function sheet() {
  const w = el('div', 'sheet-wrap');
  const st = nb.style();
  const row = (lab, name, items, cur) => '<div class="srow"><div class="slab">' + lab + '</div><div class="schips">' +
    items.map(i => '<button class="chip' + (i[0] === cur ? ' on' : '') + '" data-' + name + '="' + i[0] + '">' + (i[0] === cur ? '✓ ' : '') + i[1] + '</button>').join('') + '</div></div>';
  const bin = nb.trashList().slice(0, 8);
  w.innerHTML = '<div class="sheet"><div class="shead"><b>Notes</b><button class="sbtn" data-s="close">Close</button></div>' +
    '<div class="srow"><div class="slab">Apply to</div><div class="schips">' +
      ['page', 'after', 'all'].map((k, i) => '<button class="chip' + (i === 0 ? ' on' : '') + '" data-scope="' + k + '">' + (i === 0 ? '✓ ' : '') +
        ['This page', 'This page and new ones', 'The whole notebook'][i] + '</button>').join('') + '</div></div>' +
    row('Paper', 'paper', PAPERS, st.paper) +
    row('Page colour', 'colour', COLOURS.map(c => [c[0], c[1]]), st.colour) +
    row('Layout', 'layout', LAYOUTS, st.layout) +
    (bin.length ? '<div class="srow"><div class="slab">Deleted pages</div><div class="sbin">' +
      bin.map(t => '<div class="sbin1"><span>' + t.label + ' · ' + (t.marks ? t.marks + ' mark' + (t.marks === 1 ? '' : 's') : 'empty') + '</span><button class="chip" data-restore="' + t.id + '">↺ Restore</button></div>').join('') +
      '</div></div>' : '') +
    '<div class="srow"><div class="slab">Notebook of</div><div class="schips"><button class="chip on">✓ ' + (WHO ? WHO.name : '') + '</button><button class="chip" data-s="who">Change who is writing</button></div></div>' +
    '<div class="snote" data-backup></div></div>';
  let scope = 'page';
  const mark = (sel, b) => w.querySelectorAll(sel).forEach(x => { x.classList.toggle('on', x === b); x.textContent = x.textContent.replace(/^✓ /, ''); if (x === b) x.textContent = '✓ ' + x.textContent; });
  w.addEventListener('click', e => {
    const b = e.target.closest('button'); if (!b) { if (e.target === w) w.remove(); return; }
    if (b.dataset.s === 'close') { w.remove(); return; }
    if (b.dataset.s === 'who') { saver.flush(); inkSaver.flush(); try { localStorage.removeItem(WKEY); } catch (e) { /* */ } setTimeout(() => location.reload(), 300); return; }
    if (b.dataset.restore) { nb.restore(b.dataset.restore); w.remove(); return; }
    if (b.dataset.scope) { scope = b.dataset.scope; mark('[data-scope]', b); return; }
    for (const k of ['paper', 'colour', 'layout']) if (b.dataset[k]) { nb.setStyle({ [k]: b.dataset[k] }, scope); mark('[data-' + k + ']', b); }
  });
  document.body.appendChild(w);
  paintBackup(w.querySelector('[data-backup]'));
}
// the backup state is a shape, never only a colour
const DOT = {
  local:     ['▢', 'Saved on this tablet — waiting to back up to Drive'],
  saving:    ['↑', 'Backing up to Drive…'],
  saved:     ['✓', 'Backed up to Drive'],
  offline:   ['✕', 'Not backed up — no connection. It is safe on this tablet and will go up when you are online.'],
  nobackend: ['⊘', 'Backup is off on this device — open Trace once and connect it to Drive']
};
function paintBackup(node) { if (node) node.textContent = DOT[window.__sync || 'local'][0] + '  ' + DOT[window.__sync || 'local'][1]; }

/* ---------- who is writing on this tablet ----------
   Naven's notebook keeps the original names (nb:<page>, studynotes-<page>.json), so nothing of his moves.
   Anyone else gets their own: nb:<page>:<id>, studynotes-<page>-<id>.json. Two people sharing one Drive
   therefore never load or overwrite each other's notes. */
const WKEY = 'desk.writer';
const WRITERS = [{ id: 'naven', name: 'Naven' }, { id: 'ht', name: 'HT' }];
function readWriter() { try { const w = JSON.parse(localStorage.getItem(WKEY) || 'null'); return w && w.id ? w : null; } catch (e) { return null; } }
function whoWrites() {
  const known = readWriter(); if (known) return Promise.resolve(known);
  return new Promise(res => {
    const w = el('div', 'sheet-wrap', '<div class="sheet small"><div class="shead"><b>Who is writing on this tablet?</b></div>' +
      '<p class="snote">Asked once. Each person gets their own notebook, saved and backed up separately, so nobody overwrites anybody.</p>' +
      '<div class="sact" style="justify-content:flex-start;flex-wrap:wrap">' + WRITERS.map(x => '<button class="chip" data-w="' + x.id + '">' + x.name + '</button>').join('') +
      '<span style="display:inline-flex;gap:6px"><input data-wn placeholder="Someone else: name" style="font:inherit;padding:5px 8px;border:1px solid #b9c1cf;border-radius:8px;width:11em"><button class="chip" data-w="other">OK</button></span></div></div>');
    w.addEventListener('click', e => {
      const b = e.target.closest('[data-w]'); if (!b) return;
      let pick = WRITERS.find(x => x.id === b.dataset.w);
      if (!pick) {
        const nm = (w.querySelector('[data-wn]').value || '').trim(); if (!nm) return;
        const id = nm.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 20) || 'guest';
        pick = { id: id === 'naven' ? 'naven-2' : id, name: nm };
      }
      try { localStorage.setItem(WKEY, JSON.stringify(pick)); } catch (err) { /* */ }
      w.remove(); res(pick);
    });
    document.body.appendChild(w);
  });
}
let WHO = null;
const nbKey = () => 'nb:' + PAGE + (WHO.id === 'naven' ? '' : ':' + WHO.id);
const inkKey = () => 'ink:' + PAGE + (WHO.id === 'naven' ? '' : ':' + WHO.id);
const fileSfx = f => WHO.id === 'naven' ? f : f.replace(/\.json$/, '-' + WHO.id + '.json');

/* ---------- start ---------- */
async function start() {
  const desk = build();
  WHO = await whoWrites();
  window.__writer = { who: WHO.id, nb: nbKey(), ink: inkKey(), files: [fileSfx(NOTES_FILE(PAGE)), fileSfx(INK_FILE(PAGE))] };
  startInk();
  const cards = [...document.querySelectorAll('section.view')].map(v => ({
    id: v.id,
    label: v.id === 'HOME' ? 'Home' : ((v.querySelector('.chead .code') || v.querySelector('.top .where') || {}).textContent || v.id).trim()
  }));
  nb = new Notebook(notesPane, cards, () => saver && saver.touch());
  saver = makeSaver(nbKey(), fileSfx(NOTES_FILE(PAGE)), () => nb.data);
  inkSaver = makeSaver(inkKey(), fileSfx(INK_FILE(PAGE)), () => ink);
  onState(s => {
    window.__sync = s;
    const d = document.querySelector('[data-dot]');
    if (d) { d.textContent = DOT[s][0]; d.title = DOT[s][1]; d.setAttribute('aria-label', DOT[s][1]); d.dataset.state = s; }
    paintBackup(document.querySelector('[data-backup]'));
  });
  let [local, localInk] = await Promise.all([localGet(nbKey()), localGet(inkKey())]);
  // HT began on the trauma page before notebooks were split: what this tablet saved there is hers
  if (WHO.id !== 'naven' && PAGE === 'trauma' && !local && !localInk) {
    [local, localInk] = await Promise.all([localGet('nb:' + PAGE), localGet('ink:' + PAGE)]);
    if (local) await localSet(nbKey(), local);
    if (localInk) await localSet(inkKey(), localInk);
  }
  if (localInk && localInk.views) ink = localInk;
  nb.load(local);
  // Drive copies: whichever is newer wins, the notebook as a whole and each study screen on its own
  Promise.all([
    cloudGet(fileSfx(NOTES_FILE(PAGE))).then(remote => { if (remote && remote.ts && (!local || remote.ts > (local.ts || 0))) nb.load(remote); }),
    cloudGet(fileSfx(INK_FILE(PAGE))).then(remote => {
      if (!remote || !remote.views) return;
      for (const [k, r] of Object.entries(remote.views)) {
        const mine = ink.views[k];
        if (!mine || (r.ts || 0) > (mine.ts || 0)) { ink.views[k] = r; const h = inks.get(k); if (h) h.load(r.objs); }
      }
    })
  ]).then(markSynced).catch(() => {});

  zStudy = P.get('zStudy', 0) || 0; base = baseWidth();
  markSticky();
  if (!zStudy) fitStudy(); else applyStudyZoom();
  // content that grows or shrinks (a tab opened, recall on) re-measures the scroll box, so the end stays reachable
  if (window.ResizeObserver) { let ro = 0; new ResizeObserver(() => { if (sp || ro) return; ro = requestAnimationFrame(() => { ro = 0; if (Math.abs((zw.offsetHeight || zw.scrollHeight) - zH) > 1) applyStudyZoom(); }); }).observe(zw); }
  const zn = P.get('zNotes', 0);
  nb.setZoom(zn || 1);
  if (P.get('notes', false)) showNotes(true);
  setupSplit(desk);
  pinch(study, 'study'); pinch(notesPane, 'notes');

  document.querySelector('header').addEventListener('click', e => {
    const b = e.target.closest('[data-s]'); if (!b) return;
    const a = b.dataset.s;
    if (a === 'pen') setWriting(!isWriting());
    else if (a === 'notes') showNotes(!desk.classList.contains('notes-on'));
    else if (a === 'set') sheet();
    else if (a === 'dot') toast(DOT[window.__sync || 'local'][0] + '  ' + DOT[window.__sync || 'local'][1]);
    else if (a === 'home') { saver.flush(); inkSaver.flush(); }
    else if (a === 'fit') { if (zWho === 'notes' && desk.classList.contains('notes-on')) { fitNotes(); nb.scrollToPage(nb.idx); } else fitStudy(); toast('⇔ ' + (zWho === 'notes' ? 'Notes' : 'Study') + ' fitted to its side · ' + Math.round(zNow(zWho) * 100) + '%'); }
    else if (a === 'zin') setZoom(zWho, zNow(zWho) + 0.1);
    else if (a === 'zout') setZoom(zWho, zNow(zWho) - 0.1);
  });
  const rng = document.querySelector('[data-z-range]');
  let rr = 0;
  rng.addEventListener('input', () => { if (rr) return; rr = requestAnimationFrame(() => { rr = 0; liveZoom(zWho, +rng.value / 100); }); });
  rng.addEventListener('change', () => { if (rr) { cancelAnimationFrame(rr); rr = 0; liveZoom(zWho, +rng.value / 100); } endZoom(zWho); });
  study.addEventListener('pointerdown', () => { if (zWho !== 'study') { zWho = 'study'; paintZoom(); } }, true);
  notesPane.addEventListener('pointerdown', () => { if (zWho !== 'notes') { zWho = 'notes'; paintZoom(); } }, true);
  onWriting(on => { const b = document.querySelector('[data-s="pen"]'); if (b) b.setAttribute('aria-pressed', on ? 'true' : 'false'); });

  let shown = null;
  const follow = () => {
    const v = viewNow(); if (!v) return;
    inkFor(v);
    if (v.id !== shown) { shown = v.id; study.scrollTop = 0; nb.show(v.id, 0); applyStudyZoom(); orientNote(v); }
  };
  follow();
  new MutationObserver(follow).observe(document.querySelector('main'), { attributes: true, attributeFilter: ['hidden'], subtree: true });
  let rz = 0;
  new ResizeObserver(() => { if (sp) return; clearTimeout(rz); rz = setTimeout(applyStudyZoom, 60); }).observe(zw);
  addEventListener('resize', () => { base = baseWidth(); applyStudyZoom(); const v = viewNow(); if (v) { inkFor(v); orientNote(v); } });
  const flushAll = () => { saver.flush(); inkSaver.flush(); };
  addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden') flushAll(); });
  addEventListener('pagehide', flushAll);
  addEventListener('beforeunload', flushAll);
}
if (document.readyState === 'loading') addEventListener('DOMContentLoaded', start); else start();
