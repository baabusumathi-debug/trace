import { CONFIG, CHANNEL, PROFILE, IS_HT, setProfile } from './config.js';
import { db, useDemoDb, useDbName, peekDb } from './db.js';
import { renderPalace, renderMeditation, stopMeditation, lastMeditation, TRACKS } from './palace.js';
import { initApi, hasBackend, isDemo, setBackend, call, batch } from './api.js';
import { S, loadAll, emit, cardsOf, withFix, deckMeta, neetTag, qbOf, hitsOf, inPool, isNeet, POOLS, COMPONENTS, poolParts, togglePool, poolName, isTopupDeck, hasTopups, seen, walked, avgPace, tier, shade, systems, isReady, recount, lastSeen, deckLastTs, seenOn, daily, allDays, today, dkey, againList, chunkOf, repairsDueLater, unmappedMisses, missOf } from './store.js';
import { status, sync, loadQbank, loadQmap, loadCardfix, startAutoSync, recordView, undoView, buildLogRows, saveEdit, resetEdit, uid, countPending, downloadDecks, deckState, addTarget, removeTarget, targetItems, compressNos } from './sync.js';
import { render, splitQ, plain, inline } from './md.js';
import { seal, emblem } from './emblems.js';
import { FM, pilotAllowed, resumePending, sendRequest, stopPolling } from './flowmsg.js';
import { todayBeads, chase, livePace, cardsPerDay, studyIntervals, studyMs, bestHours, gtTrend, addDays, daysBetween, winStart, winEnd, PHASE1_END, WIN_START, WIN_END, STUDY_GOAL_H } from './loftx.js';
import { peekOn, setPeek, PEAK_LABEL } from './peek.js';
import { mountInk, setWriting, isWriting, unmountInk } from './inkcard.js';
import { X, initExplain, loadExplain, xOf, mapOf, closeOf, hasExplain, gistHtml, panelHtml, depthOf, partsQHtml, partsAHtml, bridgeHtml, arcHtml, spineOf, mapHtml, closeHtml, patternHtml, getNote, setNote, feedback } from './explain.js';
import { loadPlan, savePlan, currentStretch, newStretch, deleteStretch, addSubject, compute, todayCards, todayParts, subjectDone, dayType, dayList as planDays, DAY_TYPES, repairOpts, dayOrder, setDayOrder, rowOrder, moveRow, undoPlan, canUndoPlan, markVivaDone, vivaDoneToday, addVivaLane, removeVivaLane, computeViva, vivaPlanToday } from './plan.js';
import { REASONS, reasonOf, MEALS, TEAS, AWAY_MIN, current as currentBreak, breaksOn, startBreak, endBreak, logAway, hiddenAt, markHidden, pendingAway, setPendingAway } from './breaks.js';
import { initViva, loadViva, imgSrc as vivaImgSrc, pkgs as vivaPkgs, pkgOf as vivaPkg, vivaQueue, vivaKeys, qOf as vivaQ, vivaX, vivaLines, keyOf as vivaKey, vivaPanelHtml, xpSwitch, qHeadHtml, spineHtml, marks as vivaMarks, setMark as vivaSetMark, lastMark as vivaLast, addQTime, qTimes as vivaTimes } from './viva.js';
import * as DAYP from './day.js';
import * as DESK from './desk.js';
import { lessonOf, lessonHtml, mountLesson, hasLessons, allLessonParts, makeLessons, makingLessons, lessonDeck, estMin as lessonMin } from './lesson.js';
import { voiceOn, partsOf, deckIndex, hasClip, makingDeck, makeDeck, play as vPlay, stop as vStop, nowPlaying as vNow, speed as vSpeed, setSpeed as vSetSpeed, pos as vPos, total as vTotal, seek as vSeek, skip as vSkip, pause as vPause, resume as vResume, isPaused as vPaused } from './voice.js';
import { V, loadVisuals, syncVisuals, linkCard, hasVisual, drawPanel, panelKey, releaseUrls } from './visuals.js';

const $ = (sel, el = document) => el.querySelector(sel);
const app = $('#app');
const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const TIER_NAME = { gold: 'GOLD', silver: 'SILVER', bronze: 'BRONZE', plain: 'PLAIN' };
const fmtDur = s => { s = Math.round(s); return s < 60 ? s + ' s' : Math.floor(s / 60) + ' m ' + (s % 60) + ' s'; };
const clock = s => { s = Math.floor(s); const h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60); return (h ? h + ':' + String(m).padStart(2, '0') : m) + ':' + String(s % 60).padStart(2, '0'); };
const ICON = {
  back: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>',
  close: '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
  undo: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 14L4 9l5-5"/><path d="M4 9h10.5a5.5 5.5 0 0 1 0 11H11"/></svg>',
  again: '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 1 0 2.5-5.8M4 4v4h4"/></svg>',
  flip: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="7.5" y="9" width="9" height="12.5" rx="1.5"/><path d="M4.5 9.5C5.5 5.5 8.5 3.5 12 3.5s6.5 2 7.5 6"/><path d="M19.5 9.5l.3-3.1M19.5 9.5l-3-.9"/></svg>',
  pause: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 5v14M15 5v14"/></svg>',
  play: '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M7 5l12 7-12 7z"/></svg>',
  next: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
  edit: '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M13.5 6.5l4 4"/></svg>',
  decks: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><rect x="7" y="3.5" width="12" height="17" rx="1.5"/><path d="M4.5 6.5v12.5a2 2 0 0 0 2 2"/></svg>',
  walk: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M7 4.5l11 7.5-11 7.5z"/></svg>',
  walkS: '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M7 4.5l11 7.5-11 7.5z"/></svg>',
  shelf: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="M4 20h16M6 20V7h3v13M10 20V4h3v16M15 20l-1-11 3-.5 1.5 11.5"/></svg>',
  prev: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>',
  palace: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="M3.5 20.5h17M5 20.5V10l7-5.5 7 5.5v10.5"/><path d="M10 20.5v-5a2 2 0 0 1 4 0v5"/><circle cx="12" cy="10.5" r="1.4"/></svg>',
  ledger: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M4 12a8 8 0 1 0 2.5-5.8M4 4v4h4"/></svg>'
};

/* ============================ boot ============================ */
async function boot() {
  const params = new URLSearchParams(location.search);
  const demo = params.has('demo');
  if (demo) useDemoDb();
  else {
    // Profile first: Naven's existing devices (a live connection already saved) are Trace without asking.
    if (!PROFILE) {
      let b = null;
      for (const n of ['trace', 'trace-test']) { b = await peekDb(n, 'kv', 'backend').catch(() => null); if (b) break; }   // Naven's devices: a connection from either copy
      if (b) { if (setProfile('trace')) { location.reload(); return; } }   // if storage is blocked, carry on as Trace
      else return renderProfilePick();
    }
    const base = CHANNEL === 'test' ? 'trace-test' : 'trace';
    // each profile keeps its own copy of everything; HT's is a separate database
    if (IS_HT || CHANNEL === 'test') useDbName(base + (IS_HT ? '-ht' : ''));
    if (!(await db.kv.get('backend'))) {        // borrow the connection already saved on this device, never study data
      for (const n of ['trace', 'trace-ht', 'trace-test', 'trace-test-ht']) { const b = await peekDb(n, 'kv', 'backend').catch(() => null); if (b) { await db.kv.set('backend', b); break; } }
    }
    if (CHANNEL === 'test') document.documentElement.classList.add('ch-test');
    if (IS_HT) document.documentElement.classList.add('pf-ht');
  }
  await initApi(demo);

  // private setup link: #setup=<base64url {"u":..., "k":...}>
  if (!demo) await trySetup(location.href);
  if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(() => {});
  await loadAll();
  await initExplain(); await initViva();
  loadQbank(); loadQmap(); loadCardfix(); loadExplain(); loadViva();
  if (!IS_HT) await loadVisuals();      // HT's profile has no visual decks
  if (demo && !S.library) {
    status.state = 'syncing';
  }
  S.listeners.add(() => { if (!flow) route(); else updateFlowChrome(); });
  window.addEventListener('hashchange', async () => {
    if (/#setup=/.test(location.hash) && !isDemo()) { if (await trySetup(location.href)) { await countPending(); startAutoSync(); } }
    route();
  });
  route();
  if (hasBackend()) { await countPending(); startAutoSync(); }
  registerSW();
  watchAway();
  DESK.setDeskSource(deskSnap);
  if (hasBackend() && DESK.deskOn() && !/^#\/desk/.test(location.hash)) setTimeout(() => DESK.startHost(), 4000);   // T-142: the Tab offers the link again
  // visual decks: look for new versions a little after opening, then every 30 minutes (each check is skipped if done < 6 h ago)
  const vcheck = (force) => syncVisuals(d => (S.decks.get(d) || { cards: [] }).cards, { force }).then(() => { if (!flow && /^#\/status/.test(location.hash)) route(); });
  window._vcheck = vcheck;
  if (!IS_HT) { setTimeout(() => vcheck(false), 8000); setInterval(() => vcheck(false), 30 * 60000); }
}

// A two-tap switch (no browser dialog): the first tap arms it for 4 seconds.
let _pfArm = 0, _clArm = 0;
function confirmCopy() { if (Date.now() - _clArm < 4000) return true; _clArm = Date.now(); toast('Tap again to copy the private setup link. It opens your Drive and Sheet: keep it private.'); return false; }
function confirmSwitch() { if (Date.now() - _pfArm < 4000) return true; _pfArm = Date.now(); toast('Tap again to switch profile. Each profile keeps its own data.'); return false; }
function renderProfilePick() {
  app.innerHTML = `<div class="screen welcome"><div class="scroll pad pfpick">
    <span class="mono kick">TRACE · FIRST OPEN ON THIS DEVICE</span>
    <h1 class="h1s">Who studies on this device?</h1>
    <p class="muted">Each profile keeps its own cards seen, targets and flows, and writes to the War Map under its own name.</p>
    <div class="pf-btns"><button class="btn primary press" data-pf="trace">Naven<small>War Map name: Trace</small></button>
      <button class="btn ghost press" data-pf="ht">HT<small>War Map name: HT</small></button></div>
    <p class="muted small">You can change this later on the This device page.</p>
  </div></div>`;
  app.querySelectorAll('[data-pf]').forEach(b => b.onclick = () => { setProfile(b.dataset.pf); location.reload(); });
}

/* ============================ router ============================ */
let lastRoute = '';
function route() {
  if (flow) return;
  if (!/^#\/?meditation/.test(location.hash)) stopMeditation();
  const sc = app.querySelector('.scroll'), y = sc ? sc.scrollTop : 0, same = lastRoute === location.hash;
  lastRoute = location.hash;
  routeInner();
  if (same && y) { const s2 = app.querySelector('.scroll'); if (s2) s2.scrollTop = y; }
}
function routeInner() {
  if (!hasBackend()) return renderWelcome();
  const h = location.hash.replace(/^#\/?/, '');
  const [page, arg] = h.split('/');
  if (page === 'deck' && arg) return renderDeck(decodeURIComponent(arg));
  if (page === 'sys' && arg) return renderSystem(arg);
  if (page === 'flow') return renderFlowTab();
  if (page === 'loft') return renderLoft();
  if (page === 'plan') return renderPlan();
  if (page === 'day') return renderDay();
  if (page === 'desk') return renderDeskPage();
  if (page === 'status') return renderStatus();
  if (page === 'changes') return renderChanges();
  if (page === 'shelf') return renderCabinet();
  if (page === 'meditation') return renderMeditation(app, { nav: nav(''), back: '#/loft', P });
  if (page === 'pilot') return startPilot();
  if (page === 'viva') return renderViva(arg ? decodeURIComponent(arg) : '');
  renderPalace(app, { nav: nav('palace'), top: topBar(true) });
  vivaTile();
  bindGo(); bindGoingOut();
}
const go = h => { location.hash = h; };

function syncPill() {
  const p = status.pending;
  let cls = 'ok', txt = 'Synced';
  if (isDemo()) { cls = 'demo'; txt = 'Demo'; }
  else if (status.state === 'syncing' || status.downloading) { cls = 'busy'; txt = status.downloading ? `Downloading ${status.downloading}` : 'Syncing'; }
  else if (!navigator.onLine) { cls = 'off'; txt = p ? `Offline · ${p} to send` : 'Offline'; }
  else if (status.state === 'error') { cls = 'err'; txt = 'Sync problem'; }
  else if (p) { cls = 'busy'; txt = `${p} to send`; }
  return `<button class="pill pill-${cls}" data-go="#/status" aria-label="Sync status: ${esc(txt)}"><span class="dot"></span>${esc(txt)}</button>`;
}
function daysLeft() {
  const d = Math.ceil((new Date(CONFIG.exam.date + 'T09:00:00+05:30') - Date.now()) / 864e5);
  return d > 0 ? 'D-' + d : 'Exam';
}
function nav(active) {
  const item = (key, href, icon, label) => `<a class="nav-i${active === key ? ' on' : ''}" href="${href}">${icon}<span>${label}</span></a>`;
  return `<nav class="nav">${item('palace', '#/', ICON.palace, 'Palace')}${item('shelf', '#/shelf', ICON.shelf, 'Shelf')}${item('flow', '#/flow', ICON.walk, 'Flow')}${item('changes', '#/changes', ICON.ledger, 'Changes')}</nav>`;
}
let _lastDeck = null;
const lastFlowTarget = () => _lastDeck;

/* ============================ welcome ============================ */
// Accepts the full setup link (or just the part after #setup=). Returns true when connected.
async function trySetup(text) {
  const t = String(text || ''), at = t.indexOf('setup=');
  if (at < 0) return false;
  // tolerate a link that a message app split onto several lines, or wrapped in quotes/brackets
  const m = [null, (t.slice(at + 6).replace(/\s+/g, '').match(/^[\w\-]+/) || [''])[0]];
  if (!m[1]) return false;
  try {
    if (m[1].length % 4 === 1) throw new Error('the link looks cut off (' + m[1].length + ' characters after setup=). Copy it again in one piece');
    let b = m[1].replace(/-/g, '+').replace(/_/g, '/');
    while (b.length % 4) b += '=';
    const j = JSON.parse(atob(b));
    if (!j.u || !j.k) throw new Error('incomplete link');
    await setBackend(j.u, j.k);
    await initApi(false);
    history.replaceState(null, '', location.pathname + '#/');
    toast('Connected to your Drive. Downloading your decks…');
    return true;
  } catch (e) { toast('That setup link did not work: ' + (/cut off|incomplete/.test(e.message) ? e.message : 'it looks incomplete or changed. Copy it again in one piece.')); return false; }
}

function renderWelcome() {
  app.innerHTML = `<div class="screen welcome">
    <div class="brand wbrand">${brandMark()}<span class="brand-t"><span class="b1">TRACE</span><span class="b2">THE MAGICIAN’S CABINET</span></span></div>
    <h1>Connect this device.</h1>
    <p class="muted">Paste the private setup link Claude gave you, then tap Connect. You do this once on each device (phone, tab, Mac). After that, Trace works offline and syncs by itself.</p>
    <textarea id="setup-in" rows="4" placeholder="https://baabusumathi-debug.github.io/trace/#setup=…" autocapitalize="off" autocorrect="off" spellcheck="false"></textarea>
    <button class="btn primary press" id="setup-go">Connect</button>
  </div>`;
  $('#setup-go').onclick = async () => {
    const ok = await trySetup($('#setup-in').value);
    if (ok) { await loadAll(); route(); await countPending(); startAutoSync(); }
  };
}
function topBar(goOut = false) {
  return `<header class="top">
      <a class="brand" href="#/" aria-label="The palace">${brandMark()}<span class="brand-t"><span class="b1">TRACE${CHANNEL === 'test' ? ' <i class="testpill">TEST</i>' : ''}${IS_HT ? ' <i class="testpill htpill">HT</i>' : ''}</span><span class="b2">THE MAGICIAN’S CABINET</span></span></a>
      <div class="top-r">${syncPill()}<span class="exam mono"><span class="gold">${CONFIG.exam.name}</span>${daysLeft()}</span>${goOut ? goingOutButton('sm') : ''}</div>
    </header>`;
}
function brandMark() { return '<span class="mark"><span>✦</span></span>'; }

/* ============================ preferences (per device) ============================ */
const PK = (CHANNEL === 'test' ? 'trace-test.' : 'trace.') + (IS_HT ? 'ht.' : '');   // per-profile view settings and last flow
const P = {
  get(k, d) { try { const v = localStorage.getItem(PK + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
  set(k, v) { try { localStorage.setItem(PK + k, JSON.stringify(v)); } catch (e) { /* private mode */ } }
};
const sysNum = name => String(name || '').slice(0, 2);
const sysLabel = name => String(name || '').replace(/^\d+\s+/, '');
const pctWalked = d => d.cards ? walked(d.deck) / d.cards : 0;
const SORTS = [['neet', '✦ NEET'], ['chrono', 'Chronology'], ['least', 'Least walked'], ['size', 'Size'], ['recent', 'Recent']];
function sortDecks(list, mode) {
  const nat = (a, b) => a.deck.localeCompare(b.deck, undefined, { numeric: true });
  const by = {
    neet: (a, b) => (b.star || 0) - (a.star || 0) || a.cards - b.cards || nat(a, b),
    chrono: (a, b) => a.system.localeCompare(b.system, undefined, { numeric: true }) || nat(a, b),
    least: (a, b) => pctWalked(a) - pctWalked(b) || (b.star || 0) - (a.star || 0) || nat(a, b),
    size: (a, b) => b.cards - a.cards || nat(a, b),
    recent: (a, b) => deckLastTs(b.deck) - deckLastTs(a.deck) || nat(a, b)
  };
  return list.slice().sort(by[mode] || by.neet);
}

/* ============================ the Loft button (7-day hours) ============================ */
const HEAT = ['#faf6ea', '#ecdcb0', '#d7b56c', '#b3843a', '#84591c', '#4f3410'];
function heatColour(v, step) { return v <= 0 ? HEAT[0] : HEAT[Math.min(5, 1 + Math.floor(v / step))]; }
function fmtHM(min) { min = Math.round(min); const h = Math.floor(min / 60), m = min % 60; return h ? h + ' h ' + (m ? m + ' m' : '') : m + ' m'; }
function lastDays(n) {
  const out = [];
  for (let i = n - 1; i >= 0; i--) { const d = new Date(); d.setHours(12, 0, 0, 0); d.setDate(d.getDate() - i); out.push(dkey(d.getTime())); }
  return out;
}
function loftButton() {
  const days = lastDays(7), week = days.reduce((a, d) => a + daily(d).min, 0), tdy = daily(today()).min;
  const names = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  const tg = targetItems(), tgTotal = tg.reduce((a, i) => a + i.nos.length, 0);
  const tgDone = tg.reduce((a, i) => a + i.nos.filter(n => seenOn(i.deck, n, today())).length, 0);
  return `<a class="loftbtn" href="#/loft" aria-label="Open the Loft">
    <span class="lb-top"><span><span class="mono lb-k">THE LOFT</span><span class="lb-t">Today ${fmtHM(tdy)}</span></span>
      <span class="mono lb-r">${fmtHM(week)} this week${tgTotal ? ` · target ${tgDone}/${tgTotal}` : ''} ›</span></span>
    <span class="lb-week" aria-hidden="true">${days.map(d => { const v = daily(d).min / 60; return `<span><i style="background:${heatColour(v, 1)}"></i><b class="mono">${names[new Date(d + 'T12:00').getDay()]}</b></span>`; }).join('')}</span>
  </a>`;
}

/* ============================ shelf (home) ============================ */
let pulled = null;
// Top-up cards not walked yet in a deck: the spine's coral "+n" badge counts these and disappears once they are walked.
const tuLeft = deck => hasTopups(deck) ? cardsOf(deck).filter(c => c.topup && !seen(deck, c.no)).length : 0;
// Long titles shrink instead of being cut off.
const titleSize = (t, mini) => { const n = (t || '').length, f = n <= 26 ? 18.5 : n <= 40 ? 15.5 : n <= 56 ? 13.5 : n <= 72 ? 12 : 11; return (mini ? Math.max(9.5, f * 0.7) : f).toFixed(1) + 'px'; };
function spine(d, out) {
  const t = tier(d.star || 0), w = walked(d.deck), size = P.get('spine', 'm');
  const k = size === 's' ? 0.8 : size === 'l' ? 1.25 : 1;
  const h = Math.round((92 + Math.min(d.cards, 36) / 36 * 46) * k);
  return `<button class="spine t-${t}${out ? ' out' : ''}${isReady(d.deck) ? '' : ' notready'}${d.topupDeck ? ' tu' : tuLeft(d.deck) ? ' hastu' : ''}" data-tu="+${tuLeft(d.deck)}" data-deck="${esc(d.deck)}" style="--h:${h}px;--tone:${emblem(d.system, d.deck).tone}" aria-label="${esc(d.deck)}: ${esc(d.title)}, ${d.star || 0} NEET cards, ${w} of ${d.cards} walked">
    <span class="sp-star mono">${d.topupDeck ? 'TU' : d.star ? '✦' + d.star : ''}</span><span class="sp-code mono">${esc(d.deck)}</span>
    <span class="sp-bar"><i style="width:${Math.round(100 * w / Math.max(1, d.cards))}%"></i></span></button>`;
}
function pulledPanel(d) {
  const t = tier(d.star || 0), cards = cardsOf(d.deck), w = walked(d.deck);
  const neetN = cards.filter(c => isNeet(c)).length, last = deckLastTs(d.deck);
  const ago = last ? Math.max(0, Math.round((Date.now() - last) / 864e5)) : null;
  return `<div class="pulled" id="pulled">
    <div class="pl-main">${deckBack(d, true)}
      <div class="pl-info"><span class="mono kick">${esc(d.deck)} · ${TIER_NAME[t]}</span><span class="pl-title">${esc(d.title)}</span>
        <span class="mono pl-facts">✦ ${d.star || 0} NEET cards<br>${d.cards} cards · ${w} walked${ago != null ? `<br>last walked ${ago === 0 ? 'today' : ago === 1 ? 'yesterday' : ago + ' days ago'}` : ''}</span></div></div>
    ${cards.length ? `<div class="pl-strip">${chunked(cards, c => `<i class="s${shade(seen(c.deck, c.no))}${isNeet(c) ? ' ng' : ''}${c.topup || c.tdeck ? (seen(c.deck, c.no) ? ' tu tu1' : ' tu') : ''}" data-tip="${esc(tipOf(c))}"></i>`)}</div>` : ''}
    <div class="pl-btns"><a class="btn primary press" href="#/deck/${encodeURIComponent(d.deck)}">Open deck</a>
      <button class="btn ghost" data-scope="flow">▶ Flow now</button><button class="btn ghost" data-scope="add">+ Add to flow</button><button class="btn ghost" data-putback>↩ Put back</button></div>
  </div>`;
}
function renderCabinet() {
  const sort = P.get('sort', 'neet'), group = P.get('group', 'sys'), size = P.get('spine', 'm');
  let body;
  if (!S.library) body = `<div class="empty"><p>${status.state === 'error' ? 'Could not reach your Drive: ' + esc(status.error) : 'Fetching your library…'}</p></div>`;
  else {
    const groups = group === 'all' ? [{ name: 'All decks', label: 'All decks', decks: S.library.decks, all: true }] : systems();
    body = groups.map(g => {
      const decks = sortDecks(g.decks, sort), stars = decks.reduce((t, d) => t + (d.star || 0), 0), cards = decks.reduce((t, d) => t + d.cards, 0);
      const hasPulled = pulled && decks.some(d => d.deck === pulled);
      return `<section class="shelfsec">
        ${g.all ? `<span class="plate static"><span class="pl-n">All decks</span><span class="mono">✦ ${stars} · ${decks.length} decks · ${cards} cards</span></span>`
          : `<a class="plate" href="#/sys/${sysNum(g.name)}" aria-label="Fan out ${esc(g.label)}"><span class="pl-n">${esc(g.label)}</span><span class="mono">✦ ${stars} · ${decks.length} decks · ${cards} cards</span></a>`}
        <div class="shelf sz-${size}">${decks.map(d => spine(d, d.deck === pulled)).join('')}</div>
        ${hasPulled ? pulledPanel(deckMeta(pulled)) : ''}
      </section>`;
    }).join('');
  }
  app.innerHTML = `<div class="screen cabinet">
    ${topBar()}
    <div class="scroll pad shelfwrap">
      <div class="shelf-side">${loftButton()}
      <div class="shelf-ctl">
        <div class="chips nowrap-row">${SORTS.map(([k, l]) => `<button class="chip${sort === k ? ' on' : ''}" data-sort="${k}">${l}</button>`).join('')}</div>
        <div class="ctl-row"><span class="seg"><button class="${group === 'sys' ? 'on' : ''}" data-group="sys">By system</button><button class="${group === 'all' ? 'on' : ''}" data-group="all">All decks</button></span><a class="chip dash" href="#/sys/all" aria-label="Mosaic of every card">▦ Eagle view</a>
          <span class="sizes mono" aria-label="Spine size">${['s', 'm', 'l'].map(z => `<button class="${size === z ? 'on' : ''}" data-size="${z}">${z.toUpperCase()}</button>`).join('')}</span></div>
      </div></div>
      <div class="shelf-main">${body}</div>
    </div>
    ${nav('shelf')}
  </div>`;
  bindGo();
  app.querySelectorAll('[data-sort]').forEach(b => b.onclick = () => { P.set('sort', b.dataset.sort); renderCabinet(); });
  app.querySelectorAll('[data-group]').forEach(b => b.onclick = () => { P.set('group', b.dataset.group); renderCabinet(); });
  app.querySelectorAll('[data-size]').forEach(b => b.onclick = () => { P.set('spine', b.dataset.size); renderCabinet(); });
  app.querySelectorAll('.spine').forEach(b => b.onclick = () => {
    const d = b.dataset.deck;
    const sc = app.querySelector('.scroll'), y = sc.scrollTop;
    pulled = pulled === d ? null : d;                     // second tap on the same spine puts the deck back
    renderCabinet();
    const s2 = app.querySelector('.scroll'); s2.scrollTop = y;
    const pl = $('#pulled'); if (pl) setTimeout(() => pl.scrollIntoView({ block: 'nearest', behavior: 'smooth' }), 60);
  });
  const pl = $('#pulled');
  hideTip();
  if (pl) {
    bindTips(pl);
    pl.querySelectorAll('[data-scope]').forEach(b => b.onclick = () => openScope(pulled, b.dataset.scope));
    const pb = pl.querySelector('[data-putback]');
    if (pb) pb.onclick = () => { const sc = app.querySelector('.scroll'), y = sc.scrollTop; pulled = null; renderCabinet(); app.querySelector('.scroll').scrollTop = y; };
  }
}

function deckBack(d, mini) {
  const t = tier(d.star || 0), w = walked(d.deck), ok = isReady(d.deck);
  const pct = d.cards ? Math.round(100 * w / d.cards) : 0;
  const face = `<span class="back t-${t}${mini ? ' mini' : ''}${d.topupDeck ? ' tu' : ''}" style="--tone:${emblem(d.system, d.deck).tone}">
      <span class="frame1"></span><span class="frame2"></span>
      <span class="back-top mono"><span>${esc(d.deck)}</span><span>✦ ${d.star || 0}</span></span>
      <span class="back-seal">${seal(d.system, '', d.deck)}</span>
      <span class="back-title" style="font-size:${titleSize(d.title, mini)}" title="${esc(d.title)}">${esc(d.title)}</span>
      <span class="back-foot mono"><span>${d.cards} CARDS${!d.topupDeck && hasTopups(d.deck) ? ' +' + ((S.xtopups && S.xtopups[d.deck]) || S.qb.topups[d.deck]).length + ' TU' : ''}</span><span>${d.topupDeck ? 'TOP-UP DECK' : ok ? TIER_NAME[t] : 'NOT DOWNLOADED'}</span></span>
    </span>`;
  if (mini) return face;
  return `<a class="deck${ok ? '' : ' notready'}" href="#/deck/${encodeURIComponent(d.deck)}" aria-label="Open ${esc(d.title)}">${face}
    <span class="prog mono"><span class="bar"><span style="width:${pct}%"></span></span><span>${w}/${d.cards}</span></span></a>`;
}

/* ============================ one system: fanned out, or as a mosaic ============================ */
function renderSystem(num) {
  const all = num === 'all';
  const s = all ? (S.library ? { name: 'all', label: 'Eagle view · every card', decks: S.library.decks } : null) : systems().find(x => sysNum(x.name) === num);
  if (!s) return renderCabinet();
  const tab = all ? 'mosaic' : P.get('sysTab', 'decks'), sort = P.get('sort', 'neet'), mp = P.get('moPool', 'all'), mw = P.get('moWalk', ''), mst = 'any';
  // T-095: a Viva package lights its cards instead of the pools, and Flow lit walks them in question order
  const vv = vivaPkg(P.get('moViva', '')) ? P.get('moViva', '') : '', vset = vv ? vivaKeys(vv) : null;
  const litOk = c => vset ? vset.has(c.deck + '|' + c.code) : inPool(c, mp) && walkOk(c, mw);
  const pickW = deck => cardsOf(deck).filter(litOk);
  const hitN = d => pickW(d.deck).length, cn = P.get('cnames', false), pk = P.get('pickOn', false);
  const decks = sort === 'hits' ? s.decks.slice().sort((a, b) => hitN(b) - hitN(a) || a.deck.localeCompare(b.deck, undefined, { numeric: true })) : sortDecks(s.decks, sort);
  const stars = decks.reduce((t, d) => t + (d.star || 0), 0), cards = decks.reduce((t, d) => t + d.cards, 0), w = decks.reduce((t, d) => t + walked(d.deck), 0);
  let body, litList = [];
  if (tab === 'mosaic') {
    // lit cards in the order the mosaic shows them (Eagle view: system by system)
    const shown = all ? systems().flatMap(g => decks.filter(d => d.system === g.name)) : decks;
    litList = shown.flatMap(d => pickW(d.deck));
    if (vv) { const inShown = new Set(shown.map(d => d.deck)); litList = vivaQueue(vv).list.filter(c => inShown.has(c.deck)); }
    body = `<div class="legend mono"><span>SEEN</span>${[0, 1, 2, 3].map(n => `<span class="lg s${n}">${n === 3 ? '3+' : n}</span>`).join('')}<span class="lg-n">gold ring = NEET</span><span class="lg-n"><i class="lg-tu"></i>coral corner = Top-up</span></div>
      ${vv ? '' : poolChips(mp, 'data-mp')}
      ${vivaPkgs().length ? `<div class="chips mo-pools mo-viva"><span class="mono muted small">VIVA</span>${vivaPkgs().map(p => `<button class="chip vchip-p${vv === p.package ? ' on' : ''}" data-mviva="${esc(p.package)}" aria-pressed="${vv === p.package}">${vv === p.package ? '✓ ' : ''}${esc(p.package)} · ${esc(p.title)}</button>`).join('')}${vv ? `<a class="chip dash" href="#/viva/${esc(vv)}">${vivaPkg(vv).questions.length} questions ›</a>` : ''}</div>` : ''}
      <div class="chips mo-pools">${vv ? '' : WALKS.map(([k, l]) => `<button class="chip${walkParts(mw).includes(k) ? ' on' : ''}" data-mw="${k}" aria-pressed="${walkParts(mw).includes(k)}">${walkParts(mw).includes(k) ? '✓ ' : ''}${l}</button>`).join('')}${vv ? '' : '<span class="pool-sep" aria-hidden="true">|</span>'}<button class="chip dash${cn ? ' on' : ''}" data-cnames aria-pressed="${cn}">${cn ? '✓ ' : ''}Chunk names</button><button class="chip pickchip${pk ? ' on' : ''}" data-pick aria-pressed="${pk}">${pk ? '✓ Pick on' : 'Pick'}</button><span class="mono mo-sum">${decks.reduce((t, d) => t + hitN(d), 0)} of ${decks.reduce((t, d) => t + cardsOf(d.deck).length, 0)} cards lit</span></div>
      <div class="mosaic">${(all ? systems().map(g => ({ g, ds: decks.filter(d => d.system === g.name) })) : [{ g: null, ds: decks }]).map(({ g, ds }) => (g ? `<div class="mo-sys mono">${esc(g.label)} · ${ds.reduce((t, d) => t + hitN(d), 0)}</div>` : '') + ds.map(d => {
        const cs = cardsOf(d.deck), lit = litOk;
        return `<div class="mo-row${d.topupDeck ? ' tu' : ''}"><a class="mo-l mono" href="#/deck/${encodeURIComponent(d.deck)}"><b>${esc(d.deck)}</b><span>${d.topupDeck ? 'TOP-UP' : d.star ? '✦ ' + d.star : ''}${mp !== 'all' || mw ? ' · ' + hitN(d) : ''}</span></a>
          <span class="mo-cells${cn ? ' named' : ''}">${cs.length ? chunked(cs, c => `<button class="mo s${shade(seen(c.deck, c.no))}${isNeet(c) ? ' ng' : ''}${c.topup || c.tdeck ? (seen(c.deck, c.no) ? ' tu tu1' : ' tu') : ''}${c.vcard ? ' vv' : ''}${lit(c) ? '' : ' off'}" data-deck="${esc(c.deck)}" data-code="${esc(c.code)}" data-tip="${esc(tipOf(c))}" aria-label="${esc(tipOf(c))}, seen ${seen(c.deck, c.no)}"></button>`, cn) : '<span class="muted small">not downloaded</span>'}</span></div>`;
      }).join('')).join('')}</div>`;
  } else {
    body = `<div class="spread">${decks.map((d, i) => `<div class="fan" style="--rot:${[-1.5, 1.2, 0.8, -1, 1.4, -0.8, -1.2, 1][i % 8]}deg">${deckBack(d)}</div>`).join('')}</div>`;
  }
  app.innerHTML = `<div class="screen sysv">
    <header class="top col">
      <div class="row"><a class="iconbtn" href="#/shelf" aria-label="Back to the shelf">${ICON.back}</a>
        <span class="tt"><span class="mono kick">${all ? 'ALL' : num} · ✦ ${stars} · ${decks.length} DECKS · ${cards} CARDS · ${w} WALKED</span><span class="h1s">${esc(s.label)}</span></span></div>
      <div class="row sb">${all ? '<span></span>' : `<span class="seg"><button class="${tab === 'decks' ? 'on' : ''}" data-tab="decks">Decks</button><button class="${tab === 'mosaic' ? 'on' : ''}" data-tab="mosaic">Mosaic</button></span>`}
        <span class="chips nowrap-row small">${SORTS.slice(0, 3).concat(tab === 'mosaic' ? [['hits', 'Most lit']] : []).map(([k, l]) => `<button class="chip${sort === k ? ' on' : ''}" data-sort="${k}">${l}</button>`).join('')}</span></div>
    </header>
    <div class="scroll pad">${body}</div>
    ${tab === 'mosaic' ? (pk ? pickBar() : litBar(litList)) : ''}
    ${nav('shelf')}
  </div>`;
  bindGo(); hideTip();
  if (tab === 'mosaic') {
    bindTips(app);
    const lab = vv ? 'Viva ' + vv + ' · ' + vivaPkg(vv).title : (all ? 'All decks' : s.label) + ' · ' + [poolName(mp), walkName(mw)].filter(Boolean).join(' · ');
    const lf = app.querySelector('[data-litflow]'), la = app.querySelector('[data-litadd]');
    if (lf) lf.onclick = () => { hideTip(); startFlow(litList, { label: lab, returnTo: location.hash, viva: vv }); };
    app.querySelectorAll('[data-mviva]').forEach(b => b.onclick = () => { P.set('moViva', vv === b.dataset.mviva ? '' : b.dataset.mviva); keep(() => renderSystem(num)); });
    if (la) la.onclick = () => addLit(litList, lab);
    const cb = app.querySelector('[data-cnames]'); if (cb) cb.onclick = () => { P.set('cnames', !cn); keep(() => renderSystem(num)); };
    const pb = app.querySelector('[data-pick]'); if (pb) pb.onclick = () => { P.set('pickOn', !pk); if (pk) { pickSel.clear(); pickAnchor = null; P.set('pickForPlan', false); } keep(() => renderSystem(num)); };
    app.querySelectorAll('[data-mw]').forEach(b => b.onclick = () => { P.set('moWalk', toggleWalk(mw, b.dataset.mw)); keep(() => renderSystem(num)); });
    if (pk) bindPick(litList, lab, all ? 'All decks' : s.label, [poolName(mp), walkName(mw)].filter(x => x && x !== 'All').join(' · '));
  }
  app.querySelectorAll('[data-tab]').forEach(b => b.onclick = () => { P.set('sysTab', b.dataset.tab); renderSystem(num); });
  app.querySelectorAll('[data-sort]').forEach(b => b.onclick = () => { P.set('sort', b.dataset.sort); renderSystem(num); });
  app.querySelectorAll('[data-mp]').forEach(b => b.onclick = () => { P.set('moPool', togglePool(mp, b.dataset.mp)); renderSystem(num); });
  app.querySelectorAll('[data-mst]').forEach(b => b.onclick = () => { P.set('moState', b.dataset.mst); renderSystem(num); });
  app.querySelectorAll('.mo').forEach(b => b.onclick = () => {
    hideTip();
    if (P.get('pickOn', false) && tab === 'mosaic') return;          // Pick mode: tiles select (bindPick), they don't open
    const list = cardsOf(b.dataset.deck);
    startFlow(list, { browse: true, start: list.findIndex(c => c.code === b.dataset.code), label: 'Look', returnTo: location.hash });
  });
}

/* ============================ deck ============================ */
const deckFilter = {};
function filtersFor(deck, cards) {
  return [
    ...POOLS.map(([key, label]) => ({ key, label, list: cards.filter(c => inPool(c, key)) })),
    { key: 'low', label: 'Seen ≤ 1', list: cards.filter(c => seen(deck, c.no) <= 1) },
    { key: 'new', label: 'Unseen', list: cards.filter(c => seen(deck, c.no) === 0) },
    { key: 'edited', label: 'Edited', list: cards.filter(c => c.edited) }
  ].filter(f => f.key === 'all' || f.list.length);
}
function sectionsOf(cards) {            // chunks, in card order (War Map Chunks tab; see chunkOf)
  const out = [];
  for (const c of cards) {
    const ch = chunkOf(c), last = out[out.length - 1];
    if (last && last.key === ch.key) last.cards.push(c); else out.push({ key: ch.key, name: ch.name, cards: [c] });
  }
  return out;
}
// Small gap between chunks (card sections) in every strip of tiles; with names on, each chunk starts with its name.
function chunked(cards, tileFn, names) {
  let out = '', prev = null;
  cards.forEach((c, i) => {
    const ch = chunkOf(c);
    if (i === 0 || ch.key !== prev) {
      if (i > 0) out += '<span class="cgap" aria-hidden="true"></span>';
      if (names) out += `<span class="cname mono">${esc(ch.name)}</span>`;
    }
    prev = ch.key;
    out += tileFn(c);
  });
  return out;
}
const tipOf = c => `${c.deck} · ${chunkOf(c).name} · ${c.vcard ? c.code + ' · Viva' : 'card ' + c.no}${neetTag(c) ? ' · ' + neetTag(c) : ''}${c.topup ? ' · Top-up' : ''}`;
// Hover label for tiles: mouse on the Mac, S Pen hovering on the Tab and the phone (touch never shows it).
function bindTips(root) {
  let tip = document.getElementById('hovtip');
  if (!tip) { tip = document.createElement('div'); tip.id = 'hovtip'; tip.className = 'hovtip mono'; document.body.appendChild(tip); }
  tip.hidden = true;
  root.querySelectorAll('[data-tip]').forEach(el => {
    el.addEventListener('pointerover', e => {
      if (e.pointerType === 'touch') return;
      tip.textContent = el.dataset.tip; tip.hidden = false;
      const r = el.getBoundingClientRect();
      tip.style.left = Math.max(8, Math.min(window.innerWidth - tip.offsetWidth - 8, r.left + r.width / 2 - tip.offsetWidth / 2)) + 'px';
      tip.style.top = Math.max(8, r.top - tip.offsetHeight - 8) + 'px';
    });
    el.addEventListener('pointerleave', () => { tip.hidden = true; });
  });
}
function hideTip() { const t = document.getElementById('hovtip'); if (t) t.hidden = true; }
// Lit cards → Flow now or today's target, keeping the order they are shown in.
async function addLit(list, label) {
  if (!list.length) { toast('No lit cards.'); return; }
  const by = new Map();
  list.forEach(c => { if (!by.has(c.deck)) by.set(c.deck, []); by.get(c.deck).push(c.no); });
  await addTarget([...by].map(([deck, nos]) => ({ deck, label, nos })));
  toast(`Added ${list.length} card${list.length === 1 ? '' : 's'} to today’s target.`);
  if (hasBackend()) sync({ downloadAll: false });
}
// Pick mode: tap a first tile, then a last tile (a range of lit cards); tap a deck name or a chunk name for all of it.
const pickSel = new Set(); let pickAnchor = null;
function pickBar() {
  return `<div class="buildfoot litbar pickbar">
    <div class="sumrow mono"><span data-pick-sum></span><span data-pick-hint></span></div>
    <div class="two"><button class="big press" data-pick-plan>ADD TO PLAN</button><button class="btn ghost" data-pick-flow>+ Add to flow</button><button class="btn ghost" data-pick-clear>Clear</button></div>
  </div>`;
}
function bindPick(litList, lab, name, sub) {
  const order = litList.map(c => c.deck + '|' + c.code), byKey = new Map(litList.map(c => [c.deck + '|' + c.code, c]));
  const tiles = new Map(); app.querySelectorAll('.mo').forEach(b => tiles.set(b.dataset.deck + '|' + b.dataset.code, b));
  const paint = () => {
    tiles.forEach((b, k) => { b.classList.toggle('sel', pickSel.has(k)); b.classList.toggle('anc', pickAnchor === k); });
    const list = order.filter(k => pickSel.has(k)).map(k => byKey.get(k)), nNew = list.filter(c => !seen(c.deck, c.no)).length;
    app.querySelector('[data-pick-sum]').innerHTML = list.length ? `<b>${list.length}</b> picked · ${nNew} new · ${list.length - nNew} to revise` : '<b>0</b> picked';
    app.querySelector('[data-pick-hint]').textContent = pickAnchor ? 'now tap the last tile' : list.length ? 'tap more, or a deck name' : 'tap a first tile, then a last tile';
  };
  const toggleKeys = keys => { const all = keys.every(k => pickSel.has(k)); keys.forEach(k => all ? pickSel.delete(k) : pickSel.add(k)); };
  tiles.forEach((b, k) => b.addEventListener('click', () => {
    if (b.classList.contains('off')) return;
    if (pickAnchor && pickAnchor !== k) {
      const a = order.indexOf(pickAnchor), z = order.indexOf(k);
      if (a >= 0 && z >= 0) order.slice(Math.min(a, z), Math.max(a, z) + 1).forEach(x => pickSel.add(x));
      pickAnchor = null;
    } else if (pickAnchor === k) { pickAnchor = null; }
    else if (pickSel.has(k)) { pickSel.delete(k); }
    else { pickSel.add(k); pickAnchor = k; }
    paint();
  }));
  app.querySelectorAll('.mo-l').forEach(a => a.addEventListener('click', e => {
    e.preventDefault(); const deck = decodeURIComponent(a.getAttribute('href').split('/').pop());
    toggleKeys(order.filter(k => k.startsWith(deck + '|'))); pickAnchor = null; paint();
  }));
  app.querySelectorAll('.cname').forEach(el => el.addEventListener('click', () => {
    const keys = []; let n = el.nextElementSibling;
    while (n && !n.classList.contains('cgap') && !n.classList.contains('cname')) { if (n.classList.contains('mo') && !n.classList.contains('off')) keys.push(n.dataset.deck + '|' + n.dataset.code); n = n.nextElementSibling; }
    toggleKeys(keys); pickAnchor = null; paint();
  }));
  const chosen = () => order.filter(k => pickSel.has(k));
  app.querySelector('[data-pick-plan]').onclick = () => {
    const keys = chosen(); if (!keys.length) { toast('Pick some cards first.'); return; }
    const decks = [...new Set(keys.map(k => k.split('|')[0]))];
    planPending = { name: decks.length <= 3 ? decks.join(' + ') : name, sub, keys };
    pickSel.clear(); pickAnchor = null; P.set('pickOn', false); P.set('pickForPlan', false);
    if (!currentStretch()) newStretch({});
    go('#/plan');
  };
  app.querySelector('[data-pick-flow]').onclick = () => { const keys = chosen(); if (!keys.length) { toast('Pick some cards first.'); return; } addLit(keys.map(k => byKey.get(k)), lab); };
  app.querySelector('[data-pick-clear]').onclick = () => { pickSel.clear(); pickAnchor = null; paint(); };
  paint();
}
function litBar(list) {
  const avg = avgPace() || 75000;
  return `<div class="buildfoot litbar">
    <div class="sumrow mono"><span><b>${list.length}</b> lit card${list.length === 1 ? '' : 's'}</span><span>≈ ${Math.max(list.length ? 1 : 0, Math.round(list.length * avg / 60000))} min at your pace</span></div>
    <div class="two"><button class="big press" data-litflow ${list.length ? '' : 'disabled'}>${ICON.walkS}FLOW LIT</button><button class="btn ghost" data-litadd ${list.length ? '' : 'disabled'}>+ Add lit to flow</button></div>
  </div>`;
}

function renderDeck(code) {
  const m = deckMeta(code);
  if (!m) return renderCabinet();
  _lastDeck = code;
  const cards = cardsOf(code), t = tier(m.star || 0), size = P.get('tile', 'm');
  const df = deckFilter[code] || (deckFilter[code] = { pool: 'all', st: 'any' });
  const cur = { list: pick2(code, df.pool, df.st) };
  const inSet = new Set(cur.list.map(c => c.code));
  const st = deckState(code), neetN = cards.filter(c => isNeet(c)).length;
  const tiles = sectionsOf(cards).map(sec => `<section class="dsec"><div class="rule-h"><span class="h3">${esc(sec.name || 'Cards')}</span><span class="line"></span><span class="mono muted small">${sec.cards[0].no}–${sec.cards[sec.cards.length - 1].no}</span></div>
    <div class="tiles tz-${size}">${sec.cards.map(c => tile(c, inSet.has(c.code))).join('')}</div></section>`).join('');
  app.innerHTML = `<div class="screen deckv">
    <div class="dhead slim t-${t}" style="--tone:${emblem(m.system, code).tone}">
      <div class="dhead-row"><a class="iconbtn on-foil" href="#/shelf" aria-label="Back to the shelf">${ICON.back}</a>
        <span class="dh-t"><span class="mono kick">${esc(code)} · ${TIER_NAME[t]} · ✦ ${m.star || 0}</span><span class="dh-n">${esc(m.title)}</span></span>
        ${seal(m.system, 'hseal', code)}</div>
      <div class="dstats mono"><span><b>${m.cards}</b> cards</span><span><b>${walked(code)}</b> walked</span><span><b>${neetN}</b> NEET cards</span>${cards.some(c => c.topup) ? `<span><b>${cards.filter(c => c.topup).length}</b> Top-up</span><span><b>${cards.filter(c => inPool(c, 'hit')).length}</b> with a hit</span>` : ''}</div>
    </div>
    <div class="scroll pad">
      ${st !== 'ready' ? `<div class="notice">${st === 'missing' ? 'This deck is not on this device yet.' : 'A newer version of this deck is waiting.'} <button class="link" data-act="dl">Download now</button></div>` : ''}
      ${poolChips(df.pool, 'data-dp', k => pick2(code, k === 'all' || k === 'hit' ? k : k, df.st).length)}
      <div class="chips">${STATES_DECK.map(([k, l]) => { const n = pick2(code, df.pool, k).length; return n || k === 'any' || k === df.st ? `<button class="chip${df.st === k ? ' on' : ''}" data-ds="${k}">${l} · ${n}</button>` : ''; }).join('')}<span class="mono muted small lit">${cur.list.length} of ${cards.length} lit</span></div>
      <div class="ctl-row mt"><span class="legend mono"><span>SEEN</span>${[0, 1, 2, 3].map(n => `<span class="lg s${n}">${n === 3 ? '3+' : n}</span>`).join('')}</span>
        <span class="sizes mono" aria-label="Card tile size">${['s', 'm', 'l'].map(z => `<button class="${size === z ? 'on' : ''}" data-size="${z}">${z.toUpperCase()}</button>`).join('')}</span></div>
      ${voiceOn() && cards.length ? '<div class="vdeck" id="vdeck"><span class="mono kick">VOICE</span><span class="vd-s muted small">checking…</span><button class="pillbtn" data-vmake hidden>Make voice</button></div>' : ''}
      ${cards.length ? tiles : '<p class="muted">No cards on this device yet.</p>'}
      <p class="muted small mt">Tap a card to look through it. Looking is never timed or logged; only Flow counts.</p>
    </div>
    <div class="dfoot two">
      <button class="big press" data-scope="flow">${ICON.walkS}FLOW NOW</button>
      <button class="btn ghost" data-scope="add">+ Add to flow</button>
    </div>
  </div>`;
  bindGo();
  app.querySelectorAll('[data-dp]').forEach(b => b.onclick = () => { df.pool = togglePool(df.pool, b.dataset.dp); renderDeck(code); });
  app.querySelectorAll('[data-ds]').forEach(b => b.onclick = () => { df.st = b.dataset.ds; renderDeck(code); });
  app.querySelectorAll('[data-size]').forEach(b => b.onclick = () => { P.set('tile', b.dataset.size); renderDeck(code); });
  const dl = app.querySelector('[data-act=dl]');
  if (dl) dl.onclick = async () => { dl.disabled = true; try { await downloadDecks([code]); toast('Downloaded and checked.'); } catch (e) { toast(e.message); } emit(); };
  app.querySelectorAll('[data-scope]').forEach(b => b.onclick = () => openScope(code, b.dataset.scope, df));
  if (voiceOn() && cards.length) vDeckBox(code, cards);
  app.querySelectorAll('.tile').forEach(el => el.onclick = () => {
    const list = cur.list.find(c => c.code === el.dataset.code) ? cur.list : cards;
    startFlow(list, { browse: true, start: list.findIndex(c => c.code === el.dataset.code), label: 'Look', returnTo: location.hash });
  });
}
// T-099: how much of this deck has its voice, and a button to make the rest (the bridge makes it, a few points a call)
async function vDeckBox(code, cards) {
  const box = document.getElementById('vdeck'); if (!box) return;
  const s = box.querySelector('.vd-s'), b = box.querySelector('[data-vmake]');
  await deckIndex(code);
  const parts = cards.flatMap(c => partsOf(c, xParts(c))), have = parts.filter(p => hasClip(code, p)).length;
  if (!box.isConnected) return;
  s.textContent = have === parts.length ? `All ${parts.length} points have their voice.` : `${have} of ${parts.length} points have their voice.`;
  b.hidden = have === parts.length;
  if (makingDeck()) { b.disabled = true; b.textContent = 'Making ' + makingDeck() + '…'; }
  b.onclick = async () => {
    b.disabled = true; b.textContent = 'Making…';
    const r = await makeDeck(code, cards.map(c => ({ c, extra: xParts(c) })), st => { if (s.isConnected) s.textContent = `Making ${st.done} of ${st.total}…${st.used != null ? ` · this month ${Math.round(st.used / 60)} of ${Math.round(st.limit / 60)} min` : ''}`; });
    if (!box.isConnected) return;
    b.disabled = false; b.textContent = 'Make voice';
    if (r.error) toast('Voice stopped: ' + r.error);
    vDeckBox(code, cards);
  };
}
function tile(c, active) {
  const n = seen(c.deck, c.no), tag = neetTag(c);
  return `<button class="tile s${shade(n)}${active ? '' : ' dim'}${tag ? ' ng' : ''}${c.topup || c.tdeck ? (seen(c.deck, c.no) ? ' tu tu1' : ' tu') : ''}" data-code="${esc(c.code)}" aria-label="Card ${c.no}, seen ${n} times${tag ? ', ' + tag : ''}">
    <span class="tl-top mono"><span>${c.topup ? 'TOP-UP' : tag ? '✦' : esc(c.code)}</span><span>×${n}</span></span>
    <span class="tl-no">${c.no}</span>
    <span class="tl-tag mono">${esc(tag)}${c.edited ? ' ✎' : ''}</span></button>`;
}

/* ============================ scope sheet: Flow now / Add to flow from one deck ============================ */
const STATES = [['any', 'Any'], ['new', 'Unseen'], ['low', 'Seen ≤ 1'], ['stale', 'Not seen 7+ days']];
const STATES_DECK = STATES.concat([['edited', 'Edited']]);
const poolLabel = k => poolName(k);
// All · Any hit · then components that add up (tap several: NEET + DocT GT, DocT + Marrow, …). count(k) optional.
function poolChips(cur, attr, count) {
  const parts = poolParts(cur), on = k => k === 'all' ? !parts.length : k === 'hit' ? parts[0] === 'hit' : parts.includes(k);
  const n = k => count ? ' · ' + count(k) : '';
  return `<div class="chips pool">${[['all', 'All'], ['hit', 'Any hit']].map(([k, l]) => `<button class="chip${on(k) ? ' on' : ''}" ${attr}="${k}">${l}${n(k)}</button>`).join('')}<span class="pool-sep" aria-hidden="true">|</span>${COMPONENTS.map(([k, l]) => `<button class="chip comp${on(k) ? ' on' : ''}" ${attr}="${k}" aria-pressed="${on(k)}">${on(k) ? '✓ ' : '+ '}${l}${n(k)}</button>`).join('')}</div>`;
}
const stateLabel = k => (STATES.find(p => p[0] === k) || ['', k])[1];
function inState(c, st) {
  if (!st || st === 'any') return true;
  if (st === 'new') return seen(c.deck, c.no) === 0;
  if (st === 'low') return seen(c.deck, c.no) <= 1;
  if (st === 'stale') return lastSeen(c.deck, c.no) < Date.now() - 7 * 864e5;
  if (st === 'edited') return !!c.edited;
  return true;
}
const pick2 = (deck, pool, st) => cardsOf(deck).filter(c => inPool(c, pool) && inState(c, st));
function scopeCards(deck, key) {
  const cards = cardsOf(deck);
  if (key === 'entire' || key === 'all') return cards;
  if (POOLS.some(p => p[0] === key)) return cards.filter(c => inPool(c, key));
  if (key === 'new') return cards.filter(c => seen(deck, c.no) === 0);
  if (key === 'low') return cards.filter(c => seen(deck, c.no) <= 1);
  if (key === 'stale') { const lim = Date.now() - 7 * 864e5; return cards.filter(c => lastSeen(deck, c.no) < lim); }
  if (key === 'edited') return cards.filter(c => c.edited);
  return cards;
}
function openScope(deck, mode, preset) {
  const m = deckMeta(deck), cards = cardsOf(deck);
  if (!m) return;
  if (!cards.length) { toast('This deck is not on this device yet.'); return; }
  const secs = sectionsOf(cards);
  let pool = (preset && preset.pool) || 'all';
  let st = preset && STATES.some(p => p[0] === preset.st) ? preset.st : 'any';
  const secPick = new Set();
  const wrap = document.createElement('div');
  wrap.className = 'modal';
  const draw = () => {
    let sel;
    if (secPick.size) sel = secs.filter((s, i) => secPick.has(i)).flatMap(s => s.cards);
    else sel = pick2(deck, pool, st);
    const avg = avgPace() || 75000;
    wrap.innerHTML = `<div class="sheet scope" role="dialog" aria-label="What to take from ${esc(deck)}">
      <span class="grab" aria-hidden="true"></span>
      <div class="sheet-h"><span><span class="mono kick">${esc(deck)} · WHAT TO TAKE</span><span class="sh-t">${esc(m.title)}</span></span><button class="iconbtn" data-x aria-label="Close">${ICON.close}</button></div>
      <span class="mono lab">WHICH CARDS · widest pool first</span>
      ${poolChips(secPick.size ? '' : pool, 'data-k', k => pick2(deck, k, st).length)}
      <span class="mono lab">SEEN</span>
      <div class="chips">${STATES.map(([k, l]) => `<button class="chip${!secPick.size && st === k ? ' on' : ''}" data-st="${k}">${!secPick.size && st === k ? '✓ ' : ''}${l} · ${pick2(deck, pool, k).length}</button>`).join('')}</div>
      <span class="mono lab">OR PICK SECTIONS (CHUNKS)</span>
      <div class="seclist">${secs.map((s, i) => `<label><input type="checkbox" data-s="${i}" ${secPick.has(i) ? 'checked' : ''}><span>${esc(s.name || 'Cards')}</span><span class="mono">${s.cards[0].no}–${s.cards[s.cards.length - 1].no} · ${s.cards.length}</span></label>`).join('')}</div>
      <div class="sumrow mono"><span><b>${sel.length}</b> cards selected</span><span>≈ ${Math.max(1, Math.round(sel.length * avg / 60000))} min at your pace</span></div>
      <div class="sheet-f"><button class="big press" data-go-flow ${sel.length ? '' : 'disabled'}>${ICON.walkS}FLOW NOW</button><button class="btn ghost" data-add ${sel.length ? '' : 'disabled'}>+ Add to flow<small>today’s target</small></button></div>
    </div>`;
    wrap.querySelector('[data-x]').onclick = () => wrap.remove();
    wrap.querySelectorAll('[data-k]').forEach(b => b.onclick = () => { secPick.clear(); pool = togglePool(pool, b.dataset.k); draw(); });
    wrap.querySelectorAll('[data-st]').forEach(b => b.onclick = () => { secPick.clear(); st = b.dataset.st; draw(); });
    wrap.querySelectorAll('[data-s]').forEach(b => b.onchange = () => { const i = +b.dataset.s; b.checked ? secPick.add(i) : secPick.delete(i); draw(); });
    const label = secPick.size ? secs.filter((s, i) => secPick.has(i)).map(s => s.name).join(', ') : [pool !== 'all' ? poolLabel(pool) : '', st !== 'any' ? stateLabel(st) : ''].filter(Boolean).join(' · ');
    wrap.querySelector('[data-go-flow]').onclick = () => { wrap.remove(); startFlow(sel, { label, returnTo: location.hash }); };
    wrap.querySelector('[data-add]').onclick = async () => { await addTarget([{ deck, label, nos: sel.map(c => c.no) }]); wrap.remove(); toast(`Added ${sel.length} cards to today’s target.`); if (hasBackend()) sync({ downloadAll: false }); };
  };
  wrap.onclick = e => { if (e.target === wrap) wrap.remove(); };
  draw();
  document.body.appendChild(wrap);
  if (mode === 'flow') { /* same sheet; Flow now is the primary button */ }
}

/* ============================ Flow tab: the session desk ============================ */
// Choosing happens on the shelf, a deck, the Mosaic or Eagle view (+ Add to flow). The Flow tab runs the day:
// today's target, continue the last flow, and the Again pile.
const LASTFLOW = 'lastFlow';
function saveLastFlow() {
  if (!flow || flow.browse || flow.pilot) return;
  if (flow.done) { P.set(LASTFLOW, null); return; }
  P.set(LASTFLOW, { keys: flow.queue.map(c => c.deck + '|' + c.code), idx: flow.idx, label: flow.label, ts: Date.now(), viva: flow.viva || '', vl: flow.viva ? flow.queue.map(c => c.vq ? [c.vq.q, c.vq.key, c.vq.again ? 1 : 0] : null) : null });
}
function lastFlowCards() {
  const lf = P.get(LASTFLOW, null);
  if (!lf || !lf.keys || Date.now() - lf.ts > 3 * 864e5) return null;
  const byDeck = new Map(); let out = [];
  // T-138: a viva walk comes back as a viva walk (lessons, spine, seen-above), not as plain cards
  if (lf.viva && lf.vl) {
    const byK = new Map(vivaQueue(lf.viva).list.map(c => [c.vq.q + '|' + c.vq.key, c]));
    out = lf.vl.map(v => { const c = v && byK.get(v[0] + '|' + v[1]); return !c ? null : v[2] ? { ...c, vq: { ...c.vq, bridge: null, again: true } } : c; }).filter(Boolean);
  } else for (const k of lf.keys) {
    const i = k.indexOf('|'), deck = k.slice(0, i), code = k.slice(i + 1);
    if (!byDeck.has(deck)) byDeck.set(deck, new Map(cardsOf(deck).map(c => [c.code, c])));
    const c = byDeck.get(deck).get(code); if (c) out.push(c);
  }
  const left = out.slice(Math.min(lf.idx, out.length));
  return left.length ? { cards: left, done: out.length - left.length, total: out.length, label: lf.label, ts: lf.ts, viva: lf.viva || '' } : null;
}
function againCards() {
  return againList().map(a => { const cs = cardsOf(a.deck); const c = cs.find(x => x.code === a.code) || cs.find(x => x.no === a.no); return c ? ({ ...c, _why: a.why + (a.label ? ' · ' + a.label : '') + (a.cohort != null && a.cohort !== '' ? ' · ' + a.cohort + '% got it' : '') }) : null; }).filter(Boolean);
}
function targetProgress() {
  const items = targetItems(), day = today();
  return items.map(i => ({ ...i, done: i.nos.filter(n => seenOn(i.deck, n, day)).length }));
}
function targetQueue() {
  const day = today(), out = [];
  for (const i of targetItems()) {
    const cs = cardsOf(i.deck), want = new Set(i.nos);
    cs.forEach(c => { if (want.has(c.no) && !seenOn(c.deck, c.no, day)) out.push(c); });
  }
  return out;
}
function targetBlock(openByDefault) {
  const tp = targetProgress(), total = tp.reduce((a, i) => a + i.nos.length, 0), done = tp.reduce((a, i) => a + i.done, 0);
  return `<details class="target"${openByDefault ? ' open' : ''}>
    <summary><span><span class="mono kick">TODAY’S TARGET</span><span class="tg-s">${tp.length ? `${tp.length} part${tp.length === 1 ? '' : 's'} · ${total} cards · <b>${done} done</b>` : 'Nothing set yet'}</span></span>
      ${total > done ? `<button class="pillbtn" data-target-start>${ICON.walkS}Start</button>` : ''}</summary>
    <div class="tg-list">${tp.map(i => `<div class="tg-i"><span class="mono">${esc(i.deck)}</span><span class="tg-w">${esc(i.label || '')}${i.from ? ' · from War Map' : ''}</span><span class="mono">${i.done} / ${i.nos.length}</span><button class="xbtn" data-rm="${i.id}" aria-label="Remove from target">${ICON.close}</button></div>`).join('') || '<p class="muted small">Add cards with + Add to flow from a deck, the shelf, a Mosaic or Eagle view. Targets set in the War Map show here too.</p>'}
      ${status.targetNote ? `<p class="muted small">${esc(status.targetNote)}</p>` : ''}</div>
  </details>`;
}
function bindTarget(rerender) {
  const st = app.querySelector('[data-target-start]');
  if (st) st.onclick = e => { e.preventDefault(); const q = targetQueue(); if (q.length) startFlow(q, { label: 'Target', returnTo: location.hash }); };
  app.querySelectorAll('[data-rm]').forEach(b => b.onclick = async () => { await removeTarget(b.dataset.rm); rerender(); if (hasBackend()) sync({ downloadAll: false }); });
}
/* ============================ viva (T-095) ============================ */
const MARKN = { fluent: 'Fluent', patchy: 'Patchy', blank: 'Blank' };
function vivaTile() {
  const ps = vivaPkgs(); if (!ps.length) return;
  const sc = app.querySelector('.palace-screen'); if (!sc) return;
  // T-125: one Viva button; the packages are listed in order inside it
  const nq = ps.reduce((n, p) => n + p.questions.length, 0);
  sc.insertAdjacentHTML('beforeend', `<div class="viva-tiles"><a class="viva-tile mono" href="#/viva"><b>VIVA</b><span>${ps.length} package${ps.length === 1 ? '' : 's'} · ${nq} Qs</span></a></div>`);
}
// T-102: lessons autoplay (per session) — open → each card's lesson → close → spine run on their own
const vAuto = () => { try { return sessionStorage.getItem('trace.vauto') === '1'; } catch (e) { return false; } };
const setVAuto = on => { try { sessionStorage.setItem('trace.vauto', on ? '1' : '0'); } catch (e) { /* */ } if (flow) flow.vauto = on; };
function lessonPic(x, c) {
  const L = x.L; if (!L.pic) return '';
  // a card's own figure: cut from its PDF page into data/viva/img/<pkg>/card_<DECK>_<CODE>.png (button if it is not there)
  if (L.pic === 'card' || /^card:/.test(L.pic)) {
    const key = (L.pic === 'card' ? (c ? c.deck + '|' + c.code : '') : L.pic.slice(5)).replace('|', '_');
    return `<figure class="vx-fig ls-fig-img"><img src="${esc(vivaImgSrc(x.pkg, 'card_' + key + '.png'))}" alt="${esc(L.cap || 'Card figure')}" loading="lazy" onerror="this.closest('figure').outerHTML='<button class=&quot;ls-fig mono&quot; data-lcardfig>◈ The card&#39;s figure</button>'"><figcaption>${esc(L.cap || '')}</figcaption></figure>`;
  }
  return `<figure class="vx-fig ls-fig-img"><img src="${esc(vivaImgSrc(x.pkg, L.pic))}" alt="${esc(L.cap || 'Diagram')}" loading="lazy"><figcaption>${esc(L.cap || '')}</figcaption></figure>`;
}
function autoChip() { return `<button class="chip ls-auto${flow && flow.vauto ? ' on' : ''}" data-vauto>${flow && flow.vauto ? 'Autoplay on' : 'Tap to play'}</button>`; }
function bindAutoChip(el, then) { el.querySelectorAll('[data-vauto]').forEach(b => b.onclick = e => { e.stopPropagation(); setVAuto(!flow.vauto); el.querySelectorAll('[data-vauto]').forEach(x => { x.classList.toggle('on', flow.vauto); x.textContent = flow.vauto ? 'Autoplay on' : 'Tap to play'; }); then && then(); }); }
function walkViva(pkg, onlyQ) {
  const { list } = vivaQueue(pkg, onlyQ), P2 = vivaPkg(pkg);
  if (!list.length) { toast('These cards are not on this device yet.'); return; }
  startFlow(list, { viva: pkg, label: 'Viva ' + pkg + (onlyQ ? ' · ' + onlyQ : ' · ' + P2.title), returnTo: '#/viva/' + pkg });
}
// T-125: the Viva button opens this list of packages, in order
function renderVivaIndex(ps) {
  app.innerHTML = `<div class="screen vivap">
    <header class="top"><a class="iconbtn" href="#/" aria-label="Back">${ICON.back}</a><span class="tt"><span class="mono kick">VIVA · ${ps.length} PACKAGES</span><span class="h1s">Viva</span></span></header>
    <div class="scroll pad">
      ${ps.map(p => `<a class="vp-q vp-pkg" href="#/viva/${esc(p.package)}"><span class="vp-n mono">${esc(p.package)}</span><span class="vp-t">${esc(p.title)}<small class="mono">${p.questions.length} questions${hasLessons(p.package) ? ' · narrated' : ''}</small></span><span></span><span class="mono muted">›</span></a>`).join('')}
    </div>
    ${nav('flow')}
  </div>`;
}
async function renderViva(pkg) {
  const ps = vivaPkgs();
  if (!pkg && ps.length) return renderVivaIndex(ps);
  const P2 = vivaPkg(pkg);
  if (!P2) { app.innerHTML = `<div class="screen"><header class="top"><a class="iconbtn" href="#/flow" aria-label="Back">${ICON.back}</a><span class="tt"><span class="mono kick">VIVA</span><span class="h1s">No viva package yet</span></span></header><div class="scroll pad"><p class="muted">The package file has not loaded. Open the app online once.</p></div>${nav('flow')}</div>`; return; }
  const m = await vivaMarks(), { missing } = vivaQueue(pkg);
  const missDecks = [...new Set(missing.map(k => /^V/.test(k) ? (P2.cards[k] || {}).deck : k.split('|')[0]))];
  const tally = { fluent: 0, patchy: 0, blank: 0, none: 0 };
  P2.questions.forEach(q => { const k = vivaLast(m, pkg, q.q); tally[k || 'none']++; });
  const gens = []; P2.questions.forEach(q => { let g = gens.find(x => x.g === q.gen); if (!g) gens.push(g = { g: q.gen, qs: [] }); g.qs.push(q); });
  const vcards = Object.values(P2.cards).filter(v => !v.retired).length;
  app.innerHTML = `<div class="screen vivap">
    <header class="top"><a class="iconbtn" href="#/viva" aria-label="Back">${ICON.back}</a><span class="tt"><span class="mono kick">VIVA ${esc(pkg)} · ${P2.questions.length} QUESTIONS · ${vcards} VIVA CARDS</span><span class="h1s">${esc(P2.title)}</span></span></header>
    <div class="scroll pad">
      <section class="dk-box">
        <div class="dk-h"><span><span class="mono kick">WALK</span><span class="dk-t">All ${P2.questions.length} questions, in study order</span></span><button class="pillbtn" data-vwalk>${ICON.walkS}Walk</button></div>
        <p class="muted small">Each question opens with its card, then the cards behind it with a bridge under each answer, then the spine to say in 60 seconds. A card that came under an earlier question shows as “seen above” and is not counted twice.</p>
        <p class="mono small vp-tally"><span class="vm-fluent">${tally.fluent} fluent</span> · <span class="vm-patchy">${tally.patchy} patchy</span> · <span class="vm-blank">${tally.blank} blank</span> · ${tally.none} not marked</p>
        ${(() => { const v = vivaPlanToday(pkg); return v ? `<div class="chips"><button class="chip on" data-vplanwalk>${ICON.walkS} Today’s plan · Q${qNumOf(pkg, v.todayQs[0])}–Q${qNumOf(pkg, v.todayQs[v.todayQs.length - 1])} · ${v.doneToday}/${v.todayQs.length} done</button></div>` : `<div class="chips"><button class="chip dash" data-vplanadd>+ Plan this package</button></div>`; })()}
        <div class="chips"><button class="chip dash" data-vmosaic>▦ Show in the Mosaic</button>${tally.patchy + tally.blank ? `<button class="chip" data-vweak>Walk patchy + blank (${tally.patchy + tally.blank})</button>` : ''}</div>
        ${hasLessons(pkg) ? `<div class="vp-ls" id="vpls"><p class="mono small"><b>LESSONS</b> · <span class="vpls-s">checking…</span></p><div class="chips">${autoChipPage()}<button class="chip" data-lmake1 hidden></button><button class="chip" data-lmake hidden></button></div></div>` : ''}
        ${missDecks.length ? `<p class="warn small">${missing.length} card${missing.length === 1 ? '' : 's'} sit on deck${missDecks.length === 1 ? '' : 's'} not on this device (${missDecks.map(esc).join(', ')}); the walk leaves them out.</p>` : ''}
      </section>
      ${gens.map(g => `<section class="vp-gen"><h3 class="mono">${esc(g.g)}</h3>${g.qs.map(q => { const mk = vivaLast(m, pkg, q.q); return `<button class="vp-q" data-vq="${esc(q.q)}"><span class="vp-n mono">${P2.questions.indexOf(q) + 1}</span><span class="vp-t">${esc(q.text)}<small class="mono">${esc(q.q)} · ${q.steps.length} card${q.steps.length === 1 ? '' : 's'}</small></span><span class="vt vt-${esc(q.tier)} mono">${esc(q.tier)}</span><span class="vm vm-${mk || 'none'} mono">${mk ? MARKN[mk] : '–'}</span></button>`; }).join('')}</section>`).join('')}
      <p class="muted small">Package ${esc(P2.version)}.</p>
    </div>
    ${nav('flow')}
  </div>`;
  app.querySelector('[data-vwalk]').onclick = () => walkViva(pkg);
  const vpw = app.querySelector('[data-vplanwalk]'); if (vpw) vpw.onclick = () => walkVivaPlan(pkg);
  const vpa = app.querySelector('[data-vplanadd]'); if (vpa) vpa.onclick = () => { const st = currentStretch(); if (!st) { toast('Make a stretch on the Plan first.'); go('#/plan'); return; } vivaLaneSheet(st, null, () => renderViva(pkg)); };
  if (hasLessons(pkg)) lessonBox(pkg, P2);
  app.querySelector('[data-vmosaic]').onclick = () => { P.set('moViva', pkg); go('#/sys/all'); };
  const wk = app.querySelector('[data-vweak]');
  if (wk) wk.onclick = () => {
    const weak = new Set(P2.questions.filter(q => ['patchy', 'blank'].includes(vivaLast(m, pkg, q.q))).map(q => q.q));
    const list = P2.questions.filter(q => weak.has(q.q)).flatMap(q => vivaQueue(pkg, q.q).list);
    if (list.length) startFlow(list, { viva: pkg, label: 'Viva ' + pkg + ' · patchy + blank', returnTo: '#/viva/' + pkg });
  };
  app.querySelectorAll('[data-vq]').forEach(b => b.onclick = () => walkViva(pkg, b.dataset.vq));
}
function autoChipPage() { const on = vAuto(); return `<button class="chip${on ? ' on' : ''}" data-vautop>${on ? 'Autoplay on' : 'Tap to play'}</button>`; }
// the Viva page's lessons line: how much is made, and Make voice (one question first, then all) — only when Naven presses it
async function lessonBox(pkg, P2) {
  const box = app.querySelector('#vpls'); if (!box) return;
  const ap = box.querySelector('[data-vautop]'); ap.onclick = () => { setVAuto(!vAuto()); ap.classList.toggle('on', vAuto()); ap.textContent = vAuto() ? 'Autoplay on' : 'Tap to play'; };
  const deck = lessonDeck(pkg), s = box.querySelector('.vpls-s'), b1 = box.querySelector('[data-lmake1]'), b = box.querySelector('[data-lmake]');
  const firstQ = P2.questions.find(q => q.open || q.close || q.steps.some(x => x.lesson));
  const draw = async fresh => {
    const all = allLessonParts(pkg); await deckIndex(deck, fresh);
    const miss = all.filter(p => !hasClip(deck, p)), m1 = miss.filter(p => p.k.startsWith('L-' + firstQ.q + '-'));
    const nq = P2.questions.filter(q => q.open || q.close || q.steps.some(x => x.lesson)).length;
    s.textContent = `${nq} question${nq === 1 ? '' : 's'} · about ${lessonMin(all)} min · ${all.length - miss.length} of ${all.length} pieces made`;
    b1.hidden = !m1.length || makingLessons(); b1.textContent = `Make voice · ${firstQ.q} only (${lessonMin(m1)} min)`;
    b.hidden = !miss.length || makingLessons(); b.textContent = `Make voice · all (${lessonMin(miss)} min)`;
  };
  const run = async onlyQ => {
    b.hidden = b1.hidden = true;
    const r = await makeLessons(pkg, st => { if (box.isConnected) s.textContent = `making… ${st.done} of ${st.total}${st.failed ? ` · ${st.failed} failed` : ''}`; }, onlyQ);
    if (r.error) toast('Lesson voice: ' + r.error);
    if (box.isConnected) draw(true);
  };
  // a second tap starts it (Naven, 8 Nov: a stray tap started 2 hours of voice)
  const arm = (btn, go) => { let t = 0; btn.onclick = () => { if (btn.dataset.armed) { clearTimeout(t); delete btn.dataset.armed; go(); return; } btn.dataset.armed = '1'; const was = btn.textContent; btn.textContent = 'Tap again to start · ' + was.replace(/^Make voice · /, ''); btn.classList.add('on'); t = setTimeout(() => { delete btn.dataset.armed; btn.textContent = was; btn.classList.remove('on'); }, 4000); }; };
  arm(b1, () => run(firstQ.q)); arm(b, () => run());
  draw(false);
}
function renderFlowTab() {
  const draw = () => {
    const lf = lastFlowCards(), ag = againCards(), avg = avgPace() || 75000, mins = n => Math.max(1, Math.round(n * avg / 60000));
    const sys = systems();
    app.innerHTML = `<div class="screen flowtab">
      <header class="top"><span class="tt"><span class="mono kick">FLOW</span><span class="h1s">Today’s desk.</span></span><button class="btn ghost" data-pdk>Phone Desk${DESK.deskState() === 'live' ? ' ●' : ''}</button>${goingOutButton()}</header>
      <div class="scroll pad desk">
        ${planDesk()}
        ${targetBlock(!currentStretch())}
        <section class="dk-box">
          <div class="dk-h"><span><span class="mono kick">CONTINUE</span><span class="dk-t">${lf ? esc(lf.label || 'Last flow') : 'No flow left open'}</span></span>
            ${lf ? `<button class="pillbtn" data-cont>${ICON.walkS}Continue</button>` : ''}</div>
          <p class="muted small">${lf ? `${lf.done} of ${lf.total} done · ${lf.cards.length} left · ≈ ${mins(lf.cards.length)} min · stopped ${whenLabel(lf.ts)}` : 'A flow you leave before the end waits here for 3 days.'}</p>
        </section>
        ${vivaPkgs().map(p => `<section class="dk-box">
          <div class="dk-h"><span><span class="mono kick">VIVA ${esc(p.package)}</span><span class="dk-t">${esc(p.title)} · ${p.questions.length} questions</span></span><a class="pillbtn" href="#/viva/${esc(p.package)}">${ICON.walkS}Open</a></div>
        </section>`).join('')}
        <section class="dk-box">
          <div class="dk-h"><span><span class="mono kick">AGAIN PILE</span><span class="dk-t">${ag.length ? ag.length + ' card' + (ag.length === 1 ? '' : 's') + ' to repair' : 'Nothing to repair'}</span></span>
            ${ag.length ? `<button class="pillbtn" data-again>${ICON.walkS}Repair</button>` : ''}</div>
          ${ag.length ? `<div class="pl-strip">${ag.slice(0, 120).map(c => `<i class="s${shade(seen(c.deck, c.no))}${isNeet(c) ? ' ng' : ''}" data-tip="${esc(tipOf(c) + ' · ' + c._why)}"></i>`).join('')}</div>` : ''}
          ${ag.length ? `<div class="ag-why">${ag.slice(0, 6).map(c => `<span class="mono small"><b>${esc(c.deck)}</b> ${esc(chunkOf(c).name)} · ${esc(c._why)}</span>`).join('')}${ag.length > 6 ? `<span class="muted small">+ ${ag.length - 6} more</span>` : ''}</div>` : ''}
          <p class="muted small">Cards you mark Again, and cards behind DocT questions you got wrong or guessed (from the day after the test). A card leaves the pile once you walk it without Again.${repairsDueLater().length ? ` <b>${repairsDueLater().length}</b> more join${repairsDueLater().length === 1 ? 's' : ''} tomorrow.` : ''}${unmappedMisses().length ? ` ${unmappedMisses().length} missed question${unmappedMisses().length === 1 ? ' has' : 's have'} no card yet.` : ''}</p>
        </section>
        <section class="dk-box">
          <div class="dk-h"><span><span class="mono kick">ADD MORE</span><span class="dk-t">Pick cards, then + Add to flow</span></span></div>
          <div class="chips">
            <a class="chip" href="#/sys/all">▦ Eagle view · every deck</a>
            ${sys.map(g => `<a class="chip dash" href="#/sys/${sysNum(g.name)}" data-mosaic>${esc(g.label)}</a>`).join('')}
          </div>
          <p class="muted small">A system opens in its Mosaic. Tap a deck’s code there to open the deck and pick sections.</p>
        </section>
      </div>
      ${nav('flow')}
    </div>`;
    bindGo(); bindTarget(draw); hideTip(); bindTips(app); bindGoingOut();
    app.querySelectorAll('[data-mosaic]').forEach(a => a.addEventListener('click', () => P.set('sysTab', 'mosaic')));
    const c = app.querySelector('[data-cont]');
    const pdk = app.querySelector('[data-pdk]'); if (pdk) pdk.onclick = () => deskChooser();
    if (c) c.onclick = () => startFlow(lf.cards, { label: lf.label || 'Continue', returnTo: lf.viva ? '#/viva/' + lf.viva : '#/flow', viva: lf.viva || '' });
    const r = app.querySelector('[data-again]');
    if (r) r.onclick = () => startFlow(ag, { label: 'Again pile', returnTo: '#/flow' });
    const pt = app.querySelector('[data-plantoday]');
    if (pt) pt.onclick = () => { const st = currentStretch(), q = st ? todayCards(st) : []; if (q.length) startFlow(q, { label: 'The Plan · today', returnTo: '#/flow' }); else toast('Today’s plan is done.'); };
  };
  draw();
}
// Flow desk: today's slice of the plan, with the thread as it stands
function planDesk() {
  const st = currentStretch();
  if (!st) return `<section class="dk-box"><div class="dk-h"><span><span class="mono kick">THE PLAN</span><span class="dk-t">No plan yet</span></span><a class="pillbtn" href="#/plan">Plan</a></div><p class="muted small">Make a stretch in the Loft’s planner and today’s cards will wait here every morning.</p></section>`;
  const r = compute(st), parts = todayParts(st, r), left = todayCards(st, r).length, done = todayBeads().length;
  if (!r.active) return `<section class="dk-box"><div class="dk-h"><span><span class="mono kick">THE PLAN · ${esc(st.name.toUpperCase())}</span><span class="dk-t">${r.td < r.days[0] ? 'Starts ' + dShort(r.days[0]) : 'Stretch finished'}</span></span><a class="pillbtn" href="#/plan">Open</a></div></section>`;
  return `<section class="dk-box plandesk">
    <div class="dk-h"><span><span class="mono kick">TODAY FROM THE PLAN · ${esc(st.name.toUpperCase())}</span><span class="dk-t">${done} of ${r.todayPlan} walked today${left ? ` · ${left} waiting` : ' · plan done'}</span></span>
      ${left ? `<button class="pillbtn" data-plantoday>${ICON.walkS}Start</button>` : ''}</div>
    <div class="pd-parts">${parts.map(x => `<span><i>${esc(x.name)}</i><b>${x.done}/${x.n}</b></span>`).join('')}</div>
    <p class="muted small">Repairs first, then the subjects in plan order. <a href="#/plan">Open the planner</a></p>
  </section>`;
}
function keep(fn) { const sc = app.querySelector('.scroll'), y = sc ? sc.scrollTop : 0; fn(); const s2 = app.querySelector('.scroll'); if (s2) s2.scrollTop = y; }

/* ============================ the Loft ============================ */
const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
let loftMonth = null, loftDay = null;
// Coverage: walked ÷ cards in a pool; each pool is its own denominator. Walked = seen at least once (War Map history + Trace).
const COVER = [['all', 'All cards'], ['hit', 'Any hit'], ['neet', 'NEET'], ['neet+gt', 'NEET + GT']];
function coverage(pool) {
  const sys = new Map(); let t = 0, w = 0, w2 = 0, missing = 0;
  for (const d of (S.library ? S.library.decks : [])) {
    const cs = cardsOf(d.deck);
    let n, a, b;
    let x3 = 0;
    if (cs.length) { const l = cs.filter(c => inPool(c, pool)); n = l.length; a = l.filter(c => seen(c.deck, c.no) > 0).length; b = l.filter(c => seen(c.deck, c.no) > 1).length; x3 = l.filter(c => seen(c.deck, c.no) > 2).length; }
    else if (pool === 'all') { n = d.cards; a = walked(d.deck); b = 0; }
    else { missing++; continue; }
    t += n; w += a; w2 += b;
    const g = sys.get(d.system) || { name: d.system, n: 0, a: 0, b: 0, c: 0 }; g.n += n; g.a += a; g.b += b; g.c += x3; sys.set(d.system, g);
  }
  return { t, w, w2, missing, sys: [...sys.values()].filter(g => g.n).sort((x, y) => x.name.localeCompare(y.name, undefined, { numeric: true })) };
}
const pct = (a, n) => n ? Math.round(100 * a / n) : 0;
function coverCard() {
  const cp = P.get('covPool', 'neet'), all = COVER.map(([k, l]) => ({ k, l, c: coverage(k) })), sel = all.find(x => x.k === cp) || all[2];
  return `<div class="cover">
    <span class="mono kick">COVERAGE · WALKED AT LEAST ONCE</span>
    <div class="cv-tiles">${all.map(x => `<button class="cv-t${x.k === sel.k ? ' on' : ''}" data-cov="${x.k}"><b>${pct(x.c.w, x.c.t)}%</b><span>${x.l}</span><i class="mono">${x.c.w.toLocaleString()} / ${x.c.t.toLocaleString()}</i></button>`).join('')}</div>
    <div class="cv-sys">${sel.c.sys.map(g => `<div class="cv-r"><span class="cv-n">${esc(sysLabel(g.name))}</span><span class="cv-bar" title="${g.a} of ${g.n} walked · ${g.b} twice or more · ${g.c} three times or more"><i class="s3" style="width:${pct(g.c, g.n)}%"></i><i class="s2" style="width:${pct(g.b - g.c, g.n)}%"></i><i class="s1" style="width:${pct(g.a - g.b, g.n)}%"></i></span><span class="mono cv-p">${pct(g.a, g.n)}%</span></div>`).join('')}</div>
    ${SEEN_LEGEND}
    <p class="muted small">${sel.l}: ${sel.c.w.toLocaleString()} of ${sel.c.t.toLocaleString()} cards walked, ${sel.c.w2.toLocaleString()} twice or more.${sel.c.missing ? ` ${sel.c.missing} deck${sel.c.missing === 1 ? ' is' : 's are'} not on this device yet and ${sel.c.missing === 1 ? 'is' : 'are'} left out.` : ''}</p>
  </div>`;
}
/* ============================ Loft sections (T-045) ============================ */
const SEEN_LEGEND = `<div class="lg-row mono"><span><i class="sq s0"></i>not seen</span><span><i class="sq s1"></i>once</span><span><i class="sq s2"></i>twice</span><span><i class="sq s3"></i>3+ times</span></div>`;
const CHASE_POOLS = [['all', 'All cards'], ['hit', 'Any hit'], ['neet+gt', 'NEET + GT'], ['neet', 'NEET']];
const shortDay = d => { const x = new Date(d + 'T12:00'); return x.getDate() + ' ' + MONTHS[x.getMonth()].slice(0, 3); };
function chaseCard() {
  const pool = P.get('chasePool', 'all'), c = chase(pool), lp = livePace(c), slide = P.get('whatIf', 0);
  const W = 600, H = 150, x0 = 8, x1 = W - 8, y0 = 128, y1 = 16;
  const X = i => x0 + (x1 - x0) * i / (c.nDays - 1), Y = v => y0 - (y0 - y1) * Math.min(1, v / Math.max(1, c.total));
  const ti = c.series.length - 1;
  const actual = c.series.map((p, i) => `${X(i).toFixed(1)},${Y(p.walked).toFixed(1)}`).join(' ');
  const need = ti >= 0 ? `${X(ti).toFixed(1)},${Y(c.walkedNow).toFixed(1)} ${X(c.nDays - 1).toFixed(1)},${Y(c.total).toFixed(1)}` : '';
  const rate = slide || c.rate, projDays = rate > 0 ? Math.ceil(c.left / rate) : null;
  const projEndI = projDays == null ? null : Math.min(c.nDays - 1, ti + projDays);
  const proj = ti >= 0 && projEndI != null ? `${X(ti).toFixed(1)},${Y(c.walkedNow).toFixed(1)} ${X(projEndI).toFixed(1)},${Y(c.walkedNow + rate * (projEndI - ti)).toFixed(1)}` : '';
  const finish = rate > 0 ? addDays(today(), projDays) : null, late = finish ? daysBetween(PHASE1_END, finish) : null;
  const verdict = c.left === 0 ? 'Phase 1 done for this pool.' : !finish ? 'No pace yet: walk some new cards to see where you land.'
    : late > 0 ? `At ${rate}/day you finish <b class="behind">${shortDay(finish)}: ${late} day${late === 1 ? '' : 's'} late</b>.`
    : `At ${rate}/day you finish <b class="ahead">${shortDay(finish)}: ${-late === 0 ? 'on the day' : -late + ' day' + (late === -1 ? '' : 's') + ' early'}</b>.`;
  const wmax = Math.max(1, ...c.weeks.map(w => Math.max(w.done, w.need)));
  const ringP = c.requiredToday ? Math.min(1, c.doneToday / c.requiredToday) : 1, circ = 2 * Math.PI * 26;
  const pace = lp.before ? `Your window opens at ${WIN_START}.` : lp.after ? 'The day window has closed.'
    : `${lp.diff >= 0 ? `<b class="ahead">▲ ${lp.diff} ahead</b>` : `<b class="behind">▼ ${-lp.diff} behind</b>`} · should be ${lp.should} by now · ${lp.perHour != null ? lp.perHour + ' an hour needed' : ''}`;
  return `<div class="lcard chase">
    <div class="lc-h"><span class="mono kick">PHASE 1 CHASE · EVERY CARD ONCE BY 30 NOV</span></div>
    <div class="chips small">${CHASE_POOLS.map(([k, l]) => `<button class="chip${pool === k ? ' on' : ''}" data-cpool="${k}">${l}</button>`).join('')}</div>
    <div class="cs-board">
      <div class="cs-ring"><svg viewBox="0 0 64 64" width="72" height="72" aria-hidden="true"><circle cx="32" cy="32" r="26" class="r0"/><circle cx="32" cy="32" r="26" class="r1${ringP >= 1 ? ' full' : ''}" stroke-dasharray="${(circ * ringP).toFixed(1)} ${circ.toFixed(1)}" transform="rotate(-90 32 32)"/></svg><span><b>${c.doneToday}</b><i>of ${c.requiredToday} today</i></span></div>
      <div class="cs-nums"><span><b>${c.walkedNow.toLocaleString()}</b> / ${c.total.toLocaleString()} walked · <b>${c.left.toLocaleString()}</b> to go · ${c.daysLeft} day${c.daysLeft === 1 ? '' : 's'} left</span>
        <span class="cs-rr"><span>Current <b>${c.rate}</b>/day ${c.rate >= c.required ? '▲' : '▼'}</span><span>Required <b>${c.required}</b>/day</span></span>
        <span class="cs-v">${verdict}</span><span class="cs-live">${pace}</span></div>
    </div>
    <svg viewBox="0 0 ${W} ${H}" width="100%" class="worm" role="img" aria-label="Cards walked against the path to 30 November">
      <line x1="${x0}" y1="${y1}" x2="${x1}" y2="${y1}" class="gl"/><line x1="${x0}" y1="${y0}" x2="${x1}" y2="${y0}" class="gl"/>
      <text x="${x0}" y="${y1 - 4}" class="tx">${c.total.toLocaleString()}</text><text x="${x0}" y="${H - 4}" class="tx">1 Nov</text><text x="${x1}" y="${H - 4}" class="tx" text-anchor="end">30 Nov</text>
      ${need ? `<polyline points="${need}" class="need"/>` : ''}${proj ? `<polyline points="${proj}" class="proj"/>` : ''}
      ${actual ? `<polyline points="${actual}" class="act"/>` : ''}${ti >= 0 ? `<circle cx="${X(ti).toFixed(1)}" cy="${Y(c.walkedNow).toFixed(1)}" r="3.5" class="dot"/>` : ''}
    </svg>
    <div class="lg-row mono"><span><i class="ln act"></i>walked</span><span><i class="ln need"></i>needed</span><span><i class="ln proj"></i>${slide ? 'what-if' : 'your 7-day pace'}</span></div>
    <div class="wk">${c.weeks.map(w => `<div class="wk-c${w.future ? ' fut' : ''}" title="${w.a} – ${w.b}: ${w.done} walked, ${w.need} needed"><span class="wk-b"><i style="height:${Math.round(w.done / wmax * 100)}%"></i><em style="bottom:${Math.round(w.need / wmax * 100)}%"></em></span><span class="mono">${shortDay(w.a)}</span></div>`).join('')}</div>
    <label class="whatif mono">What if I walk <input type="range" min="0" max="200" step="5" value="${slide}" data-whatif> <b>${slide || 'my pace'}</b>${slide ? ' a day' : ''}</label>
  </div>`;
}
const CPD = [['all', 'All'], ['new', 'New'], ['x2', '×2'], ['x3', '×3+'], ['repair', 'Repairs']];
const CPD_COL = { new: 'var(--s1)', x2: 'var(--s2)', x3: 'var(--s3)', repair: '#c9a6d6', wm: '#6b6f78' };
function cardsDayCard() {
  const f = P.get('cpdFilter', 'all'), n = P.get('cpdRange', 14), rows = cardsPerDay(n);
  const keys = f === 'all' ? ['new', 'x2', 'x3', 'repair', 'wm'] : [f];
  const goal = 65, mx = Math.max(goal + 10, ...rows.map(r => keys.reduce((t, k) => t + r[k], 0)));
  const W = 600, H = 130, w = W / n, td = today();
  const bars = rows.map((r, i) => {
    let y = H - 14, s = '';
    for (const k of keys) { const h = r[k] / mx * (H - 26); if (h > 0) { y -= h; s += `<rect x="${(i * w + w * 0.15).toFixed(1)}" y="${y.toFixed(1)}" width="${(w * 0.7).toFixed(1)}" height="${h.toFixed(1)}" rx="1.5" fill="${CPD_COL[k]}"/>`; } }
    const lab = n <= 14 || i % 5 === 0 || r.day === td ? `<text x="${(i * w + w / 2).toFixed(1)}" y="${H - 2}" text-anchor="middle" class="tx${r.day === td ? ' now' : ''}">${n <= 14 ? 'SMTWTFS'[new Date(r.day + 'T12:00').getDay()] : new Date(r.day + 'T12:00').getDate()}</text>` : '';
    return `<g data-day="${r.day}" class="cpd-b">${s}<rect x="${(i * w).toFixed(1)}" y="0" width="${w.toFixed(1)}" height="${H}" fill="transparent"/>${lab}</g>`;
  }).join('');
  const gy = (H - 14 - goal / mx * (H - 26)).toFixed(1);
  const tot = rows.reduce((t, r) => t + keys.reduce((a, k) => a + r[k], 0), 0), met = rows.filter(r => r.new + r.x2 + r.x3 + r.repair + r.wm >= goal).length;
  return `<div class="lcard">
    <div class="lc-h"><span class="mono kick">CARDS PER DAY</span><span class="seg">${[7, 14, 30].map(k => `<button class="${n === k ? 'on' : ''}" data-cpdr="${k}">${k}</button>`).join('')}</span></div>
    <div class="chips small">${CPD.map(([k, l]) => `<button class="chip${f === k ? ' on' : ''}" data-cpdf="${k}">${l}</button>`).join('')}</div>
    <svg viewBox="0 0 ${W} ${H}" width="100%" class="cpd" role="img" aria-label="Cards per day">${f === 'all' ? `<line x1="0" y1="${gy}" x2="${W}" y2="${gy}" class="goal"/><text x="${W - 2}" y="${(+gy - 3).toFixed(1)}" text-anchor="end" class="tx gold">goal ${goal}</text>` : ''}${bars}</svg>
    <div class="lg-row mono"><span><i class="sq s1"></i>new</span><span><i class="sq s2"></i>×2</span><span><i class="sq s3"></i>×3+</span><span><i class="sq" style="background:#c9a6d6"></i>repair</span><span><i class="sq" style="background:#6b6f78"></i>War Map flow</span><span class="lg-r">tap a bar → that day</span></div>
    <p class="muted small">${CPD.find(x => x[0] === f)[1]}: ${Math.round(tot / n)} a day on average over ${n} days${f === 'all' ? ` · goal met ${met} of ${n} days` : ''}.</p>
  </div>`;
}
const fmtMin = ms => fmtHM(ms / 60000);
function dayBreakdown(day) {
  const study = studyMs(day), list = breaksOn(day), byR = {};
  for (const b of list) byR[b.reason] = (byR[b.reason] || 0) + Math.max(0, (b.end || Date.now()) - b.start);
  const cur = curBreak(); if (cur && dkey(cur.start) === day) byR[cur.reason] = (byR[cur.reason] || 0) + (Date.now() - cur.start);
  const a = winStart(day), b = Math.min(winEnd(day), Date.now()), elapsed = Math.max(0, b - a);
  const brk = Object.values(byR).reduce((t, v) => t + v, 0), unexpl = Math.max(0, elapsed - study - brk);
  const rows = [['Study', study]].concat(Object.entries(byR).map(([k, v]) => [reasonOf(k)[1], v, k])).concat(unexpl > 60000 ? [['Unexplained', unexpl]] : []);
  return { rows: rows.sort((x, y) => y[1] - x[1]), study, elapsed, byR };
}
function allowanceNote(byR) {
  const meals = MEALS.reduce((t, k) => t + (byR[k] || 0), 0), teas = TEAS.reduce((t, k) => t + (byR[k] || 0), 0);
  const mealsAllowed = MEALS.filter(k => byR[k]).length * 30 * 60000, teaAllowed = (byR.eveningtea ? 30 : 0) * 60000 + (byR.tea ? Math.ceil(byR.tea / (15 * 60000)) * 15 * 60000 : 0);
  const over = (v, al) => v > al ? ` <b class="behind">(+${fmtMin(v - al)})</b>` : '';
  return `Meals ${fmtMin(meals)}${over(meals, mealsAllowed)} · tea ${fmtMin(teas)}${over(teas, teaAllowed)}`;
}
function dayList(day) {
  const items = studyIntervals(day).map(([s, e]) => ({ s, e, what: 'Study' }))
    .concat(breaksOn(day).map(b => ({ s: b.start, e: b.end || Date.now(), what: reasonOf(b.reason)[1] + (b.allowed && b.end - b.start > b.allowed * 60000 ? ` (+${fmtMin(b.end - b.start - b.allowed * 60000)})` : '') })))
    .sort((x, y) => x.s - y.s);
  const hm = t => new Date(t).toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
  return items.length ? `<div class="daylist">${items.map(i => `<div><span class="mono">${hm(i.s)}–${hm(i.e)}</span><span>${esc(i.what)}</span><span class="mono">${fmtMin(i.e - i.s)}</span></div>`).join('')}</div>` : '<p class="muted small">Nothing recorded on this day.</p>';
}
function timeCard() {
  const td = today(), selDay = P.get('timeDay', td), span = P.get('bdSpan', 'day'), hr = P.get('hoursRange', 14);
  const tb = dayBreakdown(td), cardsToday = cardsPerDay(1)[0], studyH = tb.study / 3600e3;
  const perH = studyH > 0.05 ? Math.round((cardsToday.new + cardsToday.x2 + cardsToday.x3 + cardsToday.repair) / studyH * 10) / 10 : 0;
  const days7 = []; for (let i = 6; i >= 0; i--) days7.push(addDays(td, -i));
  const strip = d => { const a = winStart(d), L = winEnd(d) - a; return studyIntervals(d).map(([s, e]) => { const x = Math.max(0, (s - a) / L), y = Math.min(1, (e - a) / L); return y > x ? `<i style="left:${(x * 100).toFixed(2)}%;width:${((y - x) * 100).toFixed(2)}%"></i>` : ''; }).join(''); };
  // breakdown for the day or the last 7 days
  let bd;
  if (span === 'week') { const acc = {}; for (const d of days7) for (const [l, v] of dayBreakdown(d).rows) acc[l] = (acc[l] || 0) + v; bd = Object.entries(acc).sort((x, y) => y[1] - x[1]); }
  else bd = dayBreakdown(selDay).rows.map(r => [r[0], r[1]]);
  const bmax = Math.max(1, ...bd.map(r => r[1]));
  const hdays = []; for (let i = hr - 1; i >= 0; i--) hdays.push(addDays(td, -i));
  const hv = hdays.map(d => studyMs(d) / 3600e3), hmx = Math.max(STUDY_GOAL_H + 1, ...hv), W = 600, H = 110, w = W / hr;
  const hbars = hv.map((v, i) => `<rect x="${(i * w + w * 0.15).toFixed(1)}" y="${(H - 12 - v / hmx * (H - 22)).toFixed(1)}" width="${(w * 0.7).toFixed(1)}" height="${(v / hmx * (H - 22)).toFixed(1)}" rx="1.5" fill="var(--s2)"><title>${hdays[i]}: ${v.toFixed(1)} h</title></rect>${hr <= 14 ? `<text x="${(i * w + w / 2).toFixed(1)}" y="${H - 1}" text-anchor="middle" class="tx">${'SMTWTFS'[new Date(hdays[i] + 'T12:00').getDay()]}</text>` : ''}`).join('');
  const gy = (H - 12 - STUDY_GOAL_H / hmx * (H - 22)).toFixed(1);
  const bh = bestHours(), bmx = Math.max(1, ...bh);
  const shade4 = v => v <= 0 ? 0 : v >= bmx * 0.85 ? 3 : v >= bmx * 0.55 ? 2 : 1;
  return `<div class="lcard time">
    <div class="lc-h"><span class="mono kick">TIME · ${WIN_START}–${WIN_END} WINDOW</span></div>
    <div class="tm-hn"><span><b>${fmtMin(tb.study)}</b><i>study${tb.elapsed ? ' · ' + Math.round(tb.study / tb.elapsed * 100) + '% so far' : ''}</i></span><span><b>${perH || '–'}</b><i>cards per study hour</i></span><span><b class="sm">${allowanceNote(tb.byR)}</b><i>breaks vs allowance</i></span></div>
    <span class="mono lab">WHEN YOU STUDIED · LAST 7 DAYS</span>
    <div class="strips">${days7.map(d => `<button class="strip-r${d === selDay ? ' on' : ''}" data-tday="${d}"><span class="mono">${'SMTWTFS'[new Date(d + 'T12:00').getDay()]} ${new Date(d + 'T12:00').getDate()}</span><span class="strip">${strip(d)}</span><span class="mono">${fmtMin(studyMs(d))}</span></button>`).join('')}
      <div class="strip-ax mono"><span></span><span><i>9:30</i><i>12</i><i>3 pm</i><i>6 pm</i><i>9:30</i></span><span></span></div></div>
    <div class="lc-h"><span class="mono lab">WHERE DID MY ${span === 'week' ? 'WEEK' : '12 HOURS'} GO? · ${span === 'week' ? 'LAST 7 DAYS' : shortDay(selDay).toUpperCase()}</span><span class="seg"><button class="${span === 'day' ? 'on' : ''}" data-bdspan="day">Day</button><button class="${span === 'week' ? 'on' : ''}" data-bdspan="week">Week</button></span></div>
    <div class="bd">${bd.map(([l, v]) => `<div class="bd-r${l === 'Unexplained' ? ' unx' : ''}"><span>${esc(l)}</span><span class="bd-bar"><i style="width:${(v / bmax * 100).toFixed(1)}%"></i></span><span class="mono">${fmtMin(v)}</span></div>`).join('') || '<p class="muted small">Nothing yet.</p>'}</div>
    ${span === 'day' ? `<details class="dl"${P.get('dlOpen', false) ? ' open' : ''}><summary class="mono muted small">The day, in order</summary>${dayList(selDay)}</details>` : ''}
    <div class="lc-h"><span class="mono lab">STUDY HOURS PER DAY</span><span class="seg">${[7, 14, 30].map(k => `<button class="${hr === k ? 'on' : ''}" data-hr="${k}">${k}</button>`).join('')}</span></div>
    <svg viewBox="0 0 ${W} ${H}" width="100%" class="cpd" role="img" aria-label="Study hours per day"><line x1="0" y1="${gy}" x2="${W}" y2="${gy}" class="goal"/><text x="${W - 2}" y="${(+gy - 3).toFixed(1)}" text-anchor="end" class="tx gold">goal ${STUDY_GOAL_H} h</text>${hbars}</svg>
    <span class="mono lab">YOUR BEST HOURS · CARDS PER HOUR, 14-DAY AVERAGE</span>
    <div class="heat">${bh.map((v, i) => `<span class="sq-h s${shade4(v)}" title="${i + 9}:30–${i + 10}:30">${v ? Math.round(v) : ''}</span>`).join('')}</div>
    <div class="strip-ax mono heat-ax"><span><i>9:30</i><i>12</i><i>3 pm</i><i>6 pm</i><i>9:30</i></span></div>
    <p class="muted small">Breaks and their reasons are recorded from Going out and the "where were you?" question; until then gaps count as unexplained.</p>
  </div>`;
}
function tilesRow(chronN) {
  const ag = againList().length, gts = gtTrend(), last = gts[gts.length - 1];
  return `<div class="ltiles">
    <a class="lt" href="#/meditation"><span class="mono kick teal">QUIET ALCOVE</span><b id="al-last">Guidance</b><i>morning · afternoon · night</i></a>
    <button class="lt" data-chron><span class="mono kick">CHRONICLES</span><b>${chronN} entries</b><i>${P.get('chronOpen', false) ? 'hide the list' : 'open the list'}</i></button>
    <a class="lt" href="#/flow"><span class="mono kick">AGAIN PILE</span><b>${ag} to repair</b><i>to the Flow desk</i></a>
    <button class="lt" data-gt><span class="mono kick">GT TREND</span><b>${last ? last.pct + '% · ' + esc(last.gt) : 'No GT yet'}</b><i>${gts.length ? gts.length + ' paper' + (gts.length === 1 ? '' : 's') : 'from the War Map'}</i></button>
  </div>
  ${P.get('gtOpen', false) && gts.length ? `<div class="lcard"><span class="mono kick">GT TREND · NET % (+4 / −1)</span><div class="gtt">${gts.map(g => `<span title="${esc(g.gt)} · ${g.date}: ${g.right} right, ${g.wrong} wrong of ${g.total}"><i style="height:${Math.max(4, g.pct)}%"></i><b class="mono">${g.pct}%</b><em class="mono">${esc(String(g.gt).replace(/NEET-?/i, ''))}</em></span>`).join('')}</div></div>` : ''}`;
}
function bindLoftParts() {
  const r = () => keep(renderLoft);
  app.querySelectorAll('[data-cpool]').forEach(b => b.onclick = () => { P.set('chasePool', b.dataset.cpool); r(); });
  const wi = app.querySelector('[data-whatif]'); if (wi) wi.onchange = () => { P.set('whatIf', +wi.value); r(); };
  app.querySelectorAll('[data-cpdf]').forEach(b => b.onclick = () => { P.set('cpdFilter', b.dataset.cpdf); r(); });
  app.querySelectorAll('[data-cpdr]').forEach(b => b.onclick = () => { P.set('cpdRange', +b.dataset.cpdr); r(); });
  app.querySelectorAll('.cpd-b').forEach(g => g.addEventListener('click', () => { loftDay = g.dataset.day; P.set('timeDay', g.dataset.day); r(); }));
  app.querySelectorAll('[data-tday]').forEach(b => b.onclick = () => { P.set('timeDay', b.dataset.tday); P.set('bdSpan', 'day'); loftDay = b.dataset.tday; r(); });
  app.querySelectorAll('[data-bdspan]').forEach(b => b.onclick = () => { P.set('bdSpan', b.dataset.bdspan); r(); });
  app.querySelectorAll('[data-hr]').forEach(b => b.onclick = () => { P.set('hoursRange', +b.dataset.hr); r(); });
  const dl = app.querySelector('details.dl'); if (dl) dl.addEventListener('toggle', () => P.set('dlOpen', dl.open));
  const ch = app.querySelector('[data-chron]'); if (ch) ch.onclick = () => { P.set('chronOpen', !P.get('chronOpen', false)); r(); };
  const gt = app.querySelector('[data-gt]'); if (gt) gt.onclick = () => { P.set('gtOpen', !P.get('gtOpen', false)); r(); };
}

/* ============================ The Plan (T-053): stretches → subjects → today's slice ============================ */
const WALKS = [['w0', 'Not walked'], ['w1', '×1'], ['w2', '×2'], ['w3', '×3+']];
const walkParts = v => String(v || '').split('+').filter(x => /^w[0-3]$/.test(x));
function walkOk(c, v) { const p = walkParts(v); if (!p.length) return true; const n = Math.min(3, seen(c.deck, c.no)); return p.includes('w' + n); }
const walkName = v => walkParts(v).map(k => WALKS.find(w => w[0] === k)[1]).join(' + ');
function toggleWalk(cur, k) { const s = new Set(walkParts(cur)); s.has(k) ? s.delete(k) : s.add(k); return WALKS.map(w => w[0]).filter(x => s.has(x)).join('+'); }
const WD = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
const dHead = d => { const x = new Date(d + 'T12:00'); return [WD[x.getDay()], x.getDate()]; };
const dShort = d => { const [w, n] = dHead(d); return `${w} ${n} ${MONTHS[new Date(d + 'T12:00').getMonth()].slice(0, 3)}`; };
function paceBand(p) { return p <= 55 ? ['comfortable', 'ok'] : p <= 70 ? ['a stretch', 'mid'] : ['more than your best week (55)', 'hi']; }
let planPending = null;
const startSelect = (st, cur, attr) => `<label>Starts on <select ${attr}>${planDays(st).map((d, i) => `<option value="${i ? d : ''}"${(cur || '') === (i ? d : '') ? ' selected' : ''}>${i ? dShort(d) + ' (day ' + (i + 1) + ')' : 'the first day'}</option>`).join('')}</select></label>`;            // cards picked in the Mosaic, waiting to become a subject

function renderPlan() {
  const p = loadPlan(), st = currentStretch();
  if (!st) return renderPlanNew();
  const r = compute(st), days = r.days, td = r.td, band = paceBand(st.pace);
  const R = repairOpts(st);
  const repRow = { id: 'repair', name: 'Repair pile', sub: R.on ? `${r.repairTotal} waiting · ${R.spread === 'fixed' ? R.fixed + ' a day' : R.spread === 'by' && R.by ? 'done by ' + dShort(R.by) + ', up to ' + R.cap + ' a day' : 'up to ' + R.cap + ' a day'}` : 'off', auto: true };
  const subRows = st.subjects.map(s => ({ ...s, sub: `${s.sub ? s.sub + ' · ' : ''}${s.keys.length} cards · ${splitName(s)}${s.from && !s.once ? ' · from ' + dShort(s.from) : ''}` }));
  const rows = rowOrder(st).map(id => id === 'repair' ? repRow : subRows.find(x => x.id === id));
  const vr = Object.values(computeViva(st));                       // T-138: viva lanes, counted in questions
  const anyOver = r.over > 0 || vr.some(x => x.over > 0);
  const vcell = (x, d) => {
    const plan = x.cells[d] || 0, did = x.actual[d] || 0;
    if (d < td) return `<td class="pc past vq${did ? ' on' : ''}">${did || ''}</td>`;
    if (d === td) return `<td class="pc today vq${plan || did ? ' on' : ''}">${plan || did ? `<b>${did}</b><i>/${plan}</i>` : ''}</td>`;
    return `<td class="pc vq${plan ? ' on' : ''}">${plan || ''}</td>`;
  };
  const vrow = x => { const l = x.lane, P2 = vivaPkg(l.pkg); return `<tr class="vrow"><td class="nm tap" data-vlane="${l.id}"><b>Viva ${esc(l.pkg)}${P2 ? ' · ' + esc(P2.title) : ''}</b><i>${l.qs.length} questions (Q${qNumOf(l.pkg, l.qs[0])}–Q${qNumOf(l.pkg, l.qs[l.qs.length - 1])}) · ${l.perDay ? l.perDay + ' a day' : 'spread over the days'}${l.from ? ' · from ' + dShort(l.from) : ''} · ${x.left} left</i></td>${days.map(d => vcell(x, d)).join('')}${anyOver ? `<td class="pc ov${x.over ? ' on' : ''}">${x.over || ''}</td>` : ''}</tr>`; };
  const cell = (row, d) => {
    const plan = r.cells[row.id][d] || 0, did = r.actual[row.id][d] || 0, pin = st.pins[row.id + '|' + d] != null;
    if (d < td) return `<td class="pc past${did ? ' on' : ''}">${did || ''}</td>`;
    if (d === td) return `<td class="pc today${plan || did ? ' on' : ''}${!row.auto ? ' tap' : ''}" data-cell="${row.id}|${d}">${plan || did ? `<b>${did}</b><i>/${plan}</i>` : ''}${pin ? '<span class="pin" aria-label="fixed">•</span>' : ''}</td>`;
    return `<td class="pc${plan ? ' on' : ''}${!row.auto ? ' tap' : ''}" data-cell="${row.id}|${d}">${plan || ''}${pin ? '<span class="pin" aria-label="fixed">•</span>' : ''}</td>`;
  };
  const verdict = r.over > 0
    ? `<span class="behind">${r.cards} cards, room for ${r.room}. ${r.over} don’t fit.</span> Three ways out: pace ${r.needPace} a day, add ${Math.ceil(r.over / st.pace * 10) / 10} days, or narrow a subject.`
    : r.raised ? `<span class="mid">Fits by raising normal days to ${r.effPace} a day</span> (your pace ${st.pace}, ceiling ${st.ceiling}).`
    : `<span class="ahead">${r.cards} cards, room for ${r.room}. It fits, ${r.spare} spare.</span>`;
  app.innerHTML = `<div class="screen plan">
    <header class="top"><a class="iconbtn" href="#/loft" aria-label="Back to the Loft">${ICON.back}</a>
      <span class="tt"><span class="mono kick">${esc(st.name.toUpperCase())} · ${dShort(days[0]).toUpperCase()} – ${dShort(days[days.length - 1]).toUpperCase()} · ${st.days} DAYS</span><span class="h1s">The Plan</span></span><a class="btn ghost" href="#/day">Day plan</a><button class="btn ghost pundo-top" data-pundo ${canUndoPlan() ? '' : 'disabled'} aria-label="Undo last change to the plan" title="Undo last change">↶ Undo</button>${goingOutButton()}</header>
    <div class="scroll pad planbody">
      ${p.stretches.length > 1 ? `<div class="chips small">${p.stretches.map(s => `<button class="chip${s.id === st.id ? ' on' : ''}" data-stretch="${s.id}">${esc(s.name)}</button>`).join('')}<button class="chip dash" data-newstretch>+ New stretch</button></div>` : ''}
      <ol class="steps">
        <li><b>Days.</b> <span class="stp">Starts <input type="date" value="${st.start}" data-pstart> · <button class="iconbtn sm" data-pdays="-1" aria-label="One day fewer">−</button> <b>${st.days}</b> days <button class="iconbtn sm" data-pdays="1" aria-label="One day more">+</button></span></li>
        <li><b>Pace.</b> <span class="stp"><input type="range" min="30" max="110" step="1" value="${st.pace}" data-ppace> <b data-ppace-out>${st.pace} a day</b> <span class="band ${band[1]}">· ${band[0]}</span></span>
          <span class="stp muted small">Ceiling when catching up: <button class="iconbtn sm" data-pceil="-5" aria-label="Lower ceiling">−</button> ${st.ceiling} <button class="iconbtn sm" data-pceil="5" aria-label="Raise ceiling">+</button> · your best week 55 a day, best day 89</span></li>
        <li><b>Subjects.</b> Trace counts the cards and writes how many go on each day. Tap a day to make it a GT, half or off day; tap a number to fix it; tap a subject to change it.</li>
      </ol>
      <div class="pgrid-wrap"><table class="pgrid">
        <thead><tr><th class="nm"></th>${days.map(d => { const [w, n] = dHead(d), t = dayType(st, d); return `<th class="dh${d === td ? ' today' : ''}${d < td ? ' past' : ''}" data-dtype="${d}"><span>${w}</span><b>${n}</b>${t !== 'normal' ? `<em>${t === 'gt' ? 'GT' : t === 'half' ? 'half' : 'off'}</em>` : ''}</th>`; }).join('')}${anyOver ? '<th class="dh ovh"><span>Doesn’t</span><b>fit</b></th>' : ''}</tr></thead>
        <tbody>${rows.map(row => `<tr><td class="nm${row.auto ? '' : ' tap'}" data-subj="${row.id}"><b>${esc(row.name)}</b><i>${esc(row.sub)}</i></td>${days.map(d => cell(row, d)).join('')}${anyOver ? `<td class="pc ov${r.overflow[row.id] ? ' on' : ''}">${r.overflow[row.id] || ''}</td>` : ''}</tr>`).join('')}
          ${vr.map(vrow).join('')}
          <tr class="tot"><td class="nm"><i>Day total (cards)</i></td>${days.map(d => `<td>${d < td ? (r.done[d] || '–') : d === td ? `${r.done[d] || 0}/${r.total[d] || 0}` : `${r.total[d] || 0}/${r.cap(d)}`}${d < td && r.done[d] >= st.pace ? ' ✓' : ''}</td>`).join('')}${anyOver ? '<td></td>' : ''}</tr></tbody>
      </table></div>
      <p class="pverdict"><span class="mono kick">VERDICT</span> ${verdict}</p>
      <div class="two pbtns"><button class="btn primary" data-addsubj>+ Add subject</button><button class="btn ghost" data-pickmosaic>Pick cards in the Mosaic</button><button class="btn ghost" data-addviva>+ Add viva</button></div>
      ${vr.filter(x => x.todayQs.some(q => !vivaDoneToday(x.lane.pkg, q))).map(x => `<div class="two pbtns"><button class="btn ghost" data-vwalkplan="${esc(x.lane.pkg)}">${ICON.walkS} Walk today’s viva ${esc(x.lane.pkg)} · Q${qNumOf(x.lane.pkg, x.todayQs[0])}–Q${qNumOf(x.lane.pkg, x.todayQs[x.todayQs.length - 1])} (${x.doneToday}/${x.todayQs.length} done)</button></div>`).join('')}

      ${r.active ? `<div class="two pbtns">${r.todayPlan ? `<button class="btn ghost" data-plantoday>${ICON.walkS} Walk today’s ${r.todayPlan} in Flow</button>` : ''}<button class="btn ghost" data-chtoday>Change today…</button></div>` : ''}
      <p class="muted small">Past days show what you walked; today shows walked / planned; later days are re-planned every morning from what is left. Extra cards never lower tomorrow; a short day is spread over the days left, up to your ceiling. • marks a number you fixed.</p>
      <button class="linkbtn muted small" data-delstretch>Delete ${esc(st.name)}</button>
    </div>
    ${nav('')}
  </div>`;
  bindGo(); bindGoingOut();
  const re = () => keep(renderPlan);
  app.querySelectorAll('[data-stretch]').forEach(b => b.onclick = () => { p.current = b.dataset.stretch; savePlan(false); re(); });
  const ns = app.querySelector('[data-newstretch]'); if (ns) ns.onclick = () => { newStretch({}); re(); };
  app.querySelector('[data-pstart]').onchange = e => { if (e.target.value) { st.start = e.target.value; savePlan(); re(); } };
  app.querySelectorAll('[data-pdays]').forEach(b => b.onclick = () => { st.days = Math.max(1, Math.min(60, st.days + +b.dataset.pdays)); savePlan(); re(); });
  app.querySelectorAll('[data-pceil]').forEach(b => b.onclick = () => { st.ceiling = Math.max(st.pace, Math.min(150, st.ceiling + +b.dataset.pceil)); savePlan(); re(); });
  const pr = app.querySelector('[data-ppace]');
  pr.oninput = () => { app.querySelector('[data-ppace-out]').textContent = pr.value + ' a day'; };
  pr.onchange = () => { st.pace = +pr.value; if (st.ceiling < st.pace) st.ceiling = st.pace; savePlan(); re(); };
  app.querySelectorAll('[data-dtype]').forEach(th => th.onclick = () => dayTypeSheet(st, th.dataset.dtype, re));
  app.querySelectorAll('td.tap[data-cell]').forEach(td2 => td2.onclick = () => { const [id, d] = td2.dataset.cell.split('|'); pinSheet(st, id, d, r.cells[id][d] || 0, re); });
  app.querySelectorAll('td.nm[data-subj]').forEach(t => t.onclick = () => { const id = t.dataset.subj; if (id === 'repair') repairSheet(st, re); else subjectSheet(st, id, re); });
  app.querySelector('[data-addsubj]').onclick = () => addSubjectSheet(st, re);
  app.querySelector('[data-addviva]').onclick = () => vivaLaneSheet(st, null, re);
  app.querySelectorAll('td.nm[data-vlane]').forEach(t => t.onclick = () => vivaLaneSheet(st, t.dataset.vlane, re));
  app.querySelectorAll('[data-vwalkplan]').forEach(b => b.onclick = () => walkVivaPlan(b.dataset.vwalkplan));
  app.querySelector('[data-pickmosaic]').onclick = () => { P.set('pickOn', true); P.set('pickForPlan', true); go('#/sys/all'); };
  const pt = app.querySelector('[data-plantoday]'); if (pt) pt.onclick = () => { const q = todayCards(st); if (q.length) startFlow(q, { label: 'The Plan · today', returnTo: location.hash }); else toast('Today’s plan is done.'); };
  const ct = app.querySelector('[data-chtoday]'); if (ct) ct.onclick = () => changeTodaySheet(st, re);
  const un = app.querySelector('[data-pundo]'); if (un) un.onclick = () => { if (undoPlan()) { toast('Undone.'); re(); } };
  app.querySelector('[data-delstretch]').onclick = () => confirmSheet(`Delete ${st.name}? Its subjects and numbers go; your walked cards stay.`, 'Delete', () => { deleteStretch(st.id); re(); toast(`Deleted ${st.name}. Undo is on the Plan.`); });
  if (planPending) { const pend = planPending; planPending = null; nameSubjectSheet(st, pend, re); }
}
/* ============================ T-141: the day plan ============================
   Blocks of the day in 10, 15, 30 or 60-minute rows. Meals and Out are fixed; breaks are earned while studying and fall due
   at the end of a question; a break taken late moves what follows (up to the next fixed block). */
const DCOL = { study: 'dz-study', break: 'dz-break', rest: 'dz-rest', meal: 'dz-meal', out: 'dz-out' };
const DDEF = { study: 60, break: 10, rest: 30, meal: 45, out: 60 };
function renderDay() {
  const day = today(), set = DAYP.settingsDay(), z = set.zoom, n = DAYP.nowInfo(), b = DAYP.bank(), list = n.list;
  const lo = Math.min(n.m - 60, ...list.map(x => x.a)), hi = Math.max(23 * 60, ...list.map(x => x.b));
  const from = Math.max(0, Math.floor(lo / 60) * 60), to = Math.min(24 * 60, Math.ceil(hi / 60) * 60);
  const RH = 30, ppm = RH / z, rows = [];
  for (let m = from; m < to; m += z) rows.push(m);
  const tot = t => list.filter(x => x.type === t).reduce((a, x) => a + x.b - x.a, 0);
  const cur = n.cur, nx = n.next;
  const nowLine = cur ? `<b>${esc(DAYP.typeName(cur.type))}${cur.label ? ' · ' + esc(cur.label) : ''}</b> until ${DAYP.hm(n.sessionEnd || cur.b)} · <b>${DAYP.dur((n.sessionEnd || cur.b) - n.m)}</b> left` : nx ? `Free now · next <b>${esc(DAYP.typeName(nx.type))}</b> at ${DAYP.hm(nx.a)}` : 'Nothing planned for the rest of today';
  const nb = n.nextBreak && (!cur || n.nextBreak.id !== cur.id) ? `Next: ${esc(DAYP.typeName(n.nextBreak.type))} ${DAYP.dur(n.nextBreak.b - n.nextBreak.a)} at ${DAYP.hm(n.nextBreak.a)} · in ${DAYP.dur(n.nextBreak.a - n.m)}` : '';
  app.innerHTML = `<div class="screen dayp">
    <header class="top"><a class="iconbtn" href="#/plan" aria-label="Back to the Plan">${ICON.back}</a>
      <span class="tt"><span class="mono kick">DAY PLAN · ${esc(new Date().toLocaleDateString([], { weekday: 'short', day: 'numeric', month: 'short' }).toUpperCase())}</span><span class="h1s">Today</span></span><span class="dz-clock mono" id="dz-clock">${DAYP.hm(n.m)}</span>${goingOutButton()}</header>
    <div class="scroll pad dzbody">
      <section class="dz-now">
        <p class="dz-l1">${nowLine}</p>${nb ? `<p class="dz-l2 mono">${nb}</p>` : ''}
        <p class="dz-l2 mono">BREAKS EARNED <b>${Math.floor(b.left)} min</b> · studied ${DAYP.dur(b.studied)} today · ${DAYP.dur(b.since)} since the last break</p>
      </section>
      <div class="dz-bar">
        <div class="seg">${[10, 15, 30, 60].map(v => `<button class="${v === z ? 'on' : ''}" data-dzz="${v}">${v === 60 ? '1 h' : v + ' min'}</button>`).join('')}</div>
        <span class="dz-tot mono"><span class="dz-study">STUDY ${DAYP.dur(tot('study'))}</span> · <span class="dz-break">BREAKS ${DAYP.dur(tot('break'))}</span> · <span class="dz-rest">REST, MEALS, OUT ${DAYP.dur(tot('rest') + tot('meal') + tot('out'))}</span></span>
      </div>
      <div class="chips dz-add">${DAYP.TYPES.map(([k, l]) => `<button class="chip ${DCOL[k]}" data-dzadd="${k}">+ ${l}</button>`).join('')}<button class="chip dash" data-dzfill>Fill free time…</button><button class="chip dash" data-dzrule>Breaks: 1 min per ${set.ratio} min · ${set.size} min</button></div>
      <div class="dz-tl" style="height:${(to - from) * ppm}px">
        ${rows.map(m => `<button class="dz-row${m % 60 === 0 ? ' hr' : ''}" style="top:${(m - from) * ppm}px;height:${RH}px" data-dzat="${m}" aria-label="Add at ${DAYP.hm(m)}"><span class="mono">${m % 60 === 0 || z < 60 ? DAYP.hm(m) : ''}</span></button>`).join('')}
        ${list.map(x => { const h = Math.max(8, (x.b - x.a) * ppm - 2), small = h < 24; return `<button class="dz-blk ${DCOL[x.type]}${x.done ? ' done' : ''}${x === cur ? ' now' : ''}" style="top:${(x.a - from) * ppm}px;height:${h}px" data-dzb="${x.id}">${small ? '' : `<b>${esc(DAYP.typeName(x.type))}</b><span class="mono">${DAYP.hm(x.a)}–${DAYP.hm(x.b)}</span>${x.label ? `<i>${esc(x.label)}</i>` : ''}`}</button>`; }).join('')}
        ${n.m >= from && n.m <= to ? `<div class="dz-nowl" style="top:${(n.m - from) * ppm}px"></div>` : ''}
      </div>
      <p class="muted small">Tap a row to add a block there, or a block to change it. Meals and Out stay where you put them. A break falls due at the end of a question (never in the middle of one); if you take it late, the blocks after it move, up to the next meal or Out.</p>
      <button class="linkbtn muted small" data-dzclear>Clear today’s plan</button>
    </div>
    ${nav('')}
  </div>`;
  bindGo(); bindGoingOut();
  const re = () => keep(renderDay);
  app.querySelectorAll('[data-dzz]').forEach(x => x.onclick = () => { DAYP.setSetting('zoom', +x.dataset.dzz); re(); });
  app.querySelectorAll('[data-dzat]').forEach(x => x.onclick = () => dayBlockSheet(day, { type: 'study', a: +x.dataset.dzat }, re));
  app.querySelectorAll('[data-dzb]').forEach(x => x.onclick = () => dayBlockSheet(day, list.find(y => y.id === x.dataset.dzb), re));
  app.querySelectorAll('[data-dzadd]').forEach(x => x.onclick = () => { const t = x.dataset.dzadd, a = Math.ceil(n.m / z) * z; dayBlockSheet(day, { type: t, a, b: a + DDEF[t] }, re); });
  app.querySelector('[data-dzfill]').onclick = () => dayFillSheet(day, n.m, re);
  app.querySelector('[data-dzrule]').onclick = () => dayRuleSheet(re);
  app.querySelector('[data-dzclear]').onclick = () => confirmSheet('Clear today’s day plan?', 'Clear', () => { DAYP.clearDay(day); re(); });
  const nl = app.querySelector('.dz-nowl'); if (nl) nl.scrollIntoView({ block: 'center' });
  clearInterval(window.__dzT); window.__dzT = setInterval(() => { if (!document.querySelector('.screen.dayp')) return clearInterval(window.__dzT); const c = document.getElementById('dz-clock'); if (c) c.textContent = DAYP.hm(DAYP.nowMin()); }, 15000);
}
const toHM = m => String(Math.floor(m / 60) % 24).padStart(2, '0') + ':' + String(Math.round(m) % 60).padStart(2, '0');
const fromHM = v => { const [h, mm] = String(v || '').split(':').map(Number); return isNaN(h) ? null : h * 60 + (mm || 0); };
function dayBlockSheet(day, x, re) {
  const isNew = !x.id; let type = x.type || 'study', a = x.a, b = x.b != null ? x.b : x.a + DDEF[type];
  planSheet(isNew ? 'Add to the day' : DAYP.typeName(type) + ' block', 'DAY PLAN', `<div class="chips" data-dzt>${DAYP.TYPES.map(([k, l]) => `<button class="chip ${DCOL[k]}${k === type ? ' on' : ''}" data-t="${k}">${l}</button>`).join('')}</div>
    <div class="pnew"><label>From <input type="time" step="300" value="${toHM(a)}" data-dza></label><label>to <input type="time" step="300" value="${toHM(b)}" data-dzb2></label><label>Note <input type="text" placeholder="e.g. Viva P1 Q5–Q9" value="${esc(x.label || '')}" data-dzl></label></div>
    <div class="chips small">${[10, 15, 20, 30, 45, 60, 90, 120].map(d => `<button class="chip" data-dzd="${d}">${d < 60 ? d + ' min' : d / 60 + ' h'}</button>`).join('')}</div>
    <div class="sheet-f">${isNew ? '' : '<button class="btn ghost" data-dzdel>Remove</button>'}<button class="btn primary" data-dzsave>${isNew ? 'Add' : 'Save'}</button></div>`, (w, c) => {
    const A = w.querySelector('[data-dza]'), B = w.querySelector('[data-dzb2]');
    w.querySelectorAll('[data-t]').forEach(t => t.onclick = () => { type = t.dataset.t; w.querySelectorAll('[data-t]').forEach(y => y.classList.toggle('on', y === t)); if (isNew) B.value = toHM((fromHM(A.value) || a) + DDEF[type]); });
    w.querySelectorAll('[data-dzd]').forEach(t => t.onclick = () => { B.value = toHM((fromHM(A.value) || a) + +t.dataset.dzd); });
    w.querySelector('[data-dzsave]').onclick = () => {
      const a2 = fromHM(A.value), b2 = fromHM(B.value); if (a2 == null || b2 == null || b2 <= a2) { toast('The end must be after the start.'); return; }
      const ch = { type, a: a2, b: b2, label: w.querySelector('[data-dzl]').value.trim() };
      if (isNew) DAYP.addBlock(day, ch); else DAYP.updateBlock(day, x.id, ch);
      c(); re();
    };
    const dl = w.querySelector('[data-dzdel]'); if (dl) dl.onclick = () => { DAYP.removeBlock(day, x.id); c(); re(); };
  });
}
function dayFillSheet(day, now, re) {
  const a0 = Math.ceil(now / 15) * 15;
  planSheet('Fill free time', 'DAY PLAN', `<p class="muted small">Puts study in the empty time between two times, with a break every so often. Blocks already there are kept. The breaks are a plan: when one falls due you finish the question you are on first.</p>
    <div class="pnew"><label>From <input type="time" step="300" value="${toHM(a0)}" data-fa></label><label>to <input type="time" step="300" value="${toHM(Math.min(23 * 60 + 30, a0 + 180))}" data-fb></label></div>
    <div class="chips">${[[50, 10], [45, 15], [90, 15], [120, 20]].map(([s2, b2], i) => `<button class="chip${i === 0 ? ' on' : ''}" data-fr="${s2}|${b2}">Study ${s2} min · break ${b2}</button>`).join('')}</div>
    <div class="sheet-f"><button class="btn primary" data-fgo>Fill</button></div>`, (w, c) => {
    let r = [50, 10];
    w.querySelectorAll('[data-fr]').forEach(t => t.onclick = () => { r = t.dataset.fr.split('|').map(Number); w.querySelectorAll('[data-fr]').forEach(y => y.classList.toggle('on', y === t)); });
    w.querySelector('[data-fgo]').onclick = () => { const a = fromHM(w.querySelector('[data-fa]').value), b = fromHM(w.querySelector('[data-fb]').value); if (a == null || b == null || b <= a) { toast('The end must be after the start.'); return; } DAYP.fillRhythm(day, a, b, r[0], r[1]); c(); re(); };
  });
}
function dayRuleSheet(re) {
  const s0 = DAYP.settingsDay();
  planSheet('Earned breaks', 'DAY PLAN', `<p class="muted small">Every few minutes of study earn a minute of break. When enough is earned after a long stretch, a break falls due at the end of the question you are on.</p>
    <p class="mono small">ONE MINUTE OF BREAK FOR EVERY</p><div class="chips">${[4, 5, 6, 8].map(v => `<button class="chip${s0.ratio === v ? ' on' : ''}" data-rr="${v}">${v} min studied</button>`).join('')}</div>
    <p class="mono small">A BREAK IS</p><div class="chips">${[5, 10, 15, 20].map(v => `<button class="chip${s0.size === v ? ' on' : ''}" data-rs="${v}">${v} min</button>`).join('')}</div>
    <p class="mono small">DUE AFTER AT LEAST</p><div class="chips">${[30, 45, 60, 90].map(v => `<button class="chip${s0.gap === v ? ' on' : ''}" data-rg="${v}">${v} min of study</button>`).join('')}</div>
    <div class="sheet-f"><button class="btn primary" data-x>Done</button></div>`, (w, c) => {
    const bind = (attr, key) => w.querySelectorAll(`[${attr}]`).forEach(t => t.onclick = () => { DAYP.setSetting(key, +t.getAttribute(attr)); w.querySelectorAll(`[${attr}]`).forEach(y => y.classList.toggle('on', y === t)); });
    bind('data-rr', 'ratio'); bind('data-rs', 'size'); bind('data-rg', 'gap');
    w.querySelector('[data-x]').addEventListener('click', () => re());
  });
}
/* ============================ T-142: the phone Desk ============================ */
// what the phone shows, sent by the Tab: small, no card text beyond the current question's title
function deskSnap() {
  const n = DAYP.nowInfo(), b = DAYP.bank(), cb = curBreak(), sd = DAYP.settingsDay();
  const o = { v: 1, day: { bl: n.list.map(x => [x.type, x.a, x.b, x.label || '', x.done ? 1 : 0]), left: Math.floor(b.left), since: Math.round(b.since), studied: Math.round(b.studied), size: sd.size }, brk: cb ? { r: reasonOf(cb.reason)[1], s: cb.start, al: cb.allowed || 0 } : null, f: null };
  if (!flow || flow.browse) return o;
  const c = !flow.done && current(), nT = flow.times.length, avg = nT ? flow.times.reduce((a, x) => a + x, 0) / nT : avgPace() || 0;
  const f = o.f = { label: flow.label, viva: flow.viva || '', t0: flow.t0, p: flow.pausedAt || 0, up: !!flow.userPause, done: !!flow.done, idx: flow.idx, total: flow.queue.length, avg: Math.round(avg), cardT0: flow.cardT0, card: c ? [c.deck, c.code, c.section || ''] : null };
  if (!flow.viva) return o;
  const L = flow.look ? flow.lookStep : flow.st ? flow.st.s : null;
  f.step = L ? { k: L.kind, qn: L.q ? qNumOf(L.pkg, L.q) : 0, t0: flow.look ? flow.lookT0 : flow.st ? flow.st.t0 : 0, look: !!flow.look, qms: L.q ? flow.qms[L.pkg + '|' + L.q] || 0 : 0 } : null;
  const td = vivaTileData(), SC = { cur: 'n', vdone: 'd', vseen: 's', vahead: 'a' };
  f.gi = td.gi; f.g = td.groups.map(g => [g.qn, g.steps.map(x => x.lab + SC[x.st] + (x.look ? '!' : '')).join(',')]);
  const P2 = vivaPkg(flow.viva), curQ = L && L.q, mk = q => (flow.vm ? vivaLast(flow.vm, flow.viva, q) : '') || '';
  if (P2) { f.pt = P2.title; f.qs = P2.questions.map(q => [qNumOf(flow.viva, q.q), q.q === curQ ? 2 : (flow.vdone && flow.vdone[flow.viva + '|' + q.q]) || vivaDoneToday(flow.viva, q.q) ? 1 : 0, mk(q.q).slice(0, 1), Math.round((flow.qms[flow.viva + '|' + q.q] || 0) / 1000)]); const cq = curQ && vivaQ(flow.viva, curQ); f.qt = cq ? cq.text : ''; }
  return o;
}
// Flow tab → Phone Desk: which device is this?
function deskChooser() {
  planSheet('Phone Desk', 'TRACE DESK', `<p class="muted small">The phone beside the Tab shows the time, your session and breaks, this question and card, and the mosaic, live. Both need Trace open and the same Wi-Fi or hotspot.</p>
    <div class="rs-grid"><button class="btn ghost rs" data-dtab><b>This is the Tab</b><small>show a code for the phone</small></button><button class="btn ghost rs" data-dph><b>This is the phone</b><small>open the Desk</small></button></div>`, (w, c) => {
    w.querySelector('[data-dtab]').onclick = () => { c(); deskHostSheet(); };
    w.querySelector('[data-dph]').onclick = () => { c(); go('#/desk'); };
  });
}
function deskHostSheet() {
  const ST = { off: 'Not linked', waiting: 'Waiting for the phone…', live: 'Linked · the phone is showing this Tab', lost: 'Link lost · offering it again…', idle: 'The phone did not answer in 3 minutes', error: 'Could not reach Drive to offer the link', unsupported: 'This browser cannot make the link' };
  planSheet('Link a phone', 'TRACE DESK', `<p class="muted small">On the phone: open Trace, then Flow › Phone Desk › This is the phone, and type this code.</p>
    <p class="pdk-code mono" data-dcode>${esc(DESK.deskCode())}</p><p class="mono small" data-dst></p>
    <div class="sheet-f"><button class="btn ghost" data-dnew>New code</button><button class="btn ghost" data-doff>Unlink</button><button class="btn primary" data-dgo>Offer the link</button></div>`, (w, c) => {
    const st = w.querySelector('[data-dst]'), show = s2 => { st.textContent = ST[s2] || s2; };
    show(DESK.deskState()); const off = DESK.onDesk(s2 => { if (!w.isConnected) return off(); show(s2); });
    w.querySelector('[data-dgo]').onclick = () => DESK.startHost();
    w.querySelector('[data-dnew]').onclick = () => { w.querySelector('[data-dcode]').textContent = DESK.newDeskCode(); DESK.startHost(); };
    w.querySelector('[data-doff]').onclick = () => { DESK.stopHost(); };
    if (!['live', 'waiting'].includes(DESK.deskState())) DESK.startHost();
  });
}
// the phone: #/desk (portrait: timers on top, mosaic below; landscape: side by side)
function renderDeskPage() {
  const view = () => P.get('pdkView', 'cards'), rows = () => P.get('pdkRows', 'q');
  app.innerHTML = `<div class="screen pdk">
    <header class="pdk-top"><div><span class="mono kick"><a class="pdk-x" href="#/flow" aria-label="Close the Desk">‹</a> TRACE DESK</span><span class="mono pdk-link" id="pdk-link"></span></div><div class="pdk-clock"><b class="mono" id="pdk-clock"></b><span class="mono" id="pdk-date"></span></div></header>
    <div class="pdk-body">
      <section class="pdk-left">
        <div class="pdk-card pdk-sess"><svg viewBox="0 0 128 128" class="pdk-ring" aria-hidden="true"><circle cx="64" cy="64" r="56" class="r0"></circle><circle cx="64" cy="64" r="56" class="r1" id="pdk-r1" stroke-dasharray="351.9" stroke-dashoffset="351.9"></circle><text x="64" y="62" text-anchor="middle" id="pdk-rt">–</text><text x="64" y="80" text-anchor="middle" class="sm" id="pdk-rs"></text></svg>
          <div class="pdk-sx"><span class="mono kick" id="pdk-bk">SESSION</span><b class="pdk-big" id="pdk-until"></b><span class="mono pdk-next" id="pdk-next"></span><span class="mono pdk-earn" id="pdk-earn"></span></div></div>
        <div class="pdk-tm"><div><span class="mono kick">Session</span><b class="mono" id="pdk-ts">–</b><i class="mono" id="pdk-ts2"></i></div><div class="q"><span class="mono kick" id="pdk-qn">Question</span><b class="mono" id="pdk-tq">–</b><i class="mono" id="pdk-tq2"></i></div><div><span class="mono kick" id="pdk-cl">Card</span><b class="mono" id="pdk-tc">–</b><i class="mono" id="pdk-tc2"></i></div></div>
        <div class="pdk-strip"><div class="pdk-hrs mono" id="pdk-hrs"></div><div class="pdk-bar" id="pdk-bar"></div></div>
        <p class="pdk-where" id="pdk-where"></p>
      </section>
      <section class="pdk-right">
        <div class="pdk-mh"><span class="pdk-pos" id="pdk-pos"></span><div class="seg"><button data-pv="q">Questions</button><button data-pv="cards">Cards</button></div><div class="seg" id="pdk-rowseg"><button data-pr="q">By question</button><button data-pr="5">5 a row</button></div></div>
        <div class="pdk-mosaic" id="pdk-mosaic"></div>
        <p class="pdk-leg mono"><span class="d">■ done</span> <span class="s">■ done earlier in this walk</span> <span class="n">□ now</span> <span class="a">■ ahead</span> · ● O / C lessons · S spine</p>
      </section>
    </div>
    <div class="pdk-cover" id="pdk-cover" hidden></div>
    <div class="pdk-pair" id="pdk-pair" hidden><span class="mono kick">LINK TO THE TAB</span><p class="muted small">On the Tab: Flow › Phone Desk › This is the Tab. Type the code it shows.</p><div class="pnew"><input type="text" inputmode="numeric" maxlength="4" placeholder="0000" data-pc value="${esc(DESK.guestCode())}"></div><button class="btn primary" data-pjoin>Link</button><button class="linkbtn muted small" data-pleave>Forget this Tab</button><p class="mono small" id="pdk-pst"></p></div>
  </div>`;
  const $p = id => document.getElementById(id);
  const segs = () => { app.querySelectorAll('[data-pv]').forEach(b => b.classList.toggle('on', b.dataset.pv === view())); app.querySelectorAll('[data-pr]').forEach(b => b.classList.toggle('on', b.dataset.pr === rows())); $p('pdk-rowseg').hidden = view() !== 'cards'; };
  app.querySelectorAll('[data-pv]').forEach(b => b.onclick = () => { P.set('pdkView', b.dataset.pv); segs(); lastM = ''; paint(); });
  app.querySelectorAll('[data-pr]').forEach(b => b.onclick = () => { P.set('pdkRows', b.dataset.pr); segs(); lastM = ''; paint(); });
  segs();
  const GS = { off: 'Not linked', looking: 'Looking for the Tab…', connecting: 'Linking…', live: '● linked to the Tab', lost: 'Link lost · trying again…', notfound: 'The Tab is not offering a link (open Phone Desk on the Tab)', badcode: 'The code has 4 digits', error: 'Could not reach Drive', unsupported: 'This browser cannot make the link' };
  app.querySelector('[data-pjoin]').onclick = () => DESK.joinDesk(app.querySelector('[data-pc]').value);
  app.querySelector('[data-pleave]').onclick = () => { DESK.leaveDesk(); app.querySelector('[data-pc]').value = ''; };
  const showState = st => { $p('pdk-link').textContent = GS[st] || st; $p('pdk-pst').textContent = GS[st] || st; $p('pdk-pair').hidden = st === 'live' || (DESK.guestSnap() && ['lost', 'connecting'].includes(st)); };
  const offG = DESK.onGuest(st => { if (!document.querySelector('.screen.pdk')) return offG(); showState(st); paint(); });
  showState(DESK.guestState());
  // keep the phone's screen on while the Desk is open
  let wl = null; const lock = async () => { try { if (navigator.wakeLock && document.visibilityState === 'visible') wl = await navigator.wakeLock.request('screen'); } catch (e) { /* */ } };
  lock(); document.addEventListener('visibilitychange', lock);
  let lastM = '';
  const paint = () => {
    if (!document.querySelector('.screen.pdk')) { clearInterval(tk); document.removeEventListener('visibilitychange', lock); try { wl && wl.release(); } catch (e) { /* */ } return; }
    const S2 = DESK.guestSnap(), off = S2 ? DESK.guestAt() - S2.ts : 0, now = Date.now() - off, nm = DAYP.nowMin(now);
    $p('pdk-clock').textContent = DAYP.hm(DAYP.nowMin()); $p('pdk-date').textContent = new Date().toLocaleDateString([], { weekday: 'short', day: 'numeric', month: 'short' }).toUpperCase();
    if (!S2) { $p('pdk-where').textContent = 'Waiting for the Tab.'; return; }
    const D2 = S2.day, bl = D2.bl.map(([t, a, b, l, d]) => ({ t, a, b, l, d })), cur = bl.find(x => x.a <= nm && x.b > nm);
    let s0 = null, s1 = null; if (cur && cur.t === 'study') { s0 = cur.a; s1 = cur.b; for (const x of bl) if (x.a === s1 && x.t === 'study') s1 = x.b; for (const x of [...bl].reverse()) if (x.b === s0 && x.t === 'study') s0 = x.a; }
    const nb = bl.find(x => x.a > nm && x.t !== 'study');
    const ring = $p('pdk-r1'), F = S2.f;
    if (s1 != null) { const fr = Math.min(1, Math.max(0, (nm - s0) / (s1 - s0))); ring.setAttribute('stroke-dashoffset', (351.9 * (1 - fr)).toFixed(1)); $p('pdk-rt').textContent = clockHM(s1 - nm); $p('pdk-rs').textContent = 'LEFT'; $p('pdk-bk').textContent = 'STUDY BLOCK'; $p('pdk-until').textContent = 'until ' + DAYP.hm(s1); }
    else { ring.setAttribute('stroke-dashoffset', '351.9'); $p('pdk-rt').textContent = cur ? '' : '–'; $p('pdk-rs').textContent = cur ? DAYP.typeName(cur.t).toUpperCase() : 'NO PLAN'; $p('pdk-bk').textContent = cur ? DAYP.typeName(cur.t).toUpperCase() : 'DAY PLAN'; $p('pdk-until').textContent = cur ? 'until ' + DAYP.hm(cur.b) : 'Nothing planned now'; }
    $p('pdk-next').textContent = S2.brk ? `ON ${S2.brk.r.toUpperCase()} · ${S2.brk.al ? Math.max(0, Math.ceil(S2.brk.al - (now - S2.brk.s) / 60000)) + ' min left' : DAYP.dur((now - S2.brk.s) / 60000) + ' so far'}` : nb ? `NEXT · ${DAYP.typeName(nb.t).toUpperCase()} ${DAYP.dur(nb.b - nb.a)} at ${DAYP.hm(nb.a)} · in ${DAYP.dur(nb.a - nm)}` : '';
    $p('pdk-earn').textContent = `BREAK EARNED ${D2.left} MIN · ${DAYP.dur(D2.since)} SINCE THE LAST`;
    // timers
    const tnow = F && F.p ? F.p : now;
    if (F) {
      $p('pdk-ts').textContent = clock((tnow - F.t0) / 1000); $p('pdk-ts2').textContent = F.label || '';
      if (F.step) { $p('pdk-qn').textContent = 'Question ' + (F.step.qn || ''); const sm = Math.max(0, tnow - F.step.t0); $p('pdk-tq').textContent = clock((F.step.qms + (F.step.look ? 0 : sm)) / 1000); $p('pdk-tq2').textContent = F.step.look ? 'looking back' : ''; $p('pdk-cl').textContent = { card: 'Card', vq: 'Opening lesson', vclose: 'Closing lesson', spine: 'Spine' }[F.step.k] || 'Step'; $p('pdk-tc').textContent = clock(sm / 1000); }
      else { $p('pdk-qn').textContent = 'Question'; $p('pdk-tq').textContent = '–'; $p('pdk-cl').textContent = 'Card'; $p('pdk-tc').textContent = F.done ? '–' : clock(Math.max(0, tnow - F.cardT0) / 1000); }
      const left = Math.max(0, F.total - F.idx); $p('pdk-tc2').textContent = F.avg ? 'pace ' + fmtDur(F.avg / 1000) + ' · ends ' + DAYP.hm(DAYP.nowMin(Date.now() + left * F.avg)) : '';
      $p('pdk-where').textContent = F.qt ? F.qt : F.card ? F.card[2] + ' · ' + F.card[1] : '';
      $p('pdk-pos').textContent = F.viva ? `Q ${F.step ? F.step.qn : ''} of ${(F.qs || []).length} · card ${Math.min(F.total, F.idx + 1)} of ${F.total}` : `card ${Math.min(F.total, F.idx + 1)} of ${F.total}`;
    } else { ['pdk-ts', 'pdk-tq', 'pdk-tc'].forEach(i => $p(i).textContent = '–'); $p('pdk-where').textContent = 'No flow open on the Tab.'; $p('pdk-pos').textContent = ''; }
    const cv = $p('pdk-cover'); const pz = F && F.p; cv.hidden = !pz && !S2.brk; cv.innerHTML = S2.brk ? `<span class="mono kick">ON A BREAK</span><b>${esc(S2.brk.r)}</b>` : pz ? `<span class="mono kick">PAUSED</span><b>The clock is stopped</b>` : '';
    // day strip: the hour before now and three after
    const h0 = Math.floor(nm / 60) * 60 - 60, h1 = h0 + 240, pc = m => ((Math.min(h1, Math.max(h0, m)) - h0) / 240 * 100).toFixed(2) + '%';
    $p('pdk-hrs').innerHTML = [0, 1, 2, 3, 4].map(i => `<span style="left:${i * 25}%">${DAYP.hm(h0 + i * 60).replace(':00', '')}</span>`).join('');
    $p('pdk-bar').innerHTML = bl.filter(x => x.b > h0 && x.a < h1).map(x => `<i class="dz-${x.t}" style="left:${pc(x.a)};width:calc(${pc(x.b)} - ${pc(x.a)})"></i>`).join('') + `<b style="left:${pc(nm)}"></b>`;
    // the mosaic: only redrawn when it changes
    const key = JSON.stringify([view(), rows(), F && F.g, F && F.qs]); if (key === lastM) return; lastM = key;
    const M = $p('pdk-mosaic');
    if (!F || !F.viva) { M.innerHTML = '<p class="muted small">The mosaic shows during a viva walk.</p>'; return; }
    const tile = x => { const look = x.endsWith('!'), y = look ? x.slice(0, -1) : x, st = y.slice(-1), lab = y.slice(0, -1); return `<i class="pt ${st}${/^[OCS]$/.test(lab) ? ' les' : ''}${look ? ' look' : ''}">${lab}</i>`; };
    if (view() === 'q') M.innerHTML = `<div class="pdk-qg">${(F.qs || []).map(([n2, st, mk, sec]) => `<span class="pq s${st}${mk ? ' m' + mk : ''}"><b>${n2}</b><i>${sec ? clockShort(sec) : ''}</i></span>`).join('')}</div>`;
    else if (rows() === '5') M.innerHTML = `<div class="pdk-g5">${F.g.flatMap(([n2, t]) => t.split(',').map((x, i) => i === 0 ? tile(x).replace('>O<', '>O' + n2 + '<') : tile(x))).join('')}</div>`;
    else M.innerHTML = F.g.map(([n2, t], i) => `<div class="pdk-row${i === F.gi ? ' on' : ''}"><span class="mono">Q${n2}</span><div>${t.split(',').map(tile).join('')}</div></div>`).join('');
    const on = M.querySelector('.pdk-row.on, .pq.s2, .pt.n'); if (on) on.scrollIntoView({ block: 'center', behavior: 'smooth' });
  };
  const tk = setInterval(paint, 1000); paint();
  if (DESK.guestCode() && ['off', 'notfound', 'error'].includes(DESK.guestState())) DESK.joinDesk(DESK.guestCode());
}
const clockHM = m => { m = Math.max(0, Math.round(m)); return Math.floor(m / 60) + ':' + String(m % 60).padStart(2, '0'); };
const clockShort = sec => sec >= 3600 ? Math.floor(sec / 3600) + 'h' + String(Math.floor(sec % 3600 / 60)).padStart(2, '0') : Math.floor(sec / 60) + ':' + String(sec % 60).padStart(2, '0');
// in a flow: is a break due? asked only between questions (viva) or between sections (other flows)
function checkBreakDue() {
  if (!flow || flow.browse || flow.pausedAt || document.querySelector('.f-due')) return;
  const d = DAYP.breakDue(); if (!d) return;
  const el = document.createElement('div'); el.className = 'f-due';
  el.innerHTML = `<span><b>Break due</b> · ${d.why === 'planned' ? `planned ${d.mins} min` : d.why === 'end' ? 'this study block is over' : `${Math.floor(d.bank.left)} min earned`} · ${DAYP.dur(d.bank.since)} since the last one</span><button class="pillbtn" data-dtake>Take a break</button><button class="btn ghost" data-dsnz>One more ${flow.viva ? 'question' : 'section'}</button>`;
  el.querySelector('[data-dtake]').onclick = () => { el.remove(); goingOutSheet(); };
  el.querySelector('[data-dsnz]').onclick = () => { el.remove(); DAYP.snooze(); };
  const main = document.querySelector('.flow .f-main'); if (main) main.prepend(el);
}
// T-138: a viva package in the plan: which questions, how many a day, from which day
function vivaLaneSheet(st, id, re) {
  const ps = vivaPkgs(); if (!ps.length) { toast('No viva package on this device yet.'); return; }
  const l = id ? (st.viva || []).find(x => x.id === id) : null;
  let pkg = l ? l.pkg : ps[0].package;
  planSheet(l ? 'Viva in the plan' : 'Add a viva package', 'THE PLAN · VIVA', `<div class="pnew">
      <label>Package <select data-vpkg>${ps.map(p2 => `<option value="${esc(p2.package)}"${p2.package === pkg ? ' selected' : ''}>${esc(p2.package)} · ${esc(p2.title)}</option>`).join('')}</select></label>
      <label>From question <input type="number" min="1" data-vfromq></label><label>to <input type="number" min="1" data-vtoq></label>
      <label>Questions a day <input type="number" min="1" max="99" placeholder="spread" data-vper></label>
      ${startSelect(st, (l && l.from) || '', 'data-vfrom')}</div>
    <p class="muted small">A question is done when you reach its spine in a walk. Viva questions have their own row and never use your card pace. Leave “a day” empty to spread them over the days left.</p>
    <div class="sheet-f">${l ? '<button class="btn ghost" data-vdel>Remove from plan</button>' : ''}<button class="btn primary" data-vsave>${l ? 'Save' : 'Add to plan'}</button></div>`, (w, c) => {
    const setRange = () => { const P2 = vivaPkg(pkg), n = P2.questions.length, qs = l && l.pkg === pkg ? l.qs : null; const a = w.querySelector('[data-vfromq]'), b = w.querySelector('[data-vtoq]'); a.value = qs ? qNumOf(pkg, qs[0]) : 1; b.value = qs ? qNumOf(pkg, qs[qs.length - 1]) : n; a.max = b.max = n; };
    setRange(); if (l && l.perDay) w.querySelector('[data-vper]').value = l.perDay;
    w.querySelector('[data-vpkg]').onchange = e => { pkg = e.target.value; setRange(); };
    w.querySelector('[data-vsave]').onclick = () => {
      const all = vivaPkg(pkg).questions.map(q => q.q);
      let a = Math.max(1, +w.querySelector('[data-vfromq]').value || 1), b = Math.min(all.length, +w.querySelector('[data-vtoq]').value || all.length); if (b < a) [a, b] = [b, a];
      const qs = all.slice(a - 1, b), per = Math.max(0, +w.querySelector('[data-vper]').value || 0) || null, from = w.querySelector('[data-vfrom]').value || null;
      if (l) { l.pkg = pkg; l.qs = qs; l.perDay = per; l.from = from && from > st.start ? from : null; savePlan(); } else addVivaLane(st, { pkg, qs, perDay: per, from });
      c(); re();
    };
    const dl = w.querySelector('[data-vdel]'); if (dl) dl.onclick = () => { removeVivaLane(st, l.id); c(); re(); };
  });
}
function walkVivaPlan(pkg) {
  const v = vivaPlanToday(pkg); if (!v) { toast('No viva planned for today.'); return; }
  const want = new Set(v.todayQs.filter(q => !vivaDoneToday(pkg, q))); if (!want.size) { toast('Today’s viva plan is done.'); return; }
  const list = vivaQueue(pkg).list.filter(c => want.has(c.vq.q));
  if (!list.length) { toast('These cards are not on this device yet.'); return; }
  startFlow(list, { viva: pkg, label: 'Viva ' + pkg + ' · today’s plan', returnTo: location.hash });
}
function renderPlanNew() {
  app.innerHTML = `<div class="screen plan">
    <header class="top"><a class="iconbtn" href="#/loft" aria-label="Back to the Loft">${ICON.back}</a><span class="tt"><span class="mono kick">PHASE 1 · TO 30 NOV</span><span class="h1s">The Plan</span></span></header>
    <div class="scroll pad planbody"><div class="lcard">
      <span class="mono kick">FIRST STRETCH</span>
      <p>A stretch is a run of days with the subjects you want to finish in it. Trace counts the cards, spreads them over the days at your pace, and re-plans every morning.</p>
      <div class="pnew"><label>Starts <input type="date" value="${today()}" data-nstart></label><label>Days <input type="number" min="1" max="60" value="10" data-ndays></label><label>Pace <input type="number" min="20" max="150" value="65" data-npace> a day</label></div>
      <button class="btn primary" data-ncreate>Create stretch</button>
      <button class="btn ghost pundo" data-pundo ${canUndoPlan() ? '' : 'disabled'}>↶ Undo last change</button>
    </div></div>${nav('')}</div>`;
  bindGo();
  const un = app.querySelector('[data-pundo]'); if (un) un.onclick = () => { if (undoPlan()) { toast('Undone.'); renderPlan(); } };
  app.querySelector('[data-ncreate]').onclick = () => { newStretch({ start: app.querySelector('[data-nstart]').value || today(), days: +app.querySelector('[data-ndays]').value || 10, pace: +app.querySelector('[data-npace]').value || 65 }); renderPlan(); };
}
function planSheet(title, kick, html, bind) {
  const wrap = document.createElement('div'); wrap.className = 'modal';
  wrap.innerHTML = `<div class="sheet" role="dialog" aria-label="${esc(title)}"><div class="sheet-h"><span><span class="mono kick">${esc(kick)}</span><span class="sh-t">${esc(title)}</span></span><button class="iconbtn" data-x aria-label="Close">${ICON.close}</button></div>${html}</div>`;
  const close = () => wrap.remove();
  wrap.onclick = e => { if (e.target === wrap || e.target.closest('[data-x]')) close(); };
  document.body.appendChild(wrap); bind(wrap, close);
}
function confirmSheet(text, yes, fn) { planSheet(text, 'CONFIRM', `<div class="sheet-f"><button class="btn ghost" data-x>Keep</button><button class="btn primary" data-yes>${esc(yes)}</button></div>`, (w, c) => { w.querySelector('[data-yes]').onclick = () => { c(); fn(); }; }); }
function dayTypeSheet(st, d, re) {
  const cur = dayType(st, d);
  planSheet(dShort(d), 'DAY TYPE', `<div class="rs-grid">${DAY_TYPES.map(([k, l, n]) => `<button class="btn ghost rs${cur === k ? ' on' : ''}" data-t="${k}"><b>${l}</b><small>${n == null ? st.pace + ' cards (your pace)' : n + ' cards'}</small></button>`).join('')}</div>`, (w, c) => {
    w.querySelectorAll('[data-t]').forEach(b => b.onclick = () => { if (b.dataset.t === 'normal') delete st.dayType[d]; else st.dayType[d] = b.dataset.t; savePlan(); c(); re(); });
  });
}
function pinSheet(st, id, d, n, re) {
  const s = st.subjects.find(x => x.id === id), key = id + '|' + d, pinned = st.pins[key] != null;
  planSheet(`${s ? s.name : ''} · ${dShort(d)}`, 'FIX THIS NUMBER', `<p class="muted small">Trace planned ${n}. Fix your own number for this day; the days around it adjust.</p>
    <div class="pnew"><label>Cards <input type="number" min="0" max="200" value="${pinned ? st.pins[key] : n}" data-pin></label></div>
    <div class="sheet-f">${pinned ? '<button class="btn ghost" data-unpin>Let Trace decide</button>' : ''}<button class="btn primary" data-setpin>Fix it</button></div>`, (w, c) => {
    w.querySelector('[data-setpin]').onclick = () => { st.pins[key] = Math.max(0, +w.querySelector('[data-pin]').value || 0); savePlan(); c(); re(); };
    const u = w.querySelector('[data-unpin]'); if (u) u.onclick = () => { delete st.pins[key]; savePlan(); c(); re(); };
  });
}
function repairSheet(st, re) {
  const R = repairOpts(st);
  planSheet('Repair pile', 'AUTOMATIC ROW', `<p class="muted small">Cards waiting from DocT misses and Again marks. It grows by itself after each GT or module review.</p>
    <div class="pnew"><label><input type="checkbox" data-ron ${R.on ? 'checked' : ''}> Plan repairs</label></div>
    <p class="mono kick">HOW MANY A DAY</p>
    <div class="seg wide"><button class="${R.spread === 'even' ? 'on' : ''}" data-rsp="even">Spread evenly</button><button class="${R.spread === 'by' ? 'on' : ''}" data-rsp="by">Finish by a date</button><button class="${R.spread === 'fixed' ? 'on' : ''}" data-rsp="fixed">Fixed a day</button></div>
    <div class="pnew"><label data-rbox="by">Done by <select data-rby>${planDays(st).map(d => `<option value="${d}"${(R.by || planDays(st).slice(-1)[0]) === d ? ' selected' : ''}>${dShort(d)}</option>`).join('')}</select></label><label data-rbox="fixed">Cards a day <input type="number" min="0" max="100" value="${R.fixed}" data-rfix></label><label data-rbox="cap">Never more than <input type="number" min="0" max="100" value="${R.cap}" data-rcap> a day</label></div>
    <p class="muted small">You can still change today’s number in Change today.</p>
    <div class="sheet-f"><button class="btn ghost" data-rup ${R.at === 0 ? 'disabled' : ''}>↑ Earlier</button><button class="btn ghost" data-rdown ${R.at === st.subjects.length ? 'disabled' : ''}>↓ Later</button><button class="btn primary" data-rsave>Save</button></div>`, (w, c) => {
    let sp = R.spread;
    w.querySelector('[data-rup]').onclick = () => { moveRow(st, 'repair', -1); c(); re(); };
    w.querySelector('[data-rdown]').onclick = () => { moveRow(st, 'repair', 1); c(); re(); };
    const show = () => { w.querySelector('[data-rbox=by]').hidden = sp !== 'by'; w.querySelector('[data-rbox=fixed]').hidden = sp !== 'fixed'; w.querySelector('[data-rbox=cap]').hidden = sp === 'fixed'; };
    const seg = (attr, set) => w.querySelectorAll(`[${attr}]`).forEach(b => b.onclick = () => { set(b.getAttribute(attr)); w.querySelectorAll(`[${attr}]`).forEach(x => x.classList.toggle('on', x === b)); show(); });
    seg('data-rsp', v => sp = v); show();
    w.querySelector('[data-rsave]').onclick = () => {
      Object.assign(st.repair, { on: w.querySelector('[data-ron]').checked, spread: sp, cap: Math.max(0, +w.querySelector('[data-rcap]').value || 0), fixed: Math.max(0, +w.querySelector('[data-rfix]').value || 0), by: w.querySelector('[data-rby]').value || planDays(st).slice(-1)[0] });
      savePlan(); c(); re();
    };
  });
}
const splitOf = s => s.mode !== 'daily' ? 'seq' : s.daily ? 'fixed' : s.to ? 'by' : 'even';
function splitName(s) { if (s.once) return 'today only'; const k = splitOf(s); return k === 'seq' ? 'in order' : k === 'fixed' ? s.daily + ' a day' : k === 'by' ? 'finish by ' + dShort(s.to) : 'evenly'; }
// T-080: change today only — numbers (± fixes today), the order of the walk, add something for today, go deep on one subject
function changeTodaySheet(st, re) {
  const draw = () => {
    const r = compute(st), td = r.td, ids = dayOrder(st, td), R = repairOpts(st);
    const nameOf = id => id === 'repair' ? 'Repair pile' : (st.subjects.find(x => x.id === id) || {}).name || '';
    const rows = ids.filter(id => id === 'repair' ? R.on : true).map((id, i, arr) => {
      const n = r.cells[id][td] || 0, did = r.actual[id][td] || 0, pin = st.pins[id + '|' + td] != null;
      const left = id === 'repair' ? r.repairTotal : (r.leftStart[id] || 0);
      return `<div class="ct-row" data-id="${id}"><span class="ct-n"><b>${esc(nameOf(id))}</b><i>${did ? did + ' walked · ' : ''}${left} left${pin ? ' · fixed today' : ''}</i></span>
        <span class="ct-ord"><button class="iconbtn sm" data-up ${i === 0 ? 'disabled' : ''} aria-label="Walk earlier">↑</button><button class="iconbtn sm" data-dn ${i === arr.length - 1 ? 'disabled' : ''} aria-label="Walk later">↓</button></span>
        <span class="ct-num"><button class="iconbtn sm" data-m aria-label="5 fewer">−</button><b>${n}</b><button class="iconbtn sm" data-p aria-label="5 more">+</button></span>
        ${left > n ? `<button class="btn ghost sm" data-deep>Finish today (${left})</button>` : '<span></span>'}</div>`;
    }).join('');
    return { r, td, ids, html: `<p class="muted small">Only today changes. The other days re-plan from what is left. ↑↓ is the order you walk them; − + changes today’s number by 5.</p>
      <div class="ct-list">${rows}</div>
      <p class="ct-tot mono">TODAY ${r.total[td] || 0} · ROOM ${r.cap(td)}${(r.total[td] || 0) > r.cap(td) ? ' · OVER BY ' + ((r.total[td] || 0) - r.cap(td)) : ''}</p>
      <div class="sheet-f"><button class="btn ghost" data-ctundo ${canUndoPlan() ? '' : 'disabled'}>↶ Undo</button><button class="btn ghost" data-ctreset>Reset today</button><button class="btn ghost" data-ctadd>+ Add for today only</button><button class="btn primary" data-x>Done</button></div>` };
  };
  planSheet('Change today', 'THE PLAN · TODAY', '<div data-ctbody></div>', (w, c) => {
    const paint = () => {
      const d = draw(), body = w.querySelector('[data-ctbody]'); body.innerHTML = d.html;
      const pinK = id => id + '|' + d.td;
      body.querySelectorAll('.ct-row').forEach(row => {
        const id = row.dataset.id, cur = d.r.cells[id][d.td] || 0;
        const mv = k => { const ids = d.ids.slice(), i = ids.indexOf(id); ids.splice(i, 1); ids.splice(i + k, 0, id); setDayOrder(st, d.td, ids); paint(); re(); };
        row.querySelector('[data-up]').onclick = () => mv(-1); row.querySelector('[data-dn]').onclick = () => mv(1);
        row.querySelector('[data-m]').onclick = () => { st.pins[pinK(id)] = Math.max(0, cur - 5); savePlan(); paint(); re(); };
        row.querySelector('[data-p]').onclick = () => { st.pins[pinK(id)] = cur + 5; savePlan(); paint(); re(); };
        const dp = row.querySelector('[data-deep]'); if (dp) dp.onclick = () => { st.pins[pinK(id)] = id === 'repair' ? d.r.repairTotal : d.r.leftStart[id]; savePlan(); paint(); re(); };
      });
      body.querySelector('[data-ctundo]').onclick = () => { if (undoPlan()) { c(); re(); const st2 = currentStretch(); if (st2) changeTodaySheet(st2, re); } };
      body.querySelector('[data-ctreset]').onclick = () => { Object.keys(st.pins).forEach(k => { if (k.endsWith('|' + d.td)) delete st.pins[k]; }); if (st.order) delete st.order[d.td]; savePlan(); paint(); re(); };
      body.querySelector('[data-ctadd]').onclick = () => { c(); addSubjectSheet(st, re, { once: true }); };
    };
    paint();
  });
}
function subjectSheet(st, id, re) {
  const s = st.subjects.find(x => x.id === id); if (!s) return;
  const i = st.subjects.indexOf(s), done = subjectDone(s), ro = rowOrder(st), ri = ro.indexOf(s.id);
  planSheet(s.name, 'SUBJECT', `<p class="muted small">${s.keys.length} cards · ${done} walked since you added it${s.sub ? ' · ' + esc(s.sub) : ''}</p>
    <div class="pnew"><label>Name <input type="text" value="${esc(s.name)}" data-sname></label>${startSelect(st, s.from, 'data-sfrom')}</div>
    <div class="seg wide"><button class="${splitOf(s) === 'seq' ? 'on' : ''}" data-smode="seq">In order (fills the days)</button><button class="${splitOf(s) === 'even' ? 'on' : ''}" data-smode="even">Evenly</button><button class="${splitOf(s) === 'fixed' ? 'on' : ''}" data-smode="fixed">Fixed a day</button><button class="${splitOf(s) === 'by' ? 'on' : ''}" data-smode="by">Finish by</button></div>
    <div class="pnew"><label data-sbox="fixed">Cards a day <input type="number" min="0" max="150" value="${s.daily || 10}" data-sdaily></label><label data-sbox="by">Last day <input type="date" value="${s.to || planDays(st).slice(-1)[0]}" data-sto></label></div>
    <p class="muted small" data-shelp></p>
    <div class="sheet-f"><button class="btn ghost" data-sup ${ri === 0 ? 'disabled' : ''}>↑ Earlier</button><button class="btn ghost" data-sdown ${ri === ro.length - 1 ? 'disabled' : ''}>↓ Later</button><button class="btn ghost" data-sdel>Remove</button><button class="btn primary" data-ssave>Save</button></div>`, (w, c) => {
    let mode = splitOf(s);
    const HELP = { seq: 'Fills each day after the others, in the order of the rows.', even: 'The same number every day until the last day of the stretch.', fixed: 'This many every day until it is done.', by: 'Spread evenly so it is done by that day.' };
    const show = () => { w.querySelector('[data-sbox=fixed]').hidden = mode !== 'fixed'; w.querySelector('[data-sbox=by]').hidden = mode !== 'by'; w.querySelector('[data-shelp]').textContent = HELP[mode]; };
    w.querySelectorAll('[data-smode]').forEach(b => b.onclick = () => { mode = b.dataset.smode; w.querySelectorAll('[data-smode]').forEach(x => x.classList.toggle('on', x === b)); show(); }); show();
    const mv = k => { moveRow(st, s.id, k); c(); re(); };
    w.querySelector('[data-sup]').onclick = () => mv(-1); w.querySelector('[data-sdown]').onclick = () => mv(1);
    w.querySelector('[data-sdel]').onclick = () => { if (st.repair && repairOpts(st).at > i) st.repair.at = repairOpts(st).at - 1; st.subjects.splice(i, 1); Object.keys(st.pins).forEach(k => { if (k.startsWith(s.id + '|')) delete st.pins[k]; }); savePlan(); c(); re(); toast(`Removed ${s.name}. Undo is on the Plan.`); };
    w.querySelector('[data-ssave]').onclick = () => { s.name = w.querySelector('[data-sname]').value.trim() || s.name; s.mode = mode === 'seq' ? 'seq' : 'daily'; s.daily = mode === 'fixed' ? (+w.querySelector('[data-sdaily]').value || 10) : null; s.to = mode === 'by' ? (w.querySelector('[data-sto]').value || null) : null; s.once = false; s.from = w.querySelector('[data-sfrom]').value || null; savePlan(); c(); re(); };
  });
}
// Quick add: a system (or all), a pool and walk counts → live count → subject
function addSubjectSheet(st, re, opt = {}) {
  const sys = systems();
  let sk = sys[0] ? sysNum(sys[0].name) : '', pool = 'hit', wk = '';
  const pick = () => { const g = sys.find(x => sysNum(x.name) === sk); return g ? g.decks.flatMap(d => cardsOf(d.deck)).filter(c => inPool(c, pool) && walkOk(c, wk)) : []; };
  const draw = w => {
    const list = pick(), nNew = list.filter(c => !seen(c.deck, c.no)).length;
    w.querySelector('[data-abody]').innerHTML = `<label class="pnew">System <select data-asys>${sys.map(g => `<option value="${sysNum(g.name)}"${sysNum(g.name) === sk ? ' selected' : ''}>${esc(g.label)}</option>`).join('')}</select></label>
      <div class="chips small">${[['all', 'All'], ['hit', 'Any hit'], ['neet', 'NEET'], ['neet+gt', 'NEET + GT']].map(([k, l]) => `<button class="chip${pool === k ? ' on' : ''}" data-apool="${k}">${l}</button>`).join('')}</div>
      <div class="chips small">${WALKS.map(([k, l]) => `<button class="chip${walkParts(wk).includes(k) ? ' on' : ''}" data-awalk="${k}">${walkParts(wk).includes(k) ? '✓ ' : ''}${l}</button>`).join('')}</div>
      <p class="acount"><b>${list.length}</b> cards · ${nNew} new · ${list.length - nNew} to revise${list.length && !cardsOf((sys.find(x => sysNum(x.name) === sk) || { decks: [] }).decks[0]?.deck || '').length ? ' <span class="muted small">(download the decks to count them all)</span>' : ''}</p>`;
    w.querySelector('[data-asys]').onchange = e => { sk = e.target.value; draw(w); };
    w.querySelectorAll('[data-apool]').forEach(b => b.onclick = () => { pool = b.dataset.apool; draw(w); });
    w.querySelectorAll('[data-awalk]').forEach(b => b.onclick = () => { wk = toggleWalk(wk, b.dataset.awalk); draw(w); });
  };
  planSheet(opt.once ? 'Add for today only' : 'Add a subject', opt.once ? 'THE PLAN · TODAY' : 'THE PLAN', `<div data-abody></div><div class="pnew">${opt.once ? '<p class="muted small">All of it goes on today. Whatever is not walked today shows under Doesn’t fit, and you can remove it.</p><input type="hidden" data-afrom value="">' : startSelect(st, '', 'data-afrom')}</div><div class="sheet-f"><button class="btn ghost" data-apick>Pick part of it in the Mosaic</button><button class="btn primary" data-aadd>Add to plan</button></div>`, (w, c) => {
    draw(w);
    w.querySelector('[data-apick]').onclick = () => { c(); if (opt.once) P.set('pickOnce', true); P.set('pickOn', true); P.set('pickForPlan', true); P.set('moPool', pool); P.set('moWalk', wk); go('#/sys/' + sk); };
    w.querySelector('[data-aadd]').onclick = () => {
      const list = pick(); if (!list.length) { toast('No cards match.'); return; }
      const g = sys.find(x => sysNum(x.name) === sk);
      const ns = addSubject(st, { name: g.label, sub: [poolName(pool), walkName(wk)].filter(x => x && x !== 'All').join(' · '), keys: list.map(c2 => c2.deck + '|' + c2.code), from: w.querySelector('[data-afrom]').value || null });
      if (opt.once) makeOnce(ns);
      c(); re();
    };
  });
}
const makeOnce = s => { s.once = true; s.mode = 'daily'; s.daily = null; s.from = today(); s.to = today(); savePlan(); };
function nameSubjectSheet(st, pend, re) {
  const once = !!P.get('pickOnce', false); P.set('pickOnce', false);
  planSheet('New subject', 'FROM THE MOSAIC', `<p class="muted small">${pend.keys.length} cards picked.</p><div class="pnew"><label>Name <input type="text" value="${esc(pend.name)}" data-nname></label>${startSelect(st, '', 'data-nfrom')}<label><input type="checkbox" data-nonce ${once ? 'checked' : ''}> Today only</label></div><div class="sheet-f"><button class="btn ghost" data-x>Cancel</button><button class="btn primary" data-nadd>Add to plan</button></div>`, (w, c) => {
    w.querySelector('[data-nadd]').onclick = () => { const ns = addSubject(st, { name: w.querySelector('[data-nname]').value.trim() || pend.name, sub: pend.sub, keys: pend.keys, from: w.querySelector('[data-nfrom]').value || null }); if (w.querySelector('[data-nonce]').checked) makeOnce(ns); c(); re(); };
  });
}
// Loft card: the plan at a glance
function planCard() {
  const st = currentStretch();
  if (!st) return `<a class="lcard plancard" href="#/plan"><span class="mono kick">THE PLAN</span><span class="pc-t">Plan your next days</span><span class="muted small">Split Phase 1 into stretches, choose subjects, and let Trace spread them at your pace.</span><span class="pc-go mono">Open the planner →</span></a>`;
  const r = compute(st), parts = todayParts(st, r), td = r.td;
  const verdict = r.over > 0 ? `<b class="behind">${r.over} cards don’t fit</b>` : r.raised ? `<b class="mid">fits at ${r.effPace} a day</b>` : `<b class="ahead">on track · ${r.spare} spare</b>`;
  return `<a class="lcard plancard" href="#/plan"><span class="mono kick">THE PLAN · ${esc(st.name.toUpperCase())} · ${dShort(r.days[0]).toUpperCase()} – ${dShort(r.days[r.days.length - 1]).toUpperCase()}</span>
    <span class="pc-t">${r.active ? `Today ${r.done[td] || 0} of ${r.todayPlan}` : td < r.days[0] ? `Starts ${dShort(r.days[0])}` : 'Stretch finished'} · ${verdict}</span>
    ${parts.length ? `<span class="pc-parts">${parts.map(x => `<span><i>${esc(x.name)}</i><b>${x.done}/${x.n}</b></span>`).join('')}</span>` : ''}
    <span class="pc-strip" aria-hidden="true">${r.days.map(d => `<i class="${d < td ? 'p' : d === td ? 't' : ''}${dayType(st, d) !== 'normal' ? ' x' : ''}" title="${d}"></i>`).join('')}</span>
    <span class="pc-go mono">Open the planner →</span></a>`;
}

/* ============================ Going out, breaks and "where were you?" (T-045) ============================ */
const curBreak = () => currentBreak();
const hmT = t => new Date(t).toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
function goingOutButton(cls = '') { return `<button class="btn ghost goout ${cls}" data-goout title="Going out (a break)" aria-label="Going out">⏏<span class="gol"> Going out</span></button>`; }
function bindGoingOut(root = app) { root.querySelectorAll('[data-goout]').forEach(b => b.onclick = e => { e.preventDefault(); goingOutSheet(); }); }
function reasonButtons(attr) {
  const h = new Date().getHours(), eveningOk = h >= 16 && h < 18 && !breaksOn(today()).some(b => b.reason === 'eveningtea');
  return REASONS.filter(r => r[0] !== 'other' || attr === 'data-away').map(([k, l, a, rem]) => {
    if (k === 'eveningtea' && !eveningOk && attr === 'data-go') return '';
    return `<button class="btn ghost rs" ${attr}="${k}"><b>${esc(l)}</b><small>${a ? a + ' min' : rem ? 'nudge at ' + rem + ' min' : 'counted'}</small></button>`;
  }).join('');
}
function goingOutSheet() {
  if (curBreak()) { toast('You are already on a break. Tap I’m back first.'); return; }
  const wrap = document.createElement('div'); wrap.className = 'modal';
  wrap.innerHTML = `<div class="sheet" role="dialog" aria-label="Going out"><div class="sheet-h"><span><span class="mono kick">GOING OUT</span><span class="sh-t">Where are you going?</span></span><button class="iconbtn" data-x aria-label="Close">${ICON.close}</button></div>
    <div class="rs-grid">${reasonButtons('data-go')}</div>
    <p class="muted small">The flow pauses while you are out. ${hasBackend() && !isDemo() ? 'Timed breaks set a reminder in your Google Calendar.' : ''} Opening Trace during the break doesn’t end it: tap I’m back.</p></div>`;
  wrap.onclick = e => { if (e.target === wrap || e.target.closest('[data-x]')) wrap.remove(); };
  wrap.querySelectorAll('[data-go]').forEach(b => b.onclick = async () => {
    wrap.remove();
    if (flow && !flow.browse) {
      // T-138: a pause already on is settled first, so the break clock and the pause clock never overwrite each other
      if (flow.userPause) { shiftClocks(Date.now() - flow.pausedAt); flow.userPause = false; const sc = $('.screen.flow'); if (sc) sc.classList.remove('paused'); const pb = $('#f-pause'); if (pb) pb.innerHTML = `${ICON.pause}<span class="lbl">Pause</span>`; }
      flow.pausedAt = Date.now(); if (vNow() && !vPaused()) vPause();
    }
    await startBreak(b.dataset.go); try { DAYP.onBreakStart(); } catch (e) { /* */ } drawBanner();
    const fd = document.querySelector('.f-due'); if (fd) fd.remove();
    toast(reasonOf(b.dataset.go)[1] + ': timer started.');
  });
  document.body.appendChild(wrap);
}
async function iamBack() {
  const rec = await endBreak(); if (!rec) return;
  if (flow && flow.pausedAt) { shiftClocks(Date.now() - flow.pausedAt); flow.pausedAt = null; flow.userPause = false; }
  drawBanner();
  const over = rec.allowed ? rec.end - rec.start - rec.allowed * 60000 : 0;
  toast(`Back after ${fmtHM((rec.end - rec.start) / 60000)}${over > 60000 ? ` (+${fmtHM(over / 60000)} over)` : ''}.`);
  if (!flow && /^#\/(loft|flow)/.test(location.hash)) route();
}
function drawBanner() {
  let el = document.getElementById('brk');
  const b = curBreak();
  if (!b) { if (el) el.remove(); return; }
  if (!el) { el = document.createElement('div'); el.id = 'brk'; el.className = 'brk'; document.body.appendChild(el); }
  const used = Date.now() - b.start, left = b.allowed ? b.allowed * 60000 - used : null;
  const t = left == null ? `${fmtHM(used / 60000)} so far` : left >= 0 ? `${Math.ceil(left / 60000)} min left` : `<b>+${Math.ceil(-left / 60000)} min over</b>`;
  el.className = 'brk' + (left != null && left < 0 ? ' over' : '');
  el.innerHTML = `<span>On ${esc(reasonOf(b.reason)[1].toLowerCase())} · ${t}</span><button class="pillbtn" data-back>I’m back</button>`;
  el.querySelector('[data-back]').onclick = iamBack;
}
function awayPrompt(start, end) {
  if (document.querySelector('.modal.away')) return;
  const wrap = document.createElement('div'); wrap.className = 'modal away';
  wrap.innerHTML = `<div class="sheet" role="dialog" aria-label="Where were you"><div class="sheet-h"><span><span class="mono kick">WELCOME BACK</span><span class="sh-t">Away ${fmtHM((end - start) / 60000)} (${hmT(start)}–${hmT(end)}). What was it?</span></span></div>
    <div class="rs-grid">${reasonButtons('data-away')}</div>
    <div class="sheet-f"><button class="btn ghost" data-still>Still away, just checking</button><button class="btn ghost" data-study>I was studying (off Trace)</button></div></div>`;
  const done = () => { wrap.remove(); setPendingAway(null); };
  wrap.querySelectorAll('[data-away]').forEach(b => b.onclick = () => { logAway(b.dataset.away, start, end); done(); if (/^#\/loft/.test(location.hash) && !flow) route(); });
  wrap.querySelector('[data-still]').onclick = () => { setPendingAway({ start }); wrap.remove(); };
  wrap.querySelector('[data-study]').onclick = done;
  document.body.appendChild(wrap);
}
function watchAway() {
  document.addEventListener('visibilitychange', () => {
    const now = Date.now();
    // T-072: always the latest leave time (a mark left behind when Chrome dropped the tab made the flow clock run
    // negative and asked "where were you?" on every switch)
    if (document.visibilityState === 'hidden') { markHidden(now); if (flow) flow.hidListen = !!(vNow() && !vPaused()); return; }
    const h = hiddenAt(); markHidden(null);
    if (!h || h > now) return;
    // T-138: a lesson playing with the screen off is study, not time away
    const listened = !!(flow && flow.hidListen); if (flow) flow.hidListen = false;
    if (flow && !flow.browse && !flow.pausedAt && !listened) {     // time away never counts as card time — but never more than this flow has run
      const away = now - Math.max(h, flow.wall0 || h, flow.cardWall || 0);
      if (away > 0) shiftClocks(away);
    }
    if (listened) return;
    if (curBreak()) { drawBanner(); return; }
    if (now - h < AWAY_MIN * 60000) return;                        // a quick switch to another app: nothing to ask
    let pend = pendingAway(); if (pend && now - pend.start > 12 * 3600e3) { setPendingAway(null); pend = null; }
    const start = pend ? pend.start : h, d = dkey(start);
    if (start < winEnd(d) && now > winStart(d)) awayPrompt(Math.max(start, winStart(d)), now);
  });
  { const h = hiddenAt(); if (h && Date.now() - h > 12 * 3600e3) markHidden(null); }   // a mark from a previous day: drop it
  setInterval(drawBanner, 15000);
  drawBanner();
}

function renderLoft() {
  const unit = P.get('heatUnit', 'h');
  const now = new Date();
  if (!loftMonth) loftMonth = { y: now.getFullYear(), m: now.getMonth() };
  if (!loftDay) loftDay = today();
  const { y, m } = loftMonth, first = new Date(y, m, 1, 12), days = new Date(y, m + 1, 0).getDate();
  const lead = (first.getDay() + 6) % 7;                      // Monday first, like the War Map
  const exam = CONFIG.exam.date, tdy = today();
  let cells = '';
  for (let i = 0; i < lead; i++) cells += '<span class="cd blank"></span>';
  for (let d = 1; d <= days; d++) {
    const k = y + '-' + String(m + 1).padStart(2, '0') + '-' + String(d).padStart(2, '0');
    const v = daily(k), val = unit === 'h' ? v.min / 60 : v.cards, has = unit === 'h' ? v.min >= 3 : v.cards > 0;
    const lvl = !has ? 0 : unit === 'h' ? Math.min(5, 1 + Math.floor(val)) : Math.min(5, 1 + Math.floor(val / 20));
    const txt = !has ? '' : unit === 'h' ? (Math.round(val * 10) / 10) + 'h' : String(v.cards);
    const mark = k === exam ? 'EX' : (S.gtDays[k] || '');
    cells += `<button class="cd l${lvl}${k === tdy ? ' today' : ''}${k === loftDay ? ' sel' : ''}${k > tdy ? ' future' : ''}" data-day="${k}" aria-label="${k}: ${fmtHM(v.min)}, ${v.cards} cards">
      <span class="cd-n">${d}</span>${mark ? `<span class="cd-m">${mark}</span>` : ''}<b>${txt}</b></button>`;
  }
  // the selected day, as in the War Map's "Day in the chronicle"
  const dv = daily(loftDay), dItems = buildChronicle().filter(c => c.day === loftDay);
  const dd = new Date(loftDay + 'T12:00');
  const dayCard = `<div class="dayc">
    <span class="mono kick">DAY IN THE CHRONICLE</span>
    <span class="dc-d">${['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'][dd.getDay()]} ${dd.getDate()} ${MONTHS[dd.getMonth()].slice(0, 3)}</span>
    <div class="dc-stats"><span><b>${fmtHM(dv.min)}</b><i>STUDIED</i></span><span><b>${dv.cards}</b><i>CARDS</i></span><span><b>${dv.cards ? (dv.min / dv.cards).toFixed(1) : '–'}</b><i>MIN / CARD</i></span></div>
    ${dItems.length ? `<div class="chron">${dItems.map(c => `<div class="ch-i"><span class="mono">${esc(c.when.replace(/^(Today|Yday) /, ''))}</span><span>${esc(c.what)}</span><span class="mono">${esc(c.size)}${c.key ? ` <button class="iconbtn sm ch-ed" data-chedit="${esc(c.key)}" aria-label="Edit this entry">${ICON.edit}</button>` : ''}</span></div>`).join('')}</div>` : '<p class="muted small">No study logged on this day.</p>'}
  </div>`;
  const chron = buildChronicle();
  app.innerHTML = `<div class="screen loft">
    <header class="top"><a class="iconbtn" href="#/" aria-label="Back to the palace">${ICON.back}</a>
      <span class="tt"><span class="mono kick">${daysLeft()} · ${CONFIG.exam.name} 11 DEC</span><span class="h1s">The Loft</span></span>${goingOutButton()}</header>
    <div class="scroll pad loftbody">
        ${CHANNEL === 'test' ? `<div class="peekbar${peekOn() ? ' on' : ''}"><span><b>${peekOn() ? 'PREVIEW · your peak week' : 'Preview your peak week'}</b><i>${peekOn() ? `${PEAK_LABEL}, laid onto the last 7 days. Study times are real (War Map Log); break reasons are assumed from the gaps. Calendar and Coverage stay real. Nothing is saved.` : `${PEAK_LABEL}: see the chase, cards per day and time charts filled with it.`}</i></span><button class="btn ghost" data-peek>${peekOn() ? 'Back to my data' : 'Show it'}</button></div>` : ''}
        ${planCard()}
      <div class="loft-grid">
        <div class="loft-main">
          ${chaseCard()}
          ${cardsDayCard()}
          ${timeCard()}
        </div>
        <div class="loft-side">
          ${targetBlock(false)}
          <div class="paper cal">
          <div class="cal-h"><button class="iconbtn sm" data-mo="-1" aria-label="Previous month">‹</button><span class="cal-t">${MONTHS[m]} ${y}</span><button class="iconbtn sm" data-mo="1" aria-label="Next month">›</button></div>
          <div class="cal-sw"><span class="seg light"><button class="${unit === 'h' ? 'on' : ''}" data-unit="h">Hours</button><button class="${unit === 'c' ? 'on' : ''}" data-unit="c">Cards</button></span></div>
          <div class="cal-g"><span class="cw">M</span><span class="cw">T</span><span class="cw">W</span><span class="cw">T</span><span class="cw">F</span><span class="cw">S</span><span class="cw">S</span>${cells}</div>
          <div class="pp-f mono"><span>GT = grand test · EX = exam</span><span class="hk">less${HEAT.slice(1).map(c => `<i style="background:${c}"></i>`).join('')}more ${unit === 'h' ? 'hours' : 'cards'}</span></div>
        </div>
          ${dayCard}
          ${coverCard()}
          ${tilesRow(chron.length)}
          <details class="chrond${P.get('chronOpen', false) ? '' : ' hid'}"${P.get('chronOpen', false) ? ' open' : ''}><summary><span class="mono kick">CHRONICLES</span><span class="mono muted small">${chron.length} entries</span></summary>
          <div class="chron">${chron.slice(0, 80).map(c => `<div class="ch-i"><span class="mono">${esc(c.when)}</span><span>${esc(c.what)}</span><span class="mono">${esc(c.size)}${c.key ? ` <button class="iconbtn sm ch-ed" data-chedit="${esc(c.key)}" aria-label="Edit this entry">${ICON.edit}</button>` : ''}</span></div>`).join('') || '<p class="muted small">Nothing yet.</p>'}</div>
        </details>
        </div>
      </div>
    </div>
    ${nav('')}
  </div>`;
  bindGo(); bindTarget(renderLoft); bindLoftParts(); bindGoingOut();
  app.querySelectorAll('[data-chedit]').forEach(b => b.onclick = e => { e.preventDefault(); e.stopPropagation(); editEntrySheet(b.dataset.chedit); });
  const pkb = app.querySelector('[data-peek]'); if (pkb) pkb.onclick = () => { setPeek(!peekOn()); keep(renderLoft); };
  lastMeditation().then(m => { const el = app.querySelector('#al-last'); if (m && el && TRACKS[m.track]) el.textContent = `Last: ${TRACKS[m.track].title} · ${whenLabel(m.ts)} · ${Math.max(1, Math.round(m.sec / 60))} min`; });
  app.querySelectorAll('[data-unit]').forEach(b => b.onclick = () => { P.set('heatUnit', b.dataset.unit); keep(renderLoft); });
  app.querySelectorAll('[data-cov]').forEach(b => b.onclick = () => { P.set('covPool', b.dataset.cov); keep(renderLoft); });
  app.querySelectorAll('[data-mo]').forEach(b => b.onclick = () => { let mm = loftMonth.m + +b.dataset.mo, yy = loftMonth.y; if (mm < 0) { mm = 11; yy--; } if (mm > 11) { mm = 0; yy++; } loftMonth = { y: yy, m: mm }; keep(renderLoft); });
  app.querySelectorAll('[data-day]').forEach(b => b.onclick = () => { loftDay = b.dataset.day; keep(renderLoft); });
  const cd = app.querySelector('details.chrond'); if (cd) cd.addEventListener('toggle', () => P.set('chronOpen', cd.open));
}
// Edit a Flow entry: remove single cards or the whole entry (an undo, as Undo in Flow does; synced to the Sheet's TraceEvents)
function editEntrySheet(key) {
  const evs = S.events.filter(e => e.kind === 'view' && !S.undone.has(e.id) && (e.session || e.id) === key).sort((a, b) => a.ts - b.ts);
  if (!evs.length) return;
  const hm = t => new Date(t).toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
  planSheet('Flow entry · ' + whenLabel(evs[0].ts), 'EDIT', `<p class="muted small">Remove a card that got walked by mistake, or the whole entry. Removed cards count as never walked in this entry.</p>
    <div class="ed-list">${evs.map(e => `<div class="ed-i"><span class="mono">${hm(e.ts)}</span><span><b>${esc(e.deck)}</b> ${esc(e.code || '')} · card ${e.no}${e.again ? ' · Again' : ''}</span><button class="btn ghost" data-edrm="${esc(e.id)}">Remove</button></div>`).join('')}</div>
    <div class="sheet-f"><button class="btn ghost" data-x>Keep all</button><button class="btn primary" data-edall>Remove whole entry (${evs.length})</button></div>`, (w, c) => {
    const done = async list => { for (const e of list) await undoView(e); c(); toast(list.length === 1 ? 'Card removed.' : list.length + ' cards removed.'); keep(renderLoft); if (hasBackend()) sync({ downloadAll: false }); };
    w.querySelectorAll('[data-edrm]').forEach(b => b.onclick = () => done(evs.filter(e => e.id === b.dataset.edrm)));
    w.querySelector('[data-edall]').onclick = () => done(evs);
  });
}
function buildChronicle() {
  const items = [];
  // Trace sessions: group views by session
  const by = new Map();
  for (const e of S.events) {
    if (S.undone.has(e.id) || e.kind !== 'view') continue;
    const k = e.session || e.id;
    const s = by.get(k) || { key: k, ts: e.ts, end: e.ts, decks: new Map(), ms: 0, n: 0 };
    s.ts = Math.min(s.ts, e.ts); s.end = Math.max(s.end, e.ts); s.ms += Math.min(e.ms || 0, 20 * 60000); s.n++;
    const d = s.decks.get(e.deck) || []; d.push(e.no); s.decks.set(e.deck, d);
    by.set(k, s);
  }
  for (const s of by.values()) {
    const parts = [...s.decks.entries()].map(([d, nos]) => d + ' ' + compressNos(nos));
    items.push({ key: s.key, ts: s.ts, day: dkey(s.ts), when: whenLabel(s.ts), what: 'Flow · ' + parts.slice(0, 2).join(', ') + (parts.length > 2 ? ` +${parts.length - 2}` : ''), size: `${s.n} · ${fmtHM(s.ms / 60000)}` });
  }
  for (const r of S.logChron) {
    const ts = new Date(r[0] + 'T' + (/^\d{1,2}:\d{2}/.test(r[1]) ? r[1].padStart(5, '0') : '12:00')).getTime();
    items.push({ ts, day: r[0], when: whenLabel(ts), what: 'War Map · ' + r[2] + ' ' + r[3] + (r[4] !== r[3] ? '–' + r[4] : ''), size: `${r[5]} · ${fmtHM(r[6])}` });
  }
  return items.sort((a, b) => b.ts - a.ts);
}
function whenLabel(ts) {
  const d = new Date(ts), k = dkey(ts), t = today();
  const y = new Date(); y.setDate(y.getDate() - 1);
  const hmS = String(d.getHours()).padStart(2, '0') + ':' + String(d.getMinutes()).padStart(2, '0');
  if (k === t) return 'Today ' + hmS;
  if (k === dkey(y.getTime())) return 'Yday ' + hmS;
  return d.getDate() + ' ' + ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][d.getMonth()] + ' ' + hmS;
}

/* ============================ flow ============================ */
let flow = null;
/** list: cards (may span decks). opts: { start, label, browse, returnTo } */
function startFlow(list, opts = {}) {
  if (!list || !list.length) return;
  const at = Math.max(0, opts.start || 0);
  const queue = list.slice(at).concat(list.slice(0, at));
  flow = { deck: queue[0].deck, label: opts.label || '', viva: opts.viva || '', vauto: !!opts.viva && vAuto(), vqSeen: {}, browse: !!opts.browse, pilot: !!opts.pilot, pilotSent: false, returnTo: opts.returnTo || '#/deck/' + encodeURIComponent(queue[0].deck),
    queue, idx: 0, face: 'q', session: uid('s'), t0: Date.now(), wall0: Date.now(), cardT0: Date.now(), times: [], hist: [], busy: false, done: false, trail: [], look: 0, qms: {} };
  _lastDeck = queue[0].deck;
  renderFlow();
  if (flow.viva) vivaMarks().then(m => { if (flow) { flow.vm = m; drawThread(); } });
  flow.tick = setInterval(updateClock, 1000);
  document.addEventListener('keydown', flowKeys);
}
// Leaving a flow always asks: save the cards walked, discard them, or keep going (Naven, 3 Nov).
function walkedNow() { return flow ? flow.hist.filter(h => h.ev).length : 0; }
function askEnd(discardOnly) {
  if (!flow) return;
  if (flow.browse || flow.pilot || !walkedNow()) return endFlow();
  const n = walkedNow(), tot = (Date.now() - flow.t0) / 1000;
  const wrap = document.createElement('div'); wrap.className = 'modal endask';
  wrap.innerHTML = `<div class="sheet" role="dialog" aria-label="End this flow">
    <div class="sheet-h"><span><span class="mono kick">${flow.done ? 'FLOW COMPLETE' : 'LEAVING THE FLOW'}</span><span class="sh-t">${discardOnly ? 'Discard this flow?' : 'Save this flow?'}</span></span></div>
    <p>You walked <b>${n}</b> card${n === 1 ? '' : 's'} in ${clock(tot)}.${flow.done ? '' : ` ${flow.queue.length - flow.idx} left; a saved flow waits under Continue on the Flow tab.`}</p>
    <div class="sheet-f end-btns">
      ${discardOnly ? '' : '<button class="big press" data-save>SAVE</button>'}
      <button class="btn ghost" data-drop>Discard ${n} card${n === 1 ? '' : 's'}</button>
      <button class="btn ghost" data-stay>${flow.done ? 'Back' : 'Keep going'}</button>
    </div></div>`;
  const close = () => wrap.remove();
  wrap.onclick = e => { if (e.target === wrap) close(); };
  const sv = wrap.querySelector('[data-save]'); if (sv) sv.onclick = () => { close(); endFlow(); };
  wrap.querySelector('[data-stay]').onclick = close;
  wrap.querySelector('[data-drop]').onclick = async () => { close(); await discardFlow(); };
  document.body.appendChild(wrap);
}
async function discardFlow() {
  if (!flow) return;
  for (const h of [...flow.hist].reverse()) if (h.ev) await undoView(h.ev);
  flow.hist = []; flow.times = [];
  P.set(LASTFLOW, null);
  toast('Flow discarded. Nothing from it counts.');
  await endFlow();
}
async function endFlow() {
  if (!flow) return;
  clearInterval(flow.tick);
  document.removeEventListener('keydown', flowKeys);
  unmountInk(); vStop();
  closePanel(); releaseUrls();
  if (flow.pilot) stopPolling();
  const sid = flow.session, back = flow.returnTo, browse = flow.browse;
  flow = null;
  if (!browse) { await buildLogRows(sid); await countPending(); }
  if (location.hash === back) route(); else go(back);
  if (!browse && hasBackend()) sync({ downloadAll: false });
}
function current() { return flow.peek ? flow.queue[flow.hist[flow.hist.length - flow.peek].idx] : flow.queue[flow.idx]; }
/* ---------- T-138: the steps of a viva walk ----------
   Every question is opening lesson → its cards → closing lesson → spine. Each is a step: it has a tile, its own time,
   and Back walks through all of them (looking only: nothing is undone or logged again). flow.trail = the steps reached,
   in order; flow.look = how many steps back from now you are looking; flow.st = the step being timed now. */
function shiftClocks(d) { if (!flow || !(d > 0)) return; flow.cardT0 += d; flow.t0 += d; if (flow.peekT0) flow.peekT0 += d; if (flow.st) flow.st.t0 += d; if (flow.lookT0) flow.lookT0 += d; if (flow.vt0) flow.vt0 += d; }
const stepKey = s => s ? s.kind + ':' + s.idx : '';
function liveStep() {
  if (!flow || flow.done) return null;
  const it = flow.inter;
  if (it) return it.kind === 'vq' ? { kind: 'vq', idx: it.at, pkg: it.pkg, q: it.q } : (it.kind === 'vclose' || it.kind === 'spine') ? { kind: it.kind, idx: it.idx, pkg: it.pkg, q: it.q } : null;
  const c = flow.queue[flow.idx]; return c ? { kind: 'card', idx: flow.idx, pkg: c.vq && c.vq.pkg, q: c.vq && c.vq.q } : null;
}
function closeStep() {
  const st = flow && flow.st; if (!st) return;
  flow.st = null;
  const ms = Math.max(0, Math.min(30 * 60e3, (flow.pausedAt || Date.now()) - st.t0));
  if (st.s.q) { const k = st.s.pkg + '|' + st.s.q; flow.qms[k] = (flow.qms[k] || 0) + ms; addQTime(st.s.pkg, st.s.q, flow.session, ms, st.s.kind); }
}
function noteStep() {
  if (!flow || !flow.viva || flow.browse || flow.look || flow.peek) return;
  const s = liveStep(), k = stepKey(s);
  if (flow.st && flow.st.k === k) return;
  closeStep();
  if (!s) return;
  const tr = flow.trail; if (!tr.length || stepKey(tr[tr.length - 1]) !== k) tr.push(s);
  flow.st = { k, s, t0: flow.pausedAt || Date.now() };
  if (s.kind === 'vq' && tr.length > 1) setTimeout(checkBreakDue, 400);     // T-141: between questions, never inside one
  // reaching the spine finishes the question for the plan (once per walk)
  if (s.kind === 'spine' && s.q) { flow.vdone = flow.vdone || {}; const dk = s.pkg + '|' + s.q; if (!flow.vdone[dk]) { flow.vdone[dk] = 1; markVivaDone(s.pkg, s.q); } }
}
// where "now" sits in the trail: on the last step, or just past it once the walk is finished
const liveAt = () => { const tr = flow.trail, s = liveStep(); return s && tr.length && stepKey(tr[tr.length - 1]) === stepKey(s) ? tr.length - 1 : tr.length; };
function lookSet(look) {
  if (!flow) return;
  const was = flow.look || 0, now = Date.now();
  if (was && flow.lookT0 && flow.lookStep && flow.lookStep.q) {          // time spent looking back belongs to the question looked at
    const ms = Math.max(0, Math.min(30 * 60e3, (flow.pausedAt || now) - flow.lookT0)), k = flow.lookStep.pkg + '|' + flow.lookStep.q;
    flow.qms[k] = (flow.qms[k] || 0) + ms; addQTime(flow.lookStep.pkg, flow.lookStep.q, flow.session, ms, flow.lookStep.kind);
  }
  if (!was && look) { closeStep(); flow.lookFrom = now; }
  vStop();
  flow.look = look; flow.lookInter = null; flow.peek = 0;
  if (!look) {
    if (flow.lookFrom) flow.cardT0 += now - flow.lookFrom;        // looking back is not card time
    flow.lookFrom = null; flow.lookT0 = null; flow.lookStep = null;
    return;
  }
  const s = flow.trail[liveAt() - look]; flow.lookStep = s; flow.lookT0 = now;
  if (s.kind === 'card') { let k = -1; for (let j = flow.hist.length - 1; j >= 0; j--) if (flow.hist[j].idx === s.idx) { k = j; break; } if (k >= 0) flow.peek = flow.hist.length - k; else flow.lookInter = null; }
  else flow.lookInter = { kind: s.kind, pkg: s.pkg, q: s.q, at: s.idx, idx: s.idx, look: true };
}
function lookBack() {
  if (!flow || flow.busy || flow.pausedAt) return;
  const at = liveAt(), want = (flow.look || 0) + 1;
  if (at - want < 0) { toast(flow.trail.length > 1 ? 'That is the first step of this walk.' : 'No earlier step in this walk yet.'); return; }
  lookSet(want);
  animate('back', () => { drawCard(); updateFlowChrome(); });
}
function lookForward(all) {
  if (!flow || !flow.look || flow.busy) return;
  lookSet(all ? 0 : flow.look - 1);
  animate('deal', () => { drawCard(); updateFlowChrome(); });
}
function lookToKey(k) {
  if (!flow || flow.busy || flow.pausedAt) return;
  const at = liveAt(), j = flow.trail.findIndex(s => stepKey(s) === k);
  if (j < 0) { toast('That step is still ahead in this walk.'); return; }
  const want = Math.max(0, at - j); if (want === (flow.look || 0)) return;
  const back = want > (flow.look || 0); lookSet(want);
  animate(back ? 'back' : 'deal', () => { drawCard(); updateFlowChrome(); });
}
const backToNow = () => flow.look ? lookForward(true) : peekForward(true);
// every step of the walk, in order, for the tiles: O = opening lesson, cards, C = closing lesson, S = spine
function vivaSteps() {
  const out = [];
  flow.queue.forEach((c, i) => {
    const v = c.vq; if (!v) { out.push({ kind: 'card', idx: i }); return; }
    if (v.i === 0 && !v.again) out.push({ kind: 'vq', idx: i, pkg: v.pkg, q: v.q });
    out.push({ kind: 'card', idx: i, pkg: v.pkg, q: v.q, n: v.i + 1, rep: !!v.rep, again: !!v.again });
    if (!v.again && v.i === v.n - 1) { if (lessonOf(v.pkg, v.q, 'c')) out.push({ kind: 'vclose', idx: i, pkg: v.pkg, q: v.q }); out.push({ kind: 'spine', idx: i, pkg: v.pkg, q: v.q }); }
  });
  return out;
}
const qNumOf = (pkg, q) => { const P2 = vivaPkg(pkg); return P2 ? P2.questions.findIndex(x => x.q === q) + 1 : 0; };
/* Back = look at cards already walked in this flow; nothing is logged or changed, and the time spent looking back is not
   counted as card time. Pause stops the clock and covers the card. (T-070, Naven's notes 5 Nov) */
// the left bottom button (T-078): question side → look at the card before; answer side → back to this card's question;
// looking back → one card further back; browse → previous card
function leftAction() {
  if (!flow || flow.busy || flow.userPause || (flow.done && !flow.inter && !flow.viva)) return;
  // T-138: in a viva walk, Back looks at the step before (lessons and spine included); the answer side goes to its question first
  if (flow.viva && !flow.browse) {
    if (!flow.look && !flow.inter && !flow.done && flow.face === 'a') { animate('flip', () => { flow.face = 'q'; drawCard(); }); return; }
    lookBack(); return;
  }
  // T-129: Back from a viva lesson or spine card (Naven, 11 Nov): closing lesson and opening lesson → the card before;
  // spine → its closing lesson
  if (flow.inter) {
    const it = flow.inter;
    if (it.kind === 'spine' && lessonOf(it.pkg, it.q, 'c')) { vStop(); flow.inter = { kind: 'vclose', pkg: it.pkg, q: it.q }; animate('back', () => { drawCard(); updateFlowChrome(); }); return; }
    if ((it.kind === 'vclose' || it.kind === 'vq' || it.kind === 'spine') && flow.hist.length) { vStop(); if (it.kind === 'vq' && flow.vqSeen) delete flow.vqSeen[it.at]; undo(); return; }
    clearInter(); return;
  }
  if (flow.browse) { undo(); return; }
  if (flow.peek) { peekBack(); return; }
  if (flow.face === 'a') { animate('flip', () => { flow.face = 'q'; drawCard(); }); return; }
  peekBack();
}
function leftLabel() {
  if (!flow) return '';
  if (flow.viva && !flow.browse) {
    if (!flow.look && !flow.inter && !flow.done && flow.face === 'a') return `${ICON.prev}<span>Question</span>`;
    return liveAt() - (flow.look || 0) > 0 ? `${ICON.prev}<span>${flow.look ? 'Further back' : 'Back'}</span>` : '';
  }
  if (flow.inter) {
    const it = flow.inter;
    if (it.kind === 'spine' && lessonOf(it.pkg, it.q, 'c')) return `${ICON.prev}<span>Lesson</span>`;
    if ((it.kind === 'vclose' || it.kind === 'vq' || it.kind === 'spine') && flow.hist.length) return `${ICON.prev}<span>Back</span>`;
    return '';
  }
  if (flow.done) return '';
  if (flow.browse) return `${ICON.prev}<span>Back</span>`;
  if (flow.peek) return `${ICON.prev}<span>Further back</span>`;
  return flow.face === 'a' ? `${ICON.prev}<span>Question</span>` : `${ICON.prev}<span>Back</span>`;
}
function peekBack() {
  if (flow && flow.viva && !flow.browse) return lookBack();
  if (!flow || flow.browse || flow.busy || flow.pausedAt) return;
  if (flow.inter) flow.inter = null;
  if (!flow.hist.length || (flow.peek || 0) >= flow.hist.length) { toast(flow.hist.length ? 'That is the first card of this flow.' : 'No earlier card in this flow yet.'); return; }
  if (!flow.peek) flow.peekT0 = Date.now();
  flow.peek = (flow.peek || 0) + 1;
  animate('back', () => { drawCard(); updateFlowChrome(); });
}
// tap a tile: a walked card opens to look at (nothing changes); the current one brings you back
function jumpTo(i) {
  if (!flow || flow.busy || flow.pausedAt) return;
  if (i === flow.idx) { if (flow.peek) peekForward(true); return; }
  let k = -1; for (let j = flow.hist.length - 1; j >= 0; j--) if (flow.hist[j].idx === i) { k = j; break; }
  if (k < 0) { toast(i > flow.idx ? 'That card is still ahead in this flow.' : 'That card was undone.'); return; }
  const want = flow.hist.length - k; if (want === flow.peek) return;
  if (!flow.peek) flow.peekT0 = Date.now();
  const back = want > (flow.peek || 0); flow.peek = want;
  animate(back ? 'back' : 'deal', () => { drawCard(); updateFlowChrome(); });
}
function peekForward(all) {
  if (flow && flow.look) return lookForward(all);
  if (!flow || !flow.peek) return;
  flow.peek = all ? 0 : flow.peek - 1;
  if (!flow.peek) { const d = Date.now() - (flow.peekT0 || Date.now()); flow.cardT0 += d; flow.peekT0 = null; }
  animate('deal', () => { drawCard(); updateFlowChrome(); });
}
function togglePause() {
  if (!flow || flow.browse) return;
  if (flow.pausedAt && !flow.userPause) { toast('You are on a break — tap I’m back.'); return; }
  if (flow.userPause) { shiftClocks(Date.now() - flow.pausedAt); flow.pausedAt = null; flow.userPause = false; if (vNow() && vPaused()) vResume(); }
  else { flow.pausedAt = Date.now(); flow.userPause = true; if (vNow() && !vPaused()) vPause(); }   // T-138: pause stops the lesson voice too
  const b = $('#f-pause'); if (b) b.innerHTML = flow.userPause ? `${ICON.play}<span class="lbl">Resume</span>` : `${ICON.pause}<span class="lbl">Pause</span>`;
  $('.screen.flow').classList.toggle('paused', !!flow.userPause);
  updateClock(); DESK.pushDesk(true);
}
function sectionRange() {
  const c = current(); if (!c) return '';
  const ch = chunkOf(c), same = flow.queue.filter(x => x.deck === c.deck && chunkOf(x).key === ch.key).map(x => x.no);
  return ch.name + (same.length > 1 ? ' · cards ' + Math.min(...same) + '–' + Math.max(...same) : same.length ? ' · card ' + same[0] : '');
}

function renderFlow() {
  const m = deckMeta(flow.deck) || {};
  const cs = P.get('cardScale', 1);
  // T-072 layout: one slim bar + one strip; the card and Explain get the rest of the screen
  app.innerHTML = `<div class="screen flow v3${flow.browse ? ' browse' : ''}" data-page="${esc(P.get('page', 'white'))}" style="--cs:${cs}">
    <header class="f-bar">
      <button class="iconbtn sm" data-act="close" aria-label="End flow">${ICON.close}</button>
      <div class="f-title"><span class="mono kick" id="f-kick"></span><span class="f-sec" id="f-sec"></span><span class="f-sub muted" id="f-sub">${esc(m.title || '')}</span></div>
      <span class="ring" id="f-ring"></span>
      <div class="f-stats mono"><span><i>${flow.viva ? 'SESSION' : 'TIME'}</i><b id="f-time">0:00</b></span>${flow.viva ? '<span class="f-qs"><i id="f-ql">QUESTION</i><b id="f-qt">0:00</b></span><span><i id="f-stl">CARD</i><b id="f-stp">0:00</b></span>' : ''}<span><i>PER CARD</i><b id="f-pace">–</b></span><span><i>VS AVG</i><b id="f-diff">–</b></span></div>
      <span class="f-day mono" id="f-day"></span>
      <span class="f-grow"></span>
      <button class="iconbtn" data-act="undo" aria-label="${flow.browse ? 'Previous card' : 'Undo last card'}" title="${flow.browse ? 'Previous card' : 'Undo the last card'}" id="f-undo">${flow.browse ? ICON.prev : ICON.undo}<span class="lbl">${flow.browse ? 'Back' : 'Undo'}</span></button>
      ${flow.browse ? '' : `<button class="iconbtn" data-act="pause" aria-label="Pause the flow" title="Pause (P)" id="f-pause">${ICON.pause}<span class="lbl">Pause</span></button>`}
      ${flow.browse ? '' : goingOutButton('sm')}
      ${P.get('inkDock', 1) ? '<div class="ik-host ik-dock" id="f-ink" hidden></div>' : ''}
      <span class="f-break" aria-hidden="true"></span>
      <button class="iconbtn sm" id="f-gear" aria-label="Explain settings" aria-expanded="false">⚙</button>
      <div class="f-pop" id="f-pop" hidden><div class="f-xp" id="f-xp"></div><p class="f-note muted small">${flow.browse ? 'Looking only: nothing is timed or logged. Space reveals and moves on · ← back · E = Edit · Esc closes.' : 'Space reveals and moves on · ← looks back · P pauses · A = Again · U = Undo · E = Edit · Esc ends.'}</p></div>
    </header>
    <div class="f-strip" id="f-strip" role="button" tabindex="0" aria-label="This flow and today: tap for the full view">
      <span class="mono f-sl" id="f-lab">THIS FLOW</span><span class="mono f-cnt" id="f-cnt"></span><div class="f-tiles" id="f-tiles"></div>
      ${flow.browse ? '' : '<div class="thread" id="f-thread" aria-live="polite"></div><div class="f-live mono" id="f-live"></div>'}
    </div>
    <main class="f-main">
      ${P.get('inkDock', 1) ? '' : '<div class="ik-host" id="f-ink" hidden></div>'}
      <div class="card-wrap"><article class="card" id="card"></article>${flow.browse ? '' : '<button class="pause-cover" id="f-cover" aria-label="Resume the flow"><span class="mono">PAUSED</span><b>Tap to resume</b><small>The clock is stopped.</small></button>'}</div>
      ${flow.pilot ? '<div class="fm-slot" id="fm-slot" aria-live="polite"></div>' : ''}
      <div class="f-nav"><button class="big2 press" id="f-left"></button><button class="big press" id="f-big"></button></div>
    </main>
  </div>`;
  setupGestures($('.card-wrap'));
  const ikh = $('#f-ink.ik-dock'); if (ikh && window.ResizeObserver) { let t = 0; new ResizeObserver(() => { clearTimeout(t); t = setTimeout(fitBar, 60); }).observe(ikh); }
  const gear = $('#f-gear'), pop = $('#f-pop');
  gear.onclick = e => { e.stopPropagation(); pop.hidden = !pop.hidden; gear.setAttribute('aria-expanded', !pop.hidden); };
  if (!window.__fpop) window.__fpop = 1, document.addEventListener('pointerdown', e => { const pp = document.getElementById('f-pop'); if (pp && !pp.hidden && !e.target.closest('#f-pop, #f-gear')) pp.hidden = true; }, { capture: true });
  const strip = $('#f-strip'); strip.onclick = e => {
    if (e.target.closest('button, a')) return;
    const sk = e.target.closest('[data-sk]');
    if (sk && !flow.browse) { if (sk.classList.contains('cur') && !flow.look) return; if (sk.classList.contains('cur')) { lookForward(true); return; } lookToKey(sk.dataset.sk); return; }
    const t = e.target.closest('[data-ti]');
    if (t && !flow.browse) { const i = +t.dataset.ti; jumpTo(i); return; }
    strip.classList.toggle('open');
  };
  $('[data-act=close]').onclick = () => askEnd();
  app.querySelectorAll('[data-ts]').forEach(b => b.onclick = () => {
    const v = Math.max(0.8, Math.min(1.5, Math.round((P.get('cardScale', 1) + 0.1 * +b.dataset.ts) * 10) / 10));
    P.set('cardScale', v); $('.screen.flow').style.setProperty('--cs', v);
  });
  $('#f-undo').onclick = undo;
  const pk = $('#f-peek'); if (pk) pk.onclick = peekBack;
  const ps = $('#f-pause'); if (ps) ps.onclick = togglePause;
  bindGoingOut();
  $('#f-left').onclick = leftAction;
  $('#f-big').onclick = () => flow.userPause ? togglePause() : flow.pausedAt ? toast('You are on a break — tap I’m back.') : (flow.look || flow.peek) ? backToNow() : flow.inter ? clearInter() : flow.done ? endFlow() : (flow.face === 'q' ? reveal() : next(false));
  const cv = $('#f-cover'); if (cv) cv.onclick = togglePause;
  drawXpToggles();
  drawCard();
  updateFlowChrome();
}
/* ---------- Explain layer in Flow (T-069): toggles, deck map / deck close interstitials ---------- */
const xpOpenMode = () => P.get('xpOpen', 'new');          // 'new' = open on a card's first sight · 'tap' = only when tapped
const xpTraps = () => !!P.get('xpTraps', 1);
const xpDepth = () => P.get('xpDepth', 'auto');   // 'auto' = Learn on a card's first sight, Revise after · or always one of them
const PAGES = [['white', 'White'], ['grey', 'Soft grey'], ['cream', 'Cream'], ['mint', 'Mint']];
function drawXpToggles() {
  const h = document.getElementById('f-xp'); if (!h) return;
  const o = xpOpenMode(), t = xpTraps();
  const wasOpen = true;   // T-072: the settings live in the ⚙ pop-up, always unfolded there
  h.innerHTML = `<details class="f-xpd"${wasOpen ? ' open' : ''}><summary class="mono">EXPLAIN SETTINGS</summary><div class="f-xpg"><span class="mono muted small">EXPLAIN</span>
    <div class="seg"><button class="${o !== 'tap' ? 'on' : ''}" data-xo="new">Open</button><button class="${o === 'tap' ? 'on' : ''}" data-xo="tap">Only when tapped</button></div>
    <span class="mono muted small">DEPTH</span>
    <div class="seg">${[['auto', 'Auto'], ['learn', 'Learn'], ['revise', 'Revise']].map(([k, l]) => `<button class="${xpDepth() === k ? 'on' : ''}" data-xd="${k}">${l}</button>`).join('')}</div>
    <span class="mono muted small">EXAM TRAPS</span>
    <div class="seg"><button class="${t ? 'on' : ''}" data-xt="1">Show</button><button class="${!t ? 'on' : ''}" data-xt="0">Hide</button></div>
    <span class="mono muted small">PAGE</span>
    <div class="seg">${PAGES.map(([k2, l]) => `<button class="${P.get('page', 'white') === k2 ? 'on' : ''}" data-pg="${k2}"><i class="pgsw pg-${k2}"></i>${l}</button>`).join('')}</div>
    <span class="mono muted small">PEN TOOLS</span>
    <div class="seg"><button class="${P.get('inkDock', 1) ? 'on' : ''}" data-nv="inkDock:1">In the top bar</button><button class="${!P.get('inkDock', 1) ? 'on' : ''}" data-nv="inkDock:0">Floating</button></div></div></details>${chatSettingsHtml()}`;
  bindChatSettings(h);
  h.querySelectorAll('[data-nv]').forEach(b => b.onclick = () => {
    const [k, v] = b.dataset.nv.split(':'); P.set(k, +v);
    if (k === 'inkDock' && flow) { renderFlow(); const p2 = $('#f-pop'); if (p2) p2.hidden = false; return; }
    drawXpToggles();
  });
  h.querySelectorAll('[data-pg]').forEach(b => b.onclick = () => { P.set('page', b.dataset.pg); const sc = $('.screen.flow'); if (sc) sc.dataset.page = b.dataset.pg; drawXpToggles(); });
  h.querySelectorAll('[data-xo]').forEach(b => b.onclick = () => { P.set('xpOpen', b.dataset.xo); drawXpToggles(); if (flow && flow.face === 'a' && !flow.inter) drawCard(); });
  h.querySelectorAll('[data-xd]').forEach(b => b.onclick = () => { P.set('xpDepth', b.dataset.xd); if (flow) flow.depthOver = {}; drawXpToggles(); if (flow && flow.face === 'a' && !flow.inter) drawCard(); });
  h.querySelectorAll('[data-xt]').forEach(b => b.onclick = () => { P.set('xpTraps', +b.dataset.xt); drawXpToggles(); if (flow && flow.face === 'a' && !flow.inter) drawCard(); });
}
function clearInter() {
  if (!flow || !flow.inter || flow.pausedAt) return;
  vStop();
  if (flow.inter.kind === 'vclose') { const it = flow.inter; flow.inter = { kind: 'spine', pkg: it.pkg, q: it.q, idx: it.idx }; animate('deal', () => { drawCard(); updateFlowChrome(); }); return; }
  flow.inter = null;
  flow.cardT0 = Date.now();                        // T-138: a lesson's time is the lesson's, not the next card's
  animate('deal', () => { drawCard(); updateFlowChrome(); });
}
function drawInter(el, big, it = flow.inter) {
  const deck = it.deck, m = deckMeta(deck) || {};
  unmountInk();
  const walking = new Set(flow.queue.filter(x => x.deck === deck).map(x => x.code));
  el.classList.remove('ng');
  if (it.kind === 'vq' || it.kind === 'spine' || it.kind === 'vclose') return drawVivaInter(el, big, it);
  el.innerHTML = it.kind === 'map' ? mapHtml(deck, m.title, walking) : closeHtml(deck);
  big.innerHTML = it.kind === 'map' ? `START${ICON.next}` : `CONTINUE${ICON.next}`;
  bindBridges(el);
}
// T-129: opening and closing lessons sit in a card face of their own, so the size slider, Fit, the pen, the highlighter
// and Select text work on them as on any card; their ink is kept under VIVA-<pkg> | <question>-open / -close
const viLessonFrame = body => `<div class="c-tags vi-tags"></div><div class="c-q vi-lesson"><div class="zw">${body}</div></div>`;
function viLessonTools(el, it, slot) {
  const pc = { deck: 'VIVA-' + it.pkg, code: it.q + '-' + slot, section: 'Viva lesson' };
  setupFit(el);
  mountInk(el, pc, 'q', inkOpts(pc));
}
// T-138: turning Autoplay on starts the lesson straight away (also when looking back at an earlier lesson)
function autoKick(el) { if (!flow || !flow.vauto) return; const pp = el.querySelector('[data-lpp]'); if (pp && pp.textContent.trim() === '▶') pp.click(); }
function viLeft() { const lb = $('#f-left'); if (lb) { lb.innerHTML = leftLabel(); lb.classList.toggle('dimmed', !leftLabel()); } }
// T-095: the viva question card (before its steps) and the spine card (after them)
function drawVivaInter(el, big, it) {
  if (it.kind === 'vq') {
    const steps = flow.queue.filter((x, j) => j >= it.at && x.vq && x.vq.q === it.q && x.vq.pkg === it.pkg);
    const lx = lessonOf(it.pkg, it.q, 'o');
    const body = qHeadHtml(it.pkg, it.q, { n: steps.length, reps: steps.filter(x => x.vq.rep).length }) + (lx ? `<div class="c-done ls-wrap"><div class="ls-head"><span class="mono kick dark">OPENING LESSON</span></div>${lessonHtml(lx, lessonPic(lx), autoChip())}</div>` : '');
    el.innerHTML = lx ? viLessonFrame(body) : body;
    big.innerHTML = `START${ICON.next}`;
    if (it.look) big.innerHTML = `BACK TO NOW${ICON.next}`;
    if (lx) { bindAutoChip(el, () => autoKick(el)); mountLesson(el, lx, { auto: flow.vauto, onEnd: () => { if (flow && flow.vauto && flow.inter === it) setTimeout(() => { if (flow && flow.inter === it) clearInter(); }, 1500); } }); viLessonTools(el, it, 'open'); }
    viLeft();
    return;
  }
  if (it.kind === 'vclose') {
    const lx = lessonOf(it.pkg, it.q, 'c'), q = vivaQ(it.pkg, it.q);
    el.innerHTML = viLessonFrame(`<div class="c-done vq-head"><span class="mono kick dark">VIVA ${esc(it.pkg)} · CLOSING LESSON · ${esc(it.q)}</span><h2 class="vq-t">${esc(q ? q.text : '')}</h2><p class="muted-d">The recap, then the spine card: say it yourself in 60 seconds.</p></div><div class="c-done ls-wrap"><div class="ls-head"><span class="mono kick dark">CLOSING LESSON</span></div>${lessonHtml(lx, lessonPic(lx), autoChip())}</div>`);
    big.innerHTML = it.look ? `BACK TO NOW${ICON.next}` : `SPINE${ICON.next}`;
    bindAutoChip(el, () => autoKick(el));
    mountLesson(el, lx, { auto: flow.vauto, onEnd: () => { if (flow && flow.vauto && flow.inter === it) setTimeout(() => { if (flow && flow.inter === it) clearInter(); }, 1500); } });
    viLessonTools(el, it, 'close');
    viLeft();
    return;
  }
  vivaMarks().then(m => {
    if (!flow || (flow.inter !== it && flow.lookInter !== it)) return;
    el.innerHTML = spineHtml(it.pkg, it.q, vivaLast(m, it.pkg, it.q));
    viLeft();
    const more = flow.queue.slice(flow.idx).some(x => x.vq);
    big.innerHTML = it.look ? `BACK TO NOW${ICON.next}` : more ? `NEXT QUESTION${ICON.next}` : `FINISH${ICON.next}`;
    const clk = el.querySelector('[data-vclock]'), tb = el.querySelector('[data-vtimer]');
    tb.onclick = e => {
      e.stopPropagation(); clearInterval(flow.vtimer); flow.vt0 = Date.now(); tb.textContent = 'Restart';
      flow.vtimer = setInterval(() => { if (!flow) return; const left = Math.max(0, 60 - Math.floor(((flow.pausedAt || Date.now()) - flow.vt0) / 1000)); if (!clk.isConnected) return clearInterval(flow && flow.vtimer); clk.textContent = '0:' + String(left).padStart(2, '0'); clk.classList.toggle('over', left === 0); if (!left) { clearInterval(flow.vtimer); const d = el.querySelector('[data-vspine]'); if (d) d.open = true; } }, 250);
    };
    el.querySelectorAll('[data-vmark]').forEach(b => b.onclick = async e => {
      e.stopPropagation(); await vivaSetMark(it.pkg, it.q, b.dataset.vmark); vivaMarks().then(m2 => { if (flow) { flow.vm = m2; drawThread(); } });
      el.querySelectorAll('[data-vmark]').forEach(x => x.classList.toggle('on', x === b));
      const d = el.querySelector('[data-vspine]'); if (d) d.open = true;
    });
  });
}
function bindBridges(el) { el.querySelectorAll('[data-xp-bridge]').forEach(b => b.onclick = e => { e.stopPropagation(); const a = b.nextElementSibling; if (a) a.hidden = false; b.remove(); }); }
// was the card just before this one (same deck) left out of this flow? then the bridge lines carry what it taught
function skippedBefore(c) {
  if (!c || c.topup || !(+c.no > 1)) return false;
  const prev = cardsOf(c.deck).find(x => +x.no === +c.no - 1 && !x.topup);
  return !!prev && !flow.queue.some(x => x.deck === c.deck && x.code === prev.code);
}

/* ---------- T-075: size per side = one slider (and a pinch), which re-flows the text; the card also has Fit ----------
   Fit = the whole card in view (the size goes down until it fits, not below 55%). Slider or pinch = your own size. */
const VZ = k => P.get('vz' + k, 1);
const fitMode = k => P.get('fit' + k, k === 'Card' && innerWidth >= 700 ? 'page' : 'custom');
function paneOf(el, k) { return k === 'Card' ? el.querySelector('.c-a, .c-q') : el.querySelector('.xp-pane'); }
function fitPane(el, k, live) {
  const box = paneOf(el, k); if (!box) return;
  box.classList.remove('pv'); box.style.removeProperty('--ts');
  let z = live != null ? live : VZ(k);
  if (live == null && fitMode(k) === 'page') {
    z = 1; box.style.setProperty('--z', 1);
    box.querySelectorAll(':scope > .ink-ov').forEach(c => { c.style.height = '0px'; });   // the ink layer is re-sized after; don't let its old height count
    for (let i = 0; i < 5; i++) { const H = box.clientHeight, S2 = box.scrollHeight; if (!H || S2 <= H + 2) break; z = Math.max(0.55, z * Math.pow(H / S2, 0.85)); box.style.setProperty('--z', z.toFixed(3)); if (z <= 0.55) break; }
  }
  box.style.setProperty('--z', (+z).toFixed(3));
  const c = el.querySelector(`[data-szc="${k}"]`);
  if (c) { c.querySelector('.fz').textContent = Math.round(z * 100) + '%'; const r = c.querySelector('input'); if (r && document.activeElement !== r) r.value = Math.round(z * 100); const f = c.querySelector('[data-fit]'); if (f) f.classList.toggle('on', fitMode(k) === 'page'); }
  box.dispatchEvent(new Event('toggle'));                       // ink follows the new geometry
}
function sizeControl(k) {
  return `<span class="fitc szc mono" data-szc="${k}" role="group" aria-label="${k === 'Card' ? 'Card' : 'Explain'} size">${k === 'Card' ? '<button data-fit title="Fit the whole card in view">Fit</button>' : ''}<input type="range" min="50" max="200" step="5" value="100" aria-label="Size"><span class="fz"></span></span>`;
}
function setupFit(el) {
  const ct = el.querySelector('.c-tags'); if (ct && !ct.querySelector('[data-szc]')) ct.insertAdjacentHTML('beforeend', sizeControl('Card'));
  const xb = el.querySelector('.xp-head .xp-bar'); if (xb && !xb.querySelector('[data-szc]')) xb.querySelector('.xp-tog').insertAdjacentHTML('afterend', sizeControl('Xp'));
  el.querySelectorAll('[data-szc]').forEach(c => {
    const k = c.dataset.szc, r = c.querySelector('input'), f = c.querySelector('[data-fit]');
    ['pointerdown', 'touchstart'].forEach(t => c.addEventListener(t, e => e.stopPropagation(), { passive: true }));
    r.oninput = () => { P.set('fit' + k, 'custom'); P.set('vz' + k, +r.value / 100); fitPane(el, k); };
    if (f) f.onclick = e => { e.stopPropagation(); P.set('fit' + k, fitMode(k) === 'page' ? 'custom' : 'page'); fitPane(el, k); };
  });
  requestAnimationFrame(() => { fitPane(el, 'Card'); fitPane(el, 'Xp'); });
  if (!window.__fitRO) { window.__fitRO = 1; addEventListener('resize', () => { const c = document.getElementById('card'); if (c && flow) { fitPane(c, 'Card'); fitPane(c, 'Xp'); } }); }
}
/* ---------- two-finger pinch on either side sets its size (swipes were removed on 5 Nov: not precise enough) ---------- */
function setupGestures(wrap) {
  if (!wrap || wrap.dataset.g) return; wrap.dataset.g = 1;
  let g = null;
  const pts = e => [...e.touches].slice(0, 2).map(t => [t.clientX, t.clientY]);
  const dist = q => Math.hypot(q[0][0] - q[1][0], q[0][1] - q[1][1]), mid = q => [(q[0][0] + q[1][0]) / 2, (q[0][1] + q[1][1]) / 2];
  wrap.addEventListener('touchstart', e => {
    if (e.touches.length !== 2 || !flow) { if (e.touches.length > 2) g = null; return; }
    const q = pts(e), m = mid(q), tgt = document.elementFromPoint(m[0], m[1]), k = tgt && tgt.closest('.xp-pane') ? 'Xp' : 'Card', card = document.getElementById('card');
    const box = card && paneOf(card, k); const z0 = box ? (+getComputedStyle(box).getPropertyValue('--z') || 1) : 1;
    g = { d0: dist(q), k, z0, card, on: false }; e.preventDefault();
  }, { passive: false });
  wrap.addEventListener('touchmove', e => {
    if (!g || e.touches.length !== 2) return; e.preventDefault();
    const r = dist(pts(e)) / g.d0; if (!g.on && Math.abs(r - 1) < 0.06) return; g.on = true;
    g.z = Math.max(0.5, Math.min(2, g.z0 * r)); fitPane(g.card, g.k, g.z);
  }, { passive: false });
  wrap.addEventListener('touchend', e => { if (!g || e.touches.length > 1) return; const G = g; g = null; if (G.on) { P.set('fit' + G.k, 'custom'); P.set('vz' + G.k, +G.z.toFixed(3)); fitPane(G.card, G.k); } });
}
// +1 = forward (reveal on the question side, next on the answer side); −1 = back (look at the card before)
function turn(dir, axis) {
  if (!flow || flow.busy || flow.userPause) return;
  flow.turnAxis = axis;
  if (dir > 0) { if (flow.peek) peekForward(false); else if (flow.inter) clearInter(); else if (flow.done) endFlow(); else if (flow.face === 'q') reveal(); else next(false); }
  else { if (flow.browse) undo(); else peekBack(); }
  setTimeout(() => { if (flow) flow.turnAxis = null; }, 600);
}
/* ---------- T-072: drag the divider between the card and Explain (remembered per profile, per orientation) ---------- */
function setupSplit(el) {
  const sp = el.querySelector('.a-split'), dv = sp && sp.querySelector('.a-div'); if (!dv) return;
  const land = () => matchMedia('(orientation:landscape) and (min-width:900px)').matches, key = () => land() ? 'splitL' : 'splitP';
  const apply = () => { const v = P.get(key(), land() ? 52 : 46); sp.style.setProperty('--split', v + '%'); };
  apply();
  dv.addEventListener('pointerdown', e => {
    if (e.pointerType === 'pen' && isWriting()) return;
    e.preventDefault(); dv.setPointerCapture(e.pointerId); sp.classList.add('dragging');
    const r = sp.getBoundingClientRect();
    const mv = ev => { const v = land() ? (ev.clientX - r.left) / r.width * 100 : (ev.clientY - r.top) / r.height * 100; const c = Math.max(22, Math.min(78, v)); sp.style.setProperty('--split', c.toFixed(1) + '%'); };
    const up = ev => { dv.removeEventListener('pointermove', mv); dv.removeEventListener('pointerup', up); dv.removeEventListener('pointercancel', up); sp.classList.remove('dragging'); P.set(key(), parseFloat(sp.style.getPropertyValue('--split')) || 50); fitPane(el, 'Card'); fitPane(el, 'Xp'); };
    dv.addEventListener('pointermove', mv); dv.addEventListener('pointerup', up); dv.addEventListener('pointercancel', up);
  });
  dv.ondblclick = () => { P.set(key(), land() ? 52 : 46); apply(); fitPane(el, 'Card'); fitPane(el, 'Xp'); };
}
// "Still unclear" (lasso or Select text on the Explain side): kept on this device per profile; Claude reads the list when it is shared
const inkOpts = c => ({ toolbarHost: () => document.getElementById('f-ink'), modeChanged: () => {}, docked: () => !!P.get('inkDock', 1),
  onAsk: (texts, from, rect) => askMenu(rect, { c, texts, from }),
  pin: () => { P.set('inkDock', P.get('inkDock', 1) ? 0 : 1); if (flow) renderFlow(); }, onUnclear: async texts => {
  const all = (await db.kv.get('xpUnclear')) || [];
  for (const t of texts) all.push({ deck: c.deck, code: c.code, text: t, ts: Date.now(), ver: X.v });
  await db.kv.set('xpUnclear', all);
} });
/* ---------- T-077: Ask Claude — copy a ready question (card context + what you selected) and open one of your chats ----------
   Claude can't receive a message into an existing chat from a link, so Trace copies the question and opens the chat;
   you paste and send. Chats (name + claude.ai/chat/… link) are kept per profile in ⚙ › Claude chats. */
const ASK_TPL = `{deck} · {code} · {title}
Question: {question}
Card answer: {answer}
I selected ({from}): "{selected}"
{ask}
Look it up first: card {code} in deck {deckid} — Google Drive › Trace › Study desk › 00 INDEX tells you where; link related cards from other decks and cite their IDs.`;
// T-080: quick intents — the {ask} line. Editable in ⚙ › Claude chats; most-used first. The free box adds your own words.
const INTENTS = [
  ['explain', 'Explain', 'Explain this part properly: the mechanism, step by step.'],
  ['normal', 'Normal value', 'Give the normal values and cut-offs with units, and what moves them up or down.'],
  ['mech', 'Mechanism', 'Walk me through the mechanism from the cause to this finding, one step at a time.'],
  ['basics', 'Basics first', 'Start from the basic physiology I need for this, then build up to it.'],
  ['compare', 'Compare', 'Compare this with its close mimics in a table, and name the one feature that separates them.'],
  ['why', 'Why wrong', 'What is the common wrong answer here, and why is it wrong? Show the reasoning.'],
  ['exam', 'Exam angle', 'How is this asked in NEET-SS? The traps, the cut-offs and the wording examiners use.'],
  ['connect', 'Connect', 'connect: where else does this come up in my other decks and systems? Cite the card IDs.']
].map(([id, label, line]) => ({ id, label, line }));
// T-086: more ready-made intents to add from ⚙ › Claude chats › Quick intents (tap a suggestion to add it)
const INTENT_IDEAS = [
  ['patho', 'Pathophysiology', 'Explain the pathophysiology behind this, from the trigger to the bedside finding.'],
  ['ddx', 'Differential', 'What else presents like this, and what is the one feature that separates each?'],
  ['steps', 'Steps in order', 'What are the management steps in order, with the decision point at each step?'],
  ['doses', 'Doses & why', 'Give the doses, routes and timings, and why each dose is what it is.'],
  ['guide', 'Guideline now', 'What does the current guideline say (name and year), and has it changed recently?'],
  ['case', 'Clinical case', 'Give me one clinical vignette where this decides the answer, then explain the answer.'],
  ['asked', 'What was asked', 'what was asked: list the real QBank, GT and NEET questions linked to this card.'],
  ['quiz', 'Quiz me 3', 'quiz: ask me 3 new MCQs on this, one at a time, and wait for my answer each time.'],
  ['simple', 'Simpler', 'simpler: explain this again as to a first-year resident.'],
  ['table', 'Table', 'table: put this and its mimics in a comparison table.'],
  ['check', 'Check card', 'check: is anything on this card wrong or outdated against current guidelines?']
].map(([id, label, line]) => ({ id, label, line }));
const intents = () => { const a = P.get('aiIntents', null); return Array.isArray(a) && a.length ? a : INTENTS; };
const intentsSorted = () => { const use = P.get('aiIntentUse', {}); return intents().slice().sort((a, b) => (use[b.id] || 0) - (use[a.id] || 0)); };
const chats = () => P.get('aiChats', []), activeChat = () => { const a = chats(), id = P.get('aiActive', ''); return a.find(x => x.id === id) || a[0] || null; };
function askText({ c, texts, from, kind, intent, own }) {
  const one = s => plain(String(s || '')).replace(/\s+/g, ' ').trim();
  const { head, rest } = splitQ(c.q);
  const sel = texts && texts.length ? texts.join(' … ') : '';
  let t = P.get('aiTpl', '') || ASK_TPL;
  const it = intent ? intents().find(x => x.id === intent) : null;
  let ask = kind === 'trap' ? 'Why is this wrong, and what is right? Show the reasoning.'
    : it ? it.line : (sel ? 'Explain this part properly: the mechanism, step by step.' : 'Explain this card properly: the mechanism behind each part, step by step.');
  if (it && it.id === 'explain' && !sel) ask = 'Explain this card properly: the mechanism behind each part, step by step.';
  own = String(own || '').trim();
  if (own) ask = it || kind === 'trap' ? ask + '\n' + own : own;
  if (!/\{ask\}/.test(t)) t = /Explain this part properly[^\n]*/.test(t) ? t.replace(/Explain this part properly[^\n]*/, '{ask}') : t + '\n{ask}';
  t = t.replace(/\{ask\}/g, () => ask.replace(/\$/g, '$$$$'));
  if (!sel) t = t.replace(/I selected[^\n]*\n?/, '');
  if (kind === 'trap') t = t.replace(/I selected[^\n]*/, 'Exam trap on this card: "{selected}"');
  const m = deckMeta(c.deck) || {};
  return t.replace(/\{deckid\}/g, c.deck).replace(/\{deck\}/g, c.deck + (m.title ? ' (' + m.title + ')' : '')).replace(/\{code\}/g, c.code).replace(/\{title\}/g, one(head).replace(/:$/, ''))
    .replace(/\{question\}/g, one(rest || head).slice(0, 400)).replace(/\{answer\}/g, one(c.a).slice(0, 700)).replace(/\{selected\}/g, sel).replace(/\{from\}/g, from || 'card');
}
async function copyText(t) { try { await navigator.clipboard.writeText(t); return true; } catch (e) { try { const ta = document.createElement('textarea'); ta.value = t; ta.style.position = 'fixed'; ta.style.opacity = '0'; document.body.appendChild(ta); ta.select(); const ok = document.execCommand('copy'); ta.remove(); return ok; } catch (er) { return false; } } }
async function logAsk(o) { try { const a = (await db.kv.get('askLog')) || []; a.push({ ...o, ts: Date.now() }); await db.kv.set('askLog', a.slice(-500)); } catch (e) { /* */ } }
async function doAsk(where, payload) {
  const text = askText(payload), c = payload.c;
  if (where === 'google') { const q = (payload.texts && payload.texts.length ? payload.texts.join(' ') : plain(splitQ(c.q).head)) + ' ' + ((deckMeta(c.deck) || {}).system || ''); window.open('https://www.google.com/search?q=' + encodeURIComponent(q.trim().slice(0, 300)), 'trace-google'); logAsk({ deck: c.deck, code: c.code, where: 'google', text: q }); return; }
  const ok = await copyText(text);
  if (where === 'new') { window.open('https://claude.ai/new?q=' + encodeURIComponent(text), 'trace-claude'); toast(ok ? 'Copied too — if the new chat is empty, paste and send' : 'Opened a new chat'); logAsk({ deck: c.deck, code: c.code, where: 'new', text }); return; }
  const ch = chats().find(x => x.id === where); if (!ch) return;
  P.set('aiActive', ch.id);
  window.open(ch.url, 'trace-claude');
  toast(ok ? `Copied · in “${ch.name}” long-press, Paste, Send` : 'Could not copy — the browser blocked it');
  logAsk({ deck: c.deck, code: c.code, where: ch.name, text });
}
function askMenu(rect, payload) {
  document.querySelectorAll('.ask-menu').forEach(n => n.remove());
  const list = chats(), act = activeChat();
  const m = document.createElement('div'); m.className = 'ask-menu';
  const its = intentsSorted();
  let pick = P.get('aiIntentLast', '') && its.some(x => x.id === P.get('aiIntentLast', '')) ? P.get('aiIntentLast', '') : (its[0] || {}).id;
  if (payload.kind === 'trap') pick = '';
  m.innerHTML = `<p class="mono am-h">ASK CLAUDE${payload.texts && payload.texts.length ? ' · selection' : payload.kind === 'trap' ? ' · exam trap' : ' · whole card'}</p>
    <div class="am-int" role="radiogroup" aria-label="What do you want?">${its.map(x => `<button data-int="${esc(x.id)}" role="radio" aria-checked="${x.id === pick}" class="${x.id === pick ? 'on' : ''}">${x.id === pick ? '✓ ' : ''}${esc(x.label)}</button>`).join('')}</div>
    <textarea class="am-own" rows="2" placeholder="Or ask in your own words…" data-own></textarea>
    <p class="mono am-h am-h2">SEND TO</p>
    ${list.length ? list.map(x => `<button data-ask="${esc(x.id)}" class="${act && act.id === x.id ? 'on' : ''}"><b>${esc(x.name)}</b>${act && act.id === x.id ? '<span class="mono">last used</span>' : ''}</button>`).join('') : '<p class="am-n">No chats yet. Add your Claude chats in ⚙ › Claude chats.</p>'}
    <button data-ask="new" class="am-sub">New chat (pre-filled)</button>
    <button data-ask="google" class="am-sub">Search Google</button>
    <button data-ask="manage" class="am-sub mono">Manage chats…</button>`;
  document.body.appendChild(m);
  const own = m.querySelector('[data-own]');
  own.onkeydown = e => e.stopPropagation();
  m.querySelectorAll('[data-int]').forEach(b => b.onclick = e => { e.stopPropagation(); pick = pick === b.dataset.int ? '' : b.dataset.int;
    m.querySelectorAll('[data-int]').forEach(x => { const on = x.dataset.int === pick; x.classList.toggle('on', on); x.setAttribute('aria-checked', on); x.textContent = (on ? '✓ ' : '') + (its.find(i => i.id === x.dataset.int) || {}).label; }); });
  const w = Math.min(320, innerWidth - 16), x = Math.max(8, Math.min(innerWidth - w - 8, (rect ? rect.left : innerWidth / 2 - w / 2))), y = rect ? Math.min(innerHeight - m.offsetHeight - 8, rect.bottom + 6) : 80;
  Object.assign(m.style, { left: x + 'px', top: Math.max(8, y) + 'px', width: w + 'px' });
  const off = e => { if (!m.contains(e.target)) { m.remove(); document.removeEventListener('pointerdown', off, true); } };
  setTimeout(() => document.addEventListener('pointerdown', off, true), 0);
  m.querySelectorAll('[data-ask]').forEach(b => b.onclick = e => { e.stopPropagation(); const k = b.dataset.ask; m.remove(); document.removeEventListener('pointerdown', off, true);
    if (k === 'manage') { const pp = $('#f-pop'); if (pp) { pp.hidden = false; const cs = pp.querySelector('.ai-set'); if (cs) cs.open = true; } return; }
    if (pick) { const use = P.get('aiIntentUse', {}); use[pick] = (use[pick] || 0) + 1; P.set('aiIntentUse', use); P.set('aiIntentLast', pick); }
    doAsk(k, { ...payload, intent: pick, own: own.value }); });
}
function chatSettingsHtml() {
  const list = chats(), act = activeChat();
  return `<details class="ai-set"><summary class="mono">CLAUDE CHATS · ${list.length}</summary>
    <div class="ai-list">${list.map(x => `<div class="ai-row${act && act.id === x.id ? ' on' : ''}"><b>${esc(x.name)}</b><span class="mono">${esc(x.url.replace(/^https?:\/\//, '').slice(0, 34))}…</span><button data-aidel="${esc(x.id)}" aria-label="Remove ${esc(x.name)}">✕</button></div>`).join('') || '<p class="muted small">None yet.</p>'}</div>
    <div class="ai-add"><input data-ain placeholder="Name (e.g. TOX doubts)"><input data-aiu placeholder="Chat link: https://claude.ai/chat/…"><button data-aiadd>Add</button></div>
    <details class="ai-tpl ai-ints"><summary class="mono">QUICK INTENTS · ${intents().length}</summary>
      <p class="muted small">The button name, and the line it puts into the message. Most-used come first in the Ask menu.</p>
      ${intents().map((x, i) => `<div class="ai-int" data-i="${i}"><input data-il value="${esc(x.label)}" aria-label="Button name"><textarea data-iline rows="2" aria-label="Line it adds">${esc(x.line)}</textarea><button data-idel aria-label="Remove ${esc(x.label)}">✕</button></div>`).join('')}
      <p class="mono ai-sug-h">SUGGESTIONS · TAP TO ADD</p>
      <div class="ai-sug">${INTENT_IDEAS.filter(x => !intents().some(y => y.id === x.id || y.label === x.label)).map(x => `<button data-isug="${x.id}" title="${esc(x.line)}">+ ${esc(x.label)}</button>`).join('') || '<span class="muted small">All added.</span>'}</div>
      <div class="ai-add"><button data-iadd>+ Write your own</button><button data-ireset>Reset to defaults</button></div></details>
    <details class="ai-tpl"><summary class="mono">MESSAGE TEMPLATE</summary><textarea data-aitpl rows="6">${esc(P.get('aiTpl', '') || ASK_TPL)}</textarea><p class="muted small">{deck} {deckid} {code} {title} {question} {answer} {selected} {from} are filled in from the card; {ask} is the quick intent or your own words.</p><button data-aitplreset>Reset</button></details>
  </details>`;
}
function bindChatSettings(h) {
  const add = h.querySelector('[data-aiadd]');
  if (add) add.onclick = () => {
    const n = h.querySelector('[data-ain]').value.trim(), u = h.querySelector('[data-aiu]').value.trim();
    if (!/^https:\/\/(claude\.ai|chatgpt\.com|chat\.openai\.com|gemini\.google\.com)\//.test(u)) { toast('Paste the chat’s link (https://claude.ai/chat/…)'); return; }
    const a = chats(); a.push({ id: 'c' + Date.now().toString(36), name: n || 'Chat ' + (a.length + 1), url: u }); P.set('aiChats', a); drawXpToggles(); keepOpen();
  };
  h.querySelectorAll('[data-aidel]').forEach(b => b.onclick = () => { P.set('aiChats', chats().filter(x => x.id !== b.dataset.aidel)); drawXpToggles(); keepOpen(); });
  const ta = h.querySelector('[data-aitpl]'); if (ta) { ta.onkeydown = e => e.stopPropagation(); ta.onchange = () => P.set('aiTpl', ta.value.trim() === ASK_TPL.trim() ? '' : ta.value); }
  const rs = h.querySelector('[data-aitplreset]'); if (rs) rs.onclick = () => { P.set('aiTpl', ''); drawXpToggles(); keepOpen(); };
  const saveInts = a => P.set('aiIntents', a);
  h.querySelectorAll('.ai-int').forEach(row => {
    const i = +row.dataset.i;
    row.querySelectorAll('input,textarea').forEach(f => { f.onkeydown = e => e.stopPropagation(); f.onchange = () => { const a = intents().map(x => ({ ...x })); a[i] = { ...a[i], label: row.querySelector('[data-il]').value.trim() || a[i].label, line: row.querySelector('[data-iline]').value.trim() || a[i].line }; saveInts(a); }; });
    row.querySelector('[data-idel]').onclick = () => { const a = intents().filter((_, j) => j !== i); saveInts(a.length ? a : null); drawXpToggles(); keepOpen(true); };
  });
  const ia = h.querySelector('[data-iadd]'); if (ia) ia.onclick = () => { const a = intents().map(x => ({ ...x })); a.push({ id: 'i' + Date.now().toString(36), label: 'New', line: 'Write the line it adds here.' }); saveInts(a); drawXpToggles(); keepOpen(true); };
  h.querySelectorAll('[data-isug]').forEach(b => b.onclick = () => { const x = INTENT_IDEAS.find(i => i.id === b.dataset.isug); if (!x) return; saveInts(intents().map(y => ({ ...y })).concat({ ...x })); drawXpToggles(); keepOpen(true); });
  const ir = h.querySelector('[data-ireset]'); if (ir) ir.onclick = () => { P.set('aiIntents', null); drawXpToggles(); keepOpen(true); };
  h.querySelectorAll('input').forEach(i => { i.onkeydown = e => e.stopPropagation(); });
  function keepOpen(ints) { const d = document.querySelector('#f-xp .ai-set') || document.querySelector('.ai-set'); if (d) { d.open = true; if (ints) { const e = d.querySelector('.ai-ints'); if (e) e.open = true; } } }
}
// the Explain header (title, size, Learn/Revise) lives above the scrolling explanation, never inside it
function placeXpBar(el) {
  const head = el.querySelector('.xp-head'), bar = el.querySelector('.xp-pane .xp-bar'); if (!head || !bar) return;
  head.innerHTML = ''; head.appendChild(bar);
  if (!bar.querySelector('[data-act=askx]')) bar.insertAdjacentHTML('beforeend', '<button class="askbtn mono" data-act="askx" aria-label="Ask Claude about this explanation">Ask ▸</button>');
}
function bindXp(el, c) {
  el.querySelectorAll('[data-xtab]').forEach(b => b.onclick = e => { e.stopPropagation(); flow.xpTab = flow.xpTab || {}; flow.xpTab[c.deck + '|' + c.code] = b.dataset.xtab; drawCard(); });
  const ax = el.querySelector('[data-act=askx]'); if (ax) ax.onclick = e => { e.stopPropagation(); askMenu(ax.getBoundingClientRect(), { c, texts: [], from: 'Explain' }); };
  const ab = el.querySelector('[data-act=ask]'); if (ab) ab.onclick = e => { e.stopPropagation(); askMenu(ab.getBoundingClientRect(), { c, texts: [], from: 'card' }); };
  const xt = el.querySelector('[data-xp-tog]');
  if (xt) xt.onclick = e => { e.stopPropagation(); const xp = el.querySelector('.xp-pane .xp') || xt.closest('.xp'), body = xp.querySelector('.xp-body'), open = body.hidden; body.hidden = !open; xp.classList.toggle('open', open); xt.setAttribute('aria-expanded', open); const hn = xt.querySelector('.xp-hint'); if (hn) hn.textContent = open ? 'hide' : 'mechanism · context · what the exam tempts you with'; const sp = xt.closest('.a-split'); if (sp) sp.classList.toggle('xp-on', open); };
  el.querySelectorAll('[data-xp-depth]').forEach(b => b.onclick = e => { e.stopPropagation(); const cc = current(); flow.depthOver = flow.depthOver || {}; flow.depthOver[cc.deck + '|' + cc.code] = b.dataset.xpDepth; if (vivaX(cc)) { drawCard(); return; } const pane = el.querySelector('.xp-pane'); const xx = xOf(cc); if (pane && xx) { pane.innerHTML = panelHtml(cc, xx, { open: true, traps: xpTraps(), depth: b.dataset.xpDepth }); pane.scrollTop = 0; placeXpBar(el); const sp = el.querySelector('.a-split'); if (sp) sp.classList.add('xp-on'); bindXp(el, cc); setupFit(el); mountInk(el, cc, 'a', inkOpts(cc)); } });
  el.querySelectorAll('[data-pat]').forEach(b => b.onclick = e => { e.stopPropagation(); const k = b.dataset.pat; planSheet(X.patterns[k].name, 'PATTERN', patternHtml(k), () => {}); });
  const nt = el.querySelector('[data-xp-note]');
  if (nt) { getNote(c).then(v => { if (v && !nt.value) nt.value = v; }); nt.onkeydown = e => e.stopPropagation(); nt.onchange = () => setNote(c, nt.value.trim()); nt.onblur = () => setNote(c, nt.value.trim()); }
  el.querySelectorAll('[data-xp-fb]').forEach(b => b.onclick = e => { e.stopPropagation(); feedback(c, b.dataset.xpFb); b.closest('.xp-fb').querySelectorAll('button').forEach(x => x.classList.toggle('on', x === b)); toast('Thanks — noted for the next rewrite.'); });
}
function drawCard() {
  const el = $('#card'), big = $('#f-big');
  vStop();
  if (flow.lookInter) { drawInter(el, big, flow.lookInter); return; }
  if (!flow.inter && !flow.done && !flow.peek && !flow.look && flow.face === 'q') {
    const cd = current(); flow.mapSeen = flow.mapSeen || {};
    if (flow.viva) { if (cd && cd.vq && cd.vq.i === 0 && !cd.vq.again && !flow.vqSeen[flow.idx]) { flow.vqSeen[flow.idx] = 1; flow.inter = { kind: 'vq', pkg: cd.vq.pkg, q: cd.vq.q, at: flow.idx }; } }
    else if (cd && mapOf(cd.deck) && !flow.mapSeen[cd.deck]) { flow.mapSeen[cd.deck] = 1; flow.inter = { kind: 'map', deck: cd.deck }; }
  }
  if (flow.inter && !flow.peek) { drawInter(el, big); return; }   // looking back at a card keeps the live lesson waiting
  if (flow.done && !flow.peek) {
    const n = flow.times.length, tot = (Date.now() - flow.t0) / 1000;
    el.classList.remove('ng');
    if (flow.browse) { el.innerHTML = `<div class="c-done"><span class="mono kick dark">END OF THE DECK</span><h2>You looked through ${flow.queue.length} card${flow.queue.length === 1 ? '' : 's'}</h2><p class="muted-d">Nothing was logged. Use Flow now when you want it to count.</p></div>`; big.innerHTML = 'CLOSE'; return; }
    el.innerHTML = `<div class="c-done"><span class="mono kick dark">FLOW COMPLETE</span><h2>${n} card${n === 1 ? '' : 's'} walked</h2>
      <p>${clock(tot)} in total · ${n ? fmtDur(flow.times.reduce((a, b) => a + b, 0) / n / 1000) : '–'} per card</p>
      <p class="muted-d">Save sends these cards to your counts and the War Map Sheet. Discard removes them as if this flow never happened.</p>
      <button class="link" data-discard>Discard this flow</button></div>`;
    big.innerHTML = 'SAVE';
    const dc = el.querySelector('[data-discard]'); if (dc) dc.onclick = () => askEnd(true);
    return;
  }
  const c = current(), tag = neetTag(c), n = seen(c.deck, c.no);
  const { head, rest } = splitQ(c.q);
  const isQ = !flow.peek && flow.face === 'q';
  const top = `<div class="c-head mono"><span>${esc((c.section || '').toUpperCase())}</span><span>${esc(c.code)}</span></div>
    <div class="c-tags">${tag ? `<span class="neet mono">${esc(tag)}</span>` : ''}${qbChips(c)}<span class="mono seen">seen ×${n}</span>${c.edited ? '<span class="mono seen">edited</span>' : ''}
      ${isQ ? '' : `<button class="askbtn mono" data-act="ask" aria-label="Ask Claude about this card">Ask ▸</button><button class="tagbtn" data-act="edit" aria-label="Edit this card">${ICON.edit}</button>${flow.browse || flow.peek ? '' : `<button class="again" data-act="again" aria-label="Show this card again at the end">${ICON.again}Again</button>`}`}</div>`;
  let body;
  if (isQ) {
    const xq = xOf(c);
    // T-091: the primer and story always sit on the card (so marks on them always have a home): open while learning,
    // folded when the card is at Revise depth (same rule as the Explain pane), tap to open
    const arc = spineOf(c.deck) && xq && xq.step ? { open: ((flow.depthOver && flow.depthOver[c.deck + '|' + c.code]) || depthOf(xq, n, xpDepth())) !== 'revise' } : null;
    // T-090: the primer and story boxes sit inside the question face so the pen, highlighter, Select text and Ask work on them
    const vrep = c.vq && c.vq.rep ? `<p class="vq-rep mono">SEEN ABOVE · under ${esc(c.vq.rep)} · not counted again · Reveal to look, Next to move on</p>` : '';
    body = `<div class="c-q" data-act="reveal" role="button" tabindex="0" aria-label="Reveal answer"><div class="zw">${vrep}${flow.viva ? '' : arc ? arcHtml(c, xq, arc.open) : bridgeHtml(c, xq, skippedBefore(c))}<span class="qh${rest ? '' : ' solo'}">${inline(head)}</span>${rest ? `<div class="qr">${render(rest)}</div>` : ''}${c.vpic ? `<img class="vq-pic" src="${esc(vivaImgSrc(c.vcard, c.vpic))}" alt="Spotter image">` : ''}${n > 0 ? partsQHtml(c, xq) : ''}<span class="star">✦</span></div></div>`;
  } else {
    const lx = c.vq && c.vq.j != null ? lessonOf(c.vq.pkg, c.vq.q, 's' + c.vq.j) : null;
    const xa = xOf(c), vx = vivaX(c), v2 = !!(xa && xa.v === 2) || !!vx || !!lx, xOpen = (flow.viva && (vx || lx)) || xpOpenMode() !== 'tap' || (xpOpenMode() === 'new' && n === 0);
    // T-095: NEET | Viva switch when a card has both; opens on Viva in a viva walk, on NEET elsewhere
    const ck = c.deck + '|' + c.code; flow.xpTab = flow.xpTab || {};
    const avail = [lx && 'lesson', xa && 'neet', vx && 'viva'].filter(Boolean);
    let xtab = flow.xpTab[ck]; if (!avail.includes(xtab)) xtab = lx ? 'lesson' : !vx ? 'neet' : !xa ? 'viva' : (flow.viva ? 'viva' : 'neet');
    const sw = avail.length > 1 ? tabSwitch(xtab, avail) : '';
    const xpPane = o => xtab === 'lesson' ? `<div class="xp v2 vx open ls-pane" data-depth="learn"><div class="xp-bar"><span class="xp-tog"${sw ? ' hidden' : ''}><span>Lesson</span></span>${sw}</div><div class="xp-body">${lessonHtml(lx, lessonPic(lx, c), autoChip())}</div></div>`
      : xtab === 'viva' ? vivaPanelHtml(vx, sw) : (sw ? panelHtml(c, xa, o).replace('<div class="xp-bar">', '<div class="xp-bar">' + sw) : panelHtml(c, xa, o));
    const depth = (flow.depthOver && flow.depthOver[c.deck + '|' + c.code]) || depthOf(xa, n, xpDepth());
    body = `${v2 ? `<div class="a-split${xOpen ? ' xp-on' : ''}"><section class="pane-card"><div class="pane-head">${top}</div>` : ''}<div class="c-a${hasExplain(c) && !v2 ? ' has-xp' : ''}"><div class="zw">
      <h2 class="c-title">${esc(plain(head).replace(/:$/, ''))}</h2>
      ${rest ? `<details class="qrecap" open><summary>Question parts</summary><div class="qr small">${render(rest)}</div></details>` : ''}
      ${qbFix(c)}
      <div class="ans">${render(c.a)}</div>
      ${vivaAns(c)}
      ${c.fixed ? `<p class="qsrc-card mono">Corrected ${esc(c.fixed.date)} · ${esc(c.fixed.src)}</p>` : ''}
      ${gistHtml(xOf(c))}${n > 0 ? partsAHtml(c, xOf(c)) : ''}
      ${c.img ? `<div class="box note"><span class="mono">DIAGRAM</span><p>This card has a figure on page ${c.a_page || c.q_page || '?'} of the PDF deck.</p></div>` : ''}
      ${c.why ? `<div class="box why"><span class="mono">WHY</span><div class="bx">${render(c.why)}</div></div>` : ''}
      ${c.watch ? `<div class="box watch"><span class="mono">WATCH</span><div class="bx">${render(c.watch)}</div></div>` : ''}
      ${hasExplain(c) && !v2 ? panelHtml(c, xa, { open: xpOpenMode() === 'new' && n === 0, traps: xpTraps(), note: '' }) : v2 ? (c.vcard ? qbBoxes(c) : '') : qbBoxes(c)}
      <label class="hook"><span class="mono">YOUR OT HOOK</span><input type="text" id="hook" value="${esc(c.hook || '')}" placeholder="A detail that makes it stick…" enterkeyhint="done"></label>
    </div></div>${v2 ? `</section><div class="a-div" role="separator" aria-label="Drag to resize the card and Explain" tabindex="0"><i></i></div><section class="pane-xp"><div class="xp-head"></div><aside class="xp-pane">${xpPane({ open: xOpen, traps: xpTraps(), depth })}</aside></section></div>` : ''}`;
  }
  const split = !isQ && el && body.startsWith('<div class="a-split');
  el.innerHTML = (flow.peek ? `<div class="peek-bar mono"><span>LOOKING BACK · ${flow.peek} card${flow.peek > 1 ? 's' : ''} back · nothing changes</span><span>← further · → forward</span></div>` : '') + (split ? '' : top) + body;
  placeXpBar(el);
  if (voiceOn()) mountVoice(el, c, isQ);
  if (!flow.peek && flow.viva && c.vq && c.vq.j != null) {
    const lx = lessonOf(c.vq.pkg, c.vq.q, 's' + c.vq.j);
    if (lx && isQ && flow.vauto) { const at = flow.idx; setTimeout(() => { if (flow && flow.idx === at && flow.face === 'q' && !flow.inter) reveal(); }, 1200); }
    if (lx && !isQ && el.querySelector('[data-lesson]')) {
      bindAutoChip(el);
      const at = flow.idx;
      el.querySelectorAll('[data-lcardfig]').forEach(b => b.onclick = e => { e.stopPropagation(); const v = el.querySelector('.vchip'); if (v && !v.disabled) v.click(); else toast(c.img ? 'The figure is on page ' + (c.a_page || c.q_page || '?') + ' of the PDF deck.' : 'No figure for this card on this device.'); });
      mountLesson(el, lx, { auto: flow.vauto, onEnd: () => { if (flow && flow.vauto && flow.idx === at && !flow.inter) setTimeout(() => { if (flow && flow.idx === at && !flow.inter) next(false); }, 1500); } });
    }
  }
  el.classList.toggle('peeking', !!flow.peek);
  el.classList.toggle('ng', isNeet(c));
  closePanel();
  if (!IS_HT && hasVisual(c)) {
    const chip = document.createElement('button'); chip.className = 'vchip mono'; chip.textContent = isQ ? '◈ visual after reveal' : '◈ Visual';
    if (isQ) chip.disabled = true; else chip.onclick = e => { e.stopPropagation(); const t = el.querySelector('.vl-head'); if (t) t.click(); else { const v = el.querySelector('.vl'); v && v.click(); } };
    el.querySelector('.c-tags').appendChild(chip);
    if (!isQ) linkCard(el, c, openPanel);
  }
  el.scrollTop = 0;
  const a = el.querySelector('.c-a'); if (a) a.scrollTop = 0;
  const xpn = el.querySelector('.xp-pane'); if (xpn) xpn.scrollTop = 0;
  big.innerHTML = flow.peek ? `BACK TO CURRENT${ICON.next}` : isQ ? `${ICON.flip}REVEAL` : `NEXT${ICON.next}`;
  const lb = $('#f-left'); if (lb) { lb.innerHTML = leftLabel(); lb.classList.toggle('dimmed', !flow.browse && !flow.peek && isQ && !flow.hist.length); }
  el.querySelectorAll('[data-act=reveal]').forEach(b => { b.onclick = e => { if (isWriting()) return; { const ws = getSelection(); if ((ws && !ws.isCollapsed && b.contains(ws.anchorNode)) || document.querySelector('.ik-tsel')) return; } if (e.target.closest && e.target.closest('.xp-before, .xp-bridge')) return; reveal(); }; b.onkeydown = e => { if (e.key === 'Enter') { e.preventDefault(); reveal(); } }; });
  const ag = el.querySelector('[data-act=again]'); if (ag) ag.onclick = () => next(true);
  const ed = el.querySelector('[data-act=edit]'); if (ed) ed.onclick = () => openEditor(current());
  const ib = el.querySelector('[data-act=ink]'); if (ib) ib.onclick = e => { e.stopPropagation(); setWriting(!isWriting()); };
  mountInk(el, c, isQ ? 'q' : 'a', inkOpts(c));
  bindBridges(el);
  bindXp(el, c);
  setupFit(el);
  setupSplit(el);
  const hk = el.querySelector('#hook');
  if (hk) {
    const save = () => { const v = hk.value.trim(); const cc = current(); if (v !== (cc.hook || '')) saveHook(cc, v); };
    hk.onchange = save; hk.onblur = save;
    hk.onkeydown = e => { e.stopPropagation(); if (e.key === 'Enter') hk.blur(); };
  }
}
/* ---------- T-099 card voice: Listen (the whole side) and ▶ for each point; speed − / + ---------- */
// the explanation points of a card: NEET (intro, part by part, punchline) and Viva (intro, part by part, picture caption)
function xParts(c, only) {
  const code = String(c.code).replace(/[^\w.\-]/g, '_'), out = [];
  const x = xOf(c), vx = vivaX(c);
  if ((!only || only === 'neet') && x && x.v === 2) {
    if (x.intro) out.push({ k: code + '.n0', label: 'Intro', t: x.intro, side: 'neet' });
    (x.why || []).forEach(([l, t], i) => out.push({ k: code + '.n' + (i + 1), label: l || String(i + 1), t, side: 'neet' }));
    if (x.punch) out.push({ k: code + '.np', label: 'Punch', t: x.punch, side: 'neet' });
  }
  if ((!only || only === 'viva') && vx) {
    const v = vx.x;
    if (v.intro) out.push({ k: code + '.v0', label: 'Intro', t: v.intro, side: 'viva' });
    (v.why || []).forEach(([l, t], i) => out.push({ k: code + '.v' + (i + 1), label: l || String(i + 1), t, side: 'viva' }));
    if (v.cap) out.push({ k: code + '.vc', label: 'Pic', t: v.cap, side: 'viva' });
  }
  return out;
}
function mountVoice(el, c, isQ) {
  if (!isQ) { const xp = el.querySelector('.xp-pane .xp-body'); if (xp && !xp.querySelector('[data-lesson]')) { const tab = xp.closest('.xp.vx') ? 'viva' : 'neet'; const xs = partsOf({ code: c.code, q: '' }, xParts(c, tab)).filter(p => p.k.split('.').pop() !== 'q'); if (xs.length) voiceStrip(c, xs, xp, 'prepend', 'explanation'); } }
  const all = partsOf(c), show = isQ ? all.filter(p => p.label === 'Q') : all;
  if (!show.length) return;
  const host = isQ ? el.querySelector('.c-q .zw') : el.querySelector('.c-a .ans');
  if (!host) return;
  voiceStrip(c, show, host, isQ ? 'append' : 'after', isQ ? 'question' : 'answer', isQ);
}
const TABN = { lesson: 'Lesson', neet: 'NEET', viva: 'Viva' };
const tabSwitch = (tab, avail) => `<span class="xv-seg vx-sw" role="group" aria-label="Which explanation">${avail.map(k => `<button class="${tab === k ? 'on' : ''}" data-xtab="${k}" aria-pressed="${tab === k}">${TABN[k]}</button>`).join('')}</span>`;
const mmss = t => { t = Math.max(0, Math.round(t || 0)); return Math.floor(t / 60) + ':' + String(t % 60).padStart(2, '0'); };
function voiceStrip(c, show, host, where, what, noChips) {
  const strip = document.createElement('div'); strip.className = 'vstrip';
  strip.innerHTML = `<button class="vlisten mono" data-vall aria-label="Listen to this ${what}">▶ Listen</button>${noChips ? '' : show.map(p => `<button class="vp mono" data-vk="${esc(p.k)}" aria-label="Play point ${esc(p.label)}">${esc(p.label)}</button>`).join('')}<span class="vspd mono"><button data-vs="-1" aria-label="Slower">−</button><b>${vSpeed().toFixed(1)}×</b><button data-vs="1" aria-label="Faster">+</button></span>
    <div class="vbar" hidden><button class="mono" data-vj="-10" aria-label="Back 10 seconds">−10</button><button class="mono" data-vj="-5" aria-label="Back 5 seconds">−5</button><button class="vpp" data-vpp aria-label="Pause">❚❚</button><button class="mono" data-vj="5" aria-label="Forward 5 seconds">+5</button><button class="mono" data-vj="10" aria-label="Forward 10 seconds">+10</button><input type="range" class="vseek" min="0" max="1000" value="0" step="1" aria-label="Position"><span class="vtime mono">0:00 / 0:00</span></div><span class="vmsg mono muted"></span>`;
  if (where === 'append') host.appendChild(strip); else if (where === 'prepend') host.prepend(strip); else host.insertAdjacentElement('afterend', strip);
  ['pointerdown', 'click', 'touchstart', 'input', 'change'].forEach(t => strip.addEventListener(t, e => e.stopPropagation()));
  const mark = k => strip.querySelectorAll('[data-vk]').forEach(b => b.classList.toggle('on', b.dataset.vk === k));
  const lis = strip.querySelector('[data-vall]'), bar = strip.querySelector('.vbar'), rng = bar.querySelector('.vseek'), tm = bar.querySelector('.vtime'), pp = bar.querySelector('[data-vpp]');
  let tick = null, drag = false;
  const draw = () => {
    if (!strip.isConnected) { clearInterval(tick); return; }
    const T = vTotal(), t = vPos();
    if (!drag) rng.value = T ? Math.round(t / T * 1000) : 0;
    tm.textContent = mmss(drag ? rng.value / 1000 * T : t) + ' / ' + mmss(T);
    pp.textContent = vPaused() ? '▶' : '❚❚'; pp.setAttribute('aria-label', vPaused() ? 'Play' : 'Pause');
  };
  const cb = k => {
    mark(k); lis.classList.toggle('on', !!k); lis.textContent = k ? '■ Stop' : '▶ Listen';
    bar.hidden = !k; clearInterval(tick); if (k) { draw(); tick = setInterval(draw, 250); }
  };
  const go = async list => {
    if (vNow()) { vStop(); return; }
    const ok = await vPlay(c.deck, list, cb);
    if (!ok) strip.querySelector('.vmsg').textContent = 'no voice yet · make it on the deck page';
  };
  lis.onclick = () => go(show);
  strip.querySelectorAll('[data-vk]').forEach(b => b.onclick = () => { const i = show.findIndex(p => p.k === b.dataset.vk); vStop(); go(show.slice(i)); });
  strip.querySelectorAll('[data-vs]').forEach(b => b.onclick = () => { const v = Math.round(Math.min(2, Math.max(0.8, vSpeed() + 0.1 * +b.dataset.vs)) * 10) / 10; vSetSpeed(v); strip.querySelector('.vspd b').textContent = v.toFixed(1) + '×'; });
  bar.querySelectorAll('[data-vj]').forEach(b => b.onclick = () => { vSkip(+b.dataset.vj); draw(); });
  pp.onclick = () => { if (vPaused()) vResume(); else vPause(); draw(); };
  rng.addEventListener('input', () => { drag = true; draw(); });
  rng.addEventListener('change', () => { vSeek(rng.value / 1000 * vTotal()); drag = false; draw(); });
  deckIndex(c.deck).then(() => {
    if (!strip.isConnected) return;
    const have = show.filter(p => hasClip(c.deck, p)).length;
    strip.querySelectorAll('[data-vk]').forEach(b => b.classList.toggle('none', !hasClip(c.deck, show.find(p => p.k === b.dataset.vk))));
    strip.classList.toggle('empty', !have);
    if (!have) strip.querySelector('.vmsg').textContent = 'no voice yet';
  });
}
/* ---------- QBank/GT layer (data/qbank.json): shown beside the card, never written into it ---------- */
function qbChips(c) {
  if (c.vcard) return `<span class="qc qc-viva mono">VIVA</span><span class="qc qc-tier mono">Tier ${esc(c.tier)}</span>`;
  if (c.topup) { const h = hitsOf(c).h; return `<span class="qc qc-top mono">Top-up</span><span class="qc qc-tier mono">Tier ${c.tier}${c.nq ? ' · ' + c.nq + ' Qs' : ''}</span>${[['marrow', 'Marrow'], ['doct', 'DocT'], ['gt', 'DocT GT']].filter(([k]) => h.has(k)).map(([k, t]) => `<span class="qc qc-${k} mono">${t}</span>`).join('')}`; }
  if (c.tdeck) { const h = hitsOf(c).h; return `<span class="qc qc-top mono">Top-up deck</span>${[['marrow', 'Marrow'], ['doct', 'DocT'], ['gt', 'DocT GT']].filter(([k]) => h.has(k)).map(([k, t]) => `<span class="qc qc-${k} mono">${t}</span>`).join('')}`; }
  const q = qbOf(c);
  if (!q || !q.chips) return '';
  return q.chips.filter(x => x.k !== 'recall').map(x => `<span class="qc qc-${x.k} mono" title="${x.n} question${x.n > 1 ? 's' : ''}">${esc(x.t)}${x.n > 1 ? ' ×' + x.n : ''}</span>`).join('');
}
const bankLine = l => { const m = l.match(/^([A-Za-z0-9 +·]{2,40}?):\s+(.*)$/s); return m ? `<p><b class="bk">${esc(m[1])}</b> ${inline(m[2])}</p>` : `<p>${inline(l)}</p>`; };
// T-095: in a viva walk, the package's one-liners for this card and the bridge to the next card
function vivaAns(c) {
  if (!flow || !flow.viva) return '';
  const ls = vivaLines(c), br = c.vq && c.vq.bridge;
  return (ls.length ? `<div class="box vlines"><span class="mono">VIVA</span><div class="bx">${ls.map(l => `<p>${inline(l)}</p>`).join('')}</div></div>` : '')
    + (br ? `<p class="vbridge">${inline(br)}</p>` : '');
}
function qbBoxes(c) {
  if (c.tdeck || c.topup || c.vcard) { const src = c.src || ''; return src ? `<p class="qsrc-card mono">From: ${esc(src)}</p>` : ''; }
  const q = qbOf(c);
  if (!q) return '';
  let h = '';
  // folded by default (4 Nov): the exam add-ons open only when tapped, so the card itself reads as a card
  if (q.lines && q.lines.length) h += `<details class="box qlines qfold"><summary class="mono">TOP-UP LINES · ${q.lines.length} <span class="qf-hint">tap to open</span></summary><div class="bx">${q.lines.map(bankLine).join('')}</div></details>`;
  if (q.cross && q.cross.length) h += `<details class="box qcross qfold"><summary class="mono">CROSSFIRE · ${q.cross.length} <span class="qf-hint">tap to open</span></summary><div class="bx">${q.cross.map(l => `<p>${inline(l)}</p>`).join('')}</div></details>`;
  return h;
}
function qbFix(c) {
  const q = qbOf(c), x = xOf(c);
  const bank = q && q.fix && q.fix.length ? q.fix.map(f => `<p>${inline(f.t)}</p>${f.src ? `<p class="qsrc">${f.url ? `<a href="${esc(f.url)}" target="_blank" rel="noopener">${esc(f.src)}</a>` : esc(f.src)}</p>` : ''}`).join('') : '';
  // T-084: corrections found while writing and checking the explanations (approved by Naven); the card text stays as it was
  const xf = x && x.fix && x.fix.length ? x.fix.map(([a, b]) => `<p><span class="qwas">Card: ${inline(a)}</span> → <b>${inline(b)}</b></p>`).join('') : '';
  if (!bank && !xf) return '';
  return `<div class="box qfix"><span class="mono">CORRECTION · CHECKED</span><div class="bx">${bank}${xf}</div></div>`;
}
async function saveHook(c, v) {
  const e = S.edits.get(c.deck + '|' + c.code);
  await saveEdit(c, { ...((e && e.fields) || {}), hook: v });
  const i = flow && flow.queue.findIndex(x => x.code === c.code && x.deck === c.deck);
  if (flow && i >= 0) flow.queue[i] = { ...flow.queue[i], hook: v, edited: true };
}

// the top bar never pushes ⚙ off screen: first the button labels go, then the pen tools take their own row
function fitBar() {
  const b = $('.f-bar'); if (!b) return;
  // the pinned pen tools keep the width they have when open, folded or not, so nothing else ever moves
  const dk = b.querySelector('.ik-dock');
  if (dk) { const bar = dk.querySelector('.ik-bar'); if (bar) { const w = Math.ceil(bar.getBoundingClientRect().width); if (w > 60) try { localStorage.setItem('trace.ink.dockw', w); } catch (e) { /* */ } }
    let w2 = 510; try { w2 = +(localStorage.getItem('trace.ink.dockw') || 510); } catch (e) { /* */ } dk.style.minWidth = Math.min(w2, innerWidth - 24) + 'px'; }
  // one row when it fits; otherwise row 1 = title, progress, time, ⚙ and row 2 = Back, Undo, Pause, Going out, pen tools
  b.classList.remove('tight', 'tworow');
  const over = () => b.scrollWidth > b.clientWidth + 1;
  if (over()) b.classList.add('tworow');
  const row2 = [...b.querySelectorAll('#f-peek, #f-undo, #f-pause, .goout, .ik-dock')];
  if (b.classList.contains('tworow') && row2.some(x => x.getBoundingClientRect().right > innerWidth - 4)) b.classList.add('tight');
}
if (!window.__fitBar) { window.__fitBar = 1; addEventListener('resize', () => fitBar()); }
function updateClock() {
  if (!flow) return;
  const t = $('#f-time'); if (t) t.textContent = clock(((flow.pausedAt || Date.now()) - flow.t0) / 1000);
  // T-141: the day plan in the bar: this block's end, time left, breaks earned (worked out every 20 s)
  const fd = $('#f-day');
  if (fd && (!flow.dayT || Date.now() - flow.dayT > 20000)) {
    flow.dayT = Date.now();
    try { const n = DAYP.nowInfo(), b = DAYP.bank(); fd.innerHTML = (n.sessionEnd != null ? `until ${DAYP.hm(n.sessionEnd)} · <b>${DAYP.dur(n.left)}</b> left` : n.cur ? esc(DAYP.typeName(n.cur.type)) + ' now' : n.next ? 'next ' + esc(DAYP.typeName(n.next.type)) + ' ' + DAYP.hm(n.next.a) : '') + (b.left >= 1 ? ` · break ${Math.floor(b.left)}m earned` : ''); } catch (e) { fd.textContent = ''; }
  }
  // T-138: in a viva walk, this step's time (card or lesson) and this question's time, both running
  const stp = $('#f-stp'); if (!stp) return;
  const now = flow.pausedAt || Date.now(), L = flow.look ? flow.lookStep : flow.st && flow.st.s;
  const lab = !L ? 'STEP' : L.kind === 'card' ? 'CARD' : L.kind === 'spine' ? 'SPINE' : 'LESSON';
  const stepMs = flow.look ? now - (flow.lookT0 || now) : flow.st ? now - flow.st.t0 : 0;
  $('#f-stl').textContent = (flow.look ? 'LOOK · ' : '') + lab; stp.textContent = clock(Math.max(0, stepMs) / 1000);
  if (L && L.q) { const k = L.pkg + '|' + L.q; $('#f-ql').textContent = 'Q' + qNumOf(L.pkg, L.q); $('#f-qt').textContent = clock(Math.max(0, (flow.qms[k] || 0) + stepMs) / 1000); }
}
// Today's thread: one bead per card walked today, against today's planned number. Read by lightness and shape, never by
// hue alone: new = light, ×2 = mid, ×3+ = dark, repair = ring; beads past the target carry a gold edge; at the target
// the whole thread is sealed in gold.
function dayGoal() { const st = currentStretch(); if (st) { const r = compute(st); if (r.active && r.todayPlan) return { n: r.todayPlan, st, r }; } return { n: P.get('dayGoal', 65) }; }
function drawThread() {
  const el = $('#f-thread'); if (!el) return;
  const vth = flow && flow.viva && !flow.browse;
  if (vth && P.get('vthread', 'viva') !== 'day') return drawVivaThread(el);
  const beads = todayBeads(), g = dayGoal(), n = g.n, done = beads.length;
  const td = today(), a = winStart(td), b = winEnd(td), f = Math.min(1, Math.max(0, (Date.now() - a) / (b - a)));
  const should = Math.round(n * f), diff = done - should, sealed = done >= n;
  const slots = Math.max(n, done);
  let h = '';
  for (let i = 0; i < slots; i++) h += `<i class="bd${i < done ? ' ' + beads[i] : ''}${i >= n ? ' ex' : ''}${i === should - 1 && !sealed ? ' now' : ''}"></i>`;
  const parts = g.st ? todayParts(g.st, g.r) : [];
  el.className = 'thread' + (sealed ? ' sealed' : '');
  el.innerHTML = `<div class="th-h mono"><span>TODAY’S THREAD</span><span><b>${done}</b> / ${n}${sealed ? ' · <b class="gold">day sealed</b>' : f > 0 && f < 1 ? ` · ${diff >= 0 ? `<b class="ahead">${diff} ahead</b>` : `<b class="behind">${-diff} behind</b>`}` : ''}</span></div>
    <div class="th-b" style="--n:${slots}">${h}</div>
    ${parts.length ? `<div class="th-p mono"><span>From the plan</span> · ${parts.map(x => `${esc(x.name)} ${x.done}/${x.n}`).join(' · ')}</div>` : ''}`;
  if (vth) { el.querySelector('.th-h').insertAdjacentHTML('beforeend', '<button class="th-sw mono" data-vth="viva">Viva plan</button>'); bindThreadSw(el); }
}
function bindThreadSw(el) { el.querySelectorAll('[data-vth]').forEach(b => b.onclick = e => { e.stopPropagation(); P.set('vthread', b.dataset.vth); drawThread(); }); }
/* T-138: in a viva walk the thread is today's viva plan: its questions laid out from the start (the chase), each filling in
   as you finish it (the build-up); questions past the plan go after a "beyond plan" mark. No plan for today: the questions
   finished today, as they come. One tap switches to the day's card thread. */
function drawVivaThread(el) {
  const pkg = flow.viva, v = vivaPlanToday(pkg), P2 = vivaPkg(pkg); if (!P2) return;
  const cur = flow.look ? flow.lookStep : liveStep(), curQ = cur && cur.q;
  const doneQ = q => vivaDoneToday(pkg, q), mk = q => (flow.vm ? vivaLast(flow.vm, pkg, q) : '') || 'none';
  const todayDone = P2.questions.map(x => x.q).filter(doneQ);
  let frame, extra = [];
  if (v) { frame = v.todayQs; extra = todayDone.filter(q => !frame.includes(q)); if (curQ && !frame.includes(curQ) && !extra.includes(curQ)) extra.push(curQ); }
  else frame = todayDone.concat(curQ && !todayDone.includes(curQ) ? [curQ] : []);
  const bead = q => `<i class="bd vb${doneQ(q) ? ' vdone vm-' + mk(q) : ''}${q === curQ ? ' now' : ''}" title="Q${qNumOf(pkg, q)}"><b class="mono">${qNumOf(pkg, q)}</b></i>`;
  const n = frame.length, done = frame.filter(doneQ).length;
  const td = today(), a = winStart(td), b = winEnd(td), f = Math.min(1, Math.max(0, (Date.now() - a) / (b - a)));
  const should = Math.round(n * f), diff = done + extra.filter(doneQ).length - should, sealed = v && done >= n;
  el.className = 'thread vthread' + (sealed ? ' sealed' : '');
  el.innerHTML = `<div class="th-h mono"><span>${v ? 'VIVA PLAN' : 'THIS WALK'} · ${esc(pkg)}</span><span>${v ? `<b>${done}</b> / ${n} questions${sealed ? ' · <b class="gold">done for today</b>' : f > 0 && f < 1 ? ` · ${diff >= 0 ? `<b class="ahead">${diff} ahead</b>` : `<b class="behind">${-diff} behind</b>`}` : ''}` : `<b>${todayDone.length}</b> question${todayDone.length === 1 ? '' : 's'} today · no viva plan for today`}</span><button class="th-sw mono" data-vth="day">Day thread</button></div>
    <div class="th-b vth-b">${frame.map(bead).join('')}${extra.length ? `<span class="vth-x mono">beyond plan</span>${extra.map(bead).join('')}` : ''}</div>`;
  bindThreadSw(el);
}
function updateFlowChrome() {
  if (!flow || !$('#f-ring')) return;
  noteStep(); setTimeout(() => DESK.pushDesk(false), 0);
  const total = flow.queue.length, step = Math.min(total, flow.idx + (flow.done ? 0 : 1));
  const circ = 2 * Math.PI * 22;
  if ($('.flow.v3')) { $('#f-ring').innerHTML = ''; const fc = $('#f-cnt'); if (fc) fc.innerHTML = `<b>${step}</b>/${total}`; }
  else $('#f-ring').innerHTML = `<svg viewBox="0 0 52 52"><circle cx="26" cy="26" r="22" class="r0"/><circle cx="26" cy="26" r="22" class="r1" stroke-dasharray="${(circ * step / total).toFixed(1)} ${circ.toFixed(1)}" transform="rotate(-90 26 26)"/></svg><span>${step}/${total}</span>`;
  $('#f-sec').textContent = flow.done ? 'Done' : sectionRange();
  fitBar();
  drawThread();
  const fl = $('#f-live');
  if (fl) { try { const c = chase(P.get('chasePool', 'all')), lp = livePace(c); fl.innerHTML = lp.before || lp.after ? `Today ${c.doneToday} / ${c.requiredToday} new` : `Today ${c.doneToday} / ${c.requiredToday} new · ${lp.diff >= 0 ? `<b class="ahead">▲ ${lp.diff}</b>` : `<b class="behind">▼ ${-lp.diff}</b>`}${lp.perHour != null ? ' · ' + lp.perHour + '/h needed' : ''}`; } catch (e) { fl.textContent = ''; } }
  const cc = !flow.done && current(), cm = cc ? deckMeta(cc.deck) || {} : {};
  $('#f-kick').textContent = (flow.browse ? 'LOOK · ' : 'FLOW · ') + (cc ? cc.deck : flow.deck) + (cm.star ? ' · ✦ ' + cm.star : '');
  const fl2 = $('#f-lab'); if (fl2) { const lb = flow.label && flow.label !== 'Look' ? flow.label.toUpperCase() : ''; fl2.textContent = lb || 'THIS FLOW'; fl2.classList.toggle('chip-lab', !!lb); }
  $('#f-sub').textContent = cm.title || '';
  const n = flow.times.length;
  const mine = n ? flow.times.reduce((a, b) => a + b, 0) / n : 0;
  const avg = avgPace();
  $('#f-pace').textContent = n ? fmtDur(mine / 1000) : '–';
  if (n && avg) {
    const d = Math.round((mine - avg) / 1000);
    $('#f-diff').innerHTML = `${fmtDur(Math.abs(d))} <span class="gold">${d < 0 ? '↓' : d > 0 ? '↑' : '='}</span> <small>avg</small>`;
  } else $('#f-diff').textContent = '–';
  $('#f-undo').classList.toggle('dimmed', flow.browse ? flow.idx === 0 : !flow.hist.length);
  const pkb = $('#f-peek'); if (pkb) pkb.classList.toggle('dimmed', !flow.hist.length || (flow.peek || 0) >= flow.hist.length);
  if (flow.viva && !flow.browse) { drawVivaTiles(); updateClock(); return; }
  const seenNow = new Set(flow.queue.slice(0, flow.idx).map(c => c.code));
  const w0 = Math.max(0, Math.min(flow.idx - 20, flow.queue.length - 60)), fq = flow.queue.slice(w0, w0 + 60);   // T-138: a window around where you are
  $('#f-tiles').innerHTML = fq.map((c, i0) => { const i = i0 + w0; return `<span data-ti="${i}" class="ft${i0 && (c.deck !== fq[i0 - 1].deck || chunkOf(c).key !== chunkOf(fq[i0 - 1]).key) ? ' cs' : ''} s${shade(seen(c.deck, c.no))}${c.topup || c.tdeck ? (seen(c.deck, c.no) ? ' tu tu1' : ' tu') : ''}${i === flow.idx && !flow.done ? ' cur' : ''}${seenNow.has(c.code) ? ' was' : ''}${flow.peek && flow.hist[flow.hist.length - flow.peek] && flow.hist[flow.hist.length - flow.peek].idx === i ? ' look' : ''}"><b>${c.no}</b><i>×${seen(c.deck, c.no)}</i></span>`; }).join('');
}
// T-138: the viva walk's tiles, question by question: O opening lesson · 1…n cards · C closing lesson · S spine
// the walk's tiles as data (used by the strip here and by the phone Desk)
function vivaTileData() {
  const steps = vivaSteps(), live = stepKey(liveStep()), done = new Set(flow.trail.map(stepKey));
  const ck = i => { const c = flow.queue[i]; return c ? c.deck + '|' + c.code : ''; };
  const walkedK = new Set(flow.trail.filter(x => x.kind === 'card').map(x => ck(x.idx)));   // a card done once lights up wherever it comes again
  const look = flow.look ? stepKey(flow.trail[liveAt() - flow.look]) : '';
  const groups = []; let g = null;
  for (const s of steps) {
    const q = s.q || ''; if (!g || g.q !== q || s.kind === 'vq') { g = { q, pkg: s.pkg, qn: qNumOf(s.pkg, s.q), steps: [] }; groups.push(g); }
    const k = stepKey(s);
    g.steps.push({ ...s, k, lab: s.kind === 'vq' ? 'O' : s.kind === 'vclose' ? 'C' : s.kind === 'spine' ? 'S' : String(s.n || ''), st: k === live && !flow.done ? 'cur' : done.has(k) ? 'vdone' : s.kind === 'card' && walkedK.has(ck(s.idx)) ? 'vseen' : 'vahead', look: k === look });
  }
  let gi = groups.findIndex(x => x.steps.some(s => s.k === (look || live)));
  if (gi < 0) gi = flow.done ? groups.length - 1 : 0;
  return { groups, gi };
}
function drawVivaTiles() {
  const { groups, gi } = vivaTileData();
  const a = Math.max(0, gi - 2), b = Math.min(groups.length, a + 8);
  const tile = s => `<span data-sk="${s.k}" class="ft vt-${s.kind} ${s.st}${s.look ? ' look' : ''}${s.rep ? ' vrep' : ''}" title="${esc(s.kind === 'vq' ? 'Opening lesson' : s.kind === 'vclose' ? 'Closing lesson' : s.kind === 'spine' ? 'Spine' : 'Card ' + s.n)}"><b>${s.lab}</b></span>`;
  $('#f-tiles').innerHTML = (a ? '<span class="vg-more mono">…</span>' : '') + groups.slice(a, b).map((x, j) => `<span class="vg${a + j === gi ? ' on' : ''}"><span class="vg-n mono">Q${x.qn}</span>${x.steps.map(tile).join('')}</span>`).join('') + (b < groups.length ? '<span class="vg-more mono">…</span>' : '');
  const cur = groups[gi], P2 = cur && vivaPkg(cur.pkg), qn = cur ? cur.qn : 0;
  const cards = flow.queue.length, cardAt = Math.min(cards, flow.idx + (flow.done ? 0 : 1));
  const fc = $('#f-cnt'); if (fc) fc.innerHTML = `Q <b>${qn}</b>/${P2 ? P2.questions.length : '–'} · card ${cardAt}/${cards}`;
}

function animate(kind, swap) {
  const el = $('#card');
  flow.busy = true;
  if (flow && flow.turnAxis === 'y' && kind !== 'flip') kind = kind === 'back' ? 'down' : 'up';
  const out = { flip: 'anim-flip-out', back: 'anim-back-out', up: 'anim-up-out', down: 'anim-down-out' }[kind] || 'anim-deal-out';
  const inn = { flip: 'anim-flip-in', back: 'anim-back-in', up: 'anim-up-in', down: 'anim-down-in' }[kind] || 'anim-deal-in';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) { swap(); flow.busy = false; return; }
  el.classList.add(out);
  setTimeout(() => {
    el.classList.remove(out);
    swap();
    el.classList.add(inn);
    setTimeout(() => { el.classList.remove(inn); if (flow) flow.busy = false; }, kind === 'flip' ? 230 : 320);
  }, kind === 'flip' ? 170 : 230);
}
function reveal() {
  if (flow && flow.pausedAt) return;
  if (flow && (flow.look || flow.peek)) return backToNow();
  if (flow && flow.inter) return clearInter();
  if (!flow || flow.busy || flow.face !== 'q' || flow.done) return;
  animate('flip', () => { flow.face = 'a'; drawCard(); });
}
async function next(again) {
  if (flow && flow.pausedAt) return;                 // T-138: nothing moves on while paused or out on a break
  if (flow && (flow.look || flow.peek)) return backToNow();
  if (flow && flow.inter) return clearInter();
  if (!flow || flow.busy || flow.done) return;
  if (flow.face === 'q') return reveal();
  if (flow.pilot && !flow.pilotSent) {                  // the one reviewed card of this pilot session (not logged anywhere)
    flow.pilotSent = true;
    const c = current(), m = deckMeta(c.deck) || {};
    sendRequest(c, m.title, (Date.now() - flow.cardT0) / 1000, false);
  }
  if (flow.browse) {
    animate('deal', () => { flow.idx++; flow.face = 'q'; if (flow.idx >= flow.queue.length) flow.done = true; drawCard(); updateFlowChrome(); });
    return;
  }
  const c = current(), ms = Math.max(0, Date.now() - flow.cardT0);
  const hk = $('#hook'); if (hk && hk.value.trim() !== (c.hook || '')) await saveHook(c, hk.value.trim());
  // T-095: a card already walked under an earlier question of this viva is not counted a second time
  const rep = !!(c.vq && (c.vq.rep || flow.queue.slice(0, flow.idx).some(x => x.deck === c.deck && x.code === c.code)));
  const ev = rep ? null : await recordView({ id: uid('e'), ts: Date.now(), deck: c.deck, code: c.code, no: c.no, ms, again: !!again, session: flow.session });
  flow.hist.push({ idx: flow.idx, ev, appended: !!again, cardT0: flow.cardT0 });
  if (!rep) flow.times.push(ms);
  if (again) flow.queue.push({ ...c, vq: c.vq ? { ...c.vq, bridge: null, again: true } : undefined });
  if (c.vq && !c.vq.again && c.vq.i === c.vq.n - 1) flow.pendingSpine = { pkg: c.vq.pkg, q: c.vq.q, idx: flow.idx };
  // the last card of a deck in this flow: its deck close comes next (once)
  flow.closeSeen = flow.closeSeen || {};
  if (!flow.viva && closeOf(c.deck) && !flow.closeSeen[c.deck] && !flow.queue.slice(flow.idx + 1).some(x => x.deck === c.deck)) { flow.closeSeen[c.deck] = 1; flow.pendingClose = c.deck; }
  animate('deal', () => {
    if (flow.pendingClose) { flow.inter = { kind: 'close', deck: flow.pendingClose }; flow.pendingClose = null; }
    if (flow.pendingSpine) { flow.inter = { kind: lessonOf(flow.pendingSpine.pkg, flow.pendingSpine.q, 'c') ? 'vclose' : 'spine', ...flow.pendingSpine }; flow.pendingSpine = null; }
    flow.idx++;
    flow.face = 'q';
    flow.cardT0 = Date.now();
    if (flow.idx >= flow.queue.length) flow.done = true;
    else if (!flow.viva) { const nc = flow.queue[flow.idx]; if (nc.deck !== c.deck || chunkOf(nc).key !== chunkOf(c).key) setTimeout(checkBreakDue, 400); }
    saveLastFlow();
    drawCard(); updateFlowChrome();
  });
}
async function undo() {
  if (flow && flow.look) lookSet(0);
  if (flow && flow.peek) { flow.peek = 0; flow.peekT0 = null; }
  if (flow && flow.browse) { if (flow.busy || flow.idx === 0) return; animate('back', () => { flow.idx--; flow.face = 'q'; flow.done = false; drawCard(); updateFlowChrome(); }); return; }
  if (!flow || flow.busy || !flow.hist.length) return;
  const h = flow.hist.pop();
  closeStep();
  // T-138: the steps after this card go too (it becomes the step you are on again)
  if (flow.trail) { let p = -1; for (let j = flow.trail.length - 1; j >= 0; j--) if (flow.trail[j].kind === 'card' && flow.trail[j].idx === h.idx) { p = j; break; } if (p >= 0) flow.trail.length = p + 1; }
  flow.inter = null;
  if (h.ev) await undoView(h.ev);
  if (h.appended) flow.queue.pop();
  if (h.ev) flow.times.pop();
  flow.idx = h.idx; flow.face = 'q'; flow.done = false; flow.cardT0 = Date.now();
  drawCard(); updateFlowChrome();
}
/* ============ Journal Flow-message pilot (TEST build only) ============ */
function startPilot() {
  if (!pilotAllowed()) { go('#/'); return; }
  // an explicit, isolated session: look-mode Flow (nothing logged), starting at GI02B PANC-14 when it is on this device
  const pick = (cardsOf('GI02B') || []).length ? 'GI02B' : (S.library && S.library.decks.find(d => isReady(d.deck)) || {}).deck;
  const cards = pick ? cardsOf(pick) : [];
  if (!cards.length) { toast('No downloaded deck for the pilot yet.'); go('#/'); return; }
  const at = Math.max(0, cards.findIndex(c => c.code === 'PANC-14'));
  startFlow(cards, { browse: true, pilot: true, start: at, label: 'Journal pilot', returnTo: '#/' });
  resumePending(drawFm).then(resumed => { if (resumed && flow) { flow.pilotSent = true; } drawFm(); });
}
function drawFm() {
  const slot = document.getElementById('fm-slot'); if (!slot || !flow || !flow.pilot) return;
  const st = FM.state, about = FM.card ? ` · on ${esc(FM.card)}` : '';
  if (st === 'idle') { slot.innerHTML = '<p class="fm-hint mono">JOURNAL PILOT · reveal a card, then tap Next once</p>'; return; }
  if (FM.dismissed) { slot.innerHTML = ''; return; }
  if (st === 'reply') {
    if (slot.querySelector('.fm-note[data-id="' + FM.requestId + '"]')) return;       // one appearance per reply
    slot.innerHTML = `<div class="fm-note" data-id="${esc(FM.requestId)}" role="status">
      <div class="fm-h"><span class="mono">✦ JOURNAL${about}</span><button class="fm-x" aria-label="Dismiss">×</button></div>
      <p class="fm-t"></p><button class="fm-more" hidden>Read more</button></div>`;
    const t = slot.querySelector('.fm-t'); t.textContent = FM.text;                 // plain text only
    requestAnimationFrame(() => { const more = slot.querySelector('.fm-more'); if (t.scrollHeight > t.clientHeight + 2) { more.hidden = false; more.onclick = () => { t.classList.add('open'); more.remove(); }; } });
  } else {
    const end = st === 'timeout' || st === 'error' || st === 'invalid';
    slot.innerHTML = `<div class="fm-wait${end ? ' end' : ''}" role="status"><span class="mono">${end ? '✦' : '<i class="fm-dot"></i>'} ${esc(FM.note || 'Asking Journal…')}</span>${FM.wake && !end ? `<span class="mono fm-wake">${esc(FM.wake)}</span>` : ''}
      ${end ? '<a class="fm-new" href="#/" data-fmnew>New pilot session</a>' : ''}<button class="fm-x" aria-label="Dismiss">×</button></div>`;
    const nw = slot.querySelector('[data-fmnew]'); if (nw) nw.onclick = e => { e.preventDefault(); endFlow().then(() => setTimeout(() => go('#/pilot'), 50)); };
  }
  const x = slot.querySelector('.fm-x'); if (x) x.onclick = () => { FM.dismissed = true; slot.innerHTML = ''; };
}

/* the visual panel: beside the card on wide screens, over it on the phone */
let vstate = null;
function openPanel(o) {
  vstate = { deck: o.deck, code: o.code, stack: o.ov ? [{ ov: o.ov }] : [{ seq: o.seq, i: 0 }] };
  let host = $('#vpanel');
  if (!host) { host = document.createElement('aside'); host.id = 'vpanel'; host.className = 'vpanel'; $('.screen.flow').appendChild(host); }
  $('.screen.flow').classList.add('vp-open');
  drawPanel(host, vstate, { P, onClose: closePanel });
}
function closePanel() {
  vstate = null;
  const h = $('#vpanel'); if (h) h.remove();
  const f = $('.screen.flow'); if (f) f.classList.remove('vp-open');
}
function flowKeys(e) {
  if (!flow || e.target.matches('input, textarea')) return;
  if ($('.modal')) return;
  if (vstate) {
    if (e.key === 'Escape') { e.preventDefault(); closePanel(); return; }
    if (panelKey(vstate, e)) { drawPanel($('#vpanel'), vstate, { P, onClose: closePanel }); return; }
  }
  if (flow.userPause) { if (e.key === ' ' || e.key === 'p' || e.key === 'P') { e.preventDefault(); togglePause(); } return; }
  if (e.key === 'p' || e.key === 'P') { if (!flow.browse) { e.preventDefault(); togglePause(); } return; }
  if (flow.peek && (e.key === ' ' || e.key === 'Enter' || e.key === 'ArrowRight')) { e.preventDefault(); peekForward(e.key !== 'ArrowRight'); return; }
  if (e.key === ' ' || e.key === 'Enter' || e.key === 'ArrowRight') { e.preventDefault(); flow.inter ? clearInter() : flow.done ? endFlow() : flow.face === 'q' ? reveal() : next(false); }
  else if (e.key === 'ArrowLeft') { if (flow.browse) undo(); else peekBack(); }
  else if (e.key === 'q' || e.key === 'Q') { if (flow.face === 'a' && !flow.peek) { e.preventDefault(); leftAction(); } }
  else if (e.key === 'a' || e.key === 'A') { if (flow.face === 'a' && !flow.browse) next(true); }
  else if (e.key === 'u' || e.key === 'U' || e.key === 'Backspace' || (e.key === 'z' && (e.metaKey || e.ctrlKey))) { e.preventDefault(); undo(); }
  else if (e.key === 'e' || e.key === 'E') { if (flow.face === 'a') openEditor(current()); }
  else if (e.key === 'Escape') { if ($('.modal.endask')) $('.modal.endask').remove(); else askEnd(); }
}

/* ============================ editor ============================ */
function openEditor(c) {
  const orig = withFix((S.decks.get(c.deck) || { cards: [] }).cards.find(x => x.code === c.code) || c);
  const wrap = document.createElement('div');
  wrap.className = 'modal';
  const field = (k, label, rows) => `<label><span class="mono">${label}</span><textarea name="${k}" rows="${rows}">${esc(c[k] || '')}</textarea></label>`;
  wrap.innerHTML = `<div class="sheet" role="dialog" aria-label="Edit card ${esc(c.code)}">
    <div class="sheet-h"><span class="mono kick">EDIT · ${esc(c.deck)} · ${esc(c.code)}</span><button class="iconbtn" data-x aria-label="Close">${ICON.close}</button></div>
    <p class="muted small">Plain text with **bold**, *italic*, lines starting "- " for bullets, and "a | b" for table rows. Your edit is kept on this device and synced to Drive; the original stays untouched.</p>
    ${field('q', 'QUESTION', 4)}${field('a', 'ANSWER', 9)}${field('why', 'WHY', 3)}${field('watch', 'WATCH', 3)}
    <div class="sheet-f">${c.edited ? '<button class="btn ghost" data-reset>Back to original</button>' : '<span></span>'}<button class="btn primary" data-save>Save</button></div>
  </div>`;
  document.body.appendChild(wrap);
  const close = () => wrap.remove();
  wrap.querySelector('[data-x]').onclick = close;
  wrap.onclick = e => { if (e.target === wrap) close(); };
  wrap.querySelector('[data-save]').onclick = async () => {
    const fields = {};
    for (const k of ['q', 'a', 'why', 'watch']) { const v = wrap.querySelector(`[name=${k}]`).value; if (v !== (orig[k] || '')) fields[k] = v; }
    const prev = S.edits.get(c.deck + '|' + c.code);
    if (prev && prev.fields && prev.fields.hook != null) fields.hook = prev.fields.hook;
    await saveEdit(c, fields);
    refreshFlowCard(c);
    close(); toast('Saved. It syncs to Drive with your next sync.');
  };
  const rs = wrap.querySelector('[data-reset]');
  if (rs) rs.onclick = async () => { await resetEdit(c); refreshFlowCard(c); close(); toast('Back to the original card.'); };
}
function refreshFlowCard(c) {
  if (!flow) return;
  const fresh = cardsOf(c.deck).find(x => x.code === c.code);
  flow.queue = flow.queue.map(x => x.code === c.code && x.deck === c.deck ? fresh : x);
  drawCard();
}

/* ============================ status ============================ */
async function renderStatus() {
  const lib = S.library, total = lib ? lib.decks.length : 0;
  const ready = lib ? lib.decks.filter(d => isReady(d.deck)).length : 0;
  const cards = lib ? lib.decks.filter(d => isReady(d.deck)).reduce((a, d) => a + d.cards, 0) : 0;
  const persisted = navigator.storage && navigator.storage.persisted ? await navigator.storage.persisted() : false;
  const est = navigator.storage && navigator.storage.estimate ? await navigator.storage.estimate() : null;
  const last = (await db.kv.get('lastSync')) || status.last;
  const sw = 'serviceWorker' in navigator && navigator.serviceWorker.controller ? 'yes' : 'not yet (reload once)';
  const allReady = total && ready === total;
  app.innerHTML = `<div class="screen status">
    <header class="top"><a class="iconbtn" href="#/" aria-label="Back">${ICON.back}</a><span class="h2">This device</span><span></span></header>
    <div class="scroll pad">
      <div class="ready ${allReady && sw === 'yes' ? 'yes' : 'no'}"><span class="h2">${allReady && sw === 'yes' ? 'Ready offline' : 'Not fully offline yet'}</span>
        <span class="muted">${ready} of ${total} decks (${cards} cards) downloaded and checked${sw === 'yes' ? ' · app saved for offline use' : ' · app not yet saved for offline use'}.</span></div>
      <dl class="facts">
        <dt>Sync</dt><dd>${isDemo() ? 'Demo mode: nothing leaves this device' : esc(status.state === 'error' ? 'Problem: ' + status.error : status.state === 'syncing' ? 'Syncing now' : navigator.onLine ? 'Connected' : 'Offline')}</dd>
        <dt>Last sync</dt><dd>${last ? new Date(last).toLocaleString() : 'never'}</dd>
        <dt>Waiting to send</dt><dd>${status.pending} item${status.pending === 1 ? '' : 's'}</dd>
        <dt>Storage</dt><dd>${persisted ? 'Protected from clean-up' : 'Browser may clear it if space runs low'}${est ? ` · ${(est.usage / 1048576).toFixed(1)} MB used` : ''}</dd>
        <dt>Setup link</dt><dd>${hasBackend() && !isDemo() ? '<button class="link" data-act="copylink">Copy it, to connect another device</button><div id="setup-out" hidden><textarea class="mono" readonly rows="4"></textarea><span class="mono muted small so-n"></span></div>' : '—'}</dd>
        <dt>Reminders</dt><dd>${hasBackend() && !isDemo() ? '<button class="link" data-act="testrem">Send a test reminder (in 2 minutes)</button>' : '—'}</dd>
        <dt>Profile</dt><dd>${IS_HT ? 'HT' : 'Naven (Trace)'} · <button class="link" data-act="profile">switch to ${IS_HT ? 'Naven (Trace)' : 'HT'}</button></dd>
        <dt>Device</dt><dd class="mono">${esc(S.device)}</dd>
        <dt>App</dt><dd class="mono">${CONFIG.appVersion}</dd>
      </dl>
      <div class="row-btns">
        <button class="btn primary" data-act="sync" ${status.busy ? 'disabled' : ''}>Sync now</button>
        <button class="btn ghost" data-act="dl">Re-check all decks</button>
      </div>
      <div class="vstat"><span class="mono kick">VISUAL DECKS</span>
        ${V.packs.size ? `<ul>${[...V.packs.values()].map(p => `<li><b class="mono">${esc(p.deck)}</b> v${p.version} · ${p.scenes.length} scenes · checked ${new Date(p.checkedAt).toLocaleString()}</li>`).join('')}</ul>` : '<p class="muted small">None on this device yet.</p>'}
        ${Object.entries(V.status.problems || {}).map(([d, m]) => `<p class="vprob"><b class="mono">${esc(d === '*' ? 'Visual check' : d)}</b> ${esc(m)}${d === '*' ? '' : ' — keeping the previous accepted version.'}</p>`).join('')}
        <p class="muted small">${V.status.busy ? 'Checking now…' : V.status.checked ? 'Last checked ' + new Date(V.status.checked).toLocaleString() : 'Not checked yet'}</p>
        <button class="btn ghost" data-act="vis" ${V.status.busy ? 'disabled' : ''}>Check visual decks now</button></div>
      ${isDemo() ? '<p class="muted small">You are in demo mode with sample decks. <a href="./">Leave demo</a></p>' : ''}
    </div>
    ${nav('')}
  </div>`;
  bindGo();
  $('[data-act=sync]').onclick = () => sync();
  const cl = $('[data-act=copylink]');
  if (cl) cl.onclick = async () => {
    if (!confirmCopy()) return;
    const b = await db.kv.get('backend'); if (!b) return;
    const bu = b.url || b.u, bk = b.key || b.k;
    const enc = btoa(JSON.stringify({ u: bu, k: bk })).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
    const link = 'https://baabusumathi-debug.github.io/trace/#setup=' + enc;
    // shown on screen as well, so it can be checked by eye and selected by hand if the clipboard fails
    const box = document.getElementById('setup-out');
    if (box) { box.hidden = false; box.querySelector('textarea').value = link; box.querySelector('.so-n').textContent = `${link.length} characters · connection ${bu ? '✓' : '✗ no address'} · key ${bk ? '✓' : '✗ missing'}`; }
    try { await navigator.clipboard.writeText(link); toast('Setup link copied (' + link.length + ' characters). Keep it private.'); }
    catch (e) { toast('Select the link in the box and copy it by hand.'); }
  };
  const tr = $('[data-act=testrem]');
  if (tr) tr.onclick = async () => {
    tr.disabled = true;
    try {
      const [r] = await batch([{ op: 'calendar', action: 'add', who: IS_HT ? 'HT' : 'Trace', at: new Date(Date.now() + 2 * 60000).toISOString(), title: 'Trace · test reminder', note: 'Sent from This device to check reminders.' }]);
      if (r.ok) toast('Added to the "' + r.data.calendar + '" calendar for ' + new Date(Date.now() + 2 * 60000).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) + '. Your phone should notify you then.');
      else toast(/unknown op/.test(r.error) ? 'The connection script needs the calendar update first.' : 'Reminder not added: ' + r.error);
    } catch (e) { toast('Reminder not added: ' + e.message); }
    tr.disabled = false;
  };
  const pf = $('[data-act=profile]');
  if (pf) pf.onclick = () => { if (confirmSwitch()) { setProfile(IS_HT ? 'trace' : 'ht'); location.reload(); } };
  $('[data-act=vis]').onclick = () => { if (window._vcheck) { window._vcheck(true); setTimeout(route, 300); } };
  $('[data-act=dl]').onclick = async () => {
    for (const d of S.decks.values()) d.verified = false;
    try { await downloadDecks(); toast('All decks downloaded and checked.'); } catch (e) { toast(e.message); }
    emit();
  };
}

/* ============================ changes ============================ */
function renderChanges() {
  const edits = [...S.edits.values()].filter(e => e.fields && Object.keys(e.fields).length).sort((a, b) => b.ts - a.ts);
  const libChanges = (S.library && S.library.changes) || [];
  app.innerHTML = `<div class="screen changes">
    <header class="top"><div class="brand">${brandMark()}<span class="brand-t"><span class="b1">TRACE</span><span class="b2">THE LEDGER</span></span></div>${syncPill()}</header>
    <div class="scroll pad">
      <div class="intro"><span class="kicker">THE LEDGER</span><h1>What changed.</h1><p class="muted">Edits Claude makes to your decks, and the edits you make here.</p></div>
      ${libChanges.length ? `<span class="mono kick">FROM CLAUDE</span><div class="ledger">${libChanges.map(c => `<div class="lg-i"><span class="mono tagc">${esc(c.kind || 'FIX')}</span><b>${esc(c.title)}</b><span class="muted">${esc(c.detail || '')}</span><span class="mono small muted">${esc(c.date || '')}</span></div>`).join('')}</div>` : ''}
      <span class="mono kick">YOUR EDITS</span>
      ${edits.length ? `<div class="ledger">${edits.map(e => `<button class="lg-i" data-deck="${esc(e.deck)}" data-code="${esc(e.code)}"><span class="mono tagc">${e.synced ? 'SYNCED' : 'ON DEVICE'}</span><b>${esc(e.deck)} · ${esc(e.code)}</b><span class="muted">${esc(Object.keys(e.fields).join(', '))} · ${new Date(e.ts).toLocaleString()}</span></button>`).join('')}</div>` : '<p class="muted">No edits yet. Open a card, reveal it and tap ✎.</p>'}
    </div>
    ${nav('changes')}
  </div>`;
  bindGo();
  app.querySelectorAll('[data-code]').forEach(b => b.onclick = () => {
    const cards = cardsOf(b.dataset.deck); const c = cards.find(x => x.code === b.dataset.code);
    if (c) startFlow([c], { browse: true, label: 'Edited', returnTo: '#/changes' });
  });
}

/* ============================ misc ============================ */
function bindGo() { app.querySelectorAll('[data-go]').forEach(b => b.onclick = () => go(b.dataset.go)); }
let toastT = null;
function toast(msg) {
  let t = $('#toast');
  if (!t) { t = document.createElement('div'); t.id = 'toast'; t.setAttribute('role', 'status'); document.body.appendChild(t); }
  t.textContent = msg; t.classList.add('show');
  clearTimeout(toastT); toastT = setTimeout(() => t.classList.remove('show'), 3800);
}
function registerSW() {
  if (!('serviceWorker' in navigator) || location.protocol === 'file:') return;
  navigator.serviceWorker.register('sw.js', { updateViaCache: 'none' }).then(reg => {
    // look for a new version every 10 minutes and whenever the app comes back to the front
    const check = () => reg.update().catch(() => {});
    setInterval(check, 10 * 60000);
    document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') check(); });
    reg.addEventListener('updatefound', () => {
      const nw = reg.installing;
      nw && nw.addEventListener('statechange', () => {
        if (nw.state === 'installed' && navigator.serviceWorker.controller) {
          const b = document.createElement('button');
          b.className = 'update'; b.textContent = 'A new version of Trace is ready. Tap to update.';
          b.onclick = () => { nw.postMessage('skip'); };
          document.body.appendChild(b);
        }
      });
    });
    let reloaded = false;
    const hadController = !!navigator.serviceWorker.controller;      // first install: no reload needed
    let pendingReload = false;
    navigator.serviceWorker.addEventListener('controllerchange', () => {
      if (!hadController || reloaded) return;
      if (flow) { pendingReload = true; return; }          // never interrupt a flow: reload after it ends
      reloaded = true; location.reload();
    });
    setInterval(() => { if (pendingReload && !flow && !reloaded) { reloaded = true; location.reload(); } }, 3000);
  }).catch(() => {});
}

// demo: seed the library from bundled files on first open
async function demoSeed() {
  if (!isDemo()) return;
  if (!S.library) await sync();
}
window.addEventListener('online', () => emit());
window.addEventListener('offline', () => emit());
boot().then(demoSeed).catch(e => { app.innerHTML = `<div class="screen pad"><h1>Trace could not start</h1><p>${esc(e.message)}</p></div>`; console.error(e); });
