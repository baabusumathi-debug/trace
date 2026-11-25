# Rater task: where does the viva lesson add explanation to the NEET packet? (P12 cardiology)

You are an independent rater for Dr Naven Harish's study app Trace. He sits **NEET-SS DM Critical Care on 11–12 Dec 2026**. The NEET cardiology packet P12 is his MCQ preparation and **stays the main lesson for every card**: it already carries the numbers, cut-offs and traps. Weeks ago he studied many of the same cards in viva lessons (packages P1, P5, P8, P10, P11), and some of those taught him better.

**The one question you answer per card: does a viva lesson explain this card better than the P12 lesson, in a way that adds understanding?** If yes, it will be offered beside the P12 lesson so he can revise with it. You are not judging which lesson answers MCQs better; P12 has that job.

## Input
Google Drive › My Drive › Trace › `P12_Viva_Rate_batch1.json`, `…batch2.json`, `…batch3.json` (97 pairs). Do the batch you are told to do, all of it.

Each pair:
- `pair` — id (R001…R097)
- `card` — the card: `q`, `a`, `why`, `watch` (already corrected)
- `p12` — the NEET packet step: `id`, `section`, `question`, `bridge`, `lesson`
- `viva` — 1–6 viva versions of the same card: `id`, `question`, `bridge`, `lesson`, `callback` (true when it opens "You met this card…" and builds on an earlier viva lesson)

Markup: `[[…]]` = takeaway line, `{{…}}` = on-screen text or a model/picture description (not spoken), `{{pic}}` = a picture.

## Read the P12 lesson and every viva version in full. For each viva version, judge what it adds:
- **adds** — what does it explain that the P12 lesson doesn't, or explains more clearly? Examples: the mechanism behind a number, a cause-and-effect chain, a patient that shows why it matters, a different angle that makes the same fact click, a comparison that separates two look-alikes. Say exactly what, in one or two sentences.
- **value** 0–3: 0 = adds nothing (repeats P12 or is thinner) · 1 = small extra · 2 = clearly better explanation of part of the card · 3 = explains the card much better than P12.
- **standalone** yes/no — does it make sense played on its own inside the P12 step? A callback that leans on "the lesson before" is usually no; say if only its first line needs dropping.
- **conflicts** — anything in it that contradicts the P12 lesson or the card (a different number, an older guideline). This matters because he'll hear both.

## Fact-checking rule
Check facts independently, against current guidelines (AHA 2025 resuscitation, ESC 2023–2025, SCAI 2022, SSC 2021) and standard texts. **Do not leave flags or questions for Naven.** Decide each issue yourself: state the correct fact and source. If the viva version is right and P12 or the card is wrong, say so (that is a fix, record it). If the viva version is wrong, it can still be offered only when the error is minor and you give a one-line correction; otherwise don't offer it.

## Decide per pair
- `offer` — the viva id to offer beside the P12 lesson, or `null`. Offer when value ≥ 2, it stands alone (or does after dropping its first line), and any error is minor and corrected. At most one per pair: the one that adds most.
- `drop_first_line` — true if the offered version needs its opening callback line removed to stand alone.
- `listen_for` — one plain sentence telling him what to listen for in the viva version (what it adds). No mnemonics or memory tricks.

## Output
One JSON file per batch, saved to Drive › Trace as `P12_Viva_Rate_out<batch>.json`:

```json
{"batch": 1, "rater": "<model name>", "pairs": [
  {"pair": "R001", "p12": "P12-101|s1",
   "viva": [{"id": "P1-060|s2", "value": 2, "standalone": true, "adds": "…", "conflicts": null}],
   "offer": "P1-060|s2", "drop_first_line": false,
   "listen_for": "…",
   "fixes": [{"in": "P12-101|s1 | card | P1-060|s2", "wrong": "…", "right": "…", "source": "…"}]}
]}
```

Every pair in the batch must appear, in order. When finished, reply with: pairs done, how many offers (by value 2 / 3), how many fixes (in P12 / card / viva), and anything that blocked you.
