// T-160: the Viva Map (#/vmap) — every viva question on one screen, plus the synced viva record.
// Package → Section (the writer's generator, G1…) → Question (the unit) → Cards.
// Tile colour = tier (gold S, silver A, bronze B). Dots under a tile = full walks (reached the spine).
// Cards are blue by times walked (the same scale as the Mosaic); lessons and the spine are blue once heard; shape tells them apart.
//
// The viva record is synced like study time: tiny "study" events (ms 0) in TraceEvents —
//   code "<q>:done"         a walk reached the spine
//   code "<q>:mark:<mark>"  a Fluent / Patchy / Blank mark
// so walks and marks made on the Tab show on the Mac and later days. Nothing is ever rewritten; the Sheet only gains rows.
import { S, seen } from './store.js';
import { pkgs, pkgOf, qOf, vivaQueue, marks as localMarks } from './viva.js';
import { lessonOf } from './lesson.js';
import { plain, splitQ } from './md.js';
import { recordStudy, uid } from './sync.js';
import { vivaDoneAll } from './plan.js';

/* ---------------- section names (drafted 13 Nov from each group's questions; rename freely) ---------------- */
export const SECTIONS = {
  P1: { G1: 'Perfusion & shock signals', G2: 'Fluid responsiveness & monitors', G3: 'Fluids in sepsis', G4: 'Vasopressors & steroids', G5: 'Sepsis: definitions & SSC 2026', G6: 'Cardiogenic shock & echo', G7: 'Trauma, haemorrhage & obstetric', G8: 'Burns' },
  P2: { G1: 'Antibiotic PK/PD & resistance', G2: 'MDR Gram-negatives', G3: 'ICU-acquired infections', G4: 'Fungal infections', G5: 'Tropical fevers' },
  P3: { G1: 'CNS infection', G2: 'Neuro-monitoring', G3: 'Raised ICP & TBI', G4: 'Sodium in brain injury', G5: 'SAH & stroke', G6: 'Seizures & eclampsia', G7: 'Neuromuscular failure', G8: 'Cord injury & brain death' },
  P4: { G1: 'Modes & mechanics', G2: 'Lung stress & VILI', G3: 'Obstructive lung & APRV', G4: 'ARDS, PEEP & oxygen', G5: 'Ventilating ARDS & prone', EV: 'Evidence: ARDS trials', G6: 'Lung ultrasound', G7: 'Asynchrony & new modes', G8: 'Sedation & delirium', G9: 'Weaning & extubation' },
  P5: { G1: 'BLS & ACLS', G2: 'Arrhythmias & special arrests', G3: 'Post-arrest care', G4: 'Pulmonary embolism' },
  P6: { G1: 'AKI', G2: 'Renal replacement therapy', G3: 'Acid–base', G4: 'Electrolytes' },
  P7: { G1: 'Liver failure & paracetamol', G2: 'GI bleed & cirrhosis', G3: 'Pancreatitis', G4: 'ICU nutrition' },
  P8: { G1: 'Approach to poisoning', G2: 'Pesticides & phosphides', G3: 'Toxic alcohols & others', G4: 'Cardiotoxic drugs' },
  P10: { G1: 'Heat, cold & anaphylaxis', G2: 'Endocrine emergencies' }
};
export const secName = (pkg, g) => (SECTIONS[pkg] || {})[g] || g;
const SHORT = { P1: 'Haemodynamics', P2: 'Infection', P3: 'Neuro', P4: 'Ventilation', P5: 'Arrest, ACLS, PE', P6: 'Renal & metabolic', P7: 'Abdomen', P8: 'Toxicology', P10: 'Blind zones' };
const shortTitle = P => SHORT[P.package] || P.title;
const TIERN = { S: 'Gold', A: 'Silver', B: 'Bronze' };
const KIND = { direct: 'Direct', xvy: 'X vs Y', scenario: 'Scenario', spotter: 'Spotter', trial: 'Trial' };
const VIVA_DAY = new Date('2026-11-17T09:00:00+05:30').getTime();

/* ---------------- the synced record ---------------- */
function studyOf(pkg, q) { return (S.study || []).filter(e => !(S.undone && S.undone.has(e.id)) && e.deck === 'VIVA-' + pkg && String(e.code || '').split(':')[0] === q); }
export function vivaRecord() {
  const done = {}, mark = {}, heard = {};
  for (const e of S.study || []) {
    if (S.undone && S.undone.has(e.id)) continue;
    const pkg = String(e.deck || '').replace(/^VIVA-/, ''); if (!pkg || pkg === e.deck) continue;
    const [q, kind, m] = String(e.code || '').split(':'); if (!q) continue;
    const k = pkg + '|' + q;
    if (kind === 'done') (done[k] || (done[k] = new Set())).add(Math.round(e.ts / 60000));     // one walk per minute at most
    else if (kind === 'mark' && m) { if (!mark[k] || mark[k].ts < e.ts) mark[k] = { ts: e.ts, mark: m }; }
    else if (kind === 'vq' || kind === 'vclose' || kind === 'spine') heard[k + '|' + kind] = 1;
  }
  return { done, mark, heard };
}
// T-165: a walk of a question is any of: reaching its spine ("<q>:done"), marking it Fluent/Patchy/Blank (marks are
// given at the spine), or a session in which every card of the question was walked. Times within 30 minutes of each
// other are one walk, so a session that does all three counts once. Works from data already synced from every device.
let WC = null, WKEY = '';
function walkTimes(pkg, q) {
  const key = (S.events || []).length + '|' + (S.study || []).length;
  if (WKEY !== key) { WC = new Map(); WKEY = key; }
  const k = pkg + '|' + q; if (WC.has(k)) return WC.get(k);
  const ts = [];
  for (const e of S.study || []) {
    if (S.undone && S.undone.has(e.id)) continue;
    if (e.deck !== 'VIVA-' + pkg) continue;
    const [qq, kind] = String(e.code || '').split(':');
    if (qq === q && (kind === 'done' || kind === 'mark')) ts.push(e.ts);
  }
  const cards = vivaQueue(pkg, q).list.filter(c => !c.vq.rep);
  if (cards.length) {
    const want = new Set(cards.map(c => c.deck + '|' + c.no)), bySess = new Map();
    for (const e of S.events || []) {
      if (!want.has(e.deck + '|' + e.no) || (S.undone && S.undone.has(e.id))) continue;
      const m = bySess.get(e.session) || bySess.set(e.session, new Map()).get(e.session);
      m.set(e.deck + '|' + e.no, Math.max(m.get(e.deck + '|' + e.no) || 0, e.ts));
    }
    for (const m of bySess.values()) if (m.size === want.size) ts.push(Math.max(...m.values()));
  }
  ts.sort((a, b) => a - b);
  const walks = []; for (const t of ts) if (!walks.length || t - walks[walks.length - 1] > 30 * 60e3) walks.push(t); else walks[walks.length - 1] = t;
  WC.set(k, walks); return walks;
}
export const walksOf = (R, pkg, q) => walkTimes(pkg, q).length;
export function noteDone(pkg, q, session) {
  return recordStudy({ id: uid('t'), ts: Date.now(), deck: 'VIVA-' + pkg, code: q + ':done', ms: 0, session: session || 'vmap' }).catch(() => {});
}
export function noteMark(pkg, q, mark, session) {
  return recordStudy({ id: uid('t'), ts: Date.now(), deck: 'VIVA-' + pkg, code: q + ':mark:' + mark, ms: 0, session: session || 'vmap' }).catch(() => {});
}
// once per device and profile: what was kept only on this device (walks done, marks) goes into the synced record,
// with its original times; ids are fixed, so running it twice adds nothing
export async function migrateViva(P) {
  if (P.get('vivaSync1', false)) return 0;
  const have = new Set((S.study || []).map(e => e.id)), dev = S.device || 'dev';
  let n = 0;
  const put = async (pkg, q, ts, code) => {
    const id = 'vm' + dev + pkg + q + code.replace(/\W/g, '') + ts;
    if (have.has(id)) return;
    await recordStudy({ id, ts, deck: 'VIVA-' + pkg, code, ms: 0, session: 'migrate' }); n++;
  };
  const vd = vivaDoneAll();
  for (const [k, list] of Object.entries(vd)) { const [pkg, q] = k.split('|'); for (const ts of list || []) await put(pkg, q, ts, q + ':done'); }
  const m = await localMarks();
  for (const [k, list] of Object.entries(m)) { const [pkg, q] = k.split('|'); for (const x of list || []) await put(pkg, q, x.ts, q + ':mark:' + x.mark); }
  P.set('vivaSync1', Date.now());
  return n;
}

/* ---------------- the questions, flattened ---------------- */
const lessonMin = q => { const t = [q.open, q.close, ...q.steps.map(s => s.lesson)].reduce((a, L) => a + (L && L.text ? L.text.length : 0), 0); return Math.max(1, Math.round(t / 720)); };
function allQs() {
  const out = [];
  for (const P of pkgs()) P.questions.forEach((q, i) => out.push({ pkg: P.package, P, q, n: i + 1, g: q.gen, sec: secName(P.package, q.gen), min: lessonMin(q) }));
  return out;
}
const hay = x => (x.q.text + ' ' + x.sec + ' ' + shortTitle(x.P) + ' ' + x.q.q).toLowerCase();   // the question, its section and package (spines matched too much)

/* ---------------- state ---------------- */
let st = null, ctx = null;
const defaults = () => ({ tab: 'map', tiers: ['S', 'A', 'B'], notWalked: false, q: '', pick: false, list: [], ex: [], pkg: '', arrange: 'tier', ptiers: ['S'], pex: [] });
function load() { st = { ...defaults(), ...(ctx.P.get('vmap', {}) || {}) }; st.q = st.q || ''; }
function save() { const { q, ...keep } = st; ctx.P.set('vmap', keep); }

/* ---------------- small pieces ---------------- */
const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
function dots(w) { if (!w) return '<span class="vm-dots"></span>'; return `<span class="vm-dots">${'<i></i>'.repeat(Math.min(3, w))}${w > 3 ? `<b>+${w - 3}</b>` : ''}</span>`; }
function tile(x, R, extra = '') {
  const w = walksOf(R, x.pkg, x.q.q);
  return `<span class="vm-tw${extra}"><button class="vm-t vm-${x.q.tier}" data-vmq="${esc(x.pkg)}|${esc(x.q.q)}" title="${esc(x.q.text)}" aria-label="${esc(x.pkg)} question ${x.n}, ${TIERN[x.q.tier] || x.q.tier}${w ? ', walked ' + w + ' time' + (w === 1 ? '' : 's') : ''}: ${esc(x.q.text)}">${x.n}</button>${dots(w)}</span>`;
}
const bar = (a, b, cls = '') => `<span class="vm-bar ${cls}"><i style="width:${b ? Math.round(100 * a / b) : 0}%"></i></span>`;
function bullseye(on) { return `<svg class="vm-bull${on ? ' on' : ''}" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10.5"/><circle class="r2" cx="12" cy="12" r="7.5"/><circle class="c" cx="12" cy="12" r="4.5"/></svg>`; }
const shade = n => 's' + Math.min(3, n || 0);
function heardOf(R, pkg, q, kind) {
  if (R.heard[pkg + '|' + q + '|' + kind]) return true;
  const loc = ctx.P.get('vivaHeard', {}) || {}; if (loc[pkg + '|' + q + '|' + kind]) return true;
  return walksOf(R, pkg, q) > 0;
}
function mosaic(x, R) {
  const { pkg } = x, qid = x.q.q, cards = vivaQueue(pkg, qid).list;
  const L = k => `<i class="vm-ml${heardOf(R, pkg, qid, k) ? ' on' : ''}"></i>`;
  return `<span class="vm-mos" aria-hidden="true">${lessonOf(pkg, qid, 'o') ? L('vq') : ''}${cards.map(c => `<i class="vm-mc ${shade(seen(c.deck, c.no))}"></i>`).join('')}${lessonOf(pkg, qid, 'c') ? L('vclose') : ''}${bullseye(walksOf(R, pkg, qid) > 0)}</span>`;
}

/* ---------------- the walk list ---------------- */
function listQs(all) {
  const ex = new Set(st.ex), seenQ = new Set(), out = [];
  for (const e of st.list) {
    const add = all.filter(x => x.pkg === e.pkg && (e.q ? x.q.q === e.q : x.g === e.g));
    for (const x of add) { const k = x.pkg + '|' + x.q.q; if (ex.has(k) || seenQ.has(k)) continue; seenQ.add(k); out.push(x); }
  }
  return out;
}
function buildWalk(xs) {
  const list = [], first = new Map();
  for (const x of xs) for (const c of vivaQueue(x.pkg, x.q.q).list) {
    const k = c.deck + '|' + c.code, rep = first.has(k) ? first.get(k) : null;
    if (!rep) first.set(k, x.q.q);
    list.push({ ...c, vq: { ...c.vq, rep: c.vq.rep || rep } });
  }
  return list;
}
function walk(xs, label) {
  const list = buildWalk(xs);
  if (!list.length) { ctx.toast('These cards are not on this device yet.'); return; }
  ctx.startFlow(list, { viva: xs[0].pkg, label, returnTo: '#/vmap' });
}
const inList = (pkg, g) => st.list.findIndex(e => e.pkg === pkg && !e.q && e.g === g);

/* ---------------- the screen ---------------- */
export function renderVivaMap(c) {
  ctx = c; if (!st) load();
  const sc = c.app.querySelector('.vmap .scroll'), y = sc ? sc.scrollTop : 0;
  const all = allQs(), R = vivaRecord();
  const qq = st.q.trim().toLowerCase(), hit = x => !qq || hay(x).includes(qq);
  const show = x => st.tiers.includes(x.q.tier) && (!st.notWalked || !walksOf(R, x.pkg, x.q.q)) && hit(x);
  const days = Math.max(0, Math.floor((VIVA_DAY - Date.now()) / 864e5));
  const sa = all.filter(x => 'SA'.includes(x.q.tier) && !walksOf(R, x.pkg, x.q.q)).length;
  const tabs = [['map', 'Map'], ['pkg', 'Package'], ['prio', 'Priority']];
  const lq = listQs(all), lmin = lq.reduce((a, x) => a + x.min, 0);
  let body = '';
  if (st.tab === 'map') body = mapView(all, R, show);
  else if (st.tab === 'pkg') body = pkgView(all, R, show);
  else body = prioView(all, R, hit);
  c.app.innerHTML = `<div class="screen vmap">
    <header class="top"><a class="iconbtn" href="#/viva" aria-label="Back to Viva">${c.ICON.back}</a><span class="tt"><span class="mono kick">VIVA MAP · ${pkgs().length} PACKAGES · ${all.length} QUESTIONS</span><span class="h1s">Viva Map</span></span>
      <span class="seg vm-tabs">${tabs.map(([k, l]) => `<button class="${st.tab === k ? 'on' : ''}" data-vmtab="${k}">${l}</button>`).join('')}</span></header>
    <div class="scroll pad">
      <section class="vm-sum">
        <div class="vm-tiers">${['S', 'A', 'B'].map(t => { const xs = all.filter(x => x.q.tier === t), w = xs.filter(x => walksOf(R, x.pkg, x.q.q)).length; return `<div class="vm-tr"><i class="vm-sw vm-${t}"></i><b>${TIERN[t]}</b>${bar(w, xs.length, 'vm-' + t)}<span class="mono">${w}/${xs.length} walked</span></div>`; }).join('')}</div>
        <div class="vm-days"><span class="vm-dn">${days} day${days === 1 ? '' : 's'} left</span><span>Gold + silver not yet walked: <b>${sa}</b>${days ? ` → about <b>${Math.ceil(sa / days)}</b> a day` : ''}</span></div>
      </section>
      <div class="vm-ctl">
        <label class="vm-search">Search <input type="search" id="vm-q" value="${esc(st.q)}" placeholder="brain death, pregnancy, REBOA…" autocomplete="off"></label>
        ${st.tab !== 'prio' ? `<span class="mono vm-lab">SHOW</span>${['S', 'A', 'B'].map(t => `<button class="chip${st.tiers.includes(t) ? ' on' : ''}" data-vmtier="${t}">${TIERN[t]}</button>`).join('')}<button class="chip${st.notWalked ? ' on' : ''}" data-vmnw>Not walked only</button>` : ''}
        ${st.tab === 'map' ? `<span class="mono vm-lab">SELECT</span><button class="chip${st.pick ? ' on' : ''}" data-vmpick>${st.pick ? '✓ Picking' : 'Pick to walk'}</button>${st.pick ? `<button class="chip" data-vmall="S">+ All gold</button><button class="chip" data-vmall="SA">+ Gold &amp; silver</button>` : ''}` : ''}
      </div>
      <p class="vm-legend mono"><span><i class="vm-sw vm-S"></i>Gold = tier S</span><span><i class="vm-sw vm-A"></i>Silver = A</span><span><i class="vm-sw vm-B"></i>Bronze = B</span><span><span class="vm-dots"><i></i><i></i><i></i></span> one dot per full walk (to the spine)</span>${st.tab === 'pkg' ? `<span><i class="vm-mc s0"></i><i class="vm-mc s1"></i><i class="vm-mc s2"></i><i class="vm-mc s3"></i> cards: white, ×1, ×2, ×3+</span><span><i class="vm-ml on"></i> lesson heard</span><span>${bullseye(true)} spine</span>` : ''}${st.pick && st.tab === 'map' ? '<span class="vm-hint">Tick a section to add it · tap a question to leave it out (or add it alone)</span>' : ''}</p>
      ${body}
      ${lq.length ? '<div class="vm-traypad"></div>' : ''}
    </div>
    ${lq.length ? `<div class="vm-tray"><span class="vm-tt"><span class="mono kick">WALK LIST</span><span><b>${lq.length}</b> question${lq.length === 1 ? '' : 's'} · about <b>${lmin >= 60 ? Math.floor(lmin / 60) + ' h ' : ''}${lmin % 60} m</b>${st.ex.length ? ` · ${st.ex.length} left out` : ''}</span></span>
      <span class="vm-pills">${st.list.map((e, i) => `<span class="vm-pill"><b class="mono">${i + 1}</b><span>${esc(e.pkg)} ${e.q ? 'Q' + ((qOf(e.pkg, e.q) && pkgOf(e.pkg).questions.indexOf(qOf(e.pkg, e.q)) + 1) || '') : esc(e.g) + ' ' + esc(secName(e.pkg, e.g))}</span><button data-vmup="${i}" aria-label="Move earlier"${i ? '' : ' disabled'}>↑</button><button data-vmdn="${i}" aria-label="Move later"${i < st.list.length - 1 ? '' : ' disabled'}>↓</button><button data-vmrm="${i}" aria-label="Remove">×</button></span>`).join('')}</span>
      <span class="vm-ta"><button class="chip" data-vmclear>Clear</button><button class="pillbtn" data-vmgo>${c.ICON.walkS} Start flow</button></span></div>` : ''}
    ${c.nav('flow')}
  </div>`;
  const s2 = c.app.querySelector('.vmap .scroll'); if (s2 && y) s2.scrollTop = y;
  bind(all, R);
}
const rerender = () => renderVivaMap(ctx);

function mapView(all, R, show) {
  return `<div class="vm-map">${pkgs().map(P => {
    const xs = all.filter(x => x.pkg === P.package), w = xs.filter(x => walksOf(R, x.pkg, x.q.q)).length;
    const gens = []; xs.forEach(x => { let g = gens.find(y => y.g === x.g); if (!g) gens.push(g = { g: x.g, xs: [] }); g.xs.push(x); });
    const secs = gens.map(g => {
      const vis = g.xs.filter(show); if (!vis.length) return '';
      const at = inList(P.package, g.g), on = at >= 0, ex = new Set(st.ex);
      const head = st.pick ? `<button class="vm-sh" data-vmsec="${esc(P.package)}|${esc(g.g)}" aria-pressed="${on}"><i class="vm-box${on ? ' on' : ''}">${on ? '✓' : ''}</i>${on ? `<b class="vm-ord">${at + 1}</b>` : ''}<b class="g">${esc(g.g)}</b> ${esc(secName(P.package, g.g))} · ${g.xs.filter(x => walksOf(R, x.pkg, x.q.q)).length}/${g.xs.length}</button>`
        : `<span class="vm-sh"><b class="g">${esc(g.g)}</b> ${esc(secName(P.package, g.g))} · ${g.xs.filter(x => walksOf(R, x.pkg, x.q.q)).length}/${g.xs.length}</span>`;
      const solo = k => st.list.some(e => e.q && e.pkg + '|' + e.q === k);
      return `<div class="vm-sec${on ? ' on' : ''}">${head}<div class="vm-tiles">${vis.map(x => { const k = x.pkg + '|' + x.q.q; return tile(x, R, on ? (ex.has(k) ? ' off' : ' sel') : solo(k) ? ' sel' : ''); }).join('')}</div></div>`;
    }).join('');
    if (!secs) return '';
    return `<section class="vm-pkg"><button class="vm-pl" data-vmpkg="${esc(P.package)}"><span class="mono">${esc(P.package)}</span><b>${esc(shortTitle(P))}</b>${bar(w, xs.length)}<span class="mono">${w}/${xs.length} walked</span></button><div class="vm-secs">${secs}</div></section>`;
  }).join('') || '<p class="muted">Nothing matches.</p>'}</div>`;
}

function pkgView(all, R, show) {
  const ps = pkgs(); if (!st.pkg || !pkgOf(st.pkg)) st.pkg = ps.length ? ps[0].package : '';
  const P = pkgOf(st.pkg); if (!P) return '';
  const xs = all.filter(x => x.pkg === P.package);
  const gens = []; xs.forEach(x => { let g = gens.find(y => y.g === x.g); if (!g) gens.push(g = { g: x.g, xs: [] }); g.xs.push(x); });
  return `<div class="chips vm-pchips">${ps.map(p => `<button class="chip${p.package === st.pkg ? ' on' : ''}" data-vmp="${esc(p.package)}">${esc(p.package)} · ${esc(shortTitle(p))}</button>`).join('')}</div>
  <div class="vm-pgrid">${gens.map(g => {
    const vis = g.xs.filter(show); if (!vis.length) return '';
    const w = g.xs.filter(x => walksOf(R, x.pkg, x.q.q)).length, mins = g.xs.reduce((a, x) => a + x.min, 0);
    return `<section class="vm-psec"><div class="vm-psh"><span><span class="mono kick">${esc(g.g)} · ${g.xs.length} QUESTIONS · ${mins} MIN</span><b>${esc(secName(P.package, g.g))}</b></span><span class="vm-psr">${bar(w, g.xs.length)}<span class="mono">${w}/${g.xs.length}</span><button class="chip" data-vmaddsec="${esc(P.package)}|${esc(g.g)}">${inList(P.package, g.g) >= 0 ? '✓ In walk list' : '+ Walk list'}</button></span></div>
      ${vis.map(x => `<div class="vm-row">${tile(x, R)}<button class="vm-rt" data-vmq="${esc(x.pkg)}|${esc(x.q.q)}">${esc(plain(x.q.text))}<small class="mono">${KIND[x.q.kind] || ''} · ${x.q.steps.length} cards · ${x.min} min</small></button>${mosaic(x, R)}</div>`).join('')}</section>`;
  }).join('')}</div>`;
}

function prioView(all, R, hit) {
  const pex = new Set(st.pex), order = pkgs().map(p => p.package);
  let xs = all.filter(x => st.ptiers.includes(x.q.tier) && hit(x));
  const ti = t => 'SAB'.indexOf(t);
  xs.sort(st.arrange === 'tier' ? (a, b) => ti(a.q.tier) - ti(b.q.tier) || order.indexOf(a.pkg) - order.indexOf(b.pkg) || a.n - b.n
    : (a, b) => order.indexOf(a.pkg) - order.indexOf(b.pkg) || ti(a.q.tier) - ti(b.q.tier) || a.n - b.n);
  const ticked = xs.filter(x => !pex.has(x.pkg + '|' + x.q.q));
  let last = '';
  const rows = xs.map(x => {
    const grp = st.arrange === 'tier' ? TIERN[x.q.tier] + ' · ' + x.pkg + ' ' + shortTitle(x.P) : x.pkg + ' ' + shortTitle(x.P);
    const head = grp !== last ? `<div class="vm-ph mono">${esc(grp.toUpperCase())}</div>` : ''; last = grp;
    const k = x.pkg + '|' + x.q.q, on = !pex.has(k);
    return head + `<div class="vm-prow${on ? '' : ' off'}"><input type="checkbox" data-vmpx="${esc(k)}" ${on ? 'checked' : ''} aria-label="Include in the walk">${tile(x, R)}<button class="vm-rt" data-vmq="${esc(k)}">${esc(plain(x.q.text))}<small class="mono">${esc(x.sec)} · ${x.q.steps.length} cards · ${x.min} min</small></button></div>`;
  }).join('');
  return `<div class="vm-ctl"><span class="mono vm-lab">ARRANGE</span><button class="chip${st.arrange === 'tier' ? ' on' : ''}" data-vmarr="tier">Tier, then system</button><button class="chip${st.arrange === 'sys' ? ' on' : ''}" data-vmarr="sys">System, then tier</button>
    <span class="mono vm-lab">SHOW</span>${['S', 'A', 'B'].map(t => `<button class="chip${st.ptiers.includes(t) ? ' on' : ''}" data-vmpt="${t}">${TIERN[t]}</button>`).join('')}
    <button class="pillbtn" data-vmpgo ${ticked.length ? '' : 'disabled'}>${ctx.ICON.walkS} Walk the ${ticked.length} ticked</button></div>
    <p class="muted small">"Tier, then system" keeps study order inside each tier: P1 → P10, section by section. Untick a row to leave it out.</p>
    <section class="vm-plist">${rows || '<p class="muted">Nothing matches.</p>'}</section>`;
}

/* ---------------- the opened question ---------------- */
function openQ(pkg, qid) {
  const x = allQs().find(y => y.pkg === pkg && y.q.q === qid); if (!x) return;
  const R = vivaRecord(), w = walksOf(R, pkg, qid), mk = R.mark[pkg + '|' + qid], cards = vivaQueue(pkg, qid).list;
  const sib = allQs().filter(y => y.pkg === pkg && y.g === x.g);
  const lessonRow = (k, label) => `<li><span class="vm-line"><span class="vm-ic"><i class="vm-ml big${heardOf(R, pkg, qid, k) ? ' on' : ''}"></i></span><span class="vm-st"><b>${label}</b><small class="mono">${heardOf(R, pkg, qid, k) ? 'heard' : 'not yet'}</small></span></span></li>`;
  const rows = (lessonOf(pkg, qid, 'o') ? lessonRow('vq', 'Opening lesson') : '') +
    cards.map((c, j) => { const n = seen(c.deck, c.no); return `<li><span class="vm-line"><button class="vm-step" data-vmlook="${j}" aria-label="Look at card ${j + 1} (nothing is counted)"><span class="vm-ic"><i class="vm-mc big ${shade(n)}">${j + 1}</i></span><span class="vm-st"><b>${esc(plain(splitQ(c.q).head).replace(/:$/, ''))}</b><small class="mono">${esc(c.deck)} · ${esc(c.code)} · walked ×${n}${c.vq.rep ? ' · seen above in this question' : ''}</small></span></button><button class="chip vm-go" data-vmstart="${j}">Start here ›</button></span></li>`; }).join('') +
    (lessonOf(pkg, qid, 'c') ? lessonRow('vclose', 'Closing lesson') : '') +
    `<li><span class="vm-line"><span class="vm-ic">${bullseye(w > 0)}</span><span class="vm-st"><b>Spine</b><small class="mono">${w ? 'walked ×' + w : 'not yet'} · say it in 60 s</small></span></span></li>`;
  const wrap = document.createElement('div'); wrap.className = 'modal vm-modal';
  wrap.innerHTML = `<div class="sheet vm-q vm-q-${x.q.tier}" role="dialog" aria-label="${esc(x.q.text)}">
    <div class="vm-qh"><nav class="mono">${esc(pkg)} ${esc(shortTitle(x.P))} › ${esc(x.g)} ${esc(x.sec)} › Q${x.n} of ${x.P.questions.length}</nav><button class="iconbtn" data-vmclose aria-label="Close">${ctx.ICON.close || '×'}</button></div>
    <p class="vm-tags"><span class="vm-badge vm-${x.q.tier}">${TIERN[x.q.tier]} · Tier ${x.q.tier}</span>${x.q.kind ? `<span class="vm-tag mono">${KIND[x.q.kind] || x.q.kind}</span>` : ''}${mk ? `<span class="vm-tag mono">last mark: ${esc(mk.mark)}</span>` : ''}<span class="vm-tag mono">${w ? 'walked ×' + w : 'not walked yet'}</span></p>
    <h2 class="vm-qt">${esc(plain(x.q.text))}</h2>
    <p class="muted small">${cards.length} cards · lessons about ${x.min} min</p>
    <div class="vm-btns"><button class="pillbtn" data-vmwalk>${ctx.ICON.walkS} Walk from the start</button><button class="chip" data-vmspine>Spine only · 60 s</button><button class="chip" data-vmadd>${st.list.some(e => e.q === qid && e.pkg === pkg) ? '✓ In walk list' : '+ Add to walk list'}</button></div>
    <div class="vm-spine" hidden><span class="mono vm-clock">1:00</span><ol>${(x.q.spine || []).map(l => `<li>${esc(plain(l))}</li>`).join('')}</ol></div>
    <h3 class="mono kick">THE WALK · TAP A CARD TO LOOK · START HERE TO WALK FROM IT</h3>
    <ol class="vm-walk">${rows}</ol>
    <div class="vm-qf"><span class="mono vm-lab">MARK</span>${['fluent', 'patchy', 'blank'].map(m => `<button class="chip${mk && mk.mark === m ? ' on' : ''}" data-vmmark="${m}">${m[0].toUpperCase() + m.slice(1)}</button>`).join('')}
      <span class="vm-sib">${sib.map(y => tile(y, R, y.q.q === qid ? ' sel' : '')).join('')}</span></div>
  </div>`;
  document.body.appendChild(wrap);
  const close = () => { wrap.remove(); clearInterval(tm); };
  let tm = null;
  wrap.onclick = e => { if (e.target === wrap) close(); };
  wrap.querySelector('[data-vmclose]').onclick = close;
  wrap.querySelector('[data-vmwalk]').onclick = () => { close(); walk([x], 'Viva ' + pkg + ' · Q' + x.n); };
  // looking at a card is a browse: nothing is timed, counted or logged
  wrap.querySelectorAll('[data-vmlook]').forEach(b => b.onclick = () => {
    const j = +b.dataset.vmlook, list = cards.map(c => { const { vq, ...rest } = c; return rest; });
    close(); if (list.length) ctx.startFlow(list, { browse: true, start: j, label: 'Looking · ' + pkg + ' Q' + x.n, returnTo: '#/vmap' });
  });
  wrap.querySelectorAll('[data-vmstart]').forEach(b => b.onclick = () => {
    const j = +b.dataset.vmstart, list = buildWalk([x]).slice(j);
    close(); if (list.length) ctx.startFlow(list, { viva: pkg, label: 'Viva ' + pkg + ' · Q' + x.n + ' from card ' + (j + 1), returnTo: '#/vmap' });
  });
  wrap.querySelector('[data-vmadd]').onclick = () => { if (!st.list.some(e => e.q === qid && e.pkg === pkg)) st.list.push({ pkg, q: qid }); save(); close(); rerender(); };
  wrap.querySelector('[data-vmspine]').onclick = () => {
    const box = wrap.querySelector('.vm-spine'), clk = box.querySelector('.vm-clock'); box.hidden = false; let t = 60; clk.textContent = '1:00'; clearInterval(tm);
    tm = setInterval(() => { t--; clk.textContent = Math.floor(t / 60) + ':' + String(t % 60).padStart(2, '0'); if (t <= 0) { clearInterval(tm); clk.textContent = 'Time'; } }, 1000);
  };
  wrap.querySelectorAll('[data-vmmark]').forEach(b => b.onclick = async () => { await ctx.setMark(pkg, qid, b.dataset.vmmark); await noteMark(pkg, qid, b.dataset.vmmark); close(); openQ(pkg, qid); rerender(); });
  wrap.querySelectorAll('.vm-sib [data-vmq]').forEach(b => b.onclick = () => { const [p, q] = b.dataset.vmq.split('|'); close(); openQ(p, q); });
}

/* ---------------- events ---------------- */
function bind(all, R) {
  const a = ctx.app, on = (sel, fn) => a.querySelectorAll(sel).forEach(b => b.onclick = e => { e.stopPropagation(); fn(b, e); });
  on('[data-vmtab]', b => { st.tab = b.dataset.vmtab; save(); rerender(); });
  on('[data-vmtier]', b => { const t = b.dataset.vmtier; st.tiers = st.tiers.includes(t) ? st.tiers.filter(x => x !== t) : st.tiers.concat(t); if (!st.tiers.length) st.tiers = [t]; save(); rerender(); });
  on('[data-vmnw]', () => { st.notWalked = !st.notWalked; save(); rerender(); });
  on('[data-vmpick]', () => { st.pick = !st.pick; save(); rerender(); });
  on('[data-vmall]', b => { const ts = b.dataset.vmall; all.filter(x => ts.includes(x.q.tier)).forEach(x => { const k = x.pkg + '|' + x.q.q; if (!listQs(all).some(y => y.pkg + '|' + y.q.q === k)) st.list.push({ pkg: x.pkg, q: x.q.q }); st.ex = st.ex.filter(e => e !== k); }); save(); rerender(); });
  on('[data-vmsec]', b => { const [p, g] = b.dataset.vmsec.split('|'), i = inList(p, g); if (i >= 0) st.list.splice(i, 1); else st.list.push({ pkg: p, g }); save(); rerender(); });
  on('[data-vmaddsec]', b => { const [p, g] = b.dataset.vmaddsec.split('|'), i = inList(p, g); if (i >= 0) st.list.splice(i, 1); else st.list.push({ pkg: p, g }); save(); rerender(); });
  on('[data-vmpkg]', b => { st.tab = 'pkg'; st.pkg = b.dataset.vmpkg; save(); rerender(); });
  on('[data-vmp]', b => { st.pkg = b.dataset.vmp; save(); rerender(); });
  on('[data-vmup]', b => { const i = +b.dataset.vmup; if (i > 0) { [st.list[i - 1], st.list[i]] = [st.list[i], st.list[i - 1]]; save(); rerender(); } });
  on('[data-vmdn]', b => { const i = +b.dataset.vmdn; if (i < st.list.length - 1) { [st.list[i + 1], st.list[i]] = [st.list[i], st.list[i + 1]]; save(); rerender(); } });
  on('[data-vmrm]', b => { const e = st.list.splice(+b.dataset.vmrm, 1)[0]; if (e && !e.q) st.ex = st.ex.filter(k => !k.startsWith(e.pkg + '|') || !all.some(x => x.pkg + '|' + x.q.q === k && x.g === e.g)); save(); rerender(); });
  on('[data-vmclear]', () => { st.list = []; st.ex = []; save(); rerender(); });
  on('[data-vmgo]', () => { const xs = listQs(all); if (xs.length) walk(xs, 'Viva Map · ' + xs.length + ' question' + (xs.length === 1 ? '' : 's')); });
  on('[data-vmarr]', b => { st.arrange = b.dataset.vmarr; save(); rerender(); });
  on('[data-vmpt]', b => { const t = b.dataset.vmpt; st.ptiers = st.ptiers.includes(t) ? st.ptiers.filter(x => x !== t) : st.ptiers.concat(t); if (!st.ptiers.length) st.ptiers = [t]; save(); rerender(); });
  a.querySelectorAll('[data-vmpx]').forEach(i => i.onchange = () => { const k = i.dataset.vmpx; st.pex = i.checked ? st.pex.filter(x => x !== k) : st.pex.concat(k); save(); rerender(); });
  on('[data-vmpgo]', () => {
    const pex = new Set(st.pex), order = pkgs().map(p => p.package), ti = t => 'SAB'.indexOf(t), qq = st.q.trim().toLowerCase();
    let xs = all.filter(x => st.ptiers.includes(x.q.tier) && !pex.has(x.pkg + '|' + x.q.q) && (!qq || hay(x).includes(qq)));
    xs.sort(st.arrange === 'tier' ? (p, q) => ti(p.q.tier) - ti(q.q.tier) || order.indexOf(p.pkg) - order.indexOf(q.pkg) || p.n - q.n : (p, q) => order.indexOf(p.pkg) - order.indexOf(q.pkg) || ti(p.q.tier) - ti(q.q.tier) || p.n - q.n);
    if (xs.length) walk(xs, 'Viva priority · ' + xs.length + ' questions');
  });
  // tiles: in picking mode on the map they add/leave out; otherwise they open the question
  a.querySelectorAll('[data-vmq]').forEach(b => b.onclick = e => {
    e.stopPropagation(); const [p, q] = b.dataset.vmq.split('|'), k = p + '|' + q, x = all.find(y => y.pkg === p && y.q.q === q);
    if (st.tab === 'map' && st.pick && x) {
      if (inList(p, x.g) >= 0) st.ex = st.ex.includes(k) ? st.ex.filter(y => y !== k) : st.ex.concat(k);
      else { const i = st.list.findIndex(y => y.q && y.pkg === p && y.q === q); if (i >= 0) st.list.splice(i, 1); else st.list.push({ pkg: p, q }); }
      save(); rerender(); return;
    }
    openQ(p, q);
  });
  const inp = a.querySelector('#vm-q');
  if (inp) { inp.oninput = () => { st.q = inp.value; clearTimeout(inp._t); inp._t = setTimeout(() => { const pos = inp.selectionStart; rerender(); const i2 = ctx.app.querySelector('#vm-q'); if (i2) { i2.focus(); try { i2.setSelectionRange(pos, pos); } catch (e) {} } }, 250); }; }
}
