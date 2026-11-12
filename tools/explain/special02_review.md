# SPECIAL02 — independent review of special02_learn.py and special02_topups_learn.py (13 Nov 2026)

Checker: `python3 check_learn.py SPECIAL02` → `SPECIAL02 12 cards 12 entries OK`, `v3 spine 6 steps OK`.
Top-ups (no checker) checked by hand: every part starts with the bold restated card answer (verbatim), all mimic/trap/decode pairs have 2 items, punch 260 and 181 characters (limit 320), no banned phrases.

## Changes (card: what was wrong → what it says now; source)

### Factual
- EOL-06 trap (palliative involvement) and mimic: "with equal or better family satisfaction" stated as fact (copied from the DocT line) → reduces non-beneficial procedures, readmission and cost without raising mortality; effects on families mixed: palliative-care-led meetings did not reduce relatives' anxiety or depression and may have increased PTSD symptoms. Mimic now says "often shortens stay", SSC advice "suggests (conditional) against" routine consult. Source: Carson et al., JAMA 2016 (summary in Relias Media); SSC 2021 author commentary (empendium).
- EOL-04 mimic: continuous deep sedation "reserved for refractory suffering in the last days" (2009 EAPC wording) → considered when lighter sedation has failed, generally in the final stage of life; EAPC 2024 sets no fixed life expectancy; proportional sedation light/intermittent first. Source: Surges et al., Palliative Medicine 2024 (revised EAPC framework, statements 1, 22–26).
- EOL-08 d: "midazolam being the usual infusion" → midazolam first-line (EAPC 2024); added that opioids and haloperidol are not used as sedatives. Source: EAPC 2024 statements 27–28.
- EOL-07 b: "structured meetings … reduce later anxiety, depression and PTSD" given without a source → attributed to Lautrette, NEJM 2007 (22 French ICUs, 126 relatives; proactive conference with relatives speaking about half the time plus brochure; PTSD symptoms 45% vs 69%, anxiety 45% vs 67%, depression 29% vs 56% at 90 days). Source: PubMed 17267907.
- EOL-10 c: "The 2006 report dealt with withholding treatment" → names the 196th (2006, withholding/withdrawal from the terminally ill, not active euthanasia) and 210th (2008, IPC 309 "inhuman", recommended removal); added 241st (2012, passive euthanasia). Source: SC Observer "Right to die: court in review"; Legal Service India on Report 241 (2012) and 196th (forwarding letter 28 Aug 2006).
- EOL-10 trap and new `extra`: Harish Rana v Union of India (11 March 2026, J.B. Pardiwala and K.V. Viswanathan JJ, 2026 SCC OnLine SC 358) was missing → added: first withdrawal reported as approved under Common Cause; CANH is medical treatment; holistic best-interests test; withdrawal is not abandonment, DAMA misuse disapproved; district CMOs to keep panels for secondary boards; Parliament urged to legislate. Source: SCC Online blog (12 Mar 2026); The Week (11 Mar 2026).
- EOL-06 g and trap (DAMA): added that Harish Rana held CANH to be medical treatment the boards may withdraw, and disapproved misuse of discharge against advice. Same sources.
- EOL-03 mimic (substituted judgment vs best interests): added that Indian courts (Aruna Shanbaug, Harish Rana) apply a best-interests test to incapacitated patients without a directive, with known wishes as one factor. Same sources; Legal Vidhiya summary of Aruna Shanbaug.
- EOL-11 extra (MoHFW draft): "hospitals should have clinical ethics committees" → "may set up" (the text says "may constitute"); listed conditions now include "compliance with the Supreme Court procedure", with the wording "must apply" noted and that the first two are really alternatives; added that it was released for comment in late September 2024 and no final version was found. Source: MoHFW PDF "Guidelines for withdrawal of Life Support" (main.mohfw.gov.in); India Legal (Isra Black, 16 Nov 2024); ThePrint 1 Oct 2024.
- EOL-11 f: High Court route described only as "boards disagree" → the 2023 order gives it whenever a board refuses; Division Bench, may appoint three doctors of ≥20 years' standing, decides on best interests. Source: SCC Online explainer of the 24 Jan 2023 order.
- EOL-11 c: persons named in the directive "decide" → "give consent" (the order requires their consent; the boards certify). Same source.
- T_d32ab4c4 d and FLAG: FLAG said "SEP-59" is an unidentifiable SSC number → it is the cross-reference to card SEP-59 in deck SEP01E (goals of care and palliative care); flag removed, part d now says so and grades the SSC advice (goals of care early within 72 h, weak; against routine consult, conditional; palliative principles integrated). Source: cards/SEP01E.jsonl; SSC 2021 author commentary.

### Structural / minor
- T_d32ab4c4 decode: generic items written without the stems → rewritten from the real stems (CGT5 Q132: trach/PEG consideration is the trigger, vasopressors are not; Q131: deficient communication training). Source: map/doct_gt_distinct_all.jsonl.
- T_43e8d00d decode: rewritten from the real stem (CGT1 Q31, health minister, four options). Same source.
- T_d32ab4c4 a: "Uncertainty is the commonest excuse" (unverifiable ranking) → "a frequent reason given for waiting".
- EOL-11 intro: "almost never used" (unverifiable) → "hardly workable in an ICU".
- EOL-10 extra / trap: "the first withdrawal" softened to "reported as the first".
- FLAGS for EOL-10 and EOL-11 rewritten; EOL-06 flag added; header comments of both files updated to record what was re-checked.

### Checked and left unchanged
- P. Rathinam v Union of India: 26 April 1994, two judges (Hansaria, Sahai), struck down IPC 309 — confirmed (bnblegal). Gian Kaur v State of Punjab: 21 March 1996, five judges, Verma J; Rathinam held "not correct"; ss 306 and 309 upheld — confirmed (bnblegal; Wikipedia "Section 309 of the IPC").
- Aruna Shanbaug: 7 March 2011, Katju and Gyan Sudha Misra JJ; active euthanasia illegal; withdrawal via High Court (Article 226, bench of ≥2 judges, committee of three doctors); KEM staff held to be her next friend and wished her to live; vegetative since 27 Nov 1973; died 18 May 2015 of pneumonia — confirmed (Legal Vidhiya; Wikipedia).
- BNS in force 1 July 2024; no general offence of attempted suicide; s226 covers an attempt to compel or restrain a public servant — confirmed (Babushahi; Wikipedia). MHA 2017 s115 presumes severe stress unless proved otherwise and bars trial and punishment — confirmed (SCC Online; Wikipedia).
- 24 Jan 2023 order (2023 SCC OnLine SC 99; five judges, K.M. Joseph J; on ISCCM's application): two witnesses + notary/gazetted officer; PMB = treating physician + ≥2 experts ≥5 years, preferably 48 h; SMB formed by hospital = CMO nominee + ≥2 experts ≥5 years, none from PMB, preferably 48 h; JMFC informed, visit deleted; 2018 version HoD + 3 experts of 20 years, Collector's board chaired by CDMO — all confirmed (SCC Online explainer).
- MoHFW draft details: PMB members may be from the treating team; CMO nominee "may be from the same hospital"; TBI with no recovery after ≥72 h; JMFC form "only notification, approval is not required" — confirmed in the MoHFW PDF.
- Mani RK et al., IJCCM 2024;28(3):200–250 — confirmed (BVS/MEDLINE record). Myatra et al., IJCCM 2014;18(9):615–635 — confirmed. ICMR DNAR, IJMR 2020;151(4):303–310: DNAR does not mean withholding other treatment; form signed, timed and dated by patient/surrogate and physician; CPR default when in doubt — confirmed. ICMR 2018 definitions including palliative sedation "at the minimal dosages necessary" — confirmed (Medical Dialogues).
- Maltoni 2012 (JCO systematic review, 11 studies, 1,807 patients): sedation not associated with shorter survival — confirmed; the text's "has not been shown to shorten survival" matches.
- WHO ladder 1986, three steps (step 2 weak opioids), fourth interventional step a later adaptation — confirmed (StatPearls). Four conditions of double effect — confirmed (Stanford Encyclopedia).
- Glycopyrrolate (quaternary, no BBB crossing) vs hyoscine hydrobromide (crosses, sedation/delirium); stopping neuromuscular blockers before withdrawal so distress can be seen (rationale confirmed in American Nurse; consensus as I know it from Truog et al. 2008, not re-opened) — standard, left.
- SOLER (Egan), Beauchamp and Childress, macro- vs microallocation — standard teaching, left.

## Final FLAGS — special02_learn.py
- EOL-06: Card sound. Linked DocT explanation claims equal or better family satisfaction; SSC 2021 notes mixed family effects and Carson (JAMA 2016) found possible harm (more PTSD symptoms). Harish Rana (2026) supports the DAMA watch line.
- EOL-08: Watch line gives the WHO ladder as four steps; original (1986) has three, interventional step is a later adaptation. "Moderate pain: oxycodone, morphine, fentanyl" differs from WHO step 2 (weak opioids). Acceptable for ICU practice.
- EOL-10: Card labels the 2006 Law Commission report "Euthanasia" (196th dealt with withholding/withdrawal, not active euthanasia); 241st report (2012) missing. Watch line omits the 2024 ISCCM–IAPC update and the MoHFW draft (still a draft). "Upheld IPC 309" is history (MHA 2017 s115; BNS from 1 July 2024). Harish Rana (11 March 2026) not on the card.
- EOL-11: Correct for the 24 Jan 2023 order; "at least" two experts and "preferably" 48 h for both boards; High Court route whenever a board refuses. Omits notary/gazetted-officer attestation, the MoHFW draft, and Harish Rana's district CMO panels.
- No flags: EOL-01, 02, 03, 04, 05, 07, 09, 12.

## Final FLAGS — special02_topups_learn.py
- None. (Writer's flag on "SEP-59" removed: it is the cross-reference to card SEP-59 in the sepsis deck SEP01E.)
