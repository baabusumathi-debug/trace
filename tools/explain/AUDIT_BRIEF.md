# Brief: audit an existing deck's explanations against the real exam questions

Naven's rule (5 Nov): every line of an explanation must change how he answers a question. The Toxicology explanations were written from the cards and bank summary lines, not from the real stems. Audit them now.

Inputs per deck:
- explanations: `/home/claude/map/explain/<deck>_learn.py` (L dict; FLAGS). For TOX01 also `tox01_topups_learn.py` (T dict, Top-up cards).
- real questions per card: `/home/claude/map/explain/qpack/<DECK>.md` (DocT QBank with cohort % right, DocT GT, Marrow, NEET 2024/2025 recalls; options, keys, notes).
- cards: `/home/claude/map/cards/<DECK>.jsonl` (never edit).
- style reference: the file itself; rules: no mnemonics/hooks, British spelling, curly ’, punchline last.

For every card:
1. **Coverage.** For each real question linked to the card: could a reader of the explanation answer it, including the discriminating detail the distractors test? If not, add the missing point in the most natural place (a part’s why, a trap, or `extra`). Keep it short.
2. **decode = how it is really asked.** Rewrite `decode` items from the real stems, each tagged with its source in brackets (“[DocT]”, “[DocT GT]”, “[Marrow]”, “[NEET 2024]”, “[NEET 2025]”); 2–4 items. A card with no linked question keeps 1–2 items tagged “[pattern]”.
3. **traps from real distractors.** Where a question’s cohort % is low (< 60%), the wrong belief behind it must be a trap. If a key is wrong or disputed (the notes say so), state it in the trap.
4. **Cut what does not serve answering.** Remove or shorten sentences, mimics, extras and tables that no real question (or a close variant) would need: history for its own sake, tangents, repeated points. Keep each part’s core mechanism (the why behind the answer) — that is what makes variants answerable. Cards with zero linked questions: tighten to the essentials.
5. Do not introduce new facts you are unsure of; numbers only from standard references. Keep FLAGS (add if a question reveals a card error).

After editing run `python3 /home/claude/map/explain/check_learn.py <DECK>` until OK (for TOX01 the topups file is checked by loading it: `python3 -c "exec(open('tox01_topups_learn.py').read())"`).
Write `/home/claude/map/explain/<deck>_audit.md`: per card one line — questions linked (n), what you added (with the question it serves), what you cut. End with totals. Final reply: totals (added / cut / decode rewritten), the 5 most important additions. Edit only your deck files and the audit file.
