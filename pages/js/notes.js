// The notebook: one per study page, divided by card. Each card owns a run of pages.
// Back and next flip page by page through the whole notebook, in card order.
import { applyPaper, PAPERS, COLOURS, LAYOUTS } from './paper.js';
import { mountInk } from './ink-mount.js';

export const PW = 820;                       // page width in units; everything is stored in these units
const A4 = Math.round(PW * 1.414);
const uid = () => Math.random().toString(36).slice(2, 9);
const DEF = { paper: 'lines-n', colour: 'cream', layout: 'fixed' };

export class Notebook {
  constructor(host, cards, save) {
    this.host = host; this.cards = cards; this.save = save;
    this.data = { v: 1, defaults: { ...DEF }, cards: {}, ts: 0 };
    this.card = cards[0] && cards[0].id; this.idx = 0; this.zoom = 1; this.ink = null;
    this.build();
  }
  /* ---------- model ---------- */
  cardRec(id) {
    let r = this.data.cards[id];
    if (!r) r = this.data.cards[id] = { layout: this.data.defaults.layout, pages: [] };
    if (!r.pages.length) r.pages.push(this.blank(r.layout));
    return r;
  }
  blank(layout) { const d = this.data.defaults; return { id: uid(), paper: d.paper, colour: d.colour, h: layout === 'flow' ? A4 : A4, objs: [] }; }
  flat() {
    const out = [];
    for (const c of this.cards) {
      const r = this.data.cards[c.id]; if (!r || !r.pages.length) continue;
      r.pages.forEach((p, i) => out.push({ card: c, rec: r, page: p, i, of: r.pages.length }));
    }
    return out;
  }
  here() { const r = this.cardRec(this.card); return { r, p: r.pages[Math.min(this.idx, r.pages.length - 1)] }; }
  /* ---------- moving about ---------- */
  show(cardId, idx) {
    if (cardId) this.card = cardId;
    const r = this.cardRec(this.card);
    this.idx = Math.max(0, Math.min(idx == null ? 0 : idx, r.pages.length - 1));
    this.paint();
  }
  step(d) {
    const all = this.flat();
    if (!all.length) return;
    let at = all.findIndex(x => x.card.id === this.card && x.i === this.idx);
    if (at < 0) at = 0;
    const n = all[Math.max(0, Math.min(at + d, all.length - 1))];
    this.card = n.card.id; this.idx = n.i; this.paint();
  }
  addPage() {
    const { r } = this.here();
    r.pages.splice(this.idx + 1, 0, this.blank(r.layout));
    this.idx++; this.touch(); this.paint();
  }
  delPage() {
    const { r } = this.here();
    if (r.pages.length <= 1) { r.pages[0] = this.blank(r.layout); this.idx = 0; }
    else { r.pages.splice(this.idx, 1); this.idx = Math.max(0, this.idx - 1); }
    this.touch(); this.paint();
  }
  /* ---------- paper, colour, layout ---------- */
  setStyle(part, scope) {                       // scope: page | after | all
    const { r, p } = this.here();
    const set = q => { if (part.paper) q.paper = part.paper; if (part.colour) q.colour = part.colour; };
    if (part.paper) this.data.defaults.paper = part.paper;
    if (part.colour) this.data.defaults.colour = part.colour;
    if (part.layout) this.data.defaults.layout = part.layout;
    if (scope === 'all') {
      for (const id of Object.keys(this.data.cards)) {
        const rec = this.data.cards[id];
        rec.pages.forEach(set);
        if (part.layout) this.relayout(id, part.layout);
      }
    } else if (scope === 'after') {
      set(p);
      if (part.layout) this.relayout(this.card, part.layout);
    } else {
      set(p);
      if (part.layout) this.relayout(this.card, part.layout);
    }
    this.touch(); this.paint();
  }
  // joining and splitting: the writing is kept, shifted by where each page sat
  relayout(cardId, layout) {
    const r = this.data.cards[cardId]; if (!r || r.layout === layout) { if (r) r.layout = layout; return; }
    if (layout === 'flow' && r.pages.length > 1) {
      const breaks = [], objs = []; let y = 0;
      for (const pg of r.pages) {
        breaks.push({ at: y, h: pg.h });
        for (const o of pg.objs) objs.push(shift(o, y));
        y += pg.h;
      }
      r.pages = [{ id: uid(), paper: r.pages[0].paper, colour: r.pages[0].colour, h: y, objs, breaks }];
    } else if (layout === 'fixed' && r.pages.length === 1 && r.pages[0].breaks) {
      const src = r.pages[0], out = [];
      src.breaks.forEach(b => {
        const objs = src.objs.filter(o => mid(o) >= b.at && mid(o) < b.at + b.h).map(o => shift(o, -b.at));
        out.push({ id: uid(), paper: src.paper, colour: src.colour, h: b.h, objs });
      });
      const tail = src.objs.filter(o => mid(o) >= src.breaks.reduce((a, b) => Math.max(a, b.at + b.h), 0));
      if (tail.length) out.push({ id: uid(), paper: src.paper, colour: src.colour, h: A4, objs: tail.map(o => shift(o, -(src.h - A4))) });
      r.pages = out.length ? out : [this.blank('fixed')];
    }
    r.layout = layout; this.idx = 0;
  }
  grow() {
    const { r, p } = this.here();
    if (r.layout !== 'flow') return false;
    let max = 0;
    for (const o of p.objs) for (const q of (o.pts || [])) max = Math.max(max, q[1]);
    if (max > p.h - 160) { p.h = Math.ceil((max + 500) / 100) * 100; return true; }
    return false;
  }
  /* ---------- view ---------- */
  build() {
    this.host.innerHTML =
      '<div class="nb-bar">' +
        '<button class="nbb" data-nb="prev" aria-label="Previous page">\u25c0</button>' +
        '<span class="nb-lab"></span>' +
        '<button class="nbb" data-nb="next" aria-label="Next page">\u25b6</button>' +
        '<span class="nb-sp"></span>' +
        '<button class="nbb" data-nb="add">+ Page</button>' +
        '<button class="nbb ghost" data-nb="del">Delete</button>' +
      '</div>' +
      '<div class="nb-scroll"><div class="nb-stage"><div class="nb-page"></div></div></div>';
    this.scroll = this.host.querySelector('.nb-scroll');
    this.stage = this.host.querySelector('.nb-stage');
    this.pageEl = this.host.querySelector('.nb-page');
    this.lab = this.host.querySelector('.nb-lab');
    this.host.addEventListener('click', e => {
      const b = e.target.closest('[data-nb]'); if (!b) return;
      const a = b.dataset.nb;
      if (a === 'prev') this.step(-1);
      else if (a === 'next') this.step(1);
      else if (a === 'add') this.addPage();
      else if (a === 'del') this.delPage();
    });
    this.ink = mountInk(this.pageEl, {
      width: () => PW,
      height: () => this.here().p.h,
      scroller: () => this.scroll,
      changed: () => { this.sync(); if (this.grow()) this.fit(); this.touch(); }
    });
  }
  sync() { const { p } = this.here(); p.objs = this.ink.objs().slice(); }
  fit() {
    const { p } = this.here();
    this.pageEl.style.width = PW + 'px';
    this.pageEl.style.height = p.h + 'px';
    this.pageEl.style.transform = 'scale(' + this.zoom + ')';
    this.stage.style.width = Math.round(PW * this.zoom) + 'px';
    this.stage.style.height = Math.round(p.h * this.zoom) + 'px';
    this.ink.size();
  }
  paint() {
    const { r, p } = this.here();
    applyPaper(this.pageEl, p.paper, p.colour);
    this.fit();
    this.ink.load(p.objs);
    const c = this.cards.find(x => x.id === this.card);
    this.lab.textContent = (c ? c.label : '') + ' \u00b7 page ' + (this.idx + 1) + ' of ' + r.pages.length;
    this.host.querySelector('[data-nb="del"]').disabled = false;
  }
  setZoom(z) { this.zoom = Math.max(0.4, Math.min(3, z)); this.fit(); }
  getZoom() { return this.zoom; }
  load(data) {
    if (data && data.cards) this.data = Object.assign({ v: 1, defaults: { ...DEF }, cards: {}, ts: 0 }, data);
    this.paint();
  }
  style() { const { r, p } = this.here(); return { paper: p.paper, colour: p.colour, layout: r.layout }; }
  touch() { this.data.ts = Date.now(); this.save(); }
}
function shift(o, dy) {
  const c = JSON.parse(JSON.stringify(o));
  if (c.pts) c.pts = c.pts.map(q => q.length > 2 ? [q[0], q[1] + dy, q[2]] : [q[0], q[1] + dy]);
  if (c.rects) c.rects = c.rects.map(r => [r[0], r[1] + dy, r[2], r[3]]);
  return c;
}
function mid(o) { const q = o.pts || []; return q.length ? q[0][1] : 0; }
