# Trace — change log

Changelog format: 2 (stable entry IDs `T-NNN`, newest first). The rules for reading and writing this file are in `AGENTS.md` §11–§12.

In progress: none

## State (as of entry T-015)

This summary helps you orient. It **does not prove** that content is unchanged; only a verified commit or content fingerprint does (`AGENTS.md` §12).

| Item | Value |
|---|---|
| Live app (repo root) | **1.2.3** · last code commit `c780cce` |
| Test build (`test/`) | **1.3.5** · last code commit: see entry T-014 (`git log -- test/`) |
| Bridge (Apps Script) | **v3** deployed by Naven 31 Oct · repo source `backend/Code.gs` |
| Guidance | `AGENTS.md` guidance version **4** · `docs/visual-deck-contract.md` contract version **3.1** (schema unchanged from 3) |
| Visual decks | No package published in Drive yet. ChatGPT's real GI02B PANC-14 package passed the validator **locally** (31 Oct). Publication, device download and offline acceptance are **still outstanding**. Claude's earlier test pass used **placeholder** images only. |
| Meditation | Test build only. Sample scripts are read by the device voice, and **one Journal pilot recording** (`Trace › meditation › …_trace_pilot….mp3`) is loaded through the existing bridge. Real file verified in Naven's Chrome on 31 Oct: found, downloaded (6,381,340 bytes), decoded (531.72 s), and actually played to 0:12. Pause held and resume advanced. Not yet checked: offline playback, and whether the sound was actually heard. Nothing is automated or scheduled, and the producer's capabilities are unverified. |
| Flow message pilot | Test build only. The route `#/pilot` sends **one** request, `req-<id>.json`, to `Trace › flowmsg` on the first Next after Reveal, and shows **one** plain-text reply from Journal, `res-<id>.json`, within 5 minutes. **One real round trip passed on 31 Oct (T-015)**, as an active-session pilot. Journal's watch was started by hand in chat, so this is **not** unattended automation. |
| Waiting on Naven | Promote test to live · meditation producer, times and input source · sign-off after the visual pilot |

---

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
