/**
 * Trace backend v6 — card voice (Gemini voices through Google Cloud Text-to-Speech).
 * Lives beside Code.gs in the same Apps Script project. Needs:
 *   - the project linked to the Google Cloud project that has Cloud Text-to-Speech enabled
 *     (Project Settings › Google Cloud Platform project › Change project), and
 *   - the cloud-platform scope in appsscript.json (see backend/appsscript.json in the repo).
 * No API key: the call runs under the owner's own Google sign-in (ScriptApp.getOAuthToken()).
 *
 * Audio is saved as MP3 in Trace › voice › <DECK> (samples in Trace › voice › _samples), one file per
 * point of a card, with an index.json per deck: { "<part key>": { "id", "h", "sec", "voice" } }.
 * A hard monthly limit (VOICE_LIMIT_SEC, default 10 hours of audio) stops generation before the
 * credit can run out; Google cannot cap Text-to-Speech spending itself.
 */
var VOICE_PROJECT = 'trace-voice-514011';
var VOICE_MODEL = 'gemini-2.5-flash-tts';
var VOICE_LANG = 'en-US';            // Naven, 7 Nov: the accent Claude speaks with, not Indian English
var VOICE_LIMIT_SEC_DEFAULT = 36000;            // 10 h of audio a month (well under the ₹3,500 alert)
var VOICE_PROMPT_DEFAULT = 'Read this as a sharp, confident critical care consultant revising high-yield points with a resident. Neutral American English accent. Brisk revision pace, clear and crisp, short pauses only at full stops.';

// estimated seconds of speech for a text (about 8 characters a second, measured on the first clip); used for the monthly limit
function voiceSec_(t) { return Math.max(1, Math.round(String(t).length / 8)); }
function voiceUsage_() {
  var p = PropertiesService.getScriptProperties(), m = Utilities.formatDate(new Date(), 'Asia/Kolkata', 'yyyy-MM');
  if (p.getProperty('VOICE_MONTH') !== m) { p.setProperty('VOICE_MONTH', m); p.setProperty('VOICE_USED_SEC', '0'); }
  return { p: p, month: m, used: Number(p.getProperty('VOICE_USED_SEC') || 0), limit: Number(p.getProperty('VOICE_LIMIT_SEC') || VOICE_LIMIT_SEC_DEFAULT) };
}
function voiceDir_(deck) {
  var root = DriveApp.getFolderById(TRACE_FOLDER_ID);
  var v = sub_(root, 'voice') || root.createFolder('voice');
  var name = deck === '_samples' ? '_samples' : String(deck || '');
  if (name !== '_samples' && !/^[A-Z0-9\-]{2,20}$/.test(name)) throw new Error('bad deck');
  return sub_(v, name) || v.createFolder(name);
}
function voiceIndexFile_(dir) {
  var it = dir.getFilesByName('index.json');
  while (it.hasNext()) { var f = it.next(); if (!f.isTrashed()) return f; }
  return dir.createFile('index.json', '{}', 'application/json');
}
// OpenAI voices are named "oa-<voice>" (e.g. oa-cedar). Key: Script Property OPENAI_KEY (set by Naven; never in the repo).
var OA_MODEL = 'gpt-4o-mini-tts';
function synthOpenAI_(text, voice, prompt) {
  var key = PropertiesService.getScriptProperties().getProperty('OPENAI_KEY');
  if (!key) throw new Error('speech 401: OPENAI_KEY is not set in Script Properties');
  var res = UrlFetchApp.fetch('https://api.openai.com/v1/audio/speech', {
    method: 'post', contentType: 'application/json', muteHttpExceptions: true,
    headers: { Authorization: 'Bearer ' + key },
    payload: JSON.stringify({ model: OA_MODEL, voice: voice, input: String(text).slice(0, 3800), instructions: String(prompt || VOICE_PROMPT_DEFAULT).slice(0, 1500), response_format: 'mp3' })
  });
  var code = res.getResponseCode();
  if (code !== 200) { var msg = res.getContentText(); try { msg = JSON.parse(msg).error.message; } catch (e) { /* raw */ } throw new Error('speech ' + code + ': ' + String(msg).slice(0, 300)); }
  return res.getBlob().getBytes();
}
function synth_(text, voice, prompt) {
  if (/^oa-/.test(voice)) return synthOpenAI_(text, voice.slice(3), prompt);
  var res = UrlFetchApp.fetch('https://texttospeech.googleapis.com/v1/text:synthesize', {
    method: 'post', contentType: 'application/json', muteHttpExceptions: true,
    headers: { Authorization: 'Bearer ' + ScriptApp.getOAuthToken(), 'x-goog-user-project': VOICE_PROJECT },
    payload: JSON.stringify({
      input: { prompt: String(prompt || VOICE_PROMPT_DEFAULT).slice(0, 1500), text: String(text).slice(0, 3800) },
      voice: { languageCode: VOICE_LANG, name: voice, modelName: VOICE_MODEL },
      audioConfig: { audioEncoding: 'MP3' }
    })
  });
  var code = res.getResponseCode(), body = res.getContentText();
  if (code !== 200) { var msg = body; try { msg = JSON.parse(body).error.message; } catch (e) { /* raw */ } throw new Error('speech ' + code + ': ' + String(msg).slice(0, 300)); }
  return Utilities.base64Decode(JSON.parse(body).audioContent);
}

// Word timings (lessons read-along): OpenAI Whisper with word timestamps, run once per clip, saved as <k>.t.json beside it.
// The app matches Whisper's words to the script's words itself, so this file holds Whisper's raw words: { words: [[w, start, end]] }.
function alignWords_(bytes, text) {
  var key = PropertiesService.getScriptProperties().getProperty('OPENAI_KEY');
  if (!key) throw new Error('align 401: OPENAI_KEY is not set');
  var res = UrlFetchApp.fetch('https://api.openai.com/v1/audio/transcriptions', {
    method: 'post', muteHttpExceptions: true, headers: { Authorization: 'Bearer ' + key },
    payload: { file: Utilities.newBlob(bytes, 'audio/mpeg', 'clip.mp3'), model: 'whisper-1', response_format: 'verbose_json',
      'timestamp_granularities[]': 'word', language: 'en', prompt: String(text || '').slice(0, 800) }
  });
  var code = res.getResponseCode();
  if (code !== 200) { var msg = res.getContentText(); try { msg = JSON.parse(msg).error.message; } catch (e) { /* raw */ } throw new Error('align ' + code + ': ' + String(msg).slice(0, 200)); }
  var r = JSON.parse(res.getContentText());
  return { words: (r.words || []).map(function (w) { return [w.word, Math.round(w.start * 1000), Math.round(w.end * 1000)]; }), dur: Math.round((r.duration || 0) * 1000) };
}
function saveAlign_(dir, k, bytes, text, al) {
  var t = al || alignWords_(bytes, text), name = k + '.t.json', old = dir.getFilesByName(name);
  while (old.hasNext()) old.next().setTrashed(true);
  return dir.createFile(name, JSON.stringify(t), 'application/json').getId();
}
// Gemini sometimes runs on after the text (repeats it, or keeps talking). Whisper's word count against the script's shows it:
// 0 = clean; 0.5 = half as many extra words again. Clips above RUNON_MAX are made again (at most 3 tries; the best one is kept).
var RUNON_MAX = 0.2;
function runOn_(text, al) {
  var n = String(text).split(/\s+/).filter(String).length, w = (al.words || []).length;
  return Math.max(0, (w - n) / Math.max(n, 1));
}

/**
 * op 'voice': { deck, voice, prompt?, items:[{ k, t, h }] }   k = part key (e.g. "VENT-10.a2"), t = text to speak,
 * h = hash of t chosen by the app (a changed text gets a new h, so it is made again). At most 12 items a call.
 * Items whose k already has the same h are skipped. Returns { made:[k], skipped:[k], failed:[{k,error}], used, limit }.
 */
function voice_(o) {
  var items = (o.items || []).slice(0, 12), voice = String(o.voice || 'Kore');
  if (!/^(oa-)?[A-Za-z]{2,20}$/.test(voice)) throw new Error('bad voice');
  // the slow part (speech + timings) runs without the lock, so several calls can work at once; the lock is held only to
  // merge this call's results into the index and the monthly count
  var dir = voiceDir_(o.deck), idxF = voiceIndexFile_(dir), idx = {};
  try { idx = JSON.parse(idxF.getBlob().getDataAsString('UTF-8') || '{}'); } catch (e) { idx = {}; }
  var u = voiceUsage_(), made = [], skipped = [], failed = [], add = {}, spent = 0;
  for (var i = 0; i < items.length; i++) {
    var it = items[i], k = String(it.k || ''), t = String(it.t || ''), h = String(it.h || '');
    if (!/^[\w.\-]{1,60}$/.test(k) || !t.trim()) { failed.push({ k: k, error: 'bad item' }); continue; }
    if (!o.redo && idx[k] && idx[k].h === h && idx[k].voice === voice) { skipped.push(k); continue; }   // redo: make it again (a run-on clip)
    var sec = voiceSec_(t);
    if (u.used + spent + sec * (o.align ? 3 : 1) > u.limit) { failed.push({ k: k, error: 'monthly voice limit reached' }); break; }
    try {
      var bytes = null, al = null, aerr = '', tries = 0, ro = 0;
      for (var a = 0; a < (o.align ? 3 : 1); a++) {
        var b = synth_(t, voice, o.prompt); tries++; spent += sec;
        if (!o.align) { bytes = b; break; }
        var x = null; try { x = alignWords_(b, t); } catch (e) { aerr = String(e && e.message || e).slice(0, 120); bytes = b; break; }
        var r = runOn_(t, x);
        if (!bytes || r < ro) { bytes = b; al = x; ro = r; }
        if (r <= RUNON_MAX) break;
      }
      var name = k + '.mp3', old = dir.getFilesByName(name);
      while (old.hasNext()) old.next().setTrashed(true);
      var f = dir.createFile(Utilities.newBlob(bytes, 'audio/mpeg', name));
      var e2 = { id: f.getId(), h: h, sec: sec, voice: voice, tries: tries };
      if (al) { e2.tid = saveAlign_(dir, k, bytes, t, al); e2.ro = Math.round(ro * 100) / 100; }
      if (aerr) e2.aerr = aerr;
      try { f.setDescription(JSON.stringify(e2)); } catch (e) { /* the index still has it */ }
      add[k] = e2; made.push(k);
    } catch (e) { failed.push({ k: k, error: String(e && e.message || e) }); if (/ 40[13]:/.test(String(e))) break; }
  }
  var lock = LockService.getScriptLock(); lock.waitLock(60000);
  try {
    var cur = {}; try { cur = JSON.parse(idxF.getBlob().getDataAsString('UTF-8') || '{}'); } catch (e) { cur = {}; }
    for (var kk in add) cur[kk] = add[kk];
    idxF.setContent(JSON.stringify(cur));
    var u2 = voiceUsage_(); u2.p.setProperty('VOICE_USED_SEC', String(u2.used + spent));
    return { made: made, skipped: skipped, failed: failed, used: u2.used + spent, limit: u2.limit, month: u2.month };
  } finally { lock.releaseLock(); }
}
/** op 'voiceAlign': { deck, keys:[k] } → word timings for clips already made (at most 12 a call); { done:[k], failed:[{k,error}] }. */
function voiceAlign_(o) {
  var keys = (o.keys || []).slice(0, 12), texts = o.texts || {};
  var lock = LockService.getScriptLock(); lock.waitLock(30000);
  try {
    var dir = voiceDir_(o.deck), idxF = voiceIndexFile_(dir), idx = {}, done = [], failed = [];
    try { idx = JSON.parse(idxF.getBlob().getDataAsString('UTF-8') || '{}'); } catch (e) { idx = {}; }
    for (var i = 0; i < keys.length; i++) {
      var k = String(keys[i]), e = idx[k];
      if (!e) { failed.push({ k: k, error: 'no clip' }); continue; }
      try { e.tid = saveAlign_(dir, k, DriveApp.getFileById(e.id).getBlob().getBytes(), texts[k]); delete e.aerr; done.push(k); }
      catch (x) { failed.push({ k: k, error: String(x && x.message || x) }); if (/ 40[13]:| 429:/.test(String(x))) break; }
    }
    idxF.setContent(JSON.stringify(idx));
    return { done: done, failed: failed };
  } finally { lock.releaseLock(); }
}
/** op 'voiceReindex': { deck } → puts back index entries another call's save overwrote (Drive can hand a parallel call a
 *  stale index). Each clip carries its own entry in its file description; the newest file per key wins. Returns { added }. */
function voiceReindex_(o) {
  var dir = voiceDir_(o.deck), idxF = voiceIndexFile_(dir), best = {}, it = dir.getFiles();
  while (it.hasNext()) {
    var f = it.next(), n = f.getName(); if (!/\.mp3$/.test(n) || f.isTrashed()) continue;
    var d = f.getDescription(); if (!d) continue;
    var e; try { e = JSON.parse(d); } catch (x) { continue; }
    var k = n.slice(0, -4), tm = f.getLastUpdated().getTime();
    if (!best[k] || best[k].tm < tm) best[k] = { e: e, tm: tm };
  }
  var lock = LockService.getScriptLock(); lock.waitLock(60000);
  try {
    var idx = {}; try { idx = JSON.parse(idxF.getBlob().getDataAsString('UTF-8') || '{}'); } catch (x) { idx = {}; }
    var added = 0;
    for (var k2 in best) if (!idx[k2] || idx[k2].id !== best[k2].e.id) { idx[k2] = best[k2].e; added++; }
    if (added) idxF.setContent(JSON.stringify(idx));
    return { added: added };
  } finally { lock.releaseLock(); }
}
/** op 'voiceIndex': { deck } → the deck's index (part key → file id, hash, seconds, voice). */
function voiceIndex_(o) {
  var dir = voiceDir_(o.deck), it = dir.getFilesByName('index.json');
  while (it.hasNext()) { var f = it.next(); if (!f.isTrashed()) { try { return JSON.parse(f.getBlob().getDataAsString('UTF-8') || '{}'); } catch (e) { return {}; } } }
  return {};
}
/** op 'voiceUsage': this month's audio seconds made and the limit. */
function voiceUsageOp_() { var u = voiceUsage_(); return { used: u.used, limit: u.limit, month: u.month }; }

/** Run once from the editor (Run › authoriseVoice) after switching the Cloud project: it grants the new permission
 *  and makes one short test clip in Trace › voice › _samples. */
function authoriseVoice() {
  var r = voice_({ deck: '_samples', voice: 'Kore', items: [{ k: 'hello', t: 'Trace voice is ready. Positive end-expiratory pressure, PEEP, of eight centimetres of water.', h: 'v1' }] });
  Logger.log(JSON.stringify(r));
  return JSON.stringify(r);
}

/** Run from the editor (Run › makeSamples): the same card in the voices being compared, in Trace › voice › _samples. */
var VOICE_PROMPT_CALM = 'Speak as a calm, composed critical care consultant teaching one resident at the bedside. Neutral American English accent. Unhurried, measured pace, a little slower than normal conversation. Enunciate every word and every medical term clearly, and say numbers and units in full. Pause briefly after each sentence and after each colon. Warm and authoritative, never rushed.';
function makeSamples() {
  var t = 'What it is: driving pressure is plateau minus PEEP. It equals tidal volume divided by compliance: the stretch each breath puts on the open lung. Why it matters: in ARDS the open lung is small, so compliance tells you its size. Driving pressure scales the breath to that baby lung, not to body weight. What I do: keep it at or below fifteen centimetres of water, with a smaller tidal volume, or PEEP that recruits.';
  var out = ['oa-cedar', 'oa-onyx'].map(function (name) { return name + ': ' + JSON.stringify(voice_({ deck: '_samples', voice: name, prompt: VOICE_PROMPT_CALM, items: [{ k: 'dp-' + name.toLowerCase() + '-calm', t: t.replace(/PEEP/g, 'peep').replace(/ARDS/g, 'A R D S'), h: 'calm1' }] })); });
  Logger.log(out.join('\n'));
}

/** Run from the editor (Run › testAlign): word timings for the Iapetus sample, logged. */
function testAlign() {
  var r = voiceAlign_({ deck: '_samples', keys: ['dp-iapetus-us'] });
  var e = voiceIndex_({ deck: '_samples' })['dp-iapetus-us'];
  Logger.log(JSON.stringify(r) + '\n' + (e && e.tid ? DriveApp.getFileById(e.tid).getBlob().getDataAsString().slice(0, 600) : 'no timings'));
}
