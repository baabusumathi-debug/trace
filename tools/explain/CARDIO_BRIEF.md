# Cardiology addendum to BRIEF_v3.md (19 Nov 2026)

Read `/home/claude/map/explain/BRIEF_v3.md` first. Everything there applies; this adds the cardiology specifics.

## Inputs for your deck
- **Cards (final text):** `/home/claude/map/cards/<DECK>.jsonl`. This already includes the approved corrections (cardfix) and the table layout fixes. Card text is final: never change it; disagreements go in FLAGS.
- **Real questions:** `/home/claude/map/explain/qpack/<DECK>.md`, from these sources:
  - DocT QBank (cohort %)
  - 20 DocT Grand Tests
  - Marrow QBank
  - NEET 2025 recall (DocT's version)
  - NEET 2024 recall
- **The card layer:** `/home/claude/map/explain/cvs_cardlayer.json` under the key `"<DECK>|<code>"`.
  - `lines` are the bank Top-up lines, exam-key and Crossfire lines already shown under the card in the app. Your explanation must agree with them and cover what they add.
  - If a line says a bank key is wrong or disputed, your trap must say the same; if you think the line itself is wrong, FLAG it.
  - `chips` show which banks hit the card.
- **Bank Top-up cards:** `/home/claude/map/explain/cvs_topups.json` under `"<DECK>"`, each with `id, topic, q, a[], src`.
  - If your deck has any, also write `/home/claude/map/explain/<deck>_topups_learn.py` with `T = {id: dict(...)}`: the same fields and voice as the main cards, a `step` into your deck's SPINE, parts lettered a, b, c… in the order of the `a` list.
  - Style reference: `/home/claude/map/explain/resp03_topups_learn.py`.
- **Style and format references** (the newest, best ones): `obs02a_learn.py`, `resp03_learn.py` and `special05b_learn.py` in the same folder. Match their voice, depth, header comment (sources checked, with dates) and the SPINE / PRIMER / FLAGS layout.

## Current guidelines to write from (check the exact figures online; don't rely on memory)
- **Resuscitation:**
  - AHA 2025 Guidelines for CPR & ECC (Circulation, Oct 2025): BLS, ALS, post-arrest care, special circumstances, neonatal and paediatric
  - ERC 2025
  - ERC–ESICM post-resuscitation care 2025 (and 2021 where 2025 is silent)
- **ACS:** ESC 2023 ACS guideline; AHA/ACC 2025 ACS guideline; Fourth Universal Definition of MI (2018).
- **Aortic dissection:** ESC 2024 peripheral arterial and aortic diseases; ACC/AHA 2022 aortic disease.
- **Pericardium and myocardium:** ESC 2025 myocarditis and pericarditis guideline; ESC 2015 pericardial (where still quoted); AHA 2020 fulminant myocarditis statement.
- **RV failure, PH, PE:** ESC/ERS 2022 pulmonary hypertension; ESC 2019 acute PE (check for any 2025 update); the ATS/ESC/AHA statements on acute RV failure.
- **Cardiogenic shock:** SCAI SHOCK stages (2022 update); ESC 2021/2023 heart failure; trials:
  - IABP-SHOCK II
  - CULPRIT-SHOCK
  - ECLS-SHOCK (2023)
  - DanGer Shock (2024)
  - DOREMI
  - SHOCK
- **Echo:** ASE/EACVI chamber quantification 2015; ASE 2019 and later guidelines as relevant.

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
