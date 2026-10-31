# Trace — change log

In progress: none

## 1.3.3 — 2026-10-31 — Claude — test
- Text card answer view: "Question parts" starts open (touch to close). The question side is unchanged and Reveal never opens the visual viewer.
- Visual viewer: card-level clinical notes are available on every scene of the card (overview and scenes entered directly), in a section that starts closed (touch to open). Scene notes stay on their own scene.
- Visual viewer, Learn: each cue sits beside its meaning, right under the image, with no taps. Self-test is unchanged: meanings stay hidden until "Reveal meaning".
- Live app untouched (still 1.2.3).

## bridge v3 — 2026-10-31 — Claude — bridge
- Bridge v3 deployed by Naven: Targets tab (two-way targets with the War Map), visualIndex + readBinary for visual decks.

## 1.3.2 — 2026-10-31 — Claude — test
- Visual decks in Flow: download and validate packages from Drive, tappable heading and phrases on the answer side, side panel (landscape) or full screen (phone) with scenes, hotspots, cues (Learn / Self-test), stories and clinical notes.
- `backend/trace_validate.py`, identical rules to the app (parity checked).
- This device screen: visual deck status and "Check visual decks now".

## 1.3.0 — 2026-10-31 — Claude — test
- Test build at /test/: own storage, borrows the connection, never writes to the Sheet or Drive.
- Palace home (landscape and portrait artwork, four rooms: Loft, Decks, Flow, Meditation; the window has no function).
- Meditation alcove: morning, afternoon and night guidance plus four scenario playlists (sample scripts, device voice).
- Loft: "The quiet alcove" entry. Bottom bar: Palace · Shelf · Flow · Changes.

## 1.2.3 — 2026-10-31 — Claude — live
- Duplicate War Map Log rows ignored; a card counts once per day in history.

## 1.2.2 — 2026-10-30 — Claude — live
- War Map history rebuilt from the full Log on every sync (no double counting across open copies).

## 1.2.1 — 2026-10-30 — Claude — live
- Updates install themselves (checked every 10 minutes and on reopen).

## 1.2.0 — 2026-10-30 — Claude — live
- Loft month calendar with a day panel, collapsible chronicles, War Map card numbering for split decks.
