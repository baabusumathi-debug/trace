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
var VOICE_LANG = 'en-IN';
var VOICE_LIMIT_SEC_DEFAULT = 36000;            // 10 h of audio a month (well under the ₹3,500 alert)
var VOICE_PROMPT_DEFAULT = 'Read this as a calm, clear Indian-English critical care lecturer revising with a student. Moderate pace, natural pauses between items, every number and unit spoken fully and exactly.';

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
function synth_(text, voice, prompt) {
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

/**
 * op 'voice': { deck, voice, prompt?, items:[{ k, t, h }] }   k = part key (e.g. "VENT-10.a2"), t = text to speak,
 * h = hash of t chosen by the app (a changed text gets a new h, so it is made again). At most 12 items a call.
 * Items whose k already has the same h are skipped. Returns { made:[k], skipped:[k], failed:[{k,error}], used, limit }.
 */
function voice_(o) {
  var items = (o.items || []).slice(0, 12), voice = String(o.voice || 'Kore');
  if (!/^[A-Za-z]{2,20}$/.test(voice)) throw new Error('bad voice');
  var lock = LockService.getScriptLock(); lock.waitLock(30000);
  try {
    var dir = voiceDir_(o.deck), idxF = voiceIndexFile_(dir), idx = {};
    try { idx = JSON.parse(idxF.getBlob().getDataAsString('UTF-8') || '{}'); } catch (e) { idx = {}; }
    var u = voiceUsage_(), made = [], skipped = [], failed = [];
    for (var i = 0; i < items.length; i++) {
      var it = items[i], k = String(it.k || ''), t = String(it.t || ''), h = String(it.h || '');
      if (!/^[\w.\-]{1,60}$/.test(k) || !t.trim()) { failed.push({ k: k, error: 'bad item' }); continue; }
      if (idx[k] && idx[k].h === h && idx[k].voice === voice) { skipped.push(k); continue; }
      var sec = voiceSec_(t);
      if (u.used + sec > u.limit) { failed.push({ k: k, error: 'monthly voice limit reached' }); break; }
      try {
        var bytes = synth_(t, voice, o.prompt);
        var name = k + '.mp3', old = dir.getFilesByName(name);
        while (old.hasNext()) old.next().setTrashed(true);
        var f = dir.createFile(Utilities.newBlob(bytes, 'audio/mpeg', name));
        idx[k] = { id: f.getId(), h: h, sec: sec, voice: voice };
        u.used += sec; made.push(k);
      } catch (e) { failed.push({ k: k, error: String(e && e.message || e) }); if (/ 40[13]:/.test(String(e))) break; }
    }
    u.p.setProperty('VOICE_USED_SEC', String(u.used));
    idxF.setContent(JSON.stringify(idx));
    return { made: made, skipped: skipped, failed: failed, used: u.used, limit: u.limit, month: u.month };
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

/** Run from the editor (Run › makeSamples): the same card in five male voices, in Trace › voice › _samples. */
function makeSamples() {
  var t = 'What it is: driving pressure is plateau minus PEEP. It equals tidal volume divided by compliance: the stretch each breath puts on the open lung. Why it matters: in ARDS the open lung is small, so compliance tells you its size. Driving pressure scales the breath to that baby lung, not to body weight. What I do: keep it at or below fifteen centimetres of water, with a smaller tidal volume, or PEEP that recruits.';
  var prompt = 'Read this as a sharp, confident Indian-English critical care consultant revising high-yield points with a resident. Brisk revision pace, clear and crisp, short pauses only at full stops. Say PEEP as the word peep and ARDS as A R D S.';
  var out = ['Charon', 'Iapetus', 'Sadaltager', 'Schedar', 'Orus'].map(function (name) { return name + ': ' + JSON.stringify(voice_({ deck: '_samples', voice: name, prompt: prompt, items: [{ k: 'dp-' + name.toLowerCase(), t: t, h: 'v1' }] })); });
  Logger.log(out.join('\n'));
}
