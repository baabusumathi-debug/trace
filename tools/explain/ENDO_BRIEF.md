# Endocrine addendum to BRIEF_v3.md (22 Nov 2026)

Read `/home/claude/map/explain/BRIEF_v3.md` first. Everything there applies; this adds the endocrine specifics.

## Inputs for your deck
- **Cards (final text):** `/home/claude/map/cards/<DECK>.jsonl`. This already includes the approved corrections (cardfix) and the table layout fixes. Card text is final: never change it; disagreements go in FLAGS.
- **Real questions:** `/home/claude/map/explain/qpack/<DECK>.md`, from these sources:
  - DocT QBank (cohort %)
  - 20 DocT Grand Tests
  - Marrow QBank
  - NEET 2025 recall (DocT's version)
  - NEET 2024 recall
- **The card layer:** `/home/claude/map/explain/endo_cardlayer.json` under the key `"<DECK>|<code>"`.
  - `lines` are the bank Top-up lines, exam-key and Crossfire lines already shown under the card in the app. Your explanation must agree with them and cover what they add.
  - If a line says a bank key is wrong or disputed, your trap must say the same; if you think the line itself is wrong, FLAG it.
  - `chips` show which banks hit the card.
- **Bank Top-up cards:** `/home/claude/map/explain/endo_topups.json` under `"<DECK>"`, each with `id, topic, q, a[], src`.
  - If your deck has any, also write `/home/claude/map/explain/<deck>_topups_learn.py` with `T = {id: dict(...)}`: the same fields and voice as the main cards, a `step` into your deck's SPINE, parts lettered a, b, c… in the order of the `a` list.
  - Style reference: `/home/claude/map/explain/resp03_topups_learn.py`.
- **Style and format references** (the newest, best ones): `obs02a_learn.py`, `resp03_learn.py` and `special05b_learn.py` in the same folder. Match their voice, depth, header comment (sources checked, with dates) and the SPINE / PRIMER / FLAGS layout.

## Current guidelines to write from (check the exact figures online; don't rely on memory)
- **Thyroid storm and myxoedema coma (ENDO01A):** ATA 2016 hyperthyroidism guideline; Japan Thyroid Association 2016 thyroid storm guideline; Burch–Wartofsky and JTA criteria; ATA 2014 hypothyroidism (myxoedema coma); ETA 2018 if relevant.
- **Adrenal insufficiency, pituitary apoplexy, diabetes insipidus (ENDO01B):** Endocrine Society 2016 primary adrenal insufficiency; SCCM/ESICM 2017 and 2024 CIRCI/corticosteroid guidance; UK 2011 pituitary apoplexy guideline (and any update); Society for Endocrinology / Endocrine Society DI guidance and the 2022 renaming to arginine vasopressin deficiency/resistance; copeptin testing.
- **Glucose control (CCM01, ENDO02A):** ADA Standards of Care 2025/2026 (hospital chapter); SCCM 2024 glycaemic control guideline; NICE-SUGAR, Leuven trials, TGC-fast (2023), LUCID; stress hyperglycaemia ratio.
- **DKA and HHS (ENDO02B):** ADA/EASD/JBDS/AACE/DTS 2024 consensus on hyperglycaemic crises; JBDS 2023 DKA and 2022 HHS guidance; ISPAD 2022 for paediatric points; SCOPE-DKA, balanced crystalloid trials.
- **HY5 (haem, endocrine, obstetric emergencies):** the above plus BSH/ASH transfusion guidance (TRALI/TACO definitions 2019 ISBT), ESA 2023 bleeding guideline, CRASH-2/WOMAN, ACOG/RCOG/FIGO eclampsia and PPH guidance, NICE hypertension in pregnancy.

**Where a card states an older figure,** the bold restatement keeps the card's wording. The explanation then states the current guideline plainly ("AHA 2025 now says …"). Add a FLAG if the card is now wrong.

## Rules (from Naven; same as all earlier decks)
- **Every card gets an explanation, asked or not.** Depth follows the questions:
  - asked cards get the full treatment
  - never-asked cards get a short, clean explanation, about half the length, with 1–2 "[pattern]" decode items
- **No mnemonics or memory hooks.** Punchline last. Plain British English, curly apostrophes (’) inside the Python strings.
- **Traps come from the distractors people actually chose** (low cohort %). If a bank key is wrong or disputed, say so plainly and give the exam-day answer.
- **The reader is an ICU resident:** teach the why (mechanism), not a repeat of the card.

## Output and checks
- Write `/home/claude/map/explain/<deck>_learn.py` (`L`, `SPINE`, `PRIMER`, `FLAGS`, header comment with sources and dates), and the topups file if any.
- Run `python3 /home/claude/map/explain/check_learn.py <DECK>` until it prints no errors.
- **Final reply (short):**
  - card count
  - which cards had the most questions
  - FLAGS (card errors) in one line each
  - anything you could not verify
- Edit only your own files.
