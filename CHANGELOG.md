# Trace — change log

Changelog format: 2 (stable entry IDs `T-NNN`, newest first). The rules for reading and writing this file are in `AGENTS.md` §11–§12.

In progress: none

## State (as of entry T-012)

This summary helps you orient. It **does not prove** that content is unchanged; only a verified commit or content fingerprint does (`AGENTS.md` §12).

| Item | Value |
|---|---|
| Live app (repo root) | **1.2.3** · last code commit `c780cce` |
| Test build (`test/`) | **1.3.3** · last code commit `0ccae2d` |
| Bridge (Apps Script) | **v3** deployed by Naven 31 Oct · repo source `backend/Code.gs` |
| Guidance | `AGENTS.md` guidance version **2** · `docs/visual-deck-contract.md` contract version **3.1** (schema unchanged from 3) |
| Visual decks | No package published in Drive yet. ChatGPT's real GI02B PANC-14 package passed the validator **locally** (31 Oct). Publication, device download and offline acceptance are **still outstanding**. Claude's earlier test pass used **placeholder** images only. |
| Meditation | Sample scripts read by the device voice (test build only). An automated producer is planned: "Journal bot", on a platform Naven calls "Graphbots". Its identity and capabilities are **unverified**. Nothing is built, connected or scheduled. |
| Waiting on Naven | Promote test to live · meditation producer, times and input source · sign-off after the visual pilot |

---

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
