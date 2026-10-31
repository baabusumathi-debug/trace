# AGENTS.md — working on Trace

Read this whole file before you change anything. It is written for **any AI assistant** working on this project
(Claude, ChatGPT, Grok, Muse or others) and for Naven. Each assistant reads it at the start of a task and keeps it true at the end.

---

## 1. What Trace is

Trace is Naven's (Dr. Harish's) offline card app for the **NEET-SS DM Critical Care** exam, which is on **11–12 Dec 2026**.

- **What it is:** an installable web app (PWA) used on a Galaxy Tab S10 Ultra (mostly landscape), an Android phone and a MacBook.
- **What it does:** shows text flashcards from Drive. Naven "walks" cards in **Flow** sessions, and his progress goes to the **War Map**, the Google Sheet "CCM War Map Data". His study partner **HT (Harshita)** uses the War Map, so she sees his Trace progress there.
- **Who's who in the data:** in the Sheet and the War Map, Naven's rows carry `who = "Trace"`, and HT's carry other names.

## 2. Roles

| Area | Who |
|---|---|
| App code (this repo), card text, Drive layout, sync, Sheet integration | **Any assistant** Naven assigns the task to |
| **Visual decks** (images, stories, cues, hotspots, correction notes) | **ChatGPT only**. See section 9. |
| Pasting and redeploying the Apps Script bridge | **Naven**, from code an assistant prepares (section 7) |
| Deciding what ships to the live app | **Naven** |

**One assistant works on the app at a time.** Before you start, read the "In progress" line at the top of `CHANGELOG.md`.
- If it names another assistant and is less than 24 hours old, stop and ask Naven.
- Otherwise, write your own line there before you begin, and clear it when you finish.

## 3. Rules that are never broken

1. **Never lose or corrupt Naven's data.** Progress lives in IndexedDB on each device, in the Sheet and in Drive.
   - Never delete, rewrite or reorder existing Sheet rows.
   - Trace only **appends** to `Log`, appends to `TraceEvents`, and appends to or updates the status of `Targets`.
2. **Test first.** Every change goes to the test build (`/test/`, section 6) and is checked there. It reaches the live app only after Naven says "promote".
3. **Change the version number on every release.**
   - Bump `CONFIG.appVersion` in `js/config.js` **and** `VERSION` in `sw.js`.
   - If you don't, devices keep the old cached files forever.
4. **No secrets in the repo.** The bridge key and the setup link (`#setup=…`) are private.
   - `backend/Code.gs` here carries the placeholder `__TRACE_KEY__`. Never commit the real key.
   - Never paste the setup link into a file, a commit, an issue or a chat that others can read.
5. **Don't build anything that can rewrite running code from a request.** That includes self-updating bridges, `eval` of fetched code, and remote script loaders. Bridge updates are always pasted by Naven.
6. **Keep the card text as it is.** Card wording comes from Naven's decks. Edits Naven makes in the app are stored separately (`Trace/edits.json`), and the original stays untouched.
7. **Log what you did** in `CHANGELOG.md` (section 11), with your name.

## 4. Where everything lives

| What | Where |
|---|---|
| App code | GitHub `baabusumathi-debug/trace`, branch `main`, served by GitHub Pages |
| Live app | https://baabusumathi-debug.github.io/trace/ (repo root) |
| Test build | https://baabusumathi-debug.github.io/trace/test/ (repo `test/` folder) |
| Drive root for Trace | `My Drive › Trace` (folder id `1e_lx6kl_MhG4aOracgTr_HG3NUp7OsYs`) |
| Deck library | `Trace › library.json`. The app finds the newest non-trashed file by name. |
| One deck | `Trace › decks › <DECKCODE> › cards.jsonl` (+ `deck.json`) |
| Visual decks | `Trace › decks › <DECKCODE> › visual ›` (section 9) |
| Naven's card edits | `Trace › edits.json` |
| War Map Sheet | "CCM War Map Data", id `150OxumS0XPBlPfmiNP9HLxwPrjUGEzbmmIBknvNJssk` |
| Bridge | Apps Script project **"Trace Backend"** in Naven's account, deployed as a web app |
| Shared docs for assistants | `My Drive › Trace › docs`: copies of this file, `CHANGELOG.md` and the visual-deck contract. The validator is downloaded from https://baabusumathi-debug.github.io/trace/backend/trace_validate.py so there is only ever one copy. **The repo is the master copy.** Whoever changes one of these updates both places. A Drive file can't be edited in place by every tool, so upload the new copy and trash the old one. |

**Sheet tabs Trace may touch**, as enforced by the bridge:

| Tab | Permission |
|---|---|
| `TraceEvents` | read + write |
| `Log` | read + append |
| `Targets` | read + append + update status |
| `Chunks`, `Decks`, `Signals` | read only |

**Card fields** (one JSON object per line in `cards.jsonl`): `deck, code, no, section, q, a, why, watch, hook, q_page, a_page, img`.
- `q` holds the heading first.
- Lettered sub-parts look like `a Text` or `**a** Text`.
- `- ` starts a list line. `x | y` lines are table rows.

## 5. The app's files

Plain JavaScript modules, with no build step and no framework. Fonts are self-hosted, with no external requests.

| File | Responsibility |
|---|---|
| `index.html`, `manifest.webmanifest`, `icons/`, `fonts/`, `img/` | shell, install metadata, assets (`img/` = palace artwork) |
| `css/app.css` | all styles |
| `sw.js` | service worker: caches the app shell for offline use. **Bump `VERSION` on every release.** |
| `js/config.js` | constants, `appVersion`, `CHANNEL` (`live` or `test`, from the URL path), `readOnly` (true in test) |
| `js/db.js` | IndexedDB wrapper. Stores: `kv, decks, events, logrows, edits, visuals, vimg`. Database names: `trace` (live), `trace-test` (test), `trace-demo` (`?demo`). DB version 2. |
| `js/api.js` | talks to the bridge (`batch`, `call`). The connection `{url,key}` is in `kv.backend`. |
| `js/store.js` | in-memory state `S`, counts (`seen`, `walked`), daily stats, War Map numbering (`off(deck)`) |
| `js/sync.js` | sync loop: pulls the library, Log, TraceEvents, edits and targets; pushes events, Log rows, edits and targets; downloads decks |
| `js/md.js` | card text → HTML: `reflow` (undoes PDF line-wrapping), `render`, `splitQ`, `plain` |
| `js/emblems.js` | system and deck emblems |
| `js/app.js` | router and screens: palace (home), shelf, system spread, deck, Flow builder, Flow, Loft, Changes, This device |
| `js/palace.js` | palace home (four rooms on the supplied artwork) and the meditation alcove/player |
| `js/visuals.js` | visual decks: download, validation, tappable phrases, the side panel |
| `backend/Code.gs` | the Apps Script bridge (placeholder key) |
| `backend/trace_validate.py` | the visual-deck validator (section 9) |

**Routes:** `#/` palace · `#/shelf` · `#/sys/<nn>` · `#/deck/<CODE>` · `#/flow` · `#/loft` · `#/meditation` · `#/changes` · `#/status`.

## 6. Test build and release

- **The test build** is a full copy of the app in `test/`, with these differences:
  - In `test/manifest.webmanifest`: name and short_name "Trace Test", and `"id": "./"`.
  - In `test/index.html`: the title "Trace Test".
- **What the test build does on its own**, because it runs from a path containing `/test/`:
  - It uses its own database (`trace-test`).
  - It borrows the live app's connection on that device. It reads `kv.backend` only, and never creates or changes the live DB.
  - It **never writes** to the Sheet or Drive (`CONFIG.readOnly`).
  - It shows a teal **TEST** tag.
- **Cache safety:** service-worker caches are prefixed `trace-v` (live) and `tracetest-v` (test), and each worker only deletes caches with its own prefix.
- **To release to test:**
  1. Edit the files.
  2. Bump the versions.
  3. Copy the app into `test/`, keeping the manifest and title differences above.
  4. Commit and push. Pages publishes within about a minute.
- **To promote** (only after Naven says so): copy `test/` back to the root, with the manifest name "Trace" and the title "Trace". Bump the version, then commit and push. Live devices pick it up within about 10 minutes or on their next open, and reload by themselves unless a Flow is running.
- **Before any release, check:**
  - The app opens offline.
  - Flow works.
  - Sync shows "Synced".
  - The numbers on the This device screen look right.
  - The test build left the Sheet unchanged.
  - Use a mock bridge and real Sheet exports where you can.

## 7. The bridge (Apps Script)

**Operations** (each request carries the key): `ping, readFile, listFolder, findFile, writeFile, sheetRead, sheetAppend (dedupe), sheetUpdate, visualIndex, readBinary, batch`.
- The current version is **3**.
- It only reaches files inside `My Drive › Trace` and the tabs in section 4.

**To change it:**
1. Edit `backend/Code.gs` and bump `VERSION`.
2. Give Naven the full file with the real key filled in, privately.
3. Naven pastes it over Code.gs, then goes to Deploy › Manage deployments › edit (pencil) › Version: **New version** › Deploy. **Not** "New deployment", which would change the link.
4. Check it with This device › Check visual decks now, or a sync.

**Keep bridge changes rare.** Prefer building on the existing basic operations, and batch any needed changes into one update.

## 8. Data rules learned the hard way (don't regress these)

- **War Map numbering.**
  - Split decks are numbered continuously in the War Map (`Decks.card_from`), while Trace's `no` starts at 1 in each deck.
  - Convert with `off(deck) = card_from − 1`. Log, Chunks and Targets use War Map numbers.
- **Counts are rebuilt from the full Log on every sync. Never add to them incrementally.**
  - Earlier, several open copies of the app doubled and tripled the counts.
  - Identical Log rows (`date|who|deck|stage|from|to|time`) are counted once, and a card counts once per day.
- **Owner filter:** only Log rows whose `who` is `trace`, `naven` or blank count as Naven's.
- **Trace's own rows:** Log rows written by Trace have a note starting `Trace app · <id>`. They're excluded from the Log-based counts, because they're already counted from TraceEvents, and they're written with dedupe on that id.
- **Log row format:** `[date, time, "Trace", deck, chunk_id, pass1_exposure|pass2_encoding, cards, minutes, "Trace app · <id>", from, to, ""]`.
- **Targets** go both ways. A target set in Trace appears in the War Map, and the reverse. A target is removed by setting `status = pulled`, never by deleting it.
- **PDF line-wrapping:** card text keeps the PDF's line wrapping. `md.reflow` rejoins the lines, and anything that matches text must use the same reflow (section 9).

## 9. Visual decks: ChatGPT's zone

**ChatGPT** makes and publishes the visual decks. Other assistants don't write inside any `visual/` folder unless Naven explicitly reassigns this work. They may read it, and they maintain the app's side and the validator.

- **The contract:** `docs/visual-deck-contract.md`. It covers the folder layout, the files and columns, the matching rules for tappable phrases, and staged publishing through `current.json`.
- **The validator:** `backend/trace_validate.py`. Run it before switching `current.json`, and switch only on `"result":"pass"`.
- **The app re-validates on every device** with identical rules (`js/visuals.js`). It keeps the previous accepted version if a new one fails.
- **If an assistant changes the matching rules,** it must change `js/visuals.js` and `backend/trace_validate.py` together, re-run the parity check (all demo cards, JS vs Python, plus a rendered-DOM check), and update the contract.
- **Pilot:** GI02B · PANC-14. Then the seven GIT decks: GI01A, GI01B, GI01C, GI02A, GI02B, GI03, GI04A.

## 10. Planned, not active

- **Meditation recordings:** three daily scripts (morning, afternoon, night) written from Naven's real performance, voiced by a TTS service and stored privately for offline listening.
  - The **voice provider and the daily times are undecided.** Don't activate anything until Naven confirms them.
  - API keys stay in the bridge's script properties, never in the app.
- **Palace and meditation home:** built in the test build (1.3.x), and waiting for Naven's "promote".

## 11. CHANGELOG.md

At the top is one **In progress** line: `In progress: <assistant> — <task> — <date time IST>`, or `In progress: none`.

Then add one entry per release, newest first:

```
## 1.3.2 — 2026-10-31 — Claude — test
- what changed, in plain words
- data/safety notes, if any
```

The channel is `test`, `live` or `bridge`. Commit messages start with the version, and end with the assistant's name, plus any attribution lines that assistant's own rules require.

## 12. Talking to Naven

- Be direct and efficient. Give one step at a time when he has to do something, and explain why.
- He shouldn't have to deploy or fix things himself, except for pasting the bridge.
- Say plainly what is in the test build and what is live.
