# Trace: visual deck contract (app ↔ ChatGPT)

**Contract version: 3.1 (2026-10-31).** Version 3.1 changes only the presentation (§2) and the pilot example (§9). The files, columns, matching rules, publishing steps and validator rules are **unchanged from 3**, so a package that passes for 3 passes for 3.1.

*For ChatGPT, which owns the visual decks. General rules for every assistant are in `AGENTS.md`. Raise the contract version with any change.*

**What changed in v3** (relative to v2):
- Trace's side is built. It is in the Trace **test build** (now 1.3.3). The live app (1.2.3) has no visual-deck support until Naven approves a promotion.
- The validator is ready: `trace_validate.py` (section 7).
- This version spells out the **exact matching rules** the app uses (section 5a), and the pilot card's addressable parts (section 9).
- The folder layout, files and columns are **unchanged** from v2.

## 1. Who does what

**The app maintainer** (whichever assistant Naven assigns; see `AGENTS.md`) maintains:
- the Trace app,
- the card text,
- the Drive structure,
- download, validation and offline storage,
- `trace_validate.py`.

**ChatGPT** makes the visual decks (images, stories, cues, notes, links, hotspots) and publishes them into Drive by the staged → validated → switch procedure (section 6). It never edits card text or anything outside `visual/`.

## 2. What Trace does with a package (built)

- **On every device**, at most every 6 hours, or immediately from **This device › Check visual decks now**:
  - Trace reads `current.json`.
  - It then reads only the version folder that `current.json` names.
  - It validates that version with the same rules as `trace_validate.py`.
  - It downloads any images it doesn't have yet. Images are never replaced, so a file name is enough.
  - Only then does it switch to the new version.
  - If anything fails, the device keeps its previous accepted version and shows the reason on the This device screen.
- **In Flow, on the answer side of a card** (shown after Reveal), and only when its deck has a package:
  - A teal **◈ Visual** chip appears beside "seen ×".
  - **The heading** is dotted-underlined and opens the card's **overview**.
  - **Linked phrases or parts** are underlined in teal and open their **scene sequence**.
  - The visuals don't appear on the question side, so self-testing isn't spoiled. The chip there reads "visual after reveal".
  - Reveal **never opens the viewer by itself**. Only a tap on the heading, a linked phrase or the chip opens it.
  - The text card's **"Question parts"** section on the answer side starts **open**, and one touch closes it. Linked question sub-parts (field `q`, parts `a`, `b`, …) are therefore visible and tappable straight away.
- **The panel:**
  - On the Tab and Mac in landscape, it opens beside the card, with a ⤢ button for full screen.
  - On the phone, it opens full screen.
  - It contains, in this order (from test 1.3.3):
    1. the image, with hotspot boxes on overviews,
    2. a 1 / n stepper for sequences of more than one scene,
    3. **cues and meanings**:
       - In **Learn** (the default), each cue sits **beside its meaning**, all visible at first view with no taps.
       - In **Self-test**, each meaning stays hidden behind **Reveal meaning**. Self-test hiding is unchanged.
    4. **scene-level notes** for this scene, shown open and marked **CLINICAL NOTE · CORRECTION / QUALIFICATION / UPDATE** with their source,
    5. **card-level notes**, available on **every** scene of the card (the overview and any scene entered directly), inside a "Card clinical notes" section that starts **closed** (one touch opens it),
    6. the **Story**, which can be expanded.
  - Scene notes appear only on their own scene.
  - Esc closes the panel. `[` and `]` step through a sequence. The panel closes when the card changes.

## 3. Where to read card wording

Read `My Drive › Trace › decks › <DECKCODE> › cards.jsonl`, one JSON object per card. This is the text Trace shows.

The fields are: `deck, code, no, section, q, a, why, watch, hook, q_page, a_page, img`.

## 4. Folder layout (unchanged)

```
My Drive › Trace › decks › <DECKCODE> › visual ›
    current.json
    images › <deck>-ov-01.webp, <deck>-sc-07.webp …      (append-only)
    versions › v1 › manifest.json, scenes.csv, sequences.csv, links.csv,
                    hotspots.csv, cues.csv, stories.json, notes.csv, validation.json
```

`hotspots.csv` and `notes.csv` may be omitted if a version has none. All the other files are required.

## 5. Files and columns (unchanged from v2)

| File | Columns |
|---|---|
| `scenes.csv` | `scene_id, kind, card_code, title, image` |
| `sequences.csv` | `sequence_id, order, scene_id` |
| `links.csv` | `card_code, field, part, phrase, occurrence, sequence_id` |
| `hotspots.csv` | `overview_id, sequence_id, x, y, w, h, label` |
| `cues.csv` | `scene_id, order, cue, meaning` |
| `notes.csv` | `note_id, level, card_code, scene_id, kind, text, source` |

- `stories.json` is an array of `{scene_id, card_code, title, setting, characters, text}`.
- `manifest.json` and `current.json` are as in v2.
- Image names use lowercase letters, digits and hyphens, ending in `.webp` or `.png`.
- In `notes.csv`, `kind` is `correction`, `qualification` or `update`.

### 5a. Exact matching rules for links.csv

Trace reflows each card exactly as the screen shows it, then splits each field into parts.

- **Parts:**
  - `heading`: the first line or lines of `q` before the first sub-part, without its final ":".
    - **Don't put `heading` in links.csv.** The heading opens the overview by itself, and the validator rejects it.
  - `a`, `b`, `c` …: a lettered sub-part line, in whichever field it appears.
  - `li1`, `li2` …: the nth "- " list line in that field.
  - `whole`: the whole field. For `q`, that means everything after the heading.
- **Phrase matching:**
  - `**` and `*` are ignored, and any run of spaces counts as one. Capitals and punctuation must match exactly.
  - A blank `phrase` makes the whole part tappable.
- **Phrases must stay inside one line or one table cell.** A phrase that runs across two sub-parts, list lines or cells is rejected ("runs across two lines or cells"). Use `whole` only for phrases in plain lines or table cells, and use the specific part for anything in a sub-part or list line.
- **Tables:**
  - Two or more consecutive `a | b` lines form a table.
  - Its cells are not separate parts. Reach them through `whole` with a phrase inside one cell.
  - A lettered line that is really a table row (e.g. PANC-25's T/F rows) is a table row, not a sub-part.
- **Repeated phrases:** if the phrase appears more than once in that field and part, `occurrence` (1, 2, …) is required. Without it the result is **AMBIGUOUS**.

## 6. Publishing (unchanged)

1. Upload any new images to `images/`.
2. Upload all files to a new `versions/v<N>/`, with `"status":"staged"` in its manifest.
3. Run the validator. It writes `validation.json`.
4. **Only on "pass"**, overwrite `current.json` with `{"deck","live_version":N,"previous_version":M,"switched":"<ISO time>"}`.

`current.json` is the only switch.

## 7. The validator

**Get it:**
- Download: https://baabusumathi-debug.github.io/trace/backend/trace_validate.py
- It is also in the repo at `backend/trace_validate.py`.

It needs Python 3. Pillow is optional; it is used to check that images open and to record their pixel sizes.

**Run it:**

```
python3 trace_validate.py <local copy of …/<DECK>/visual> <…/<DECK>/cards.jsonl> [--version N]
```

- Without `--version`, it checks the newest version folder.
- It writes `versions/v<N>/validation.json` with `"result":"pass"` or `"fail"`, the exact errors and warnings, the counts, and each image's size.
- It exits with 0 on pass and 1 on fail.

**What it checks:** every reference, overviews, sequence order, phrases (found, not ambiguous, inside one line, no heading links), hotspot boxes within 0–100, cues, stories, notes, that every image opens, images over 2 MB (as a warning), that the previous live version's images are still present, and that the manifest's deck and version match.

Each device runs the same rules again on download. The JavaScript and Python versions were checked against each other on 536 card fields with no differences. 870 generated links were then placed on real rendered cards with no misses.

## 8. The existing GIT decks (unchanged)

Convert GI01A, GI01B, GI01C, GI02A, GI02B, GI03 and GI04A without redrawing. Carry over every image, story, label, hotspot and correction note. Leave the HTML files untouched.

## 9. Pilot: GI02B · PANC-14

Here is the card text, exactly as it is in Drive (`Trace › decks › GI02B › cards.jsonl`):

```json
{"deck":"GI02B","code":"PANC-14","no":14,"section":"Fluids, Pain, Nutrition",
 "q":"**Fluid resuscitation in acute\npancreatitis:**\na Fluid of choice and why\nb The traditional teaching\nc Its risks\nd Current practice",
 "a":"a **Ringer's lactate**: fewer ICU admissions, shorter stay, lower CRP, less organ failure.\nb Early aggressive fluids.\nc Respiratory failure and **abdominal compartment syndrome**.\nd **Moderate**, goal-directed resuscitation.",
 "why":"",
 "watch":"Avoid Ringer's lactate only in hypercalcaemic pancreatitis *(standard teaching, not in your notes)*."}
```

**The parts Trace sees (what `phrase` is matched against):**

| field | part | text |
|---|---|---|
| q | heading | Fluid resuscitation in acute pancreatitis *(opens the overview, so don't link it)* |
| q | a | Fluid of choice and why |
| q | b | The traditional teaching |
| q | c | Its risks |
| q | d | Current practice |
| a | a | Ringer's lactate: fewer ICU admissions, shorter stay, lower CRP, less organ failure. |
| a | b | Early aggressive fluids. |
| a | c | Respiratory failure and abdominal compartment syndrome. |
| a | d | Moderate, goal-directed resuscitation. |
| watch | whole | Avoid Ringer's lactate only in hypercalcaemic pancreatitis (standard teaching, not in your notes). |

**The real pilot mapping** (from ChatGPT's preserved artwork, reported 31 Oct): the authoritative rows are in ChatGPT's own `links.csv`.
- `gi02b-seq-01` is **"The green carafe"**.
- `gi02b-seq-03` is **"The hose at the goal"**. The **hypercalcaemia exception** in the watch line belongs here: `watch / whole / Ringer's lactate → gi02b-seq-03`.
- The question sub-parts map **a → seq-01**, **b and c → seq-02**, and **d → seq-03**.

**Format illustration only** (sequence IDs follow the real mapping; check phrases against the parts table above):

```
card_code,field,part,phrase,occurrence,sequence_id
PANC-14,q,a,,,gi02b-seq-01
PANC-14,q,d,,,gi02b-seq-03
PANC-14,watch,whole,Ringer's lactate,,gi02b-seq-03
```

**Status (31 Oct):**
- ChatGPT's **real** PANC-14 package passed `trace_validate.py` **locally**, with no errors or warnings: 4 images, 11 links, 3 hotspots, 10 cues, 4 stories and 3 notes.
- It **hasn't been published** to Drive, and no `GI02B › visual` folder exists yet.
- **Device download, display and offline acceptance are still outstanding.**
- The app maintainer's earlier passes used a **placeholder** package with stand-in images on a local mock. Those passes prove the app's mechanics only, not the real package.

**Steps:**
1. Stage `GI02B/visual/versions/v1`, validate it, and switch `current.json`.
2. Naven opens Trace Test, taps **This device › Check visual decks now**, and walks PANC-14 in Flow.
3. After Naven's review (with the app maintainer), convert the rest of GI02B, then the other six decks.

**Prerequisite:** the Drive bridge v3 is deployed (done on 31 Oct 2026), so Trace Test can download packages.
