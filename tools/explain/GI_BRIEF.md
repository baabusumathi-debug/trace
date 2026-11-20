# GI addendum to BRIEF_v3.md (20 Nov 2026)

Read `/home/claude/map/explain/BRIEF_v3.md` first. Everything there applies; this adds the GI specifics.

## Inputs for your deck
- **Cards (final text):** `/home/claude/map/cards/<DECK>.jsonl`. This already includes the approved corrections (cardfix) and the table layout fixes. Card text is final: never change it; disagreements go in FLAGS.
- **Real questions:** `/home/claude/map/explain/qpack/<DECK>.md`, from these sources:
  - DocT QBank (cohort %)
  - 20 DocT Grand Tests
  - Marrow QBank
  - NEET 2025 recall (DocT's version)
  - NEET 2024 recall
- **The card layer:** `/home/claude/map/explain/gi_cardlayer.json` under the key `"<DECK>|<code>"`.
  - `lines` are the bank Top-up lines, exam-key and Crossfire lines already shown under the card in the app. Your explanation must agree with them and cover what they add.
  - If a line says a bank key is wrong or disputed, your trap must say the same; if you think the line itself is wrong, FLAG it.
  - `chips` show which banks hit the card.
- **Bank Top-up cards:** `/home/claude/map/explain/gi_topups.json` under `"<DECK>"`, each with `id, topic, q, a[], src`.
  - If your deck has any, also write `/home/claude/map/explain/<deck>_topups_learn.py` with `T = {id: dict(...)}`: the same fields and voice as the main cards, a `step` into your deck's SPINE, parts lettered a, b, c… in the order of the `a` list.
  - Style reference: `/home/claude/map/explain/resp03_topups_learn.py`.
- **Style and format references** (the newest, best ones): `obs02a_learn.py`, `resp03_learn.py` and `special05b_learn.py` in the same folder. Match their voice, depth, header comment (sources checked, with dates) and the SPINE / PRIMER / FLAGS layout.

## Current guidelines to write from (check the exact figures online; don't rely on memory)
- **Acute liver failure (GI01A–C):** EASL 2017 ALF guideline; AASLD position paper 2011 and any ACG ALF guideline (check for 2025/2026); King’s College, Clichy, MELD criteria; ALFSG data; Indian data (ALF in India, ATT-DILI, ACLF/ALF INASL consensus) where the card quotes them; trials on high-volume plasma exchange (Larsen 2016), MARS (FULMAR), hypertonic saline.
- **Acute pancreatitis (GI02A–B):** Revised Atlanta 2012; IAP/APA 2013; ACG 2024 acute pancreatitis guideline; AGA 2018; WSES 2019; trials: WATERFALL (fluids), PYTHON, POINTER, TENSION/step-up (PANTER), APEC (ERCP).
- **Gut in critical illness (GI03):** ESICM 2012 AGI grading and later ESICM statements (GIDS); ESPEN 2023 ICU nutrition; ASPEN/SCCM 2016/2022.
- **Mesenteric ischaemia (GI04):** ESVS 2017 and 2025 mesenteric guideline; WSES 2022 acute mesenteric ischaemia; ACG 2015 colon ischaemia.
- **Intra-abdominal hypertension (GI05):** WSACS 2013 consensus definitions and guidelines (and any later update).
- **ACLF (GI06):** EASL 2023 ACLF clinical practice guideline; EASL-CLIF (CANONIC, CLIF-C OF / ACLF scores); APASL AARC 2019 (and 2023 update if any); NACSELD; CHANCE study.
- **Cirrhosis (GI07A–B, HY6):** Baveno VII (2022); EASL 2018 decompensated cirrhosis; AASLD 2021 ascites/SBP/HRS guidance; ICA–ADQI 2024 HRS-AKI consensus; AASLD/EASL 2014 HE guideline (and EASL 2022 HE); AASLD 2023 TIPS/variceal practice guidance; terlipressin (CONFIRM, FDA label 2022); albumin trials (ANSWER, ATTIRE, PRECIOSA).
- **Nutrition and other HY6 topics:** ESPEN 2023, ASPEN/SCCM 2022, EFFORT Protein, TARGET, NUTRIREA-3.

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
