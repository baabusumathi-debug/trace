import { CONFIG } from './config.js';
import { db, useDemoDb } from './db.js';
import { initApi, hasBackend, isDemo, setBackend, call } from './api.js';
import { S, loadAll, emit, cardsOf, deckMeta, neetTag, seen, walked, avgPace, tier, shade, systems, isReady, recount } from './store.js';
import { status, sync, startAutoSync, recordView, undoView, buildLogRows, saveEdit, resetEdit, uid, countPending, downloadDecks, deckState } from './sync.js';
import { render, splitQ, plain, inline } from './md.js';
import { seal, emblem } from './emblems.js';

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
  ledger: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M4 12a8 8 0 1 0 2.5-5.8M4 4v4h4"/></svg>'
};

/* ============================ boot ============================ */
async function boot() {
  const params = new URLSearchParams(location.search);
  const demo = params.has('demo');
  if (demo) useDemoDb();
  await initApi(demo);

  // private setup link: #setup=<base64url {"u":..., "k":...}>
  if (!demo) await trySetup(location.href);
  if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(() => {});
  await loadAll();
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
}

/* ============================ router ============================ */
let lastRoute = '';
function route() {
  if (flow) return;
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
  if (page === 'status') return renderStatus();
  if (page === 'changes') return renderChanges();
  renderCabinet();
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
  const last = lastFlowTarget();
  return `<nav class="nav">${item('decks', '#/', ICON.decks, 'Decks')}${item('walk', last ? '#/deck/' + encodeURIComponent(last) : '#/', ICON.walk, 'Walk')}${item('changes', '#/changes', ICON.ledger, 'Changes')}</nav>`;
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
function brandMark() { return '<span class="mark"><span>✦</span></span>'; }

/* ============================ cabinet ============================ */
function renderCabinet() {
  const sys = systems();
  const ready = S.library ? S.library.decks.filter(d => isReady(d.deck)).length : 0;
  const total = S.library ? S.library.decks.length : 0;
  let body;
  if (!S.library) body = `<div class="empty"><p>${status.state === 'error' ? 'Could not reach your Drive: ' + esc(status.error) : 'Fetching your library…'}</p></div>`;
  else body = sys.map(s => {
    const stars = s.decks.reduce((t, d) => t + (d.star || 0), 0);
    const decks = s.decks.slice().sort((a, b) => (b.star || 0) - (a.star || 0) || a.deck.localeCompare(b.deck, undefined, { numeric: true }));
    return `<section class="sys"><div class="rule-h"><span class="h2">${esc(s.label)}</span><span class="line"></span><span class="mono gold">✦ ${stars}</span></div>
      <div class="deck-grid">${decks.map(deckBack).join('')}</div></section>`;
  }).join('');
  app.innerHTML = `<div class="screen cabinet">
    <header class="top">
      <div class="brand">${brandMark()}<span class="brand-t"><span class="b1">TRACE</span><span class="b2">THE MAGICIAN’S CABINET</span></span></div>
      <div class="top-r">${syncPill()}<span class="exam mono"><span class="gold">${CONFIG.exam.name}</span>${daysLeft()}</span></div>
    </header>
    <div class="scroll">
      <div class="intro"><span class="kicker">YOUR COLLECTION</span><h1>Choose a deck.</h1>
      <p class="muted">Gold, silver and bronze foil mark the decks the real NEET-SS papers drew from most. ${total ? `<span class="nowrap">${ready} of ${total} decks ready offline.</span>` : ''}</p></div>
      ${body}
    </div>
    ${nav('decks')}
  </div>`;
  bindGo();
}

function deckBack(d) {
  const t = tier(d.star || 0), w = walked(d.deck), ok = isReady(d.deck);
  const pct = d.cards ? Math.round(100 * w / d.cards) : 0;
  return `<a class="deck${ok ? '' : ' notready'}" href="#/deck/${encodeURIComponent(d.deck)}" aria-label="Open ${esc(d.title)}">
    <span class="back t-${t}" style="--tone:${emblem(d.system).tone}">
      <span class="frame1"></span><span class="frame2"></span>
      <span class="back-top mono"><span>${esc(d.deck)}</span><span>✦ ${d.star || 0}</span></span>
      <span class="back-seal">${seal(d.system)}</span>
      <span class="back-title">${esc(d.title)}</span>
      <span class="back-foot mono"><span>${d.cards} CARDS</span><span>${ok ? TIER_NAME[t] : 'NOT DOWNLOADED'}</span></span>
    </span>
    <span class="prog mono"><span class="bar"><span style="width:${pct}%"></span></span><span>${w}/${d.cards}</span></span>
  </a>`;
}

/* ============================ deck ============================ */
const deckFilter = {};
function filtersFor(deck, cards) {
  const neet = cards.filter(c => neetTag(c));
  return [
    { key: 'all', label: 'All', list: cards },
    { key: 'neet', label: 'NEET', list: neet },
    { key: 'low', label: 'Seen ≤ 1', list: cards.filter(c => seen(deck, c.no) <= 1) },
    { key: 'new', label: 'Unseen', list: cards.filter(c => seen(deck, c.no) === 0) },
    { key: 'edited', label: 'Edited', list: cards.filter(c => c.edited) }
  ].filter(f => f.key === 'all' || f.list.length);
}
function renderDeck(code) {
  const m = deckMeta(code);
  if (!m) return renderCabinet();
  _lastDeck = code;
  const cards = cardsOf(code);
  const t = tier(m.star || 0);
  const fs = filtersFor(code, cards);
  const fk = fs.find(f => f.key === deckFilter[code]) ? deckFilter[code] : 'all';
  const cur = fs.find(f => f.key === fk);
  const inSet = new Set(cur.list.map(c => c.code));
  const sections = [];
  for (const c of cards) {
    const last = sections[sections.length - 1];
    if (last && last.name === (c.section || '')) last.cards.push(c); else sections.push({ name: c.section || '', cards: [c] });
  }
  const st = deckState(code);
  const tiles = sections.map(sec => `<section class="dsec"><div class="rule-h"><span class="h3">${esc(sec.name || 'Cards')}</span><span class="line"></span><span class="mono muted small">${sec.cards[0].no}–${sec.cards[sec.cards.length - 1].no}</span></div>
    <div class="tiles">${sec.cards.map(c => tile(c, inSet.has(c.code))).join('')}</div></section>`).join('');
  app.innerHTML = `<div class="screen deckv">
    <div class="dhead t-${t}" style="--tone:${emblem(m.system).tone}">
      <div class="dhead-row"><a class="iconbtn on-foil" href="#/" aria-label="Back to the cabinet">${ICON.back}</a>
        <span class="mono kick">${esc((m.system || '').replace(/^\d+\s+/, '').toUpperCase())} · ${TIER_NAME[t]}</span></div>
      <div class="dhead-main">${seal(m.system, 'hseal')}<div><span class="mono">${esc(code)}</span><h1>${esc(m.title)}</h1></div></div>
      <div class="dstats mono"><span><b>${m.cards}</b> cards</span><span><b>✦ ${m.star || 0}</b> real NEET Qs</span><span><b>${walked(code)}</b> walked</span></div>
    </div>
    <div class="scroll pad">
      ${st !== 'ready' ? `<div class="notice">${st === 'missing' ? 'This deck is not on this device yet.' : 'A newer version of this deck is waiting.'} <button class="link" data-act="dl">Download now</button></div>` : ''}
      <div class="chips">${fs.map(f => `<button class="chip${f.key === fk ? ' on' : ''}" data-f="${f.key}">${f.label} · ${f.list.length}</button>`).join('')}</div>
      <div class="legend mono"><span>TIMES SEEN</span>${[0, 1, 2, 3].map(n => `<span class="lg s${n}">${n === 3 ? '3+' : n}</span>`).join('')}</div>
      ${cards.length ? tiles : '<p class="muted">No cards on this device yet.</p>'}
    </div>
    <div class="dfoot">
      <button class="btn primary press" data-act="walk" ${cur.list.length ? '' : 'disabled'}>${fk === 'all' ? `Walk all ${cur.list.length} cards` : `Walk ${cur.list.length} ${cur.label} cards`}</button>
    </div>
  </div>`;
  bindGo();
  app.querySelectorAll('[data-f]').forEach(b => b.onclick = () => { deckFilter[code] = b.dataset.f; renderDeck(code); });
  const dl = app.querySelector('[data-act=dl]');
  if (dl) dl.onclick = async () => { dl.disabled = true; try { await downloadDecks([code]); toast('Downloaded and checked.'); } catch (e) { toast(e.message); } emit(); };
  app.querySelector('[data-act=walk]').onclick = () => startFlow(code, cur.list, 0, cur.key === 'all' ? '' : cur.label);
  app.querySelectorAll('.tile').forEach(el => el.onclick = () => {
    const list = cur.list.find(c => c.code === el.dataset.code) ? cur.list : cards;
    startFlow(code, list, list.findIndex(c => c.code === el.dataset.code), cur.key === 'all' || list === cards ? '' : cur.label);
  });
}
function tile(c, active) {
  const n = seen(c.deck, c.no), tag = neetTag(c);
  return `<button class="tile s${shade(n)}${active ? '' : ' dim'}" data-code="${esc(c.code)}" aria-label="Card ${c.no}, seen ${n} times${tag ? ', ' + tag : ''}">
    <span class="tl-top mono"><span>${esc(c.code)}</span><span>×${n}</span></span>
    <span class="tl-no">${c.no}</span>
    <span class="tl-tag mono">${esc(tag)}${c.edited ? ' ✎' : ''}</span></button>`;
}

/* ============================ flow ============================ */
let flow = null;
function startFlow(deck, list, startAt, label) {
  if (!list.length) return;
  const queue = list.slice(Math.max(0, startAt)).concat(list.slice(0, Math.max(0, startAt)));
  flow = { deck, label, queue, idx: 0, face: 'q', session: uid('s'), t0: Date.now(), cardT0: Date.now(), times: [], hist: [], again: new Set(), busy: false, done: false };
  _lastDeck = deck;
  renderFlow();
  flow.tick = setInterval(updateClock, 1000);
  document.addEventListener('keydown', flowKeys);
}
async function endFlow() {
  if (!flow) return;
  clearInterval(flow.tick);
  document.removeEventListener('keydown', flowKeys);
  const sid = flow.session, deck = flow.deck;
  flow = null;
  await buildLogRows(sid);
  await countPending();
  go('#/deck/' + encodeURIComponent(deck));
  route();
  if (hasBackend()) sync({ downloadAll: false });
}
function current() { return flow.queue[flow.idx]; }
function sectionRange() {
  const c = current(); if (!c) return '';
  const same = flow.queue.filter(x => x.section === c.section).map(x => x.no);
  return (c.section || 'Cards') + (same.length > 1 ? ' · ' + Math.min(...same) + '–' + Math.max(...same) : '');
}

function renderFlow() {
  const m = deckMeta(flow.deck) || {};
  app.innerHTML = `<div class="screen flow">
    <aside class="f-side">
      <div class="f-top">
        <button class="iconbtn" data-act="close" aria-label="End flow">${ICON.close}</button>
        <div class="f-title"><span class="mono kick">FLOW · ${esc(flow.deck)}${m.star ? ' · ✦ ' + m.star : ''}${flow.label ? ' · ' + esc(flow.label.toUpperCase()) : ''}</span><span class="f-sec" id="f-sec"></span><span class="f-sub muted" id="f-sub">${esc(m.title || '')}</span></div>
        <button class="iconbtn" data-act="undo" aria-label="Undo last card" id="f-undo">${ICON.undo}<span class="lbl">Undo</span></button>
        <span class="ring" id="f-ring"></span>
      </div>
      <div class="f-stats mono">
        <span><i>TIME</i><b id="f-time">0:00</b></span>
        <span><i>PER CARD</i><b id="f-pace">–</b></span>
        <span><i>VS AVERAGE</i><b id="f-diff">–</b></span>
      </div>
      <div class="f-tiles-wrap"><span class="mono muted small">THIS FLOW</span><div class="f-tiles" id="f-tiles"></div></div>
      <p class="f-note muted small">Again cards come back at the end of this flow. Space reveals and moves on · A = Again · U = Undo · E = Edit · Esc ends.</p>
    </aside>
    <main class="f-main">
      <div class="card-wrap"><article class="card" id="card"></article></div>
      <button class="big press" id="f-big"></button>
    </main>
  </div>`;
  $('[data-act=close]').onclick = endFlow;
  $('#f-undo').onclick = undo;
  $('#f-big').onclick = () => flow.done ? endFlow() : (flow.face === 'q' ? reveal() : next(false));
  drawCard();
  updateFlowChrome();
}

function drawCard() {
  const el = $('#card'), big = $('#f-big');
  if (flow.done) {
    const n = flow.times.length, tot = (Date.now() - flow.t0) / 1000;
    el.innerHTML = `<div class="c-done"><span class="mono kick dark">FLOW COMPLETE</span><h2>${n} card${n === 1 ? '' : 's'} walked</h2>
      <p>${clock(tot)} in total · ${n ? fmtDur(flow.times.reduce((a, b) => a + b, 0) / n / 1000) : '–'} per card</p>
      <p class="muted-d">Your progress is saved on this device and goes to the War Map Sheet as soon as you are online.</p></div>`;
    big.innerHTML = 'BACK TO THE DECK';
    return;
  }
  const c = current(), tag = neetTag(c), n = seen(c.deck, c.no);
  const { head, rest } = splitQ(c.q);
  const isQ = flow.face === 'q';
  const top = `<div class="c-head mono"><span>${esc((c.section || '').toUpperCase())}</span><span>${esc(c.code)}</span></div>
    <div class="c-tags">${tag ? `<span class="neet mono">${esc(tag)}</span>` : ''}<span class="mono seen">seen ×${n}</span>${c.edited ? '<span class="mono seen">edited</span>' : ''}
      ${isQ ? '' : `<button class="tagbtn" data-act="edit" aria-label="Edit this card">${ICON.edit}</button><button class="again" data-act="again" aria-label="Show this card again at the end">${ICON.again}Again</button>`}</div>`;
  let body;
  if (isQ) {
    body = `<button class="c-q" data-act="reveal" aria-label="Reveal answer"><span class="qh${rest ? '' : ' solo'}">${inline(head)}</span>${rest ? `<div class="qr">${render(rest)}</div>` : ''}<span class="star">✦</span></button>`;
  } else {
    body = `<div class="c-a">
      <h2 class="c-title">${esc(plain(head).replace(/:$/, ''))}</h2>
      ${rest ? `<details class="qrecap"><summary>Question parts</summary><div class="qr small">${render(rest)}</div></details>` : ''}
      <div class="ans">${render(c.a)}</div>
      ${c.img ? `<div class="box note"><span class="mono">DIAGRAM</span><p>This card has a figure on page ${c.a_page || c.q_page || '?'} of the PDF deck.</p></div>` : ''}
      ${c.why ? `<div class="box why"><span class="mono">WHY</span>${render(c.why)}</div>` : ''}
      ${c.watch ? `<div class="box watch"><span class="mono">WATCH</span>${render(c.watch)}</div>` : ''}
      <label class="hook"><span class="mono">YOUR OT HOOK</span><input type="text" id="hook" value="${esc(c.hook || '')}" placeholder="A detail that makes it stick…" enterkeyhint="done"></label>
    </div>`;
  }
  el.innerHTML = top + body;
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
  const n = flow.times.length;
  const mine = n ? flow.times.reduce((a, b) => a + b, 0) / n : 0;
  const avg = avgPace();
  $('#f-pace').textContent = n ? fmtDur(mine / 1000) : '–';
  if (n && avg) {
    const d = Math.round((mine - avg) / 1000);
    $('#f-diff').innerHTML = `${fmtDur(Math.abs(d))} <span class="gold">${d < 0 ? '↓' : d > 0 ? '↑' : '='}</span> <small>avg</small>`;
  } else $('#f-diff').textContent = '–';
  $('#f-undo').classList.toggle('dimmed', !flow.hist.length);
  const seenNow = new Set(flow.queue.slice(0, flow.idx).map(c => c.code));
  $('#f-tiles').innerHTML = flow.queue.slice(0, 60).map((c, i) => `<span class="ft s${shade(seen(c.deck, c.no))}${i === flow.idx && !flow.done ? ' cur' : ''}${seenNow.has(c.code) ? ' was' : ''}"><b>${c.no}</b><i>×${seen(c.deck, c.no)}</i></span>`).join('');
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
    drawCard(); updateFlowChrome();
  });
}
async function undo() {
  if (!flow || flow.busy || !flow.hist.length) return;
  const h = flow.hist.pop();
  await undoView(h.ev);
  if (h.appended) flow.queue.pop();
  flow.times.pop();
  flow.idx = h.idx; flow.face = 'q'; flow.done = false; flow.cardT0 = Date.now();
  drawCard(); updateFlowChrome();
}
function flowKeys(e) {
  if (!flow || e.target.matches('input, textarea')) return;
  if ($('.modal')) return;
  if (e.key === ' ' || e.key === 'Enter' || e.key === 'ArrowRight') { e.preventDefault(); flow.done ? endFlow() : flow.face === 'q' ? reveal() : next(false); }
  else if (e.key === 'a' || e.key === 'A') { if (flow.face === 'a') next(true); }
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
        <dt>Device</dt><dd class="mono">${esc(S.device)}</dd>
        <dt>App</dt><dd class="mono">${CONFIG.appVersion}</dd>
      </dl>
      <div class="row-btns">
        <button class="btn primary" data-act="sync" ${status.busy ? 'disabled' : ''}>Sync now</button>
        <button class="btn ghost" data-act="dl">Re-check all decks</button>
      </div>
      ${isDemo() ? '<p class="muted small">You are in demo mode with sample decks. <a href="./">Leave demo</a></p>' : ''}
    </div>
    ${nav('')}
  </div>`;
  bindGo();
  $('[data-act=sync]').onclick = () => sync();
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
    if (c) startFlow(b.dataset.deck, [c], 0, 'Edited');
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
  navigator.serviceWorker.register('sw.js').then(reg => {
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
    navigator.serviceWorker.addEventListener('controllerchange', () => { if (!reloaded && !flow) { reloaded = true; location.reload(); } });
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
