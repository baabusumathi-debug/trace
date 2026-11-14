// T-170: the 3D echo model beside a viva lesson. One iframe (echo/index.html?embed=1) is kept alive for the whole walk and
// laid over an empty box in the card, so moving from step to step only sends the new state (no reload, no flicker).
// A step's `model` object (view, turn, tilt, camera, show, path, phase, mmode, highlight) goes to the model by postMessage.
import { qOf } from './viva.js';

const SRC = 'echo/index.html?embed=1';
let P = { get: () => null, set: () => {} };
export const initEcho = prefs => { P = prefs; };
let layer = null, frame = null, ready = false, want = null, raf = 0;
const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

export function stepModel(pkg, qid, j) { const q = qOf(pkg, qid); const s = q && q.steps && q.steps[j]; return s && s.model && typeof s.model === 'object' ? s.model : null; }
const isOff = () => !!P.get('echoOff');

export function echoSlotHtml(model) {
  if (!model) return '';
  const off = isOff();
  return `<div class="echo-slot${off ? ' off' : ''}" data-echo="${esc(JSON.stringify(model))}"><div class="echo-bar mono"><span>3D MODEL · ${esc(model.view || '')}${model.path && model.path !== 'normal' ? ' · ' + esc(model.path) : ''}</span><button class="linkbtn small" data-echotog>${off ? 'Show' : 'Hide'}</button></div>${off ? '' : '<div class="echo-box"></div>'}</div>`;
}

function ensure() {
  if (layer) return;
  layer = document.createElement('div'); layer.id = 'echoLayer'; layer.style.display = 'none';
  frame = document.createElement('iframe'); frame.title = '3D echo model'; frame.setAttribute('allow', 'fullscreen');
  frame.src = SRC + (want ? '#' + encodeURIComponent(JSON.stringify(want)) : '');
  layer.appendChild(frame); document.body.appendChild(layer);
  addEventListener('message', e => { if (e.source === frame.contentWindow && e.data && e.data.type === 'echo-ready') { ready = true; if (want) send(want); } });
}
function send(m) { want = m; if (ready && frame && frame.contentWindow) frame.contentWindow.postMessage({ type: 'echo-model', model: m }, location.origin); }

function place() {
  raf = 0;
  const box = document.querySelector('.echo-slot .echo-box');
  if (!box || !box.isConnected) { if (layer) layer.style.display = 'none'; return; }
  const r = box.getBoundingClientRect();
  if (r.width < 40 || r.height < 40) layer.style.display = 'none';
  else Object.assign(layer.style, { display: 'block', left: r.left + 'px', top: r.top + 'px', width: r.width + 'px', height: r.height + 'px' });
  raf = requestAnimationFrame(place);
}

// call after a card is drawn; it finds the slot (if any), shows the model there with this step's state
export function mountEcho(root) {
  const slot = root.querySelector('.echo-slot');
  if (!slot) { if (layer) layer.style.display = 'none'; return; }
  if (!slot.dataset.bound) { slot.dataset.bound = '1'; ['pointerdown', 'click', 'touchstart'].forEach(t => slot.addEventListener(t, e => e.stopPropagation())); }
  const tog = slot.querySelector('[data-echotog]');
  if (tog) tog.onclick = () => {   // in place: redrawing the card would restart the lesson voice
    const off = !isOff(); P.set('echoOff', off); slot.classList.toggle('off', off); tog.textContent = off ? 'Show' : 'Hide';
    const b = slot.querySelector('.echo-box'); if (off && b) b.remove(); if (!off && !b) slot.insertAdjacentHTML('beforeend', '<div class="echo-box"></div>');
    if (off) hideEcho(); else mountEcho(root);
  };
  if (isOff()) { if (layer) layer.style.display = 'none'; return; }
  let m = null; try { m = JSON.parse(slot.dataset.echo); } catch (e) { /* no state */ }
  want = m || want; ensure(); if (m) send(m);
  if (!raf) raf = requestAnimationFrame(place);
}
export function hideEcho() { if (layer) layer.style.display = 'none'; }
