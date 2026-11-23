// ==UserScript==
// @name         Trace · DocT recorder
// @namespace    trace
// @version      2.9
// @description  Records your own DocT QBank and GT attempts and reviews (time per question, answer, key, cohort %, explanation, images, guess flags) for Trace.
// @match        https://*.doctutorials.com/*
// @match        https://doctutorials.com/*
// @grant        GM_registerMenuCommand
// @grant        GM_unregisterMenuCommand
// @grant        GM_getValue
// @grant        GM_setValue
// @grant        GM_download
// @grant        GM_xmlhttpRequest
// @connect      script.google.com
// @connect      script.googleusercontent.com
// @connect      cloudfront.net
// @connect      doctutorials.com
// @run-at       document-start
// ==/UserScript==

/*
  Passive: it only reads the page. It never clicks, types, or changes anything DocT shows.
  Shortcuts (Control, not Cmd):
    Control+Shift+G  mark / unmark the current question as a guess
    Control+Shift+Y  save a raw page snapshot (for building new screens)
  Leaving the review (or closing the tab) saves *_review_<n>of<total>.json if anything new was captured.
  Images are remembered across sessions and never downloaded twice.
  Guesses / marked-for-review: in review, tick DocT's "Guessed Right", "Guessed Wrong" or
  "Marked for Review" filter and step through; every question seen while it is ticked gets that flag.
  Review: a label at bottom-left shows each question's state and the count saved.
  A question counts once its correct answer is read; the explanation is saved too
  when DocT shows one. When all are saved, *_review.json downloads by itself.
  Images in a question or its explanation are downloaded automatically,
  once each, as trace_img_<MCQID>_<where>_<n>.<ext>.
  Recording switch (menu): turns QBank recording on/off. Test-series (GT) pages always record.
  Attempts: each question remembers how many times you have solved it (attempt 1, 2, 3…).
  Mark a line: select text in an explanation, then menu > Mark selected line (or Control+Shift+M
  where DocT lets shortcuts through). Saved with that question.
  QBank learning mode (answers shown, nothing to solve) is captured like a review.
  Live screens are detected generically (question number + options), so new GT layouts
  are likely covered; a live attempt is saved as *_attempt_<n>of<total>.json when you leave it.
  v2.3: in review, ticking only Skipped reads the Skipped list (like Wrong), so skipped questions become repairs.
  v2.5: Wrong and Skipped ticked together also works (Skipped = the grid minus the Wrong list already read);
  a note flashes the filters the recorder sees ticked.
  v2.7: leaving a review that was already sent says "nothing new · already sent" and switches recording Off.
  v2.8: that only applies to the same person; a review by the other person (HT, then you) always starts its own session,
  saved under that person.
  v2.9: (1) sectional GTs: the current section is the last unlocked "Section X" tab (DocT keeps finished sections
  marked active, so v2.8 read every section as A and sections B and C overwrote A's records).
  (2) switching Mode no longer relabels a review that is already captured; it only relabels an unfinished live attempt.
  (3) in a review, a question showing the key and no wrong mark clears any wrong mark left from an earlier session.
  (4) several list filters ticked one after another (e.g. Wrong, then Guessed Right) each get their own list:
  the newly ticked one is the grid minus the lists already read.
  Menu (Tampermonkey icon > this script > ›):
    Recording · Mark selected line · Save session file now · Start a fresh session · Save page snapshot
*/

(function () {
  'use strict';

  const KEY = 'trace_doct_session';
  const IMGKEY = 'trace_doct_images_seen';
  const VERSION = '2.9';
  const TITLEKEY = 'trace_doct_last_title';
  const RECKEY = 'trace_doct_recording';
  const SEENKEY = 'trace_doct_attempts';
  // v2.0: one recording mode chosen before each sitting; finished attempts go straight to Trace (Drive › Trace › doct)
  const MODEKEY = 'trace_doct_mode';          // off | trace | ht | htreview
  const CONNKEY = 'trace_doct_conn';          // { u, k } from the private setup link; kept only in Tampermonkey's storage
  const FOLDKEY = 'trace_doct_folder';
  const TRACE_FOLDER = '1e_lx6kl_MhG4aOracgTr_HG3NUp7OsYs', DOCT_FOLDER = '1wqRbRG-nqldfafFL-AughcBEBfo6atQo';
  const MODES = { off: 'Off', trace: 'Trace solving', ht: 'HT solving', htreview: 'HT review' };
  const getMode = () => { const m = GM_getValue(MODEKEY, 'off'); return MODES[m] ? m : 'off'; };

  // ---------- page reading (pure functions, no side effects) ----------
  const txt = (el) => (el ? (el.innerText || el.textContent || '').replace(/​/g, '').trim() : '');

  function findText(re) {
    const els = document.querySelectorAll('p, h6, h5, div, span');
    for (const el of els) {
      if (el.children.length > 2) continue;
      const m = txt(el).match(re);
      if (m) return m;
    }
    return null;
  }

  function mode() {
    const body = txt(document.body);
    if (/\/question-bank\/review/.test(location.pathname) && /Total MCQs/.test(body)) return 'result';
    if (/Filters/.test(body) && /All \(\d+\)/.test(body)) return 'review';
    if (/Not Visited/.test(body) && /Overview/.test(body)) return 'live';
    // QBank learning mode: answer + explanation already shown, no options to pick, no filters
    if (findText(/^Question\s+\d+\s*\/\s*\d+$/) && findText(/^MCQID:/) && !document.querySelector('input[type="radio"]') &&
        (/answered this correctly/.test(body) || document.querySelector('svg[data-testid="CheckCircleIcon"]'))) return 'learn';
    // generic: a question header with selectable options (covers GT layouts not seen yet)
    if (findText(/^Question\s+\d+\s*\/\s*\d+$/) && document.querySelector('input[type="radio"]')) return 'live';
    return 'other';
  }

  function readQuestion() {
    const q = findText(/^Question\s+(\d+)\s*\/\s*(\d+)$/);
    const id = findText(/^MCQID:\s*(\S+)$/);
    if (!q) return null;
    // sectional GTs: "Section A/B/C" tabs, numbering restarts at 1 in each section, no MCQID shown live
    // v2.9: DocT keeps finished sections marked "active", so take the last unlocked active tab (A, then B, then C)
    const secBtns = [...document.querySelectorAll('button')].filter((b) => /^Section\s+[A-Z]$/.test(txt(b)));
    const selBtn = secBtns.find((b) => b.getAttribute('aria-selected') === 'true' || /\bMui-selected\b/.test(b.className));
    const openBtns = secBtns.filter((b) => /\bactive\b/.test(b.className) && !b.querySelector('svg[data-testid="LockIcon"]') && !b.disabled);
    const secBtn = selBtn || openBtns[openBtns.length - 1] || null;
    const section = secBtn ? txt(secBtn).slice(-1) : null;
    const liveId = (section || 'Q') + String(+q[1]).padStart(3, '0');
    const out = { qno: +q[1], total: +q[2], mcqid: id ? id[1] : liveId, no_mcqid: !id, section,
                  global_no: section ? (section.charCodeAt(0) - 65) * (+q[2]) + (+q[1]) : +q[1], stem: '', options: [], correct: null, marked_wrong: null, cohort_pct: null, explanation: '', references: '' };

    const form = document.querySelector('form');
    if (form) {
      const ft = txt(form);
      const cut = ft.search(/(^|\n|\s)A\)\s/);
      out.stem = (cut > 0 ? ft.slice(0, cut) : ft).trim();
    }
    // options: leaf elements whose text starts "A) " … "E) "
    const optEls = [...(form || document).querySelectorAll('div, span')].filter((el) => {
      const t = txt(el);
      return /^[A-E]\)\s/.test(t) && ![...el.querySelectorAll('div, span')].some((c) => /^[A-E]\)\s/.test(txt(c)));
    });
    const seen = new Set();
    for (const el of optEls) {
      const letter = txt(el)[0];
      if (seen.has(letter)) continue;
      seen.add(letter);
      out.options.push(txt(el));
      const row = el.closest('label') || el.parentElement;
      const icon = row && row.querySelector('svg[data-testid]');
      const tid = icon && icon.getAttribute('data-testid');
      if (tid === 'CheckCircleIcon') out.correct = letter;
      if (tid === 'CancelIcon') out.marked_wrong = letter;
    }
    // images inside the question (stem/options) and the explanation block
    out.images = [];
    const okImg = (img) => img.src && /^https?:/.test(img.src) && !/logo|\/assets\/|adsct|analytics|twitter|t\.co\/|facebook|google/i.test(img.src) &&
      img.alt !== 'Reference' && img.alt !== 'Profile Picture' && (img.naturalWidth || img.width || 100) >= 40;
    if (form) form.querySelectorAll('img').forEach((img) => { if (okImg(img)) out.images.push({ where: 'question', src: img.src }); });
    // explanation images: anything between the "% answered this correctly" line (or the options)
    // and "Feedback/Report Error" in page order — works whatever heading the explanation uses
    const startEl = [...document.querySelectorAll('p')].find((el) => /answered this correctly$/.test(txt(el))) ||
                    (form ? form : null);
    const endEl = [...document.querySelectorAll('p')].find((el) => /^Feedback\/Report Error$/.test(txt(el)));
    const seenSrc = new Set(out.images.map((x) => x.src));
    if (startEl) document.querySelectorAll('img').forEach((img) => {
      if (!okImg(img) || seenSrc.has(img.src)) return;
      if (form && form.contains(img)) return;
      const afterStart = startEl.compareDocumentPosition(img) & Node.DOCUMENT_POSITION_FOLLOWING;
      const beforeEnd = !endEl || (endEl.compareDocumentPosition(img) & Node.DOCUMENT_POSITION_PRECEDING);
      if (afterStart && beforeEnd) { out.images.push({ where: 'explanation', src: img.src }); seenSrc.add(img.src); }
    });
    const c = findText(/^(\d+)%\s+answered this correctly$/);
    if (c) out.cohort_pct = +c[1];
    // live state: DocT's own "Guess Answer" box and the option currently selected
    const gLab = [...document.querySelectorAll('label')].find((l) => /^Guess Answer$/.test(txt(l)));
    if (gLab) { const gi = gLab.querySelector('svg[data-testid]'); out.live_guess = !!gi && gi.getAttribute('data-testid') === 'CheckBoxIcon'; }
    const chk = document.querySelector('input[type="radio"]:checked');
    if (chk) { const l = chk.closest('label'); const lm = l && txt(l).match(/^([A-E])\)/); out.live_selected = lm ? lm[1] : ('ABCDE'[+chk.value] || chk.value); }
    else if (document.querySelector('input[type="radio"]')) out.live_selected = null;

    // explanation = everything after the cohort line (or the last option) up to References / Feedback
    const body = txt(document.body);
    let start = -1;
    const cm = body.match(/\d+%\s+answered this correctly/);
    if (cm) start = cm.index + cm[0].length;
    else if (out.options.length) {
      const lastOpt = out.options[out.options.length - 1];
      const i = body.indexOf(lastOpt.slice(0, 40));
      if (i >= 0) start = i + lastOpt.length;
    }
    // only once the answer is revealed (otherwise this region is navigation, not a solution)
    if (start >= 0 && (cm || out.correct)) {
      const rest = body.slice(start);
      const mRef = rest.indexOf('References');
      const mFb = rest.indexOf('Feedback/Report Error');
      const ends = [mRef, mFb].filter((x) => x >= 0);
      const end = ends.length ? Math.min(...ends) : Math.min(rest.length, 8000);
      const ex = rest.slice(0, end).trim().replace(/^Explanation\s*:?\s*/i, '');
      if (ex.length >= 20) out.explanation = ex;
      if (mRef >= 0) {
        const after = rest.slice(mRef + 'References'.length);
        const fb = after.indexOf('Feedback/Report Error');
        out.references = (fb >= 0 ? after.slice(0, fb) : after.slice(0, 600)).trim();
      }
    }
    return out;
  }

  function readResult() {
    const tm = [...document.querySelectorAll('p')].find((p) => /^Total MCQs/.test(txt(p)));
    const box = tm && tm.parentElement;
    const h = box && box.querySelector('h6');
    const body = txt(document.body);
    const g = (re) => { const m = body.match(re); return m ? m[1] : null; };
    return {
      module: txt(h),
      total_mcqs: g(/Total MCQs:\s*(\d+)/),
      correct: g(/(?:^|\s)(\d+)\s+Correct/m),
      incorrect: g(/(?:^|\s)(\d+)\s+Incorrect/m),
      skipped: g(/(?:^|\s)(\d+)\s+Skipped/m),
      total_time: g(/(\d{2}:\d{2}:\d{2})\s*\n?\s*Total Time/),
    };
  }

  // review filters (GT and QBank): which are ticked, their counts, and the paper name
  const FILTERS = ['All', 'Bookmarked', 'Correct', 'Wrong', 'Skipped', 'Marked for Review', 'Guessed Right', 'Guessed Wrong'];
  function readFilters() {
    const out = { active: [], counts: {}, paper: null, paper_total: null };
    document.querySelectorAll('label').forEach((lab) => {
      const m = txt(lab).match(/^(.+?)\s*\((\d+)\)$/);
      if (!m) return;
      const name = m[1].trim(), n = +m[2];
      const icon = lab.querySelector('svg[data-testid]');
      const on = !!icon && /^CheckBox(Icon)?$/.test(icon.getAttribute('data-testid'));
      if (FILTERS.includes(name)) { out.counts[name] = n; if (on && name !== 'All') out.active.push(name); }
      else if (!out.paper) { out.paper = name; out.paper_total = n; }
    });
    return out;
  }

  // review: the Questions grid beside the filters lists the original question numbers that the active filter shows
  function readGrid() {
    const h = [...document.querySelectorAll('h6, p, span')].find((e) => txt(e) === 'Questions' && !e.children.length);
    if (!h || !h.parentElement) return null;
    const box = h.parentElement.nextElementSibling || h.parentElement.parentElement;
    const nums = [...box.querySelectorAll('button p, button')].map((b) => txt(b)).filter((x) => /^\d{1,3}$/.test(x)).map(Number);
    return [...new Set(nums)];
  }

  // module / paper name from the card you click on DocT's QBank or Test Series list
  function nameFromCard(el) {
    for (let n = el, i = 0; n && i < 12; n = n.parentElement, i++) {
      const t = txt(n);
      const leaves = [...n.querySelectorAll('span, p, b')].filter((x) => !x.querySelector('span, p, b')).map(txt);
      const qb = leaves.filter((x) => /^(?:\d+\s*\/\s*)?\d+\s*MCQ'?s$/i.test(x));
      const gt = leaves.filter((x) => /^\d+\s*Questions$/i.test(x));
      if ((qb && qb.length > 1) || (gt && gt.length > 1)) return null;   // climbed past a single card
      if (qb && qb.length === 1) {
        const titled = n.querySelector('[title]');
        const name = titled ? titled.getAttribute('title') : t.split('\n')[0];
        const total = +(qb[0].match(/(\d+)\s*MCQ/i) || [])[1] || null;
        return { name: name.trim(), total, kind: 'qbank' };
      }
      if (gt && gt.length === 1) {
        const first = [...n.querySelectorAll('p')].find((x) => !/^\d+\s*(Questions|min)$/i.test(txt(x)) && txt(x).length > 3);
        return { name: txt(first) || t.split('\n')[0], total: +gt[0].match(/\d+/)[0], kind: 'gt' };
      }
    }
    return null;
  }

  // expose readers for testing only
  if (typeof window !== 'undefined') window.__traceDocT = { readQuestion, readResult, mode, readFilters, nameFromCard };

  // ---------- recording ----------
  if (typeof GM_getValue !== 'function') return; // test harness: readers only

  const now = () => Date.now();
  let S = GM_getValue(KEY, null);
  let cur = null;          // { mcqid, since }
  let dirty = false;

  function fresh() {
    const m = getMode();
    return { v: VERSION, started: new Date().toISOString(), url: location.href, module: null, result: null, saved: false, questions: {}, log: [], who: m === 'trace' ? 'Trace' : 'HT', rmode: m };
  }
  function save() { if (dirty) { GM_setValue(KEY, S); dirty = false; } }
  setInterval(save, 3000);
  window.addEventListener('pagehide', () => { closeCurrent(); save(); });
  window.addEventListener('beforeunload', () => {
    if (typeof liveDirty !== 'undefined' && liveDirty) saveAttempt();
    if (typeof reviewDirty !== 'undefined' && reviewDirty && S) {
      const done = Object.values(S.questions).filter((x) => x.correct).length;
      download('_review_' + done + 'of' + (S.total || '?')); reviewDirty = false;
    }
  });

  function rec(id) {
    if (!S.questions[id]) S.questions[id] = { mcqid: id, qno: null, ms: 0, visits: 0, chosen: null, changes: 0, guess: false, answered_at_ms: null };
    return S.questions[id];
  }
  function closeCurrent() {
    if (cur && S) {
      if (!document.hidden) rec(cur.mcqid).ms += now() - cur.since;
      S.log.push({ t: now(), ev: 'leave', id: cur.mcqid });
      cur = null; dirty = true;
    }
  }
  // small corner label, shown only on the review screen (after you have submitted)
  let badgeEl = null;
  function badge(text) {
    if (!text) { if (badgeEl) { badgeEl.remove(); badgeEl = null; } return; }
    if (!badgeEl || !badgeEl.isConnected) {
      badgeEl = document.createElement('div');
      badgeEl.setAttribute('style', 'position:fixed;left:12px;bottom:12px;z-index:2147483647;background:rgba(20,20,20,.88);color:#9fe3b0;font:12px/1.3 -apple-system,system-ui,sans-serif;padding:6px 10px;border-radius:8px;pointer-events:none;border:1px solid #2f6b44');
      document.documentElement.appendChild(badgeEl);
    }
    if (badgeEl.textContent !== text) badgeEl.textContent = text;
  }
  function flash(msg) {
    const old = document.title.replace(/^\[.*?\]\s/, '');
    document.title = '[' + msg + '] ' + old;
    setTimeout(() => { document.title = old; }, 1500);
  }

  document.addEventListener('visibilitychange', () => {
    if (!cur) return;
    if (document.hidden) { rec(cur.mcqid).ms += now() - cur.since; cur.since = now(); }
    else cur.since = now();
    dirty = true;
  });

  // your answer, straight from the radio you click
  document.addEventListener('change', (e) => {
    const t = e.target;
    if (!t || t.type !== 'radio' || !cur || !recording()) return;
    const lab = t.closest('label');
    const lm = lab && txt(lab).match(/^([A-E])\)/);
    const letter = lm ? lm[1] : ('ABCDE'[+t.value] || t.value);
    const r = rec(cur.mcqid);
    if (r.chosen && r.chosen !== letter) r.changes++;
    r.chosen = letter;
    r.answered_at_ms = r.ms + (document.hidden ? 0 : now() - cur.since);
    S.log.push({ t: now(), ev: 'answer', id: cur.mcqid, a: letter });
    dirty = true; liveDirty = true;
  }, true);

  // remember which module / GT you opened from the list (just reads the card you clicked)
  document.addEventListener('click', (e) => {
    if (!/\/question-bank\/topics|\/test-series\/test\//.test(location.pathname)) return;
    const info = nameFromCard(e.target);
    if (info && info.name) GM_setValue(TITLEKEY, { name: info.name, total: info.total, kind: info.kind, t: now(), from: 'list' });
  }, true);

  window.addEventListener('keydown', (e) => {
    if (!e.ctrlKey || !e.shiftKey) return;
    const k = (e.key || '').toLowerCase();
    if (k === 'g' && cur) {
      e.preventDefault(); e.stopPropagation();
      const r = rec(cur.mcqid); r.guess = !r.guess; dirty = true;
      flash(r.guess ? 'guess ✓' : 'guess ✗');
    } else if (k === 'y') {
      e.preventDefault(); e.stopPropagation(); snapshot();
    } else if (k === 'm') {
      e.preventDefault(); e.stopPropagation(); markLine();
    }
  }, true);

  const isTest = () => /\/test-series\//.test(location.pathname);
  const recording = () => getMode() !== 'off';
  let lastQid = null, liveDirty = false;

  function markLine() {
    const sel = String(window.getSelection ? window.getSelection() : '').replace(/\s+/g, ' ').trim();
    const id = (cur && cur.mcqid) || lastQid;
    if (!sel) { flash('Trace: select text first'); return; }
    if (!id || !S) { flash('Trace: no question open'); return; }
    const r = rec(id); r.marked_lines = r.marked_lines || [];
    if (!r.marked_lines.includes(sel)) { r.marked_lines.push(sel); dirty = true; reviewDirty = true; save(); }
    flash('line marked (' + r.marked_lines.length + ')');
    if (badgeEl) badge(badgeEl.textContent.replace(/ · \d+ line\(s\) marked$/, '') + ' · ' + r.marked_lines.length + ' line(s) marked');
  }

  function applyTitle(total, kind) {
    if (!S || S.module) return;
    const lt = GM_getValue(TITLEKEY, null);
    if (!lt || now() - lt.t > 4 * 3600 * 1000) return;
    if (lt.total && total && lt.total !== total && !(kind === 'gt' && lt.kind === 'gt')) return;
    S.module = lt.name; dirty = true;
  }

  function saveAttempt() {
    if (!S || !liveDirty) return;
    liveDirty = false; closeCurrent(); save();
    const answered = Object.values(S.questions).filter((x) => x.chosen).length;
    download('_attempt_' + answered + 'of' + (S.total || '?'));
  }

  const pauseShown = {}; let pauseTimer = null;
  let lastMode = null, reviewDirty = false, lastFilters = '', lastGridWarn = '';
  function noteModulePage() {
    // QBank module page (Learning Mode / Solve / Previous Attempts): name is in the address
    const mm = location.pathname.match(/\/question-bank\/subject-details\/([^/]+)/);
    if (!mm) return;
    let name; try { name = decodeURIComponent(mm[1]).trim(); } catch (e) { return; }
    const tm = txt(document.body).match(/(\d+)\s*MCQs/);
    const lt = GM_getValue(TITLEKEY, null);
    if (!lt || lt.name !== name || now() - lt.t > 60000)
      GM_setValue(TITLEKEY, { name, total: tm ? +tm[1] : null, kind: 'qbank', t: now(), from: 'module page' });
  }

  function isRev(x) { return x === 'review' || x === 'learn'; }   // (was a const declared after its first use: threw while recording was off)
  function tick() {
    noteModulePage();
    const m = mode();
    if (lastMode === 'live' && m !== 'live' && m !== 'result') saveAttempt();
    if (!recording() && (m === 'live' || isRev(m) || m === 'result')) {
      closeCurrent();
      // remind briefly once per screen type (solving / review / result), not on every question
      if (m !== lastMode && !pauseShown[m]) {
        pauseShown[m] = true;
        badge('⏸ Trace: recording is Off · menu › Mode');
        clearTimeout(pauseTimer); pauseTimer = setTimeout(() => { pauseTimer = null; badge(null); }, 4000);
      }
      lastMode = m;
      return;
    }
    if (isRev(lastMode) && !isRev(m) && reviewDirty && S) {
      const done = Object.values(S.questions).filter((x) => x.correct).length;
      reviewDirty = false; save();
      download('_review_' + done + 'of' + (S.total || '?'));
    } else if (isRev(lastMode) && !isRev(m) && S && S.saved && getMode() !== 'off' && S.who === (getMode() === 'trace' ? 'Trace' : 'HT')) {
      // v2.7: re-opening a review that was already sent adds nothing; say so and still switch recording Off
      GM_setValue(MODEKEY, 'off'); modeUI();
      flash('Trace: nothing new · this review was already sent · recording now Off');
    }
    lastMode = m;
    if (!isRev(m) && !pauseTimer) badge(null);
    if (m === 'live') {
      const q = readQuestion();
      if (!q) return;
      const last = S && S.log.length ? S.log[S.log.length - 1].t : 0;
      const stale = S && (now() - last > 2 * 3600 * 1000 || (S.total && S.total !== q.total));
      // a new attempt (or a different paper) never continues an old session
      const ltL = GM_getValue(TITLEKEY, null);
      const otherPaper = S && S.module && ltL && now() - ltL.t < 6 * 3600 * 1000 && ltL.name !== S.module;
      const afterReview = S && (S.review_saved || S.review_only || S.mode === 'learn');
      if (!S || S.saved || stale || otherPaper || afterReview) { closeCurrent(); S = fresh(); cur = null; dirty = true; liveDirty = false; }
      if (!cur || cur.mcqid !== q.mcqid) {
        closeCurrent();
        cur = { mcqid: q.mcqid, since: now() };
        const r = rec(q.mcqid); r.visits++; r.qno = q.qno; S.total = q.total;
        S.counted = S.counted || {};
        if (!S.counted[q.mcqid]) {
          const seenIds = GM_getValue(SEENKEY, {});
          seenIds[q.mcqid] = (seenIds[q.mcqid] || 0) + 1; GM_setValue(SEENKEY, seenIds);
          r.attempt = seenIds[q.mcqid]; S.counted[q.mcqid] = 1;
        }
        if (isTest()) S.kind = 'gt';
        applyTitle(S.sectional ? null : q.total, isTest() ? 'gt' : 'qbank');
        S.log.push({ t: now(), ev: 'enter', id: q.mcqid, n: q.qno });
        dirty = true;
      }
      lastQid = q.mcqid;
      const r0 = rec(q.mcqid);
      if (q.section) { r0.section = q.section; r0.global_no = q.global_no; S.sectional = true; }
      if (q.live_guess !== undefined && r0.guess !== q.live_guess) { r0.guess = q.live_guess; r0.guess_source = 'doct'; dirty = true; liveDirty = true; }
      if (q.live_selected !== undefined && r0.chosen !== q.live_selected) {
        if (r0.chosen && q.live_selected && r0.chosen !== q.live_selected) r0.changes++;
        if (r0.chosen && !q.live_selected) r0.cleared = (r0.cleared || 0) + 1;
        r0.chosen = q.live_selected; dirty = true; liveDirty = true;
      }
      merge(q);
    } else if (isRev(m)) {
      closeCurrent();
      const q = readQuestion();
      if (!q) return;
      if (m === 'learn') {
        // new learning session when a different module starts (or after a review/test session)
        if (!S || S.mode !== 'learn' || S.total !== q.total || (q.qno === 1 && !S.questions[q.mcqid])) { S = fresh(); S.mode = 'learn'; S.review_only = true; dirty = true; }
        applyTitle(q.total, 'qbank');
      }
      const F0 = m === 'learn' ? { active: [], counts: {} } : readFilters();
      const fullTotal = F0.counts.All || q.total;
      const ltNow = m === 'learn' ? null : GM_getValue(TITLEKEY, null);
      const otherModule = S && S.module && ltNow && now() - ltNow.t < 6 * 3600 * 1000 && ltNow.name !== S.module && !S.questions[q.mcqid];
      // v2.8: a review by the other person (HT, then Trace, or back) never continues the first person's session
      const who = getMode() === 'trace' ? 'Trace' : 'HT', otherPerson = S && S.who && S.who !== who;
      if (!S || (S.total && S.total !== fullTotal) || otherModule || otherPerson) { S = fresh(); S.review_only = true; dirty = true; }
      S.total = fullTotal;
      if (!S.module && m !== 'learn') {
        const lt = GM_getValue(TITLEKEY, null);
        if (lt && now() - lt.t < 6 * 3600 * 1000 && (!lt.total || lt.total === fullTotal)) { S.module = lt.name; dirty = true; }
      }
      const hadEx = !!(S.questions[q.mcqid] && S.questions[q.mcqid].explanation);
      const had = !!(S.questions[q.mcqid] && S.questions[q.mcqid].correct);
      const r = rec(q.mcqid); r.qno = q.qno;
      if (r.attempt == null && r.prior_attempts == null) { r.prior_attempts = GM_getValue(SEENKEY, {})[q.mcqid] || 0; dirty = true; }
      if (isTest()) S.kind = 'gt';
      lastQid = q.mcqid;
      const imgBefore = (r.images || []).length;
      merge(q);
      // v2.9: key shown and no wrong mark = this person did not get it wrong; clear a mark left from another session
      if (q.correct && !q.marked_wrong && r.marked_wrong) { r.marked_wrong = null; dirty = true; reviewDirty = true; }
      if ((r.images || []).length > imgBefore) reviewDirty = true;
      const F = m === 'learn' ? { active: [], counts: {}, paper: null } : readFilters();
      if (!S.module) applyTitle(fullTotal, isTest() ? 'gt' : 'qbank');
      if (F.paper && !S.module) { S.module = F.paper; dirty = true; }
      if (F.paper) S.paper_group = F.paper;
      if (JSON.stringify(S.filter_counts) !== JSON.stringify(F.counts)) { S.filter_counts = F.counts; dirty = true; }
      r.flags = r.flags || [];
      for (const f of F.active) {
        if (!r.flags.includes(f)) { r.flags.push(f); dirty = true; reviewDirty = true; }
        if (/^Guessed/.test(f) && !r.guess) { r.guess = true; dirty = true; }
      }
      // one tap per list: with Wrong / Skipped / Guessed Wrong / Guessed Right ticked, read every question number in the grid at once
      const grid = m === 'learn' ? null : readGrid();
      // v2.5: two lists ticked together (e.g. Wrong + Skipped) are read too; when one of them is already known, the other is
      // the rest of the grid. A note shows which filters the recorder sees ticked.
      const LISTS = /^(Wrong|Skipped|Guessed Wrong|Guessed Right)$/;
      const act = F.active.filter((f) => LISTS.test(f)), others = F.active.filter((f) => !LISTS.test(f));
      const listName = act.length >= 1 && !others.length ? act.join('+') : null;
      const fkey = F.active.join(', ') || 'none';
      if (fkey !== lastFilters) { lastFilters = fkey; if (F.active.length) flash('Trace: filters ticked · ' + fkey); }
      if (grid && grid.length) {
        if (listName) {
          S.lists = S.lists || {};
          let name = listName, nums = grid;
          if (act.length >= 2) {
            // v2.9: any number ticked; if exactly one of them is new, it is the grid minus the lists already read
            const known = act.filter((f) => S.lists[f]), fresh1 = act.filter((f) => !S.lists[f]);
            if (fresh1.length === 1) { name = fresh1[0]; const seen = new Set(known.flatMap((f) => S.lists[f])); nums = grid.filter((n) => !seen.has(n)); }
            else if (fresh1.length === 0) name = null;   // nothing new ticked (a filter was unticked or re-ticked)
            else flash('Trace: tick one list at a time so each is read on its own');
          }
          if (name && JSON.stringify(S.lists[name]) !== JSON.stringify(nums)) { S.lists[name] = nums; dirty = true; reviewDirty = true; flash('Trace: ' + name + ' list read · ' + nums.length + ' question(s)'); }
          // the anchor ties one question ID to its paper number; keep the first one, because after a filter change the
          // question on screen can still be the old one while the grid already shows the new list
          if (!S.anchor && grid[q.qno - 1]) S.anchor = { mcqid: q.mcqid, qno: grid[q.qno - 1] };
        } else if (!F.active.length && grid.length === fullTotal) S.anchor = { mcqid: q.mcqid, qno: q.qno };
      } else if (listName && !grid) {
        if (lastGridWarn !== fkey) { lastGridWarn = fkey; flash('Trace: question grid not found — list not read'); }
      }
      if (!hadEx && r.explanation) reviewDirty = true;
      const done = Object.values(S.questions).filter((x) => x.correct).length;
      const state = !r.correct ? ' … reading' : (r.explanation ? ' ✓ answer + explanation' : ' ✓ answer (no explanation shown)');
      const tagNote = F.active.filter((f) => !['Correct', 'Wrong', 'Skipped'].includes(f)).length ? ' · tagging: ' + F.active.join(', ') : '';
      badge('Trace · Q' + q.qno + state + ' · ' + done + '/' + S.total + ' saved' + tagNote);
      if (!had && r.correct) reviewDirty = true;
      if (!had && r.correct) {
        flash('✓ ' + done + '/' + S.total);
        if (done >= S.total && !S.review_saved) {
          S.review_saved = true; dirty = true; save(); reviewDirty = false;
          download('_review'); setTimeout(() => flash('Trace: review saved'), 1600);
        }
      }
    } else if (m === 'result') {
      badge(null);
      closeCurrent();
      liveDirty = false;
      const RR = readResult();
      if (RR.module) {
        const lt = GM_getValue(TITLEKEY, null);
        if (!lt || lt.name !== RR.module || now() - lt.t > 60000) GM_setValue(TITLEKEY, { name: RR.module, total: +RR.total_mcqs || null, t: now() });
      }
      if (S && !S.result) {
        S.result = readResult(); S.module = S.result.module; dirty = true; save();
        download(); S.saved = true; dirty = true; save();
        flash('Trace: saved');
      }
    } else {
      closeCurrent();
    }
  }
  function merge(q) {
    const r = rec(q.mcqid);
    if (q.images && q.images.length) {
      r.images = r.images || [];
      for (const im of q.images) {
        if (r.images.some((x) => x.src === im.src)) continue;
        const seenImgs = GM_getValue(IMGKEY, {});
        if (seenImgs[im.src]) { r.images.push({ where: im.where, src: im.src, file: seenImgs[im.src], earlier: true }); dirty = true; continue; }
        const n = r.images.filter((x) => x.where === im.where).length + 1;
        const ext = ((im.src.split('?')[0].match(/\.(png|jpe?g|gif|webp|svg)$/i) || [, 'jpg'])[1]).toLowerCase();
        const file = 'trace_img_' + q.mcqid + '_' + im.where + '_' + n + '.' + ext;
        r.images.push({ where: im.where, src: im.src, file });
        seenImgs[im.src] = file; GM_setValue(IMGKEY, seenImgs);
        dirty = true;
        try {
          GM_download({ url: im.src, name: file, onerror: () => { r.images.find((x) => x.file === file).failed = true; dirty = true; } });
        } catch (err) { r.images.find((x) => x.file === file).failed = true; }
      }
    }
    for (const k of ['stem', 'options', 'correct', 'marked_wrong', 'cohort_pct', 'explanation', 'references']) {
      const v = q[k];
      if (v != null && v !== '' && !(Array.isArray(v) && !v.length)) {
        if (JSON.stringify(r[k]) !== JSON.stringify(v)) { r[k] = v; dirty = true; }
      }
    }
  }

  function download(suffix) {
    if (!S) return;
    const firstId = Object.keys(S.questions || {}).find((k) => /^DT|^TS/.test(k)) || '';
    const label = S.module || (S.kind === 'gt' ? 'GT' + (S.sectional ? '_sectional' : '') : (S.mode === 'learn' ? 'QBank_learn_' + firstId : 'QBank'));
    const name = 'trace_doct_' + label.replace(/[^\w]+/g, '_').slice(0, 40) + '_' + S.started.slice(0, 16).replace(/[:T]/g, '-') + (suffix || '') + '.json';
    S.saved_by = VERSION; S.saved_at = new Date().toISOString();
    const blob = new Blob([JSON.stringify(S, null, 1)], { type: 'application/json' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob); a.download = name;
    (document.body || document.documentElement).appendChild(a); a.click();
    setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 2000);
    upload(suffix || '', name);
    // one sitting per mode: once a review (or learning-mode capture) is saved, recording switches itself Off
    // QBank solving shows the key on each question, so the attempt alone is enough; a GT needs its review (the key is only there)
    const qbankDone = /^_attempt/.test(suffix || '') && !isTest() && S.kind !== 'gt';
    if (/^_review/.test(suffix || '') || S.mode === 'learn' || qbankDone) { GM_setValue(MODEKEY, 'off'); modeUI(); flash('Trace: saved · recording now Off'); }
  }
  // Compact copy for Trace: no stems, options or explanations, only what Trace needs to find cards and reasons.
  function upload(suffix, fname) {
    const c = GM_getValue(CONNKEY, null);
    if (!c || !c.u || !c.k) { flash('Trace: not connected · menu › Connect to Trace'); return; }
    const qs = Object.values(S.questions || {}).map((q) => ({ mcqid: q.mcqid, qno: q.qno, ms: Math.round(q.ms || 0), chosen: q.chosen || null,
      correct: q.correct || null, marked_wrong: q.marked_wrong || null, guess: !!q.guess, flags: q.flags || [], cohort: q.cohort_pct == null ? null : q.cohort_pct,
      attempt: q.attempt || null, section: q.section || null, global_no: q.global_no || null }));
    const rec = { type: 'trace.doct.attempt', v: 1, recorder: VERSION, who: S.who || 'Trace', rmode: S.rmode || getMode(), module: S.module || null, kind: S.kind || (isTest() ? 'gt' : 'qbank'),
      mode: S.mode || null, started: S.started, saved_at: new Date().toISOString(), suffix, total: S.total || null, result: S.result || null, questions: qs,
      lists: S.lists || null, anchor: S.anchor || null };
    const name = fname.replace(/^trace_doct_/, 'doct_' + (rec.who === 'HT' ? 'HT' : 'Trace') + '_').replace(/[^\w .\-]/g, '_').slice(0, 80);
    const send = (ops, cb) => GM_xmlhttpRequest({ method: 'POST', url: c.u, headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      data: JSON.stringify({ key: c.k, op: 'batch', ops }), timeout: 60000,
      onload: (r) => { let j = null; try { j = JSON.parse(r.responseText); } catch (e) {} cb(j && j.ok ? j.results : null, j && j.error); },
      onerror: () => cb(null, 'network'), ontimeout: () => cb(null, 'timeout') });
    const write = (folder) => send([{ op: 'writeFile', folderId: folder, name, text: JSON.stringify(rec), mime: 'application/json' }], (res, err) => {
      if (res && res[0] && res[0].ok) flash('Trace: sent to Trace ✓'); else flash('Trace: not sent (' + ((res && res[0] && res[0].error) || err || '?') + ') · file kept in Downloads');
    });
    write(GM_getValue(FOLDKEY, DOCT_FOLDER));
  }
  function connect() {
    const t = window.prompt('Trace recorder: paste your private Trace setup link (kept only in Tampermonkey on this Mac).');
    const m = String(t || '').match(/setup=([\w\-]+)/);
    if (!m) { if (t) flash('Trace: that is not a setup link'); return; }
    try {
      let b = m[1].replace(/-/g, '+').replace(/_/g, '/'); while (b.length % 4) b += '=';
      const j = JSON.parse(atob(b)); if (!j.u || !j.k) throw new Error('incomplete');
      GM_setValue(CONNKEY, { u: j.u, k: j.k }); flash('Trace: connected ✓');
    } catch (e) { flash('Trace: that link did not work'); }
  }
  // the current mode, always visible on DocT pages (bottom-right)
  let modeEl = null;
  function modePill() {
    const m = getMode();
    if (!document.body) return;
    if (!modeEl) { modeEl = document.createElement('div'); modeEl.style.cssText = 'position:fixed;right:10px;bottom:10px;z-index:2147483647;font:12px/1.3 system-ui,sans-serif;padding:5px 10px;border-radius:14px;pointer-events:none;box-shadow:0 2px 8px rgba(0,0,0,.3)'; document.body.appendChild(modeEl); }
    modeEl.textContent = 'Trace rec · ' + MODES[m] + (GM_getValue(CONNKEY, null) ? '' : ' · not connected');
    modeEl.style.background = m === 'off' ? '#e9e5da' : m === 'trace' ? '#1f6f5c' : '#6d4a8a';
    modeEl.style.color = m === 'off' ? '#3a3328' : '#fff';
  }
  setInterval(modePill, 1500);
  function snapshot() {
    const html = '<!-- ' + location.href + ' | ' + new Date().toISOString() + ' -->\n' + document.documentElement.outerHTML;
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([html], { type: 'text/html' }));
    a.download = 'doct_snapshot_' + Date.now() + '.html';
    (document.body || document.documentElement).appendChild(a); a.click();
    setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 2000);
  }

  let pending = false;
  function schedule() { if (pending) return; pending = true; setTimeout(() => { pending = false; try { tick(); } catch (err) { console.debug('trace', err); } }, 120); }
  function start() {
    new MutationObserver(schedule).observe(document.documentElement, { childList: true, subtree: true, characterData: true });
    schedule();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();

  let modeIds = [];
  function modeUI() {
    if (typeof GM_unregisterMenuCommand === 'function') for (const id of modeIds) { try { GM_unregisterMenuCommand(id); } catch (e) {} }
    modeIds = Object.keys(MODES).map((k) => GM_registerMenuCommand((getMode() === k ? '● ' : '○ ') + 'Mode: ' + MODES[k], () => {
      closeCurrent(); save();
      GM_setValue(MODEKEY, k);
      // v2.9: only an unfinished live attempt changes owner; a captured review stays with the person who made it
      const liveOnly = S && !S.saved && !S.review_only && !S.review_saved && !S.lists && S.mode !== 'learn';
      if (liveOnly) { S.who = k === 'trace' ? 'Trace' : 'HT'; S.rmode = k; dirty = true; save(); }
      modeUI(); modePill(); flash('Trace: ' + MODES[k]);
      for (const p in pauseShown) delete pauseShown[p];
      badge(null); schedule();
    }));
    modePill();
  }
  modeUI();
  GM_registerMenuCommand('Connect to Trace (once)', connect);
  GM_registerMenuCommand('Mark selected line', markLine);
  GM_registerMenuCommand('Save session file now', () => { closeCurrent(); save(); download(); });
  GM_registerMenuCommand('Start a fresh session', () => { closeCurrent(); S = fresh(); dirty = true; save(); flash('Trace: new session'); });
  GM_registerMenuCommand('Save page snapshot', snapshot);
  GM_registerMenuCommand('Reset everything (start over)', () => {
    if (!window.confirm('Trace recorder: forget all recorded sessions, attempt counts and the list of saved images? Files already in Downloads are not touched.')) return;
    closeCurrent(); S = null; cur = null; liveDirty = false; reviewDirty = false;
    GM_setValue(KEY, null); GM_setValue(IMGKEY, {}); GM_setValue(SEENKEY, {}); GM_setValue(TITLEKEY, null);
    flash('Trace: reset done');
  });
})();