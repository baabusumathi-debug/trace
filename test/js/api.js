// Talks to the private Apps Script backend (or to bundled demo files in demo mode).
import { db } from './db.js';

let conn = null;      // { url, key }
let demo = false;

export async function initApi(isDemo) {
  demo = isDemo;
  if (!demo) conn = (await db.kv.get('backend')) || null;
}
export const isDemo = () => demo;
export const hasBackend = () => demo || !!(conn && conn.url && conn.key);
export async function setBackend(url, key) { conn = { url, key }; await db.kv.set('backend', conn); }

async function post(body, timeoutMs = 60000) {
  const ctl = new AbortController();
  const t = setTimeout(() => ctl.abort(), timeoutMs);
  try {
    const res = await fetch(conn.url, {
      method: 'POST',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },   // simple request: no CORS preflight
      body: JSON.stringify({ key: conn.key, ...body }),
      redirect: 'follow',
      signal: ctl.signal
    });
    if (!res.ok) throw new Error('backend HTTP ' + res.status);
    const j = await res.json();
    if (!j.ok) throw new Error(j.error || 'backend error');
    return j;
  } finally { clearTimeout(t); }
}

/** Run several operations in one round trip. Returns [{ok, data|error}] in order. */
export async function batch(ops) {
  if (!ops.length) return [];
  if (demo) return Promise.all(ops.map(demoOp));
  const j = await post({ op: 'batch', ops });
  return j.results;
}
export async function call(op) {
  const [r] = await batch([op]);
  if (!r.ok) throw new Error(r.error);
  return r.data;
}

/* ---------- demo mode: read bundled files, accept writes silently ---------- */
async function demoOp(o) {
  try {
    if (o.op === 'readFile') {
      const res = await fetch('demo/' + o.id);
      if (!res.ok) throw new Error('missing demo file ' + o.id);
      return { ok: true, data: { id: o.id, text: await res.text() } };
    }
    if (o.op === 'sheetRead') return { ok: true, data: { values: [], lastRow: 0 } };
    if (o.op === 'sheetAppend') return { ok: true, data: { appended: (o.rows || []).length } };
    if (o.op === 'findFile') {
      const res = await fetch('demo/' + o.name, { method: 'HEAD' });
      return { ok: true, data: res.ok ? { id: o.name, name: o.name } : null };
    }
    if (o.op === 'writeFile') return { ok: true, data: { id: 'demo-' + o.name } };
    if (o.op === 'ping') return { ok: true, data: { demo: true } };
    throw new Error('demo: ' + o.op);
  } catch (e) { return { ok: false, error: e.message }; }
}
