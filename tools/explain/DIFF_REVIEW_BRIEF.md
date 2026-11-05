# Brief: independent fact-check of the audit edits

An auditor edited the Toxicology explanations so they answer the real exam questions (see AUDIT_BRIEF.md). Its additions have not been checked by anyone else. You are that check. A wrong fact is worse than none.

- Before: `/home/claude/map/explain/pre_audit/<deck>_learn.py` (already fact-checked earlier). After: `/home/claude/map/explain/<deck>_learn.py`. Use `diff` (or Python) to see what changed per card. TOX01 also has `tox01_topups_learn.py` (pre_audit copy alongside).
- The questions: `/home/claude/map/explain/qpack/<DECK>.md`. The audit log: `<deck>_audit.md`.

For every ADDED or CHANGED statement:
1. Is it true by standard references and current guidelines? Use WebSearch for any number, dose, cut-off, trial or claim about a key being wrong that you are not certain of.
2. Where the edit says a DocT/Marrow key is wrong or disputed: is that right? Check against the question and the literature.
3. Did a cut remove something a linked question needs? Restore it briefly if so.
Fix errors directly in the after file (keep the format; no mnemonics; curly ’). Run `python3 /home/claude/map/explain/check_learn.py <DECK>` until OK.
Write `/home/claude/map/explain/<deck>_audit_review.md` (one line per fix with source). Final reply: per deck number of fixes (factual vs minor) and the most important ones. Edit only those files.
