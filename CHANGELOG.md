# Trace — change log

Changelog format: 2 (stable entry IDs `T-NNN`, newest first). The rules for reading and writing this file are in `AGENTS.md` §11–§12.

In progress: none

## State (as of entry T-018)

This summary helps you orient. It **does not prove** that content is unchanged; only a verified commit or content fingerprint does (`AGENTS.md` §12).

| Item | Value |
|---|---|
| Live app (repo root) | **1.2.3** · last code commit `c780cce` |
| Test build (`test/`) | **1.3.7** · last code commit: see entry T-017 (`git log -- test/`). Panel image fix accepted on Naven's Mac (T-018); the phone and Tab haven't been checked on real devices yet. |
| Bridge (Apps Script) | **v4** deployed by Naven on 1 Nov; adds `notifyJournal`, off by default via `JOURNAL_ENABLED`. A lost `readBinary` routing line was restored the same day and redeployed (Naven calls it "v4.1"). Repo source: `backend/Code.gs` (no secrets). |
| Guidance | `AGENTS.md` guidance version **5** · `docs/visual-deck-contract.md` contract version **3.1** (schema unchanged from 3) |
| Visual decks | **GI02B v2** is published by ChatGPT (53 scenes) and was accepted in Naven's Chrome on test 1.3.6 on 1 Nov. Bridge `readBinary` routing was restored by Naven, who deployed it as "v4.1". **Offline acceptance is still outstanding.** GI01A is being prepared by ChatGPT. |
| Meditation | Test build only. Sample scripts are read by the device voice, and **one Journal pilot recording** (`Trace › meditation › …_trace_pilot….mp3`) is loaded through the existing bridge. Real file verified in Naven's Chrome on 31 Oct: found, downloaded (6,381,340 bytes), decoded (531.72 s), and actually played to 0:12. Pause held and resume advanced. Not yet checked: offline playback, and whether the sound was actually heard. Nothing is automated or scheduled, and the producer's capabilities are unverified. |
| Flow message pilot | Test build only. The route `#/pilot` sends **one** request, `req-<id>.json`, to `Trace › flowmsg` on the first Next after Reveal, and shows **one** plain-text reply from Journal, `res-<id>.json`, within 5 minutes. **One real round trip passed on 31 Oct (T-015)**, as an active-session pilot. Journal's watch was started by hand in chat, so that was **not** unattended automation. Since T-016, the test build also asks bridge v4 to wake Journal's webhook routine. **Two automatic wakes passed on 1 Nov with no chat watch** (request/reply pairs `fm-20261101-160706-k5qi7c` and `fm-20261101-161241-a2n8vw` are in Drive). Each took about 37–61 s from request to reply, nearly all of it on Journal's side. Naven then paused Journal work. **The current `JOURNAL_ENABLED` value is unconfirmed.** |
| Waiting on Naven | Promote test to live · meditation producer, times and input source · sign-off after the visual pilot |

---

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
