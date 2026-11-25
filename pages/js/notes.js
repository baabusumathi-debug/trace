// The notebook: one per study page, divided by card. Each card owns a run of pages.
// A card's pages sit one below the other and scroll freely; the run ends with a break line,
// and pulling up past that break (and holding) adds a page. ◀ ▶ step page by page through
// the whole notebook in card order.
import { applyPaper } from './paper.js';
import { mountInk, toast } from './ink-mount.js';

export const PW = 820;                       // page width in units; everything is stored in these units
const A4 = Math.round(PW * 1.414);
const GAP = 22;                              // space between pages, in units
const HOLD = 900;                            // ms to hold a pull before it adds a page
const PULL = 30;                             // px the finger must pull past the end
const uid = () => Math.random().toString(36).slice(2, 9);
const DEF = { paper: 'lines-n', colour: 'cream', layout: 'fixed' };
const el = (t, c, h) => { const n = document.createElement(t); if (c) n.className = c; if (h != null) n.innerHTML = h; return n; };

export class Notebook {
  constructor(host, cards, save) {
    this.host = host; this.cards = cards; this.save = save;
    this.data = { v: 2, defaults: { ...DEF }, last: null, cards: {}, trash: [], ts: 0 };
    this.card = cards[0] && cards[0].id; this.idx = 0; this.zoom = 1;
    this.inks = []; this.built = null;
    this.build();
  }
  /* ---------- model ---------- */
  // the style a brand-new page takes: the page it follows, else the last page used, else the defaults
  styleFor(prev) {
    const s = prev || this.data.last || this.data.defaults;
    return { paper: s.paper || DEF.paper, colour: s.colour || DEF.colour };
  }
  blank(prev) { const s = this.styleFor(prev); return { id: uid(), paper: s.paper, colour: s.colour, h: A4, objs: [] }; }
  cardRec(id) {
    let r = this.data.cards[id];
    if (!r) r = this.data.cards[id] = { layout: (this.data.last && this.data.last.layout) || this.data.defaults.layout, pages: [] };
    if (!r.pages.length) r.pages.push(this.blank());
    return r;
  }
  used(p, r) { this.data.last = { paper: p.paper, colour: p.colour, layout: r ? r.layout : this.data.defaults.layout }; }
  flat() {
    const out = [];
    for (const c of this.cards) {
      const r = this.data.cards[c.id]; if (!r || !r.pages.length) continue;
      r.pages.forEach((p, i) => out.push({ card: c, rec: r, page: p, i, of: r.pages.length }));
    }
    return out;
  }
  here() { const r = this.cardRec(this.card); return { r, p: r.pages[Math.min(this.idx, r.pages.length - 1)] }; }
  label(id) { const c = this.cards.find(x => x.id === id); return c ? c.label : id; }

  /* ---------- moving about ---------- */
  show(cardId, idx) {
    if (cardId && cardId !== this.card) { this.card = cardId; this.built = null; }
    const r = this.cardRec(this.card);
    this.idx = Math.max(0, Math.min(idx == null ? 0 : idx, r.pages.length - 1));
    this.paint(); this.scrollToPage(this.idx);
  }
  step(d) {
    const { r } = this.here();
    const i = this.idx + d;
    if (i >= 0 && i < r.pages.length) { this.idx = i; this.scrollToPage(i, true); this.paintLabel(); return; }
    const all = this.flat();
    let at = all.findIndex(x => x.card.id === this.card && x.i === this.idx); if (at < 0) at = 0;
    const n = all[at + d]; if (!n) return;
    this.show(n.card.id, n.i);
  }
  addPage(atEnd) {
    const { r, p } = this.here();
    if (r.layout === 'flow') {                     // one long page: grow it by a sheet
      p.h += A4; this.touch(); this.built = null; this.paint();
      this.scroll.scrollTop = this.scroll.scrollHeight;
      toast('Page grew by one sheet'); return;
    }
    const at = atEnd ? r.pages.length : this.idx + 1;
    r.pages.splice(at, 0, this.blank(r.pages[at - 1]));
    this.idx = at; this.touch(); this.built = null; this.paint(); this.scrollToPage(at);
    toast('Added page ' + (at + 1) + ' of ' + this.label(this.card));
  }
  // deleting: asked first, then kept in the bin so it can come back
  askDelete() {
    const { r } = this.here(), n = this.idx + 1, lab = this.label(this.card);
    const w = el('div', 'sheet-wrap', '<div class="sheet small"><div class="shead"><b>Delete page ' + n + ' of ' + lab + '?</b></div>' +
      '<p class="snote">' + (r.pages[this.idx].objs.length ? 'It has writing on it. ' : '') + 'You can bring it back afterwards: Undo, or Deleted pages in ⚙.</p>' +
      '<div class="sact"><button class="chip" data-a="no">Cancel</button><button class="chip danger" data-a="yes">Delete page</button></div></div>');
    w.addEventListener('click', e => {
      const b = e.target.closest('[data-a]');
      if (e.target === w || (b && b.dataset.a === 'no')) { w.remove(); return; }
      if (b && b.dataset.a === 'yes') { w.remove(); this.delPage(); }
    });
    document.body.appendChild(w);
  }
  delPage() {
    const { r } = this.here(), at = this.idx, page = r.pages[at];
    this.data.trash = [{ card: this.card, at, page, of: r.pages.length, ts: Date.now() }, ...(this.data.trash || [])].slice(0, 30);
    if (r.pages.length <= 1) { r.pages[0] = this.blank(page); this.idx = 0; }
    else { r.pages.splice(at, 1); this.idx = Math.max(0, at - 1); }
    this.touch(); this.built = null; this.paint(); this.scrollToPage(this.idx);
    this.undoBar('Deleted page ' + (at + 1) + ' of ' + this.label(this.card), () => this.restore(this.data.trash[0] && this.data.trash[0].page.id));
  }
  restore(pageId) {
    const t = (this.data.trash || []).findIndex(x => x.page.id === pageId); if (t < 0) return;
    const it = this.data.trash.splice(t, 1)[0];
    const r = this.cardRec(it.card);
    // a card left with one empty page gets its page back in place of the blank
    if (r.pages.length === 1 && !r.pages[0].objs.length && it.of === 1) r.pages[0] = it.page;
    else r.pages.splice(Math.min(it.at, r.pages.length), 0, it.page);
    this.touch();
    this.card = it.card; this.built = null;
    this.idx = r.pages.indexOf(it.page); this.paint(); this.scrollToPage(this.idx);
    toast('Page ' + (this.idx + 1) + ' of ' + this.label(it.card) + ' is back');
  }
  trashList() { return (this.data.trash || []).map(t => ({ id: t.page.id, label: this.label(t.card) + ' · page ' + (t.at + 1), marks: t.page.objs.length, ts: t.ts })); }
  undoBar(text, fn) {
    if (this.ub) this.ub.remove();
    const b = el('div', 'nb-undo', '<span>' + text + '</span><button class="nbb" data-u>Undo</button>');
    b.querySelector('[data-u]').onclick = () => { b.remove(); this.ub = null; fn(); };
    this.bar.after(b); this.ub = b;
    clearTimeout(this.ubT); this.ubT = setTimeout(() => { if (this.ub === b) { b.remove(); this.ub = null; } }, 9000);
  }

  /* ---------- paper, colour, layout ---------- */
  setStyle(part, scope) {                       // scope: page | after | all
    const { r, p } = this.here();
    const set = q => { if (part.paper) q.paper = part.paper; if (part.colour) q.colour = part.colour; };
    if (scope === 'all') {
      Object.assign(this.data.defaults, part);
      for (const id of Object.keys(this.data.cards)) {
        this.data.cards[id].pages.forEach(set);
        if (part.layout) this.relayout(id, part.layout);
      }
    } else if (scope === 'after') {                // this page, the pages after it in this card, and every new page
      Object.assign(this.data.defaults, part);
      r.pages.slice(this.idx).forEach(set);
      if (part.layout) this.relayout(this.card, part.layout);
    } else {                                       // this page only
      set(p);
      if (part.layout) this.relayout(this.card, part.layout);
    }
    this.used(this.here().p, this.here().r);
    this.touch(); this.built = null; this.paint(); this.scrollToPage(this.idx);
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
      const end = src.breaks.reduce((a, b) => Math.max(a, b.at + b.h), 0);
      const tail = src.objs.filter(o => mid(o) >= end);
      if (tail.length) out.push({ id: uid(), paper: src.paper, colour: src.colour, h: Math.max(A4, src.h - end), objs: tail.map(o => shift(o, -end)) });
      r.pages = out.length ? out : [this.blank()];
    }
    r.layout = layout; this.idx = 0;
  }
  grow(p) {
    const { r } = this.here();
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
        '<button class="nbb" data-nb="prev" aria-label="Previous page">◀</button>' +
        '<span class="nb-lab"></span>' +
        '<button class="nbb" data-nb="next" aria-label="Next page">▶</button>' +
        '<span class="nb-sp"></span>' +
        '<button class="nbb" data-nb="add">+ Page</button>' +
        '<button class="nbb ghost" data-nb="del">Delete</button>' +
      '</div>' +
      '<div class="nb-scroll"><div class="nb-stage"><div class="nb-col"></div></div>' +
        '<div class="nb-end"></div>' +
        '<div class="nb-pull"><div class="nb-fill"></div><span class="nb-pt"></span></div>' +
      '</div>';
    this.bar = this.host.querySelector('.nb-bar');
    this.scroll = this.host.querySelector('.nb-scroll');
    this.stage = this.host.querySelector('.nb-stage');
    this.col = this.host.querySelector('.nb-col');
    this.lab = this.host.querySelector('.nb-lab');
    this.endEl = this.host.querySelector('.nb-end');
    this.pullEl = this.host.querySelector('.nb-pull');
    this.host.addEventListener('click', e => {
      const b = e.target.closest('[data-nb]'); if (!b) return;
      const a = b.dataset.nb;
      if (a === 'prev') this.step(-1);
      else if (a === 'next') this.step(1);
      else if (a === 'add') this.addPage(false);
      else if (a === 'del') this.askDelete();
    });
    let raf = 0;
    this.scroll.addEventListener('scroll', () => { if (raf) return; raf = requestAnimationFrame(() => { raf = 0; this.trackPage(); }); }, { passive: true });
    this.pullSetup();
  }
  // which page is in view: the one under a line a third of the way down
  trackPage() {
    if (this.pinching) return;
    const { r } = this.here(); if (!this.tops) return;
    const y = (this.scroll.scrollTop + this.scroll.clientHeight * 0.33 - this.stage.offsetTop) / this.zoom;
    let i = 0; for (let k = 0; k < this.tops.length; k++) if (y >= this.tops[k]) i = k;
    i = Math.min(i, r.pages.length - 1);
    if (i !== this.idx) { this.idx = i; this.paintLabel(); }
  }
  scrollToPage(i, smooth) {
    if (!this.tops) return;
    const y = this.stage.offsetTop + this.tops[i] * this.zoom - 8;
    this.scroll.scrollTo({ top: Math.max(0, y), behavior: smooth ? 'smooth' : 'auto' });
  }
  // the pages of this card, one below the other, each with its own ink
  rebuild() {
    this.inks.forEach(h => h.destroy()); this.inks = [];
    this.col.innerHTML = '';
    const { r } = this.here();
    this.tops = []; let y = 0;
    r.pages.forEach((p, i) => {
      const pe = el('div', 'nb-page'); pe.dataset.i = i;
      pe.style.top = y + 'px'; pe.style.width = PW + 'px'; pe.style.height = p.h + 'px';
      applyPaper(pe, p.paper, p.colour);
      this.col.appendChild(pe);
      const h = mountInk(pe, {
        width: () => PW, height: () => p.h, scroller: () => this.scroll,
        changed: () => {
          p.objs = h.objs().slice(); this.used(p, r);
          if (this.grow(p)) { this.built = null; this.paint(); }
          this.touch();
        }
      });
      h.load(p.objs);
      this.inks.push(h);
      this.tops.push(y); y += p.h + GAP;
    });
    this.colH = y - GAP;
    this.built = this.card + ':' + r.pages.map(p => p.id + p.h).join(',');
  }
  fit() {
    if (!this.colH) return;
    this.col.style.width = PW + 'px';
    this.col.style.height = this.colH + 'px';
    this.col.style.transform = 'scale(' + this.zoom + ')';
    this.stage.style.width = Math.round(PW * this.zoom) + 'px';
    this.stage.style.height = Math.round(this.colH * this.zoom) + 'px';
  }
  paint() {
    const { r } = this.here();
    const sig = this.card + ':' + r.pages.map(p => p.id + p.h).join(',');
    if (this.built !== sig) this.rebuild();
    this.fit();
    this.paintLabel();
    const lab = this.label(this.card), n = r.pages.length;
    this.endEl.innerHTML = '<span>End of ' + esc(lab) + ' · ' + (r.layout === 'flow' ? 'one long page' : n + ' page' + (n === 1 ? '' : 's')) + '</span>';
    this.pullReset();
  }
  paintLabel() {
    const { r } = this.here();
    this.lab.textContent = this.label(this.card) + ' · page ' + (this.idx + 1) + ' of ' + r.pages.length;
  }

  /* ---------- pull past the end and hold: a new page ---------- */
  pullText(t) { this.pullEl.querySelector('.nb-pt').textContent = t; }
  pullReset() {
    const { r } = this.here();
    this.pullEl.classList.remove('live', 'ready');
    this.pullEl.querySelector('.nb-fill').style.width = '0';
    this.pullText(r.layout === 'flow' ? '↑ Pull up and hold to make this page longer' : '↑ Pull up and hold to add page ' + (r.pages.length + 1));
  }
  pullSetup() {
    let g = null, raf = 0;
    const atEnd = () => this.scroll.scrollTop + this.scroll.clientHeight >= this.scroll.scrollHeight - 4;
    const tick = () => {
      raf = 0; if (!g || !g.t) return;
      const k = Math.min(1, (performance.now() - g.t) / HOLD);
      this.pullEl.querySelector('.nb-fill').style.width = (k * 100).toFixed(1) + '%';
      if (k >= 1 && !g.ready) {
        g.ready = true; this.pullEl.classList.add('ready');
        this.pullText('Let go to add the page'); if (navigator.vibrate) navigator.vibrate(15);
      }
      if (!g.ready) raf = requestAnimationFrame(tick);
    };
    const stop = () => { if (raf) cancelAnimationFrame(raf); raf = 0; if (g) { g.t = 0; g.ready = false; } this.pullReset(); };
    this.scroll.addEventListener('touchstart', e => { g = e.touches.length === 1 ? { y0: null, t: 0, ready: false } : null; if (!g) stop(); }, { passive: true });
    this.scroll.addEventListener('touchmove', e => {
      if (!g) return;
      if (e.touches.length !== 1) { stop(); g = null; return; }
      const y = e.touches[0].clientY;
      if (!atEnd()) { if (g.t) stop(); g.y0 = null; return; }
      if (g.y0 == null || y > g.y0) { g.y0 = y; }          // the end was just reached: pulling counts from here
      const d = g.y0 - y;
      if (d > PULL) {
        if (!g.t) { g.t = performance.now(); this.pullEl.classList.add('live'); this.pullText('Keep holding…'); raf = requestAnimationFrame(tick); }
      } else if (g.t && d < PULL / 2) stop();
    }, { passive: true });
    const end = () => { const ok = g && g.ready; stop(); g = null; if (ok) this.addPage(true); };
    this.scroll.addEventListener('touchend', end);
    this.scroll.addEventListener('touchcancel', () => { stop(); g = null; });
  }

  /* ---------- zoom: live while the fingers move, settled when they lift ---------- */
  setZoom(z) { this.zoom = Math.max(0.4, Math.min(3, z)); this.fit(); }
  getZoom() { return this.zoom; }
  pinchStart(fx, fy) {
    this.pinching = true;
    const s = this.scroll;
    this.pz = { z0: this.zoom, cx: (s.scrollLeft + fx - this.stage.offsetLeft) / this.zoom, cy: (s.scrollTop + fy - this.stage.offsetTop) / this.zoom };
  }
  pinchTo(z, fx, fy) {
    if (!this.pz) this.pinchStart(fx, fy);
    this.zoom = Math.max(0.4, Math.min(3, z));
    this.col.style.transform = 'scale(' + this.zoom + ')';
    this.stage.style.width = Math.round(PW * this.zoom) + 'px';
    this.stage.style.height = Math.round(this.colH * this.zoom) + 'px';
    this.scroll.scrollLeft = this.pz.cx * this.zoom + this.stage.offsetLeft - fx;
    this.scroll.scrollTop = this.pz.cy * this.zoom + this.stage.offsetTop - fy;
  }
  pinchEnd() { this.pinching = false; this.pz = null; this.fit(); this.trackPage(); }

  load(data) {
    if (data && data.cards) this.data = Object.assign({ v: 2, defaults: { ...DEF }, last: null, cards: {}, trash: [], ts: 0 }, data);
    this.built = null; this.paint();
  }
  style() { const { r, p } = this.here(); return { paper: p.paper, colour: p.colour, layout: r.layout }; }
  touch() { this.data.ts = Date.now(); this.save(); }
}
function esc(s) { return String(s).replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c])); }
function shift(o, dy) {
  const c = JSON.parse(JSON.stringify(o));
  if (c.pts) c.pts = c.pts.map(q => q.length > 2 ? [q[0], q[1] + dy, q[2]] : [q[0], q[1] + dy]);
  if (c.rects) c.rects = c.rects.map(r => [r[0], r[1] + dy, r[2], r[3]]);
  return c;
}
function mid(o) { const q = o.pts || []; return q.length ? q[0][1] : 0; }
