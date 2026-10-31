// Visual decks made by ChatGPT, joined to the text cards during Flow.
// Drive: Trace › decks › <DECK> › visual › current.json · images/ · versions/v<N>/{manifest.json, scenes.csv, …}
// Contract: claude/Trace_Visual_Deck_Contract.md. Trace reads only the version current.json names, validates it,
// and keeps the previous accepted copy if anything is wrong.
import { db } from './db.js';
import { batch, hasBackend, isDemo } from './api.js';
import { splitQ, reflow, plain, SOFT, render, inline } from './md.js';

export const V = { packs: new Map(), urls: new Map(), status: { checked: 0, busy: false, problems: {} } };
const DATA = ['scenes.csv', 'sequences.csv', 'links.csv', 'hotspots.csv', 'cues.csv', 'stories.json', 'notes.csv'];

/* ---------- parsing ---------- */
export function csv(text) {
  const rows = []; let row = [], f = '', q = false;
  text = String(text || '').replace(/^﻿/, '');
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (q) { if (ch === '"') { if (text[i + 1] === '"') { f += '"'; i++; } else q = false; } else f += ch; continue; }
    if (ch === '"') q = true;
    else if (ch === ',') { row.push(f); f = ''; }
    else if (ch === '\n' || ch === '\r') { if (ch === '\r' && text[i + 1] === '\n') i++; row.push(f); f = ''; if (row.some(x => x !== '')) rows.push(row); row = []; }
    else f += ch;
  }
  row.push(f); if (row.some(x => x !== '')) rows.push(row);
  if (!rows.length) return [];
  const head = rows.shift().map(h => h.trim());
  return rows.map(r => Object.fromEntries(head.map((h, i) => [h, (r[i] || '').trim()])));
}

/* ---------- card parts, exactly as the screen shows them ---------- */
const norm = s => String(s || '').replace(/\*/g, '').replace(new RegExp(SOFT, 'g'), ' ').replace(/\s+/g, ' ').trim();
const SUB_B = /^\s*\*\*([a-h])[.)]?\*\*\s+(.*)$/, SUB_P = /^\s*([a-h])[.)]?\s+(?=[A-Z0-9*(“"'≥≤<>])(.*)$/;
export function cardParts(c, field) {
  const out = {};
  let body = '';
  if (field === 'q') { const { head, rest } = splitQ(c.q); out.heading = norm(plain(head).replace(/:$/, '')); body = rest; }
  else body = reflow(c[field] || '');
  const lines = body.split('\n'); let li = 0; const whole = [], segs = [];
  // same order as render(): bullets, then table rows (2+ in a run), then sub-parts / plain lines
  const isTbl = i => lines[i] && lines[i].includes(' | ') && !/^\s*[-•]\s+/.test(lines[i]);
  for (let i = 0; i < lines.length; i++) {
    const l = lines[i];
    if (!l.trim()) continue;
    if (isTbl(i) && (isTbl(i - 1) || isTbl(i + 1))) { whole.push(l.split(' | ').join(' ')); l.split(' | ').forEach(x => { if (norm(x)) segs.push(norm(x)); }); continue; }
    if (/^\s*[-•]\s+/.test(l)) { li++; out['li' + li] = norm(l.replace(/^\s*[-•]\s+/, '')); whole.push(out['li' + li]); segs.push(out['li' + li]); continue; }
    const m = l.match(SUB_B) || l.match(SUB_P);
    if (m && m[2]) { out[m[1]] = norm(m[2]); whole.push(m[2]); segs.push(out[m[1]]); continue; }
    if (/^\s*[-•]\s+/.test(l)) { li++; out['li' + li] = norm(l.replace(/^\s*[-•]\s+/, '')); whole.push(out['li' + li]); segs.push(out['li' + li]); continue; }
    whole.push(l.split(' | ').join(' ')); l.split(' | ').forEach(x => { if (norm(x)) segs.push(norm(x)); });
  }
  out.whole = norm(whole.join(' '));
  Object.defineProperty(out, 'segs', { value: segs, enumerable: false });   // a phrase in "whole" must sit inside one line or table cell
  return out;
}
function countIn(hay, needle) { let n = 0, i = 0; while ((i = hay.indexOf(needle, i)) >= 0) { n++; i += needle.length; } return n; }

/* ---------- validation (same rules as trace_validate.py) ---------- */
export function validate(pk, cards, imageNames) {
  const errors = [], warnings = [];
  const byCode = new Map(cards.map(c => [c.code, c]));
  const scenes = new Map(), seqs = new Map();
  for (const s of pk.scenes) {
    if (scenes.has(s.scene_id)) errors.push(`scenes.csv: duplicate scene_id ${s.scene_id}`);
    scenes.set(s.scene_id, s);
    if (!['overview', 'detail'].includes(s.kind)) errors.push(`scenes.csv: ${s.scene_id} kind "${s.kind}" must be overview or detail`);
    if (!byCode.has(s.card_code)) errors.push(`scenes.csv: ${s.scene_id} card_code ${s.card_code} is not in the deck`);
    if (!s.image || !imageNames.has(s.image)) errors.push(`scenes.csv: ${s.scene_id} image ${s.image || '(blank)'} is missing from images/`);
  }
  for (const r of pk.sequences) {
    if (!scenes.has(r.scene_id)) errors.push(`sequences.csv: ${r.sequence_id} uses unknown scene ${r.scene_id}`);
    const l = seqs.get(r.sequence_id) || []; l.push(r); seqs.set(r.sequence_id, l);
  }
  for (const [id, l] of seqs) {
    const o = l.map(r => +r.order).sort((a, b) => a - b);
    if (o.some((x, i) => x !== i + 1)) errors.push(`sequences.csv: ${id} order must run 1..${l.length} without gaps or repeats (has ${o.join(',')})`);
  }
  const needOverview = new Set();
  pk.links.forEach((r, i) => {
    const where = `links.csv row ${i + 2}`, c = byCode.get(r.card_code);
    if (!c) { errors.push(`${where}: card_code ${r.card_code} is not in the deck`); return; }
    needOverview.add(r.card_code);
    if (!seqs.has(r.sequence_id)) errors.push(`${where}: unknown sequence ${r.sequence_id}`);
    if (!['q', 'a', 'why', 'watch'].includes(r.field)) { errors.push(`${where}: field "${r.field}" must be q, a, why or watch`); return; }
    if (r.part === 'heading') { errors.push(`${where}: the heading opens the overview by itself; link a sub-part, list line or phrase instead`); return; }
    const parts = cardParts(c, r.field), text = parts[r.part];
    if (text == null) { errors.push(`${where}: ${r.card_code} ${r.field} has no part "${r.part}" (has ${Object.keys(parts).join(', ')})`); return; }
    if (!r.phrase) return;
    const ph = norm(r.phrase), n = r.part === 'whole' ? parts.segs.reduce((t, x) => t + countIn(x, ph), 0) : countIn(text, ph);
    if (!n && r.part === 'whole' && countIn(text, ph)) { errors.push(`${where}: phrase "${r.phrase}" runs across two lines or cells of ${r.card_code} ${r.field}; link it within one line`); return; }
    if (!n) errors.push(`${where}: phrase "${r.phrase}" not found in ${r.card_code} ${r.field}/${r.part}: "${text}"`);
    else if (n > 1 && !(+r.occurrence >= 1 && +r.occurrence <= n)) errors.push(`${where}: AMBIGUOUS — "${r.phrase}" appears ${n}× in ${r.card_code} ${r.field}/${r.part}; set occurrence 1..${n}`);
    else if (n === 1 && r.occurrence && +r.occurrence !== 1) errors.push(`${where}: occurrence ${r.occurrence} but the phrase appears once`);
  });
  pk.hotspots.forEach((h, i) => {
    const where = `hotspots.csv row ${i + 2}`, s = scenes.get(h.overview_id);
    if (!s || s.kind !== 'overview') errors.push(`${where}: ${h.overview_id} is not an overview scene`); else needOverview.add(s.card_code);
    if (!seqs.has(h.sequence_id)) errors.push(`${where}: unknown sequence ${h.sequence_id}`);
    const [x, y, w, hh] = [h.x, h.y, h.w, h.h].map(Number);
    if ([x, y, w, hh].some(v => !isFinite(v)) || x < 0 || y < 0 || w <= 0 || hh <= 0 || x + w > 100.001 || y + hh > 100.001) errors.push(`${where}: box ${h.x},${h.y},${h.w},${h.h} must lie inside 0–100`);
  });
  for (const code of needOverview) if (![...scenes.values()].some(s => s.kind === 'overview' && s.card_code === code)) errors.push(`${code} has links or hotspots but no overview scene`);
  pk.cues.forEach((r, i) => { if (!scenes.has(r.scene_id)) errors.push(`cues.csv row ${i + 2}: unknown scene ${r.scene_id}`); });
  (pk.stories || []).forEach((r, i) => { if (!scenes.has(r.scene_id)) errors.push(`stories.json item ${i + 1}: unknown scene ${r.scene_id}`); });
  pk.notes.forEach((r, i) => {
    const where = `notes.csv row ${i + 2}`;
    if (!byCode.has(r.card_code)) errors.push(`${where}: card_code ${r.card_code} is not in the deck`);
    if (!['card', 'scene'].includes(r.level)) errors.push(`${where}: level must be card or scene`);
    if (r.level === 'scene' && !scenes.has(r.scene_id)) errors.push(`${where}: unknown scene ${r.scene_id}`);
    if (!['correction', 'qualification', 'update'].includes(r.kind)) errors.push(`${where}: kind must be correction, qualification or update`);
  });
  return { errors, warnings };
}

/* ---------- download ---------- */
const b64toBlob = (b64, mime) => { const bin = atob(b64), a = new Uint8Array(bin.length); for (let i = 0; i < bin.length; i++) a[i] = bin.charCodeAt(i); return new Blob([a], { type: mime || 'image/webp' }); };

export async function loadVisuals() {
  try { for (const p of await db.all('visuals')) V.packs.set(p.deck, p); } catch (e) { /* first run */ }
  V.status.checked = (await db.kv.get('visualsChecked')) || 0;
}

/** cardsOf: deck -> cards (with edits applied are fine; validation uses originals when given) */
export async function syncVisuals(cardsOf, { force = false } = {}) {
  if (!hasBackend() || isDemo() || V.status.busy) return;
  if (!force && Date.now() - V.status.checked < 6 * 3600e3) return;
  V.status.busy = true;
  try {
    const [r] = await batch([{ op: 'visualIndex' }]);
    if (!r.ok) throw new Error(r.error);
    const problems = {};
    for (const row of r.data || []) {
      const deck = row.deck;
      try {
        if (row.error) throw new Error(row.error);
        const cur = JSON.parse(row.current);
        const have = V.packs.get(deck);
        if (have && have.version === +cur.live_version && !force) continue;
        const files = new Map(row.files.map(f => [f.name, f]));
        const need = ['manifest.json', ...DATA];
        const miss = need.filter(n => !files.has(n) && n !== 'hotspots.csv' && n !== 'notes.csv');
        if (miss.length) throw new Error('version v' + cur.live_version + ' is missing ' + miss.join(', '));
        const names = need.filter(n => files.has(n));
        const res = await batch(names.map(n => ({ op: 'readFile', id: files.get(n).id })));
        const txt = {}; res.forEach((x, i) => { if (!x.ok) throw new Error(names[i] + ': ' + x.error); txt[names[i]] = x.data.text; });
        const manifest = JSON.parse(txt['manifest.json']);
        const pk = {
          deck, version: +cur.live_version, manifest,
          scenes: csv(txt['scenes.csv']), sequences: csv(txt['sequences.csv']), links: csv(txt['links.csv']),
          hotspots: csv(txt['hotspots.csv'] || ''), cues: csv(txt['cues.csv']), stories: JSON.parse(txt['stories.json'] || '[]'), notes: csv(txt['notes.csv'] || '')
        };
        const imgs = new Map(row.images.map(f => [f.name, f]));
        const v = validate(pk, cardsOf(deck), new Set(imgs.keys()));
        if (v.errors.length) throw new Error(v.errors.slice(0, 6).join(' · ') + (v.errors.length > 6 ? ` (+${v.errors.length - 6} more)` : ''));
        // images: download what this device does not have yet (they are never replaced, so a name is enough)
        const used = [...new Set(pk.scenes.map(s => s.image))];
        const want = [];
        for (const n of used) if (!(await db.get('vimg', deck + '|' + n))) want.push(n);
        for (let i = 0; i < want.length; i += 4) {
          const part = want.slice(i, i + 4);
          const out = await batch(part.map(n => ({ op: 'readBinary', id: imgs.get(n).id })));
          const rows = out.map((x, j) => { if (!x.ok) throw new Error(part[j] + ': ' + x.error); return { key: deck + '|' + part[j], blob: b64toBlob(x.data.b64, x.data.mime), size: x.data.size }; });
          await db.putMany('vimg', rows);
        }
        pk.checkedAt = Date.now();
        await db.put('visuals', pk);
        V.packs.set(deck, pk);
      } catch (e) { problems[deck] = String(e.message || e); }
    }
    V.status.problems = problems;
    V.status.checked = Date.now();
    await db.kv.set('visualsChecked', V.status.checked);
  } catch (e) { const m = String(e.message || e); V.status.problems = { '*': /unknown op/.test(m) ? 'The Drive bridge is an older version. Paste the new Code.gs and redeploy it (v3) to receive visual decks.' : m }; }
  finally { V.status.busy = false; }
}

/* ---------- lookups ---------- */
export const hasVisual = c => { const p = V.packs.get(c.deck); return !!(p && p.scenes.some(s => s.card_code === c.code)); };
const overviewOf = (p, code) => p.scenes.find(s => s.kind === 'overview' && s.card_code === code);
const seqScenes = (p, id) => p.sequences.filter(r => r.sequence_id === id).sort((a, b) => a.order - b.order).map(r => p.scenes.find(s => s.scene_id === r.scene_id)).filter(Boolean);
async function imgUrl(deck, name) {
  const k = deck + '|' + name;
  if (V.urls.has(k)) return V.urls.get(k);
  const r = await db.get('vimg', k); if (!r) return '';
  const u = URL.createObjectURL(r.blob); V.urls.set(k, u); return u;
}
export function releaseUrls() { for (const u of V.urls.values()) URL.revokeObjectURL(u); V.urls.clear(); }

/* ---------- make card text tappable ---------- */
// map the visible text of an element to text nodes, collapsing white space the way the validator does
function textMap(el) {
  const chars = [], at = [];
  const push = (ch, node, off) => {
    if (/\s/.test(ch)) { if (!chars.length || chars[chars.length - 1] === ' ') return; ch = ' '; }
    chars.push(ch); at.push(node ? [node, off] : null);
  };
  const walk = n => {
    if (n.nodeType === 3) { const t = n.nodeValue; for (let i = 0; i < t.length; i++) if (t[i] !== '*') push(t[i], n, i); return; }
    if (n.nodeType !== 1) return;
    if (n.classList.contains('vl-skip') || n.classList.contains('sp')) return;   // sub-part letters are not card text
    if (n.tagName === 'BR') { push(' '); return; }
    const block = /^(P|LI|DIV|UL|OL|H2|TD|TR)$/.test(n.tagName);
    if (block) push(' ');
    n.childNodes.forEach(walk);
    if (block) push(' ');
  };
  walk(el);
  while (chars[0] === ' ') { chars.shift(); at.shift(); }
  return { text: chars.join(''), at };
}
function wrapPhrase(el, phrase, occ, seq) {
  const { text, at } = textMap(el), ph = norm(phrase);
  const blockOf = n => n.parentElement && n.parentElement.closest('p,li,.td,h2,.ans,.bx,.qr');
  let s = -1, e = -1, k = 0, from = 0;
  while (k < (occ || 1)) {
    const i = text.indexOf(ph, from); if (i < 0) return false;
    from = i + ph.length;
    let a = i, b = i + ph.length - 1;
    while (a <= b && !at[a]) a++; while (b >= a && !at[b]) b--;
    if (a > b || blockOf(at[a][0]) !== blockOf(at[b][0])) continue;   // never wrap across lines or cells
    k++; s = a; e = b;
  }
  const r = document.createRange();
  r.setStart(at[s][0], at[s][1]); r.setEnd(at[e][0], at[e][1] + 1);
  const span = document.createElement('span');
  span.className = 'vl'; span.dataset.seq = seq; span.setAttribute('role', 'button'); span.tabIndex = 0;
  span.appendChild(r.extractContents()); r.insertNode(span);
  return true;
}
function partEl(root, field, part) {
  const box = field === 'q' ? root.querySelector('.qrecap .qr') : field === 'a' ? root.querySelector('.ans') : root.querySelector('.box.' + field + ' .bx');
  if (field === 'q' && part === 'heading') return root.querySelector('.c-title');
  if (!box) return null;
  if (part === 'whole') return box;
  if (/^li\d+$/.test(part)) return box.querySelectorAll('li')[+part.slice(2) - 1] || null;
  const sub = [...box.querySelectorAll('p.sub')].find(p => p.querySelector('.sp').textContent.trim() === part);
  return sub ? sub.querySelector('.sp + span') : null;
}
/** Adds tap targets to the answer face. Returns true when this card has visuals. */
export function linkCard(root, c, open) {
  const p = V.packs.get(c.deck); if (!p) return false;
  const ov = overviewOf(p, c.code);
  const links = p.links.filter(l => l.card_code === c.code);
  if (!ov && !links.length) return false;
  const title = root.querySelector('.c-title');
  if (ov && title) { title.classList.add('vl', 'vl-head'); title.setAttribute('role', 'button'); title.tabIndex = 0; title.dataset.ov = ov.scene_id; }
  for (const l of links) {
    const el = partEl(root, l.field, l.part); if (!el) continue;
    if (!l.phrase) { el.classList.add('vl'); el.dataset.seq = l.sequence_id; el.setAttribute('role', 'button'); el.tabIndex = 0; continue; }
    wrapPhrase(el, l.phrase, +l.occurrence || 1, l.sequence_id);
  }
  root.querySelectorAll('.vl').forEach(v => {
    const go = e => { e.stopPropagation(); e.preventDefault(); v.dataset.ov ? open({ deck: c.deck, code: c.code, ov: v.dataset.ov }) : open({ deck: c.deck, code: c.code, seq: v.dataset.seq }); };
    v.onclick = go; v.onkeydown = e => { if (e.key === 'Enter') go(e); };
  });
  return true;
}

/* ---------- the visual panel ---------- */
// state: { deck, code, stack: [{ ov } | { seq, i }] }
export async function drawPanel(host, st, { P, onClose }) {
  const p = V.packs.get(st.deck); if (!p) return onClose();
  const top = st.stack[st.stack.length - 1];
  const learn = P.get('visLearn', true);
  let scene, seqList = null;
  if (top.ov) scene = p.scenes.find(s => s.scene_id === top.ov);
  else { seqList = seqScenes(p, top.seq); scene = seqList[top.i || 0]; }
  if (!scene) return onClose();
  const url = await imgUrl(st.deck, scene.image);
  const story = (p.stories || []).find(s => s.scene_id === scene.scene_id);
  const cues = p.cues.filter(c => c.scene_id === scene.scene_id).sort((a, b) => a.order - b.order);
  const notes = p.notes.filter(n => n.scene_id === scene.scene_id || (top.ov && n.level === 'card' && n.card_code === scene.card_code));
  const hs = top.ov ? p.hotspots.filter(h => h.overview_id === scene.scene_id) : [];
  const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  host.innerHTML = `<div class="vp-top">
      ${st.stack.length > 1 ? '<button class="iconbtn sm" data-vb aria-label="Back to the overview">‹</button>' : '<span class="vp-sp"></span>'}
      <span class="vp-t"><span class="mono kick">${top.ov ? 'OVERVIEW' : 'SCENE'} · ${esc(scene.card_code)}</span><span class="vp-h">${esc(scene.title || '')}</span></span>
      <span class="seg vp-mode"><button class="${learn ? 'on' : ''}" data-mode="1">Learn</button><button class="${learn ? '' : 'on'}" data-mode="0">Self-test</button></span>
      <button class="iconbtn sm vp-full" data-vf aria-label="Full screen">⤢</button>
      <button class="iconbtn sm" data-vx aria-label="Close the visual">✕</button></div>
    <div class="vp-scroll">
      <div class="vp-img">${url ? `<img src="${url}" alt="${esc(scene.title || 'Scene')}">` : '<p class="muted small">Image not on this device yet.</p>'}
        ${hs.map(h => `<button class="hot" data-seq="${esc(h.sequence_id)}" style="left:${+h.x}%;top:${+h.y}%;width:${+h.w}%;height:${+h.h}%" aria-label="${esc(h.label || 'Open scene')}"><span>${esc(h.label || '')}</span></button>`).join('')}</div>
      ${seqList && seqList.length > 1 ? `<div class="vp-seq"><button class="iconbtn sm" data-si="-1" ${top.i ? '' : 'disabled'} aria-label="Previous scene">‹</button><span class="mono">${(top.i || 0) + 1} / ${seqList.length}</span><button class="iconbtn sm" data-si="1" ${top.i >= seqList.length - 1 ? 'disabled' : ''} aria-label="Next scene">›</button></div>` : ''}
      ${notes.map(n => `<div class="vnote"><span class="mono">CLINICAL NOTE · ${esc(n.kind.toUpperCase())}</span><div>${inline(n.text)}</div>${n.source ? `<i class="mono">${esc(n.source)}</i>` : ''}</div>`).join('')}
      ${cues.length ? `<details class="vcues" open><summary><span class="mono kick">CUES → MEANINGS</span></summary><ol>${cues.map(c => `<li><b>${inline(c.cue)}</b>${learn ? `<span>${inline(c.meaning)}</span>` : `<button class="reveal-m">Reveal meaning</button><span hidden>${inline(c.meaning)}</span>`}</li>`).join('')}</ol></details>` : ''}
      ${story ? `<details class="vstory"><summary><span class="mono kick">STORY${story.setting ? ' · ' + esc(story.setting.toUpperCase()) : ''}</span></summary>${story.title ? `<h3>${esc(story.title)}</h3>` : ''}${render(story.text || '')}</details>` : ''}
    </div>`;
  const redraw = () => drawPanel(host, st, { P, onClose });
  host.querySelector('[data-vx]').onclick = onClose;
  host.querySelector('[data-vf]').onclick = () => host.classList.toggle('full');
  const vb = host.querySelector('[data-vb]'); if (vb) vb.onclick = () => { st.stack.pop(); redraw(); };
  host.querySelectorAll('[data-mode]').forEach(b => b.onclick = () => { P.set('visLearn', b.dataset.mode === '1'); redraw(); });
  host.querySelectorAll('.hot').forEach(b => b.onclick = () => { st.stack.push({ seq: b.dataset.seq, i: 0 }); redraw(); });
  host.querySelectorAll('[data-si]').forEach(b => b.onclick = () => { top.i = Math.max(0, Math.min(seqList.length - 1, (top.i || 0) + +b.dataset.si)); redraw(); });
  host.querySelectorAll('.reveal-m').forEach(b => b.onclick = () => { b.nextElementSibling.hidden = false; b.remove(); });
}
export function panelKey(st, e) {
  const p = st && V.packs.get(st.deck); if (!p) return false;
  const top = st.stack[st.stack.length - 1];
  if (top.seq && (e.key === '[' || e.key === ']')) { const n = seqScenes(p, top.seq).length; top.i = Math.max(0, Math.min(n - 1, (top.i || 0) + (e.key === ']' ? 1 : -1))); return true; }
  return false;
}
