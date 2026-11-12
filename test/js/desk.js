// T-142: Trace Desk — the phone beside the Tab. The Tab (host) sends a small picture of where you are (session, question,
// card, day plan, breaks, tiles) to the phone over a direct WebRTC link on the same Wi-Fi or hotspot. The Drive bridge
// is used only to introduce the two: the Tab leaves an offer in Trace/desk-<code>-o.json, the phone answers in
// desk-<code>-a.json (two small files, overwritten each time). Nothing about study goes through Drive. Display only.
import { CONFIG, CHANNEL, IS_HT } from './config.js';
import { batch, hasBackend } from './api.js';

const PK = (CHANNEL === 'test' ? 'trace-test.' : 'trace.') + (IS_HT ? 'ht.' : '');
const lget = (k, d) => { try { const v = localStorage.getItem(PK + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } };
const lset = (k, v) => { try { localStorage.setItem(PK + k, JSON.stringify(v)); } catch (e) { /* private mode */ } };
const ICE = { iceServers: [{ urls: 'stun:stun.l.google.com:19302' }] };
const fname = (code, side) => 'desk-' + code + '-' + side + '.json';
const wait = ms => new Promise(r => setTimeout(r, ms));
const iceDone = pc => new Promise(r => { if (pc.iceGatheringState === 'complete') return r(); const t = setTimeout(r, 3000); pc.addEventListener('icegatheringstatechange', () => { if (pc.iceGatheringState === 'complete') { clearTimeout(t); r(); } }); });
async function writeJ(name, obj) { const [r] = await batch([{ op: 'writeFile', folderId: CONFIG.traceFolderId, name, text: JSON.stringify(obj), mime: 'application/json' }]); return r && r.ok; }
async function readJ(name) {
  const [f] = await batch([{ op: 'findFile', folderId: CONFIG.traceFolderId, name }]);
  if (!f || !f.ok || !f.data || !f.data.id) return null;
  const [r] = await batch([{ op: 'readFile', id: f.data.id }]);
  try { return r && r.ok ? JSON.parse(r.data.text) : null; } catch (e) { return null; }
}

/* ============================ the Tab: host ============================ */
const H = { pc: null, ch: null, state: 'off', code: lget('deskCode', null), src: null, tick: 0, last: '', listeners: new Set(), gen: 0 };
export const deskCode = () => H.code || (H.code = String(1000 + Math.floor(Math.random() * 9000)), lset('deskCode', H.code), H.code);
export const deskState = () => H.state;
export const deskOn = () => !!lget('deskOn', false);
export function onDesk(fn) { H.listeners.add(fn); return () => H.listeners.delete(fn); }
const tell = s => { H.state = s; H.listeners.forEach(f => { try { f(s); } catch (e) { /* */ } }); };
export function setDeskSource(fn) { H.src = fn; }
export function newDeskCode() { H.code = null; lset('deskCode', null); deskCode(); return H.code; }
export async function startHost() {
  if (!hasBackend() || !window.RTCPeerConnection) { tell('unsupported'); return; }
  lset('deskOn', true);
  const g = ++H.gen; closeHost(true);
  tell('waiting');
  const pc = new RTCPeerConnection(ICE), ch = pc.createDataChannel('desk', { ordered: true });
  H.pc = pc; H.ch = ch;
  ch.onopen = () => { if (g !== H.gen) return; tell('live'); H.last = ''; pushDesk(true); clearInterval(H.tick); H.tick = setInterval(() => pushDesk(false), 2000); };
  ch.onclose = () => { if (g !== H.gen) return; clearInterval(H.tick); tell('lost'); setTimeout(() => { if (g === H.gen && deskOn()) startHost(); }, 1500); };
  pc.onconnectionstatechange = () => { if (g === H.gen && ['failed', 'disconnected'].includes(pc.connectionState) && H.state === 'live') { try { ch.close(); } catch (e) { /* */ } } };
  try {
    await pc.setLocalDescription(await pc.createOffer()); await iceDone(pc);
    const ts = Date.now();
    if (!await writeJ(fname(deskCode(), 'o'), { ts, sdp: pc.localDescription })) { tell('error'); return; }
    for (let i = 0; i < 60 && g === H.gen && H.state === 'waiting'; i++) {          // up to 3 minutes for the phone
      await wait(3000);
      const a = await readJ(fname(H.code, 'a')).catch(() => null);
      if (g !== H.gen) return;
      if (a && a.ts > ts && a.of === ts && a.sdp) { await pc.setRemoteDescription(a.sdp); return; }
    }
    if (g === H.gen && H.state === 'waiting') tell('idle');
  } catch (e) { if (g === H.gen) tell('error'); }
}
function closeHost(keepOn) {
  clearInterval(H.tick);
  try { if (H.ch) H.ch.close(); } catch (e) { /* */ }
  try { if (H.pc) H.pc.close(); } catch (e) { /* */ }
  H.pc = null; H.ch = null;
  if (!keepOn) { lset('deskOn', false); H.gen++; tell('off'); }
}
export const stopHost = () => closeHost(false);
// send when something changed (and at least every 10 s, so the phone knows the link is alive)
export function pushDesk(force) {
  if (!H.ch || H.ch.readyState !== 'open' || !H.src) return;
  let snap; try { snap = H.src(); } catch (e) { return; }
  const j = JSON.stringify({ ...snap, ts: 0 });
  if (!force && j === H.last && Date.now() - (H.sentAt || 0) < 10000) return;
  H.last = j; H.sentAt = Date.now();
  try { H.ch.send(JSON.stringify({ ...snap, ts: Date.now() })); } catch (e) { /* */ }
}

/* ============================ the phone: guest ============================ */
const G = { pc: null, state: 'off', snap: null, at: 0, gen: 0, listeners: new Set(), lastOffer: 0 };
export const guestCode = () => lget('deskJoin', '');
export const guestState = () => G.state;
export const guestSnap = () => G.snap;
export const guestAt = () => G.at;
export function onGuest(fn) { G.listeners.add(fn); return () => G.listeners.delete(fn); }
const gtell = s => { G.state = s; G.listeners.forEach(f => { try { f(s); } catch (e) { /* */ } }); };
export async function joinDesk(code) {
  if (!hasBackend() || !window.RTCPeerConnection) { gtell('unsupported'); return; }
  code = String(code || '').replace(/\D/g, '').slice(0, 4); if (code.length !== 4) { gtell('badcode'); return; }
  lset('deskJoin', code);
  const g = ++G.gen; try { if (G.pc) G.pc.close(); } catch (e) { /* */ } G.pc = null;
  gtell('looking');
  try {
    let o = null;
    for (let i = 0; i < 60 && g === G.gen; i++) {                                     // up to 3 minutes for the Tab's offer
      o = await readJ(fname(code, 'o')).catch(() => null);
      if (o && o.sdp && o.ts > G.lastOffer && Date.now() - o.ts < 10 * 60000) break;
      o = null; await wait(3000);
    }
    if (g !== G.gen) return;
    if (!o) { gtell('notfound'); return; }
    G.lastOffer = o.ts;
    const pc = new RTCPeerConnection(ICE); G.pc = pc;
    pc.ondatachannel = e => {
      const ch = e.channel;
      ch.onopen = () => { if (g === G.gen) gtell('live'); };
      ch.onmessage = m => { if (g !== G.gen) return; try { G.snap = JSON.parse(m.data); G.at = Date.now(); gtell('live'); } catch (er) { /* */ } };
      ch.onclose = () => { if (g !== G.gen) return; gtell('lost'); setTimeout(() => { if (g === G.gen) joinDesk(code); }, 2000); };
    };
    pc.onconnectionstatechange = () => { if (g === G.gen && pc.connectionState === 'failed') { gtell('lost'); setTimeout(() => { if (g === G.gen) joinDesk(code); }, 2000); } };
    gtell('connecting');
    await pc.setRemoteDescription(o.sdp);
    await pc.setLocalDescription(await pc.createAnswer()); await iceDone(pc);
    await writeJ(fname(code, 'a'), { ts: Date.now(), of: o.ts, sdp: pc.localDescription });
    setTimeout(() => { if (g === G.gen && G.state === 'connecting') { gtell('lost'); joinDesk(code); } }, 25000);
  } catch (e) { if (g === G.gen) gtell('error'); }
}
export function leaveDesk() { G.gen++; try { if (G.pc) G.pc.close(); } catch (e) { /* */ } G.pc = null; lset('deskJoin', ''); gtell('off'); }
