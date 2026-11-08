# Trace — change log

Changelog format: 2 (stable entry IDs `T-NNN`, newest first). The rules for reading and writing this file are in `AGENTS.md` §11–§12.

In progress: none

## State (as of entry T-114)

This summary helps you orient. It **does not prove** that content is unchanged; only a verified commit or content fingerprint does (`AGENTS.md` §12).

| Item | Value |
|---|---|
| Live app (repo root) | **1.4.18** · promoted from test 1.3.83 on 8 Nov (T-114: RESP01B/C Explain, ARDS-42 correction, viva P4 narrated lessons, card voice); earlier 1.4.17 from test 1.3.68 on 7 Nov; earlier 1.4.16 from test 1.3.66 on 7 Nov (T-094: checked card-text corrections, `data/cardfix.json`); earlier 1.4.15 from test 1.3.65 on 6 Nov (T-092: primer/story always on the card, pen tools on them, question-side marks fix); earlier 1.4.14 from test 1.3.63 (T-089: Explain v3, RESP01A, audited Toxicology); earlier 1.4.13 from test 1.3.61 (T-087: room fixes, Move to card, Plan undo kept, intent suggestions); earlier 1.4.12 from test 1.3.59 (T-085: Explain v2 and card corrections for all 7 Toxicology decks); earlier 1.4.11 from test 1.3.57 (T-082: Explain v2 for TOX01, flow v3 layout, ink on Explain, Ask Claude, flexible Plan with undo); earlier 1.4.10 from test 1.3.44 on 4 Nov (T-068: ink on cards, folded Top-up boxes; earlier T-056; earlier T-054, earlier T-051, T-047, T-040, first T-026): The Plan, Pick mode, Flow thread, re-laid Loft; palace home, meditation, visual decks, QBank/GT layer, Top-ups, Flow desk, save/discard on leaving a flow, new Loft, Going out / breaks. Same code as `test/` except the version and the title. |
| Test build (`test/`) | **1.3.83** · T-113 ARDS-42 correction, P4 voice checked · T-101–T-112 narrated viva lessons (P4, 49 questions) and RESP01B/C Explain · T-100 voice on the explanations · T-099 card voice (Listen, ▶ per point, speed) · T-096 viva on Naven's profile only · T-095 viva layer (P4) and 12 more card-text corrections (60 cards in `data/cardfix.json`). Carries the 7 Toxicology decks, RESP01A, the corrected decks and the P4 decks (`CONFIG.onlyDecks`, 57 decks). Live is 1.4.18 (= test 1.3.83). |
| Bridge (Apps Script) | **v5** deployed by Naven on 3 Nov (calendar reminders, T-041/T-042) · before that **v4** deployed by Naven on 1 Nov; adds `notifyJournal`, off by default via `JOURNAL_ENABLED`. A lost `readBinary` routing line was restored the same day and redeployed (Naven calls it "v4.1"). Repo source: `backend/Code.gs` (no secrets). |
| Guidance | `AGENTS.md` guidance version **6** · `docs/visual-deck-contract.md` contract version **3.1** (schema unchanged from 3) |
| Visual decks | **GI02B v2** is published by ChatGPT (53 scenes) and was accepted in Naven's Chrome on test 1.3.6 on 1 Nov. Bridge `readBinary` routing was restored by Naven, who deployed it as "v4.1". **Offline acceptance is still outstanding.** GI01A is being prepared by ChatGPT. |
| Meditation | Test build only. Sample scripts are read by the device voice, and **one Journal pilot recording** (`Trace › meditation › …_trace_pilot….mp3`) is loaded through the existing bridge. Real file verified in Naven's Chrome on 31 Oct: found, downloaded (6,381,340 bytes), decoded (531.72 s), and actually played to 0:12. Pause held and resume advanced. Not yet checked: offline playback, and whether the sound was actually heard. Nothing is automated or scheduled, and the producer's capabilities are unverified. |
| Flow message pilot | Test build only. The route `#/pilot` sends **one** request, `req-<id>.json`, to `Trace › flowmsg` on the first Next after Reveal, and shows **one** plain-text reply from Journal, `res-<id>.json`, within 5 minutes. **One real round trip passed on 31 Oct (T-015)**, as an active-session pilot. Journal's watch was started by hand in chat, so that was **not** unattended automation. Since T-016, the test build also asks bridge v4 to wake Journal's webhook routine. **Two automatic wakes passed on 1 Nov with no chat watch** (request/reply pairs `fm-20261101-160706-k5qi7c` and `fm-20261101-161241-a2n8vw` are in Drive). Each took about 37–61 s from request to reply, nearly all of it on Journal's side. Naven then paused Journal work. **The current `JOURNAL_ENABLED` value is unconfirmed.** |
| QBank/GT layer | Test 1.3.8 only. `test/data/qbank.json` (version in the file) holds, per card: bank chips (NEET 25 recall · Marrow · DocT · DocT GT), Top-up lines, Crossfire lines and checked corrections; plus 242 Top-up cards in 94 decks and 5 Top-up decks (80 cards: TU-NEURO 24, TU-IE 15, TU-TX 15, TU-AIR 13, TU-SAFE 13). Built by Claude from the DocT QBank, 20 DocT GTs and the Marrow map; every item was approved by Naven on 2 Nov. Source of truth for its content: the CCM project files `claude/QMap_FINAL_*.csv`. |
| Waiting on Naven | Device check of live 1.4.0 · meditation producer, times and input source · sign-off after the visual pilot |

---

## T-114 — 2026-11-08 — Claude — live — 1.4.18
- Promoted test 1.3.83 to live on Naven's instruction (8 Nov: "Yes fr both"). Same copy rules as T-082 (every file in `test/` except `index.html` and `manifest.webmanifest`); `CONFIG.onlyDecks` stays `null` on live.
- Live gains T-095 to T-113: NEET Explain for RESP01B and RESP01C (HT starts respiratory), the RESP01C ARDS-42 correction, the viva layer with P4 narrated lessons (read-along, player bar, Autoplay / Tap to play), card voice (Listen, speed) and the Make voice double tap. Voice and viva stay on Naven's profile only.
- Checked before release (demo, live path): modules load, version 1.4.18, `onlyDecks` null, no page errors.

## T-113 — 2026-11-08 — Claude — test — 1.3.83
- **Correction: RESP01C ARDS-42** (Naven, 8 Nov: yes to the correction). `data/cardfix.json` replaces the card's Watch line: early corticosteroids are the one drug exception (DEXA-ARDS, RECOVERY; conditionally recommended by ATS 2024 and SCCM 2024); older grade tables still rate steroids D. Sources on the card. 61 cards in the layer.
- **P4 lesson voice checked.** All 2,727 clips scanned against their scripts with the Whisper word timings. 72 had an audible fault (style instruction read aloud inside the played part, a repeated sentence, or the script not followed) and were remade; 2 key-point clips (P4-009 s2, P4-012 s5) kept reading the instruction and were remade with a shorter key-point instruction. Clips whose extra speech sits before or after the line are trimmed by the app and were left.

## T-112 — 2026-11-08 — Claude — test — 1.3.82
- Package **P4.20261108.6** (writer chat): lessons for all 49 P4 questions (G3–G9 and EV added; 330 lessons). Figures added: `P4_G3_aprv_release`, `P4_G5_eit_crossing`, `P4_G6_lus_grades`, `P4_G6_diaphragm_mmode`, `P4_G7_signal_chain`, `P4_G9_wind_clock`; card figure `card_RESP02B_COPD-17.png`. Checker clean. Voice for the 37 new questions made overnight 8 Nov (2,065 clips).

## T-111 — 2026-11-08 — Claude — test — 1.3.81
- **Fix: lesson index entries lost during long runs.** Two calls saving the index at once could drop each other's entries (Drive hands a stale copy); `voiceReindex` restores them from the clips' own files but ran only at the end, and an app update cut the G1+G2 run short (269 made clips looked missing). It now also runs every 6 calls.

## T-110 — 2026-11-08 — Claude — test — 1.3.80
- **NEET Explain for RESP01B (16 cards) and RESP01C (17 cards)** (Naven, 8 Nov: HT starts respiratory today). Same v3 method as RESP01A: built from the real questions linked to each card (`tools/explain/qpack/`), deck story (spine, primer, step), independent fact-check with sources (`tools/explain/resp01b_review.md`: 10 changes; `resp01c_review.md`: 11 changes). Card text unchanged; FLAGS list where cards or question keys disagree with current evidence (e.g. RESP01C ARDS-42: dexamethasone and the 2024 steroid guidance).

## T-109 — 2026-11-08 — Claude — test — 1.3.79
- Viva page **Make voice** buttons need a second tap within 4 s ("Tap again to start · …"). A stray tap had started all of G1 and G2 (116 min); it was stopped after 4 clips.

## T-108 — 2026-11-07 — Claude — test — 1.3.78
- Package **P4.20261107.10** (writer chat): G2 lessons for 6 more questions (P4-006, 008, 016, 009, 197, 214); new figure `P4_G2_pv_loop.svg`. 78 lessons in all; checker clean. No voice made for G2 yet.

## T-107 — 2026-11-07 — Claude — test — 1.3.77
- **P4-198 lessons remade at the new pace** (72 clips, 12.2 spoken characters a second, about 18 min). 2 clips still carried extra speech after three tries (Gemini read its style note aloud, once before the text): the app now also starts a lesson clip just before the script's first word, as well as stopping just after its last, so neither is heard.

## T-106 — 2026-11-07 — Claude — test — 1.3.76 · bridge (Apps Script version 12)
- **Fix: Gemini rate limit.** Making lessons three calls at a time hit Gemini-TTS's limit of about 10 requests a minute per project (429). The bridge now waits and retries (15, 30, 45, 60 s); the app sends two calls at a time. Clip entries are also kept on each MP3's file description, and `voiceReindex` restores any entry a parallel save overwrote.

## T-105 — 2026-11-07 — Claude — test — 1.3.75 · bridge (Apps Script version 10)
- **Lesson voice pace** (Naven, 7 Nov: "a gap between every word, even at 1.7×"): the style note asked for "unhurried, measured… enunciate every word", and Gemini read word by word at about half normal speed. New note: natural conversational pace, words in smooth connected phrases, clear but not over-articulated; takeaways "a touch slower" with gentle emphasis. Lesson version `L2`, so every lesson clip is made again.
- **Faster making:** the bridge now holds its lock only to save the index (speech and timings run outside it), and the app sends three calls at a time.

## T-104 — 2026-11-07 — Claude — test — 1.3.74 · bridge (Apps Script version 9)
- **Fix: lesson clips that run on.** In the P4-198 pilot, 22 of 72 Gemini clips did not stop at the end of their text: some repeated it, some went on with invented speech (one ran 10 minutes). Whisper's transcript shows it. The bridge now compares Whisper's word count with the script's and makes a clip again (at most 3 tries, best kept) when it runs on by more than 20%; `redo` remakes clips already made. The app also stops every lesson clip just after the script's last word (cut point from the word timings), so a run-on is never heard, and the timeline counts only up to that point.

## T-103 — 2026-11-07 — Claude — test — 1.3.73
- Package **P4.20261107.9** (writer chat, reviewed): pictures and on-screen boxes for the G1 lessons; new figures `P4_G1_autopeep_flow.svg`, `P4_G2_hold_shape.svg`.
- Lessons with `"pic": "card"` / `"card:DECK|CODE"` now show the card's own figure, cut from its PDF deck page into `data/viva/img/P4/card_<DECK>_<CODE>.png` (MV02 MODE-03 scalars A/B, MV03 ASYN-03 panels 1–3). The checker checks those files exist.

## T-102 — 2026-11-07 — Claude — test — 1.3.72 · bridge v7 (Apps Script version 8)
- **Narrated lessons, read-along** (Naven, 7 Nov; spec `docs/Trace_Lesson_Spec_7Nov.md`): a viva question's opening lesson plays on the question page, each card's micro-lesson in a new **Lesson** tab (first, beside NEET | Viva), the closing lesson on its own page before the spine card. The full text shows while it plays; the word being spoken is lit (nothing read is dimmed); the text scrolls to keep it in view, stops when Naven scrolls by hand ("↓ Follow the voice" brings it back); tap a word or a paragraph to jump there. Player bar: pause, ±5/±10 s, seek slider, time, speed. Takeaways (`[[ ]]`) are bold and are their own clips with a slower, stressed style note. `{{ }}` boxes are shown, never spoken; `pic` shows a picture, or a button for the card's own figure.
- **Word timings:** the bridge runs each new lesson clip once through OpenAI Whisper (word timestamps) and saves `<k>.t.json` beside it; the app matches Whisper's words to the script and places any unmatched word between its neighbours. Clips without timings get approximate ones (words spread by length). Timings are in clip seconds, so they hold at any speed.
- **Autoplay / Tap to play** (Viva page and every lesson bar, per session): open → each card's lesson (the card turns itself over) → close → spine run on their own; the spine waits for Naven. Lock-screen play / pause / ±10 s.
- **Viva page:** a LESSONS line (questions, minutes, pieces made) and Make voice buttons, first question only or all. Nothing is made until Naven presses one.
- **Card voice:** American accent, clear and well paced (prompt version `p3`, so card clips are made again when Make voice is pressed).
- Package **P4.20261107.7** (G1 lessons for 6 questions, 49th question P4-002). Bridge v7: `voiceAlign`, `align` on `voice`; deployed as Apps Script version 8 ("trace bridge v7").

## T-101 — 2026-11-07 — Claude — test — 1.3.71
- **Voice player bar** (Naven, 7 Nov): while a Listen plays, a bar opens under the strip: −10, −5, pause/play, +5, +10, a seek slider that can be dragged anywhere, and the time ("0:42 / 3:10"). The timeline covers the whole Listen (all its points, not one clip), so seeking and skipping cross from one point to the next. Speed − / + stays and is remembered.

## T-100 — 2026-11-07 — Claude — test — 1.3.70
- **Fix:** the voice read the style note's pronunciation hints aloud at the end of each clip ("say PEEP as peep, ARDS as A R D S"). The style note now carries no text to be spoken; PEEP → "peep" and ARDS → "A R D S" moved into the pronunciation list. Prompt version `p2`, so every clip is made again.
- **Voice on the Explain side** (Naven, 7 Nov): a Listen strip at the top of the Explain pane reads the explanation shown, NEET (intro, part by part, punchline) or Viva (intro, part by part, picture caption); the NEET | Viva switch changes what it reads. The deck page's Make voice now includes these points (RESP01A: 182 points).
- **Fix:** only one Make voice runs at a time (a second press while one ran made the two queue for the bridge lock and one gave up).

## T-099 — 2026-11-07 — Claude — test — 1.3.69
- **Card voice in the app** (Naven's profile only). New `js/voice.js`: splits a card into points (question; each lettered part, list line or table row, with lines that wrap joined back; WHY; WATCH), turns each into speakable text with a pronunciation list (units, ≥/≤/±/→, minus vs ranges, PEEP, P/F, PBW, FiO2, ECMO…), and keys each clip by a hash of its text, voice and prompt version, so a corrected line is remade and nothing else.
- Voice **Iapetus** (Naven's choice, 7 Nov, from six male samples), Gemini `gemini-2.5-flash-tts`, `en-IN`, brisk "consultant revising with a resident" style.
- On the card: **▶ Listen** plays the side in order; one button per point on the answer side plays from that point; **− / +** speed 0.8–2.0× (kept per device, pitch preserved). Clips are kept on the device after the first play (offline).
- On the deck page: a VOICE box shows how many points have their voice, with **Make voice** (the bridge makes 6 points a call; stops at the monthly limit).
- Checked in demo: MV01 (116 points), TOX01 TOX-13 table, RESP01B ARDS-26 (letters at the line end); no page errors. Audio itself needs the bridge, so it is checked on Naven's device.

## T-098 — 2026-11-07 — Claude — bridge — v6 (in progress)
- **Card voice, bridge side** (Naven, 7 Nov: Gemini voice only, so every device plays the same audio). New `backend/Voice.gs` beside `Code.gs`; `Code.gs` gains ops `voice`, `voiceIndex`, `voiceUsage` and `VERSION = 6`; `backend/appsscript.json` now lists its scopes explicitly and adds `cloud-platform`.
- Speech comes from Google Cloud Text-to-Speech, Gemini model `gemini-2.5-flash-tts`, `en-IN`, MP3, under the owner's own sign-in (no API key). One file per point of a card in `Trace › voice › <DECK>` with an `index.json` (part key → file, text hash, seconds, voice); a changed text is remade, an unchanged one skipped.
- Hard monthly limit in the bridge (`VOICE_LIMIT_SEC`, default 10 h of audio), because Google cannot cap Text-to-Speech spending.
- Google side, set up in Naven's browser on his instruction: Cloud project `trace-voice` linked to his billing account with the Google Developer Program credit (₹3,809 a month); Cloud Text-to-Speech enabled; budget "trace-voice alerts" (₹3,500, emails at 50 / 90 / 100 %, counted before credits); OAuth consent in testing with Naven as the only test user; the Apps Script project moved to this Cloud project.
- Applied to the live Apps Script editor (the private key line untouched). The new Cloud project also needed Google Drive, Sheets, Calendar and Agent Platform (Vertex AI, required by the Gemini voices) APIs enabled. Naven authorised; `authorise` ran clean (Drive + Sheet) and `authoriseVoice` made the first clip (7 s, Kore, `Trace › voice › _samples › hello.mp3`).
- Deployed as Apps Script version 7 of the existing web-app deployment (same URL, description "trace bridge v6 (card voice)"); `doGet` answers `version: 6`. Next: voice samples to choose from, then the app side (Listen and ▶ per point, speed, offline audio) in test.

## T-097 — 2026-11-07 — Claude — live — 1.4.17
- Promoted test 1.3.68 to live on Naven's instruction (7 Nov: "Promote"). Same copy rules as T-082 (every file in `test/` except `index.html` and `manifest.webmanifest`); `CONFIG.onlyDecks` stays `null` on live.
- Live gains T-095 (viva layer P4: Viva page, Mosaic chip, question-ordered walk with bridges and spine card, NEET | Viva explain, 34 viva cards) and T-096 (Naven's profile only), and the 12 further card-text corrections (`data/cardfix.json`, 60 cards).
- Checked before release (demo, live path, every deck): version 1.4.17, 62 decks, 60 corrections, 224 viva steps, a walk through P4-198 to its spine card; HT's profile shows no viva; no page errors.

## T-096 — 2026-11-07 — Claude — test — 1.3.68
- Viva is shown on Naven's profile only (Naven, 7 Nov: "Viva mode only appears for me"). On HT's profile `viva.js` loads no package, so there is no Palace tile, Flow-tab box, Mosaic chip, viva cards or viva explanation. Checked in demo on both profiles.

## T-095 — 2026-11-07 — Claude — test — 1.3.67
- **Viva layer, package P4** (Naven, 7 Nov: a Viva option in the Mosaic that groups the P4 cards in study order, viva mode elsewhere, its own viva explanation). Package file `test/data/viva/P4.json` (version `P4.20261107.4`, written by the content chat to the spec in the CCM project, `claude/Trace_Viva_File_Spec_7Nov.md`) and 6 SVG diagrams in `test/data/viva/img/P4/`. New module `js/viva.js`.
- **34 viva cards** sit at the end of their decks after the Top-ups, with permanent codes `V4-001…` and numbers `4001…` (package × 1000 + card), so seen counts, hooks and ink never shift. VIVA chip, own chunk "Viva", blue corner on the tile. Not in `qbank.json` (that would move the TU positions).
- **Mosaic:** a VIVA chip row (one chip per package). On, it lights the package's 168 cards in place of the pools and walk chips; Flow lit walks them in question order (224 steps).
- **Viva walk:** each of the 48 questions opens with a question card (tier, generator, kind, id), then its cards with the package's bridge under each answer and any viva one-liners, then a **spine card**: 60 s timer, the 4–6 spine lines folded until asked or the time is up, Fluent / Patchy / Blank. A card already walked under an earlier question shows a "seen above" strip and is not counted or logged again. Deck maps and deck closes are skipped in a viva walk. Marks are kept per profile on the device (`kv vivaMarks`), not synced yet.
- **Viva page** `#/viva/P4`: the 48 questions by generator with tier and last mark; Walk all, walk one question, walk patchy + blank, Show in the Mosaic; warns if any step's deck is not on the device. Entry points: a small tile on the Palace, a box on the Flow tab, the Mosaic chip.
- **Explain:** the viva explanation (94 entries) shows in the Explain pane. A card with both NEET and viva explanations gets a **NEET | Viva** switch: Viva in a viva walk, NEET elsewhere.
- **Corrections:** the package's 15 exact edits (12 cards: ARDS-27, VNX-03 ×2, ARDS-40, WEAN-17, PLEU-21, PLEU-26, PADIS-18, PADIS-17 ×2, WEAN-05 ×2, MODE-13, RSC-25, WEAN-15) were checked and added to `test/data/cardfix.json` (now 60 cards, 43 decks).
- Loaded copy differs from the writer's file in one line: V4-021's last line ("RSC-03's endorsement … corrected by its correction box") was dropped, because RSC-03 is now corrected in its own text.
- `tools/viva/check_viva.py` checks a package before loading (spec §9): codes, decks, step cards, spine 4–6, last bridge null, caps, pictures, each `fixes.old` once. P4 v4: 0 errors.
- `sw.js` never caches `data/viva/*.json`; diagrams are cached as they load.
- Checked in demo mode (57 decks): Viva page, walk through P4-198 to its spine and marks, the NEET | Viva switch on RESP01A ARDS-03, the Mosaic (168 of 1,225 lit), the Palace tile, the 12 corrected cards rendered, phone width; no page errors.

## T-094 — 2026-11-07 — Claude — live — 1.4.16
- Promoted test 1.3.66 to live on Naven's instruction (7 Nov: "Make it live"). Same copy rules as T-082 (every file in `test/` except `index.html` and `manifest.webmanifest`); `CONFIG.onlyDecks` stays `null` on live, so live keeps every deck.
- Live gains T-093: `data/cardfix.json` (48 corrected cards in 36 decks shown as the card's own text, with a "Corrected 7 Nov 2026 · source" line), the MDR-12 QBank box removed, `sw.js` not caching cardfix.
- Checked before release (demo, live path): the layer loads (48 cards), HY2 CAR-01 shows the corrected table and source line, no page errors.

## T-093 — 2026-11-07 — Claude — test — 1.3.66
- **Checked text corrections now change the card itself** (Naven, 7 Nov: edit the answer rather than add boxes). New layer `test/data/cardfix.json` (version in the file): 48 cards in 36 decks, each entry replaces whole fields (`q`, `a`, `why`, `watch`) as Trace shows them. Source: the INI error register re-checked by four independent checkers against primary sources (CCM project `claude/Trace_Correction_Check_7Nov.md`, `claude/Trace_Correction_Boxes_patch_v2.json`); 22 of the 52 proposed boxes were rewritten and 4 dropped as not errors.
- Order on a card: Drive `cards.jsonl` → **cardfix** → the profile's in-app edits (`edits.json` / `edits-ht.json`). `store.js withFix()`; the editor's "original" is the corrected text. The Drive deck files are unchanged (the connector cannot rewrite their content cheaply); this layer is the source of truth for the corrected wording until they are rewritten.
- A small "Corrected 7 Nov 2026 · source" line sits under the answer of each corrected card.
- Removed the QBank-layer correction box on CCM06 MDR-12 (now folded into the card text). `qbank.json` version bumped.
- `sw.js` never caches `data/cardfix.json` (same as qbank/qmap).
- Test now also carries the 34 corrected decks (`CONFIG.onlyDecks`). Checked by rendering 20 of the corrected cards in demo mode (tables, bullets, source line).

## T-092 — 2026-11-06 — Claude — live — 1.4.15
- Promoted test 1.3.65 to live on Naven's instruction (6 Nov: "do that and promote"). Same copy rules as T-082. Live gains T-090 and T-091.

## T-091 — 2026-11-06 — Claude — test — 1.3.65
- **Primer and story always on the card** (Naven, 6 Nov: "make it stay there always… open during regular flow, collapsed that can be opened during revision"). Every card of a deck with a spine now shows "WHAT YOU NEED FIRST" and "THE STORY SO FAR · STEPS 1–n" (all steps before the card's own), the same on every walk, so marks on them always have a home. They are open while the card is at Learn depth and folded (tap to open) at Revise depth — the same rule and per-card override as the Explain pane. Replaces T-088's flow-dependent "first in flow" / "steps not yet covered" logic (`arcFor` removed).
- Marks on a folded box are kept as saved and hidden; they come back when it is opened (relayout on each box's `toggle`). Marks made inside a primer/story block are anchored to that block.
- Checked in a demo: open on a new card; folding hides the primer highlight, opening restores it in place; tapping the box header doesn't reveal the card; story ranges per card (ARDS-01 steps 1–3, ARDS-02 1–4). No console errors.

## T-090 — 2026-11-06 — Claude — test — 1.3.64
- **Pen tools on the primer and story boxes** (Naven, 6 Nov: "can't touch, can't highlight, can't ask Claude" there). The boxes now sit inside the question face, so pen, highlighter, Select text (Highlight, Copy, Ask ▸) and lasso all work on them. Tapping a box no longer reveals the card. Their text blocks carry fixed keys (`arc:primer`, `arc:s<step>`, `arc:before`, `arc:bridge`), appended after the card's own anchors, so they never renumber the card's existing marks. A mark on a story box that isn't shown in a later flow is kept as saved and hidden, not drawn over the question.
- **Fix: question-side marks looked lost after Reveal → Question.** The face was measured while the flip animation was still running, so marks were placed off the text. Ink layers are measured again after the animation (260 and 520 ms). The saved ink was never lost.
- Checked in a demo: highlight on the RESP01A primer and on a TOX01 question heading both survive Reveal → Question; Select-text bar (Highlight, Copy text, Ask ▸) opens on the primer; tapping the primer doesn't reveal. No console errors.

## T-089 — 2026-11-06 — Claude — live — 1.4.14
- Promoted test 1.3.63 (= 1.3.62 plus the version bump) to live on Naven's instruction (6 Nov: "Promote"). Same copy rules as T-082. Live gains T-088: the deck-story arc (step line, primer, story so far), RESP01A explanations with its two card corrections, and the audited, re-checked Toxicology explanations.

## T-088 — 2026-11-06 — Claude — test — 1.3.62
- **Explain v3: written from the real questions, with a story arc** (Naven, 5–6 Nov: every addition must change answering capacity; give each deck an arc so any card, even in any-hit flows, makes sense).
  - `tools/explain/qpack.py <DECK>` gathers every real question linked to each card (DocT QBank with cohort % right, DocT GTs, Marrow, NEET 2024/2025 recalls) into `tools/explain/qpack/<DECK>.md`. Writers work from these; "How it is asked" items carry their source tag; traps come from low-cohort distractors.
  - **Deck story:** `SPINE` (4–6 steps), `PRIMER`, and a `step` per card (`BRIEF_v3.md`, `check_learn.py`). The app shows "STEP n OF N · title" on the explanation; on the question face, the primer the first time a deck appears in a flow, and "BEFORE THIS · THE STORY SO FAR" with the takeaways of earlier steps not yet covered in this flow (each summarised once). Code in `explain.js` (`spineOf`, `stepHtml`, `arcHtml`) and `app.js` (`arcFor`).
- **RESP01A** (ARDS I, 13 cards): written v3 from 23 linked questions, independently fact-checked (11 fixes). Card corrections on ARDS-04 (HFNO in Berlin vs 2023) and ARDS-07 (TRALI is indirect).
- **Toxicology audited against the real questions** (all 7 decks, 257 linked questions): about 265 points added where a question needed them, about 355 cut that no question needs; every decode item rewritten from real stems with source tags; every question under 60% right now has its trap. The additions were then fact-checked by two independent agents (9 fixes: e.g. HBO in pregnancy, the osmolal-gap threshold, atenolol dialysability, the labetalol guideline year). Logs: `tools/explain/<deck>_audit.md`, `<deck>_audit_review.md`.
- Test carries RESP01A as well (`CONFIG.onlyDecks`).
- Checked in a demo: RESP01A walk (primer and story-so-far on the first card, step line on every card, corrections box on ARDS-04/07) and TOX04 walk; no console errors.

## T-087 — 2026-11-06 — Claude — live — 1.4.13
- Promoted test 1.3.61 (= 1.3.60 plus the version bump) to live on Naven's instruction (6 Nov: "Ok promote"). Same copy rules as T-082. Live gains T-086: the duplicated-rooms fix, rooms under table rows, ⌃ one space less, Move to card, Plan Undo kept on the device and always visible, quick-intent suggestions.

## T-086 — 2026-11-05 — Claude — test — 1.3.60
- **Fix: writing rooms showed several times over** (Naven's photo, 5 Nov). Mounting ink again on the same answer face (switching Learn/Revise does this) left the old rooms, chevrons and canvases in place, so the same ink appeared once per remount. `mountInk` now clears them first. The saved ink itself was never duplicated.
- **Rooms, more carefully:**
  - Every **table row** of an answer is now its own answer point with its own room (key `row<t>:<r>`). Before, answer tables had no rooms.
  - Boxes without a known name (e.g. the correction box) no longer share one room key.
  - **⌃ One space less** sits beside ⌄ while writing; it never cuts into ink already written.
- **Move to card** in the Select-text bar on Explain: the selected words land on the card as a typed note on a pale sticky, already selected so they drag at once. To add words, tap the note with the Text tool (T). Text notes now measure multi-line size correctly for lasso and moving.
- **Plan Undo** is always visible in the Plan's top bar (greyed when there is nothing to undo) and its history (last 40 changes) is kept on the device, so it survives closing the app.
- **More quick intents**: ⚙ › Claude chats › Quick intents has a "Suggestions · tap to add" row (Pathophysiology, Differential, Steps in order, Doses & why, Guideline now, Clinical case, What was asked, Quiz me 3, Simpler, Table, Check card) besides "+ Write your own".
- Checked in demo runs: rooms through ⌄ ×4 and Learn/Revise switches stay single; table rows have rooms; ⌃ shrinks back to the ink; Move to card; every Flow ⚙ setting (Explain open/tap, depth Auto/Learn/Revise, traps, page colours, pen tools top bar/floating) changes what it should; Plan repair ↑↓, remove + undo, Change today undo. No console errors.

## T-085 — 2026-11-05 — Claude — live — 1.4.12
- Promoted test 1.3.59 to live on Naven's instruction (5 Nov: "Yes, promote them"). Same copy rules as T-082 (root keeps `index.html` and `manifest.webmanifest`; `onlyDecks` is null on live). Live gains T-083 and T-084: Explain v2 for all 7 Toxicology decks and the card corrections.

## T-084 — 2026-11-05 — Claude — test — 1.3.59
- **Corrections to the Toxicology cards, shown on the card and in Explain** (Naven, 5 Nov: "wherever you find corrections, put it there… with a mention in the explanation").
  - 33 corrections on 30 cards (TOX02–TOX06), curated from the writers' and reviewers' flags. Only real errors or outdated guidance; notes like "source-specific" or "card is correct" were left out.
  - On the card's answer side they appear in the existing **CORRECTION · CHECKED** box (with the bank fixes): "Card: <what it says>" struck through, then the right version in bold.
  - In the Explain pane, a **CORRECTION TO YOUR CARD** section follows "What's going on" (Learn) and comes first in Revise.
  - The card text itself stays unchanged (AGENTS.md §3.6); the corrections sit in `explain.json` as `fix`. Source: `tools/explain/tox_corrections.py`, built by `build_explain_v2.py`.
- Checked in a demo (ONC-11): the box on the card and the Explain section both show; no console errors.

## T-083 — 2026-11-05 — Claude — test — 1.3.58
- **Explain v2 for every Toxicology deck** (Naven, 5 Nov: "rewrite all the toxicology decks… keep an agent for secondary checkup"). TOX02, TOX03A, TOX03B, TOX04, TOX05 and TOX06 (81 cards) now have Learn/Revise explanations in the TOX01 style: what's going on, part by part with the why, mimics, traps, how it is asked, punchline last. No hooks or mnemonics. Card text unchanged.
  - Each deck was written by one agent and then fact-checked by a second, independent agent with web sources. The reviewers fixed 80 problems in all; about 40 were factual. Examples: physostigmine contraindications and dantrolene in REC-12; ASV premedication (SNAKE-11); the pralidoxime evidence (PEST-11); trastuzumab vs 5-FU/bevacizumab cardiotoxicity (ONC-11); EXTRIP criteria for paracetamol (APAP-12).
  - Sources: `tools/explain/tox0*_learn.py`, with the reviews in `tox0*_review.md`. The briefs are `BRIEF.md` and `REVIEW_BRIEF.md`; the checker is `check_learn.py`. The build is `build_explain_v2.py`, which now builds every deck that has a `<deck>_learn.py`.
  - **40 card flags** (where the card text looks wrong or outdated) are in the CCM project doc `claude/TOX_Card_Flags_5Nov.md`. The cards are not edited; Naven decides.
  - The few bank Top-ups of TOX03B, TOX04 and TOX05 (5 cards) have no Explain yet.
- Test build now carries the 7 Toxicology decks (`CONFIG.onlyDecks`).
- Checked in a demo walk through every TOX02–TOX06 card: each shows its Explain with all parts and the punchline; no console errors.

## T-082 — 2026-11-05 — Claude — live — 1.4.11
- Promoted test 1.3.57 to live on Naven's instruction (5 Nov: "make the app live also").
  - Copied every file in `test/` to the root except `index.html` and `manifest.webmanifest` (live keeps the name and title "Trace"). New in the root: `js/explain.js`, `data/explain.json` (Explain v2, TOX01 only for now; other decks show the card alone).
  - `CONFIG.onlyDecks` is `null` on live, so live keeps every deck.
  - Live gains everything from T-069 to T-081: Explain v2 (Learn/Revise) for TOX01; flow v3 top bar, strip and two-button bottom bar; card | Explain split with per-side size slider, Fit and pinch; page colours; ink on Explain, Select text, move marks between sides, side-button eraser; Ask Claude with quick intents and chats; Study desk look-up line; the flexible Plan, Change today and Undo.
- Checked before release (demo, live path, decks TOX01 and ABG01, 1400×1000 and 412×915): Flow opens, Reveal and Next work, Explain shows only where it exists, no console errors.
- Not yet checked on the real Tab: S Pen side-button eraser, pinch, Select text.

## T-081 — 2026-11-05 — Claude — test — 1.3.57
- **Repair pile moves like a subject** (Naven, 5 Nov). Its sheet has ↑ Earlier / ↓ Later, so it can sit anywhere among the subjects; subjects' ↑↓ now step over it too. Stored as `st.repair.at` (row index); older plans read `pos` first/last as 0/end. The first/last switch is gone.
- **Undo for the Plan.** Every change keeps the plan as it was (this session, last 40). "↶ Undo last change" on the Plan screen (also after deleting the only stretch) and "↶ Undo" in Change today. Removing a subject or deleting a stretch says where Undo is. Change today's old "Undo today's changes" is now "Reset today".
- Checked in a demo run: repair moved between two subjects, subject up past it, remove + undo, Change today − then Undo.

## T-080 — 2026-11-05 — Claude — test — 1.3.56
- **Quick intents in the Ask menu** (Naven, 5 Nov). The menu now asks *what* before *where*:
  - Chips: Explain, Normal value, Mechanism, Basics first, Compare, Why wrong, Exam angle, Connect. Most-used first; the last one used is preselected. Tap again to clear.
  - A free box, "Or ask in your own words…". With a chip it is added under the chip's line; alone it replaces it.
  - The template's ask line is now `{ask}`. A custom template without `{ask}` gets its old "Explain this part properly…" line replaced, or `{ask}` appended.
  - ⚙ › Claude chats › Quick intents: edit each button's name and line, add, remove, reset (`P aiIntents`, use counts in `P aiIntentUse`).
- **Flexible Plan.**
  - Repair pile: walked first or last in the day; spread evenly, finish by a date, or a fixed number a day; the cap still applies to the spread modes (`st.repair.pos/spread/by/fixed`; older plans read as first + even).
  - Subjects: In order, Evenly, Fixed a day, Finish by (stored on the existing `mode/daily/to`).
  - **Change today** sheet (Plan › Change today…): per row ↑↓ for today's walk order (`st.order[day]`), − + by 5 (a today pin; pins may now go over the day's room), "Finish today (n)" to go deep on one subject, "+ Add for today only" (a subject with `once`, from = to = today; it drops out after today), and "Undo today's changes". The other days re-plan from what is left.
  - `todayCards`/`todayParts` follow the day's order. The grid shows the repair row first or last to match.
- Checked in a demo run at 1400×1000: plan sheets, Change today (order, ±, finish today, undo, add for today), the Ask menu message with an intent + own words, the intents editor. No console errors.

## T-079 — 2026-11-05 — Claude — test — 1.3.55
- **Study desk in Drive** (Naven, 5 Nov). The card library is reachable from a Claude chat through Google Drive.
  - New folder `Trace › Study desk` (id `1X2wz4GPfK_FvnqX536xKjGi1DenfrbKK`) holds `00 INDEX` (every deck with its system, card count, card-ID range, and how to find its cards) and the readable explained file for TOX01.
  - The other decks are read straight from their existing `Trace › decks › <DECK> › cards.jsonl`, so they are always current.
  - Generator: `tools/studydesk/studydesk.py` (it can also write a readable file for every deck).
- **The Ask template now ends with a look-up line:** card {code} in deck {deckid}, find it via the Study desk index, link related cards and cite their IDs. New placeholder {deckid}.

## T-078 — 2026-11-05 — Claude — test — 1.3.54
- **Bottom bar: two buttons.**
  - Left button: **‹ Back** (look at the previous card) on the question side; **‹ Question** (flip back to this card's question, nothing logged) on the answer side; **Further back** while looking back.
  - Right button: Reveal, Next, or Back to current. Q on a keyboard also flips back.
- **Top bar in one line.** Undo, Pause and Going out are icons only (names on long press), and Back moved to the bottom bar.
- **One progress strip.** The count (e.g. 4/30) now leads the strip of tiles; the top-bar count and dial are gone. The title reads "Chunk · cards 3–8".
- **Ask ▸ in the Explain header.** The per-trap "ask why" buttons are removed: they sat under the ink layer and could not be tapped while writing.
- **"→ Move to card" / "→ Move to Explain"** in the selection bar moves lassoed marks to the other side. Dragging them across the divider also works; checked in the demo.
- **Side-button eraser with the pen tools closed.** The proven side-button signature (pen moves with buttons 1, pressure 0, no press, held 70 ms) switches writing on quietly (no toolbar) and erases; 700 ms after the pen goes quiet it switches back. A normal pen touch ends it at once and never draws.

## T-077 — 2026-11-05 — Claude — test — 1.3.53
- **Ask Claude** (Naven, 5 Nov). Claude can't receive a message into an existing chat from a link, so Trace copies a ready question and opens the chosen chat; you paste and send.
  - **Where to start an ask:**
    - "Ask ▸" in the Select-text/lasso bar (the selection);
    - "Ask ▸" in the card header (whole card);
    - "ask why" on each Exam trap line.
  - **The menu:** your chats (the last used one marked), New chat (pre-filled; opens `claude.ai/new?q=…`, not yet confirmed on the Tab), Search Google, Manage chats…
  - **⚙ › Claude chats:** add and remove chats (name + `claude.ai/chat/…` link; ChatGPT and Gemini links also accepted), plus an editable message template with {deck} {code} {title} {question} {answer} {selected} {from}. Kept per profile.
  - Chats open in one named browser tab (`trace-claude`), so asks reuse it.
  - Every ask is logged on the device (`kv.askLog`, last 500).
- Selected text no longer starts with the part's letter ("aEmpirical …").
- Demo check: added a chat, asked about the whole card and about a selection; the link opened and the clipboard held the filled template. No errors.

## T-076 — 2026-11-05 — Claude — test — 1.3.52
Naven's Tab check of 1.3.51, with photos. An independent QA run (Playwright at 1848×1100, 1100×1700 and 412×915 touch) checked the fixes; its bugs are fixed and re-checked.
- **Each side owns its header.**
  - Card: section, code, tags, Edit, Again, Fit and size.
  - Explain: Explain, size, Learn/Revise.
  - Both headers sit outside the scrolling area, so no text shows above or behind the Explain header any more.
- **Zoom is applied to the content inside the scroller** (`.zw` on the card, `.xp` on Explain), not to the scroller itself. This fixes the card scroll jamming after several zooms (zoomed scroll containers in Chrome).
  - QA ran about 40 scroll checks per screen size across sliders, pinches, Fit, writing mode, Next and Back: all reached the bottom and came back.
- **Fit measures correctly.** It ignored the ink layer's old height; Fit from 200% fell to 55% even when the card fitted at 100%.
- **Writing rooms grow with the text** when a side is zoomed (×1.5 at 150%). A room also grows to hold ink written below its edge.
- **No false eraser.** The "mouse after pen" and context-menu side-button guesses are removed: a tap on the toolbar or a long press had armed or started the eraser. The proven signal (pen moves with buttons 1, pressure 0, no press, held 70 ms) is the only one left.
- **Top bar.**
  - The title is always readable and ⚙ always stays on screen, pinned or floating.
  - The pinned pen tools reserve their open width (510 px until first measured), so writing on/off or folding never moves other buttons. QA: 0 px horizontal shift.
  - When one row doesn't fit (Tab portrait, phone), row 1 = title, progress, time, ⚙ and row 2 = Back, Undo, Pause, Going out and the pen tools. On the phone the pen tools wrap instead of running off screen.
- **Subtle size slider.** No black capsule: a thin track, a small white thumb, a muted label; Fit is a light outline chip.

## T-075 — 2026-11-05 — Claude — test — 1.3.51
Naven, 5 Nov: "remove the swipes … go back to the old zoom … page colour … pin".
- **Swipes removed.** Only the Next button turns cards; the ⚙ Next-button and swipe options are gone.
- **Size back to re-flowing zoom.** Each side has one slider (50–200%) and a two-finger pinch, both changing the same size, so the text re-flows.
  - The card also has **Fit** (whole card in view, not below 55%); the slider and pinch turn Fit off.
  - The T-074 fixed-page layout and the A−/A+ buttons are removed.
  - Explain's own bar keeps its size while Explain is zoomed.
- **Page colour** in ⚙: White · Soft grey · Cream · Mint, for the card and Explain (per profile).
- **Pin button in the pen kit**: pinned in the top bar ↔ floating.
  - When pinned, the tools keep one fixed slot in the bar (≥500 px on wide screens), folded or open, so the other buttons never move.
- The colour button is one dot with one thin ring (it had two rings).
- Demo check: Cream page, Explain at 130%, pin → floating; no errors.

## T-074 — 2026-11-05 — Claude — test — 1.3.50
Agreed with Naven on 5 Nov ("Yes, proceed").
- **Highlights sit behind the words.** Ink canvases use a multiply blend, so the paper turns yellow and the letters stay black.
- **New Select-text tool** (I-beam) in the pen kit.
  - Drag from the first word to the last and exactly those words are taken, snapped to whole words, across lines and parts. A tap takes the whole part.
  - The same bar follows: Highlight · Copy text · ? Still unclear.
  - The lasso is now for moving ink. When drawn over words, it only takes lines whose middle lies inside the loop.
- **Pen tools docked in the top bar.** Folded, they are one pen button; tapping the grip folds them. In portrait they take a second row. ⚙ › Pen tools: In the top bar / Floating.
- **Each side has its own text size** (A−/A+ on the card and on Explain). The bar's A−/A+ and Fit/Width are gone.
  - **Zoom is PDF-like.** The text is laid out once at the page width for 100%; a pinch only magnifies or shrinks that page, so lines never re-wrap.
  - Zoomed out, the page sits centred on white; zoomed in, it scrolls both ways (safe centring).
  - The zoom readout is a button that resets to 100%. Size and zoom are kept per profile and per side.
- **Two-finger gestures** on the card area.
  - Swipe: both fingers move the same way, at least 90 px within 0.7 s, at a steady distance. It turns the card: forward reveals, then goes next; back looks at the previous card.
  - Pinch: the distance changes. It zooms the side under the fingers.
  - ⚙ › Next button Show/Hide · 2-finger swipe ↔ sideways / ↕ up-down. Both swipes off forces the button back.
  - Vertical swipes animate vertically.
- **The flow's label** (Plan, Any hit …) moved out of the top bar to a gold chip at the start of the strip, where it can't be cut off.
- **Pure white card and Explain.** Boxes are neutral grey; the NEET gold glow around the card is reduced to a thin grey edge (the NEET tag chip stays).
- Demo check (Tab landscape, touch via CDP): pinch to 280% and to 45%; a two-finger left swipe reveals; Select-text gives the bar; Highlight lands behind the text. No errors.

## T-073 — 2026-11-05 — Claude — test — 1.3.49
Naven's Tab check of 1.3.48.
- **Draggable divider** between the card and Explain: side by side in landscape, stacked in portrait. Limits 22–78%, remembered per profile and orientation; double-tap resets it.
- **Lasso over words selects the words** (when no ink is inside the loop), on either pane. Bar: Highlight (snapped highlights that keep their words) · Copy text (system clipboard) · ? Still unclear (Explain only).
- **Highlighter snap is automatic, with no On/Off.** It snaps only when the stroke starts on words; beside or after a line it draws freely. Before, the snap also caught empty space to the right of the text.
- **Marks dragged with the lasso from one pane onto the other now move there** (Explain ↔ card), converted to that pane's units. Text-tied highlights become free marks.
- **No more false orange eraser on the first touch after picking a tool.**
  - The side-button signature (pen moves with buttons 1, pressure 0, no press) must now hold for 70 ms.
  - It never counts within 250 ms of, or during, a real pen press anywhere on the page.
  - A real press cancels it.
- **Tap a tile in the strip** to look at that walked card (the same look-only Back); the current tile brings you back. The tile you're looking at is outlined.
- **Readout:** a progress number with a thin bar replaces the round dial; time, per card and versus average sit in one quiet box.
- Removed the "explain vXXXX" version tag under each explanation.
- Demo check: divider drag, tile jump (shows 2 cards back), lasso over Explain text shows the bar; no errors.

## T-072 — 2026-11-05 — Claude — test — 1.3.48
Naven's notes from the Tab, 5 Nov: more room for the card and Explain, a PDF-like fit, ink on Explain, and the broken timer.
- **Flow layout v3.** The left panel is gone:
  - **One slim bar:** ✕, deck and section, progress ring, time, per card and versus average, then Back, Undo, Pause, Going out, A−/A+ and ⚙.
  - **⚙ pop-up:** the Explain settings and the key hints.
  - **One strip:** this flow's tiles plus Today's thread on a single line; tap it to open the full tiles with the thread beads.
  - The card and Explain panes get the rest of the screen.
- **Fit like a zoomed-out PDF.** Each pane has **Fit · Width · %**:
  - Fit scales the pane with CSS zoom until the whole card is in view (minimum 55%). The text stays live, so ink, highlights and copying keep working.
  - A two-finger pinch sets a custom size; double-tap switches between Fit and Width.
  - Kept per profile. Defaults: card Fit (Width on phones), Explain Width.
- **Ink on the Explain pane.** It has its own ink layer, saved per depth (Learn and Revise lay out differently).
  - Highlights snap to the explanation's lines. Pen, eraser, lasso and the clipboard work as on the answer.
  - A lasso selection on Explain offers **? Still unclear**, which saves the words on the device (`kv.xpUnclear`) for the next rewrite.
- **The circled letters open the writing room** for their part, in place of the ⌄ chevron. A letter is filled while its room is open and ringed once it holds ink. Lines without a letter keep the chevron.
- **Going back animates in reverse** (Back and browse ←).
- **Timer and "where were you?" fix.**
  - Cause: a leave time left behind when Chrome dropped the tab made the flow clock negative (−20:−1:−33 on Naven's Tab). It also brought back "where were you?" on every switch.
  - Now:
    - the latest leave time is always the one used;
    - away time can never exceed how long the flow has run;
    - a mark older than 12 h is dropped, and so is a "just checking" gap older than 12 h;
    - the question appears only after 5 minutes or more away.
- Demo check (Tab landscape, Pixel 7): no errors; TOX-07 fits at 92% on the Tab.

## T-071 — 2026-11-05 — Claude — test — 1.3.47
- **Fact-check corrections to the TOX01 Explain v2 texts.** An independent reviewer read all 30 explanations against the cards. It found 1 error and about 15 misleading or minor points; all are fixed in `tools/explain/tox01_learn.py` and `tox01_topups_learn.py`:
  - TOX-11: EXTRIP prefers high-flux haemodialysis for phenobarbital, carbamazepine, theophylline and valproate; haemoperfusion is the classic textbook answer (was: "dialysis removes little").
  - TOX-01: thiamine deficiency acts over hours to days, not minutes.
  - TOX-03: sympathomimetic sweating comes from central sympathetic outflow.
  - TOX-05: 5-HT1A and especially 5-HT2A.
  - TOX-08: cyanide and H2S make no arterial saturation gap; the clue is a narrowed arterial–venous difference. The fire-victim stem now also names cyanide.
  - TOX-13: the parent alcohols are relatively non-toxic, not "harmless".
  - Top-ups:
    - QT: thioridazine wording.
    - SAT: methylene blue is an MAO inhibitor (serotonin syndrome).
    - ME: dimercaprol continues with EDTA; arsenic clears from blood in hours to days.
    - CA: airway reasoning (risk of can't-intubate, can't-oxygenate; blind nasal intubation avoided).
    - AS: the interneuron mechanism is marked as proposed; the trap now names class Ia/Ic (lidocaine is second-line after bicarbonate).
    - INH: lactate clearance.

## T-070 — 2026-11-05 — Claude — test — 1.3.46
- **Explain v2, TOX01 only** (Naven, 5 Nov: "do only one deck, in test also put that only deck"). Based on the analysis of HT's 34 annotated PDFs (CCM project doc `HT_PDF_Additions_Analysis_5Nov.md`) and Naven's handwritten notes.
  - **Learn** depth (shown on a card's first sight): subcategory line → What's going on → Part by part (each card letter restated, then the why) → table where a decision or comparison needs one → Close mimics → The traps ("X" is wrong. …) → How it is asked (stem → answer) → **Punchline last**. 240–510 words per main card; 14 rebuilt Top-ups get the same treatment.
  - **Revise** depth (from the second sight): How it is asked, traps, punchline, and a button for the full explanation. A Learn/Revise switch on the panel, and Auto/Learn/Revise in the Flow panel (under "Explain settings").
  - **No hooks or mnemonics, no deck map or deck close, no WHY gist line** (Naven: map cards confuse a first-time reader; the punchline must come after the explanation).
  - Data: `test/data/explain.json` v2, built by `tools/explain/build_explain_v2.py` from `tox01_learn.py` and `tox01_topups_learn.py`. RESP04's pilot explanations are no longer shipped.
- **Explain has its own scroll pane**: beside the answer in landscape, below it in portrait; the answer pane scrolls separately. Ink stays on the answer pane.
- **Flow: Back and Pause.** Back (‹, or ←) looks at cards already walked in this flow, without changing anything logged; looking-back time is not counted as card time. Pause (⏸, or P) stops the clock and covers the card; tap to resume.
- **Cards look like the PDFs**: white page, lighter tinted boxes.
- **Pick fix**: a picked NEET tile now shows the white pick ring outside its gold NEET ring (before, the gold ring hid the pick).
- **Test carries only TOX01**: `CONFIG.onlyDecks = ['TOX01']` in the test channel filters the library, downloads and screens; live is unaffected.
- Checked in the demo (Tab landscape, Pixel 7): shelf shows only TOX01; Learn, Revise switch, separate scroll, Back, Pause; no errors. A medical fact-check of the new texts was running at commit time; its corrections follow in the next entry.

## T-069 — 2026-11-05 — Claude — test — 1.3.45
- **Explain layer pilot** (Naven approved the pilot, 5 Nov) for **TOX01 and RESP04**. The design is in the CCM project doc `Explain_Layer_Design_5Nov.md`.
  - **Data:** `test/data/explain.json`, built by `tools/explain/build_explain.py`. It ships with the app, is stored in IndexedDB and works offline; the service worker does not cache it, like qbank.json. New module: `test/js/explain.js`.
  - **On the answer side:**
    - A **WHY** gist line, always visible.
    - An **Explain** panel. It holds a mechanism chain ending in the answer and one picture (fork, grid, number scale, trio, timeline). Then labelled blocks: Tempting but, Don't confuse, Rule, Numbers, Where it sits. Then an Exam trap block (respects the toggle), pattern chips that open one-page pattern sheets, a tap-to-open Deeper section, a "Your analogy" note saved on the device, and 👍/👎/too-long feedback saved on the device.
    - On screens 1280 px and wider the panel sits beside the answer; on narrower screens it sits below.
    - The old Top-up and Crossfire boxes are replaced on cards that have an explanation.
  - **Exam add-ons:** the useful Top-up lines, rebuilt as extra lettered question/answer parts. They appear from the second time a card is seen.
  - **Rebuilt Top-up cards:** these replace the dense Top-up layer for these decks (`S.xtopups`, which wins over qbank topups in store.js).
    - TOX01: 14 cards — three new concept cards (drug-induced long QT; CO vs methaemoglobin; toxic alcohol: block or dialyse), four spot cards, and the 8 old Top-ups rewritten as lettered parts.
    - RESP04: 1 spot card (Nocardia).
  - **For Any-hit flows:**
    - A **deck map** page opens each deck: its ideas, the walked cards numbered, and skipped cards given as one line each.
    - A **Before this** bridge line appears when the previous card was skipped.
    - A **bridge card** (RSC-24 inside RSC-25) shows a short question with a Show-answer button. It is not counted.
    - A **deck close** page follows the deck's last card: a wrap-up and one recall question.
  - **Flow panel toggles:** Explain "Open on new cards / Only when tapped", and Exam traps "Show / Hide". Each profile keeps its own setting.
  - **Fact check:** an independent fact-check agent reviewed all content; 4 contradictions and about 15 misleading or minor points were fixed before release (labetalol in cocaine, NIV failure mortality in LUNG SAFE, the QRS scale labels, the QT pattern, phenytoin, charcoal timing for paracetamol, MetHb SpO₂ wording, Nocardia duration, radiation dose, thiamine regimen, gist lengths).
  - **Tested in the demo** at 1480×924 and on a phone: TOX01 all-cards flow, and RESP04 Any-hit (map → 4 hits with bridges → Top-up spot card → deck close → done). No errors.

## T-068 — 2026-11-04 — Claude — live — 1.4.10
- Promoted test 1.3.44 to live on Naven's approval (4 Nov 16:30: "update that also into the live up first"). Live gains:
  - the whole ink feature (T-057 to T-066): floating pen strip, pen and highlighter, eraser with the S Pen side button, lasso with resize and rotate, auto shapes, text, rooms under lines, clipboard history, multi-window;
  - the folded Top-up and Crossfire boxes (T-067).
- Checked on a copy of the live root with demo data: Flow opens, the boxes are folded, and the ink regression script passes.

## T-067 — 2026-11-04 — Claude — test — 1.3.44
- **Top-up lines and Crossfire are folded by default.**
  - **Why:** HT found the toxicology cards too dense, gave up on them and went back to her PDFs (4 Nov). The diagnosis is the Top-up layer itself, not toxicology:
    - 658 cards carry 1–5 lines of about 280 characters each, often 2–3× the card's own answer. On TOX-07 the card is about 400 characters and its Top-up box about 1,200.
    - Each line is a compressed QBank explanation with no question shown, with citations, numbers and lists of distractors.
  - **Change:** both boxes are now `<details>` elements shown as "TOP-UP LINES · n · tap to open". Opening one re-anchors any ink on the card.
  - **Next, waiting on Naven:** rebuild the lines as short question-and-answer parts, starting with TOX.

## T-066 — 2026-11-04 — Claude — test — 1.3.43
- Resize and rotate a selection (Naven, 4 Nov 16:16).
  - **Handles:** the selection box has four corner handles and a round rotate handle on a stalk above it (below the box when there is no room above).
  - **Resize:** dragging a corner scales the selection evenly about the opposite corner; strokes, highlights and text grow with it.
  - **Rotate:** turns about the centre of the box and snaps at every 15°. Before turning, rectangles, rounded rectangles, ellipses and triangles become point outlines, and highlights snapped to words become free highlight bands. Text turns with a stored angle.
  - Both are computed from the original marks on every move, so nothing drifts, and both can be undone.
  - **Checked:** in the demo, doubled a squiggle and turned another by 90°.
- A Pages deploy had failed with a GitHub server error (502) on the 1.3.41 and 1.3.42 pushes; Naven saw the test build stuck on 1.3.40. One run was re-run; this push deploys everything.

## T-065 — 2026-11-04 — Claude — test — 1.3.42
- Clipboard history (Naven, 4 Nov 16:11).
  - **What it keeps:** the last 12 copies or cuts, newest first, in `trace.ink.clips`. The old single clip is carried over.
  - **The panel:** the clipboard button on the strip shows how many items there are and opens a panel. Each item has a picture of its ink, a number, how many marks it holds and how long ago it was copied, plus ✕ to remove it. There is also a Clear clipboard button.
  - **Pasting:** pick an item (it is outlined and tagged "tap the card"), then tap where it should go, on this card or any other. Items stay in the clipboard so they can be pasted again; the panel closes after each paste.
  - **Checked:** in the demo, three copies, paste of a chosen older item.

## T-064 — 2026-11-04 — Claude — test — 1.3.41
- S Pen side-button erase confirmed working on Naven's Tab (4 Nov 16:07: it erases and turns orange). He noticed a small lag, so this release makes it faster:
  - It also listens on `pointerrawupdate`, which arrives sooner than `pointermove`.
  - Erasing starts on the first `pointerover` that already has buttons 1.
  - The path between samples is filled in, so fast rubs don't skip ink.
  - Erased ink is redrawn at once instead of on the next frame.
  - An orange eraser ring follows the pen.
- The "armed" flag is cleared when a side-button erase ends, so the next normal stroke writes.
- A **Clear log** button was added to the pen test.

## T-063 — 2026-11-04 — Claude — test — 1.3.40
- S Pen side button, third pen-test log (4 Nov 16:03; 1.3.39 neither erased nor turned orange).
  - **What the log showed:** with the button held, touching the glass sends **no pointerdown**. The pen arrives under a new pointer id as moves with buttons 1 and pressure 0. A normal stroke has a pointerdown and pressure above 0.
  - **New rule:** while writing, pen moves with buttons 1, pressure 0 and no pointerdown erase along their path. The eraser icon turns orange, and erasing ends when the buttons go back to 0 or the pen leaves. The earlier rules stay as fallbacks.
  - **Checked:** in a simulated run of that exact sequence, the earlier stroke was erased and the icon turned orange.

## T-062 — 2026-11-04 — Claude — test — 1.3.39
- S Pen side button, second pen-test log from Naven (4 Nov 15:56).
  - **What the log showed:** no button bits and no context menu. The pen keeps reporting as a pen (buttons 1 while touching), and a separate `pointerover · mouse` pointer appears when the side button is pressed.
  - **New rule:** while writing, and with a pen used recently, that mouse pointer appearing arms the eraser. The next pen stroke erases; a stroke already in progress switches to the eraser. It disarms when the stroke ends or the mouse pointer leaves. The eraser button on the strip turns orange while armed.
  - **Pen-test log:** now shows pointer ids and compatibility mouse events (`mousedown` / `mouseup` / `auxclick`).
  - **Checked:** with simulated events, a pen stroke followed by a mouse-over and another pen stroke erased the first.

## T-061 — 2026-11-04 — Claude — test — 1.3.38
- S Pen side button, from Naven's pen-test screenshot (4 Nov 15:44). On the Galaxy Tab, Chrome never reports the side button as a pen button. While the button is held, the pen turns into a `mouse` pointer (button -1, buttons 0) and a `contextmenu` fires. That menu also caused text selection and Google's "Tap to search" bar.
  - Now, while writing, a `mouse` pointer within 20 s of real pen use, or a context menu on the card, starts erasing. Erasing follows the pointer until the pen comes back as a pen, leaves, or goes quiet for 450 ms. A real mouse on the Mac (no pen seen) still draws.
  - While writing, text selection and the long-press menu are blocked on the card.
  - The pen-test log now records every event, collapses repeats with a count, adds timings and keeps 18 lines.
  - Checked with a simulated Samsung event sequence: a pen stroke, then mouse-over, context menu and mouse moves erased it.

## T-060 — 2026-11-04 — Claude — test — 1.3.37
- Ink round 3 (Naven, 4 Nov 15:16):
  - **S Pen button.** Any pen button beyond plain contact now counts as erase. The eraser settings (tap the eraser twice) have a **Pen test** pad and a log of the last 8 pen events (type, button, buttons). This shows whether the Tab passes the side button to the browser at all.
  - **Auto shape.** Rewritten as a fit of every candidate shape: ellipse, rectangle, rounded rectangle at three radii, capsule, triangle and other four-sided shapes. The box is refined inward for shaky outlines. Upright four-sided outlines become rectangles; open strokes become lines or V shapes, and scribbles stay handwriting. It also works with the highlighter: a free highlight held still becomes a highlighter-style shape.
  - **Lasso.** Maximum sensitivity: an object is selected if any part of it lies inside the loop or the loop line passes within about 7 px of it. A single tap selects one mark.
  - **Selection bar.** Delete, Cut, Copy and Done; 8 colours applied straight to the selection; thinner and thicker. This replaces "Apply pen style", which did nothing.
  - **Clipboard inside the app.** Copy and Cut store the ink (kept in screen pixels), so it works on this card, the next card, any card or another split-screen window. A Paste button with a count appears on the strip; tap it, then tap where the ink should go, and it lands selected.
  - **Text.** The editor opens inside the card where the pen tapped. Its mini bar above has A−/A+, Bold, 5 colours, ✓, and Delete when editing. Tapping existing text with the Text tool edits it. Escape cancels; tapping away keeps the text.
  - **Rooms.** They no longer grow by themselves. A ⌄ at the end of the room adds one full space. When the pen moves to another area or writing ends, the room trims to the space used, in half spaces (2 spaces with half of the second used → 1.5).
  - **Writing limits.** Short, faint dotted marks at the ends of the top and bottom edges of every writing area (no box). The card gets 180 px of extra writing space at the bottom while writing.
  - **Multi-window.** Overlay ink is now saved relative to the block it was written on and stretches with it, so it is no longer hidden in a narrower window or at another text size. Snap highlights store their character range and follow their words when lines re-wrap. Ink saved in the old format still shows only on the same screen.
  - **Toolbar size and position.** The strip sizes itself to the window (30–44 px buttons) and keeps its position as a share of the window. Tapping the grip folds it into one movable round button showing the current tool; tapping that opens the strip again. The floating pen button (not writing) can be dragged too.

## T-059 — 2026-11-04 — Claude — test — 1.3.36
- Ink fixes from Naven's Tab trial (4 Nov 14:20):
  - **Floating toolbar.** A vertical rail at the screen edge; it no longer pushes or covers the card. It can be dragged by its dotted grip, and a double-tap on the grip resets it. Settings and the selection bar open beside the rail.
  - **Tap behaviour.** Tapping a tool only chooses it. Tapping the chosen tool again, or the colour dot, opens its settings, and they close as soon as the pen touches the card.
  - **Pen button.** Removed from the card tags. A round floating pen button at the screen edge starts writing.
  - **Question side writable.** The question face is now a `div role=button` instead of a `<button>`. A tap reveals only when not writing. The overlay is no longer capped at 920 px.
  - **Highlights.** Snap-to-text and free highlights can be erased, selected by lasso or by a single tap with the lasso, moved and deleted. The fix is ink hit-testing by distance to segments, with snap highlights tested as a band.
  - **S Pen side button.** It now erases when held during hover, at touch or mid-stroke. The context menu is blocked while writing. The eraser settings show the last pen signal (`buttons` / `button`) for diagnosis.
  - **Auto shape.** The hold timer restarts only on movement over 5 px, so pressure jitter no longer resets it; it fires after 550 ms with a short vibration. The recogniser was rewritten: corners found on a closed ring, near-straight vertices dropped, and an ellipse-fit score. It recognises circles, ellipses, rectangles, squares, triangles, other four-sided shapes, lines and V shapes; scribbles stay handwriting. A unit check on synthetic shapes with jitter passed.
  - **Lag.** Redraws are batched once per frame, finished ink is cached in a layer while a stroke is live, and Chrome's predicted pen points are drawn ahead of the stroke.
  - **Icons.** All tool icons were redrawn; the pen and highlighter show the colour of their tip.

## T-058 — 2026-11-04 — Claude — test — 1.3.35
- Fix (Naven's Tab, 4 Nov 14:07): on the Tab every card showed a black body — the ink canvas was created with Chrome's low-latency `desynchronized` mode, which Android draws as an opaque black layer. Ink canvases now use the normal 2D context (transparent).

## T-057 — 2026-11-04 — Claude — test — 1.3.34
- **Ink on cards, stage 1** (Naven, 4 Nov: Samsung Notes look and tools): a pen button on every Flow card turns on writing. A dark Samsung-Notes-style toolbar opens above the card: Pen (Fountain pen, Pen, Pencil, Calligraphy, Brush; size as a number 0.5–20; 14 preset colours + 84 swatches + any colour), Highlighter (size 4–40, opacity %, **snap to text line** on/off), Eraser (stroke or partial, size, highlighter-only, clear), Lasso (select → move by dragging, apply pen style, copy, delete), Undo/Redo, Shapes (line, arrow, rectangle, ellipse, triangle; **auto shape**: draw, then hold), Text (size, bold, colour). Pen and mouse write; fingers scroll; the S Pen side button / eraser end erases while held; pressure changes width.
- **Write anywhere** on the question or answer side (overlay). It is tied to this screen's layout and text size (anchored to the block it was written on, so it moves when rooms open); on another screen size it is hidden with a note.
- **Rooms:** a small collapse button beside every answer line (a, b, c…, Top-up lines, Crossfire, Why, Watch) opens a lined room under that line; rooms scale to every screen, grow as you write, and in reading view show a faded peek (tap to open). The button turns into a pen mark when the line has a note.
- Stored per card on this device (`ink|deck|code`); sync across devices and images (needs a bridge update) come later.
- Tests: demo flow on a Mac-width screen — overlay stroke, snap highlight on a text line, auto-shape circle, room with ink, reading-view peek; saved to the device; no page errors.

## T-056 — 2026-11-04 — Claude — live — 1.4.9
- Promoted test 1.3.33 on Naven's approval (4 Nov, 03:49 IST: "I approve"): edit/remove Flow entries, plan subjects starting on any day (T-055).

## T-055 — 2026-11-04 — Claude — test — 1.3.33
- **Edit a Flow entry** (Naven: one card got walked by mistake, HEMO01A HDM-01 on 3 Nov 15:45 from the Mac): a pencil on each Trace Flow entry in the Loft's "Day in the chronicle" and Chronicles opens the entry's cards; remove one card or the whole entry. Removal is an undo (as Flow's Undo), synced to TraceEvents on live. The Sheet's Log row written by Trace for it stays (Log is append-only for the app); Naven can delete that row by hand if the War Map should forget it (note `Trace app · Tmw0j8nni0ogjq`).
- **The Plan:** a subject can start on any day of the stretch ("Starts on" in Add subject, Pick from the Mosaic, and the subject sheet); it works for "in order" and "a little every day" subjects; the row shows "from Fri 6 Nov".
- "Walk today's … in Flow" only shows when today has planned cards.

## T-054 — 2026-11-04 — Claude — live — 1.4.8
- Promoted test 1.3.32 on Naven's instruction (4 Nov, 03:22 IST: "bring the app live, which was in test"): The Plan (T-053) with Drive sync of `plan.json` / `plan-ht.json`, Mosaic Pick + walk chips, Flow thread, re-laid Loft. Also created Drive folder Trace › ht-notes (`1EghHqeR3Sn1CQZBOnZ2XowvRlM1gArCD`) for HT's Samsung Notes PDFs (Naven shares it with HT; she shares folder by folder, no renaming).

## T-053 — 2026-11-04 — Claude — test — 1.3.32
- **The Plan** (Naven + HT's idea, designed with Naven 4 Nov): Loft › "The Plan" opens a full-screen planner (`#/plan`, `js/plan.js`). A stretch = start date + days + pace (+ a catch-up ceiling). Rows are subjects, columns are days, every cell is a **number** (no colour coding; Naven is colour-blind). Repair pile is an automatic first row (pile ÷ days left, up to a daily cap). Subjects fill the days in order, or "a little every day" (n a day, or spread to a last day). Tap a day header → Normal / GT (20) / Half (30) / Off; tap a number → fix it (• mark); tap a subject → rename, order, mode, remove. "Doesn't fit" column + verdict with the three ways out (pace, days, narrow a subject). Re-planned from what was walked: past days show walked, today walked/planned, later days re-spread; extra cards never lower tomorrow; a short day raises normal days up to the ceiling.
- **Adding subjects:** quick add (system + pool + walk count, live count) or **Pick in the Mosaic**.
- **Mosaic:** walk chips are now *Not walked · ×1 · ×2 · ×3+* (combine with the pool chips); **Pick** toggle — tap a first then a last tile (range of lit cards), tap a deck name or chunk name for all of it; picked tiles get a white frame, the first tap a gold dashed frame; tray: Add to plan / Add to flow / Clear.
- **Flow:** "Today's thread" above the card: one bead per card walked today against today's planned number (or 65): light = new, mid = ×2, dark = ×3+, ring = repair, gold edge = past the target, notch = where you should be by now; "day sealed" in gold at the target; parts of the plan underneath. Flow desk: "Today from the plan" with Start (repairs first, then subjects in plan order).
- **Loft re-laid:** plan card full width at the top; chase, cards per day and time in the main column; today's target, a compact calendar, day in the chronicle, coverage and tiles in a side column (stacked on the phone).
- Plan storage: per profile on the device; the live app also syncs it to Drive (`Trace/plan.json`, `plan-ht.json`, newer copy wins); the test build only reads.
- ✦ stars recounted from the current NEET set on load.

## T-052 — 2026-11-04 — Claude — recorder — v2.7 (given to Naven)
- HT review batch (4 Nov, 00:42–00:47 IST, recorder 2.6): SIADH & DI (14 wrong), Adrenal Insufficiency & Crisis (12), Metabolic Encephalopathy (6), Substance-Related Disorders Part 1 (6), Part 2 (12), Part 3 (10), Drug-Related Disorders (15) — all sent automatically, lists match DocT's incorrect counts, no skipped questions in these modules, anchors correct (Q1). 65 wrong questions; 55 mapped to cards, 10 have no card yet.
- Substance Part 2 was sent at 00:44:57; Naven re-opened it, and since nothing new was captured, leaving sent nothing and recording stayed on "HT review" (looked like a failure). **v2.7:** leaving a review that was already sent flashes "nothing new · already sent" and switches recording Off.
- **v2.8** (Naven: same module, two people): a review is only "already sent" for the same person; a review by the other person (HT, then Naven, or back) starts its own session saved under that person, never merged into the first person's.

## T-051 — 2026-11-04 — Claude — live — 1.4.7
- Promoted test 1.3.31 on Naven's explicit approval (4 Nov, 00:33 IST): skipped DocT questions become repairs "Skipped" (T-049/T-050), combined Wrong+Skipped lists; the peak-week preview (T-048) is copied too but only shows on the test app.

## T-050 — 2026-11-04 — Claude — test + recorder — 1.3.31 / recorder v2.5
- Naven's Skipped pass on HT's Glucose review (00:24 IST) arrived as `…_review_3of25.json` (recorder 2.4) without a Skipped list: the questions seen carry both Wrong and Skipped flags, so both filters were ticked together and v2.4 only reads a list when one filter is ticked.
- **Recorder v2.5:** Wrong + Skipped ticked together is read too (Skipped = the grid minus the Wrong list already read; if Wrong isn't known yet, the union is kept as "Wrong+Skipped"); a note flashes the filters the recorder sees ticked; a warning shows if the question grid can't be found.
- **Recorder v2.6:** keeps the first anchor (question ID ↔ paper number) instead of re-setting it on every list read: after a filter change DocT can leave the old question on screen while the grid already shows the new list, which would have tied the wrong number to that ID.
- **Trace 1.3.31:** a combined list flag containing Skipped counts as "Skipped" (unless the question is also wrong).

## T-049 — 2026-11-03 — Claude — test + recorder — 1.3.30 / recorder v2.3
- First real HT review arrived (3 Nov, 23:40 IST): `doct_HT_Glucose_Related_Disorders_…` (attempt + review), Wrong list Q2, 6, 9, 11, 12 = DocT's 5 incorrect; all mapped → 10 repair cards in HT's profile (ENDO02A GLY-05/08/22; ENDO02B DKA-01/04/06/07/13/17/19), due 4 Nov.
- **Skipped questions become repairs** (Naven): recorder v2.3 reads the Skipped list when only Skipped is ticked; Trace counts a Skipped question (not also wrong) as a repair "Skipped", ordered after Wrong and sure and Guessed wrong, before Guessed right.
- **Cohort % check:** the DocT review page holds only the question on screen, so cohort % comes only from questions opened. Recorder v2.3 adds menu › "Save page data for Claude (cohort check)", which saves the JSON replies DocT's own page loaded (read-only, local Downloads only) to see whether every question's cohort % arrives in one reply. Naven decided not to step through every question if it doesn't.
- **Cohort check result (4 Nov, 00:00 IST):** every reply DocT's page loads (review questions included) is encrypted (`{iv, ct}`), so per-question cohort % can't be read from it. Dropped as Naven decided: cohort % only for questions opened on screen. Recorder **v2.4** = v2.3 without the page-data probe (given to Naven).

## T-048 — 2026-11-03 — Claude — test — 1.3.29
- **Peak-week preview in the Loft** (Naven, 3 Nov: "take my peak performance … before INI … assume timings … test version"): a test-only switch at the top of the Loft ("Show it" / "Back to my data") lays Naven's War Map Log rows for **17–23 Oct** (the week before INI-SS: 382 cards, 36 h 19 m; best day 21 Oct, 89 cards) onto the last 7 days. Session start times and minutes are real; cards are spread evenly inside each session. Break reasons are **assumed** from the gaps (9:30 to first session = breakfast; 12:30–15:30 = lunch; 16–18 h = evening tea; 19–21:30 = dinner; short gaps tea/restroom; others rest; a meal or tea counts up to twice its allowance, rest up to 30 min, the remainder stays Unexplained). Drives the Phase 1 chase, cards per day, time, live pace (Loft only); Calendar and Coverage stay real; nothing is saved. Data: `js/peakdata.js` (from the Log tab), logic `js/peek.js`; off on live by design.
- Tests: demo with the peak decks in the library → chase 52.3/day (finish 15 Nov in the demo pool), cards per day and study strips filled, breakdown shows study, meals, rest and unexplained; no page errors.

## T-047 — 2026-11-03 — Claude — live — 1.4.6
- Promoted test 1.3.28 on Naven's explicit approval (3 Nov, 19:50 IST: "i approve to put all these into live"): save/discard on leaving a flow (T-044), test-reminder button (T-041), Loft redesign and Going out / breaks with calendar reminders (T-045), Going out on the palace (T-046). ✦ stars recount from the current NEET set on load.

## T-046 — 2026-11-03 — Claude — test — 1.3.28
- **Going out on the palace** (Naven, 3 Nov): button in the palace top bar. On phones the break banner sits above the bottom bar (it covered the brand at the top); in Flow on phones the live pace line is padded and Going out is a small right-aligned button.
- Tests: demo palace on Mac width and Pixel 7 → Going out → Tea → banner; phone Flow with a break; no page errors.

## T-045 — 2026-11-03 — Claude — test — 1.3.27
- **Loft redesigned** (Naven, 3 Nov): right column is now Coverage (with colour legend) · **Phase 1 chase** (every card walked once by 30 Nov; pools All cards / Any hit / NEET + GT / NEET; current vs required rate, finish-date verdict, live pace, worm chart, weekly bars, today's ring, what-if slider) · **Cards per day** (stacked new / ×2 / ×3+ / repairs + War Map flow; filters; 7/14/30; goal 65) · **Time** (today's 3 numbers, 7-day study strips 9:30–21:30, "Where did my 12 hours go?" Day/Week, the day as a list, study hours per day with 8 h goal, best hours heat row) · small tiles Quiet alcove · Chronicles · Again pile · GT trend. Old hours/cards charts and the big alcove removed. New pure-calculation module `js/loftx.js`.
- **Going out / breaks** (`js/breaks.js`): sheet with breakfast, lunch, dinner 30 · evening tea (4–6 pm) 30 · tea 15 · restroom (counted) · rest (nudge at 20) · duty · phone. Banner stays until **I'm back** (opening Trace doesn't end it). Timed breaks add a calendar reminder at the end (profile's own calendar; removed if back early). After ≥5 min away inside the window: "Away n min, what was it?" with "Still away, just checking". The card clock pauses while away or on a break. Live pace line in the Flow header/aside. Breaks are stored per profile on the device (45 days).
- ✦ stars recounted from the current NEET set on load (`recountStars`).
- Tests: demo Loft on Mac width and Pixel 7, demo tea break → banner → I'm back, Flow live line; no page errors.
- Deferred to next update: time left after scheduled breaks; evening "start tomorrow at 7:30 / 7:00" plan.

## T-044 — 2026-11-03 — Claude — test — 1.3.26
- **Leaving a flow always asks** (Naven, 3 Nov): closing (✕ or Esc) after walking at least one card opens "Save this flow?" with **SAVE**, **Discard n cards** and **Keep going**. The end-of-flow screen's button is now **SAVE**, with "Discard this flow" under it. Discard undoes every view of that flow (unsynced views are deleted; synced ones get an undo event, as Undo already does), clears Continue, and writes no Log rows. Look mode and a flow with no card walked close without asking.
- Tests: demo flow of 2 cards → close → Save keeps 2 walked; Discard returns to 0; no page errors.

## T-043 — 2026-11-03 — Claude — bridge — v5.1 (given to Naven)
- HT's test reminder also rang on Naven's phone: the calendar "Trace · HT" is owned by Naven's account, and an event's own pop-up reminder applies to the owner. Fix given to Naven as a one-line edit: events for HT get no reminder of their own (`if (o.who !== 'HT') ev.addPopupReminder(0);`), so HT's ring comes from her calendar default ("0 minutes", set 3 Nov) and Naven's from his (set to none / hidden). Repo `backend/Code.gs` updated to match.

## T-042 — 2026-11-03 — Claude — bridge — v5
- Naven pasted the v5 patch into "Trace Backend", ran `authoriseCalendar` (Calendar access granted; calendars "Trace" and "Trace · HT" created) and deployed it as a new version of the existing deployment (same link). Verified end to end at 18:56 IST: test 1.3.25 › This device › "Send a test reminder" added an event to "Trace" and his phone showed the Calendar notification two minutes later.

## T-041 — 2026-11-03 — Claude — bridge + test — v5 (prepared) / 1.3.25
- **Bridge v5 (prepared, not yet deployed):** new op `calendar` (`action: add | remove`, `who: Trace | HT`, `at`, `title`, `note`, `id`). It only adds or removes short events (5 min, one pop-up at the event time) in two calendars of its own, **"Trace"** (Naven) and **"Trace · HT"** (HT; Naven shares this one with her), creating them on first use. It never reads or touches any other calendar. `authoriseCalendar()` grants Calendar access and creates both calendars. Repo `backend/Code.gs` updated (placeholder key unchanged).
- **Test 1.3.25:** This device › Reminders › "Send a test reminder (in 2 minutes)" to check the calendar route end to end (the current profile's calendar). Says plainly when the bridge has not been updated yet.
- Agreed with Naven (3 Nov): breaks, "Going out", the evening start-time plan and break reminders will use this route; HT's reminders reach her phone through the shared "Trace · HT" calendar with her own notification setting.

## T-040 — 2026-11-03 — Claude — live — 1.4.5
- Promoted test 1.3.24 on Naven's explicit approval (3 Nov, 15:53 IST): deck downloads work with the library that lacks `cards_id` (T-039), tolerant setup-link reading (T-037) and the on-screen setup link with its check (T-038).

## T-039 — 2026-11-03 — Claude — test — 1.3.24
- **Fix: new devices downloaded no decks** ("5 decks" = only the Top-up decks; Naven's Tab, 3 Nov). The newest `Trace › library.json` (file `1v7sYavDrSS5a2tWvA-9fLR-e0HyUteNx`, written 1 Nov 21:15 UTC, 157 decks) has `folder_id` and `deck_json_id` but **no `cards_id`** for any deck, and `downloadDecks` skipped decks without `cards_id`. Devices that had downloaded from the older library kept working. Now a deck without `cards_id` is found by `findFile(folder_id, 'cards.jsonl')` first (batches of 20) and the found ID is kept in the saved library.
- Deck downloads run in batches of 6 with a 150 s wait; a failed or timed-out batch is reported and the rest continue (before: 25 per batch, and one failure stopped the sync).
- Who wrote the 1 Nov library without `cards_id` is not recorded; whoever writes `library.json` should keep `cards_id` (AGENTS §4 lists it as the deck file).

## T-038 — 2026-11-03 — Claude — test — 1.3.23
- This device › Setup link also shows the link in a box on screen with its length and a check that the saved connection has an address and a key (✓/✗, values not shown separately), so a failed clipboard copy can be seen and the link selected by hand. Naven's paste showed only the link's fixed start.

## T-037 — 2026-11-03 — Claude — test — 1.3.22
- Setup link reading is tolerant: line breaks or spaces inside the link (a message app splitting a long link) are ignored; a cut-off or altered link now says so ("looks cut off / incomplete, copy it again in one piece") instead of a raw `atob` error (seen on Naven's Tab, 3 Nov).

## T-036 — 2026-11-03 — Claude — live — 1.4.4
- Promoted test 1.3.21 on Naven's explicit approval (3 Nov, 14:37 IST): devices connected only in test storage are recognised and connect by themselves (T-035), and This device › Setup link copies the private link for another device.

## T-035 — 2026-11-03 — Claude — test — 1.3.21
- **Fix: a device whose connection was saved only in the test copy's storage (`trace-test`) asked for the setup link** after the profile change (seen on Naven's Tab, 3 Nov). The profile check and the connection borrow now also look in `trace-test` / `trace-test-ht`.
- **This device › Setup link: "Copy it, to connect another device"** (two taps; copies the private link to the clipboard, or shows a copy box). Built on the device from its saved connection; the app never stores or sends it anywhere. Naven had no copy of the link; HT's tab needs it once.

## T-034 — 2026-11-03 — Claude — live — 1.4.3
- Promoted test 1.3.20 on Naven's request (3 Nov, 14:22 IST, "make trace live"): DocT misses → next-day repair cards with reasons and cohort order (T-030, T-032, T-033), `data/qmap.json`, Missed/Guessed chips, and the Loft Coverage card in card colours (T-031, T-032). Root differs from `test/` only in version and title. Nothing new is written to the Sheet; Trace reads Drive › Trace › doct.

## T-033 — 2026-11-03 — Claude — test — 1.3.20
- **One-tap miss lists** (recorder v2.2, delivered in chat): in a DocT review, ticking **Wrong**, **Guessed Wrong** or **Guessed Right** narrows the Questions grid beside the filters to those questions' original numbers (confirmed on Naven's snapshots, 3 Nov: QBank Wrong → 2, 3, 5, 6; GT Guessed Wrong → 2). The recorder reads the whole grid at once into `lists`, plus an `anchor` (the question on screen and its original number), so stepping through each question is no longer needed. Trace (`sittingQuestions` in `store.js`) turns the numbers into DocT IDs through the anchor's paper/module in `qmap.json` (label "Module Qn"), only when the anchor's label matches its number; papers not in the map count as "no card yet".
- Recorder v2.1 (also in chat): a QBank sitting needs no review — QBank solving shows the key on each question, so leaving the module saves, sends and switches Off. GTs still need the review (the key is only there).
- Recorder fix: a `const isRev` used before its declaration threw on every page tick while recording was off (since v1.x); now a function.
- Repair labels use the map's own "Module Qn" (in a filtered review DocT numbers the list 1…n).
- Tests: v2.2 in jsdom against the four 3 Nov snapshots (lists and anchors read; upload payload; auto-off); Trace demo with injected lists (Shock Wrong 1, 3 → three cards; unmapped GT paper → one "no card yet"); no page errors.

## T-032 — 2026-11-03 — Claude — test — 1.3.19
- Coverage bars use the card colours (Naven): empty = not seen (`--s0`), then seen once / twice / three times or more (`--s1`–`--s3`), as on the shelf, deck and card tiles.
- Again pile order: Wrong and sure → Guessed wrong → Guessed right; within each, the misses most of the DocT cohort got right come first (Naven: cohort % is useful).

## T-031 — 2026-11-03 — Claude — test — 1.3.18
- **Coverage card at the top of the Loft** (Naven, 3 Nov): walked ÷ cards for four pools, each its own denominator — All cards · Any hit · NEET · NEET + GT — with walked = seen at least once (War Map history + Trace). Tapping a pool shows one bar per system (lighter = walked once, darker = twice or more). Hit pools count only decks on the device; the note says how many are left out. Choice remembered (`covPool`).
- Tests: demo Loft at 1180×740, pool switch; no page errors.

## T-030 — 2026-11-03 — Claude — test — 1.3.17
- **DocT misses → next-day repair cards** (Naven's first loop update, agreed 3 Nov).
  - **Recorder v2.0** (Tampermonkey, delivered in chat, not in the repo): one mode chosen before each sitting — Off · Trace solving · HT solving · HT review — shown in a pill on every DocT page; the mode switches itself Off once a review (or learning-mode capture) is saved, so reopening an old review is never recorded by accident. Every saved file is also sent through the bridge (`writeFile`) to **Drive › Trace › doct** (folder `1wqRbRG-nqldfafFL-AughcBEBfo6atQo`, created 3 Nov) as `doct_Trace_…json` / `doct_HT_…json`, a compact record without stems, options or explanations. The connection comes from the private setup link pasted once into the recorder (menu › Connect to Trace) and stays in Tampermonkey's storage on Naven's Mac. The recorder's old QBank on/off switch is replaced by the modes; Downloads copies continue as a backup.
  - **`data/qmap.json`** (new, served like the layer and never cached by the service worker): 3,190 DocT question IDs (DT… QBank, TS… GT) → Trace cards (`deck|code`, each code resolved to the deck that actually holds it); 2,456 have cards. IDs and labels only.
  - **Trace** (`syncDoct` in `sync.js`) reads new files for the current profile from that folder; `setDoct`/`buildRepairs` in `store.js` merge attempt + review files of one sitting, mark each question **Wrong and sure / Guessed wrong / Guessed right**, and map it to its cards. A card joins the **Again pile from the day after the test** with its reason (e.g. "Wrong and sure · Shock Q1 · 88% got it") and leaves once walked without Again after that test. Misses with no card are counted ("n missed questions have no card yet").
  - **New pool chips:** `Missed · QBank`, `Missed · GT`, `Guessed` (all-time DocT misses), usable everywhere the chips are.
- Tests: recorder v2.0 in jsdom against the saved GT review page (mode menu, pill, upload payload and folder, auto-off after the review save); Trace demo with injected attempts (merge, reasons, due tomorrow, no-card count, chips); no page errors. Not yet tried against the real DocT site or Drive.

## T-029 — 2026-11-03 — Claude — live — 1.4.2
- Promoted test 1.3.16 on Naven's explicit approval (3 Nov, 13:27 IST): War Map Chunks-tab chunking (T-027), the chunk bar and Trace/HT profiles (T-028). Root differs from `test/` only in version and title.
- Naven's devices pick the Trace profile automatically (they hold the live connection); his data and database (`trace`) are unchanged. HT's tab asks once, then needs the private setup link.

## T-028 — 2026-11-03 — Claude — test — 1.3.16
- **Profiles: Naven = Trace, HT = HT** (agreed 3 Nov). First open on a device asks "Who studies on this device?"; a device that already holds the live connection (Naven's) is set to Trace without asking. Stored in local storage (`trace.profile` / `trace-test.profile`); switch on This device (two taps).
  - HT's profile has its own database (`trace-ht`, test: `trace-test-ht`), its own view settings and last flow (local-storage prefix `…ht.`), and borrows only the connection already saved on the device.
  - Sheet: HT's Log and Targets rows carry `who = HT`; her profile reads only Log/Targets rows whose who is HT (also accepts "Harshita"), so her War Map history (cards seen, walked, Loft minutes, chronicle, targets) shows in Trace. TraceEvents has no who column: HT's device ids start `HT-` and each profile merges only its own devices' events. Card edits: `edits-ht.json` for HT, `edits.json` for Naven.
  - HT's profile shows no visual decks (not loaded or checked); Top-up lines, Crossfire and corrections still show. An `HT` pill sits beside the brand.
- **Chunk marker:** the gap between chunks is now a thin gold bar (Naven: the gap didn't look good).
- Tests: fresh device at `/test/` → chooser → HT → own database (`trace-test-ht`) and setup screen; device with a saved live connection → Trace, no chooser; demo regressions (Chunks-tab chunking, lit flow, Continue, Again pile); no page errors.

## T-027 — 2026-11-02 — Claude — test — 1.3.15
- **Chunks now come from the War Map Chunks tab** (Naven, 2 Nov): before, a chunk was any run of cards with the same `section` heading, so decks where every card has its own heading (many CVS and GI decks) showed one chunk per card. Now `chunkOf(card)` in `store.js` finds the Chunks-tab range (`card_from`–`card_to`, War Map numbering via `off()`) holding the card and uses that row's `section_name`. Top-up cards form one "Top-up" chunk at the end; decks with no Chunks rows (the Top-up decks) fall back to section headings.
- Used everywhere chunks show: Mosaic/Eagle gaps and names, hover label, pulled-deck strip, deck-page section headers, the deck sheet's "pick sections", the Flow tile panel's new-row breaks and the Flow header's chunk name.
- `sync.js` keeps the Chunks tab's `section_name` and re-reads the tab once on every device (`chunksNamed`) so names arrive without waiting 12 hours.
- Tests: demo with injected Chunks rows for CVS03 (36 gaps → 3; names and deck headers match the rows); no page errors. Not yet promoted to live.

## T-026 — 2026-11-02 — Claude — live — 1.4.0
- **Promoted on Naven's "proceed" (2 Nov, 21:01 IST)**: test 1.3.14 copied to the repo root. Root differs from `test/` only in `appVersion` (1.4.0), the service-worker version and the page title "Trace"; the root manifest is unchanged. The code picks live behaviour from the URL path: database `trace`, writes to the Sheet and Drive as before, no TEST tag, pilots off.
- **Now live:** palace home and Loft; meditation (no recording pilot); visual decks (GI01A, GI01B, GI01C, GI02A, GI02B v2, GI03, GI04, GI05 published by ChatGPT; GI06, GI07A, GI07B not yet); the QBank/GT layer with bank chips, Top-up lines, Crossfire, corrections, 242 Top-up cards and 5 Top-up decks; additive pool chips; NEET tag from DocT's 2025 recall paper + 2024 tags; ✦ = NEET cards; spine put-back; Top-up marks; chunk gaps, chunk names, hover label, lit bar; the Flow desk (target, Continue, Again pile, Add more).
- **New in live writes:** views of Top-up cards and Top-up-deck cards go to `TraceEvents` (codes `TU-nn`, deck codes `TU-…` for the Top-up decks); they never become `Log` rows (T-019/T-021 rules). Database upgrades from version 1 to 2 (adds `visuals`, `vimg`); an old Trace tab left open can hold the upgrade until it is closed.
- `AGENTS.md` → guidance version 6 (file table, routes, §10 palace line).
- Tests: the root copy served at a non-`/test/` path in demo mode: palace, shelf, Eagle, Flow desk, deck, Loft, status; lit flow; offline reopen (13 spines from cache); no page errors. Not device acceptance.

## T-025 — 2026-11-02 — Claude — test — 1.3.14
Four changes Naven agreed in conversation on 2 Nov (talked through first, then approved to build):
- **Chunk gaps:** a small gap between chunks (card `section`) inside each deck in the Mosaic, Eagle view and the shelf's pulled-deck strip. In the running Flow's tile panel each chunk starts on a new row.
- **Chunk names + hover label:** a `Chunk names` chip in Mosaic/Eagle (remembered per device, key `cnames`) prints each chunk's name before its tiles. Hovering a tile with a mouse or a hovering pen (S Pen) shows "deck · chunk · card n · NEET tag"; touch never shows it. Also on the pulled-deck strip and the Again pile strip.
- **Lit bar in Mosaic and Eagle view:** "n lit cards · ≈ min at your pace · FLOW LIT · + Add lit to flow". It takes the cards the pool and Seen chips light, in the order shown (Eagle: system by system). Minutes = lit cards × the average of the last 200 Flow cards (75 s with no history).
- **Flow tab is a session desk:** Today's target (Start) · **Continue** (the last flow left before its end, kept 3 days, `lastFlow` in local storage) · **Again pile** (a card marked Again stays until walked without Again in a later session; `againList()` in `store.js`) · **Add more** (Eagle view or a system's Mosaic). The deck checkbox list, Order choices and quick picks are gone.
- Tests: demo mode at 1180×740: names toggle, hover label, lit bar → Flow, Again + leave → Continue and Again pile on the desk; no page errors.

## T-024 — 2026-11-02 — Claude — test — 1.3.13
- **T-023's board is withdrawn (Naven, 2 Nov):** `test/js/app.js` and `test/css/app.css` are back to their 1.3.11 state (commit `6af4d8c`). The shelf, mosaic, Eagle view and Flow tab look and work as in 1.3.11.
- **Kept from T-023: ✦ stars from the current NEET set.** `recountStars()` in `store.js` sets a downloaded deck's ✦ to its gold-ring NEET cards; other decks keep the library count. `sync.js` recounts after deck downloads. The shelf panel says "✦ n NEET cards" instead of "real NEET Qs".
- The mosaic and Flow selection redesign is under discussion with Naven; nothing more ships until he approves.
- Tests: demo mode at 1180×740: shelf stars and panel, Eagle mosaic, Flow tab; no page errors.

## T-023 — 2026-11-02 — Claude — test — 1.3.12
- **One board everywhere** (Naven's design, 2 Nov): the Flow tab, the Eagle view (`#/sys/all`), a system's Mosaic tab and the shelf's pulled deck now share one board. Each deck is **one horizontal row** of tiles that stretch to the width; a gold bar separates chunks (card `section`), and a thin band under each chunk shows how much of it is walked. The label shows deck code, title, ✦, **card count** and lit count.
- **Chunk zoom:** tapping a row on a touch screen (or clicking the band under a chunk with a mouse) opens that chunk below the row: chunk name, card range, lit and walked counts, big tiles, `▶ Flow`, `+ Add to flow` (today's target) and `+ Add, next ›`, with ‹ › to step chunks. With a mouse, clicking a small tile opens the card directly.
- **Lit = selection:** the pool chips (All · Any hit · NEET / DocT GT / DocT QBank / Marrow / Top-up, additive) and Seen chips are now **one shared setting** for every view and the deck page, remembered per device (`pool`, `pst`). `▶` / `+` on a chunk, deck, system or the whole board take only the lit cards (a chunk with none lit takes all its cards).
- **Order** is two choices, also shared: `Yield` (systems and decks by the **average** worth of their lit cards; chunks and cards keep their order) or `Shelf`. "Best cards first", the deck checkboxes and the quick picks are gone from the Flow tab.
- **Collapsed / Open** toggle for systems (remembered; collapsed by default). Tapping a system header opens or closes just that one.
- **Single card tap:** Flow tab = leave the card out of the flow (tap again to bring it back; footer shows "n left out · bring back"); every other view = look at the card.
- **✦ stars recounted** from the current NEET set: a deck's ✦ = its NEET (gold-ring) cards, computed on the device for downloaded decks (`recountStars()`); decks not downloaded keep the library's old count. Shelf sort, tiers and the deck back use it. Card count added to spines and to the running Flow header.
- Tests: demo mode at 1180×740 touch (Tab-like), 1400×900 mouse and 400×860 touch: collapse/open, chunk zoom, leave-out, add-and-next, deck ▶ flow; no page errors. Not device acceptance.

## T-022 — 2026-11-02 — Claude — test — 1.3.11
- **NEET tag source changed (Naven's call, 2 Nov).** NEET 2025 is now DocTutorials' full NEET-SS 2025 recall paper (150 Q, the layer's `recall` chip) plus the items only Marrow's recall reported (Wells PE, CURB-65, amniotic fluid embolism, thiamine, and Recall25 Q141 xanthochromia that the GT dedupe had folded into GT3 Q124) — layer `neet25extra`. The old merged 2025 tags in `neet.json` are ignored; its 2024 tags are kept (no full 2024 paper exists). `neetTag()` computes 24 / 25 / 24·25 from these; the gold ring, the NEET pool and the tag text are now the same set (before, the pool included recall-only cards the ring did not). The recall paper no longer shows as a separate chip.
- **Pools are additive components:** `All`, `Any hit`, then toggles `NEET`, `DocT GT`, `DocT QBank`, `Marrow`, `Top-up` — any combination is a union (e.g. DocT QBank + Marrow, or both banks + GT). Same chips on the deck page (with counts and "n of N lit"), the deck sheet, the Flow tab and the mosaic. Deck page Seen row gains `Edited`.
- **Shelf:** tapping a pulled spine again puts the deck back; the panel has `↩ Put back` beside Open deck. Long deck titles shrink to fit on deck backs instead of being cut.
- **Top-up marks after walking:** a walked Top-up card's coral ear shrinks to a small coral dot (mosaic, deck strip, Flow tiles, deck tiles). The spine's coral badge now counts unwalked Top-ups (`+n`) and disappears when they are all walked. TU decks, TU labels and the Top-up pool stay.
- Tests: demo mode, 1400×900: put-back by second tap, additive chips (DocT QBank + Marrow = 20 of 30 lit on HY2), titles; no page errors. Not device acceptance.

## T-021 — 2026-11-02 — Claude — test — 1.3.10
- **Top-up decks** (Naven asked for them on 2 Nov): five homeless Top-up clusters became decks built from their source questions — TU-NEURO *Stroke, Seizures & Coma* (24), TU-IE *Infective Endocarditis* (15), TU-TX *Transplant & Immunosuppression* (15), TU-AIR *Airway: Infection, Trauma & RSI* (13), TU-SAFE *Patient Safety & Family Communication* (13). Their 29 Top-ups were removed from the decks they were parked in.
  - They live in the layer (`qbank.json` → `decks[]`), not in Drive: `applyTopupDecks()` adds them to the library and the deck store on every load (`virtual: true`, `topupDeck: true` in the library entry). `downloadDecks` skips them (no `cards_id`). Their views never become War Map Log rows (`realCount` = 0).
  - Each card carries `src` (source questions) and `banks`; the answer side shows a "From:" line. Numbered steps are stored as list lines so reflow keeps them apart (also for Top-up cards).
- **Recognition (coral = Top-up):** Top-up deck spines are striped coral with "TU"; decks holding Top-up cards get a coral "+" badge; deck backs show "TOP-UP DECK" or "+n TOP-UP"; Top-up cards get a coral corner in the mosaic, the deck strip and Flow tiles, and a coral top edge on deck tiles; Flow-tab rows tag Top-up decks.
- **Mosaic:** pool chips (All … Marrow) and Seen chips light matching cards and dim the rest, with "n of N cards lit"; new sort "Most lit". **Eagle view** (`#/sys/all`, button on the shelf): one mosaic of every deck, grouped by system.
- **Tests:** demo mode with 8 real decks plus the 5 Top-up decks at 1400×900: shelf marks, eagle view (Any hit: 180 of 247 lit), Top-up deck Look, numbered algorithm lines; no page errors. Not device acceptance.

## T-020 — 2026-11-02 — Claude — test — 1.3.9
- **Hit pools,** one set used everywhere (deck filters, the deck's "What to take" sheet, the Flow tab), widest first: `All` · `Any hit` (real NEET tag, NEET 25 recall, any Marrow / DocT / DocT GT hit, and every Top-up) · `NEET + GT` · `NEET` (real NEET tag or NEET 25 recall) · `Top-up` · `DocT QBank` · `Marrow`. Top-up cards join each pool by the banks they came from (from the layer's `banks`), and show those bank chips.
- **Seen** is now a separate choice combined with the pool (Any · Unseen · Seen ≤ 1 · Not seen 7+ days), in the deck sheet and the Flow tab. Previously the chips were a union.
- **Flow tab order:** `Best decks first` (default; decks ranked by the summed worth of the cards they give, card order kept inside a deck), `Best cards first` (by worth, unseen first), `Shelf order`. Worth (`hitsOf().score` in `store.js`): real NEET 6, NEET 25 recall 5, DocT GT 2 per question, DocT and Marrow 1 per question (capped at 6 per bank), Top-up 1.5 per question + 3 for Tier 1. New quick picks `All decks` and `Decks with hits`.
- Deck page header also shows Top-up and hit counts.
- **Tests:** demo mode, 4 real decks: pool counts All 103 · Any hit 67 · NEET + GT 48 · Top-up 14 · DocT 34 · Marrow 33 (demo has no NEET tag file); Best-cards-first started on HY2's hypertensive-emergency Top-up (Tier 1, 15 Qs); no page errors. Not device acceptance.

## T-019 — 2026-11-02 — Claude — test — 1.3.8
- **QBank/GT layer** (Naven approved all items on 2 Nov). Card text is never changed; everything is drawn beside it.
  - **Data:** `test/data/qbank.json`, served with the app. It is fetched on open and on every sync, kept in IndexedDB (`kv.qbank`) for offline use, and bypasses the service-worker cache so a new file arrives without a version bump. 1,189 cards carry layer data: 1,169 bank-chipped, 658 with Top-up lines, 211 Crossfire lines, 34 checked corrections; 271 Top-up cards in 96 decks.
  - **Card face:** bank chips after the NEET tag — `NEET 25 recall` (amber), `Marrow` (violet), `DocT` (teal), `DocT GT` (teal, dashed), with ×n question counts. Labels carry the meaning; colours only help.
  - **Answer side:** `CORRECTION · CHECKED` box above the answer (fix + source link); `TOP-UP LINES` (bank prefix in mono) and `CROSSFIRE` boxes below Watch.
  - **Top-up cards:** appended to the end of their deck (`code TU-nn`, `no` continuing after the last real card, section `Top-up`, coral chip + tier). New deck filter chips `Top-up` and `QBank hit`; new scope `Top-up`.
  - **War Map safety:** views of Top-up cards (`no` beyond the deck's last real card) are marked logged and never become Log rows, so War Map numbering is untouched. They still count in Trace's own seen counts.
- **Files:** `test/js/store.js` (`setQb`, `qbOf`, `realCount`, Top-ups in `cardsOf`), `test/js/sync.js` (`loadQbank`, Log exclusion), `test/js/app.js` (chips, boxes, filters), `test/css/app.css`, `test/sw.js` (layer bypass), versions 1.3.8.
- **Tests:** headless Chromium in demo mode with real decks HY2, ENDO01B, CVS03, RESP03 at 1400×900 and 390×844: chips, three boxes, correction with source, Top-up tiles and cards render; no page errors. **Not device acceptance.** Live app and bridge unchanged.

## T-018 — 2026-11-01 — Claude — docs
- **Real device evidence, reported by Naven: test 1.3.7 on his connected Mac.**
  - This device showed 1.3.7, with GI02B v2 (53 scenes) kept and 0 waiting.
  - Naven was in **Look**, not Flow, so no study activity was logged.
  - Tapping the PANC-25 answer phrase "High-volume haemofiltration" opened its scene (the experimental washing machine) directly.
  - The **full original 3:2 image** now shows. Before the fix it was a strip about 90 px tall.
  - The first 3 Learn cue–meaning pairs are visible below the image, and the rest of the panel scrolls.
- **What this doesn't cover:**
  - Claude's phone (390×844) and tablet results in T-017 are browser runs with **synthetic** data on a mock bridge. They are **not** device acceptance.
  - The phone and the Tab are still to be checked on the real devices. Use **Look** for those checks, so no study activity is logged.
- No app code, live app, bridge, visual package or Journal changed.

## T-017 — 2026-11-01 — Claude — test — 1.3.7
- **Visual panel fix:**
  - **Cause:** in `.vp-scroll`, a flex column, children could shrink. The image box (`.vp-img`, which has `overflow:hidden` and so a minimum height of 0) absorbed all the shrinking when the text was long. Naven saw about 354 px on PANC-15 and about 90 px on PANC-25, and the image was cropped.
  - **Fix:** one CSS rule, `.vp-scroll>*{flex-shrink:0}`. Every block now keeps its natural height, and the panel scrolls.
- **Tests,** browser runs on a mock bridge with a **synthetic** long-content package (framed 1536×1024 images, 10 long cue pairs, long notes and story), at desktop 1437×872, tablet 1480×924 and phone 390×844:
  - **Before the fix:** the image box was 2 px tall in all three sizes.
  - **After the fix:** the box is 690×460, 711×475 and 362×242, showing the full image with no clipping in all three sizes.
  - **Unchanged:** overview hotspots stay at 14/28, 38/3 and 77/35 %; in Learn the first pair is visible with its meaning; in Self-test all 10 meanings stay hidden; card notes start closed.
- **Not yet done:** acceptance with the real GI02B v2 package on Naven's device.
- Live app untouched (1.2.3).

## T-016 — 2026-11-01 — Claude — test + bridge — 1.3.6 / v4
- **Bridge v4,** pasted and deployed by Naven on the same link:
  - It adds `notifyJournal(requestId)`, which only acts when the Script Property `JOURNAL_ENABLED` is `true`. The default is `false`.
  - It only notifies for an existing, matching, unexpired `test:true` request in `Trace › flowmsg`, once per request ID and at most once a minute.
  - It sends `POST {requestId, test:true}` with `Authorization: Bearer <JOURNAL_WEBHOOK_KEY>` to `JOURNAL_WEBHOOK_URL`.
  - Naven entered those values privately. **No secret is in the repo, the app or any chat.** Incoming authentication is unchanged.
  - The only new Google permission is `script.external_request`, granted by Naven through `authoriseJournal()`, which sends nothing.
  - Sync was confirmed working after deployment.
- **Test 1.3.6:**
  - After writing the pilot request, the app asks the bridge to notify Journal, without waiting for the answer.
  - The status line shows "Journal notified", "Journal not notified: <reason>" or "bridge is older than v4".
  - Checking for the reply and displaying it are unchanged.
- **Mock tests only:**
  - The request was written once and notify called once with the same ID; there was no second notify on the next card.
  - All three states displayed correctly.
  - A simulated reply showed.
- **Rollback:** set `JOURNAL_ENABLED=false`, or redeploy bridge version 3.

## T-015 — 2026-10-31 — Claude — docs
- **Real Journal round trip, verified:**
  - The actual test build at `/test/#/pilot`, in Naven's Chrome, wrote request `req-fm-20261031-214807-v9ye30.json` (641 bytes, `text/plain`) at 21:48:11 IST.
  - Journal, watching for one bounded active session started in chat, read the file's actual contents. **No request content was relayed by hand.**
  - Journal wrote `res-fm-20261031-214807-v9ye30.json` (315 bytes, `application/json`) at 21:49:05 IST.
  - The app showed the reply text under the card, labelled "on PANC-14".
  - Dismiss removed it, and Next continued to PANC-16.
- **Read-only checks by Claude afterwards:**
  - `Trace › flowmsg` holds exactly this one request and one reply, both owner-only.
  - The request ID matches in both files.
- **What this proves:** a file handoff during an active session, after a one-time chat start. It does **not** prove unattended wake-up.
- **Note on the reply's wording:** it says "Seen once, not yet owned". That's a judgement of mastery, which the request explicitly says isn't measured. This is a content issue for Journal's prompt, not an app defect.

## T-014 — 2026-10-31 — Claude — test — 1.3.5
- **Journal Flow-message pilot (test only):**
  - The explicit entry is `#/pilot`. It runs a look-mode Flow from GI02B PANC-14, which logs nothing to the device's history or the Sheet.
  - The first Next after Reveal writes **one** request, `req-<requestId>.json`, into `My Drive › Trace › flowmsg` using the existing bridge `writeFile`.
  - This is the **only** write the test build makes. `CONFIG.readOnly` is unchanged.
  - The app then checks every 15 seconds for `res-<requestId>.json`, for at most 5 minutes and only while the pilot Flow is open.
- **Reply rules:** it must have the type `trace.flowmsg.response`, an exact matching requestId, and plain text of 1–280 characters. It's shown as text only, and anything else is rejected and reported.
- **Display:** the note sits beneath the card and above the controls. It's labelled with the card it answers, can be dismissed and never blocks the controls. It rises 6 px and fades in over 220 ms with one faint glow, and with reduced motion there's no animation.
- **Reload safety:** a pending request is resumed rather than duplicated. A timeout or error offers "New pilot session".
- The Flow folder `Trace › flowmsg` was created (owner only, sharing unchanged).
- No bridge changes and no new permissions. Live app untouched (1.2.3).

## T-013 — 2026-10-31 — Claude — test — 1.3.4
- Meditation alcove, test only:
  - A loader finds **one** pilot recording, a file matching `*_trace_pilot*.mp3` in `My Drive › Trace › meditation`.
  - It uses only the existing bridge operations `listFolder` and `readBinary`. There are no bridge changes, no new permissions and no file IDs in the repo.
  - It refuses anything over the bridge's 8 MB limit, and checks that the downloaded byte count matches.
  - It keeps the file on this device (key `medPilot` in the device's own storage) and checks that it decodes.
  - It plays the file through the player's existing recording hook.
  - The screen shows four separate steps: **found**, **downloaded**, **decoded** and **actually played** (the audio has advanced past 5 seconds).
- Recording controls: a progress line with a seek bar and time, plus play, pause, resume and stop. Device-voice samples are unchanged.
- **Offline:** it falls back to the copy already on the device. Errors show "Try again".
- Writes nothing to the Sheet or Drive, and creates no study activity. Live app untouched (1.2.3).

## T-012 — 2026-10-31 — Claude — docs
- `AGENTS.md` guidance version 2:
  - checkpoint and delta reading rules (§12),
  - code watch-lists for live, test, bridge and visual work,
  - stale-marker rules,
  - Drive-mirror fingerprint rules,
  - the meditation producer/consumer plan (not active).
- `CHANGELOG.md` format 2: State block and stable entry IDs. The 1.2.0–1.2.2 dates are corrected to 31 Oct from the git history.
- Contract version 3.1. Presentation only; the files, columns and matching rules are unchanged:
  - §2 now describes the 1.3.3 viewer,
  - §9 uses the real PANC-14 mapping (the calcium exception goes to seq-03 "The hose at the goal"),
  - the placeholder test pass is now kept separate from real acceptance.
- No app code, live code, bridge or data changed.

## T-011 — 2026-10-31 — Claude — test — 1.3.3
- Text card answer view: "Question parts" starts **open**, and one touch closes it. The question side is unchanged, and Reveal never opens the visual viewer.
- Visual viewer: **card-level clinical notes** are available on every scene of the card, whether reached from the overview or entered directly. They sit in a section that starts **closed**. Scene notes stay on their own scene.
- Visual viewer, **Learn**: each cue sits beside its meaning directly under the image, with no taps. **Self-test** is unchanged: meanings stay hidden until "Reveal meaning".
- Live app untouched (1.2.3).

## T-010 — 2026-10-31 — Claude — docs
- `AGENTS.md` (shared rules for any assistant), `CHANGELOG.md` and `docs/visual-deck-contract.md` were added to the repo, with copies in `My Drive › Trace › docs`.

## T-009 — 2026-10-31 — Claude — bridge — v3
- Bridge v3 was deployed by Naven on the same link. It adds the Targets tab (two-way targets with the War Map), plus `visualIndex` and `readBinary` for visual decks.

## T-008 — 2026-10-31 — Claude — test — 1.3.2
- Validator fixes:
  - heading links are rejected,
  - the soft line break is written explicitly,
  - the test build was refreshed.

## T-007 — 2026-10-31 — Claude — test — 1.3.1
- Visual decks in Flow:
  - download and validate packages from Drive,
  - tappable heading and phrases on the answer side,
  - a side panel on landscape screens, full screen on the phone,
  - the panel shows scenes, hotspots, cues (Learn and Self-test), stories and clinical notes.
- `backend/trace_validate.py` uses the same rules as the app (parity checked on the demo decks).
- This device screen: visual-deck status and "Check visual decks now".

## T-006 — 2026-10-31 — Claude — test — 1.3.0
- Test build at `/test/`: it has its own storage, borrows the connection, and never writes to the Sheet or Drive.
- Palace home with landscape and portrait artwork and four rooms: Loft, Decks, Flow, Meditation. The window has no function.
- Meditation alcove: morning, afternoon and night guidance, plus four scenario playlists (sample scripts, device voice).

## T-005 — 2026-10-31 — Claude — live — 1.2.3
- Duplicate War Map Log rows are ignored, and a card counts once per day in the history.

## T-004 — 2026-10-31 — Claude — live — 1.2.2
- War Map history is rebuilt from the full Log on every sync, so open copies no longer double-count.

## T-003 — 2026-10-31 — Claude — live — 1.2.1
- Updates install themselves (checked every 10 minutes and whenever the app is reopened).

## T-002 — 2026-10-31 — Claude — live — 1.2.0
- Loft month calendar with a day panel, collapsible chronicles, and War Map card numbering for split decks.

## T-001 — 2026-10-31 — Claude — live — 1.0.0–1.1.0
- First releases: offline card cabinet (1.0.0), paste-to-connect setup (1.0.1), and the shelf, Loft, Flow builder, look mode, shared targets, NEET glow, zoom and emblems (1.1.0).
