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
  Chunks: 'r',
  Decks: 'r',
  Signals: 'r'
};
var VERSION = 1;

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

function out_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

/** Run this once from the editor (▶ Run › authorise) to grant access before deploying. */
function authorise() {
  DriveApp.getFolderById(TRACE_FOLDER_ID).getName();
  SpreadsheetApp.openById(SHEET_ID).getName();
}
