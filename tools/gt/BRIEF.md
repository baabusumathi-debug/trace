# GT cards — writer brief

You are writing **GT cards** for Naven's study app Trace. Naven is a final-year anaesthesia resident sitting **NEET-SS DM Critical Care on 11–12 Dec 2026** (MCQ, +4/−1). Each GT card is one question from a DocTutorials Grand Test (GT 7 or GT 8) that Naven and/or his study partner HT got wrong, guessed, or left blank. The card is how he reviews that question in Trace.

## Inputs
- `/home/claude/gt/papers.json`: both papers. `P["7"]` / `P["8"]` → `questions[n-1]` = `{n, id, stem, options[A..D], key, doct (DocT's own explanation), refs}`; `people.Trace` (Naven) and `people.HT`: `res` is a 150-char string (r right, w wrong, b blank) indexed by n-1; `guess` = list of n they marked as a guess; `picks` = {n: the wrong option they chose}.
- Your batch: a list of `(paper, n)` given in your prompt.
- Naven's existing cards: `/home/claude/map/cards/<DECK>.jsonl`, one card per line: `{deck, code, section, q, a, why, watch, hook}`. Corrected text for some cards: `/home/claude/trace/test/data/cardfix.json` → `cards["DECK|CODE"].fields` overrides those fields. Search these (grep -il on key terms, several synonyms) **before** writing every question.

## The two lengths (Naven's rule — the most important part)
1. **A good native card exists** (one of his cards already teaches the tested fact well): link it (and up to 2 related ones) in `links`. The GT card still makes complete sense on its own — it explains the answer, each option, and the trap — but it does **not** re-teach the background the linked card already covers. Start from where that card leaves off.
2. **The topic is new / no card covers it properly**: the `explain` must **teach the topic**, not just spit out the fact:
   - understanding first: what is happening in the body, why, and why the treatment works (physiology/pharmacology first);
   - then cover what NEET could plausibly ask **next time** from the same topic (the 3–6 neighbouring facts an examiner would pick: mechanism, defining features, the classic numbers/cut-offs, first-line management, the classic trap) — so a different question on the topic is answerable;
   - stop at what the exam could reasonably ask. Optimal balance: not a chapter, nothing said twice, but never so narrow that only this one question is answered.
   Even with a native card, link related cards whenever they exist so he can walk the whole arc.

## Style (Naven's words, follow exactly)
- **Read as normal, good prose.** Do not write every line as a punchline. The punchline/payoff appears **once**, in its proper place (usually `hook`, or the opening or closing line of `explain`), and it is concentrated.
- **Never assume he already knows the concept.** "You'll have studied this" is fine to say, but never leave out a step he needs right now to understand the card.
- Teach the why. Mechanism before numbers. Plain words; define a term the first time if it isn't standard ICU vocabulary.
- **No mnemonics, no stories, no invented acronyms.** No emoji. No colour-only meaning.
- British/Indian spelling is fine either way; drug names generic.
- Don't reproduce DocT's text; rewrite. Short quotes of a guideline phrase are fine only if essential.

## Check the key first
For every question, decide whether DocT's key is right **by current guidelines and standard texts** (search the web when unsure: Surviving Sepsis 2021/2026 updates, AHA/ERC 2025, KDIGO, ESICM, ATS, BTS, Tintinalli/Goldfrank for toxicology, Irwin & Rippe, Marino, Oh's, Vincent's, etc.).
- `key.status`: `"agree"`, `"disputed"` (a better answer exists by current evidence) or `"outdated"` (the key reflects an older guideline).
- If disputed/outdated, the card teaches the **current** answer, and says plainly what DocT keys and why, so he can still recognise the old key in the exam (NEET keys can lag guidelines — name both: "Current: X. Older keys and this bank: Y.").
- If a question is ambiguous or passage-only (the stem says "according to the passage/guidance" and the key only follows from that), set `key.status:"agree"` but say so in `key.note`, and keep the card short — don't build teaching on a flawed item.

## Picks
`picks_note`: one or two sentences on why the wrong option(s) that **Naven and/or HT actually picked** looked right, and what in the stem rules them out. Name whose pick it was ("Your pick, B …", "HT picked D …"). Leave empty if neither picked wrong (blank or guessed-right).

## Output — one JSON file per batch
Write `/home/claude/gt/out/<BATCH>.json`: an object keyed `"GT<paper>-<n>"`, e.g. `"GT8-100"`:
```json
{
  "sys": "Toxicology",
  "topic": "Strychnine",
  "links": ["TOX02|TOX-31"],
  "before": ["GT7-29"],
  "answer": "C. Benzodiazepine therapy.",
  "why": "2–4 sentences: why the key is right.",
  "watch": "1–3 sentences: the trap — why the tempting option is wrong.",
  "hook": "One line: the takeaway, said once, concentrated.",
  "explain": "Markdown. Sections start with a line '## Heading'. Paragraphs separated by a blank line. '- ' bullets allowed. **bold** allowed sparingly.",
  "options": {"A": "one or two lines on why A is right/wrong", "B": "...", "C": "...", "D": "..."},
  "picks_note": "...",
  "key": {"status": "agree", "note": ""},
  "depth": "full"
}
```
- `sys`: exactly one of: Basics of Critical Care Medicine · Mechanical Ventilation · Respiratory Disorders · Electrolyte and Acid Base Disorders · Shock · Cardiac Disorders · Infectious Diseases · Endocrine Disorders · Renal Disorders · Hematology · Gastrointestinal & Hepatological Disorders · Neurologic Disorders · Special Topics · ECMO · Toxicology · Miscellaneous Topics · Research - Biostats & Epi · Scoring Systems. (Obstetrics, trauma, burns, transplant/brain death, ethics → Special Topics; immunology/physiology basics → Basics of Critical Care Medicine.)
- `topic`: 1–4 words, the topic a student would file this under (e.g. "Strychnine", "Brain death testing", "MINOCA"). Use the same topic string for questions on the same topic.
- `links`: `"DECK|CODE"` exactly as in the card files, best first, at most 3; `[]` if none genuinely fits (don't force a weak link).
- `before`: for GT 8 questions, any GT 7 question (`"GT7-<n>"`) testing the **same concept** (search GT 7 stems in papers.json). For GT 7 questions, any GT 8 question likewise. `[]` if none.
- `depth`: `"short"` when a good native card carries the teaching, else `"full"`.
- `explain` for `full`: typically 180–450 words; `short`: 60–180 words. Use the length the topic needs.
- `options`: one entry per option letter present.

Validate your file with `python3 -c "import json;json.load(open(PATH))"` before finishing. Your final message: the batch name, how many cards, and any key you marked disputed/outdated with a one-line reason.
