# Trace — change log

Changelog format: 2 (stable entry IDs `T-NNN`, newest first). The rules for reading and writing this file are in `AGENTS.md` §11–§12.

In progress: none

## State (as of entry T-047)

This summary helps you orient. It **does not prove** that content is unchanged; only a verified commit or content fingerprint does (`AGENTS.md` §12).

| Item | Value |
|---|---|
| Live app (repo root) | **1.4.6** · promoted from test 1.3.28 on 3 Nov (T-047; earlier T-040, first T-026): palace home, meditation, visual decks, QBank/GT layer, Top-ups, Flow desk, save/discard on leaving a flow, new Loft, Going out / breaks. Same code as `test/` except the version and the title. |
| Test build (`test/`) | **1.3.28** · last code commit: see entry T-046. Live is 1.4.6 (= test 1.3.28). (`git log -- test/`). Adds the QBank/GT layer (`test/data/qbank.json`). Panel image fix (1.3.7) accepted on Naven's Mac (T-018); the phone and Tab haven't been checked on real devices yet. |
| Bridge (Apps Script) | **v5** deployed by Naven on 3 Nov (calendar reminders, T-041/T-042) · before that **v4** deployed by Naven on 1 Nov; adds `notifyJournal`, off by default via `JOURNAL_ENABLED`. A lost `readBinary` routing line was restored the same day and redeployed (Naven calls it "v4.1"). Repo source: `backend/Code.gs` (no secrets). |
| Guidance | `AGENTS.md` guidance version **6** · `docs/visual-deck-contract.md` contract version **3.1** (schema unchanged from 3) |
| Visual decks | **GI02B v2** is published by ChatGPT (53 scenes) and was accepted in Naven's Chrome on test 1.3.6 on 1 Nov. Bridge `readBinary` routing was restored by Naven, who deployed it as "v4.1". **Offline acceptance is still outstanding.** GI01A is being prepared by ChatGPT. |
| Meditation | Test build only. Sample scripts are read by the device voice, and **one Journal pilot recording** (`Trace › meditation › …_trace_pilot….mp3`) is loaded through the existing bridge. Real file verified in Naven's Chrome on 31 Oct: found, downloaded (6,381,340 bytes), decoded (531.72 s), and actually played to 0:12. Pause held and resume advanced. Not yet checked: offline playback, and whether the sound was actually heard. Nothing is automated or scheduled, and the producer's capabilities are unverified. |
| Flow message pilot | Test build only. The route `#/pilot` sends **one** request, `req-<id>.json`, to `Trace › flowmsg` on the first Next after Reveal, and shows **one** plain-text reply from Journal, `res-<id>.json`, within 5 minutes. **One real round trip passed on 31 Oct (T-015)**, as an active-session pilot. Journal's watch was started by hand in chat, so that was **not** unattended automation. Since T-016, the test build also asks bridge v4 to wake Journal's webhook routine. **Two automatic wakes passed on 1 Nov with no chat watch** (request/reply pairs `fm-20261101-160706-k5qi7c` and `fm-20261101-161241-a2n8vw` are in Drive). Each took about 37–61 s from request to reply, nearly all of it on Journal's side. Naven then paused Journal work. **The current `JOURNAL_ENABLED` value is unconfirmed.** |
| QBank/GT layer | Test 1.3.8 only. `test/data/qbank.json` (version in the file) holds, per card: bank chips (NEET 25 recall · Marrow · DocT · DocT GT), Top-up lines, Crossfire lines and checked corrections; plus 242 Top-up cards in 94 decks and 5 Top-up decks (80 cards: TU-NEURO 24, TU-IE 15, TU-TX 15, TU-AIR 13, TU-SAFE 13). Built by Claude from the DocT QBank, 20 DocT GTs and the Marrow map; every item was approved by Naven on 2 Nov. Source of truth for its content: the CCM project files `claude/QMap_FINAL_*.csv`. |
| Waiting on Naven | Device check of live 1.4.0 · meditation producer, times and input source · sign-off after the visual pilot |

---

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
