# Trace — handover for the next Trace chat (24 Nov 2026)

Read this first, then `AGENTS.md` and the top of `CHANGELOG.md` (State block + newest entries) in the repo. Older history: project docs `claude/Trace_Handoff_13Nov.md`, `claude/Trace_Handoff_10Nov.md`, `claude/Study_Partner_Handoff_10Nov.md` (the CCM project is full, so new docs go to Drive › Trace).

## 1. Who and what
- **Naven** (Dr Harish; final-year MD Anaesthesiology, IMS BHU). Study partner **HT** (Harshita). Exam: **NEET-SS DM Critical Care, 11–12 Dec 2026**, MCQ +4/−1. INI-SS Stage 2 is done (17 Nov).
- **Trace** = his offline study PWA (cards, Flow, viva/NEET packets, GTs). Repo `baabusumathi-debug/trace` (branch `main`, GitHub Pages). Live: `/trace/` · Test: `/trace/test/`.
- Devices: Galaxy Tab S10 Ultra (landscape, main), Android phone, MacBook (Mac has the Claude desktop app; the built-in browser tab "seed" = Trace Test is where in-browser jobs run).

## 2. Standing rules (Naven's)
- Test first. Naven has allowed Claude to push to test **and** live ("I allow u to push the app to test and livr as well"); still release to test, check, then promote. Promote = copy `test/` → root except `index.html` and `manifest.webmanifest`, bump versions.
- Never open or drive DocT (DocTutorials) yourself. Never press "Make voice" unless he asks (he asked for the P12 voicing, see §7).
- Be direct, one thing at a time, teach the why, 12-hour IST times. **He is colourblind: never colour alone** — shape, label, lightness.
- No mnemonics/stories in explanations. Independent fact-check before anything enters his cards. **Do not leave flags for him** — decide fact-check issues yourself, the way that is best for NEET (current answer taught, the bank/textbook key named so he recognises it).
- Credits matter: he prefers work done by separate writer chats/agents from a prompt, with this chat integrating.
- Commit messages end with the session attribution lines the harness gives.

## 3. Release mechanics
- Versions: **live 1.4.55**, **test 1.3.167** (24 Nov). Bump `appVersion` in `js/config.js` and `PREFIX + 'x.y.z'` in `sw.js` (each copy). CHANGELOG: new `T-NNN` entry (newest is **T-194**), update the State block.
- Push: `git -c push.negotiate=true push`. Pages status: `gh api repos/baabusumathi-debug/trace/actions/runs --jq '.workflow_runs[0] | "\(.head_sha[0:7]) \(.status) \(.conclusion)"'`.
- A tab needs 2+ reloads (`?r=N`) to run a new version. **An SW update reloads the tab and kills running in-tab jobs** (e.g. voice making) — don't push a test release while a job runs in the test tab.
- Data always fetched fresh by the SW (no version bump needed): `data/qbank.json`, `qmap.json`, `cardfix.json`, `explain.json`, `data/viva/*.json`, `data/gt/*.json`. The app keeps its own offline copies (IndexedDB kv).
- Check JS: `cp f.js /tmp/x.mjs && node --check /tmp/x.mjs`.
- `CONFIG.onlyDecks` limits decks in test (CHANNEL test only); `readOnly` in test (never writes Sheet/Drive except listed pilots).
- Profiles: `localStorage['trace-test.profile' | 'trace.profile']` = `'trace'` (Naven) or `'ht'`. `IS_HT` in config. Viva is Naven-only; GTs show each person's own sheet.

## 4. Drive (all under My Drive › Trace, id `1e_lx6kl_MhG4aOracgTr_HG3NUp7OsYs`)
- `doct/` (`1wqRbRG-nqldfafFL-AughcBEBfo6atQo`): recorder files `doct_<Trace|HT>_<module>_<stamp>_<review|attempt>_*.json` (compact). Full files (stems, options, explanations) land in the Mac's **Downloads** as `trace_doct_*.json` and images `trace_img_*.png` (Mac folder `/Users/harshitatiwari/Downloads`, reachable via remote-devices; Downloads listing is huge — save `device_list_dir` output and filter by mtime).
- `voice-k/` (`1IXU9A_uFNV6GCLK8TgW9mNZN4Mz9Buf3`): Kokoro clips `VIVA-P12__<partkey>.b64`, index `VIVA-P12.kidx.json` `{key:{id,h,sec,voice,tid?}}`, timing files `*.t.json`.
- `viva/`: older packages from the viva writer (P1–P11 pieces). P12 is in the repo.
- Docs: `NEET_Cardio_Packets_Plan_23Nov.md`, `Kokoro_Word_Timings_Task.md` (ChatGPT agent task; says 2,550/12 h but works off the index), `P12_Card_Flags_23Nov.md`, `P12_EC1_pack.json`, `P12_EC2_pack.json`, `P12_EC_review.md`, `P12_EC_img/` (46 SVGs), `P12_EC_img_bundle.json` (same SVGs in one file).
- War Map Sheet "CCM War Map Data" `150OxumS0XPBlPfmiNP9HLxwPrjUGEzbmmIBknvNJssk`.

## 5. Card text corrections — `data/cardfix.json`
- `cards["DECK|CODE"].fields` replaces whole fields (`a`, `why`, `watch`…), with `src`, `date`; `version` = sha1 of cards. Top-ups are keyed `DECK|TU-nn`. 431 entries now.
- Card source text for searching: `/home/claude/map/cards/<DECK>.jsonl` existed in the old container; in a fresh container get cards from Drive › Trace › decks › <DECK> › cards.jsonl (or the app's IndexedDB).
- Always edit by exact-substring replacement of the current (fix-applied) field.
- Pending: **HY2|CAR-24** Daniel score — add T-inversion depth rows (V1–V3), Q in III = 1, T inversion in III = 1 (Daniel 2001); 8 stays the keyed answer.

## 6. Viva / NEET packets
- Packages P1–P8, P10, P11 (INI viva) and **P12 NEET cardiology** (`test/data/viva/P12.json`, live has P12 as of 1.4.54 without the ECG packets).
- **P12 now: 12 packets, 60 sections, P12.20261124.1 (test only):** S1 Shock I (P12-101–105) · S2 Shock II (201–206) · **EC1 ECG I: wiring, waves, cameras (1101–1105)** · **EC2 ECG II: blocks, short circuits, drugs, what changes the waves (1201–1207)** · A1 ACS I (301–306) · A2 ACS II (401–406) · RY Rhythm (501–505) · DR Cardiac drugs (601–602) · RH Pericardium/myocarditis/IE (701–704) · RV Right heart/PH (801–804) · AO Aorta (901–903) · AR Arrest (1001–1007). New cards V12-001…076.
- Build: drafts `tools/viva/p12/<CODE>_draft.json` → `python3 assemble.py S1 S2 EC1 EC2 A1 A2 RY DR RH RV AO AR` (writes test P12.json; first arg ending .json = other output path). Check: `python3 tools/viva/check_viva.py test/data/viva/P12.json test/data/viva/img/P12/ <cards dir> test/data/cardfix.json` (0 errors now; "long"/"last bridge" warnings are fine).
- Format: question `{q,text,tier,gen,kind,open{v,text},steps[{card,bridge,lesson{v,text},model?}],spine[],close?,drill?[{q,a}],packet?}`; lesson markers `[[takeaway]]`, `{{on-screen}}`, `{{pic}}`. Briefs: `P12_BRIEF.md`, addenda, `EC_review.md`.
- Section labels: `test/js/vivamap.js` SECTIONS.P12 (EC1/EC2 added).
- ECG packets were written by a separate writer chat from the prompt artifact "ECG Foundation Packet: Writer Prompt" (https://claude.ai/artifact/55mJNAgrjNCH4CBHM2skVq). Rule used: every disease's ECG is taught in EC1/EC2 from mechanism; later packets treat it as revision; management/doses stay in later packets.

## 7. Voice
- **Kokoro "Michael"** (default; chip Voice: Michael / Iapetus, `trace.lvoice`): kokoro-js 1.2.1 on WebGPU in the Mac's built-in browser; `makeKokoro(pkg,onStep,onlyQ)` in `js/lesson.js` makes only missing/changed parts (≤320-char chunks, MP3 48 kb/s, base64 to `voice-k`).
- **In progress (started 24 Nov ~5:40 PM IST, test tab "seed")**: `makeKokoro('P12')` for the ECG sections + the 4 changed openings/closes: **781 clips, ~5 h**. Progress: `window.__kk` in that tab. If it stops (tab reload, Mac asleep), re-run the same call — it skips finished clips. Don't release to test while it runs.
- After it finishes: the new clips need **word timings** — Naven's ChatGPT agent runs `Kokoro_Word_Timings_Task.md` again (it skips clips that already have `tid`).
- **Gemini "Iapetus"** via the backend: 500,000 s/month quota (resets 1st). Real pace ~8 chars/s.
- "VT" spoken "V T" in cardiac context (voice.js rule), else "tidal volume".
- Card voice clips for cards whose text changed show as not made (free to remake in Michael when he asks).

## 8. GTs (built 24 Nov; live 1.4.55)
- Home button **GTs** → papers → answer sheet (150 tiles, sections A–C). Right = white, wrong = black, guessed = pencil stripes, blank = dashed, other person wrong = folded corner (dog-ear), repeat = second sheet + ×2. Filters Wrong/Guessed/Blank/Repeats/Shared; Walk N. Paper order / By system. Folding papers rail. "Where the marks went" + system headings → single-system page (trend per GT, topics). All GTs: score trend both people + systems across papers.
- Walk: Try/Read; option marks ✓ Key / You ✗ / other ✗; back = Answer · Why · Watch · Hook · Tempted; Explain pane tabs: Explanation | linked cards | earlier GT question | DocT's text. In HT's profile, "you" lines are swapped (`persp()`).
- Code: `js/gt.js` (self-contained), CSS `.gt-*` in `css/app.css`, route `#/gt/...` in app.js, tile `gtTile()`.
- Data: `data/gt/index.json`, `GT7.json`, `GT8.json` (`q[]` with sys/topic, `people.Trace|HT` {res string, guess[], picks{}, score…}, `cards{n: {links,before,answer,why,watch,hook,explain,options,picks_note,key,depth}}`), images `data/gt/img/`.
- Build: `tools/gt/` — `BRIEF.md` (writer rules: native card → short; new topic → teach fully incl. what NEET could ask next; one payoff; never assume knowledge), `CHECK.md` (independent checker, decides flags, cardfix entries), `assemble.py` (papers.json + classify.json + out/final/*.json → data/gt), review logs in `tools/gt/review/`. The working dir `/home/claude/gt` (papers.json = parsed captures) is not in the repo; rebuild from the Downloads full files if needed.
- **Adding a new GT**: Naven sits it with recorder v2.9, then reviews it on DocT: Start a fresh session → open review, no filter (anchor) → tick Wrong, Guessed Right, Guessed Wrong, Skipped one at a time → HT also steps through her wrong questions (for her picks). Then: parse full files → papers.json entry → classify sys/topic → writer agents (fable) per ~12 questions → checker agents → assemble → test → live.
- Not built: GT chips on regular cards; walked-state sync across devices.

## 9. DocT recorder (Tampermonkey, Chrome on the Mac)
- Source now in repo `tools/recorder/` (v2.8 as installed, **v2.9 current**; Naven installed 2.9 on 24 Nov). v2.9 fixed: sections B/C read as A (DocT keeps finished sections "active"), mode switch relabelling a captured review to the other person, stale wrong marks, cumulative list filters.
- GT 7 and GT 8 were re-captured for both people with v2.9; lists verified against DocT filter counts. Live-attempt times for GT 7/8 sections B/C are lost.

## 10. State of things / open items
- Test has the ECG packets; **not promoted** — promote when Naven says (after voicing finishes, or he may want it sooner).
- Word timings for the new Michael clips (ChatGPT agent), after voicing.
- HY2|CAR-24 cardfix rows (above).
- Older open items: voice the GI hit cards; never-asked cardio cards voicing; CVS05B/CVS06B/CVS10B HT PDFs >10 MB need downloading; card clips for changed cards.
- Naven's ideas parked: interactive physiology simulator (cardiac AP/drugs); NEET concept pages (OBS done, tox, GI, endocrine).
