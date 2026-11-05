# Brief: Explain v2 ("Learn" depth) for one Toxicology deck in Trace

You are writing the explanation layer for every card in ONE deck of Naven's flashcard app Trace (NEET-SS DM Critical Care, exam 11–12 Dec 2026). The readers are two ICU residents (Naven and his study partner HT). HT is "old school": she wants the reasoning built up step by step, and the punchline LAST. Accuracy matters more than anything: this is exam material and a wrong fact is worse than none.

## Read first (in full)
1. `/home/claude/map/explain/tox01_learn.py` — the finished, fact-checked TOX01 deck. It is the STYLE and FORMAT reference. Match its voice, depth and length exactly.
2. `/home/claude/map/cards/<DECK>.jsonl` — your deck's cards (fields: code, section, q = question with lettered parts, a = answer with the same letters, watch = WATCH note). Card text is final and is NOT changed by you.
3. `/home/claude/trace/test/data/qbank.json` → `cards["<DECK>|<code>"]`: per-card bank info. `lines` = extra exam lines asked in the question banks, `cross` = crossfire lines, `fix` = checked corrections to the card. Use these: what was asked tells you what to explain well; a `fix` is a verified correction you must respect.

## What to write
File: `/home/claude/map/explain/<deck lowercase>_learn.py` defining `L = {}` and one `L['<code>'] = dict(...)` per card, same fields as TOX01:
- `sub`: "Toxicology → <section> → <subtopic>"
- `intro`: "What's going on" — 2–4 plain sentences of physiology/clinical scene, BEFORE any answer.
- `parts`: list of (letter, text) mirroring the card's answer letters exactly, in order. Each text starts with the card's answer restated in **bold** (short, faithful), then 1–4 sentences of WHY: mechanism, step by step. For table cards without letters, use a, b, c… one per row/topic in order (see TOX-03, TOX-13 in TOX01).
- `table` (optional): dict(title, head, rows) — only when a comparison, decision or sequence is clearer as a table.
- `mimic`: [(pair, the one discriminating feature)] — close look-alikes.
- `traps`: [(“the wrong belief examiners use”, correction with its why)] — 2–4.
- `decode`: [(how an exam stem is worded, what it points to)] — 2–4.
- `punch`: the punchline, one or two sentences, comes last, ties the reasoning together.
- `extra` (optional): [dict(q, a)] one or two high-yield add-ons beyond the card (e.g. from qbank `lines`).
Also define `FLAGS = {}`: `FLAGS['<code>'] = "..."` wherever the card text looks wrong, outdated (vs current guidelines) or disagrees with a qbank `fix`. Never contradict the card silently inside the explanation; explain what is right and put the disagreement in FLAGS.

## Rules
- NO mnemonics, memory hooks, acronym tricks or "think of it as" devices. Plain clinical English, British spelling, curly quotes as in TOX01.
- Don't write superficially: every part must explain the mechanism or the reason, not just repeat the answer. But don't pad; TOX01 length is the target (~120–250 words per card plus the lists).
- Numbers, doses, cut-offs: only ones you are sure of, consistent with standard references (Goldfrank's, Tintinalli, UpToDate-level, current guidelines e.g. EXTRIP, Rumack–Matthew/UK 100-line for paracetamol, WHO/Indian snakebite protocol 2017 for ASV). When the card's number differs from a reference, follow the card in the bold restatement and FLAG it.
- Indian context matters (snakes: Big Four, Indian ASV dosing; pesticides: OP, aluminium phosphide, paraquat).
- Cross-refer other cards by their codes (e.g. "(APAP-05)") where useful, as TOX01 does.
- Python must be valid; use the same quoting as TOX01 (double-quoted strings, ’ for apostrophes inside).

## Check before you finish
Run `python3 /home/claude/map/explain/check_learn.py <DECK>` until it prints OK. Then re-read every entry once against its card for accuracy.
Final reply: the file path, the card count, the FLAGS list (one line each), and anything you were unsure of. Do not edit any other file.
