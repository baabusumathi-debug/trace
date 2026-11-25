// Notes storage: the tablet first, then a copy in Drive through the Trace backend.
// Nothing waits on the network; the local write happens at once and the upload follows.
import { db, peekDb } from '../../js/db.js';

const TRACE_FOLDER = '1e_lx6kl_MhG4aOracgTr_HG3NUp7OsYs';
let conn = null, connTried = false;
const listeners = new Set();
let state = 'local';                       // local | saving | saved | offline | nobackend
export const onState = fn => { listeners.add(fn); fn(state); };
const setState = s => { state = s; listeners.forEach(f => f(s)); };
export const syncState = () => state;

async function backend() {
  if (connTried) return conn;
  connTried = true;
  try { conn = await peekDb('trace', 'kv', 'backend'); } catch (e) { conn = null; }
  if (!conn || !conn.url || !conn.key) { conn = null; setState('nobackend'); }
  return conn;
}
async function call(op, timeoutMs = 25000) {
  const c = await backend(); if (!c) throw new Error('no backend');
  const ctl = new AbortController(), t = setTimeout(() => ctl.abort(), timeoutMs);
  try {
    const res = await fetch(c.url, {
      method: 'POST', headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify({ key: c.key, op: 'batch', ops: [op] }), redirect: 'follow', signal: ctl.signal
    });
    if (!res.ok) throw new Error('HTTP ' + res.status);
    const j = await res.json();
    if (!j.ok) throw new Error(j.error || 'backend error');
    const r = j.results[0];
    if (!r.ok) throw new Error(r.error);
    return r.data;
  } finally { clearTimeout(t); }
}

export async function localGet(key) { try { return await db.kv.get(key); } catch (e) { return null; } }
export async function localSet(key, val) { try { await db.kv.set(key, val); } catch (e) { /* private mode */ } }

// file names in the Trace folder: the notebook, and the marks written on the study screens
export const NOTES_FILE = page => 'studynotes-' + page + '.json';
export const INK_FILE = page => 'studyink-' + page + '.json';
export const markSynced = () => { if (state === 'local') setState('saved'); };

export async function cloudGet(file) {
  const f = await call({ op: 'findFile', folderId: TRACE_FOLDER, name: file });
  if (!f || !f.id) return null;
  const r = await call({ op: 'readFile', id: f.id });
  const text = typeof r === 'string' ? r : (r && (r.text || r.content)) || '';
  try { return JSON.parse(text); } catch (e) { return null; }
}
export async function cloudPut(file, data) {
  await call({ op: 'writeFile', folderId: TRACE_FOLDER, name: file, text: JSON.stringify(data), mime: 'application/json' });
}

// one writer per record: local straight away, Drive a few seconds later
export function makeSaver(key, file, read) {
  let localT = 0, cloudT = 0, busy = false, again = false, dirty = false;
  const toLocal = () => { clearTimeout(localT); localT = setTimeout(async () => { await localSet(key, read()); }, 250); };
  const toCloud = () => {
    clearTimeout(cloudT);
    cloudT = setTimeout(async () => {
      if (busy) { again = true; return; }
      busy = true; setState('saving');
      try { dirty = false; await cloudPut(file, read()); setState('saved'); }
      catch (e) { dirty = true; setState(String(e.message || e).includes('no backend') ? 'nobackend' : 'offline'); }
      finally { busy = false; if (again) { again = false; toCloud(); } }
    }, 6000);
  };
  return {
    key,
    touch() { dirty = true; toLocal(); toCloud(); setState('local'); },
    async flush() {
      clearTimeout(localT); await localSet(key, read());
      if (!dirty) return;
      clearTimeout(cloudT);
      if (await backend().catch(() => null)) {
        setState('saving');
        try { dirty = false; await cloudPut(file, read()); setState('saved'); } catch (e) { dirty = true; setState('offline'); }
      }
    }
  };
}
