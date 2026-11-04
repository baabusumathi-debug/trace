// Ink on cards (T-057): S Pen writing over the card (this device's layout only) and in "rooms" that open under any line
// (rooms scale to any screen). Pen, highlighter, eraser, lasso, shapes (with auto shape), text, undo/redo.
// Pen draws; fingers scroll; the S Pen side button erases while held. Everything is stored per card on this device.
import { db } from './db.js';

/* ============================ settings ============================ */
const SKEY = 'trace.ink.settings';
const DEF = {
  tool: 'pen',
  pen: { type: 'fountain', size: 2.5, color: '#1f4fd8' },
  hl: { size: 16, color: '#ffcc00', op: 45, snap: true },
  er: { mode: 'stroke', size: 20, hlOnly: false },
  shape: { kind: 'free', auto: true },
  text: { size: 16, color: '#1c1c1e', bold: false },
  recent: ['#1c1c1e', '#1f4fd8', '#e0312b', '#2e9d4f', '#ff9500', '#8e44ad']
};
let S = (() => { try { return Object.assign(structuredClone(DEF), JSON.parse(localStorage.getItem(SKEY) || '{}')); } catch (e) { return structuredClone(DEF); } })();
const saveS = () => { try { localStorage.setItem(SKEY, JSON.stringify(S)); } catch (e) { /* private mode */ } };
export const PEN_TYPES = [['fountain', 'Fountain pen'], ['pen', 'Pen'], ['pencil', 'Pencil'], ['calli', 'Calligraphy'], ['brush', 'Brush']];
export const PRESETS = ['#000000', '#ffffff', '#ff3b30', '#ff9500', '#ffcc00', '#34c759', '#00c7be', '#32ade6', '#007aff', '#5856d6', '#af52de', '#ff2d55', '#a2845e', '#8e8e93'];
function h2x(h, s, l) { s /= 100; l /= 100; const k = n => (n + h / 30) % 12, a = s * Math.min(l, 1 - l), f = n => l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1))); return '#' + [f(0), f(8), f(4)].map(x => Math.round(x * 255).toString(16).padStart(2, '0')).join(''); }
export const SWATCHES = ['#ffffff', '#e5e5ea', '#d1d1d6', '#c7c7cc', '#aeaeb2', '#8e8e93', '#636366', '#48484a', '#3a3a3c', '#2c2c2e', '#1c1c1e', '#000000']
  .concat(...[[95, 90], [92, 78], [88, 64], [84, 52], [74, 40], [64, 28]].map(([s, l]) => [0, 20, 35, 50, 60, 90, 130, 170, 195, 215, 245, 285].map(h => h2x(h, s, l))));

/* ============================ geometry and drawing ============================ */
const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1]);
function rdp(pts, eps) {
  if (pts.length < 3) return pts.slice();
  let dmax = 0, idx = 0; const a = pts[0], b = pts[pts.length - 1];
  for (let i = 1; i < pts.length - 1; i++) {
    const p = pts[i], L = dist(a, b);
    const d = L < 1e-6 ? dist(a, p) : Math.abs((b[1] - a[1]) * p[0] - (b[0] - a[0]) * p[1] + b[0] * a[1] - b[1] * a[0]) / L;
    if (d > dmax) { dmax = d; idx = i; }
  }
  if (dmax > eps) { const l = rdp(pts.slice(0, idx + 1), eps), r = rdp(pts.slice(idx), eps); return l.slice(0, -1).concat(r); }
  return [a, b];
}
function bbox(pts) { let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity; for (const p of pts) { x0 = Math.min(x0, p[0]); y0 = Math.min(y0, p[1]); x1 = Math.max(x1, p[0]); y1 = Math.max(y1, p[1]); } return [x0, y0, x1, y1]; }
// Auto shape: a rough line, triangle, rectangle or ellipse becomes a clean one.
// corners of a closed stroke: split at the point farthest from the start, simplify each half, then drop near-straight vertices
function corners(pts, eps) {
  let far = 0, fd = 0; pts.forEach((p, i) => { const d = dist(p, pts[0]); if (d > fd) { fd = d; far = i; } });
  const A = rdp(pts.slice(0, far + 1), eps), B = rdp(pts.slice(far).concat([pts[0]]), eps);
  let v = A.slice(0, -1).concat(B.slice(0, -1));
  for (let pass = 0; pass < 4 && v.length > 3; pass++) {
    let worst = -1, wa = 0;
    v.forEach((p, i) => { const a = v[(i + v.length - 1) % v.length], c = v[(i + 1) % v.length]; const v1 = [a[0] - p[0], a[1] - p[1]], v2 = [c[0] - p[0], c[1] - p[1]]; const cos = (v1[0] * v2[0] + v1[1] * v2[1]) / ((Math.hypot(...v1) * Math.hypot(...v2)) || 1); const ang = Math.acos(Math.max(-1, Math.min(1, cos))) * 180 / Math.PI; if (ang > 150 && ang > wa) { wa = ang; worst = i; } });
    // also merge vertices that sit very close together (the pen lifting over its start)
    if (worst < 0) { const i = v.findIndex((p, j) => dist(p, v[(j + 1) % v.length]) < eps * 1.5); if (i < 0) break; worst = i; }
    v.splice(worst, 1);
  }
  return v;
}
// Auto shape: a rough line, triangle, rectangle (or any 4-sided shape) or ellipse becomes a clean one.
export function recognise(pts) {
  if (pts.length < 5) return null;
  const [x0, y0, x1, y1] = bbox(pts), w = x1 - x0, h = y1 - y0, diag = Math.hypot(w, h) || 1;
  if (diag < 8) return null;
  let len = 0; for (let i = 1; i < pts.length; i++) len += dist(pts[i - 1], pts[i]);
  const gap = dist(pts[0], pts[pts.length - 1]);
  // open stroke
  if (gap > diag * 0.28) {
    if (gap / len > 0.9) return { kind: 'line', pts: [pts[0].slice(0, 2), pts[pts.length - 1].slice(0, 2)] };
    const s2 = rdp(pts, diag * 0.07);
    if (s2.length === 3) return { kind: 'poly', open: true, pts: s2.map(p => p.slice(0, 2)) };
    return null;
  }
  // closed: how far is it from an ellipse filling its box?
  const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2, rx = w / 2 || 1, ry = h / 2 || 1;
  const ell = pts.reduce((t, p) => t + Math.abs(Math.hypot((p[0] - cx) / rx, (p[1] - cy) / ry) - 1), 0) / pts.length;
  const v = corners(pts, diag * 0.06);
  const n = v.length;
  if (n === 3 && ell > 0.1) return { kind: 'poly', pts: v.map(p => p.slice(0, 2)) };
  if (n === 4 && ell > 0.09) {
    const right = v.every((p, i) => { const a = v[(i + 3) % 4], c = v[(i + 1) % 4]; const v1 = [a[0] - p[0], a[1] - p[1]], v2 = [c[0] - p[0], c[1] - p[1]]; return Math.abs((v1[0] * v2[0] + v1[1] * v2[1]) / ((Math.hypot(...v1) * Math.hypot(...v2)) || 1)) < 0.3; });
    const level = v.every((p, i) => { const c = v[(i + 1) % 4], ang = Math.abs(Math.atan2(c[1] - p[1], c[0] - p[0]) * 180 / Math.PI) % 90; return ang < 12 || ang > 78; });
    return right && level ? { kind: 'rect', pts: [[x0, y0], [x1, y1]] } : { kind: 'poly', pts: v.map(p => p.slice(0, 2)) };
  }
  if (ell < 0.2) return { kind: 'ellipse', pts: [[x0, y0], [x1, y1]] };
  return null;                                            // not clearly a shape: keep the handwriting
}
function widthAt(o, p, prev) {
  const base = o.s, pr = p[2] == null ? 0.5 : p[2];
  switch (o.pen) {
    case 'pen': return base;
    case 'pencil': return base * (0.75 + pr * 0.4);
    case 'brush': return base * (0.25 + pr * 1.6);
    case 'calli': { if (!prev) return base; const a = Math.atan2(p[1] - prev[1], p[0] - prev[0]); return base * (0.3 + 1.1 * Math.abs(Math.sin(a - Math.PI / 4))); }
    default: return base * (0.55 + pr * 0.85);       // fountain
  }
}
function drawStroke(g, o, X, Y, k) {
  const pts = o.pts; if (!pts.length) return;
  g.save(); g.lineCap = 'round'; g.lineJoin = 'round'; g.strokeStyle = o.c; g.fillStyle = o.c;
  if (o.pen === 'pencil') g.globalAlpha = 0.82;
  if (pts.length === 1) { g.beginPath(); g.arc(X(pts[0]), Y(pts[0]), widthAt(o, pts[0]) * k / 2, 0, Math.PI * 2); g.fill(); g.restore(); return; }
  for (let i = 1; i < pts.length; i++) {
    const a = pts[i - 1], b = pts[i], c = pts[i + 1];
    g.lineWidth = Math.max(0.6, widthAt(o, b, a) * k);
    g.beginPath();
    const m1 = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2];
    if (i === 1) { g.moveTo(X(a), Y(a)); g.lineTo(X(m1), Y(m1)); }
    g.moveTo(X(m1), Y(m1));
    if (c) { const m2 = [(b[0] + c[0]) / 2, (b[1] + c[1]) / 2]; g.quadraticCurveTo(X(b), Y(b), X(m2), Y(m2)); }
    else g.lineTo(X(b), Y(b));
    g.stroke();
  }
  g.restore();
}
function drawShape(g, o, X, Y, k) {
  g.save(); g.strokeStyle = o.c; g.lineWidth = Math.max(0.8, o.s * k); g.lineCap = 'round'; g.lineJoin = 'round';
  const p = o.pts; g.beginPath();
  if (o.kind === 'line' || o.kind === 'arrow') {
    g.moveTo(X(p[0]), Y(p[0])); g.lineTo(X(p[1]), Y(p[1]));
    if (o.kind === 'arrow') { const a = Math.atan2(Y(p[1]) - Y(p[0]), X(p[1]) - X(p[0])), L = 10 + o.s * k * 2; [a + 2.6, a - 2.6].forEach(t => { g.moveTo(X(p[1]), Y(p[1])); g.lineTo(X(p[1]) + Math.cos(t) * L, Y(p[1]) + Math.sin(t) * L); }); }
  } else if (o.kind === 'rect') { g.rect(X(p[0]), Y(p[0]), X(p[1]) - X(p[0]), Y(p[1]) - Y(p[0])); }
  else if (o.kind === 'ellipse') { const cx = (X(p[0]) + X(p[1])) / 2, cy = (Y(p[0]) + Y(p[1])) / 2; g.ellipse(cx, cy, Math.abs(X(p[1]) - X(p[0])) / 2, Math.abs(Y(p[1]) - Y(p[0])) / 2, 0, 0, Math.PI * 2); }
  else if (o.kind === 'poly') { g.moveTo(X(p[0]), Y(p[0])); p.slice(1).forEach(q => g.lineTo(X(q), Y(q))); if (!o.open) g.closePath(); }
  else if (o.kind === 'tri') { const [a, b] = p; g.moveTo((X(a) + X(b)) / 2, Y(a)); g.lineTo(X(b), Y(b)); g.lineTo(X(a), Y(b)); g.closePath(); }
  g.stroke(); g.restore();
}
function drawText(g, o, X, Y, k) {
  g.save(); g.fillStyle = o.c; g.textBaseline = 'top';
  g.font = `${o.b ? '700 ' : ''}${Math.round(o.s * k)}px system-ui, sans-serif`;
  String(o.t || '').split('\n').forEach((l, i) => g.fillText(l, X(o.pts[0]), Y(o.pts[0]) + i * o.s * k * 1.3));
  g.restore();
}
export function paint(g, objs, X, Y, k, w, h) {
  // highlighters underneath, on their own layer, multiplied onto the page
  const hls = objs.filter(o => o.type === 'hl');
  if (hls.length) {
    const off = document.createElement('canvas'); off.width = g.canvas.width; off.height = g.canvas.height;
    const og = off.getContext('2d'); og.setTransform(g.getTransform());
    for (const o of hls) {
      og.globalAlpha = 1;
      if (o.snap) { og.fillStyle = o.c; og.fillRect(X(o.pts[0]), Y(o.pts[0]) - o.h * k / 2, X(o.pts[1]) - X(o.pts[0]), o.h * k); }
      else { og.save(); og.strokeStyle = o.c; og.lineCap = 'butt'; og.lineJoin = 'round'; og.lineWidth = o.s * k; og.beginPath(); o.pts.forEach((p, i) => i ? og.lineTo(X(p), Y(p)) : og.moveTo(X(p), Y(p))); og.stroke(); og.restore(); }
    }
    g.save(); g.setTransform(1, 0, 0, 1, 0, 0); g.globalCompositeOperation = 'multiply';
    // each highlighter's own opacity: draw per opacity group
    const ops = [...new Set(hls.map(o => o.o))];
    if (ops.length === 1) { g.globalAlpha = ops[0]; g.drawImage(off, 0, 0); }
    else { g.globalAlpha = hls.reduce((t, o) => t + o.o, 0) / hls.length; g.drawImage(off, 0, 0); }
    g.restore();
  }
  for (const o of objs) {
    if (o.type === 'pen') drawStroke(g, o, X, Y, k);
    else if (o.type === 'shape') drawShape(g, o, X, Y, k);
    else if (o.type === 'text') drawText(g, o, X, Y, k);
  }
}
function objPts(o) {
  if (o.type === 'text') { const L = String(o.t || '').length * o.s * 0.55; return [o.pts[0], [o.pts[0][0] + L, o.pts[0][1]], [o.pts[0][0] + L, o.pts[0][1] + o.s * 1.3], [o.pts[0][0], o.pts[0][1] + o.s * 1.3]]; }
  if (o.type === 'hl' && o.snap) { const [a, b] = o.pts, n = 12, out = []; for (let i = 0; i <= n; i++) out.push([a[0] + (b[0] - a[0]) * i / n, a[1]]); return out; }
  if (o.type === 'shape' && (o.kind === 'rect' || o.kind === 'ellipse' || o.kind === 'tri')) { const [a, b] = o.pts; return [a, [b[0], a[1]], b, [a[0], b[1]], [(a[0] + b[0]) / 2, a[1]], [(a[0] + b[0]) / 2, b[1]], [a[0], (a[1] + b[1]) / 2], [b[0], (a[1] + b[1]) / 2]]; }
  return o.pts;
}
function segDist(p, a, b) { const dx = b[0] - a[0], dy = b[1] - a[1], L = dx * dx + dy * dy; let t = L ? ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / L : 0; t = Math.max(0, Math.min(1, t)); return Math.hypot(p[0] - a[0] - t * dx, p[1] - a[1] - t * dy); }
// is point p within r of the object (its ink, not just its points)?
export function hits(o, p, r) {
  if (o.type === 'hl' && o.snap) { const [a, b] = o.pts, x0 = Math.min(a[0], b[0]), x1 = Math.max(a[0], b[0]); return p[0] > x0 - r && p[0] < x1 + r && Math.abs(p[1] - a[1]) < o.h / 2 + r; }
  if (o.type === 'text') { const [x0, y0, x1, y1] = bbox(objPts(o)); return p[0] > x0 - r && p[0] < x1 + r && p[1] > y0 - r && p[1] < y1 + r; }
  const w = (o.type === 'hl' ? o.s : (o.s || 2)) / 2 + r;
  let q = objPts(o);
  if (o.type === 'shape' && (o.kind === 'rect' || o.kind === 'tri')) { const [a, b] = o.pts; q = [a, [b[0], a[1]], b, [a[0], b[1]], a]; }
  if (o.type === 'shape' && o.kind === 'ellipse') { const [a, b] = o.pts, cx = (a[0] + b[0]) / 2, cy = (a[1] + b[1]) / 2, rx = Math.abs(b[0] - a[0]) / 2, ry = Math.abs(b[1] - a[1]) / 2; q = []; for (let i = 0; i <= 32; i++) q.push([cx + rx * Math.cos(i / 16 * Math.PI), cy + ry * Math.sin(i / 16 * Math.PI)]); }
  if (o.type === 'shape' && o.kind === 'poly' && !o.open) q = o.pts.concat([o.pts[0]]);
  if (q.length === 1) return dist(q[0], p) < w;
  for (let i = 1; i < q.length; i++) if (segDist(p, q[i - 1], q[i]) < w) return true;
  return false;
}
function inPoly(p, poly) { let c = false; for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) { const a = poly[i], b = poly[j]; if (((a[1] > p[1]) !== (b[1] > p[1])) && (p[0] < (b[0] - a[0]) * (p[1] - a[1]) / (b[1] - a[1] + 1e-9) + a[0])) c = !c; } return c; }

/* ============================ a drawing surface ============================ */
// A surface keeps objects in its own units. map: { toUnits(clientX, clientY) -> [x, y], X(p), Y(p), k }.
class Surface {
  constructor(canvas, objs, opts) {
    this.cv = canvas; this.objs = objs || []; this.o = opts; this.undo = []; this.redo = []; this.sel = null; this.live = null;
    this.g = canvas.getContext('2d');
  }
  snapshot() { this.undo.push(JSON.stringify(this.objs)); if (this.undo.length > 60) this.undo.shift(); this.redo = []; }
  doUndo() { if (!this.undo.length) return; this.redo.push(JSON.stringify(this.objs)); this.objs.splice(0, this.objs.length, ...JSON.parse(this.undo.pop())); this.sel = null; this.render(); this.o.changed(); }
  doRedo() { if (!this.redo.length) return; this.undo.push(JSON.stringify(this.objs)); this.objs.splice(0, this.objs.length, ...JSON.parse(this.redo.pop())); this.sel = null; this.render(); this.o.changed(); }
  request() { if (this._raf) return; this._raf = requestAnimationFrame(() => { this._raf = 0; this.render(); }); }
  render() {
    if (this._raf) { cancelAnimationFrame(this._raf); this._raf = 0; }
    const cv = this.cv, g = this.g, dpr = window.devicePixelRatio || 1, m = this.o.map();
    const W = cv.clientWidth, H = cv.clientHeight;
    if (cv.width !== Math.round(W * dpr) || cv.height !== Math.round(H * dpr)) { cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); this._baseOk = false; }
    g.setTransform(1, 0, 0, 1, 0, 0); g.clearRect(0, 0, cv.width, cv.height);
    if (this.live) {
      // while a stroke is being drawn, the finished ink is painted once into a cached layer; each frame only adds the live stroke
      if (!this._baseOk) {
        const bc = this._base || (this._base = document.createElement('canvas')); bc.width = cv.width; bc.height = cv.height;
        const bg = bc.getContext('2d'); bg.setTransform(dpr, 0, 0, dpr, 0, 0); paint(bg, this.objs.filter(o => !o.hidden), m.X, m.Y, m.k, W, H); this._baseOk = true;
      }
      g.drawImage(this._base, 0, 0);
      g.setTransform(dpr, 0, 0, dpr, 0, 0);
      let lv = this.live;
      if (this.pred && this.pred.length && lv.type === 'pen') { const lp = lv.pts[lv.pts.length - 1]; lv = { ...lv, pts: lv.pts.concat(this.pred.map(q => [q[0], q[1], lp[2]])) }; }
      paint(g, [lv], m.X, m.Y, m.k, W, H);
    } else {
      this._baseOk = false;
      g.setTransform(dpr, 0, 0, dpr, 0, 0);
      paint(g, this.objs.filter(o => !o.hidden), m.X, m.Y, m.k, W, H);
    }
    if (this.sel && this.sel.ids.length) {
      const pts = this.sel.ids.filter(i => this.objs[i]).flatMap(i => objPts(this.objs[i]).map(p => [m.X(p), m.Y(p)]));
      if (pts.length) {
        const [x0, y0, x1, y1] = bbox(pts);
        g.save(); g.fillStyle = 'rgba(42,127,255,.06)'; g.fillRect(x0 - 10, y0 - 10, x1 - x0 + 20, y1 - y0 + 20);
        g.setLineDash([6, 4]); g.strokeStyle = '#2a7fff'; g.lineWidth = 1.4; g.strokeRect(x0 - 10, y0 - 10, x1 - x0 + 20, y1 - y0 + 20); g.restore();
        this.sel.box = [x0 - 10, y0 - 10, x1 + 10, y1 + 10];
      }
    }
    if (this.lasso && this.lasso.length > 1) { g.save(); g.setLineDash([4, 4]); g.strokeStyle = '#2a7fff'; g.lineWidth = 1.4; g.beginPath(); this.lasso.forEach((p, i) => i ? g.lineTo(m.X(p), m.Y(p)) : g.moveTo(m.X(p), m.Y(p))); g.stroke(); g.restore(); }
  }
}

/* ============================ the toolbar (Samsung Notes style) ============================ */
const ICONS = {
  pen: '<svg viewBox="0 0 24 24"><path d="M14.6 4.6l4.8 4.8L9 19.8l-5.3.9.9-5.3z"/><path d="M12.8 6.4l4.8 4.8"/><path class="tipc" d="M3.7 20.7l.6-3.4 2.8 2.8z"/></svg>',
  hl: '<svg viewBox="0 0 24 24"><path d="M15.2 3.4l5.4 5.4-7.9 7.9-5.4-5.4z"/><path d="M7.3 11.3l-1.6 4.6 2.4 2.4 4.6-1.6"/><path class="tipc" d="M5.7 15.9l-2.4 4.1 1.6.8 3.2-2.5z"/></svg>',
  er: '<svg viewBox="0 0 24 24"><path d="M3.9 15.1l9.5-9.5a2 2 0 0 1 2.8 0l3.2 3.2a2 2 0 0 1 0 2.8L12 19H7.8z"/><path d="M8.6 10.4l5 5"/><path d="M12 19h8.5"/></svg>',
  lasso: '<svg viewBox="0 0 24 24"><ellipse cx="12" cy="9.5" rx="8" ry="5" stroke-dasharray="2.6 2.4"/><path d="M8.2 13.6c-1.4.9-1.6 2.6-.4 3.4 1 .7 2.4.2 2.5-1"/><path d="M7.8 17l-1.3 3.5"/></svg>',
  undo: '<svg viewBox="0 0 24 24"><path d="M8.5 5.5L4 10l4.5 4.5"/><path d="M4 10h10.5a5.5 5.5 0 0 1 0 11H11"/></svg>',
  redo: '<svg viewBox="0 0 24 24"><path d="M15.5 5.5L20 10l-4.5 4.5"/><path d="M20 10H9.5a5.5 5.5 0 0 0 0 11H13"/></svg>',
  shape: '<svg viewBox="0 0 24 24"><rect x="3.5" y="3.5" width="10" height="10" rx="1.5"/><circle cx="15" cy="15" r="5.5"/></svg>',
  text: '<svg viewBox="0 0 24 24"><path d="M5 6.5V4.5h14v2"/><path d="M12 4.5v15"/><path d="M9 19.5h6"/></svg>',
  done: '<svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
  grip: '<svg viewBox="0 0 24 24"><g class="dots"><circle cx="9" cy="6" r="1.3"/><circle cx="15" cy="6" r="1.3"/><circle cx="9" cy="12" r="1.3"/><circle cx="15" cy="12" r="1.3"/><circle cx="9" cy="18" r="1.3"/><circle cx="15" cy="18" r="1.3"/></g></svg>',
  fab: '<svg viewBox="0 0 24 24"><path d="M14.6 4.6l4.8 4.8L9 19.8l-5.3.9.9-5.3z"/><path d="M12.8 6.4l4.8 4.8"/><path d="M14 20.5h6.5"/></svg>'
};
export const INK_ICONS = ICONS;
function slider(lab, key, min, max, step, val, fmt) { return `<div class="ik-row"><label>${lab}</label><input type="range" min="${min}" max="${max}" step="${step}" value="${val}" data-k="${key}"><span class="ik-num" data-n="${key}">${fmt(val)}</span></div>`; }
function colourRow(cur, more) {
  return `<div class="ik-row"><label>Colour</label><div class="ik-pre">${PRESETS.map(c => `<span class="ik-dot${c === cur ? ' on' : ''}" style="background:${c}" data-c="${c}" title="${c}"></span>`).join('')}<button class="ik-more" data-more>${more ? 'Less' : 'All colours'}</button></div></div>
    ${more ? `<div class="ik-grid">${SWATCHES.map(c => `<i style="background:${c}" data-c="${c}" class="${c === cur ? 'on' : ''}" title="${c}"></i>`).join('')}</div>
    <div class="ik-row"><label>Any colour</label><input type="color" value="${cur}" data-cpick><span class="ik-num">${cur}</span></div>` : ''}`;
}
const POS_KEY = 'trace.ink.pos';
export class Toolbar {
  constructor(host, api) { this.host = host; this.api = api; this.open = false; this.more = false; this.place(); this.draw(); }
  place() {
    let pos = null; try { pos = JSON.parse(localStorage.getItem(POS_KEY) || 'null'); } catch (e) { pos = null; }
    const h = this.host; h.classList.add('ik-float');
    if (pos && pos.x != null) { const x = Math.max(4, Math.min(innerWidth - 70, pos.x)), y = Math.max(4, Math.min(innerHeight - 120, pos.y)); h.style.left = x + 'px'; h.style.top = y + 'px'; h.style.right = 'auto'; h.style.transform = 'none'; }
    else { h.style.left = ''; h.style.top = ''; h.style.right = ''; h.style.transform = ''; }
    this.side();
  }
  side() { const r = this.host.getBoundingClientRect(); this.host.classList.toggle('ik-left', r.left + r.width / 2 < innerWidth / 2); }
  closePop() { if (this.open) { this.open = false; this.draw(); } }
  draw() {
    const t = S.tool;
    const btn = (k, lab, extra = '') => `<button class="ik-ic${t === k ? ' on' : ''}" data-t="${k}" aria-label="${lab}" title="${lab}"${extra}>${ICONS[k]}</button>`;
    const tipOf = k => k === 'hl' ? S.hl.color : k === 'text' ? S.text.color : S.pen.color;
    this.host.innerHTML = `<div class="ik-bar" role="toolbar" aria-label="Pen tools">
        <div class="ik-grip" data-grip title="Drag to move the toolbar">${ICONS.grip}</div>
        ${btn('pen', 'Pen · tap again for settings', ` style="--tip:${S.pen.color}"`)}${btn('hl', 'Highlighter · tap again for settings', ` style="--tip:${S.hl.color}"`)}${btn('er', 'Eraser · tap again for settings')}${btn('lasso', 'Lasso select')}
        ${btn('shape', 'Shapes · tap again for settings')}${btn('text', 'Text · tap again for settings')}
        <span class="ik-sep"></span>
        <button class="ik-ic" data-undo aria-label="Undo" title="Undo">${ICONS.undo}</button><button class="ik-ic" data-redo aria-label="Redo" title="Redo">${ICONS.redo}</button>
        <span class="ik-sep"></span>
        <button class="ik-cur" data-curc style="--c:${tipOf(t)}" aria-label="Colour and size" title="Colour and size"><i></i></button>
        <button class="ik-ic ik-done" data-done aria-label="Done writing" title="Done writing">${ICONS.done}</button>
      </div>
      <div class="ik-pop"${this.open ? '' : ' hidden'}><div class="ik-pophead"><b>${{ pen: 'Pen', hl: 'Highlighter', er: 'Eraser', lasso: 'Lasso', shape: 'Shapes', text: 'Text' }[t] || ''}</b><button class="ik-x" data-close aria-label="Close settings">✕</button></div>${this.popHtml()}</div>
      <div class="ik-selbar"${this.api.hasSel() ? '' : ' hidden'}><span>Selected</span><button data-sel="del">Delete</button><button data-sel="copy">Copy</button><button data-sel="style">Apply ${S.tool === 'hl' ? 'highlighter' : 'pen'} style</button><button data-sel="none">Done</button><small>drag inside the box to move</small></div>`;
    this.bind();
  }
  popHtml() {
    const t = S.tool;
    if (t === 'pen') return `<div class="ik-row"><label>Type</label><div class="ik-pt">${PEN_TYPES.map(([k, l]) => `<button class="${S.pen.type === k ? 'on' : ''}" data-pt="${k}">${l}</button>`).join('')}</div></div>`
      + slider('Size', 'pen.size', 0.5, 20, 0.5, S.pen.size, v => (+v).toFixed(1)) + colourRow(S.pen.color, this.more)
      + `<div class="ik-prev"><canvas width="560" height="56" data-prev></canvas></div>`;
    if (t === 'hl') return `<div class="ik-row"><label>Snap to text</label><div class="ik-pt"><button class="${S.hl.snap ? 'on' : ''}" data-snap="1">On</button><button class="${!S.hl.snap ? 'on' : ''}" data-snap="0">Off</button></div></div>`
      + slider('Size', 'hl.size', 4, 40, 1, S.hl.size, v => v) + slider('Opacity', 'hl.op', 10, 90, 5, S.hl.op, v => v + '%') + colourRow(S.hl.color, this.more)
      + `<div class="ik-prev"><canvas width="560" height="56" data-prev></canvas></div>`;
    if (t === 'er') return `<div class="ik-row"><label>Eraser</label><div class="ik-pt"><button class="${S.er.mode === 'stroke' ? 'on' : ''}" data-em="stroke">Stroke</button><button class="${S.er.mode === 'partial' ? 'on' : ''}" data-em="partial">Partial</button></div></div>`
      + slider('Size', 'er.size', 5, 60, 1, S.er.size, v => v)
      + `<div class="ik-row"><label>Highlighter only</label><div class="ik-pt"><button class="${S.er.hlOnly ? 'on' : ''}" data-hlo="1">On</button><button class="${!S.er.hlOnly ? 'on' : ''}" data-hlo="0">Off</button></div></div>
        <div class="ik-row"><label>S Pen button</label><span class="ik-note">hold the side button while writing to erase · last pen signal: <b class="mono">${penSignal()}</b></span></div>
        <div class="ik-row"><label></label><button class="ik-more" data-clear>Clear this side</button></div>`;
    if (t === 'lasso') return `<div class="ik-row"><label>Select</label><span class="ik-note">draw a loop round ink or highlights, or tap one mark; drag inside the box to move; Delete in the blue bar</span></div>`;
    if (t === 'shape') return `<div class="ik-row"><label>Draw</label><div class="ik-pt">${[['free', 'Freehand'], ['line', 'Line'], ['arrow', 'Arrow'], ['rect', 'Rectangle'], ['ellipse', 'Ellipse'], ['tri', 'Triangle']].map(([k, l]) => `<button class="${S.shape.kind === k ? 'on' : ''}" data-sk="${k}">${l}</button>`).join('')}</div></div>
        <div class="ik-row"><label>Auto shape</label><div class="ik-pt"><button class="${S.shape.auto ? 'on' : ''}" data-auto="1">On · draw, keep the pen still ½ s</button><button class="${!S.shape.auto ? 'on' : ''}" data-auto="0">Off</button></div></div>
        <p class="ik-note">Shapes use the pen's colour and size. Auto shape also works with the pen.</p>`;
    if (t === 'text') return slider('Size', 'text.size', 10, 36, 1, S.text.size, v => v)
      + `<div class="ik-row"><label>Bold</label><div class="ik-pt"><button class="${S.text.bold ? 'on' : ''}" data-tb="1">On</button><button class="${!S.text.bold ? 'on' : ''}" data-tb="0">Off</button></div></div>`
      + colourRow(S.text.color, this.more) + '<p class="ik-note">Tap where the text should go.</p>';
    return '';
  }
  bind() {
    const h = this.host, set = (path, v) => { const [a, b] = path.split('.'); S[a][b] = v; saveS(); };
    // tap a tool = choose it; tap the chosen tool again = its settings
    h.querySelectorAll('[data-t]').forEach(b => b.onclick = () => { const k = b.dataset.t; if (S.tool === k) this.open = !this.open; else { S.tool = k; this.open = false; this.more = false; this.api.toolChanged(); } saveS(); this.draw(); });
    const cc = h.querySelector('[data-curc]'); if (cc) cc.onclick = () => { if (S.tool === 'er' || S.tool === 'lasso') S.tool = 'pen'; this.open = !this.open; saveS(); this.draw(); };
    const cx = h.querySelector('[data-close]'); if (cx) cx.onclick = () => { this.open = false; this.draw(); };
    const gp = h.querySelector('[data-grip]');
    if (gp) gp.onpointerdown = e => {
      e.preventDefault(); gp.setPointerCapture(e.pointerId);
      const r = h.getBoundingClientRect(), ox = e.clientX - r.left, oy = e.clientY - r.top;
      const mv = ev => { const x = Math.max(4, Math.min(innerWidth - r.width - 4, ev.clientX - ox)), y = Math.max(4, Math.min(innerHeight - 60, ev.clientY - oy)); h.style.left = x + 'px'; h.style.top = y + 'px'; h.style.right = 'auto'; h.style.transform = 'none'; this.side(); };
      const up = () => { gp.removeEventListener('pointermove', mv); gp.removeEventListener('pointerup', up); gp.removeEventListener('pointercancel', up); const rr = h.getBoundingClientRect(); try { localStorage.setItem(POS_KEY, JSON.stringify({ x: rr.left, y: rr.top })); } catch (er) { /* private mode */ } };
      gp.addEventListener('pointermove', mv); gp.addEventListener('pointerup', up); gp.addEventListener('pointercancel', up);
    };
    gp && (gp.ondblclick = () => { try { localStorage.removeItem(POS_KEY); } catch (er) { /* */ } this.place(); });
    h.querySelector('[data-undo]').onclick = () => this.api.undo();
    h.querySelector('[data-redo]').onclick = () => this.api.redo();
    h.querySelector('[data-done]').onclick = () => this.api.done();
    h.querySelectorAll('[data-k]').forEach(r => r.oninput = () => { set(r.dataset.k, +r.value); const n = h.querySelector(`[data-n="${r.dataset.k}"]`); if (n) n.textContent = r.dataset.k === 'hl.op' ? r.value + '%' : r.dataset.k === 'pen.size' ? (+r.value).toFixed(1) : r.value; this.preview(); });
    const colKey = S.tool === 'hl' ? 'hl' : S.tool === 'text' ? 'text' : 'pen';
    h.querySelectorAll('[data-c]').forEach(d => d.onclick = () => { S[colKey].color = d.dataset.c; saveS(); this.draw(); });
    const cp = h.querySelector('[data-cpick]'); if (cp) cp.onchange = () => { S[colKey].color = cp.value; saveS(); this.draw(); };
    const mo = h.querySelector('[data-more]'); if (mo) mo.onclick = () => { this.more = !this.more; this.draw(); };
    h.querySelectorAll('[data-pt]').forEach(b => b.onclick = () => { S.pen.type = b.dataset.pt; saveS(); this.draw(); });
    h.querySelectorAll('[data-snap]').forEach(b => b.onclick = () => { S.hl.snap = b.dataset.snap === '1'; saveS(); this.draw(); });
    h.querySelectorAll('[data-em]').forEach(b => b.onclick = () => { S.er.mode = b.dataset.em; saveS(); this.draw(); });
    h.querySelectorAll('[data-hlo]').forEach(b => b.onclick = () => { S.er.hlOnly = b.dataset.hlo === '1'; saveS(); this.draw(); });
    h.querySelectorAll('[data-sk]').forEach(b => b.onclick = () => { S.shape.kind = b.dataset.sk; saveS(); this.draw(); });
    h.querySelectorAll('[data-auto]').forEach(b => b.onclick = () => { S.shape.auto = b.dataset.auto === '1'; saveS(); this.draw(); });
    h.querySelectorAll('[data-tb]').forEach(b => b.onclick = () => { S.text.bold = b.dataset.tb === '1'; saveS(); this.draw(); });
    const cl = h.querySelector('[data-clear]'); if (cl) cl.onclick = () => this.api.clear();
    h.querySelectorAll('[data-sel]').forEach(b => b.onclick = () => this.api.selAction(b.dataset.sel));
    this.preview();
  }
  preview() {
    const cv = this.host.querySelector('[data-prev]'); if (!cv) return;
    const g = cv.getContext('2d'); g.clearRect(0, 0, cv.width, cv.height); g.fillStyle = '#f6f1e3'; g.fillRect(0, 0, cv.width, cv.height);
    const pts = []; for (let i = 0; i <= 40; i++) { const x = 20 + i * 13; pts.push([x, 28 + Math.sin(i / 4) * 12, 0.25 + 0.75 * Math.sin(i / 40 * Math.PI)]); }
    const id = v => v;
    if (S.tool === 'hl') paint(g, [{ type: 'hl', c: S.hl.color, s: S.hl.size, o: S.hl.op / 100, snap: S.hl.snap, h: S.hl.size, pts: S.hl.snap ? [[20, 28], [540, 28]] : pts }], p => p[0], p => p[1], 1);
    else paint(g, [{ type: 'pen', pen: S.pen.type, c: S.pen.color, s: S.pen.size, pts }], p => p[0], p => p[1], 1);
    void id;
  }
}

/* ============================ storage ============================ */
const keyOf = c => 'ink|' + c.deck + '|' + c.code;
export async function loadInk(c) { return (await db.kv.get(keyOf(c))) || { rooms: {}, ov: {}, ts: 0 }; }
export async function saveInk(c, rec) { rec.ts = Date.now(); await db.kv.set(keyOf(c), rec); }
export async function hasInk(c) { const r = await db.kv.get(keyOf(c)); return !!(r && (Object.values(r.rooms || {}).some(x => x.objs && x.objs.length) || Object.values(r.ov || {}).some(x => x.objs && x.objs.length))); }
export const settings = () => S;

/* ============================ pointer handling shared by overlay and rooms ============================ */
// Pen and mouse write; touch scrolls the card. The S Pen side button (buttons & 2) or an eraser end erases while held.
let lastPen = { buttons: 0, button: -1, at: 0 };
const penSignal = () => lastPen.at ? `buttons ${lastPen.buttons} · button ${lastPen.button}` : 'none yet';
const sideButton = e => (e.buttons & 2) || (e.buttons & 32) || e.button === 2 || e.button === 5;
export function attachPointer(surface, opts) {
  const cv = surface.cv; let act = null, holdT = null, hoverSide = false;
  cv.addEventListener('contextmenu', e => { if (opts.writing()) { e.preventDefault(); e.stopPropagation(); } });
  const toEraser = () => { surface.live = null; surface.pred = null; clearTimeout(holdT); act = { erase: true, r: (S.er.size / 2) * opts.unitPerPx() }; };
  const units = e => opts.toUnits(e.clientX, e.clientY);
  const pr = e => (e.pointerType === 'pen' ? (e.pressure || 0.5) : 0.5);
  const eraseAt = (p, r) => {
    const objs = surface.objs; let changed = false;
    for (let i = objs.length - 1; i >= 0; i--) {
      const o = objs[i];
      if (S.er.hlOnly && o.type !== 'hl') continue;
      if (!hits(o, p, r)) continue;
      if (S.er.mode === 'partial' && (o.type === 'pen' || (o.type === 'hl' && !o.snap))) {
        const parts = []; let cur = [];
        for (const q of o.pts) { if (dist(q, p) < r + (o.s || 2) / 2) { if (cur.length > 1) parts.push(cur); cur = []; } else cur.push(q); }
        if (cur.length > 1) parts.push(cur);
        objs.splice(i, 1, ...parts.map(pp => ({ ...o, pts: pp })));
      } else objs.splice(i, 1);
      changed = true;
    }
    return changed;
  };
  cv.addEventListener('pointerdown', e => {
    if (!opts.writing()) return;
    if (e.pointerType === 'touch') { act = { touch: true, y: e.clientY, x: e.clientX }; cv.setPointerCapture(e.pointerId); return; }
    e.preventDefault(); cv.setPointerCapture(e.pointerId);
    if (e.pointerType === 'pen') lastPen = { buttons: e.buttons, button: e.button, at: Date.now() };
    if (opts.onDown) opts.onDown();
    const p = units(e), erasing = sideButton(e) || hoverSide || S.tool === 'er';
    const r = (S.er.size / 2) * opts.unitPerPx();
    if (erasing) { surface.snapshot(); act = { erase: true, r }; if (eraseAt(p, r)) surface.render(); return; }
    if (S.tool === 'lasso') {
      const sel = surface.sel;
      if (sel && sel.box) { const m = opts.map(), cx = m.X(p), cy = m.Y(p); if (cx > sel.box[0] && cx < sel.box[2] && cy > sel.box[1] && cy < sel.box[3]) { surface.snapshot(); act = { move: true, last: p }; return; } }
      surface.sel = null; surface.lasso = [p]; act = { lasso: true }; surface.render(); opts.selChanged(); return;
    }
    if (S.tool === 'text') { opts.textAt(p, e); return; }
    surface.snapshot();
    if (S.tool === 'shape' && S.shape.kind !== 'free') { surface.live = { type: 'shape', kind: S.shape.kind, c: S.pen.color, s: S.pen.size * opts.unitPerPx(), pts: [p, p] }; act = { shape: true }; return; }
    if (S.tool === 'hl') {
      if (S.hl.snap && opts.snapLine) { const line = opts.snapLine(e); if (line) { surface.live = { type: 'hl', snap: true, c: S.hl.color, o: S.hl.op / 100, h: line.h, pts: [[p[0], line.y], [p[0], line.y]] }; act = { snapHl: true }; return; } }
      surface.live = { type: 'hl', c: S.hl.color, s: S.hl.size * opts.unitPerPx(), o: S.hl.op / 100, pts: [p] }; act = { draw: true }; return;
    }
    surface.live = { type: 'pen', pen: S.pen.type, c: S.pen.color, s: S.pen.size * opts.unitPerPx(), pts: [[p[0], p[1], pr(e)]] };
    act = { draw: true, still: Date.now() };
  });
  cv.addEventListener('pointermove', e => {
    if (e.pointerType === 'pen') { if (e.buttons !== lastPen.buttons) lastPen = { buttons: e.buttons, button: e.button, at: Date.now() }; if (!act) hoverSide = !!sideButton(e); }
    if (!act) return;
    // the S Pen side button pressed in the middle of a stroke: switch to the eraser at once
    if (e.pointerType === 'pen' && sideButton(e) && (act.draw || act.shape || act.snapHl)) { if (surface.undo.length) { surface.objs.splice(0, surface.objs.length, ...JSON.parse(surface.undo[surface.undo.length - 1])); } toEraser(); surface.render(); }
    if (act.touch) { opts.scrollBy(act.y - e.clientY); act.y = e.clientY; return; }
    const evs = e.getCoalescedEvents ? e.getCoalescedEvents() : [e];
    if (act.erase) { let ch = false; for (const ev of evs) ch = eraseAt(units(ev), act.r) || ch; if (ch) surface.request(); return; }
    if (act.lasso) { surface.lasso.push(units(e)); surface.request(); return; }
    if (act.move) { const p = units(e), dx = p[0] - act.last[0], dy = p[1] - act.last[1]; act.last = p; act.moved = true; for (const i of surface.sel.ids) surface.objs[i].pts = surface.objs[i].pts.map(q => q.length > 2 ? [q[0] + dx, q[1] + dy, q[2]] : [q[0] + dx, q[1] + dy]); surface.request(); return; }
    if (act.shape) { surface.live.pts[1] = units(e); surface.request(); return; }
    if (act.snapHl) { surface.live.pts[1] = [units(e)[0], surface.live.pts[0][1]]; surface.request(); return; }
    if (act.draw && !act.converted) {
      for (const ev of evs) { const p = units(ev), last = surface.live.pts[surface.live.pts.length - 1]; if (dist(p, last) > 0.4 * opts.unitPerPx()) surface.live.pts.push(surface.live.type === 'pen' ? [p[0], p[1], pr(ev)] : p); }
      surface.pred = e.getPredictedEvents ? e.getPredictedEvents().slice(0, 2).map(units) : null;
      surface.request();
      // auto shape: the timer restarts only when the pen really moves (more than 5 px), so pressure jitter cannot keep resetting it
      if (surface.live.type === 'pen' && S.shape.auto && (S.tool === 'pen' || S.tool === 'shape')) {
        if (!act.hold || Math.hypot(e.clientX - act.hold[0], e.clientY - act.hold[1]) > 5) {
          act.hold = [e.clientX, e.clientY]; clearTimeout(holdT);
          holdT = setTimeout(() => { if (!act || !act.draw || act.converted) return; const sh = recognise(surface.live.pts); if (sh) { surface.live = { type: 'shape', kind: sh.kind, c: surface.live.c, s: surface.live.s, pts: sh.pts, ...(sh.open ? { open: true } : {}) }; surface.pred = null; act.converted = true; surface.render(); if (navigator.vibrate) navigator.vibrate(12); } }, 550);
        }
      }
    }
  });
  const end = () => {
    clearTimeout(holdT); surface.pred = null;
    if (!act) return;
    if (act.lasso) {
      const poly = surface.lasso; surface.lasso = null;
      const [lx0, ly0, lx1, ly1] = bbox(poly), tiny = Math.max(lx1 - lx0, ly1 - ly0) < 12 * opts.unitPerPx();
      let ids;
      if (tiny) { const r = 10 * opts.unitPerPx(); let hit = -1; for (let i = surface.objs.length - 1; i >= 0; i--) if (hits(surface.objs[i], poly[0], r)) { hit = i; break; } ids = hit >= 0 ? [hit] : []; }
      else ids = surface.objs.map((o, i) => { const pts = objPts(o); const inside = pts.filter(q => inPoly(q, poly)).length; return inside / pts.length > 0.5 ? i : -1; }).filter(i => i >= 0);
      surface.sel = ids.length ? { ids } : null; surface.render(); opts.selChanged();
    } else if (surface.live) {
      const o = surface.live; surface.live = null;
      const ok = o.type === 'text' || (o.pts.length > 1 && !(o.type === 'shape' && dist(o.pts[0], o.pts[1]) < 2)) || o.type === 'pen';
      if (ok) surface.objs.push(o); surface.render(); opts.changed(o);
    } else if (act.erase || (act.move && act.moved)) { surface.render(); opts.changed(); }
    act = null;
  };
  cv.addEventListener('pointerup', end); cv.addEventListener('pointercancel', end);
}
export { Surface };
