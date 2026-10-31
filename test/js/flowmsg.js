// Journal Flow-message pilot (TEST build only).
// One reviewed card (Next after Reveal) in an explicit pilot session → one request file → one plain-text reply from Journal.
// Transport: My Drive › Trace › flowmsg, through the existing bridge (listFolder, writeFile, findFile, readFile).
// This is a deliberate, narrow exception to the test build's read-only rule: it writes ONLY req-*.json into flowmsg,
// never study data. CONFIG.readOnly itself is unchanged. No file IDs live in the repo.
import { batch, hasBackend, isDemo } from './api.js';
import { CONFIG, CHANNEL } from './config.js';
import { db } from './db.js';

const FOLDER = 'flowmsg', WINDOW_MS = 5 * 60e3, EVERY_MS = 15e3, MAX_CHARS = 280;
const ID_RE = /^fm-\d{8}-\d{6}-[a-z0-9]{6}$/;

export const FM = { state: 'idle', requestId: '', card: '', created: 0, text: '', note: '', dismissed: false, timer: null, onChange: null, folderId: '' };
const changed = () => { try { FM.onChange && FM.onChange(); } catch (e) { /* screen gone */ } };
const ist = ts => new Date(ts + 5.5 * 3600e3).toISOString().slice(0, 19) + '+05:30';
function newId(ts) {
  const s = new Date(ts + 5.5 * 3600e3).toISOString();
  let r = ''; const a = 'abcdefghijklmnopqrstuvwxyz0123456789', b = new Uint8Array(6); crypto.getRandomValues(b);
  for (const x of b) r += a[x % 36];
  return 'fm-' + s.slice(0, 10).replace(/-/g, '') + '-' + s.slice(11, 19).replace(/:/g, '') + '-' + r;
}
export const pilotAllowed = () => CHANNEL === 'test' && !isDemo() && hasBackend();

async function folderId() {
  if (FM.folderId) return FM.folderId;
  const [r] = await batch([{ op: 'listFolder', id: CONFIG.traceFolderId }]);
  if (!r.ok) throw new Error(r.error);
  const d = (r.data || []).find(x => x.kind === 'folder' && x.name === FOLDER);
  if (!d) throw new Error('Trace › flowmsg folder not found');
  FM.folderId = d.id; return d.id;
}
const save = () => db.kv.set('flowmsgPilot', { requestId: FM.requestId, card: FM.card, created: FM.created, state: FM.state, text: FM.text, note: FM.note }).catch(() => {});

/** Pilot session opened: resume a pending request from a reload instead of making a duplicate. Returns true if resumed. */
export async function resumePending(onChange) {
  FM.onChange = onChange;
  const p = await db.kv.get('flowmsgPilot').catch(() => null);
  if (p && p.state === 'waiting' && ID_RE.test(p.requestId) && Date.now() - p.created < WINDOW_MS) {
    Object.assign(FM, { state: 'waiting', requestId: p.requestId, card: p.card || '', created: p.created, text: '', note: 'Journal is listening… (resumed)', dismissed: false });
    changed(); poll(); return true;
  }
  Object.assign(FM, { state: 'idle', requestId: '', card: '', created: 0, text: '', note: '', dismissed: false });
  return false;
}

/** The first reviewed card in a pilot session. card = the card just walked; secs = seconds on it. */
export async function sendRequest(card, deckTitle, secs, sentBackAgain) {
  if (!pilotAllowed() || FM.state !== 'idle') return;
  const created = Date.now(), requestId = newId(created);
  Object.assign(FM, { state: 'sending', requestId, card: card.code, created, text: '', note: 'Asking Journal…', dismissed: false }); changed();
  const req = {
    type: 'trace.flowmsg.request', version: 1, requestId, created: ist(created), expires: ist(created + WINDOW_MS),
    test: true, bot: 'Journal', event: 'card_reviewed',
    meaning: 'The card was revealed and moved past. This is NOT a correctness or mastery signal.',
    card: { deck: card.deck, deckTitle: deckTitle || '', code: card.code, section: card.section || '', secondsOnCard: Math.max(0, Math.round(secs)), sentBackAgain: !!sentBackAgain },
    reply: { file: 'res-' + requestId + '.json', format: 'plain text', maxChars: MAX_CHARS }
  };
  try {
    const fid = await folderId();
    const name = 'req-' + requestId + '.json';
    if (!/^req-fm-\d{8}-\d{6}-[a-z0-9]{6}\.json$/.test(name)) throw new Error('bad request name');
    const [w] = await batch([{ op: 'writeFile', folderId: fid, name, text: JSON.stringify(req, null, 1), mime: 'text/plain' }]);
    if (!w.ok) throw new Error(w.error);
    FM.state = 'waiting'; FM.note = 'Journal is listening… (up to 5 minutes)'; await save(); changed();
    poll();
  } catch (e) { FM.state = 'error'; FM.note = 'Could not send the request: ' + (e.message || e); await save(); changed(); }
}

function clean(t) { return String(t).replace(/[\u0000-\u001F\u007F\u2028\u2029]+/g, ' ').replace(/\s+/g, ' ').trim(); }
async function poll() {
  clearTimeout(FM.timer);
  if (FM.state !== 'waiting') return;
  if (Date.now() - FM.created > WINDOW_MS) { FM.state = 'timeout'; FM.note = 'No reply from Journal within 5 minutes.'; await save(); return changed(); }
  try {
    const fid = await folderId();
    const [f] = await batch([{ op: 'findFile', folderId: fid, name: 'res-' + FM.requestId + '.json' }]);
    if (!f.ok) throw new Error(f.error);
    if (f.data && f.data.id) {
      const [r] = await batch([{ op: 'readFile', id: f.data.id }]);
      if (!r.ok) throw new Error(r.error);
      if (FM.state !== 'waiting') return;                      // stopped meanwhile: a late reply is ignored
      let j; try { j = JSON.parse(String(r.data.text || '').replace(/^﻿/, '')); } catch (e) { return fail('the reply is not valid JSON'); }
      if (!j || j.type !== 'trace.flowmsg.response') return fail('wrong reply type');
      if (j.requestId !== FM.requestId) return fail('the reply is for a different request');
      if (typeof j.text !== 'string') return fail('the reply has no text');
      const text = clean(j.text);
      if (!text) return fail('the reply text is empty');
      if (text.length > MAX_CHARS) return fail(`the reply is ${text.length} characters (limit ${MAX_CHARS})`);
      FM.state = 'reply'; FM.text = text; FM.note = ''; FM.dismissed = false; await save(); return changed();
    }
  } catch (e) { FM.note = 'Journal is listening… (connection hiccup: ' + (e.message || e) + ')'; changed(); }
  FM.timer = setTimeout(poll, EVERY_MS);
}
async function fail(why) { FM.state = 'invalid'; FM.note = 'Journal replied, but it can’t be shown: ' + why + '.'; await save(); changed(); }

/** Flow closed: stop listening. A pending request stays resumable for the rest of its 5 minutes. */
export function stopPolling() { clearTimeout(FM.timer); FM.timer = null; FM.onChange = null; }
