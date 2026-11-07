/**
 * Trace backend — a small private bridge between the Trace app and your Google Drive / War Map Sheet.
 * Paste this whole file into a new Apps Script project, then Deploy › New deployment › Web app:
 *   Execute as: Me    ·    Who has access: Anyone
 * Only requests carrying the KEY below are answered. It can only read and write inside the
 * "Trace" folder, and only touch the Sheet tabs listed in TABS.
 */
var KEY = '__TRACE_KEY__';
var TRACE_FOLDER_ID = '1e_lx6kl_MhG4aOracgTr_HG3NUp7OsYs';
var SHEET_ID = '150OxumS0XPBlPfmiNP9HLxwPrjUGEzbmmIBknvNJssk';
var TABS = {            // what the app may do with each tab
  TraceEvents: 'rw',
  Log: 'ra',            // read + append only
  Targets: 'rau',       // today's target, shared with the War Map: read, append, update status
  Chunks: 'r',
  Decks: 'r',
  Signals: 'r'
};
var VERSION = 7;          // 7: lessons (voice align, word timings) · 3: visual decks (visualIndex, readBinary) · 4: notifyJournal (test only, off by default) · 5: calendar reminders (5.1: HT events carry no owner reminder) · 6: card voice (Voice.gs)

function doGet() {
  return out_({ ok: true, app: 'trace-backend', version: VERSION });
}

function doPost(e) {
  var req;
  try { req = JSON.parse(e.postData.contents); } catch (err) { return out_({ ok: false, error: 'bad json' }); }
  if (!req || req.key !== KEY) return out_({ ok: false, error: 'not allowed' });
  try {
    if (req.op === 'batch') {
      return out_({ ok: true, results: (req.ops || []).map(function (o) {
        try { return { ok: true, data: run_(o) }; } catch (err) { return { ok: false, error: String(err && err.message || err) }; }
      }) });
    }
    return out_({ ok: true, data: run_(req) });
  } catch (err) {
    return out_({ ok: false, error: String(err && err.message || err) });
  }
}

function run_(o) {
  switch (o.op) {
    case 'ping': return { version: VERSION, user: Session.getEffectiveUser().getEmail(), time: new Date().toISOString() };
    case 'readFile': return readFile_(o.id);
    case 'listFolder': return listFolder_(o.id);
    case 'findFile': return findFile_(o.folderId, o.name);
    case 'writeFile': return writeFile_(o.folderId, o.name, o.text, o.mime);
    case 'sheetRead': return sheetRead_(o.tab, o.fromRow);
    case 'sheetAppend': return sheetAppend_(o.tab, o.rows, o.header, o.dedupe);
    case 'sheetUpdate': return sheetUpdate_(o.tab, o.keyCol, o.key, o.set);
    case 'visualIndex': return visualIndex_();
    case 'readBinary': return readBinary_(o.id);
    case 'notifyJournal': return notifyJournal_(o.requestId);
    case 'calendar': return calendar_(o);
    case 'voice': return voice_(o);              // v6: card voice (Voice.gs)
    case 'voiceIndex': return voiceIndex_(o);
    case 'voiceUsage': return voiceUsageOp_();
    case 'voiceAlign': return voiceAlign_(o);    // v7: word timings for lesson read-along
    case 'voiceReindex': return voiceReindex_(o);
    default: throw new Error('unknown op ' + o.op);
  }
}

/* ---------- Drive ---------- */
function insideTrace_(file) {
  var seen = 0, queue = [];
  var p = file.getParents();
  while (p.hasNext()) queue.push(p.next());
  while (queue.length && seen < 40) {
    var f = queue.shift(); seen++;
    if (f.getId() === TRACE_FOLDER_ID) return true;
    var pp = f.getParents();
    while (pp.hasNext()) queue.push(pp.next());
  }
  return false;
}
function folder_(id) {
  var f = DriveApp.getFolderById(id);
  if (id !== TRACE_FOLDER_ID && !insideTrace_(f)) throw new Error('folder outside Trace');
  return f;
}
function readFile_(id) {
  var f = DriveApp.getFileById(id);
  if (!insideTrace_(f)) throw new Error('file outside Trace');
  return { id: id, name: f.getName(), modified: f.getLastUpdated().toISOString(), size: f.getSize(),
           text: f.getBlob().getDataAsString('UTF-8') };
}
function listFolder_(id) {
  var dir = folder_(id), outp = [];
  var fs = dir.getFiles();
  while (fs.hasNext()) { var f = fs.next(); if (f.isTrashed()) continue; outp.push({ id: f.getId(), name: f.getName(), kind: 'file', mime: f.getMimeType(), size: f.getSize(), modified: f.getLastUpdated().toISOString() }); }
  var ds = dir.getFolders();
  while (ds.hasNext()) { var d = ds.next(); outp.push({ id: d.getId(), name: d.getName(), kind: 'folder', modified: d.getLastUpdated().toISOString() }); }
  return outp;
}
function findFile_(folderId, name) {
  // newest non-trashed file with this name (Drive keeps trashed files in folder listings)
  var it = folder_(folderId).getFilesByName(name), best = null;
  while (it.hasNext()) {
    var f = it.next();
    if (f.isTrashed()) continue;
    if (!best || f.getLastUpdated() > best.getLastUpdated()) best = f;
  }
  if (!best) return null;
  return { id: best.getId(), name: best.getName(), modified: best.getLastUpdated().toISOString(), size: best.getSize() };
}
function writeFile_(folderId, name, text, mime) {
  if (!/^[\w .\-]{1,80}$/.test(name)) throw new Error('bad file name');
  var lock = LockService.getScriptLock(); lock.waitLock(20000);
  try {
    var dir = folder_(folderId), it = dir.getFilesByName(name);
    while (it.hasNext()) { var f = it.next(); if (f.isTrashed()) continue; f.setContent(text); return { id: f.getId(), updated: true }; }
    var nf = dir.createFile(name, text, mime || 'text/plain');
    return { id: nf.getId(), created: true };
  } finally { lock.releaseLock(); }
}

/* ---------- visual decks: Trace › decks › <DECK> › visual › {current.json, images/, versions/v<N>/} ---------- */
function filesOf_(dir) {
  var out = [], it = dir.getFiles();
  while (it.hasNext()) { var f = it.next(); if (f.isTrashed()) continue; out.push({ id: f.getId(), name: f.getName(), size: f.getSize(), modified: f.getLastUpdated().toISOString() }); }
  return out;
}
function sub_(dir, name) { var it = dir.getFoldersByName(name); while (it.hasNext()) { var d = it.next(); if (!d.isTrashed()) return d; } return null; }
function visualIndex_() {
  var out = [], it = DriveApp.searchFolders("title = 'visual' and trashed = false");
  while (it.hasNext()) {
    var v = it.next();
    if (!insideTrace_(v)) continue;
    var deckDir = v.getParents().hasNext() ? v.getParents().next() : null;
    if (!deckDir) continue;
    var row = { deck: deckDir.getName(), visualId: v.getId() };
    try {
      var cur = null, cf = v.getFilesByName('current.json');
      while (cf.hasNext()) { var f = cf.next(); if (!f.isTrashed() && (!cur || f.getLastUpdated() > cur.getLastUpdated())) cur = f; }
      if (!cur) { row.error = 'no current.json'; out.push(row); continue; }
      row.current = cur.getBlob().getDataAsString('UTF-8');
      var c = JSON.parse(row.current), vers = sub_(v, 'versions'), imgs = sub_(v, 'images');
      var vd = vers && sub_(vers, 'v' + c.live_version);
      if (!vd) { row.error = 'versions/v' + c.live_version + ' not found'; out.push(row); continue; }
      row.files = filesOf_(vd);
      row.images = imgs ? filesOf_(imgs) : [];
    } catch (err) { row.error = String(err && err.message || err); }
    out.push(row);
  }
  return out;
}
function readBinary_(id) {
  var f = DriveApp.getFileById(id);
  if (!insideTrace_(f)) throw new Error('file outside Trace');
  if (f.getSize() > 8 * 1024 * 1024) throw new Error('file too large');
  var b = f.getBlob();
  return { id: id, name: f.getName(), mime: b.getContentType(), size: f.getSize(), b64: Utilities.base64Encode(b.getBytes()) };
}

/* ---------- Sheet ---------- */
function tab_(name, need) {
  var mode = TABS[name];
  if (!mode || mode.indexOf(need) < 0) throw new Error('tab not allowed: ' + name);
  return SpreadsheetApp.openById(SHEET_ID).getSheetByName(name);
}
function sheetRead_(tab, fromRow) {
  var sh = tab_(tab, 'r');
  if (!sh) return { values: [], lastRow: 0 };
  var last = sh.getLastRow(), cols = sh.getLastColumn(), start = Math.max(1, fromRow || 1);
  if (last < start || cols < 1) return { values: [], lastRow: last };
  return { values: sh.getRange(start, 1, last - start + 1, cols).getDisplayValues(), lastRow: last };
}
/** dedupe = { col: <0-based column>, contains: <bool>, keys: [one key per row] } — rows whose key already appears in that column are skipped */
function sheetAppend_(tab, rows, header, dedupe) {
  if (!rows || !rows.length) return { appended: 0 };
  var mode = TABS[tab];
  if (!mode || (mode.indexOf('a') < 0 && mode.indexOf('w') < 0)) throw new Error('tab not writable: ' + tab);
  var lock = LockService.getScriptLock(); lock.waitLock(20000);
  try {
    var ss = SpreadsheetApp.openById(SHEET_ID), sh = ss.getSheetByName(tab);
    if (!sh) {
      if (mode.indexOf('w') < 0 || !header) throw new Error('tab missing: ' + tab);
      sh = ss.insertSheet(tab); sh.appendRow(header); sh.setFrozenRows(1);
    }
    var todo = rows;
    if (dedupe && sh.getLastRow() > 1) {
      var have = sh.getRange(2, dedupe.col + 1, sh.getLastRow() - 1, 1).getDisplayValues().map(function (r) { return r[0]; });
      todo = rows.filter(function (r, idx) {
        var k = String(dedupe.keys ? dedupe.keys[idx] : r[dedupe.col]);
        if (!dedupe.contains) return have.indexOf(k) < 0;
        for (var i = 0; i < have.length; i++) if (have[i].indexOf(k) >= 0) return false;
        return true;
      });
    }
    if (todo.length) {
      var width = Math.max.apply(null, todo.map(function (r) { return r.length; }));
      todo = todo.map(function (r) { var c = r.slice(); while (c.length < width) c.push(''); return c; });
      sh.getRange(sh.getLastRow() + 1, 1, todo.length, width).setValues(todo);
    }
    return { appended: todo.length, skipped: rows.length - todo.length };
  } finally { lock.releaseLock(); }
}

/** set = { <0-based column>: value } on the row whose keyCol equals key */
function sheetUpdate_(tab, keyCol, key, set) {
  var mode = TABS[tab];
  if (!mode || mode.indexOf('u') < 0) throw new Error('tab not updatable: ' + tab);
  var lock = LockService.getScriptLock(); lock.waitLock(20000);
  try {
    var sh = SpreadsheetApp.openById(SHEET_ID).getSheetByName(tab);
    if (!sh || sh.getLastRow() < 2) return { updated: 0 };
    var keys = sh.getRange(2, keyCol + 1, sh.getLastRow() - 1, 1).getDisplayValues();
    for (var i = 0; i < keys.length; i++) {
      if (keys[i][0] === String(key)) {
        Object.keys(set || {}).forEach(function (c) { sh.getRange(i + 2, Number(c) + 1).setValue(set[c]); });
        return { updated: 1 };
      }
    }
    return { updated: 0 };
  } finally { lock.releaseLock(); }
}

function out_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

/** Run this once from the editor (▶ Run › authorise) to grant access before deploying. */
function authorise() {
  DriveApp.getFolderById(TRACE_FOLDER_ID).getName();
  SpreadsheetApp.openById(SHEET_ID).getName();
}

/* ---------- v4: notify Journal about one TEST flow-message request (off unless JOURNAL_ENABLED=true) ---------- */
function notifyJournal_(id) {
  var p = PropertiesService.getScriptProperties();
  if (p.getProperty('JOURNAL_ENABLED') !== 'true') return { sent: false, reason: 'disabled' };
  if (!/^fm-\d{8}-\d{6}-[a-z0-9]{6}$/.test(String(id || ''))) return { sent: false, reason: 'bad requestId' };
  var url = p.getProperty('JOURNAL_WEBHOOK_URL') || '', key = p.getProperty('JOURNAL_WEBHOOK_KEY') || '';
  if (!/^https:\/\/\S+$/.test(url) || !key) return { sent: false, reason: 'not configured' };
  if (/^bearer\s/i.test(key) || /\s/.test(key)) return { sent: false, reason: 'key must be the raw token only' };
  // TEST allowlist: an existing, matching, unexpired test request in Trace › flowmsg
  var dir = sub_(DriveApp.getFolderById(TRACE_FOLDER_ID), 'flowmsg');
  if (!dir) return { sent: false, reason: 'no flowmsg folder' };
  var f = findFile_(dir.getId(), 'req-' + id + '.json');
  if (!f) return { sent: false, reason: 'no such request' };
  var req;
  try { req = JSON.parse(DriveApp.getFileById(f.id).getBlob().getDataAsString('UTF-8')); } catch (e) { return { sent: false, reason: 'request unreadable' }; }
  if (!req || req.type !== 'trace.flowmsg.request' || req.requestId !== id || req.test !== true) return { sent: false, reason: 'not a matching test request' };
  var exp = Date.parse(req.expires);
  if (!(exp > Date.now())) return { sent: false, reason: 'expired' };
  // once per requestId (6 h), at most one notification per 60 s
  var cache = CacheService.getScriptCache(), lock = LockService.getScriptLock();
  if (!lock.tryLock(5000)) return { sent: false, reason: 'busy' };
  try {
    if (cache.get('fm_' + id)) return { sent: false, reason: 'duplicate' };
    if (Date.now() - Number(p.getProperty('JOURNAL_LAST_SENT') || 0) < 60000) return { sent: false, reason: 'rate-limited' };
    p.setProperty('JOURNAL_LAST_SENT', String(Date.now()));
    cache.put('fm_' + id, '1', 21600);
  } finally { lock.releaseLock(); }
  try {
    var res = UrlFetchApp.fetch(url, {
      method: 'post', contentType: 'application/json',
      headers: { Authorization: 'Bearer ' + key },
      payload: JSON.stringify({ requestId: id, test: true }),
      muteHttpExceptions: true, followRedirects: false
    });
    return { sent: true, status: res.getResponseCode() };    // no body, URL or key is ever returned or logged
  } catch (e) { return { sent: false, reason: 'network' }; }
}

/** v4: run this once from the editor (Run › authoriseJournal) to grant "Connect to an external service".
 *  getRequest() only builds a request object; nothing is sent and no secret is read. */
function authoriseJournal() {
  UrlFetchApp.getRequest('https://example.com/');
  return 'external-service permission is granted';
}

/* ---------- v5: break and start-of-day reminders, only in two calendars of their own ---------- */
// "Trace" holds Naven's reminders; "Trace · HT" holds HT's (Naven shares that one calendar with her).
// The app can only add or remove short events in these two calendars; it never reads or touches any other calendar.
var CAL_NAMES = { Trace: 'Trace', HT: 'Trace · HT' };
function cal_(who) {
  var name = CAL_NAMES[who === 'HT' ? 'HT' : 'Trace'];
  var list = CalendarApp.getOwnedCalendarsByName(name);
  if (list.length) return list[0];
  return CalendarApp.createCalendar(name, { summary: 'Reminders from the Trace study app only' });
}
function calendar_(o) {
  var c = cal_(o.who);
  if (o.action === 'add') {
    var at = new Date(o.at);
    if (isNaN(at.getTime())) throw new Error('bad time');
    var ev = c.createEvent(String(o.title || 'Trace').slice(0, 80), at, new Date(at.getTime() + 5 * 60000), { description: String(o.note || '').slice(0, 300) });
    ev.removeAllReminders();
    if (o.who !== 'HT') ev.addPopupReminder(0);   // HT's ring comes from her own calendar setting, not the owner's (v5.1)
    return { id: ev.getId(), calendar: c.getName() };
  }
  if (o.action === 'remove') {
    var e = o.id ? c.getEventById(String(o.id)) : null;
    if (e) e.deleteEvent();
    return { removed: !!e };
  }
  throw new Error('unknown calendar action');
}
/** v5: run this once from the editor (Run › authoriseCalendar) to grant Calendar access and create the two calendars. */
function authoriseCalendar() {
  return 'Calendar access granted · ready: ' + cal_('Trace').getName() + ', ' + cal_('HT').getName();
}
