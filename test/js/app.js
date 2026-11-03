import { CONFIG, CHANNEL, PROFILE, IS_HT, setProfile } from './config.js';
import { db, useDemoDb, useDbName, peekDb } from './db.js';
import { renderPalace, renderMeditation, stopMeditation, lastMeditation, TRACKS } from './palace.js';
import { initApi, hasBackend, isDemo, setBackend, call } from './api.js';
import { S, loadAll, emit, cardsOf, deckMeta, neetTag, qbOf, hitsOf, inPool, isNeet, POOLS, COMPONENTS, poolParts, togglePool, poolName, isTopupDeck, hasTopups, seen, walked, avgPace, tier, shade, systems, isReady, recount, lastSeen, deckLastTs, seenOn, daily, allDays, today, dkey, againList, chunkOf } from './store.js';
import { status, sync, loadQbank, startAutoSync, recordView, undoView, buildLogRows, saveEdit, resetEdit, uid, countPending, downloadDecks, deckState, addTarget, removeTarget, targetItems, compressNos } from './sync.js';
import { render, splitQ, plain, inline } from './md.js';
import { seal, emblem } from './emblems.js';
import { FM, pilotAllowed, resumePending, sendRequest, stopPolling } from './flowmsg.js';
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
      const b = await peekDb('trace', 'kv', 'backend').catch(() => null);
      if (b) { if (setProfile('trace')) { location.reload(); return; } }   // if storage is blocked, carry on as Trace
      else return renderProfilePick();
    }
    const base = CHANNEL === 'test' ? 'trace-test' : 'trace';
    // each profile keeps its own copy of everything; HT's is a separate database
    if (IS_HT || CHANNEL === 'test') useDbName(base + (IS_HT ? '-ht' : ''));
    if (!(await db.kv.get('backend'))) {        // borrow the connection already saved on this device, never study data
      for (const n of ['trace', 'trace-ht']) { const b = await peekDb(n, 'kv', 'backend').catch(() => null); if (b) { await db.kv.set('backend', b); break; } }
    }
    if (CHANNEL === 'test') document.documentElement.classList.add('ch-test');
    if (IS_HT) document.documentElement.classList.add('pf-ht');
  }
  await initApi(demo);

  // private setup link: #setup=<base64url {"u":..., "k":...}>
  if (!demo) await trySetup(location.href);
  if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(() => {});
  await loadAll();
  loadQbank();
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
  // visual decks: look for new versions a little after opening, then every 30 minutes (each check is skipped if done < 6 h ago)
  const vcheck = (force) => syncVisuals(d => (S.decks.get(d) || { cards: [] }).cards, { force }).then(() => { if (!flow && /^#\/status/.test(location.hash)) route(); });
  window._vcheck = vcheck;
  if (!IS_HT) { setTimeout(() => vcheck(false), 8000); setInterval(() => vcheck(false), 30 * 60000); }
}

// A two-tap switch (no browser dialog): the first tap arms it for 4 seconds.
let _pfArm = 0;
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
  if (page === 'status') return renderStatus();
  if (page === 'changes') return renderChanges();
  if (page === 'shelf') return renderCabinet();
  if (page === 'meditation') return renderMeditation(app, { nav: nav(''), back: '#/loft', P });
  if (page === 'pilot') return startPilot();
  renderPalace(app, { nav: nav('palace'), top: topBar() });
  bindGo();
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
  const m = String(text || '').match(/setup=([\w\-]+)/);
  if (!m) return false;
  try {
    let b = m[1].replace(/-/g, '+').replace(/_/g, '/');
    while (b.length % 4) b += '=';
    const j = JSON.parse(atob(b));
    if (!j.u || !j.k) throw new Error('incomplete link');
    await setBackend(j.u, j.k);
    await initApi(false);
    history.replaceState(null, '', location.pathname + '#/');
    toast('Connected to your Drive. Downloading your decks…');
    return true;
  } catch (e) { toast('That setup link did not work: ' + e.message); return false; }
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
function topBar() {
  return `<header class="top">
      <a class="brand" href="#/" aria-label="The palace">${brandMark()}<span class="brand-t"><span class="b1">TRACE${CHANNEL === 'test' ? ' <i class="testpill">TEST</i>' : ''}${IS_HT ? ' <i class="testpill htpill">HT</i>' : ''}</span><span class="b2">THE MAGICIAN’S CABINET</span></span></a>
      <div class="top-r">${syncPill()}<span class="exam mono"><span class="gold">${CONFIG.exam.name}</span>${daysLeft()}</span></div>
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
      <span class="back-foot mono"><span>${d.cards} CARDS${!d.topupDeck && hasTopups(d.deck) ? ' +' + S.qb.topups[d.deck].length + ' TU' : ''}</span><span>${d.topupDeck ? 'TOP-UP DECK' : ok ? TIER_NAME[t] : 'NOT DOWNLOADED'}</span></span>
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
  const tab = all ? 'mosaic' : P.get('sysTab', 'decks'), sort = P.get('sort', 'neet'), mp = P.get('moPool', 'all'), mst = P.get('moState', 'any');
  const hitN = d => pick2(d.deck, mp, mst).length, cn = P.get('cnames', false);
  const decks = sort === 'hits' ? s.decks.slice().sort((a, b) => hitN(b) - hitN(a) || a.deck.localeCompare(b.deck, undefined, { numeric: true })) : sortDecks(s.decks, sort);
  const stars = decks.reduce((t, d) => t + (d.star || 0), 0), cards = decks.reduce((t, d) => t + d.cards, 0), w = decks.reduce((t, d) => t + walked(d.deck), 0);
  let body, litList = [];
  if (tab === 'mosaic') {
    // lit cards in the order the mosaic shows them (Eagle view: system by system)
    const shown = all ? systems().flatMap(g => decks.filter(d => d.system === g.name)) : decks;
    litList = shown.flatMap(d => pick2(d.deck, mp, mst));
    body = `<div class="legend mono"><span>SEEN</span>${[0, 1, 2, 3].map(n => `<span class="lg s${n}">${n === 3 ? '3+' : n}</span>`).join('')}<span class="lg-n">gold ring = NEET</span><span class="lg-n"><i class="lg-tu"></i>coral corner = Top-up</span></div>
      ${poolChips(mp, 'data-mp')}
      <div class="chips mo-pools">${STATES.map(([k, l]) => `<button class="chip${mst === k ? ' on' : ''}" data-mst="${k}">${l}</button>`).join('')}<button class="chip dash${cn ? ' on' : ''}" data-cnames aria-pressed="${cn}">${cn ? '✓ ' : ''}Chunk names</button><span class="mono mo-sum">${decks.reduce((t, d) => t + hitN(d), 0)} of ${decks.reduce((t, d) => t + cardsOf(d.deck).length, 0)} cards lit</span></div>
      <div class="mosaic">${(all ? systems().map(g => ({ g, ds: decks.filter(d => d.system === g.name) })) : [{ g: null, ds: decks }]).map(({ g, ds }) => (g ? `<div class="mo-sys mono">${esc(g.label)} · ${ds.reduce((t, d) => t + hitN(d), 0)}</div>` : '') + ds.map(d => {
        const cs = cardsOf(d.deck), lit = c => inPool(c, mp) && inState(c, mst);
        return `<div class="mo-row${d.topupDeck ? ' tu' : ''}"><a class="mo-l mono" href="#/deck/${encodeURIComponent(d.deck)}"><b>${esc(d.deck)}</b><span>${d.topupDeck ? 'TOP-UP' : d.star ? '✦ ' + d.star : ''}${mp !== 'all' || mst !== 'any' ? ' · ' + hitN(d) : ''}</span></a>
          <span class="mo-cells${cn ? ' named' : ''}">${cs.length ? chunked(cs, c => `<button class="mo s${shade(seen(c.deck, c.no))}${isNeet(c) ? ' ng' : ''}${c.topup || c.tdeck ? (seen(c.deck, c.no) ? ' tu tu1' : ' tu') : ''}${lit(c) ? '' : ' off'}" data-deck="${esc(c.deck)}" data-code="${esc(c.code)}" data-tip="${esc(tipOf(c))}" aria-label="${esc(tipOf(c))}, seen ${seen(c.deck, c.no)}"></button>`, cn) : '<span class="muted small">not downloaded</span>'}</span></div>`;
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
    ${tab === 'mosaic' ? litBar(litList) : ''}
    ${nav('shelf')}
  </div>`;
  bindGo(); hideTip();
  if (tab === 'mosaic') {
    bindTips(app);
    const lab = (all ? 'All decks' : s.label) + ' · ' + [poolName(mp), mst !== 'any' ? stateLabel(mst) : ''].filter(Boolean).join(' · ');
    const lf = app.querySelector('[data-litflow]'), la = app.querySelector('[data-litadd]');
    if (lf) lf.onclick = () => { hideTip(); startFlow(litList, { label: lab, returnTo: location.hash }); };
    if (la) la.onclick = () => addLit(litList, lab);
    const cb = app.querySelector('[data-cnames]'); if (cb) cb.onclick = () => { P.set('cnames', !cn); keep(() => renderSystem(num)); };
  }
  app.querySelectorAll('[data-tab]').forEach(b => b.onclick = () => { P.set('sysTab', b.dataset.tab); renderSystem(num); });
  app.querySelectorAll('[data-sort]').forEach(b => b.onclick = () => { P.set('sort', b.dataset.sort); renderSystem(num); });
  app.querySelectorAll('[data-mp]').forEach(b => b.onclick = () => { P.set('moPool', togglePool(mp, b.dataset.mp)); renderSystem(num); });
  app.querySelectorAll('[data-mst]').forEach(b => b.onclick = () => { P.set('moState', b.dataset.mst); renderSystem(num); });
  app.querySelectorAll('.mo').forEach(b => b.onclick = () => {
    hideTip();
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
const tipOf = c => `${c.deck} · ${chunkOf(c).name} · card ${c.no}${neetTag(c) ? ' · ' + neetTag(c) : ''}${c.topup ? ' · Top-up' : ''}`;
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
  app.querySelectorAll('.tile').forEach(el => el.onclick = () => {
    const list = cur.list.find(c => c.code === el.dataset.code) ? cur.list : cards;
    startFlow(list, { browse: true, start: list.findIndex(c => c.code === el.dataset.code), label: 'Look', returnTo: location.hash });
  });
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
  P.set(LASTFLOW, { keys: flow.queue.map(c => c.deck + '|' + c.code), idx: flow.idx, label: flow.label, ts: Date.now() });
}
function lastFlowCards() {
  const lf = P.get(LASTFLOW, null);
  if (!lf || !lf.keys || Date.now() - lf.ts > 3 * 864e5) return null;
  const byDeck = new Map(), out = [];
  for (const k of lf.keys) {
    const i = k.indexOf('|'), deck = k.slice(0, i), code = k.slice(i + 1);
    if (!byDeck.has(deck)) byDeck.set(deck, new Map(cardsOf(deck).map(c => [c.code, c])));
    const c = byDeck.get(deck).get(code); if (c) out.push(c);
  }
  const left = out.slice(Math.min(lf.idx, out.length));
  return left.length ? { cards: left, done: out.length - left.length, total: out.length, label: lf.label, ts: lf.ts } : null;
}
function againCards() {
  return againList().map(a => { const cs = cardsOf(a.deck); return cs.find(c => c.code === a.code) || cs.find(c => c.no === a.no); }).filter(Boolean);
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
function renderFlowTab() {
  const draw = () => {
    const lf = lastFlowCards(), ag = againCards(), avg = avgPace() || 75000, mins = n => Math.max(1, Math.round(n * avg / 60000));
    const sys = systems();
    app.innerHTML = `<div class="screen flowtab">
      <header class="top col"><span class="mono kick">FLOW</span><span class="h1s">Today’s desk.</span></header>
      <div class="scroll pad desk">
        ${targetBlock(true)}
        <section class="dk-box">
          <div class="dk-h"><span><span class="mono kick">CONTINUE</span><span class="dk-t">${lf ? esc(lf.label || 'Last flow') : 'No flow left open'}</span></span>
            ${lf ? `<button class="pillbtn" data-cont>${ICON.walkS}Continue</button>` : ''}</div>
          <p class="muted small">${lf ? `${lf.done} of ${lf.total} done · ${lf.cards.length} left · ≈ ${mins(lf.cards.length)} min · stopped ${whenLabel(lf.ts)}` : 'A flow you leave before the end waits here for 3 days.'}</p>
        </section>
        <section class="dk-box">
          <div class="dk-h"><span><span class="mono kick">AGAIN PILE</span><span class="dk-t">${ag.length ? ag.length + ' card' + (ag.length === 1 ? '' : 's') + ' to repair' : 'Nothing to repair'}</span></span>
            ${ag.length ? `<button class="pillbtn" data-again>${ICON.walkS}Repair</button>` : ''}</div>
          ${ag.length ? `<div class="pl-strip">${ag.slice(0, 80).map(c => `<i class="s${shade(seen(c.deck, c.no))}${isNeet(c) ? ' ng' : ''}" data-tip="${esc(tipOf(c))}"></i>`).join('')}</div>` : ''}
          <p class="muted small">Cards you mark Again stay here until you walk them without Again in a later session. DocT test misses will land here too once the recorder link is built.</p>
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
    bindGo(); bindTarget(draw); hideTip(); bindTips(app);
    app.querySelectorAll('[data-mosaic]').forEach(a => a.addEventListener('click', () => P.set('sysTab', 'mosaic')));
    const c = app.querySelector('[data-cont]');
    if (c) c.onclick = () => startFlow(lf.cards, { label: lf.label || 'Continue', returnTo: '#/flow' });
    const r = app.querySelector('[data-again]');
    if (r) r.onclick = () => startFlow(ag, { label: 'Again pile', returnTo: '#/flow' });
  };
  draw();
}
function keep(fn) { const sc = app.querySelector('.scroll'), y = sc ? sc.scrollTop : 0; fn(); const s2 = app.querySelector('.scroll'); if (s2) s2.scrollTop = y; }

/* ============================ the Loft ============================ */
const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
let loftMonth = null, loftDay = null;
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
    ${dItems.length ? `<div class="chron">${dItems.map(c => `<div class="ch-i"><span class="mono">${esc(c.when.replace(/^(Today|Yday) /, ''))}</span><span>${esc(c.what)}</span><span class="mono">${esc(c.size)}</span></div>`).join('')}</div>` : '<p class="muted small">No study logged on this day.</p>'}
  </div>`;
  const d14 = lastDays(14), mx = Math.max(60, ...d14.map(d => daily(d).min));
  const bars = d14.map((d, i) => `<span style="height:${Math.max(2, Math.round(daily(d).min / mx * 66))}px" class="${i === 13 ? 'now' : ''}" title="${d}: ${fmtHM(daily(d).min)}"></span>`).join('');
  const avg14 = d14.reduce((a, d) => a + daily(d).min, 0) / 14;
  const totalCards = S.library ? S.library.decks.reduce((a, d) => a + d.cards, 0) : 0;
  const walkedNow = S.library ? S.library.decks.reduce((a, d) => a + walked(d.deck), 0) : 0;
  const cum = []; let run = 0;
  for (const d of lastDays(35)) { run += daily(d).cards; cum.push(run); }
  const scale = Math.max(1, run);
  const line = cum.map((v, i) => `${(i * 140 / 34).toFixed(1)} ${(66 - v / scale * 58).toFixed(1)}`).join(' L');
  const chron = buildChronicle();
  app.innerHTML = `<div class="screen loft">
    <header class="top"><a class="iconbtn" href="#/" aria-label="Back to the palace">${ICON.back}</a>
      <span class="tt"><span class="mono kick">${daysLeft()} · ${CONFIG.exam.name} 11 DEC</span><span class="h1s">The Loft</span></span><span></span></header>
    <div class="scroll pad loftbody">
      <div class="loft-a">
        ${targetBlock(false)}
        <div class="paper cal">
          <div class="cal-h"><button class="iconbtn sm" data-mo="-1" aria-label="Previous month">‹</button><span class="cal-t">${MONTHS[m]} ${y}</span><button class="iconbtn sm" data-mo="1" aria-label="Next month">›</button></div>
          <div class="cal-sw"><span class="seg light"><button class="${unit === 'h' ? 'on' : ''}" data-unit="h">Hours</button><button class="${unit === 'c' ? 'on' : ''}" data-unit="c">Cards</button></span></div>
          <div class="cal-g"><span class="cw">M</span><span class="cw">T</span><span class="cw">W</span><span class="cw">T</span><span class="cw">F</span><span class="cw">S</span><span class="cw">S</span>${cells}</div>
          <div class="pp-f mono"><span>GT = grand test · EX = exam</span><span class="hk">less${HEAT.slice(1).map(c => `<i style="background:${c}"></i>`).join('')}more ${unit === 'h' ? 'hours' : 'cards'}</span></div>
        </div>
        ${dayCard}
      </div>
      <div class="loft-b">
        <div class="charts">
          <div class="chart"><span class="mono lab">HOURS · 14 DAYS</span><span class="bars">${bars}</span><span class="mono">avg ${fmtHM(avg14)} / day</span></div>
          <div class="chart"><span class="mono lab">CARDS · 35 DAYS</span>
            <svg viewBox="0 0 140 70" width="100%" height="70" aria-hidden="true"><path d="M${line}" stroke="#d1b77c" stroke-width="2" fill="none" stroke-linejoin="round"/></svg>
            <span class="mono">${walkedNow.toLocaleString()} / ${totalCards.toLocaleString()} walked</span></div>
        </div>
        <a class="alcove" href="#/meditation"><span class="al-t"><span class="mono kick teal">WITHIN THE LOFT</span><span class="al-h">The quiet alcove.</span><span class="al-s" id="al-last">Morning, afternoon and night guidance · scenario playlists</span></span><span class="al-go"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="12" cy="12" r="8.5" stroke-dasharray="1.2 3.1"/><circle cx="12" cy="12" r="1.6" fill="currentColor" stroke="none"/></svg></span></a>
        <details class="chrond"${P.get('chronOpen', false) ? ' open' : ''}><summary><span class="mono kick">CHRONICLES</span><span class="mono muted small">${chron.length} entries</span></summary>
          <div class="chron">${chron.slice(0, 80).map(c => `<div class="ch-i"><span class="mono">${esc(c.when)}</span><span>${esc(c.what)}</span><span class="mono">${esc(c.size)}</span></div>`).join('') || '<p class="muted small">Nothing yet.</p>'}</div>
        </details>
      </div>
    </div>
    ${nav('')}
  </div>`;
  bindGo(); bindTarget(renderLoft);
  lastMeditation().then(m => { const el = app.querySelector('#al-last'); if (m && el && TRACKS[m.track]) el.textContent = `Last: ${TRACKS[m.track].title} · ${whenLabel(m.ts)} · ${Math.max(1, Math.round(m.sec / 60))} min`; });
  app.querySelectorAll('[data-unit]').forEach(b => b.onclick = () => { P.set('heatUnit', b.dataset.unit); keep(renderLoft); });
  app.querySelectorAll('[data-mo]').forEach(b => b.onclick = () => { let mm = loftMonth.m + +b.dataset.mo, yy = loftMonth.y; if (mm < 0) { mm = 11; yy--; } if (mm > 11) { mm = 0; yy++; } loftMonth = { y: yy, m: mm }; keep(renderLoft); });
  app.querySelectorAll('[data-day]').forEach(b => b.onclick = () => { loftDay = b.dataset.day; keep(renderLoft); });
  const cd = app.querySelector('details.chrond'); if (cd) cd.addEventListener('toggle', () => P.set('chronOpen', cd.open));
}
function buildChronicle() {
  const items = [];
  // Trace sessions: group views by session
  const by = new Map();
  for (const e of S.events) {
    if (S.undone.has(e.id)) continue;
    const k = e.session || e.id;
    const s = by.get(k) || { ts: e.ts, end: e.ts, decks: new Map(), ms: 0, n: 0 };
    s.ts = Math.min(s.ts, e.ts); s.end = Math.max(s.end, e.ts); s.ms += Math.min(e.ms || 0, 20 * 60000); s.n++;
    const d = s.decks.get(e.deck) || []; d.push(e.no); s.decks.set(e.deck, d);
    by.set(k, s);
  }
  for (const s of by.values()) {
    const parts = [...s.decks.entries()].map(([d, nos]) => d + ' ' + compressNos(nos));
    items.push({ ts: s.ts, day: dkey(s.ts), when: whenLabel(s.ts), what: 'Flow · ' + parts.slice(0, 2).join(', ') + (parts.length > 2 ? ` +${parts.length - 2}` : ''), size: `${s.n} · ${fmtHM(s.ms / 60000)}` });
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
  flow = { deck: queue[0].deck, label: opts.label || '', browse: !!opts.browse, pilot: !!opts.pilot, pilotSent: false, returnTo: opts.returnTo || '#/deck/' + encodeURIComponent(queue[0].deck),
    queue, idx: 0, face: 'q', session: uid('s'), t0: Date.now(), cardT0: Date.now(), times: [], hist: [], busy: false, done: false };
  _lastDeck = queue[0].deck;
  renderFlow();
  flow.tick = setInterval(updateClock, 1000);
  document.addEventListener('keydown', flowKeys);
}
async function endFlow() {
  if (!flow) return;
  clearInterval(flow.tick);
  document.removeEventListener('keydown', flowKeys);
  closePanel(); releaseUrls();
  if (flow.pilot) stopPolling();
  const sid = flow.session, back = flow.returnTo, browse = flow.browse;
  flow = null;
  if (!browse) { await buildLogRows(sid); await countPending(); }
  if (location.hash === back) route(); else go(back);
  if (!browse && hasBackend()) sync({ downloadAll: false });
}
function current() { return flow.queue[flow.idx]; }
function sectionRange() {
  const c = current(); if (!c) return '';
  const ch = chunkOf(c), same = flow.queue.filter(x => x.deck === c.deck && chunkOf(x).key === ch.key).map(x => x.no);
  return ch.name + (same.length > 1 ? ' · ' + Math.min(...same) + '–' + Math.max(...same) : '');
}

function renderFlow() {
  const m = deckMeta(flow.deck) || {};
  const cs = P.get('cardScale', 1);
  app.innerHTML = `<div class="screen flow${flow.browse ? ' browse' : ''}" style="--cs:${cs}">
    <aside class="f-side">
      <div class="f-top">
        <button class="iconbtn" data-act="close" aria-label="End flow">${ICON.close}</button>
        <div class="f-title"><span class="mono kick" id="f-kick"></span><span class="f-sec" id="f-sec"></span><span class="f-sub muted" id="f-sub">${esc(m.title || '')}</span></div>
        <span class="tsz"><button class="iconbtn sm" data-ts="-1" aria-label="Smaller text">A−</button><button class="iconbtn sm" data-ts="1" aria-label="Larger text">A+</button></span>
        <button class="iconbtn" data-act="undo" aria-label="${flow.browse ? 'Previous card' : 'Undo last card'}" id="f-undo">${flow.browse ? ICON.prev : ICON.undo}<span class="lbl">${flow.browse ? 'Back' : 'Undo'}</span></button>
        <span class="ring" id="f-ring"></span>
      </div>
      <div class="f-stats mono">
        <span><i>TIME</i><b id="f-time">0:00</b></span>
        <span><i>PER CARD</i><b id="f-pace">–</b></span>
        <span><i>VS AVERAGE</i><b id="f-diff">–</b></span>
      </div>
      <div class="f-tiles-wrap"><span class="mono muted small">THIS FLOW</span><div class="f-tiles" id="f-tiles"></div></div>
      <p class="f-note muted small">${flow.browse ? 'Looking only: nothing is timed or logged. Space reveals and moves on · ← back · E = Edit · Esc closes.' : 'Again cards come back at the end of this flow. Space reveals and moves on · A = Again · U = Undo · E = Edit · Esc ends.'}</p>
    </aside>
    <main class="f-main">
      <div class="card-wrap"><article class="card" id="card"></article></div>
      ${flow.pilot ? '<div class="fm-slot" id="fm-slot" aria-live="polite"></div>' : ''}
      <button class="big press" id="f-big"></button>
    </main>
  </div>`;
  $('[data-act=close]').onclick = endFlow;
  app.querySelectorAll('[data-ts]').forEach(b => b.onclick = () => {
    const v = Math.max(0.8, Math.min(1.5, Math.round((P.get('cardScale', 1) + 0.1 * +b.dataset.ts) * 10) / 10));
    P.set('cardScale', v); $('.screen.flow').style.setProperty('--cs', v);
  });
  $('#f-undo').onclick = undo;
  $('#f-big').onclick = () => flow.done ? endFlow() : (flow.face === 'q' ? reveal() : next(false));
  drawCard();
  updateFlowChrome();
}

function drawCard() {
  const el = $('#card'), big = $('#f-big');
  if (flow.done) {
    const n = flow.times.length, tot = (Date.now() - flow.t0) / 1000;
    el.classList.remove('ng');
    if (flow.browse) { el.innerHTML = `<div class="c-done"><span class="mono kick dark">END OF THE DECK</span><h2>You looked through ${flow.queue.length} card${flow.queue.length === 1 ? '' : 's'}</h2><p class="muted-d">Nothing was logged. Use Flow now when you want it to count.</p></div>`; big.innerHTML = 'CLOSE'; return; }
    el.innerHTML = `<div class="c-done"><span class="mono kick dark">FLOW COMPLETE</span><h2>${n} card${n === 1 ? '' : 's'} walked</h2>
      <p>${clock(tot)} in total · ${n ? fmtDur(flow.times.reduce((a, b) => a + b, 0) / n / 1000) : '–'} per card</p>
      <p class="muted-d">Your progress is saved on this device and goes to the War Map Sheet as soon as you are online.</p></div>`;
    big.innerHTML = 'DONE';
    return;
  }
  const c = current(), tag = neetTag(c), n = seen(c.deck, c.no);
  const { head, rest } = splitQ(c.q);
  const isQ = flow.face === 'q';
  const top = `<div class="c-head mono"><span>${esc((c.section || '').toUpperCase())}</span><span>${esc(c.code)}</span></div>
    <div class="c-tags">${tag ? `<span class="neet mono">${esc(tag)}</span>` : ''}${qbChips(c)}<span class="mono seen">seen ×${n}</span>${c.edited ? '<span class="mono seen">edited</span>' : ''}
      ${isQ ? '' : `<button class="tagbtn" data-act="edit" aria-label="Edit this card">${ICON.edit}</button>${flow.browse ? '' : `<button class="again" data-act="again" aria-label="Show this card again at the end">${ICON.again}Again</button>`}`}</div>`;
  let body;
  if (isQ) {
    body = `<button class="c-q" data-act="reveal" aria-label="Reveal answer"><span class="qh${rest ? '' : ' solo'}">${inline(head)}</span>${rest ? `<div class="qr">${render(rest)}</div>` : ''}<span class="star">✦</span></button>`;
  } else {
    body = `<div class="c-a">
      <h2 class="c-title">${esc(plain(head).replace(/:$/, ''))}</h2>
      ${rest ? `<details class="qrecap" open><summary>Question parts</summary><div class="qr small">${render(rest)}</div></details>` : ''}
      ${qbFix(c)}
      <div class="ans">${render(c.a)}</div>
      ${c.img ? `<div class="box note"><span class="mono">DIAGRAM</span><p>This card has a figure on page ${c.a_page || c.q_page || '?'} of the PDF deck.</p></div>` : ''}
      ${c.why ? `<div class="box why"><span class="mono">WHY</span><div class="bx">${render(c.why)}</div></div>` : ''}
      ${c.watch ? `<div class="box watch"><span class="mono">WATCH</span><div class="bx">${render(c.watch)}</div></div>` : ''}
      ${qbBoxes(c)}
      <label class="hook"><span class="mono">YOUR OT HOOK</span><input type="text" id="hook" value="${esc(c.hook || '')}" placeholder="A detail that makes it stick…" enterkeyhint="done"></label>
    </div>`;
  }
  el.innerHTML = top + body;
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
  big.innerHTML = isQ ? `${ICON.flip}REVEAL` : `NEXT${ICON.next}`;
  el.querySelectorAll('[data-act=reveal]').forEach(b => b.onclick = reveal);
  const ag = el.querySelector('[data-act=again]'); if (ag) ag.onclick = () => next(true);
  const ed = el.querySelector('[data-act=edit]'); if (ed) ed.onclick = () => openEditor(current());
  const hk = el.querySelector('#hook');
  if (hk) {
    const save = () => { const v = hk.value.trim(); const cc = current(); if (v !== (cc.hook || '')) saveHook(cc, v); };
    hk.onchange = save; hk.onblur = save;
    hk.onkeydown = e => { e.stopPropagation(); if (e.key === 'Enter') hk.blur(); };
  }
}
/* ---------- QBank/GT layer (data/qbank.json): shown beside the card, never written into it ---------- */
function qbChips(c) {
  if (c.topup) { const h = hitsOf(c).h; return `<span class="qc qc-top mono">Top-up</span><span class="qc qc-tier mono">Tier ${c.tier}${c.nq ? ' · ' + c.nq + ' Qs' : ''}</span>${[['marrow', 'Marrow'], ['doct', 'DocT'], ['gt', 'DocT GT']].filter(([k]) => h.has(k)).map(([k, t]) => `<span class="qc qc-${k} mono">${t}</span>`).join('')}`; }
  if (c.tdeck) { const h = hitsOf(c).h; return `<span class="qc qc-top mono">Top-up deck</span>${[['marrow', 'Marrow'], ['doct', 'DocT'], ['gt', 'DocT GT']].filter(([k]) => h.has(k)).map(([k, t]) => `<span class="qc qc-${k} mono">${t}</span>`).join('')}`; }
  const q = qbOf(c);
  if (!q || !q.chips) return '';
  return q.chips.filter(x => x.k !== 'recall').map(x => `<span class="qc qc-${x.k} mono" title="${x.n} question${x.n > 1 ? 's' : ''}">${esc(x.t)}${x.n > 1 ? ' ×' + x.n : ''}</span>`).join('');
}
const bankLine = l => { const m = l.match(/^([A-Za-z0-9 +·]{2,40}?):\s+(.*)$/s); return m ? `<p><b class="bk">${esc(m[1])}</b> ${inline(m[2])}</p>` : `<p>${inline(l)}</p>`; };
function qbBoxes(c) {
  if (c.tdeck || c.topup) { const src = c.src || ''; return src ? `<p class="qsrc-card mono">From: ${esc(src)}</p>` : ''; }
  const q = qbOf(c);
  if (!q) return '';
  let h = '';
  if (q.lines && q.lines.length) h += `<div class="box qlines"><span class="mono">TOP-UP LINES</span><div class="bx">${q.lines.map(bankLine).join('')}</div></div>`;
  if (q.cross && q.cross.length) h += `<div class="box qcross"><span class="mono">CROSSFIRE</span><div class="bx">${q.cross.map(l => `<p>${inline(l)}</p>`).join('')}</div></div>`;
  return h;
}
function qbFix(c) {
  const q = qbOf(c);
  if (!q || !q.fix || !q.fix.length) return '';
  return `<div class="box qfix"><span class="mono">CORRECTION · CHECKED</span><div class="bx">${q.fix.map(f => `<p>${inline(f.t)}</p>${f.src ? `<p class="qsrc">${f.url ? `<a href="${esc(f.url)}" target="_blank" rel="noopener">${esc(f.src)}</a>` : esc(f.src)}</p>` : ''}`).join('')}</div></div>`;
}
async function saveHook(c, v) {
  const e = S.edits.get(c.deck + '|' + c.code);
  await saveEdit(c, { ...((e && e.fields) || {}), hook: v });
  const i = flow && flow.queue.findIndex(x => x.code === c.code && x.deck === c.deck);
  if (flow && i >= 0) flow.queue[i] = { ...flow.queue[i], hook: v, edited: true };
}

function updateClock() {
  if (!flow) return;
  const t = $('#f-time'); if (t) t.textContent = clock((Date.now() - flow.t0) / 1000);
}
function updateFlowChrome() {
  if (!flow || !$('#f-ring')) return;
  const total = flow.queue.length, step = Math.min(total, flow.idx + (flow.done ? 0 : 1));
  const circ = 2 * Math.PI * 22;
  $('#f-ring').innerHTML = `<svg viewBox="0 0 52 52"><circle cx="26" cy="26" r="22" class="r0"/><circle cx="26" cy="26" r="22" class="r1" stroke-dasharray="${(circ * step / total).toFixed(1)} ${circ.toFixed(1)}" transform="rotate(-90 26 26)"/></svg><span>${step}/${total}</span>`;
  $('#f-sec').textContent = flow.done ? 'Done' : sectionRange();
  const cc = !flow.done && current(), cm = cc ? deckMeta(cc.deck) || {} : {};
  $('#f-kick').textContent = (flow.browse ? 'LOOK · ' : 'FLOW · ') + (cc ? cc.deck : flow.deck) + (cm.star ? ' · ✦ ' + cm.star : '') + (flow.label && flow.label !== 'Look' ? ' · ' + flow.label.toUpperCase() : '');
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
  const seenNow = new Set(flow.queue.slice(0, flow.idx).map(c => c.code));
  const fq = flow.queue.slice(0, 60);
  $('#f-tiles').innerHTML = fq.map((c, i) => `<span class="ft${i && (c.deck !== fq[i - 1].deck || chunkOf(c).key !== chunkOf(fq[i - 1]).key) ? ' cs' : ''} s${shade(seen(c.deck, c.no))}${c.topup || c.tdeck ? (seen(c.deck, c.no) ? ' tu tu1' : ' tu') : ''}${i === flow.idx && !flow.done ? ' cur' : ''}${seenNow.has(c.code) ? ' was' : ''}"><b>${c.no}</b><i>×${seen(c.deck, c.no)}</i></span>`).join('');
}

function animate(kind, swap) {
  const el = $('#card');
  flow.busy = true;
  const out = kind === 'flip' ? 'anim-flip-out' : 'anim-deal-out';
  const inn = kind === 'flip' ? 'anim-flip-in' : 'anim-deal-in';
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
  if (!flow || flow.busy || flow.face !== 'q' || flow.done) return;
  animate('flip', () => { flow.face = 'a'; drawCard(); });
}
async function next(again) {
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
  const c = current(), ms = Date.now() - flow.cardT0;
  const hk = $('#hook'); if (hk && hk.value.trim() !== (c.hook || '')) await saveHook(c, hk.value.trim());
  const ev = await recordView({ id: uid('e'), ts: Date.now(), deck: c.deck, code: c.code, no: c.no, ms, again: !!again, session: flow.session });
  flow.hist.push({ idx: flow.idx, ev, appended: !!again, cardT0: flow.cardT0 });
  flow.times.push(ms);
  if (again) flow.queue.push(c);
  animate('deal', () => {
    flow.idx++;
    flow.face = 'q';
    flow.cardT0 = Date.now();
    if (flow.idx >= flow.queue.length) flow.done = true;
    saveLastFlow();
    drawCard(); updateFlowChrome();
  });
}
async function undo() {
  if (flow && flow.browse) { if (flow.busy || flow.idx === 0) return; flow.idx--; flow.face = 'q'; flow.done = false; drawCard(); updateFlowChrome(); return; }
  if (!flow || flow.busy || !flow.hist.length) return;
  const h = flow.hist.pop();
  await undoView(h.ev);
  if (h.appended) flow.queue.pop();
  flow.times.pop();
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
  if (e.key === ' ' || e.key === 'Enter' || e.key === 'ArrowRight') { e.preventDefault(); flow.done ? endFlow() : flow.face === 'q' ? reveal() : next(false); }
  else if (e.key === 'ArrowLeft') { if (flow.browse) undo(); }
  else if (e.key === 'a' || e.key === 'A') { if (flow.face === 'a' && !flow.browse) next(true); }
  else if (e.key === 'u' || e.key === 'U' || e.key === 'Backspace' || (e.key === 'z' && (e.metaKey || e.ctrlKey))) { e.preventDefault(); undo(); }
  else if (e.key === 'e' || e.key === 'E') { if (flow.face === 'a') openEditor(current()); }
  else if (e.key === 'Escape') endFlow();
}

/* ============================ editor ============================ */
function openEditor(c) {
  const orig = (S.decks.get(c.deck) || { cards: [] }).cards.find(x => x.code === c.code) || c;
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
