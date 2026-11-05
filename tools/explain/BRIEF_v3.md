# Brief v3: Explain ("Learn" depth) for one deck — driven by the real exam questions, with a story arc

You write the explanation layer for every card of ONE deck in Naven's flashcard app Trace (NEET-SS DM Critical Care, exam 11–12 Dec 2026). Readers: two ICU residents (Naven, and HT who wants the reasoning built up step by step, punchline LAST). Accuracy first: a wrong fact is worse than none.

## The rule above all (Naven, 5 Nov)
Every line must change how he answers a question. Start from the REAL questions, not from the card:
`/home/claude/map/explain/qpack/<DECK>.md` lists, per card, every real question linked to it (DocT QBank with the % of the cohort who got it right, DocT Grand Tests, Marrow QBank, NEET 2024/2025 recalls), with options, keys and notes.
- **decode** ("How it is asked") comes from those questions. Each item: (the stem pattern as examiners word it, tagged with its source in brackets e.g. “[DocT GT]”, “[NEET 2024]”, “[Marrow]”; what decides the answer). Use 2–4 per card. A card with no real question: 1–2 items labelled “[pattern]”, i.e. how it would plausibly be asked.
- **traps** come from the distractors people actually chose. A low cohort % (e.g. 37%) marks a live wrong belief: name it, say why it is wrong. If a key itself is wrong or disputed (the notes say so), say so plainly in the trap.
- Depth follows the questions: a card asked 4–6 times gets the full treatment (why, mechanism, numbers); a card never asked gets a short, clean explanation (about half the length).
- Cut anything that would not help answer one of those questions or a close variant, however true or interesting. No history for its own sake unless it is asked.
- **extra** (optional): only a point a real question tested that the card does not cover.

## The story arc (so any card makes sense on its own, even when walked out of order)
- `SPINE = [(title, takeaway), …]` — 4–6 steps that tell the deck’s story in order of reasoning (cause → mechanism → what you see → how it is defined/graded → what it is confused with …). Titles ≤ 6 words; each takeaway one sentence a resident could say aloud.
- `PRIMER = "…"` — 3–4 sentences: only the background a person arriving cold needs before the first card of this deck (e.g. compliance, P/F ratio). Not a summary of the deck.
- Every card has `step = n` (1-based index into SPINE). The app shows “Step n of N: <title>” above the explanation and, when cards were skipped, the skipped steps’ takeaways as a bridge.
- `intro` (“What’s going on”) should place the card in the story: one sentence linking it to the step, then the scene.

## Read first
1. `/home/claude/map/explain/tox01_learn.py` — STYLE and FORMAT reference (voice, part structure, quoting). Your file adds SPINE, PRIMER and `step`.
2. `/home/claude/map/cards/<DECK>.jsonl` — the cards (code, section, q with lettered parts, a with the same letters, watch). Card text is final; never change it.
3. `/home/claude/map/explain/qpack/<DECK>.md` — the real questions.
4. `/home/claude/trace/test/data/qbank.json` → `cards["<DECK>|<code>"]` for `fix` (verified corrections) if present.

## Fields per card (as TOX01, plus step)
`sub`, `step`, `intro`, `parts` [(letter, "**bold faithful restatement of the card’s answer** + the why")], optional `table`, `mimic` [(pair, discriminating feature)], `traps`, `decode`, `punch` (one or two sentences, last), optional `extra` [dict(q, a)].
Also `FLAGS = {code: "..."}` where the card text is wrong/outdated or disagrees with a key or a `fix`. Never contradict the card silently; explain what is right and FLAG it.

## Rules
- No mnemonics, memory hooks or “think of it as” devices. Plain clinical English, British spelling, curly apostrophes (’) as in TOX01.
- Numbers, doses, cut-offs only if you are sure (standard references, current guidelines: Berlin 2012, the 2023 global definition, ATS/ESICM/ESICM-SCCM guidance, landmark trials). If the card differs, restate the card in bold and FLAG.
- Cross-refer other cards by code where useful.

## Check
Run `python3 /home/claude/map/explain/check_learn.py <DECK>` until it prints OK (both lines). Re-read every entry against its card and its questions.
Final reply: file path, card count, the SPINE titles, FLAGS (one line each), what you were unsure of. Edit no other file.
