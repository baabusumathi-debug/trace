# GT cards — independent fact-check (you decide; nobody will review your flags)

You check one batch of GT cards written by another model for Naven (NEET-SS DM Critical Care, 11–12 Dec 2026). Naven is asleep and has said: do not leave flags for him — decide every issue yourself in the way that is best for his NEET exam, and fix the card.

Inputs: the writer brief `/home/claude/gt/BRIEF.md` (read it fully — the style and length rules are Naven's), the draft `/home/claude/gt/out/<BATCH>.json`, the papers `/home/claude/gt/papers.json`, his cards `/home/claude/map/cards/*.jsonl` (+ `/home/claude/trace/test/data/cardfix.json` overrides).

For every card:
1. **Key and facts.** Verify the key and every factual claim (numbers, doses, cut-offs, grades, guideline years, mechanisms) against current authoritative sources. **Use web search/fetch for anything not rock-solid** — the writer mostly did not. Prefer guidelines (SSC, AHA/ERC 2025, KDIGO, ESICM, ATS/IDSA, BTS, NICE, Endocrine Society, AABB, ACOG/RCOG), Goldfrank/Tintinalli for toxicology, and standard ICU texts.
   - Wrong fact → correct it in the card.
   - DocT's key wrong or outdated by current evidence → set `key.status` to `disputed`/`outdated`, teach the current answer, and name the old/bank answer plainly so he still recognises it ("Current: X. This bank and older keys: Y."). Exam advice: NEET-SS keys often follow standard textbooks; when a guideline changed recently (2025–2026), teach current and name the textbook answer as the likely key.
   - A claim you cannot verify → rewrite it to what you can verify, or remove it. Never leave "unverified" text in a card.
2. **Picks.** `picks_note` must match `people.Trace.picks` / `people.HT.picks` in papers.json for that question (Trace = Naven = "you"; HT = "HT").
3. **Links.** Each `links` entry must exist in the card files and genuinely teach the topic; drop weak ones. `depth` must match (short only if a linked card really carries the teaching).
4. **Style and length (Naven's rules).** Normal good prose; the payoff appears once; nothing assumed that he needs right now; a new topic is taught properly (physiology first, then the few neighbouring facts NEET could ask next) but not a chapter; no mnemonics/stories. Tighten bloated cards; expand thin "new topic" cards.
5. **Card errors in his decks.** If a native card he owns is wrong or outdated on the tested point, add an entry to `/home/claude/gt/review/<BATCH>_cardfix.json`: `{"DECK|CODE": {"field": "a|why|watch", "old": "<exact current text of that field>", "new": "<corrected full field text>", "why": "<one line + source>"}}`. Keep his formatting conventions (`**bold**`, `- ` bullets, `**a** ` parts). Only for real errors, not style.

Write the corrected batch to `/home/claude/gt/out/final/<BATCH>.json` (same schema, all cards, valid JSON) and a short log `/home/claude/gt/review/<BATCH>.md`: per card, what you changed and the source URL for each corrected fact. Final message: number of cards, number changed, keys you set disputed/outdated, and any cardfix entries.
