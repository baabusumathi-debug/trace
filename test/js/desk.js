// T-148: Trace Desk — the phone (or Mac) beside the Tab, with nothing to link by hand.
// Whichever device is walking a flow offers itself; whichever device opens the Desk joins it. Only Naven uses these
// devices, so there is no code: one offer per profile and channel. The two talk directly over the same Wi-Fi or
// hotspot (WebRTC). Drive is used only to introduce them: the walking device leaves an offer in
// Trace/desk-<name>-o.json, the Desk answers in desk-<name>-a.json (small files, overwritten each time).
// Nothing about study goes through Drive. Display only.
import { CONFIG, CHANNEL, IS_HT } from './config.js';
import { batch, hasBackend } from './api.js';

const NAME = (CHANNEL === 'test' ? 't' : 'l') + (IS_HT ? 'h' : 'n');
const fname = side => 'desk-' + NAME + '-' + side + '.json';
const ICE = { iceServers: [{ urls: 'stun:stun.l.google.com:19302' }] };
const wait = ms => new Promise(r => setTimeout(r, ms));
const iceDone = pc => new Promise(r => { if (pc.iceGatheringState === 'complete') return r(); const t = setTimeout(r, 3000); pc.addEventListener('icegatheringstatechange', () => { if (pc.iceGatheringState === 'complete') { clearTimeout(t); r(); } }); });
async function writeJ(name, obj) { const [r] = await batch([{ op: 'writeFile', folderId: CONFIG.traceFolderId, name, text: JSON.stringify(obj), mime: 'application/json' }]); return r && r.ok; }
async function findJ(name) { const [f] = await batch([{ op: 'findFile', folderId: CONFIG.traceFolderId, name }]); return f && f.ok && f.data && f.data.id ? f.data : null; }
async function readId(id) { const [r] = await batch([{ op: 'readFile', id }]); try { return r && r.ok ? JSON.parse(r.data.text) : null; } catch (e) { return null; } }

/* ============================ the walking device: host ============================ */
const H = { pc: null, ch: null, state: 'off', src: null, tick: 0, last: '', listeners: new Set(), gen: 0 };
export const deskState = () => H.state;
export function onDesk(fn) { H.listeners.add(fn); return () => H.listeners.delete(fn); }
const tell = s => { H.state = s; H.listeners.forEach(f => { try { f(s); } catch (e) { /* */ } }); };
export function setDeskSource(fn) { H.src = fn; }
// offered while a flow is open; a Desk that opens later is picked up (the answer file is checked every 10 s)
export async function startHost() {
  if (!hasBackend() || !window.RTCPeerConnection) return;
  const g = ++H.gen; closePc();
  tell('waiting');
  const pc = new RTCPeerConnection(ICE), ch = pc.createDataChannel('desk', { ordered: true });
  H.pc = pc; H.ch = ch;
  ch.onopen = () => { if (g !== H.gen) return; tell('live'); H.last = ''; pushDesk(true); clearInterval(H.tick); H.tick = setInterval(() => pushDesk(false), 2000); };
  ch.onclose = () => { if (g !== H.gen) return; clearInterval(H.tick); tell('waiting'); setTimeout(() => { if (g === H.gen) startHost(); }, 1500); };   // the Desk closed: offer again
  pc.onconnectionstatechange = () => { if (g === H.gen && ['failed', 'disconnected'].includes(pc.connectionState)) { try { ch.close(); } catch (e) { /* */ } if (H.state !== 'live') setTimeout(() => { if (g === H.gen) startHost(); }, 1500); } };
  try {
    await pc.setLocalDescription(await pc.createOffer()); await iceDone(pc);
    if (g !== H.gen) return;
    const ts = Date.now();
    if (!await writeJ(fname('o'), { ts, sdp: pc.localDescription })) { tell('error'); return; }
    let seen = '';
    while (g === H.gen && H.state === 'waiting') {
      await wait(document.visibilityState === 'visible' ? 10000 : 30000);
      if (g !== H.gen || H.state !== 'waiting') return;
      const f = await findJ(fname('a')).catch(() => null);
      if (!f || f.modified === seen) continue;
      seen = f.modified;
      const a = await readId(f.id).catch(() => null);
      if (g !== H.gen) return;
      if (a && a.of === ts && a.sdp) {
        await pc.setRemoteDescription(a.sdp);
        setTimeout(() => { if (g === H.gen && H.state !== 'live') startHost(); }, 20000);   // did not open: a fresh offer
        return;
      }
    }
  } catch (e) { if (g === H.gen) { tell('error'); setTimeout(() => { if (g === H.gen) startHost(); }, 30000); } }
}
function closePc() {
  clearInterval(H.tick);
  try { if (H.ch) H.ch.close(); } catch (e) { /* */ }
  try { if (H.pc) H.pc.close(); } catch (e) { /* */ }
  H.pc = null; H.ch = null;
}
export function stopHost() { const was = H.state !== 'off'; H.gen++; closePc(); tell('off'); if (was && hasBackend()) writeJ(fname('o'), { ts: Date.now(), sdp: null }).catch(() => {}); }   // the flow ended: no offer left behind
// send when something changed (and at least every 10 s, so the Desk knows the link is alive)
export function pushDesk(force) {
  if (!H.ch || H.ch.readyState !== 'open' || !H.src) return;
  let snap; try { snap = H.src(); } catch (e) { return; }
  const j = JSON.stringify({ ...snap, ts: 0 });
  if (!force && j === H.last && Date.now() - (H.sentAt || 0) < 10000) return;
  H.last = j; H.sentAt = Date.now();
  try { H.ch.send(JSON.stringify({ ...snap, ts: Date.now() })); } catch (e) { /* */ }
}

/* ============================ the Desk: guest ============================ */
const G = { pc: null, state: 'off', snap: null, at: 0, gen: 0, listeners: new Set(), lastOffer: 0 };
export const guestState = () => G.state;
export const guestSnap = () => G.snap;
export const guestAt = () => G.at;
export function onGuest(fn) { G.listeners.add(fn); return () => G.listeners.delete(fn); }
const gtell = s => { G.state = s; G.listeners.forEach(f => { try { f(s); } catch (e) { /* */ } }); };
const onDeskPage = () => /^#\/desk/.test(location.hash);
const retry = (g, ms) => setTimeout(() => { if (g === G.gen && onDeskPage()) joinDesk(); }, ms);
export async function joinDesk() {
  if (!hasBackend() || !window.RTCPeerConnection) { gtell('unsupported'); return; }
  const g = ++G.gen; try { if (G.pc) G.pc.close(); } catch (e) { /* */ } G.pc = null;
  if (G.state !== 'live') gtell('looking');
  try {
    const f = await findJ(fname('o')).catch(() => null), o = f && await readId(f.id).catch(() => null);
    if (g !== G.gen) return;
    if (!o || !o.sdp || o.ts <= G.lastOffer) { gtell('noflow'); retry(g, document.visibilityState === 'visible' ? 8000 : 30000); return; }   // no flow open, or the same offer that failed
    G.lastOffer = o.ts;
    const pc = new RTCPeerConnection(ICE); G.pc = pc;
    pc.ondatachannel = e => {
      const ch = e.channel;
      ch.onopen = () => { if (g === G.gen) gtell('live'); };
      ch.onmessage = m => { if (g !== G.gen) return; try { G.snap = JSON.parse(m.data); G.at = Date.now(); if (G.state !== 'live') gtell('live'); else G.listeners.forEach(fn => { try { fn('live'); } catch (er) { /* */ } }); } catch (er) { /* */ } };
      ch.onclose = () => { if (g !== G.gen) return; gtell('lost'); retry(g, 3000); };
    };
    pc.onconnectionstatechange = () => { if (g === G.gen && pc.connectionState === 'failed' && G.state !== 'live') { gtell('apart'); retry(g, 12000); } };
    gtell('connecting');
    await pc.setRemoteDescription(o.sdp);
    await pc.setLocalDescription(await pc.createAnswer()); await iceDone(pc);
    await writeJ(fname('a'), { ts: Date.now(), of: o.ts, sdp: pc.localDescription });
    setTimeout(() => { if (g === G.gen && G.state === 'connecting') { gtell('apart'); retry(g, 12000); } }, 30000);
  } catch (e) { if (g === G.gen) { gtell('error'); retry(g, 15000); } }
}
export function leaveDesk() { G.gen++; try { if (G.pc) G.pc.close(); } catch (e) { /* */ } G.pc = null; gtell('off'); }
