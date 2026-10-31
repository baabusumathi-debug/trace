// The Palace of the Work (home) and the meditation alcove inside the Loft.
// Four entrances: Loft (see), Decks (choose), Flow (work), Meditation (release). The open window has no function.
import { db } from './db.js';

const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

// room boxes in % of the picture — taken from the supplied model, separately for each composition
const ROOMS = {
  land: { loft: [14, 17, 27, 24], meditation: [66, 17, 24, 23], decks: [12, 45, 27, 34], flow: [49, 58, 29, 28] },
  port: { loft: [6, 17, 43, 22], meditation: [53, 17, 44, 22], decks: [5, 43, 44, 24], flow: [43, 65, 51, 24] }
};
const ROOM = {
  loft: { href: '#/loft', icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2.5 12s3.6-6 9.5-6 9.5 6 9.5 6-3.6 6-9.5 6-9.5-6-9.5-6z"/><circle cx="12" cy="12" r="2.6"/></svg>', name: 'The Loft', sub: 'See before doing', aria: 'Enter the Loft: orientation and progress' },
  meditation: { href: '#/meditation', icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.5" stroke-dasharray="1.2 3.1"/><circle cx="12" cy="12" r="1.6" fill="currentColor" stroke="none"/></svg>', name: 'Meditation', sub: 'A quiet place in the Loft', aria: 'Enter the meditation alcove' },
  decks: { href: '#/shelf', icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 20.5h17M5.5 20.5V6.5h3v14M10.5 20.5v-16h3v16M15.6 20.5l-1.4-12.6 3-.4 1.6 13"/></svg>', name: 'The Decks', sub: 'Choose your work', aria: 'Open the deck shelf' },
  flow: { href: '#/flow', icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5" stroke-opacity=".5"/><circle cx="12" cy="12" r="1.3" fill="currentColor" stroke="none"/></svg>', name: 'Flow', sub: 'One thing, held here', aria: 'Enter Flow: the working Circle' }
};
const IMG = { land: ['img/palace-land.webp', 1672, 941], port: ['img/palace-port.webp', 941, 1672] };

export function renderPalace(app, { nav, top }) {
  app.innerHTML = `<div class="screen palace-screen">
    ${top}
    <div class="palace-stage" id="pstage"><div class="palace" id="palace"></div></div>
    ${nav}
  </div>`;
  const stage = app.querySelector('#pstage'), box = app.querySelector('#palace');
  let shape = '';
  const layout = () => {
    if (!box.isConnected) { ro.disconnect(); return; }
    const W = stage.clientWidth, H = stage.clientHeight;
    if (!W || !H) return;
    const s = W / H >= 1 ? 'land' : 'port';
    const [src, iw, ih] = IMG[s];
    const k = Math.min(W / iw, H / ih);                 // the whole picture, never cropped: rooms stay where the art puts them
    box.style.width = Math.round(iw * k) + 'px'; box.style.height = Math.round(ih * k) + 'px';
    if (s === shape) return;
    shape = s;
    box.className = 'palace ' + s;
    box.innerHTML = `<img src="${src}" alt="An empty magician’s palace: a cool writing Loft and a meditation cushion above, a deck cabinet and a warmly lit working Circle below, and an open window." draggable="false">
      <div class="p-intro"><span class="p-eye">The palace of the work</span><span class="p-h">Enter with intention.</span><span class="p-p">See clearly. Choose. Begin. Return.</span></div>
      ${Object.entries(ROOMS[s]).map(([k, [l, t, w, h]]) => { const r = ROOM[k]; return `<a class="room r-${k}" href="${r.href}" style="left:${l}%;top:${t}%;width:${w}%;height:${h}%" aria-label="${r.aria}">
        <span class="room-label"><span class="room-icon" aria-hidden="true">${r.icon}</span><span><strong>${r.name}</strong><small>${r.sub}</small></span></span></a>`; }).join('')}
      <span class="p-cap">The window stays open.</span>`;
    box.querySelectorAll('.room').forEach(a => a.onclick = e => {
      e.preventDefault();
      if (box.classList.contains('entering')) return;
      a.classList.add('chosen'); box.classList.add('entering');
      setTimeout(() => { location.hash = a.getAttribute('href'); }, 280);
    });
  };
  const ro = new ResizeObserver(layout);
  ro.observe(stage);
  layout();
}

/* ============================ meditation ============================ */
// Sample guidance from the model. Later: three daily recordings generated from the real work, stored privately, kept offline.
export const TRACKS = {
  morning: { title: 'Open the window', category: 'Morning · orientation', description: 'See what is here. Name one thing. Open your hand.', text: 'Find a position that feels comfortable. Let your eyes rest wherever they wish. There is nothing you need to force.\n\nImagine the cool light in the Loft. The table is quiet. Yesterday’s work rests on it, complete in some places and unfinished in others. Let it offer information. You do not have to turn it into a verdict about yourself.\n\nAllow one ordinary breath to arrive and leave. Notice the support beneath you.\n\nThe magician’s work begins with clear seeing. What is actually here today? What time and energy do you have? What one piece of work deserves them? You do not need to answer every question at once.\n\nPlace one intention on the table. Keep it small enough to carry. Imagine taking that single slip downstairs into the Circle. The tools are ready. The rest can wait.\n\nThe window remains open. Insight may arrive; you do not have to summon it. When you are ready, return your attention to the room around you. Begin with the first honest step.' },
  afternoon: { title: 'Narrow the Circle', category: 'Afternoon · recalibration', description: 'Meet the day as it is. Adjust the next piece.', text: 'Pause where you are. Feel the place supporting you. Let your breathing find its own pace.\n\nPicture the working Circle in the palace. A warm pool of light falls on one desk. Some of the morning may have gone as you intended. Some may have taken another shape. You can begin from the day that is actually here.\n\nLook gently at what belongs in the Circle now. Notice anything you have brought in that does not need your attention yet. You may set it on the shelf outside. Nothing has to disappear for you to work on one thing.\n\nAsk yourself: what is the next useful piece, at the size I can meet? A card. A question. A short return. If you need rest, that can be an honest choice too.\n\nThe magician’s steadiness is in choosing deliberately. You do not need to manufacture a feeling of flow. You can make room for contact with the work.\n\nLet your shoulders settle if that feels comfortable. Return to the actual room. Carry only the next piece.' },
  night: { title: 'Leave the lamp', category: 'Night · release', description: 'Acknowledge what happened. Leave a line for tomorrow.', text: 'Let this be a place to finish the day. You do not have to finish every task. Find a comfortable position and allow your breathing to remain ordinary.\n\nImagine the palace becoming quiet. In the Store Room, the work you have made is still there. You do not need to inspect it again to keep it real. Let yourself acknowledge one thing you attended to today, however small.\n\nNow walk in imagination to the Threshold. A lamp lights a narrow writing ledge. There is room for one line. What would help you begin next time? Choose a simple next action. You can write it in the app after this guidance.\n\nLet the unfinished task rest beside that line. It can remain unfinished without being lost. You are allowed to put it down.\n\nThe magician leaves the tools in their places. The Circle is clear. The window stays open to what cannot be made on demand.\n\nWhen you are ready, let the lamp go out in your imagination. Notice the room around you. The work has somewhere to wait. So do you.' },
  restart: { title: 'The first honest step', category: 'Scenario · lost momentum', description: 'You do not have to recover the whole day at once.', text: 'Take a quiet moment. Notice the contact of your feet or your seat with what supports you. Let your breath be ordinary.\n\nPicture the palace as you left it. You are welcome to return without explaining your absence. The tools still have their places. The desk can hold a small beginning.\n\nChoose the smallest useful action that would count as contact with the work. Opening a deck may be enough to begin. Reading one question may be the next step. Let the action be specific and possible.\n\nThe magician’s energy here is quiet resourcefulness. You can work with the state you are in. You do not have to wait for a perfect one.\n\nLet the rest of the day remain outside the Circle for a moment. Bring in this one action. When you are ready, do it gently and deliberately.' },
  overwhelmed: { title: 'Let the Circle be small', category: 'Scenario · too many open threads', description: 'Keep one thing close. Give the others somewhere to wait.', text: 'Let your gaze settle on something still. Notice your surroundings. There is no need to make your mind empty.\n\nImagine the Circle in the palace. You may have brought many things inside it: plans, unfinished questions, expectations. Acknowledge them without solving them now.\n\nPicture placing them on the shelves around the room, one at a time. They remain available. The desk needs room for only one piece.\n\nChoose that piece by usefulness and by the energy you actually have. If you cannot choose yet, let the first action be writing down the options.\n\nThe magician prepares a clear working space. You can return to it whenever the Circle becomes crowded. Feel the support beneath you again. Take the next small action when you are ready.' },
  disappointed: { title: 'Read without a verdict', category: 'Scenario · a difficult result', description: 'A result can inform your next move without defining you.', text: 'Give yourself a moment before making a plan. You may feel disappointed. You do not have to push that feeling away. Let your body be supported and your breath remain natural.\n\nImagine placing the result on the Loft’s table. It is something you can look at. You do not need to become it.\n\nWhen you are ready, ask what it actually tells you. There may be a knowledge gap, a retrieval gap, or simply a question that needs a second look. Let the answer remain specific.\n\nYou can choose one repair. One card to revisit. One explanation to understand. The whole palace does not have to be rebuilt today.\n\nThe magician’s clarity leaves room for kindness. Let both accompany you downstairs. Return to the room around you, and choose a useful next step or a deliberate rest.' },
  close: { title: 'The work can wait here', category: 'Scenario · closing the day', description: 'Continuity does not require carrying everything with you.', text: 'Pause at the Threshold. Imagine a small lamp and a place to leave one sentence. You can stop even when something remains open.\n\nName what you were working on. Then name where to begin next. Keep it concrete enough that tomorrow’s self will understand it.\n\nThe palace can hold that line. The shelf can hold the unfinished work. You do not need to rehearse it through the night to keep it safe.\n\nNotice one thing that is complete enough for today. Allow a little space around it.\n\nSet the tool down. Let the lamp dim in your imagination. Return to the actual room. The next beginning has a place.' }
};
const DAILY = [['morning', '☼', 'Morning'], ['afternoon', '◐', 'Afternoon'], ['night', '☾', 'Night']];
const SCEN = [['restart', 'When momentum is lost', 'A small, honest return.'], ['overwhelmed', 'When everything feels open', 'Narrow the Circle.'],
  ['disappointed', 'After a difficult result', 'Read the information with kindness.'], ['close', 'When it is time to stop', 'Set the work down safely.']];

const istHour = () => Number(new Intl.DateTimeFormat('en-GB', { timeZone: 'Asia/Kolkata', hour: 'numeric', hour12: false }).format(new Date()));
export const defaultSlot = () => { const h = istHour(); return h < 12 ? 'morning' : h < 18 ? 'afternoon' : 'night'; };

// one player for the whole app, so leaving the alcove always silences it
const M = { sel: null, state: 'idle', token: 0, voices: [], startedAt: 0, heard: 0, audio: null };
export function stopMeditation() {
  M.token++;
  if ('speechSynthesis' in window) speechSynthesis.cancel();
  if (M.audio) { M.audio.pause(); M.audio = null; }
  logListen();
  M.state = 'idle';
}
// a quiet record of listening (this device only); the Loft shows the last one
async function logListen() {
  if (!M.startedAt) return;
  const sec = Math.round((Date.now() - M.startedAt) / 1000) + M.heard;
  const track = M.playing; M.startedAt = 0; M.heard = 0;
  if (sec < 20) return;
  try { const l = (await db.kv.get('meditations')) || []; l.push({ ts: Date.now(), track, sec }); await db.kv.set('meditations', l.slice(-200)); } catch (e) { /* best effort */ }
}
export async function lastMeditation() { try { const l = (await db.kv.get('meditations')) || []; return l[l.length - 1] || null; } catch (e) { return null; } }

export function renderMeditation(app, { nav, back, P, recordings }) {
  if (!M.sel || !TRACKS[M.sel]) M.sel = defaultSlot();
  const recs = recordings || {};          // { morning: {url, title, text, date}, ... } once personal recordings exist
  app.innerHTML = `<div class="screen medit">
    <header class="top"><a class="iconbtn" href="${back}" aria-label="Back">${'<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>'}</a>
      <span class="tt"><span class="mono kick teal">THE LOFT · THE QUIET ALCOVE</span><span class="h1s">Return to your centre.</span></span><span></span></header>
    <div class="scroll pad med-body">
      <div class="med-player" id="mplayer">
        <div class="orb" aria-hidden="true"><svg viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1"><circle cx="12" cy="12" r="8.5" stroke-dasharray="1.2 3.1"/><circle cx="12" cy="12" r="1.5" fill="currentColor" stroke="none"/></svg></div>
        <div class="m-cat mono" id="mcat"></div>
        <h2 class="m-title" id="mtitle"></h2>
        <p class="m-desc" id="mdesc"></p>
        <div class="m-row"><button class="m-sm" id="mre" aria-label="Restart">↺</button><button class="m-play" id="mplay" aria-label="Play">▶</button><button class="m-sm" id="mstop" aria-label="Stop">■</button></div>
        <div class="m-status" id="mstat" role="status"></div>
        <div class="m-voice"><label for="mvoice">Voice</label><select id="mvoice"><option value="">Device default</option></select></div>
        <details class="m-tr"><summary>Read the guidance</summary><p id="mtext"></p></details>
      </div>
      <div class="med-lib">
        <span class="mono kick">THREE MOMENTS IN THE DAY</span>
        <div class="m-daily" role="tablist">${DAILY.map(([k, i, l]) => `<button role="tab" data-track="${k}"><span aria-hidden="true">${i}</span>${l}${recs[k] ? '<i class="m-new">yours</i>' : ''}</button>`).join('')}</div>
        <span class="mono kick">MEET THE MOMENT</span>
        <div class="m-scen">${SCEN.map(([k, t, s]) => `<button class="scen" data-track="${k}"><span><strong>${t}</strong><small>${s}</small></span><span class="gold">↗</span></button>`).join('')}</div>
        <p class="m-note">Sample guidance for now, spoken by this device’s voice. Later, three recordings each day — morning, afternoon, night — written from your actual work and kept here for offline listening.</p>
      </div>
    </div>
    ${nav}
  </div>`;
  const $ = s => app.querySelector(s);
  const track = () => recs[M.sel] ? { ...TRACKS[M.sel], ...recs[M.sel] } : TRACKS[M.sel];
  const ui = () => {
    const playing = M.state === 'playing';
    $('#mplay').textContent = playing ? 'Ⅱ' : '▶';
    $('#mplay').setAttribute('aria-label', playing ? 'Pause' : M.state === 'paused' ? 'Resume' : 'Play');
    $('#mplayer').classList.toggle('playing', playing);
  };
  const show = () => {
    const t = track();
    $('#mcat').textContent = t.category; $('#mtitle').textContent = t.title; $('#mdesc').textContent = t.description; $('#mtext').textContent = t.text;
    app.querySelectorAll('[data-track]').forEach(b => b.classList.toggle('on', b.dataset.track === M.sel));
    $('#mstat').textContent = t.url ? 'Your recording · plays offline' : 'Sample guidance · this device’s voice';
    ui();
  };
  const loadVoices = () => {
    if (!('speechSynthesis' in window)) return;
    M.voices = speechSynthesis.getVoices().filter(v => /^en/i.test(v.lang));
    const sel = $('#mvoice'); if (!sel) return;
    const want = P.get('medVoice', '');
    sel.innerHTML = '<option value="">Device default</option>' + M.voices.map(v => `<option value="${esc(v.voiceURI)}">${esc(v.name)} · ${esc(v.lang)}</option>`).join('');
    sel.value = M.voices.some(v => v.voiceURI === want) ? want : '';
  };
  const stop = () => { stopMeditation(); ui(); };
  const play = () => {
    const t = track();
    if (M.state === 'paused') {
      if (M.audio) M.audio.play(); else speechSynthesis.resume();
      M.state = 'playing'; M.startedAt = Date.now(); ui(); $('#mstat').textContent = 'Listening'; return;
    }
    if (M.state === 'playing') {
      if (M.audio) M.audio.pause(); else speechSynthesis.pause();
      M.heard += Math.round((Date.now() - M.startedAt) / 1000); M.startedAt = 0;
      M.state = 'paused'; ui(); $('#mstat').textContent = 'Paused. Resume whenever you are ready.'; return;
    }
    stopMeditation();
    const tok = M.token; M.playing = M.sel;
    if (t.url) {                                         // a stored recording
      M.audio = new Audio(t.url);
      M.audio.onended = () => { if (tok !== M.token) return; stopMeditation(); ui(); $('#mstat').textContent = 'Guidance complete. Return in your own time.'; };
      M.audio.play().catch(() => { $('#mstat').textContent = 'Tap ▶ again to play.'; M.state = 'idle'; ui(); });
    } else {
      if (!('speechSynthesis' in window)) { $('#mstat').textContent = 'No voice on this browser. Read the guidance below.'; $('.m-tr').open = true; return; }
      const u = new SpeechSynthesisUtterance(t.text);
      u.lang = 'en-IN'; u.rate = 0.82; u.pitch = 0.95;
      const v = M.voices.find(x => x.voiceURI === $('#mvoice').value); if (v) u.voice = v;
      u.onend = () => { if (tok !== M.token) return; stopMeditation(); ui(); const s = app.querySelector('#mstat'); if (s) s.textContent = 'Guidance complete. Return in your own time.'; };
      u.onerror = e => { if (tok !== M.token || e.error === 'canceled' || e.error === 'interrupted') return; M.state = 'idle'; ui(); $('#mstat').textContent = 'This voice could not play here. Choose another or read below.'; $('.m-tr').open = true; };
      speechSynthesis.speak(u);
    }
    M.state = 'playing'; M.startedAt = Date.now(); ui(); $('#mstat').textContent = 'Listening';
  };
  app.querySelectorAll('[data-track]').forEach(b => b.onclick = () => { stop(); M.sel = b.dataset.track; show(); play(); });
  $('#mplay').onclick = play; $('#mstop').onclick = () => { stop(); $('#mstat').textContent = 'Stopped.'; };
  $('#mre').onclick = () => { stop(); play(); };
  $('#mvoice').onchange = () => { P.set('medVoice', $('#mvoice').value); if (M.state !== 'idle') { stop(); play(); } };
  if ('speechSynthesis' in window) { loadVoices(); speechSynthesis.onvoiceschanged = loadVoices; }
  show();
}
