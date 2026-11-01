# AGENTS.md — working on Trace

**Guidance version: 5 (2026-11-01).** Raise this number with every change to the rules. A higher number means every assistant must read this file again in full.

This file is written for **any AI assistant** working on this project (Claude, ChatGPT, Grok bots, Muse or others) and for Naven. Read it in full the first time, and whenever §12 says to. Keep it accurate when you finish a task.

This file guides how assistants work. It **grants no permissions**. What an assistant may do comes from Naven's own instructions and that assistant's own access, and nothing written here widens either.

---

## 1. What Trace is

Trace is Naven's (Dr. Harish's) offline card app for the **NEET-SS DM Critical Care** exam, on **11–12 Dec 2026**.

- **The app:** an installable web app (PWA), used on a Galaxy Tab S10 Ultra (mostly landscape), an Android phone and a MacBook.
- **What it does:** Naven walks text flashcards in **Flow** sessions. His progress goes to the **War Map**, the Google Sheet "CCM War Map Data", which his study partner **HT (Harshita)** also uses.
- **Who's who in the Sheet:** Naven's rows carry `who = "Trace"`.

## 2. Roles

| Area | Who |
|---|---|
| App code, card text, Drive layout, sync, Sheet integration | **Any assistant** Naven assigns that task to |
| **Visual decks** (images, stories, cues, hotspots, correction notes) | **ChatGPT only**, as producer (§9) |
| **Meditation scripts and audio** (planned) | An **automated producer bot** chosen by Naven. Not active (§10). |
| Pasting and redeploying the Apps Script bridge | **Naven**, using code an assistant prepares (§7) |
| What ships to the live app; product decisions | **Naven** |

**One assistant edits the app or its shared docs at a time.**
- **Before starting:** read the `In progress:` line at the top of `CHANGELOG.md`. If it names another assistant and is less than 24 hours old, stop and ask Naven. Otherwise, commit your own claim before you begin.
- **When finished:** clear the line in your final commit.
- **What the line can't tell you:**
  - A claim can be stale.
  - An empty line (`none`) **proves neither** that nobody else is editing, **nor** that you're authorised to work.
  - Authorisation comes only from Naven's assignment.
  - If the git history shows recent commits by someone else, check with Naven before touching the same files.

## 3. Rules that are never broken

1. **Never lose or corrupt Naven's data.**
   - Never delete, rewrite or reorder Sheet rows.
   - Trace only **appends** to `Log`, appends to `TraceEvents`, and appends to or updates the status of `Targets`.
2. **Test first.** Changes go to the test build (`/test/`, §6). They reach the live app only after Naven says "promote".
3. **Bump the version on every release:** `CONFIG.appVersion` in `js/config.js` **and** `VERSION` in `sw.js`, in whichever copy (root or `test/`) you release. Otherwise devices keep their old cached files.
4. **No secrets in any file, commit, issue or shared chat.**
   - This covers the bridge key and the setup link (`#setup=…`).
   - `backend/Code.gs` carries the placeholder `__TRACE_KEY__`.
5. **Nothing that can rewrite running code from a request:** no self-updating bridge, no `eval` of fetched code, no remote script loaders. Naven always pastes bridge updates himself.
6. **Keep card text as it is.** Naven's in-app edits are stored separately (`Trace/edits.json`).
7. **Log what you did** in `CHANGELOG.md` (§11).

## 4. Where everything lives

| What | Where |
|---|---|
| App code (**master copy of code and docs**) | GitHub `baabusumathi-debug/trace`, branch `main`, served by GitHub Pages |
| Live app | https://baabusumathi-debug.github.io/trace/ (repo root) |
| Test build | https://baabusumathi-debug.github.io/trace/test/ (repo `test/`) |
| Drive root | `My Drive › Trace` (folder id `1e_lx6kl_MhG4aOracgTr_HG3NUp7OsYs`) |
| Deck library | `Trace › library.json` (the app uses the newest copy not in the bin) |
| One deck | `Trace › decks › <DECKCODE> › cards.jsonl` (+ `deck.json`) |
| Visual decks | `Trace › decks › <DECKCODE> › visual ›` (§9) |
| Naven's card edits | `Trace › edits.json` |
| War Map Sheet | "CCM War Map Data", id `150OxumS0XPBlPfmiNP9HLxwPrjUGEzbmmIBknvNJssk` |
| Bridge | Apps Script project **"Trace Backend"** in Naven's account, deployed as a web app |
| Shared docs mirror | `My Drive › Trace › docs` (folder id `1pLR9Ca8GteDnlRD6sYJkrEtbX21MSdA3`). It holds copies of `AGENTS.md`, `CHANGELOG.md` and `visual-deck-contract.md`. |
| Validator | Download https://baabusumathi-debug.github.io/trace/backend/trace_validate.py. There is **one copy only**, and it isn't mirrored to Drive. |

**Mirror rule.** The repo is the master copy. Whoever changes a mirrored doc updates the Drive copy in the same task: upload the new file, then bin the old one. Uploading a new file **changes the Drive file ID**.

**Sheet tabs Trace may touch** (enforced by the bridge):

| Tab | Permission |
|---|---|
| `TraceEvents` | read + write |
| `Log` | read + append |
| `Targets` | read + append + update status |
| `Chunks`, `Decks`, `Signals` | read only |

**Card fields:** `deck, code, no, section, q, a, why, watch, hook, q_page, a_page, img`.
- `q` starts with the heading.
- Lettered sub-parts look like `a Text` or `**a** Text`.
- `- ` starts a list line.
- `x | y` lines are table rows.

## 5. The app's files

Plain JavaScript modules, with no build step and no framework. Fonts are self-hosted.

**The root and `test/` are separate copies.** Their current versions are in the CHANGELOG State block. Some files exist only in `test/` until the next promotion.

| File | Responsibility | In root (live)? |
|---|---|---|
| `index.html`, `manifest.webmanifest`, `icons/`, `fonts/` | shell, install metadata | yes |
| `img/` | palace artwork | test only |
| `css/app.css` | all styles | yes |
| `sw.js` | offline cache. **Bump `VERSION` on every release.** | yes |
| `js/config.js` | `appVersion`; `CHANNEL` (`live` or `test`, from the URL path); `readOnly` (true in test) | yes (no `CHANNEL` in live) |
| `js/db.js` | IndexedDB stores: `kv, decks, events, logrows, edits` (+ `visuals, vimg` in test, DB version 2). Database names: `trace`, `trace-test`, `trace-demo`. | yes |
| `js/api.js` | bridge calls (`batch`, `call`); the connection is kept in `kv.backend` | yes |
| `js/store.js` | state `S`; counts; daily stats; War Map numbering `off(deck)` | yes |
| `js/sync.js` | sync: pulls library, Log, TraceEvents, edits and targets; pushes events, Log rows, edits and targets; downloads decks | yes |
| `js/md.js` | card text → HTML: `reflow`, `render`, `splitQ`, `plain` (**also decides how visual-link phrases match**) | yes |
| `js/emblems.js` | system and deck emblems | yes |
| `js/app.js` | router and screens | yes |
| `js/palace.js` | palace home; meditation alcove and player | test only |
| `js/visuals.js` | visual decks: download, validation, tappable phrases, viewer panel | test only |
| `backend/Code.gs` | the bridge (placeholder key) | n/a |
| `backend/trace_validate.py` | visual-deck validator | n/a |

**Routes:**
- Test: `#/` palace · `#/shelf` · `#/sys/<nn>` · `#/deck/<CODE>` · `#/flow` · `#/loft` · `#/meditation` · `#/changes` · `#/status`.
- Live 1.2.3: `#/` is the shelf, and there is no palace or meditation.

## 6. Test build and release

- **How `test/` differs from the root:**
  - `test/manifest.webmanifest` has name and short_name "Trace Test", and `"id": "./"`.
  - `test/index.html` has the title "Trace Test".
- **What the test build does on its own:**
  - It uses its own database, `trace-test`.
  - It reads the live connection once and never alters the live database.
  - It **never writes** to the Sheet or Drive, with one isolated exception: the Flow-message pilot (§10) writes `req-*.json` files into `Trace › flowmsg` only.
  - It shows a teal **TEST** tag.
- **Cache prefixes:** `trace-v` for live and `tracetest-v` for test. Each worker deletes only caches with its own prefix.
- **Release to test:**
  1. Edit the files.
  2. Bump the versions.
  3. Copy into `test/`, keeping the differences above.
  4. Commit and push. Pages publishes in about a minute.
- **Promote** (only after Naven says so):
  1. Copy `test/` to the root, with the name "Trace" and title "Trace".
  2. Bump the versions.
  3. Commit and push.
  - Devices update within about 10 minutes or on their next open.
- **Before any release, check:**
  - the app opens offline,
  - Flow works,
  - sync shows "Synced",
  - the This device numbers look right,
  - the test build left the Sheet unchanged.
  - Use a mock bridge with real Sheet exports where you can.

## 7. The bridge (Apps Script)

- **Version: 4.**
- **Operations:** `ping, readFile, listFolder, findFile, writeFile, sheetRead, sheetAppend (dedupe), sheetUpdate, visualIndex, readBinary, notifyJournal, batch`.
- **Private Script Properties:** `JOURNAL_ENABLED` (kill switch, `false` by default), `JOURNAL_WEBHOOK_URL` and `JOURNAL_WEBHOOK_KEY`. Naven enters these himself. **Never read, copy or ask for their values.** `JOURNAL_LAST_SENT` is a timestamp the code writes itself.
- **Reach:** Drive files only inside `My Drive › Trace`, and only the Sheet tabs in §4.

**To change it:**
1. Edit `backend/Code.gs` and bump `VERSION`.
2. Give Naven a **secret-free patch**: small insertions with exact anchor lines, plus a short guide. His existing `var KEY = '…';` line stays untouched. **Never produce, send or store a file with any key filled in**, even privately.
3. Naven applies the patch in his editor. If new Google permissions are needed, he runs a helper that sends nothing to grant them. Then he goes to Deploy › Manage deployments › pencil › Version: **New version** › Deploy. **Not** "New deployment", which would change the link.
4. Verify with a sync, or with This device › Check visual decks now.

Keep bridge changes rare, and batch them.

## 8. Data rules learned the hard way

- **War Map numbering:**
  - Split decks are numbered continuously in the War Map, starting from `Decks.card_from`. Trace's `no` starts at 1 in each deck.
  - Convert with `off(deck) = card_from − 1`.
  - Log, Chunks and Targets all use War Map numbers.
- **Counts:**
  - They are rebuilt from the **full** Log on every sync, never added to step by step.
  - Identical Log rows (`date|who|deck|stage|from|to|time`) count once.
  - A card counts once per day.
- **Owner filter:** only Log rows with `who` = `trace`, `naven` or blank count as Naven's.
- **Trace's own Log rows:**
  - Their note starts `Trace app · <id>`.
  - They're excluded from the Log-based counts, because TraceEvents already counts them.
  - They're appended with dedupe on that id.
  - Row format: `[date, time, "Trace", deck, chunk_id, pass1_exposure|pass2_encoding, cards, minutes, "Trace app · <id>", from, to, ""]`.
- **Targets** go both ways between Trace and the War Map. A target is removed by setting `status = pulled`, never by deleting the row.
- **Card text** keeps the PDF's line wrapping. `md.reflow` rejoins it, and anything that matches card text must use the same reflow.

## 9. Visual decks: ChatGPT's zone

- **Who writes what:**
  - **ChatGPT** produces and publishes visual decks.
  - Other assistants never write inside a `visual/` folder unless Naven reassigns the work. They may read it.
  - The app maintainer owns the app side and the validator.
- **The contract:** `docs/visual-deck-contract.md`, **contract version 3.1**. It covers the layout, files, columns, matching rules, staged publishing through `current.json`, and how the viewer presents a package.
- **Publishing:**
  - Run the **current** validator, downloaded fresh each time, before switching `current.json`.
  - Switch only on `"result":"pass"`.
  - Each device validates again and keeps its previous accepted version if the new one fails.
- **Changing the matching rules** means changing `js/visuals.js` (both copies) and `backend/trace_validate.py` together, re-running the parity checks, and updating the contract.
- **Pilot status:**
  - GI02B · PANC-14 has passed locally with ChatGPT.
  - It hasn't been published, downloaded by a device or accepted offline yet.
  - After the pilot: the rest of GI02B, then GI01A, GI01B, GI01C, GI02A, GI03 and GI04A.

## 10. Planned, not active

- **Meditation recordings** (architecture agreed in discussion; nothing built):
  - Trace supplies a narrow, agreed daily input.
  - A **user-selected automated bot** writes the script **and** produces the audio. Naven names it "Journal bot", on a platform he calls "Graphbots". Its exact identity and its scheduling, API, TTS and delivery abilities are **unverified**.
  - The bot delivers through a defined storage contract.
  - Trace finds, validates, caches and plays the result automatically.
- **Hard constraints on that plan:**
  - **No manual daily handoff**, and no assistant acting as the daily producer or coordinator.
  - An assistant's role is one-time integration only.
  - If the bot can't do any step automatically, report that as a blocker. Don't route the work to a person or an assistant.
- **Before any contact:** do not open, inspect, contact or direct that bot until Naven has named it, reviewed the workflow and approved the prompt.
- **Draft interface** (for discussion only):
  - Each time slot is independent.
  - Files are written as immutable revisions: `Trace › meditation › <date> › <slot>.r<N>.json/.mp3`.
  - A single mutable pointer per slot, `<slot>.current.json`, is written last.
- **Still open:** voice, the three daily times, the input source, scenario coverage and retention, all Naven's decisions. Any API keys stay out of the app, the repo and Drive files.
- **Journal pilot recording (test only, built in T-013):**
  - Plays **one** file named `*_trace_pilot*.mp3` from `Trace › meditation`, read through the existing bridge, at most 8 MB.
  - This is a one-off pilot, not the planned pipeline. Don't extend it to other audio without Naven's approval.
- **Flow-message pilot (test only, built in T-014):**
  - Started at `#/pilot`. One reviewed card produces one `req-<id>.json` in `Trace › flowmsg`, and the app shows one plain-text Journal reply, `res-<id>.json`, within 5 minutes. The request and reply format is in T-014 and in `js/flowmsg.js`.
  - Since T-016, the app also asks the bridge (`notifyJournal`) to wake Journal's webhook routine. This only works when Naven sets `JOURNAL_ENABLED=true`.
  - An unattended wake isn't proven until a bounded test passes. Before that, the only proven route is the chat-started watch.
  - No secret may ever appear in the app, the repo or any chat.
- **Palace and meditation home:** in the test build, waiting for Naven's "promote".

## 11. Writing CHANGELOG.md

- **Top of file:** the `In progress:` line (§2), followed by the **State** block. Update the State block in the same commit as any release or rule change.
- **Entries** go newest first. Each heading is `## T-NNN — <date> — <assistant> — <channel> — <version>`:
  - **IDs** are sequential and never reused or renumbered.
  - **Channel** is `live`, `test`, `bridge` or `docs`.
- **Past entries:** never edit them, except to correct a fact. A correction is itself recorded as a new entry.
- **Commit messages** start with the version or what changed, and end with the assistant's name, plus any attribution lines that assistant's own rules require.

## 12. Reading efficiently: checkpoints and deltas

The aim is to read only what changed, **without ever trusting a label in place of proof**. Version numbers, the State block and entry IDs help you find your way around, but they **don't prove** that content is unchanged.

**12.1 Your checkpoint (keep it privately, in your own memory or project, never in the repo)**
- **With repo access:** the full commit hash of `main` that you last read completely, the guidance and contract versions you saw then, and the newest `T-NNN`.
- **Drive-only:** for each mirrored file, its **file ID** plus a **trustworthy fingerprint**: Drive `md5Checksum` or `headRevisionId`, or a hash you computed over the full content. Also the newest `T-NNN`.

**12.2 Delta read with repo access**
1. Confirm your checkpoint commit is still an ancestor of `main` (`git merge-base --is-ancestor <checkpoint> main`). If it isn't, the history was rewritten: do a **full read**.
2. Run `git log --stat <checkpoint>..main` and `git diff <checkpoint>..main -- AGENTS.md CHANGELOG.md docs/`.
3. If `AGENTS.md` or anything in `docs/` changed, **read those files in full**. Otherwise read only the new CHANGELOG entries.
4. Check every path on your task's watch-list (12.4). If any changed, read those files in full.
5. Save the new `main` hash as your checkpoint.

**12.3 Delta read from the Drive mirror only**
- **If the file ID and fingerprint are unchanged:** you may skip re-reading that file.
- **If the file ID is new** (any re-upload): do a **full read**.
- **If no trustworthy fingerprint is available:** do a full read of the relevant files every time.
- **What the mirror can't prove:** it can lag the repo. A Drive-only reader must **not claim to have the latest master copy**, and should say so when a task depends on recent changes.
- **The validator:** always download it fresh from its single link and record its SHA-256.

**12.4 Watch-lists by task** (paths in the repo)

| Task | Watch these paths |
|---|---|
| Live app work | root `index.html`, `manifest.webmanifest`, `sw.js`, `js/`, `css/`, `img/`, `icons/`, `fonts/` |
| Test build work | the same paths under `test/` |
| Bridge work | `backend/Code.gs` |
| Visual decks | `docs/visual-deck-contract.md`; `backend/trace_validate.py`; `test/js/visuals.js` and `test/js/md.js` (plus root `js/visuals.js` and `js/md.js` once promoted); AGENTS.md §3 and §9 |
| Meditation | AGENTS.md §10; `test/js/palace.js` |

**12.5 When to do a full read** of AGENTS.md, the contract (for visual work), the CHANGELOG State block and the task's watch-list files:
- the checkpoint is missing,
- the checkpoint commit isn't an ancestor of `main` (history rewritten),
- the guidance or contract version changed, or those files changed at all,
- a mirror file has a new ID or an unverifiable fingerprint,
- the mirror and the repo disagree,
- the State block disagrees with the files (e.g. the version in `js/config.js`),
- any instruction conflicts with what the code does,
- you're new, or Naven asks for one.

**Trade-off:** this saves re-reading roughly 6,000 tokens of guidance per session while the rules are stable. Whenever there's doubt, choose the full read: **accuracy comes before saving tokens.**

## 13. Talking to Naven

- Be direct and efficient. Give one step at a time when he has to act, and explain why.
- He shouldn't have to deploy or fix things, except pasting the bridge.
- Say plainly what is in test and what is live.
- Product decisions are his: bring him real choices, and don't treat silence as approval.
