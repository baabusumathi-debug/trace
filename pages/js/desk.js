// The study desk: the page on one side, a notebook on the other, a divider between them,
// each side with its own zoom, and the S Pen over both. Controls live in the header strip.
import { useDbName } from '../../js/db.js';
useDbName('trace-pages');
import { mountInk, startInk, setWriting, isWriting, onWriting, sizeAll } from './ink-mount.js';
import { Notebook, PW } from './notes.js';
import { PAPERS, COLOURS, LAYOUTS, paperName, colourName } from './paper.js';
import { localGet, localSet, cloudGet, makeSaver, onState } from './store.js';

const PAGE = (location.pathname.split('/').pop() || 'page').replace('.html', '') || 'page';
const P = {
  get: (k, d) => { try { const v = localStorage.getItem('desk.' + PAGE + '.' + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
  set: (k, v) => { try { localStorage.setItem('desk.' + PAGE + '.' + k, JSON.stringify(v)); } catch (e) { /* */ } }
};
const land = () => matchMedia('(orientation:landscape) and (min-width:900px)').matches;
const el = (t, c, h) => { const n = document.createElement(t); if (c) n.className = c; if (h != null) n.innerHTML = h; return n; };

let study, zwrap, zw, notesPane, divider, nb, saver, inks = new Map(), base = 0;

/* ---------- layout ---------- */
function build() {
  const header = document.querySelector('header'), main = document.querySelector('main');
  document.body.classList.add('desk-on');
  const desk = el('div', 'desk');
  study = el('div', 'pane pane-study');
  zwrap = el('div', 'zwrap'); zw = el('div', 'zw');
  zwrap.appendChild(zw); zw.appendChild(main); study.appendChild(zwrap);
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
    '</span>' +
    '<button class="sbtn" data-s="set" aria-label="Settings">⚙</button>' +
    '<span class="dot" data-dot title="Backup"></span>';
  return s;
}

/* ---------- zoom: the whole side scales, so writing stays exactly on the words ---------- */
let zStudy = 1, zWho = 'study';
function baseWidth() {
  const k = land() ? 'baseL' : 'baseP';
  let b = P.get(k, 0);
  if (!b) { b = Math.max(360, Math.round((land() ? Math.min(innerWidth * 0.52, 900) : innerWidth) - 8)); P.set(k, b); }
  return b;
}
function applyStudyZoom() {
  base = baseWidth();
  zw.style.width = base + 'px';
  zw.style.transform = 'scale(' + zStudy.toFixed(3) + ')';
  const h = zw.scrollHeight || zw.offsetHeight;
  zwrap.style.width = Math.round(base * zStudy) + 'px';
  zwrap.style.height = Math.round(h * zStudy) + 'px';
  sizeAll();
  paintZoom();
}
function fitNotes() {
  const w = (notesPane.clientWidth || innerWidth) - 34;
  if (w > 80) { nb.setZoom(w / PW); P.set('zNotes', nb.getZoom()); paintZoom(); }
}
function fitStudy() { zStudy = Math.max(0.4, Math.min(2.5, (study.clientWidth - 6) / baseWidth())); applyStudyZoom(); P.set('zStudy', zStudy); }
function setZoom(who, z) {
  if (who === 'study') { zStudy = Math.max(0.4, Math.min(2.5, z)); P.set('zStudy', zStudy); applyStudyZoom(); }
  else { nb.setZoom(z); P.set('zNotes', nb.getZoom()); paintZoom(); }
}
function paintZoom() {
  const z = zWho === 'study' ? zStudy : (nb ? nb.getZoom() : 1);
  const w = document.querySelector('[data-z-who]'), v = document.querySelector('[data-z-val]'), r = document.querySelector('[data-z-range]');
  if (w) w.textContent = zWho === 'study' ? 'Study' : 'Notes';
  if (v) v.textContent = Math.round(z * 100) + '%';
  if (r && document.activeElement !== r) r.value = Math.round(z * 100);
}
function pinch(pane, who) {
  let g = null;
  const pts = e => [...e.touches].slice(0, 2).map(t => [t.clientX, t.clientY]);
  const d = q => Math.hypot(q[0][0] - q[1][0], q[0][1] - q[1][1]);
  pane.addEventListener('touchstart', e => {
    if (e.touches.length !== 2) { g = null; return; }
    zWho = who; paintZoom();
    g = { d0: d(pts(e)), z0: who === 'study' ? zStudy : nb.getZoom(), on: false }; e.preventDefault();
  }, { passive: false });
  pane.addEventListener('touchmove', e => {
    if (!g || e.touches.length !== 2) return; e.preventDefault();
    const r = d(pts(e)) / g.d0; if (!g.on && Math.abs(r - 1) < 0.06) return; g.on = true;
    setZoom(who, g.z0 * r);
  }, { passive: false });
  pane.addEventListener('touchend', () => { g = null; });
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
      if (nb.getZoom() * PW > notesPane.clientWidth - 10) fitNotes(); else nb.fit();
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
  if (on) setTimeout(() => { if (!P.get('zNotes', 0) || nb.getZoom() * PW > notesPane.clientWidth) fitNotes(); }, 60);
  zWho = on ? 'notes' : 'study';
  requestAnimationFrame(() => { fitStudy(); if (nb) nb.fit(); paintZoom(); });
}

/* ---------- ink on the study side ---------- */
const viewNow = () => [...document.querySelectorAll('section.view')].find(v => !v.hidden) || null;
function inkFor(view) {
  if (inks.has(view.id)) return inks.get(view.id);
  const h = mountInk(view, {
    width: () => base, height: () => Math.max(view.scrollHeight, view.clientHeight),
    scroller: () => study,
    changed: () => { localSet('pen:' + PAGE + ':' + view.id + ':' + base, { objs: h.objs(), ts: Date.now() }); }
  });
  inks.set(view.id, h);
  localGet('pen:' + PAGE + ':' + view.id + ':' + base).then(r => { if (r && r.objs) h.load(r.objs); });
  return h;
}

/* ---------- settings ---------- */
function sheet() {
  const w = el('div', 'sheet-wrap');
  const st = nb.style();
  const row = (lab, name, items, cur) => '<div class="srow"><div class="slab">' + lab + '</div><div class="schips">' +
    items.map(i => '<button class="chip' + (i[0] === cur ? ' on' : '') + '" data-' + name + '="' + i[0] + '">' + i[1] + '</button>').join('') + '</div></div>';
  w.innerHTML = '<div class="sheet"><div class="shead"><b>Notes</b><button class="sbtn" data-s="close">Close</button></div>' +
    '<div class="srow"><div class="slab">Apply to</div><div class="schips">' +
      ['page', 'after', 'all'].map((k, i) => '<button class="chip' + (i === 0 ? ' on' : '') + '" data-scope="' + k + '">' +
        ['This page', 'This page and new ones', 'The whole notebook'][i] + '</button>').join('') + '</div></div>' +
    row('Paper', 'paper', PAPERS, st.paper) +
    row('Page colour', 'colour', COLOURS.map(c => [c[0], c[1]]), st.colour) +
    row('Layout', 'layout', LAYOUTS, st.layout) +
    '<div class="snote" data-backup></div></div>';
  let scope = 'page';
  w.addEventListener('click', e => {
    const b = e.target.closest('button'); if (!b) { if (e.target === w) w.remove(); return; }
    if (b.dataset.s === 'close') { w.remove(); return; }
    if (b.dataset.scope) { scope = b.dataset.scope; w.querySelectorAll('[data-scope]').forEach(x => x.classList.toggle('on', x === b)); return; }
    for (const k of ['paper', 'colour', 'layout']) if (b.dataset[k]) {
      nb.setStyle({ [k]: b.dataset[k] }, scope);
      w.querySelectorAll('[data-' + k + ']').forEach(x => x.classList.toggle('on', x === b));
    }
  });
  document.body.appendChild(w);
  paintBackup(w.querySelector('[data-backup]'));
}
const DOT = { local: ['#d8a200', 'Saved on this tablet'], saving: ['#d8a200', 'Backing up…'], saved: ['#2e9d4f', 'Backed up to Drive'], offline: ['#c0392b', 'Not backed up — no connection'], nobackend: ['#8e8e93', 'Backup off — connect Trace to Drive in the app'] };
function paintBackup(node) { if (node) node.textContent = DOT[window.__sync || 'local'][1]; }

/* ---------- start ---------- */
async function start() {
  const desk = build();
  startInk();
  const cards = [...document.querySelectorAll('section.view')].map(v => ({
    id: v.id,
    label: v.id === 'HOME' ? 'Home' : ((v.querySelector('.chead .code') || {}).textContent || v.id)
  }));
  nb = new Notebook(notesPane, cards, () => saver && saver.touch());
  saver = makeSaver(PAGE, () => nb.data);
  onState(s => {
    window.__sync = s;
    const d = document.querySelector('[data-dot]');
    if (d) { d.style.background = DOT[s][0]; d.title = DOT[s][1]; }
    const n = document.querySelector('[data-backup]'); paintBackup(n);
  });
  const local = await localGet('nb:' + PAGE);
  nb.load(local);
  cloudGet(PAGE).then(remote => { if (remote && remote.ts && (!local || remote.ts > (local.ts || 0))) nb.load(remote); }).catch(() => {});

  zStudy = P.get('zStudy', 0) || 0; base = baseWidth();
  if (!zStudy) fitStudy(); else applyStudyZoom();
  const zn = P.get('zNotes', 0);
  nb.setZoom(zn || 1);
  if (!zn) setTimeout(fitNotes, 80);
  if (P.get('notes', false)) showNotes(true);
  setupSplit(desk);
  pinch(study, 'study'); pinch(notesPane, 'notes');

  document.querySelector('header').addEventListener('click', e => {
    const b = e.target.closest('[data-s]'); if (!b) return;
    const a = b.dataset.s;
    if (a === 'pen') setWriting(!isWriting());
    else if (a === 'notes') showNotes(!desk.classList.contains('notes-on'));
    else if (a === 'set') sheet();
    else if (a === 'zin') setZoom(zWho, (zWho === 'study' ? zStudy : nb.getZoom()) + 0.1);
    else if (a === 'zout') setZoom(zWho, (zWho === 'study' ? zStudy : nb.getZoom()) - 0.1);
  });
  const rng = document.querySelector('[data-z-range]');
  rng.addEventListener('input', () => setZoom(zWho, +rng.value / 100));
  study.addEventListener('pointerdown', () => { if (zWho !== 'study') { zWho = 'study'; paintZoom(); } }, true);
  notesPane.addEventListener('pointerdown', () => { if (zWho !== 'notes') { zWho = 'notes'; paintZoom(); } }, true);
  onWriting(on => { const b = document.querySelector('[data-s="pen"]'); if (b) b.setAttribute('aria-pressed', on ? 'true' : 'false'); });

  const follow = () => { const v = viewNow(); if (!v) return; inkFor(v); nb.show(v.id, 0); };
  follow();
  new MutationObserver(follow).observe(document.querySelector('main'), { attributes: true, attributeFilter: ['hidden'], subtree: true });
  new ResizeObserver(() => { applyStudyZoom(); }).observe(zw);
  addEventListener('resize', () => { base = baseWidth(); applyStudyZoom(); });
  addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden') saver.flush(); });
  addEventListener('beforeunload', () => saver.flush());
}
if (document.readyState === 'loading') addEventListener('DOMContentLoaded', start); else start();
