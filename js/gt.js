// T-191: GTs — each DocTutorials Grand Test as an answer sheet (150 tiles), by system, a page per system, trends across
// papers, and a walk through the questions as GT cards (Try / Read, Explain pane with tabs for linked cards and repeats).
// Data: data/gt/index.json + data/gt/<GT>.json (questions, both people's results, written GT cards). Kept on the device.
import { S, cardsOf } from './store.js';
import { render, inline, plain } from './md.js';
import { IS_HT, CHANNEL } from './config.js';
import { db } from './db.js';

const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ch]));
const ME = IS_HT ? 'HT' : 'Trace', OTHER = IS_HT ? 'Trace' : 'HT';
const OTHER_NAME = IS_HT ? 'Naven' : 'HT';
const LK = (CHANNEL === 'test' ? 'trace-test.' : 'trace.') + (IS_HT ? 'ht.' : '') + 'gt.';
const lsGet = (k, d) => { try { const v = localStorage.getItem(LK + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } };
const lsSet = (k, v) => { try { localStorage.setItem(LK + k, JSON.stringify(v)); } catch (e) { /* */ } };
const ssGet = (k, d) => { try { const v = sessionStorage.getItem(LK + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } };
const ssSet = (k, v) => { try { sessionStorage.setItem(LK + k, JSON.stringify(v)); } catch (e) { /* */ } };

/* ---------------- data ---------------- */
const G = { index: null, papers: {}, loading: null };
export async function loadGT(force) {
  if (G.loading && !force) return G.loading;
  G.loading = (async () => {
    if (!G.index) { const c = await db.kv.get('gt:index').catch(() => null); if (c) { G.index = c; for (const p of c.papers) { const d = await db.kv.get('gt:' + p.id).catch(() => null); if (d) G.papers[p.id] = d; } } }
    try {
      const r = await fetch('data/gt/index.json?t=' + Date.now(), { cache: 'no-store' });
      if (r.ok) {
        const ix = await r.json();
        for (const p of ix.papers) {
          const have = G.papers[p.id];
          if (have && have.version === p.version) continue;
          const pr = await fetch('data/gt/' + p.file + '?v=' + encodeURIComponent(p.version), { cache: 'no-store' });
          if (pr.ok) { const d = await pr.json(); G.papers[p.id] = d; db.kv.set('gt:' + p.id, d).catch(() => {}); }
        }
        G.index = ix; db.kv.set('gt:index', ix).catch(() => {});
      }
    } catch (e) { /* offline: keep the stored copy */ }
    return G;
  })();
  return G.loading;
}
export const gtCount = () => (G.index ? G.index.papers.length : 0);
const papers = () => (G.index ? G.index.papers.map(p => G.papers[p.id]).filter(Boolean) : []).sort((a, b) => a.date.localeCompare(b.date));
const paper = id => G.papers[id];
const person = (P, who) => (P.people && P.people[who]) || null;
const resOf = (P, who, n) => { const p = person(P, who); return p ? p.res[n - 1] : null; };
const guessOf = (P, who, n) => { const p = person(P, who); return !!(p && p.guess.includes(n)); };
const pickOf = (P, who, n) => { const p = person(P, who); return p ? (p.picks[String(n)] || null) : null; };
const needs = (P, who, n) => resOf(P, who, n) !== 'r' || guessOf(P, who, n);
const missed = (P, who, n) => !!person(P, who) && (resOf(P, who, n) !== 'r' || guessOf(P, who, n));
const cardOf = (P, n) => (P.cards && P.cards[String(n)]) || null;
const qOf = (P, n) => P.q[n - 1];
const sysOf = (P, n) => { const c = cardOf(P, n); return (c && c.sys) || qOf(P, n).sys || 'Unsorted'; };
const topicOf = (P, n) => { const c = cardOf(P, n); return (c && c.topic) || qOf(P, n).topic || ''; };
const shortSys = s => s.replace(/ Disorders$/, '').replace('Gastrointestinal & Hepatological', 'GI & liver').replace('Electrolyte and Acid Base', 'Electrolytes & acid–base').replace('Research - Biostats & Epi', 'Biostats & research').replace('Basics of Critical Care Medicine', 'Basics of critical care');
function repeatsOf(P, n) {
  const c = cardOf(P, n); if (!c || !c.before || !c.before.length) return [];
  if (!missed(P, ME, n)) return [];
  return c.before.map(ref => { const m = String(ref).match(/^GT(\d+)-(\d+)$/); if (!m) return null; const Q = paper('GT' + m[1]); return Q && missed(Q, ME, +m[2]) ? { paper: 'GT' + m[1], n: +m[2] } : null; }).filter(Boolean);
}
const walkedSet = id => new Set(lsGet('walked.' + id, []));
function markWalked(id, n) { const s = walkedSet(id); if (!s.has(n)) { s.add(n); lsSet('walked.' + id, [...s]); } }

/* ---------------- tiles ---------------- */
function tileHtml(P, n, opts = {}) {
  const r = resOf(P, ME, n), g = guessOf(P, ME, n), o = resOf(P, OTHER, n);
  const rep = repeatsOf(P, n).length > 0, ear = o === 'w';
  const cls = ['gt-t', r === 'w' ? 'w' : r === 'b' ? 'b' : 'r', g ? 'g' : '', ear ? 'ear' : '', rep ? 'rep' : '', opts.dim ? 'dim' : '', opts.walked && opts.walked.has(n) ? 'done' : ''].filter(Boolean).join(' ');
  const label = `Question ${n}: ${r === 'w' ? 'wrong' : r === 'b' ? 'blank' : 'right'}${g ? ', guessed' : ''}${ear ? ', ' + OTHER_NAME + ' also wrong' : ''}${rep ? ', missed before' : ''}`;
  return `<a class="${cls}" href="#/gt/${P.id}/q/${n}" data-gtq="${n}" aria-label="${esc(label)}"><span>${n}</span>${rep ? '<em>×2</em>' : ''}</a>`;
}
const LEGEND = () => `<div class="gt-legend">
  <span><i class="gt-t r"></i>right</span><span><i class="gt-t w"></i>wrong</span><span><i class="gt-t r g"></i><i class="gt-t w g"></i>guessed</span>
  <span><i class="gt-t b"></i>blank</span><span><i class="gt-t r ear"></i>${OTHER_NAME} wrong too</span><span><i class="gt-t w rep"></i>missed in an earlier GT too</span></div>`;

/* ---------------- filters ---------------- */
const FILTERS = () => [['w', 'Wrong'], ['g', 'Guessed'], ['b', 'Blank'], ['r', 'Repeats'], ['s', 'Shared with ' + OTHER_NAME]];
function matchF(P, n, f) {
  const any = Object.values(f).some(Boolean); if (!any) return true;
  const r = resOf(P, ME, n);
  return (f.w && r === 'w') || (f.g && guessOf(P, ME, n)) || (f.b && r === 'b') || (f.r && repeatsOf(P, n).length > 0) || (f.s && r === 'w' && resOf(P, OTHER, n) === 'w');
}
function walkList(P, ns, f) {
  const any = Object.values(f).some(Boolean);
  return ns.filter(n => any ? matchF(P, n, f) : needs(P, ME, n));
}

/* ---------------- screens ---------------- */
export function renderGT(app, ctx, parts) {
  const draw = () => {
    if (!G.index && !Object.keys(G.papers).length) { app.innerHTML = shell(ctx, '', `<div class="gt-main"><p class="gt-muted">Loading the papers…</p></div>`); return; }
    const [id, sub, arg] = parts;
    if (!id) return homeScreen(app, ctx);
    if (id === 'all') return allScreen(app, ctx);
    const P = paper(id);
    if (!P) { app.innerHTML = shell(ctx, '', `<div class="gt-main"><p class="gt-muted">That paper isn't on this device yet.</p><a href="#/gt">All papers</a></div>`); return; }
    if (sub === 'q' && arg) return walkScreen(app, ctx, P, +arg);
    if (sub === 'sys' && arg) return sysScreen(app, ctx, P, decodeURIComponent(arg));
    return sheetScreen(app, ctx, P);
  };
  draw();
  loadGT().then(() => { if (/^#\/gt/.test(location.hash) && !document.querySelector('.gt-walk')) draw(); });
}

function rail(active) {
  const open = lsGet('rail', false);
  const ps = papers().slice().reverse();
  const item = (href, k, short, long, sub) => `<a class="gt-ri${active === k ? ' on' : ''}" href="${href}" title="${esc(long)}"><b>${esc(open ? long : short)}</b>${open && sub ? `<small>${esc(sub)}</small>` : ''}</a>`;
  return `<nav class="gt-rail${open ? ' open' : ''}" aria-label="Papers">
    <button class="gt-rtog" data-gtrail aria-label="${open ? 'Fold the papers list' : 'Open the papers list'}">${open ? '‹' : '›'}</button>
    ${ps.map(p => { const me = person(p, ME); return item('#/gt/' + p.id, p.id, p.id.replace('GT', 'GT '), p.title, me ? `${dshort(p.date)} · ${me.score} / ${4 * p.q.length}` : dshort(p.date)); }).join('')}
    ${item('#/gt/all', 'all', 'All', 'All GTs', 'trend · systems across papers')}
  </nav>`;
}
const dshort = d => { const x = new Date(d + 'T12:00:00'); return x.getDate() + ' ' + x.toLocaleString('en-GB', { month: 'short' }); };
function shell(ctx, active, inner, title) {
  return `<div class="screen gt-screen">
    <header class="top"><a class="iconbtn" href="${active && active !== 'home' ? '#/gt' : '#/'}" aria-label="Back">${ctx.ICON.back}</a><span class="tt"><span class="mono kick">GTs · ${IS_HT ? 'HT' : 'NAVEN'}</span><span class="h1s">${esc(title || 'Grand Tests')}</span></span></header>
    <div class="gt-body">${active === 'home' ? '' : rail(active)}<div class="scroll gt-scroll">${inner}</div></div>
    ${ctx.nav('')}</div>`;
}
function bindRail(app, redraw) { const b = app.querySelector('[data-gtrail]'); if (b) b.onclick = () => { lsSet('rail', !lsGet('rail', false)); redraw(); }; }

function homeScreen(app, ctx) {
  const ps = papers().slice().reverse();
  const cards = ps.map(P => {
    const me = person(P, ME), ot = person(P, OTHER), w = walkedSet(P.id);
    const ns = P.q.map(q => q.n).filter(n => needs(P, ME, n));
    const done = ns.filter(n => w.has(n)).length;
    return `<a class="gt-pcard" href="#/gt/${P.id}"><span class="mono gt-k">${esc(dshort(P.date))}</span><b>${esc(P.title)}</b>
      ${me ? `<span class="mono">${me.score} / ${4 * P.q.length} · ${me.right} right · ${me.wrong} wrong · ${me.blank} blank · ${me.guess.length} guessed</span>` : '<span class="gt-muted">You did not sit this one</span>'}
      ${ot ? `<span class="gt-muted small">${OTHER_NAME}: ${ot.score}</span>` : ''}
      <span class="gt-muted small">${done} of ${ns.length} walked</span></a>`;
  }).join('');
  app.innerHTML = shell(ctx, 'home', `<div class="gt-main gt-home">
    <p class="gt-muted">Each paper is its answer sheet. Wrong, guessed and blank questions open as GT cards; the rest show DocT's own explanation. A new paper appears here once it is added.</p>
    <div class="gt-pcards">${cards}<a class="gt-pcard dash" href="#/gt/all"><span class="mono gt-k">TREND</span><b>All GTs</b><span class="gt-muted small">score across papers · each system across papers</span></a></div>
  </div>`);
}

function sheetScreen(app, ctx, P) {
  const redraw = () => sheetScreen(app, ctx, P);
  const view = lsGet('view', 'paper'), f = ssGet('f.' + P.id, {}), w = walkedSet(P.id);
  const me = person(P, ME), ot = person(P, OTHER);
  const all = P.q.map(q => q.n), list = walkList(P, all, f);
  const chips = FILTERS().map(([k, l]) => { const c = all.filter(n => matchF(P, n, { [k]: true })).length; return `<button class="gt-chip${f[k] ? ' on' : ''}" data-gtf="${k}" aria-pressed="${!!f[k]}">${esc(l)} · ${c}</button>`; }).join('');
  const groups = sysGroups(P, all);
  let grid;
  if (view === 'paper') {
    const per = Math.ceil(P.q.length / P.sections.length);
    grid = `<div class="gt-sheet">${P.sections.map((s, i) => { const ns = all.slice(i * per, i * per + per); const right = ns.filter(n => resOf(P, ME, n) === 'r').length; return `<section class="gt-sec"><div class="gt-sech mono"><b>SECTION ${esc(s)}</b><span>${right} / ${ns.length} right</span></div><div class="gt-grid">${ns.map(n => tileHtml(P, n, { dim: !matchF(P, n, f), walked: w })).join('')}</div></section>`; }).join('')}
      <aside class="gt-where"><div class="mono gt-k">WHERE THE MARKS WENT · TAP A SYSTEM</div>${groups.map(g => `<a class="gt-wrow" href="#/gt/${P.id}/sys/${encodeURIComponent(g.name)}"><span class="gt-wl"><span>${esc(shortSys(g.name))}</span><span class="mono">${g.lost} of ${g.ns.length}</span></span><span class="gt-bar"><i style="width:${Math.round(100 * g.lost / g.ns.length)}%"></i></span></a>`).join('')}</aside></div>`;
  } else {
    grid = `<div class="gt-bysys">${groups.map(g => `<section class="gt-sysg"><a class="gt-sysh" href="#/gt/${P.id}/sys/${encodeURIComponent(g.name)}"><b>${esc(shortSys(g.name))}</b><span class="mono">${g.lost} lost of ${g.ns.length} ›</span></a><div class="gt-flow">${g.ns.map(n => tileHtml(P, n, { dim: !matchF(P, n, f), walked: w })).join('')}</div></section>`).join('')}</div>`;
  }
  app.innerHTML = shell(ctx, P.id, `<div class="gt-main">
    <div class="gt-head"><div><span class="mono gt-k">NEET-SS CRITICAL CARE · ${esc(dshort(P.date).toUpperCase())}</span><h1>${esc(P.title)}</h1></div>
      <div class="mono gt-score">${me ? `${me.score} / ${4 * P.q.length} · ${me.right} right · ${me.wrong} wrong · ${me.blank} blank` : 'Not sat'}<br><span class="gt-muted">${ot ? `${OTHER_NAME}: ${ot.score} · ${ot.wrong} wrong · ${ot.blank} blank` : ''}</span></div></div>
    <div class="gt-ctl"><div class="gt-seg" role="group" aria-label="Layout"><button data-gtv="paper" class="${view === 'paper' ? 'on' : ''}">Paper order</button><button data-gtv="sys" class="${view === 'sys' ? 'on' : ''}">By system</button></div>
      ${chips}<a class="gt-walkbtn${list.length ? '' : ' off'}" href="#/gt/${P.id}/q/${list[0] || 1}" data-gtwalk>Walk ${list.length}</a></div>
    ${LEGEND()}${grid}</div>`, P.title);
  bindRail(app, redraw);
  app.querySelectorAll('[data-gtv]').forEach(b => b.onclick = () => { lsSet('view', b.dataset.gtv); redraw(); });
  app.querySelectorAll('[data-gtf]').forEach(b => b.onclick = () => { const k = b.dataset.gtf; ssSet('f.' + P.id, { ...f, [k]: !f[k] }); redraw(); });
  bindTiles(app, P, list);
  const wb = app.querySelector('[data-gtwalk]'); if (wb) wb.onclick = e => { if (!list.length) { e.preventDefault(); return; } ssSet('walk', { paper: P.id, list, back: location.hash }); };
}
function bindTiles(app, P, list) {
  app.querySelectorAll('[data-gtq]').forEach(a => a.onclick = () => {
    const n = +a.dataset.gtq;
    ssSet('walk', { paper: P.id, list: list.includes(n) ? list : [n], back: location.hash });
  });
}
function sysGroups(P, ns) {
  const m = new Map();
  for (const n of ns) { const s = sysOf(P, n); if (!m.has(s)) m.set(s, []); m.get(s).push(n); }
  return [...m.entries()].map(([name, ns]) => ({ name, ns, lost: ns.filter(n => resOf(P, ME, n) !== 'r').length }))
    .sort((a, b) => b.lost / b.ns.length - a.lost / a.ns.length || b.ns.length - a.ns.length);
}

function trendRows(sys) {
  return papers().map(P => {
    const ns = P.q.map(q => q.n).filter(n => sysOf(P, n) === sys);
    if (!ns.length) return '';
    const row = (who, label) => { if (!person(P, who)) return ''; const lost = ns.filter(n => resOf(P, who, n) !== 'r').length; return `<div class="gt-tr${who === OTHER ? ' oth' : ''}"><span class="mono">${esc(label)}</span><span class="gt-bar"><i style="width:${Math.round(100 * lost / ns.length)}%"></i></span><span class="mono">lost ${lost} of ${ns.length}</span></div>`; };
    return row(ME, P.id.replace('GT', 'GT ')) + row(OTHER, OTHER_NAME);
  }).join('');
}
function sysScreen(app, ctx, P, sys) {
  const redraw = () => sysScreen(app, ctx, P, sys);
  const w = walkedSet(P.id), f = ssGet('f.' + P.id, {});
  const ns = P.q.map(q => q.n).filter(n => sysOf(P, n) === sys);
  const list = walkList(P, ns, f);
  const topics = new Map();
  for (const n of ns) { const t = topicOf(P, n) || 'Other'; if (!topics.has(t)) topics.set(t, []); topics.get(t).push(n); }
  const tlist = [...topics.entries()].map(([t, ns]) => ({ t, ns, lost: ns.filter(n => needs(P, ME, n)).length })).sort((a, b) => b.lost - a.lost || a.t.localeCompare(b.t));
  const lost = ns.filter(n => resOf(P, ME, n) !== 'r').length;
  app.innerHTML = shell(ctx, P.id, `<div class="gt-main">
    <div class="gt-head"><div><span class="mono gt-k"><a href="#/gt/${P.id}">${esc(P.title)}</a> · SYSTEM</span><h1>${esc(shortSys(sys))}</h1></div>
      <div class="mono gt-score">lost ${lost} of ${ns.length} here<br><span class="gt-muted">${ns.filter(n => guessOf(P, ME, n)).length} guessed</span></div></div>
    <div class="gt-ctl"><span class="gt-muted small">Filters from the sheet apply here too.</span><a class="gt-walkbtn${list.length ? '' : ' off'}" href="#/gt/${P.id}/q/${list[0] || ns[0]}" data-gtwalk>Walk ${list.length}</a></div>
    <div class="gt-sysflow">${ns.map(n => tileHtml(P, n, { dim: !matchF(P, n, f), walked: w })).join('')}</div>
    <div class="gt-cols">
      <section class="gt-box"><div class="mono gt-k">TREND · THIS SYSTEM IN EACH GT</div>${trendRows(sys)}<p class="gt-muted small">The black part is the share lost (wrong or blank), so papers with a different number of questions compare fairly.</p></section>
      <section class="gt-box"><div class="mono gt-k">TOPICS IN ${esc(shortSys(sys).toUpperCase())}</div>${tlist.map(x => `<div class="gt-topic"><span class="gt-tn">${esc(x.t)}<small class="mono">${x.lost ? x.lost + ' to walk' : 'all sure and right'}</small></span><span class="gt-flow">${x.ns.map(n => tileHtml(P, n, { walked: w })).join('')}</span></div>`).join('')}</section>
    </div></div>`, shortSys(sys));
  bindRail(app, redraw);
  bindTiles(app, P, list);
  const wb = app.querySelector('[data-gtwalk]'); if (wb) wb.onclick = () => ssSet('walk', { paper: P.id, list: list.length ? list : ns, back: location.hash });
}

function allScreen(app, ctx) {
  const redraw = () => allScreen(app, ctx);
  const ps = papers();
  const srow = (P, who, label) => {
    const p = person(P, who); if (!p) return '';
    const t = P.q.length, pc = x => (100 * x / t).toFixed(2) + '%';
    return `<div class="gt-srow${who === OTHER ? ' oth' : ''}"><span class="mono gt-sl">${esc(label)}</span><b class="mono">${p.score}</b>
      <span class="gt-sbar" role="img" aria-label="${p.right} right, ${p.wrong} wrong, ${p.blank} blank"><i class="r" style="width:${pc(p.right)}"></i><i class="w" style="width:${pc(p.wrong)}"></i><i class="b" style="width:${pc(p.blank)}"></i></span>
      <span class="mono gt-sn">${p.right} right · ${p.wrong} wrong · ${p.blank} blank · ${p.guess.length} guessed</span></div>`;
  };
  const sysNames = [...new Set(ps.flatMap(P => P.q.map(q => sysOf(P, q.n))))];
  const sysStats = sysNames.map(s => {
    let lost = 0, tot = 0; for (const P of ps) for (const q of P.q) if (sysOf(P, q.n) === s && person(P, ME)) { tot++; if (resOf(P, ME, q.n) !== 'r') lost++; }
    return { s, lost, tot };
  }).sort((a, b) => b.lost / (b.tot || 1) - a.lost / (a.tot || 1));
  const last = ps[ps.length - 1];
  app.innerHTML = shell(ctx, 'all', `<div class="gt-main">
    <div class="gt-head"><div><span class="mono gt-k">ALL GTs</span><h1>Trend</h1></div></div>
    <section class="gt-box"><div class="mono gt-k">SCORE · ONE ROW PER PAPER · ${OTHER_NAME.toUpperCase()} UNDER YOURS</div>
      <div class="gt-legend"><span><i class="gt-sw r"></i>right</span><span><i class="gt-sw w"></i>wrong</span><span><i class="gt-sw b"></i>blank</span><span><i class="gt-t r ear"></i>${OTHER_NAME}'s row</span></div>
      ${ps.map(P => srow(P, ME, P.id.replace('GT', 'GT ')) + srow(P, OTHER, OTHER_NAME)).join('')}</section>
    <section class="gt-box"><div class="mono gt-k">EACH SYSTEM ACROSS PAPERS · WORST FIRST · TAP FOR ${last ? esc(last.id.replace('GT', 'GT ')) : ''}</div>
      ${sysStats.map(x => `<a class="gt-sysrow" href="#/gt/${last.id}/sys/${encodeURIComponent(x.s)}"><span>${esc(shortSys(x.s))}</span><span class="gt-mini">${ps.map(P => { const ns = P.q.filter(q => sysOf(P, q.n) === x.s); if (!ns.length || !person(P, ME)) return `<span class="gt-mb none" title="${esc(P.id)}: none"><i></i></span>`; const l = ns.filter(q => resOf(P, ME, q.n) !== 'r').length; return `<span class="gt-mb" title="${esc(P.id)}: lost ${l} of ${ns.length}"><i style="width:${Math.round(100 * l / ns.length)}%"></i><small class="mono">${P.id.replace('GT', '')}: ${l}/${ns.length}</small></span>`; }).join('')}</span><span class="mono">${x.lost} of ${x.tot}</span></a>`).join('')}</section>
  </div>`, 'All GTs');
  bindRail(app, redraw);
}

/* ---------------- walk ---------------- */
// GT cards are written to Naven ("you", "your pick") and name HT; in HT's profile the two are swapped
function persp(t) {
  if (!IS_HT || !t) return t;
  const A = '\u0001', B = '\u0002', C = '\u0003', D = '\u0004';
  return String(t)
    .replace(/\bHT's\b/g, A).replace(/\bHT\b/g, B)
    .replace(/\byours\b/gi, "Naven's").replace(/\bYour\b/g, "Naven's").replace(/\byour\b/g, "Naven's").replace(/\bYou\b/g, C).replace(/\byou\b/g, D)
    .split(A).join('your').split(B).join('you').split(C).join('Naven').split(D).join('Naven')
    .replace(/(^|[.!?]\s+)your/g, (m, a) => a + 'Your').replace(/(^|[.!?]\s+)you/g, (m, a) => a + 'You');
}
function mdBlock(md) {
  const out = []; let list = null;
  const flush = () => { if (list) { out.push('<ul>' + list.map(l => `<li>${inline(l)}</li>`).join('') + '</ul>'); list = null; } };
  for (const para of String(md || '').split(/\n{2,}/)) {
    const lines = para.split('\n');
    for (const l of lines) {
      const t = l.trim(); if (!t) continue;
      if (/^#{1,3}\s+/.test(t)) { flush(); out.push(`<div class="mono gt-xk">${esc(plain(t.replace(/^#+\s+/, '')).toUpperCase())}</div>`); }
      else if (/^[-•]\s+/.test(t)) { (list = list || []).push(t.replace(/^[-•]\s+/, '')); }
      else { flush(); out.push(`<p>${inline(t)}</p>`); }
    }
    flush();
  }
  return out.join('');
}
function findCard(ref) {
  const [deck, code] = String(ref).split('|');
  const c = cardsOf(deck).find(x => x.code === code);
  return c || null;
}
function linkedCardHtml(ref) {
  const c = findCard(ref);
  if (!c) return `<p class="gt-muted">${esc(ref.replace('|', ' · '))}: this card's deck isn't on this device yet. Open the deck once from the Shelf and it appears here.</p>`;
  const lines = String(c.q || '').split('\n'), head = lines[0], rest = lines.slice(1).join('\n');
  // the answer side as Flow draws it (title, question parts, answer, why, watch), so the card looks as it did when studied
  return `<div class="c-head mono gt-lch"><span>${esc(c.deck)} · ${esc(c.code)}${c.section ? ' · ' + esc(String(c.section).toUpperCase()) : ''}</span></div>
    <div class="c-a gt-lca"><div class="zw">
    <h2 class="c-title">${esc(plain(head).replace(/:$/, ''))}</h2>
    ${rest ? `<details class="qrecap" open><summary>Question parts</summary><div class="qr small">${render(rest)}</div></details>` : ''}
    <div class="ans">${render(c.a || '')}</div>
    ${c.fixed ? `<p class="qsrc-card mono">Corrected ${esc(c.fixed.date)} · ${esc(c.fixed.src)}</p>` : ''}
    ${c.why ? `<div class="box why"><span class="mono">WHY</span><div class="bx">${render(c.why)}</div></div>` : ''}
    ${c.watch ? `<div class="box watch"><span class="mono">WATCH</span><div class="bx">${render(c.watch)}</div></div>` : ''}
    <a class="gt-open" href="#/deck/${encodeURIComponent(c.deck)}">Open ${esc(c.deck)} ›</a></div></div>`;
}
const WK = { mode: () => lsGet('mode', 'read') };
function walkScreen(app, ctx, P, n) {
  let W = ssGet('walk', null);
  if (!W || W.paper !== P.id || !W.list.includes(n)) { W = { paper: P.id, list: walkList(P, P.q.map(q => q.n), {}).includes(n) ? walkList(P, P.q.map(q => q.n), {}) : [n], back: '#/gt/' + P.id }; ssSet('walk', W); }
  const idx = W.list.indexOf(n), q = qOf(P, n), c = cardOf(P, n);
  const stKey = 'wst.' + P.id + '.' + n, saved = ssGet(stKey, {});
  const st = { mode: WK.mode(), now: null, tab: saved.tab || 'exp' };   // T-195: the open tab survives a redraw
  markWalked(P.id, n);
  const prev = W.list[idx - 1], next = W.list[idx + 1];
  const draw = () => {
    ssSet(stKey, { tab: st.tab });
    const read = st.mode === 'read', shown = read || !!st.now;
    const myR = resOf(P, ME, n), myP = pickOf(P, ME, n), otR = resOf(P, OTHER, n), otP = pickOf(P, OTHER, n);
    const reps = repeatsOf(P, n);
    const who = (r, g) => r == null ? 'did not sit' : (r === 'w' ? 'wrong' : r === 'b' ? 'blank' : 'right') + (g ? ', guessed' : '');
    const letters = 'ABCDE';
    const opts = q.options.map((t, i) => {
      const L = letters[i], marks = [];
      if (shown && L === q.key) marks.push('<span class="gt-pill key">✓ Key</span>');
      if (shown && myP === L) marks.push('<span class="gt-pill">You ✗</span>');
      if (shown && otP === L) marks.push(`<span class="gt-pill oth">${OTHER_NAME} ✗</span>`);
      if (!read && st.now === L) marks.push('<span class="gt-pill now">● Now</span>');
      return `<button class="gt-opt${shown && L === q.key ? ' key' : ''}" data-gtopt="${L}" ${read || st.now ? 'tabindex="-1"' : ''}><span class="mono">${L}</span><span class="gt-ot">${inline(t)}</span>${marks.join('')}</button>`;
    }).join('');
    const keyText = q.options[letters.indexOf(q.key)] || '';
    const row = (k, v) => v ? `<b class="mono">${k}</b><div>${render(v)}</div>` : '';
    const back = !shown ? `<p class="gt-muted">Tap an option. The answer and the explanation open by themselves; nothing you tap here is recorded.</p>`
      : c ? `<div class="gt-back">${row('ANSWER', c.answer || (q.key + '. ' + keyText))}${row('WHY', c.why)}${row('WATCH', persp(c.watch))}${row('HOOK', c.hook)}${row('TEMPTED', persp(c.picks_note))}</div>
          ${c.key && c.key.status && c.key.status !== 'agree' ? `<div class="box watch"><span class="mono">KEY ${esc(c.key.status.toUpperCase())}</span><div class="bx">${render(c.key.note || '')}</div></div>` : c.key && c.key.note ? `<p class="gt-muted small">${inline(c.key.note)}</p>` : ''}`
      : `<div class="gt-back">${row('ANSWER', q.key + '. ' + keyText)}</div><p class="gt-muted small">${needs(P, ME, n) || needs(P, OTHER, n) ? 'The GT card for this question is still being written; DocT’s explanation is in the pane.' : 'You got this right and were sure, so it shows DocT’s own explanation.'}</p>`;
    const tabs = [['exp', 'Explanation']].concat((c && c.links || []).map((l, i) => ['L' + i, l.split('|')[1] || l]), reps.map((r, i) => ['B' + i, r.paper.replace('GT', 'GT ') + ' · Q' + r.n]), [['doct', 'DocT’s text']]);
    if (!tabs.find(t => t[0] === st.tab)) st.tab = 'exp';
    let pane;
    if (st.tab === 'exp') pane = !shown ? '<p class="gt-muted">The explanation opens once you answer.</p>' : c ? `<div class="ans">${mdBlock(c.explain)}</div>${c.options ? `<div class="mono gt-xk">THE OPTIONS</div><div class="gt-optx">${Object.entries(c.options).map(([L, t]) => `<b>${esc(L)}${L === q.key ? ' ✓' : ''}</b><div>${inline(persp(t))}</div>`).join('')}</div>` : ''}${c.links && c.links.length ? `<p class="gt-muted small">Linked cards are in the tabs above.</p>` : `<p class="gt-muted small">No regular card teaches this yet, so this GT card carries it.</p>`}` : `<div class="gt-doct">${esc(q.doct)}</div>`;
    else if (st.tab === 'doct') pane = `<div class="mono gt-xk">DOCT’S EXPLANATION · AS CAPTURED</div><div class="gt-doct">${esc(q.doct)}</div>${q.refs ? `<p class="gt-muted small">${esc(q.refs)}</p>` : ''}`;
    else if (st.tab[0] === 'L') pane = linkedCardHtml(c.links[+st.tab.slice(1)]);
    else { const r = reps[+st.tab.slice(1)], Q = paper(r.paper), qq = qOf(Q, r.n), cc = cardOf(Q, r.n); pane = `<div class="mono gt-xk">${esc(Q.title.toUpperCase())} · Q${r.n} · MISSED BEFORE</div><p>${inline(qq.stem)}</p><div class="gt-optx">${qq.options.map((t, i) => `<b>${letters[i]}${letters[i] === qq.key ? ' ✓' : ''}${pickOf(Q, ME, r.n) === letters[i] ? ' · you' : ''}</b><div>${inline(t)}</div>`).join('')}</div>${cc ? `<div class="gt-back">${row('WHY', cc.why)}${row('WATCH', cc.watch)}${row('HOOK', cc.hook)}</div>` : `<div class="gt-doct">${esc(qq.doct)}</div>`}<a class="gt-open" href="#/gt/${r.paper}/q/${r.n}" data-gtjump>Open it as its own card ›</a>`; }
    const imgs = (q.img || []).map(f => `<img class="gt-img" src="data/gt/img/${esc(f)}" alt="Image for question ${n}" loading="lazy">`).join('');
    const scrollY = app.querySelector('.gt-pane') ? app.querySelector('.gt-pane').scrollTop : 0;
    app.innerHTML = `<div class="screen gt-walk">
      <header class="gt-wbar"><a class="gt-wback" href="${esc(W.back || '#/gt/' + P.id)}">‹ ${esc(P.id.replace('GT', 'GT '))}</a>
        <span class="mono gt-wk">WALK · ${idx + 1} OF ${W.list.length}</span><span class="gt-prog"><i style="width:${Math.round(100 * (idx + 1) / W.list.length)}%"></i></span>
        <span class="gt-seg dark" role="group" aria-label="Walk mode"><button data-gtm="try" class="${read ? '' : 'on'}">Try</button><button data-gtm="read" class="${read ? 'on' : ''}">Read</button></span>
        <a class="gt-nav${prev ? '' : ' off'}" href="${prev ? '#/gt/' + P.id + '/q/' + prev : '#'}" aria-label="Previous">‹ Prev</a><a class="gt-nav gold${next ? '' : ' off'}" href="${next ? '#/gt/' + P.id + '/q/' + next : '#'}" aria-label="Next">Next ›</a></header>
      <div class="gt-wbody">
        <article class="gt-qcard card">
          <div class="gt-qh"><span class="mono">${esc(P.id.replace('GT', 'GT '))} · Q${n} · ${esc(shortSys(sysOf(P, n)).toUpperCase())}${topicOf(P, n) ? ' · ' + esc(topicOf(P, n).toUpperCase()) : ''}</span>
            ${reps.map((r, i) => `<button class="gt-rep" data-gttab="B${i}"><b>×2</b> Missed before: ${esc(r.paper.replace('GT', 'GT '))} Q${r.n} ›</button>`).join('')}</div>
          <div class="gt-who mono"><span>You: ${esc(who(myR, guessOf(P, ME, n)))}</span>${person(P, OTHER) ? `<span class="oth">${OTHER_NAME}: ${esc(who(otR, guessOf(P, OTHER, n)))}</span>` : ''}</div>
          <p class="gt-stem">${inline(q.stem)}</p>${imgs}
          <div class="gt-opts">${opts}</div>
          <div class="gt-backw">${back}</div>
        </article>
        <section class="gt-xp card" aria-label="Explain pane"><div class="gt-tabs" role="tablist">${tabs.map(([k, l]) => `<button role="tab" aria-selected="${st.tab === k}" class="${st.tab === k ? 'on' : ''}" data-gttab="${k}">${esc(l)}</button>`).join('')}</div>
          <div class="gt-pane">${pane}</div></section>
      </div></div>`;
    if (st.tab === 'exp' && scrollY) { /* new question or new mode: start at the top */ }
    app.querySelectorAll('[data-gtm]').forEach(b => b.onclick = () => { st.mode = b.dataset.gtm; st.now = null; lsSet('mode', st.mode); draw(); });
    app.querySelectorAll('[data-gtopt]').forEach(b => b.onclick = () => { if (st.mode === 'try' && !st.now) { st.now = b.dataset.gtopt; draw(); } });
    app.querySelectorAll('[data-gttab]').forEach(b => b.onclick = () => { st.tab = b.dataset.gttab; draw(); });
    app.querySelectorAll('.gt-nav.off').forEach(a => a.onclick = e => e.preventDefault());
    const j = app.querySelector('[data-gtjump]'); if (j) j.onclick = () => { const m = j.getAttribute('href').match(/#\/gt\/(GT\d+)\/q\/(\d+)/); if (m) ssSet('walk', { paper: m[1], list: [+m[2]], back: location.hash }); };
  };
  draw();
  const onKey = e => {
    if (!document.querySelector('.gt-walk')) { window.removeEventListener('keydown', onKey); return; }
    if (e.target && /input|textarea/i.test(e.target.tagName)) return;
    if (e.key === 'ArrowRight' && next) { window.removeEventListener('keydown', onKey); location.hash = '#/gt/' + P.id + '/q/' + next; }
    if (e.key === 'ArrowLeft' && prev) { window.removeEventListener('keydown', onKey); location.hash = '#/gt/' + P.id + '/q/' + prev; }
  };
  window.addEventListener('keydown', onKey);
}
