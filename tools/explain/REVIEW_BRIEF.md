# Brief: independent fact-check of one deck's Explain v2 texts

Another writer produced `/home/claude/map/explain/<deck>_learn.py` (L = explanations per card, FLAGS = writer's doubts about card text). You are the second, independent check. Readers are ICU residents preparing for NEET-SS DM Critical Care; a wrong fact is worse than none.

Read: the deck's cards `/home/claude/map/cards/<DECK>.jsonl` (final, never edited), the explanation file, and `/home/claude/map/explain/tox01_learn.py` only as the style reference. Do not read the writer's notes beyond the file.

For EVERY card check:
1. **Accuracy** of every mechanism, number, dose, cut-off, timing, drug name, trial and guideline claim, against standard references (Goldfrank's, Tintinalli, current guidelines, EXTRIP, Indian snakebite protocol 2017, etc.). Use WebSearch when you are not certain; don't trust memory for exact figures or trials.
2. **Fidelity**: the bold restatement at the start of each part must match the card's answer for that letter; letters must line up.
3. **Depth**: each part explains the why (mechanism), not just a repeat of the answer. Fix anything superficial or vague.
4. **Rules**: no mnemonics or memory hooks; punchline last; traps state the wrong belief and correct it; plain British English.
5. **FLAGS**: are they right? Add flags where the card itself is wrong or outdated; remove flags that are wrong.

Fix problems directly in the file (keep the format). Invented or unverifiable specifics (e.g. a trial statistic you cannot find) are removed or softened, not kept. Run `python3 /home/claude/map/explain/check_learn.py <DECK>` until OK.

Write `/home/claude/map/explain/<deck>_review.md`: one line per change (card code: what was wrong → what it says now, with the source), then the final FLAGS list. Final reply: number of errors fixed (factual vs minor), the most important ones, and the FLAGS. Edit no other file.
