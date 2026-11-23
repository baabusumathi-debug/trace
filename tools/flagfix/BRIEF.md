# Card flags: decide and correct (Naven delegated the decisions, 23 Nov)

Naven (NEET-SS DM Critical Care, exam 11–12 Dec 2026, MCQ) cannot judge these flags himself and asked Claude to decide what is best for the NEET exam. You decide each flag and write the corrections.

## Inputs
- Flag lists: `/home/claude/flagfix/Cardio_Card_Flags_19Nov.md`, `Endo_Card_Flags_22Nov.md`, `P12_Card_Flags_23Nov.md` (some flags repeat across files; decide once).
- Cards as they are now: `/home/claude/map/cards/<DECK>.jsonl` (originals) with corrections from `/home/claude/trace/test/data/cardfix.json` applied on top (`cards["DECK|CODE"].fields` replaces whole fields). Always start from the corrected version if one exists.
- For context, the reviews in `/home/claude/p12/*_review.md`, `/home/claude/map/explain/*_review.md` and `/home/claude/trace/tools/explain/*_review.md` explain most flags and cite sources.

## Decide each flag (rules)
1. **Fix** when the card states something wrong, outdated against a current guideline that NEET-SS 2026 is likely to use, internally contradictory, or missing the fact a bank question actually tests. NEET-SS sets from standard guidelines and textbooks; when a guideline changed recently (2022–2026), put the current answer on the card and add a short line "Older keys: …" so he still recognises the old answer in an older-style question.
2. **Leave** (no card change) when the flag is only about a question-bank key (DocT/Marrow/GT key disputed, a mis-keyed GT question, the explanation's wording), about phrasing, or about something the lesson/explanation already handles and the card is not wrong. Also leave anything you cannot verify confidently.
3. Keep edits minimal and in the card's own style (bold, `- ` bullets, `a/b/c` parts, ` | ` tables, line breaks). Do not rewrite cards wholesale; change only the wrong lines, add at most one or two lines. No mnemonics.
4. Verify doubtful facts on the web; prefer WebFetch of guideline pages and PubMed abstracts (shared search budget is limited).

## Output
- `/home/claude/flagfix/cardfix_new.json`: `{"DECK|CODE": {"fields": {"a": "<whole new field text>"}, "src": "<source and date, one line>"}}` — only for cards you change. Field may be `a`, `q` or `watch`, whole-field replacement as in cardfix.json. If a card already has a cardfix entry, start from that text and include all its fields you keep.
- `/home/claude/flagfix/decisions.md`: one line per flag: card, FIX or LEAVE, the reason in under 20 words, source.
- Report in under 250 words: how many fixed and left, the most important fixes, anything unverified.
- Do not edit any other file.
