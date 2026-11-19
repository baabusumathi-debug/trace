// T-176: HT's notes — the pages of HT's annotated deck PDFs (Samsung Notes exports), one set per card.
// Built by Claude from the PDFs in Drive › Trace › ht-notes: each page is matched to its card by the card code printed in
// the page header; pages HT inserted (no code) go with the card before them. Stored per deck in Drive › Trace › ht-notes ›
// cards › <DECK>.json as { deck, pages, cards: { code: [{ p, ins, img }] } } (img = WebP data URL). Kept on the device.
import { db } from './db.js';
import { call } from './api.js';

const FOLDER = '1e3kNJOGRmKNn9m_jbozT9TxoidQyYcZz';
const H = {};          // deck → { code: [pages] }
let idx = {};          // deck → modified time of the loaded file

export async function initHtNotes() {
  try {
    idx = (await db.kv.get('htn-idx')) || {};
    for (const d of Object.keys(idx)) { const v = await db.kv.get('htn:' + d); if (v) H[d] = v; }
  } catch (e) { /* nothing stored yet */ }
}
// reads only the decks whose file changed since last time; one file at a time (each is a few MB)
export async function loadHtNotes(onDeck) {
  let list;
  try { list = await call({ op: 'listFolder', id: FOLDER }); } catch (e) { return; }
  for (const f of list || []) {
    const m = String(f.name).match(/^([A-Z0-9\-]+)\.json$/); if (!m || f.kind !== 'file') continue;
    const d = m[1]; if (idx[d] === f.modified && H[d]) continue;
    try {
      const r = await call({ op: 'readFile', id: f.id }); const j = JSON.parse(r.text);
      H[d] = j.cards || {}; idx[d] = f.modified;
      await db.kv.set('htn:' + d, H[d]); await db.kv.set('htn-idx', idx);
      onDeck && onDeck(d);
    } catch (e) { /* try again next time */ }
  }
}
export const htOf = c => (c && H[c.deck] && H[c.deck][c.code]) || null;
export const htDecks = () => Object.keys(H);

export function htPaneHtml(c, sw) {
  const all = htOf(c) || [], pg = all.length > 1 ? [...all.slice(1), all[0]] : all;   // answer page and her added pages first, the question page last
  return `<div class="xp v2 vx open ht-pane" data-depth="learn"><div class="xp-bar"><span class="xp-tog"${sw ? ' hidden' : ''}><span>HT's notes</span></span>${sw}</div>
    <div class="xp-body"><p class="ht-src mono">HT's deck · page${pg.length > 1 ? 's' : ''} ${pg.map(x => x.p).join(', ')}${pg.some(x => x.ins) ? ' · includes pages she added' : ''}</p>
    ${pg.map(x => `<figure class="ht-pg${x.ins ? ' ins' : ''}"><img src="${x.img}" alt="HT's page ${x.p}" loading="lazy">${x.ins ? '<figcaption class="mono">added by HT</figcaption>' : ''}</figure>`).join('')}</div></div>`;
}
