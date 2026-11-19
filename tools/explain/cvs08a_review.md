# CVS08A review (independent fact-check, 19 Nov 2026)

Sources checked online today: AHA 2025 Part 9 Adult ALS, Part 7 Adult BLS, Part 6 Paediatric BLS, Part 10 Special Circumstances (cpr.heart.org); 2025 circular adult arrest algorithm (250620); AHA chain-of-survival page and the 2025 neonatal newsroom infographic; ILCOR CoSTR ALS 2046 (IO vs IV); PMC meta-analysis of IO vs IV RCTs (PMC12195015); Retraction Watch 29 Dec 2025.

## Points I was asked to settle
- **ET drug route:** AHA 2025 Part 9 says it "has also been removed from the guidelines" (low, unpredictable levels). The writer's text and FLAG are right.
- **ETCO₂ for ROSC:** 2025 says an abrupt rise may be used to detect ROSC (2b), and that "a sudden increase greater than 10 mmHg may indicate ROSC". The 2025 circular algorithm has no ≥40 mmHg figure. The writer's text and FLAG are right.
- **TOR rules:** BLS rule 1 (B-NR), ALS rule 2a, Universal rule 2a. The Universal rule "uses the same criteria as the BLS rule": not witnessed by EMS, no shock, no ROSC. The ALS rule adds two criteria: not witnessed by a bystander and no bystander CPR. The rules are not valid for overdose, trauma or IHCA. The writer's text and FLAG (the card's watch line is backwards) are right.
- **Polymorphic VT:** "Immediate unsynchronized shock is recommended for adults with sustained polymorphic VT" (1, B-NR), and "all forms of polymorphic VT are considered hemodynamically and electrically unstable". Magnesium is 2b, for recurrences with a long QT, and 3: No Benefit with a normal QT. The writer's handling of the disputed CGT4 key is right.
- **Infant choking:** 5 back blows alternating with 5 chest thrusts (1, C-LD), using the heel of one hand. "Abdominal thrusts are not recommended in infants", and that was already the case in 2020. Children now start with back blows. The writer's FLAG on ACLS-07 is right.
- **IO vs IV RCTs:** the three trials are PARAMEDIC-3 (UK 2024), IVIO (Denmark 2024) and Ko et al. (Taiwan, BMJ 2024). The BMJ retracted Ko et al. on 18 Dec 2025. ILCOR's update pools the remaining two and gets the same result: sustained ROSC OR 0.89 (0.80–0.99), and no difference in survival or neurological outcome.

## Changes
- ACLS-19 c: "trials such as PARAMEDIC-3 and the Danish IVIO trial" → now names all three trials, says the Taiwanese trial was retracted in Dec 2025, and says the two-trial ILCOR update gives the same conclusion (OR 0.89, 0.80–0.99) (ILCOR CoSTR ALS 2046; Retraction Watch). **Factual.**
- ACLS-18 c: "cardioversion starting at about 200 J in AF" → "at least 200 J in AF (2a), 200 J in flutter (2b)" (AHA 2025 Part 9 §18.1). **Factual (minor).**
- ACLS-06 e: "compressions raise intrathoracic pressure far more than thrusts in a conscious patient" → "chest compressions generate airway pressures at least as high as abdominal thrusts" (the old wording overstated the evidence and the comparison was muddled). **Factual (minor).**
- ACLS-12 trap: "both prolong the QT … magnesium is also relevant in pre-eclampsia" → hypocalcaemia prolongs the QT, low magnesium triggers torsades, and magnesium sulphate toxicity in pre-eclampsia is a separate cause. **Factual (minor).**
- ACLS-03 e: removed "with more force if needed" in obesity, which is not in the guideline; it now says "same technique (AHA 2025 class 1)". **Minor.**
- ACLS-02 a: removed the invented "not by a sternal rub that wastes time" and replaced it with the reason a voice-and-tap check is used. **Minor.**
- ACLS-07 a: added that back blows first is new for children in 2025 (they used to get abdominal thrusts alone). ACLS-07 b: added that infant abdominal thrusts were not recommended in 2020 either, and the 2025 change is the heel of one hand. **Depth / fidelity to the FLAG.**
- ACLS-05 b, ACLS-06 c, ACLS-17 c: these parts only repeated the answer; each now has a one-line "why". **Depth.**
- Header: added the ILCOR, retraction, Part 9 energy and central-access checks. Moved the newborn chain's seven links from "not verified" to verified (AHA 2025 neonatal infographic).

Checked and left unchanged (correct): all BLS numbers and classes; the epinephrine timing in each limb (2a); amiodarone and lidocaine doses (2b); biphasic and monophasic energies; IV first (1, A), IO second (2a, A), central venous access 2b; the ETCO₂ targets of at least 10 and ideally ≥20 mmHg; the ETCO₂ TOR rules (2b intubated; 3: Harm non-intubated); hyperkalaemic arrest (calcium, bicarbonate and insulin–glucose each 2b; β₂-agonists 3: No Benefit); naloxone in opioid arrest; electrical injury (standard resuscitation, class 1); the six chain links; the thoracotomy windows.

Not verified: the "lungs" in the CPR icon (ACLS-01); whether AHA formally "retired" the term "rescue breaths" (ACLS-04 e; the 2025 text simply says "breaths"). The explanation does not depend on either.

Total: 4 factual fixes (1 major, 3 minor), 2 minor wording fixes, 4 depth additions; check_learn.py CVS08A OK.

## Final FLAGS
- **ACLS-13:** "PETCO₂ typically ≥40 mmHg" is the 2020 algorithm's wording. AHA 2025 says a sudden rise of more than 10 mmHg may indicate ROSC.
- **ACLS-16:** The card is correct. The cardlayer cross note (shock only for unstable polymorphic VT) is too strict: AHA 2025 recommends an immediate shock for sustained polymorphic VT and treats all polymorphic VT as unstable.
- **ACLS-19:** The watch line wrongly doubts that the ET route was removed; AHA 2025 removed it, so the Marrow ET-adrenaline line and key are outdated. Also part c: one of the "three large RCTs" (Ko et al.) was retracted in Dec 2025, though the conclusion is unchanged.
- **ACLS-20:** The watch line is backwards: the BLS rule has the same three criteria as the universal rule, and the ALS rule is the one that adds the two bystander criteria.
- **ACLS-07 (minor):** "abdominal thrusts are NO LONGER recommended" in infants suggests a change, but they were not recommended in 2020 either. What changed in 2025 is the heel of one hand.
