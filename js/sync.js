// Keeps the device and Drive/Sheet in step. Safe to call any time; it never blocks studying.
import { db } from './db.js';
import { batch, hasBackend, isDemo } from './api.js';
import { CONFIG } from './config.js';
import { S, emit, recount, setNeet, deckMeta, today } from './store.js';

export const status = { targetNote: '', state: 'idle', last: null, error: '', pending: 0, busy: false, downloading: 0 };
const EV_HEADER = ['id', 'ts', 'date', 'time', 'device', 'session', 'deck', 'code', 'no', 'ms', 'again', 'kind', 'ref'];
const OWNER = new Set(['trace', 'naven', '']);

const pad = n => String(n).padStart(2, '0');
export const ymd = d => d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
export const hm = d => pad(d.getHours()) + ':' + pad(d.getMinutes());
export const uid = p => p + Date.now().toString(36) + Math.random().toString(36).slice(2, 7);

/* ---------------- local writes (called by the study screens) ---------------- */
export async function recordView(ev) {
  const e = { kind: 'view', synced: 0, logged: 0, dev: S.device, ...ev };
  S.events.push(e);
  await db.put('events', e);
  recount();
  return e;
}
export async function undoView(e) {
  S.events = S.events.filter(x => x.id !== e.id);
  if (!e.synced) await db.del('events', e.id);
  else {
    const u = { id: uid('u'), kind: 'undo', ref: e.id, ts: Date.now(), deck: e.deck, code: e.code, no: e.no, synced: 0, logged: 1, dev: S.device, session: e.session };
    S.undone.add(e.id);
    await db.put('events', u);
  }
  recount();
}
export async function saveEdit(card, fields) {
  const key = card.deck + '|' + card.code;
  const rec = { key, deck: card.deck, code: card.code, fields, ts: Date.now(), dev: S.device, synced: 0 };
  S.edits.set(key, rec);
  await db.put('edits', rec);
  emit();
}
export async function resetEdit(card) {
  const key = card.deck + '|' + card.code;
  const rec = { key, deck: card.deck, code: card.code, fields: {}, ts: Date.now(), dev: S.device, synced: 0, reset: true };
  S.edits.set(key, rec);
  await db.put('edits', rec);
  emit();
}

/* ---------------- Log rows for the War Map ---------------- */
function chunkOf(deck, no) {
  const ch = (S.chunks[deck] || []).find(c => no >= c.from && no <= c.to);
  return ch ? ch.id : '';
}
/** Turn finished study into War Map Log rows. force = session id that just ended. */
export async function buildLogRows(force) {
  const now = Date.now();
  const all = await db.all('events');
  const undone = new Set(all.filter(e => e.kind === 'undo').map(e => e.ref));
  const views = all.filter(e => e.kind === 'view' && !undone.has(e.id));
  const pending = views.filter(e => !e.logged && (e.session === force || now - e.ts > CONFIG.logIdleMs));
  if (!pending.length) return 0;
  // cards already walked before (old War Map rows + earlier Trace sessions)
  const covered = (await db.kv.get('covered')) || {};
  const coveredSet = deck => new Set(covered[deck] || []);
  const groups = new Map();
  for (const e of pending) {
    const k = e.session + '|' + e.deck;
    if (!groups.has(k)) groups.set(k, []);
    groups.get(k).push(e);
  }
  const rows = [];
  for (const evs of groups.values()) {
    const deck = evs[0].deck;
    const before = coveredSet(deck);
    for (const e of views) if (e.logged && e.deck === deck) before.add(e.no);
    const byNo = new Map();
    for (const e of evs) {
      const x = byNo.get(e.no) || { no: e.no, ms: 0, ts: e.ts };
      x.ms += e.ms || 0; x.ts = Math.min(x.ts, e.ts);
      byNo.set(e.no, x);
    }
    const nos = [...byNo.values()].sort((a, b) => a.no - b.no);
    let run = [];
    const flush = () => {
      if (!run.length) return;
      const first = new Date(Math.min(...run.map(r => r.ts)));
      const id = uid('T');
      const minutes = Math.max(1, Math.round(run.reduce((a, r) => a + r.ms, 0) / 60000));
      const stage = before.has(run[0].no) ? 'pass2_encoding' : 'pass1_exposure';
      rows.push({ id, synced: 0, row: [ymd(first), hm(first), CONFIG.who, deck, chunkOf(deck, run[0].no), stage, run.length, minutes,
        'Trace app · ' + id, run[0].no, run[run.length - 1].no, ''] });
      run = [];
    };
    for (const x of nos) {
      const prev = run[run.length - 1];
      const stage = before.has(x.no), prevStage = prev && before.has(prev.no);
      if (prev && (x.no !== prev.no + 1 || chunkOf(deck, x.no) !== chunkOf(deck, prev.no) || stage !== prevStage)) flush();
      run.push(x);
    }
    flush();
    covered[deck] = [...new Set([...(covered[deck] || []), ...nos.map(x => x.no)])];
  }
  await db.putMany('logrows', rows);
  for (const e of pending) e.logged = 1;
  await db.putMany('events', pending);
  await db.kv.set('covered', covered);
  return rows.length;
}

/* ---------------- verification of a downloaded deck ---------------- */
export function parseDeck(text, meta) {
  const cards = [];
  const lines = text.split('\n').filter(l => l.trim());
  for (const l of lines) cards.push(JSON.parse(l));
  if (meta && cards.length !== meta.cards) throw new Error(`${meta.deck}: ${cards.length} cards, expected ${meta.cards}`);
  const codes = new Set();
  for (const c of cards) {
    if (!c.code || !c.q || c.a == null || typeof c.no !== 'number') throw new Error(`${meta ? meta.deck : ''}: card ${c.code || '?'} incomplete`);
    if (codes.has(c.code)) throw new Error(`${meta ? meta.deck : ''}: duplicate ${c.code}`);
    codes.add(c.code);
    if (meta) c.deck = meta.deck;
  }
  return cards.sort((a, b) => a.no - b.no);
}

/* ---------------- the sync itself ---------------- */
let timer = null;
export function startAutoSync() {
  if (timer) return;
  const tick = () => { if (navigator.onLine && document.visibilityState === 'visible') sync().catch(() => {}); };
  timer = setInterval(tick, CONFIG.syncEveryMs);
  window.addEventListener('online', tick);
  document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') tick(); });
  tick();
}

export async function countPending() {
  const ev = (await db.all('events')).filter(e => !e.synced).length;
  const lr = (await db.all('logrows')).filter(r => !r.synced).length;
  const ed = (await db.all('edits')).filter(r => !r.synced).length;
  status.pending = ev + lr + ed;
  return status.pending;
}

export async function sync({ downloadAll = true } = {}) {
  if (status.busy || !hasBackend()) return;
  if (!navigator.onLine && !isDemo()) { status.state = 'offline'; emit(); return; }
  status.busy = true; status.state = 'syncing'; status.error = ''; emit();
  try {
    await buildLogRows();
    if ((await db.kv.get('logVer')) !== 2) {          // v2 also keeps hours per day: read the Log again from the top
      await db.kv.set('logRow', 1); await db.kv.set('logBase', {}); await db.kv.set('logDaily', {}); await db.kv.set('logChron', []);
      S.logBase = {}; S.logDaily = {}; S.logChron = [];
      await db.kv.set('logVer', 2);
    }
    const k = {
      evRow: (await db.kv.get('evRow')) || 1,
      logRow: (await db.kv.get('logRow')) || 1,
      chunksAt: (await db.kv.get('chunksAt')) || 0,
      editsId: await db.kv.get('editsId')
    };
    const libId = isDemo() ? 'library.json' : ((await db.kv.get('libId')) || CONFIG.libraryId);
    const ops = [
      { op: 'readFile', id: libId },
      { op: 'sheetRead', tab: 'TraceEvents', fromRow: k.evRow + 1 },
      { op: 'sheetRead', tab: 'Log', fromRow: k.logRow + 1 },
      { op: 'findFile', folderId: CONFIG.traceFolderId, name: 'edits.json' },
      { op: 'findFile', folderId: CONFIG.traceFolderId, name: 'library.json' }
    ];
    const needChunks = Date.now() - k.chunksAt > 12 * 3600e3;
    if (needChunks) ops.push({ op: 'sheetRead', tab: 'Chunks', fromRow: 2 });
    const r = await batch(ops);
    // 1. library (found by name: Claude replaces the file when decks change)
    let libRes = r[0];
    const found = r[4].ok && r[4].data;
    if (found && found.id !== libId) {
      [libRes] = await batch([{ op: 'readFile', id: found.id }]);
      if (libRes.ok) await db.kv.set('libId', found.id);
    }
    if (!libRes.ok) throw new Error('library: ' + libRes.error);
    const lib = JSON.parse(libRes.data.text);
    const oldNeet = S.library && S.library.neet_version;
    S.library = lib; await db.kv.set('library', lib);
    if (lib.neet_id && (lib.neet_version !== oldNeet || !S.neet.size)) {
      const [n] = await batch([{ op: 'readFile', id: lib.neet_id }]);
      if (n.ok) { const nj = JSON.parse(n.data.text); setNeet(nj); await db.kv.set('neet', nj); }
    }

    // 2. events from other devices
    if (r[1].ok) await mergeRemoteEvents(r[1].data, k.evRow);
    // 3. old War Map Log rows -> "times seen" base + covered cards
    if (r[2].ok) await absorbLog(r[2].data, k.logRow);
    // 4. chunk ranges
    if (needChunks && r[5] && r[5].ok) {
      const chunks = {};
      for (const v of r[5].data.values) {
        const [cid, deck, , from, to] = v;
        if (!cid || !deck) continue;
        (chunks[deck] = chunks[deck] || []).push({ id: cid, from: +from, to: +to });
      }
      S.chunks = chunks; await db.kv.set('chunks', chunks); await db.kv.set('chunksAt', Date.now());
    }
    // 5. card edits (shared file)
    await syncEdits(r[3].ok ? r[3].data : null, k.editsId);

    // 6. push my study to the Sheet
    await buildLogRows();
    await pushOutbox();
    await syncTargets();

    // 7. decks: new or changed versions
    if (downloadAll) await downloadDecks();

    recount();
    status.state = 'ok'; status.last = Date.now();
    await db.kv.set('lastSync', status.last);
  } catch (e) {
    console.error(e);
    status.state = 'error'; status.error = String(e.message || e);
  } finally {
    status.busy = false;
    await countPending();
    emit();
  }
}

async function mergeRemoteEvents(data, fromRow) {
  const vals = data.values || [];
  if (fromRow <= 1 && vals.length && vals[0][0] === 'id') vals.shift();
  const have = new Set((await db.all('events')).map(e => e.id));
  const add = [];
  for (const v of vals) {
    const o = Object.fromEntries(EV_HEADER.map((h, i) => [h, v[i]]));
    if (!o.id || have.has(o.id)) continue;
    add.push({ id: o.id, ts: +o.ts, dev: o.device, session: o.session, deck: o.deck, code: o.code, no: +o.no, ms: +o.ms,
      again: o.again === 'TRUE' || o.again === '1' || o.again === 'true', kind: o.kind || 'view', ref: o.ref || undefined, synced: 1, logged: 1 });
  }
  if (add.length) {
    await db.putMany('events', add);
    for (const e of add) {
      if (e.kind === 'undo') S.undone.add(e.ref); else S.events.push(e);
    }
    S.events.sort((a, b) => a.ts - b.ts);
  }
  if (data.lastRow) await db.kv.set('evRow', Math.max(data.lastRow, 1));
}

function normDate(x) {
  x = String(x || '').trim();
  let m = x.match(/^(\d{4})-(\d{1,2})-(\d{1,2})/);
  if (m) return m[1] + '-' + m[2].padStart(2, '0') + '-' + m[3].padStart(2, '0');
  m = x.match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})/);          // d/m/yyyy or m/d/yyyy: assume day first (India)
  if (m) return m[3] + '-' + m[2].padStart(2, '0') + '-' + m[1].padStart(2, '0');
  return '';
}
async function absorbLog(data, fromRow) {
  const vals = data.values || [];
  if (fromRow <= 1 && vals.length && vals[0][0] === 'date') vals.shift();
  const base = S.logBase;
  const covered = (await db.kv.get('covered')) || {};
  for (const v of vals) {
    const [, , who, deck, , stage, , , note, from, to] = v;
    if (!deck || !OWNER.has(String(who || '').trim().toLowerCase())) continue;
    if (!/^pass[12]/.test(stage || '')) continue;
    const a = parseInt(from, 10), b = parseInt(to, 10);
    if (!(a > 0) || !(b >= a)) continue;
    const fromTrace = String(note || '').startsWith('Trace app');
    if (!fromTrace) {
      const day = normDate(v[0]);
      if (day) {
        const dd = S.logDaily[day] || (S.logDaily[day] = { min: 0, cards: 0 });
        dd.min += Math.min(parseFloat(v[7]) || 0, 600); dd.cards += parseInt(v[6], 10) || (b - a + 1);
        S.logChron.push([day, v[1] || '', deck, a, b, parseInt(v[6], 10) || (b - a + 1), Math.round(parseFloat(v[7]) || 0)]);
      }
    }
    const cov = new Set(covered[deck] || []);
    for (let n = a; n <= b; n++) {
      cov.add(n);
      if (!fromTrace) { base[deck] = base[deck] || {}; base[deck][n] = (base[deck][n] || 0) + 1; }
    }
    covered[deck] = [...cov];
  }
  S.logBase = base;
  if (S.logChron.length > 400) S.logChron = S.logChron.slice(-400);
  await db.kv.set('logDaily', S.logDaily);
  await db.kv.set('logChron', S.logChron);
  await db.kv.set('logBase', base);
  await db.kv.set('covered', covered);
  if (data.lastRow) await db.kv.set('logRow', Math.max(data.lastRow, 1));
}

async function syncEdits(found, knownId) {
  const local = await db.all('edits');
  const dirty = local.filter(e => !e.synced);
  const id = (found && found.id) || knownId;
  let remote = {};
  if (id) {
    const [f] = await batch([{ op: 'readFile', id }]);
    if (f.ok) { try { remote = JSON.parse(f.data.text).edits || {}; } catch (e) { remote = {}; } }
    await db.kv.set('editsId', id);
  }
  // newest wins, card by card
  const merged = { ...remote };
  for (const e of local) {
    const r = merged[e.key];
    if (!r || e.ts > r.ts) merged[e.key] = { deck: e.deck, code: e.code, fields: e.fields, ts: e.ts, dev: e.dev, reset: !!e.reset };
  }
  const apply = [];
  for (const [key, r] of Object.entries(merged)) {
    const mine = S.edits.get(key);
    if (!mine || r.ts > mine.ts) apply.push({ key, deck: r.deck, code: r.code, fields: r.reset ? {} : r.fields, ts: r.ts, dev: r.dev, synced: 1, reset: !!r.reset });
  }
  if (apply.length) { await db.putMany('edits', apply); apply.forEach(a => S.edits.set(a.key, a)); }
  if (dirty.length) {
    const text = JSON.stringify({ note: 'Card edits made in the Trace app. Newest edit per card wins.', updated: new Date().toISOString(), edits: merged }, null, 1);
    const [w] = await batch([{ op: 'writeFile', folderId: CONFIG.traceFolderId, name: 'edits.json', text, mime: 'application/json' }]);
    if (!w.ok) throw new Error('edits: ' + w.error);
    if (w.data && w.data.id) await db.kv.set('editsId', w.data.id);
    for (const e of dirty) e.synced = 1;
    await db.putMany('edits', dirty);
  }
}

async function pushOutbox() {
  const evs = (await db.all('events')).filter(e => !e.synced).sort((a, b) => a.ts - b.ts);
  const rows = (await db.all('logrows')).filter(r => !r.synced);
  const ops = [];
  if (evs.length) ops.push({ op: 'sheetAppend', tab: 'TraceEvents', header: EV_HEADER, dedupe: { col: 0 },
    rows: evs.map(e => { const d = new Date(e.ts); return [e.id, e.ts, ymd(d), hm(d), e.dev, e.session || '', e.deck, e.code || '', e.no || '', e.ms || '', e.again ? 1 : 0, e.kind, e.ref || '']; }) });
  if (rows.length) ops.push({ op: 'sheetAppend', tab: 'Log', dedupe: { col: 8, contains: true, keys: rows.map(r => r.id) }, rows: rows.map(r => r.row) });
  if (!ops.length) return;
  const res = await batch(ops);
  let i = 0;
  if (evs.length) { if (!res[i].ok) throw new Error('events: ' + res[i].error); evs.forEach(e => { e.synced = 1; }); await db.putMany('events', evs); i++; }
  if (rows.length) { if (!res[i].ok) throw new Error('log: ' + res[i].error); rows.forEach(r => { r.synced = 1; }); await db.putMany('logrows', rows); }
}

export async function downloadDecks(only) {
  const lib = S.library;
  if (!lib) return;
  const need = lib.decks.filter(m => (!only || only.includes(m.deck)) && m.cards_id && (() => {
    const d = S.decks.get(m.deck); return !d || !d.verified || d.version < m.version;
  })());
  status.downloading = need.length; emit();
  const failures = [];
  for (let i = 0; i < need.length; i += 25) {
    const part = need.slice(i, i + 25);
    const res = await batch(part.map(m => ({ op: 'readFile', id: m.cards_id })));
    const good = [];
    res.forEach((r, j) => {
      const m = part[j];
      try {
        if (!r.ok) throw new Error(r.error);
        const cards = parseDeck(r.data.text, m);
        good.push({ deck: m.deck, version: m.version, cards, verified: true, downloadedAt: Date.now() });
      } catch (e) { failures.push(m.deck + ': ' + e.message); }
    });
    await db.putMany('decks', good);
    good.forEach(d => S.decks.set(d.deck, d));
    status.downloading = Math.max(0, need.length - i - part.length); emit();
  }
  if (failures.length) throw new Error('Some decks did not verify: ' + failures.slice(0, 3).join('; '));
}

export const deckState = code => {
  const m = deckMeta(code), d = S.decks.get(code);
  if (!d) return 'missing';
  if (!d.verified) return 'bad';
  if (m && d.version < m.version) return 'old';
  return 'ready';
};


/* ---------------- today's target (shared with the War Map's Targets tab) ---------------- */
export function compressNos(nos) {
  const a = [...new Set(nos)].sort((x, y) => x - y), out = [];
  for (let i = 0; i < a.length; i++) {
    let j = i; while (j + 1 < a.length && a[j + 1] === a[j] + 1) j++;
    out.push(i === j ? String(a[i]) : a[i] + '-' + a[j]); i = j;
  }
  return out.join(',');
}
export function expandNos(txt, deckCards) {
  const out = [];
  String(txt || '').split(/[,\s]+/).forEach(p => {
    const m = p.match(/^(\d+)(?:-(\d+))?$/); if (!m) return;
    const a = +m[1], b = m[2] ? +m[2] : a; for (let n = a; n <= b; n++) out.push(n);
  });
  return out.length ? out : (deckCards ? Array.from({ length: deckCards }, (_, i) => i + 1) : []);
}
function curTarget() {
  if (!S.target || S.target.date !== today()) S.target = { date: today(), items: [] };
  return S.target;
}
export async function addTarget(parts) {      // parts: [{ deck, label, nos }]
  const t = curTarget();
  for (const p of parts) {
    if (!p.nos.length) continue;
    t.items.push({ id: uid('i'), item_id: 'T' + Math.random().toString(36).slice(2, 13), deck: p.deck, label: p.label, nos: p.nos, status: 'active', synced: 0, created: Date.now() });
  }
  await db.kv.set('target', t); emit();
}
export async function removeTarget(id) {
  const t = curTarget(), it = t.items.find(x => x.id === id);
  if (!it) return;
  it.status = 'pulled'; it.synced = 0;
  await db.kv.set('target', t); emit();
}
export function targetItems() { return curTarget().items.filter(i => i.status !== 'pulled'); }
const stamp = d => ymd(d) + ' ' + hm(d) + ':' + String(d.getSeconds()).padStart(2, '0');
async function syncTargets() {
  const t = curTarget();
  const ops = [{ op: 'sheetRead', tab: 'Targets', fromRow: 2 }];
  const add = t.items.filter(i => !i.synced && i.status === 'active');
  const pulled = t.items.filter(i => !i.synced && i.status === 'pulled');
  if (add.length) ops.push({ op: 'sheetAppend', tab: 'Targets', dedupe: { col: 2 }, rows: add.map((i, n) => {
    const d = new Date(i.created || Date.now());
    return [t.date, CONFIG.who, i.item_id, i.deck, '', 1, i.nos.length, compressNos(i.nos), n + 1, 'active', stamp(d), stamp(new Date()), ''];
  }) });
  for (const i of pulled) ops.push({ op: 'sheetUpdate', tab: 'Targets', keyCol: 2, key: i.item_id, set: { 9: 'pulled', 11: stamp(new Date()) } });
  const res = await batch(ops);
  status.targetNote = '';
  if (res.slice(1).some(r => !r.ok)) {
    const e = res.slice(1).find(r => !r.ok).error || '';
    status.targetNote = /not allowed|not writable|unknown op/.test(e) ? 'Your target stays on this device until the bridge script is updated.' : 'Target not sent: ' + e;
  } else {
    add.forEach(i => { i.synced = 1; }); pulled.forEach(i => { i.synced = 1; });
  }
  if (res[0].ok) {           // bring in targets set in the War Map (or on another device) for today
    for (const v of res[0].data.values || []) {
      const [date, who, item_id, deck, chunk_ids, , , card_nums, , st] = v;
      if (normDate(date) !== t.date || !OWNER.has(String(who || '').trim().toLowerCase()) || !deck) continue;
      const mine = t.items.find(i => i.item_id === item_id);
      if (mine) { if (st === 'pulled' && mine.status !== 'pulled') { mine.status = 'pulled'; mine.synced = 1; } continue; }
      if (st === 'pulled') continue;
      let nos = [];
      if (card_nums) nos = expandNos(card_nums);
      else if (chunk_ids) for (const cid of String(chunk_ids).split(/[,\s]+/)) { const ch = (S.chunks[deck] || []).find(c => c.id === cid); if (ch) for (let n = ch.from; n <= ch.to; n++) nos.push(n); }
      if (!nos.length) { const m = deckMeta(deck); if (m) nos = expandNos('', m.cards); }
      t.items.push({ id: uid('i'), item_id, deck, label: card_nums ? 'cards ' + card_nums : (chunk_ids || 'whole deck'), nos, status: 'active', synced: 1, created: Date.now(), from: 'War Map' });
    }
  }
  await db.kv.set('target', t);
}
