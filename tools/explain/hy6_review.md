# HY6 — independent review of hy6_learn.py and hy6_topups_learn.py (20 Nov 2026)

Checked all 14 cards and 3 top-ups against cards/HY6.jsonl, qpack/HY6.md, gi_cardlayer.json and gi_topups.json["HY6"]. Bold restatements match the card answers and the letters line up (GIN-04 table → a–d; GIN-09 steps 1–6 → a–f). check_learn.py HY6: OK (14/14, spine 6).

## Claims the writer could not verify, now settled
- WATERFALL: confirmed (20 mL/kg + 3 mL/kg/h vs 10 mL/kg only if hypovolaemic + 1.5 mL/kg/h; overload 20.5% vs 6.3%; moderately severe/severe 22.1% vs 17.3%, NS; stopped at first interim, n 248). Source: ACP Gastroenterology Monthly summary of NEJM 2022.
- Villanueva 2013: confirmed (n 889; Hb <7, target 7–9, vs <9; 6-week survival 95% vs 91%, HR 0.55; rebleeding 10% vs 16%; benefit in Child A/B, not C). Source: ACP IM Matters summary.
- Lee 2009: confirmed (n 173; 3-week overall survival 70% vs 66% NS; TFS 40% vs 27%; coma I–II 52% vs 30%; III–IV 9% vs 22%). Source: abstract (QxMD).
- Squires 2013: confirmed (n 184; 1-year survival 73% vs 82% NS; 1-year TFS 35% vs 53%, p 0.03; under-2s ‘particularly, but not significantly’). Source: abstract (QxMD).
- Sort 1999: confirmed (renal impairment 33% → 10%, in-hospital death 29% → 10%, 3-month 41% → 22%). Source: WikiJournalClub.
- CONFIRM: confirmed (n 300; HRS reversal 32% vs 17%; respiratory deaths 11% vs 2%). Source: abstract (UMN Experts).
- EFFORT Protein: confirmed (≥2.2 vs ≤1.2 g/kg; discharge alive NS; worse with AKI, HR 0.5, and SOFA ≥9). Source: The Bottom Line.
- PRECISe: confirmed (2.0 vs 1.3 g/kg; worse EQ-5D-5L at 180 days, −0.05; more GI intolerance; mortality NS). Source: abstract (HvA repository).
- Larsen 2016: confirmed (n 182; TFS HR 0.56; hospital survival 58.7% vs 47.8%; no gain in patients transplanted). Source: abstract (QxMD).
- EASL ‘culture negative in up to 60%’: confirmed, but it comes from the EASL 2010 ascites guideline (‘despite the use of sensitive methods… as many as 60%’), not EASL 2018 as the writer had it. Source: EASL 2010 full text (unipd repository).
- Shock index ≥0.9 / lactate >2.5 in UGIB: still no guideline source found. ESGE 2021 uses shock index >1. Card wording kept and flag kept.
- Terlipressin regimen: guideline regimen confirmed as 2 mg 4-hourly for the first 48 h (until bleeding is controlled), then 1 mg 4-hourly for prevention of rebleeding, 2–5 days in all. Source: Clin Endosc 2019 review citing guidelines. The writer’s flag was right; I tightened it.
- Sigmoid volvulus ‘empty left iliac fossa’: not found in standard descriptions (GPnotebook: tympanic distension, LIF tenderness, empty capacious rectum). New flag added.
- Capsule endoscopy yield: 38–83%, best within 48–72 h (ACG 2015, via Medtronic-hosted guideline summary). Text made specific.
- OCEAN: this is Goltstein, Gastroenterology 2024 (n 62; octreotide LAR 40 mg 4-weekly; mean 11.0 vs 21.2 units transfused; good response 61% vs 19%), not 2023. Source: gi.org EBGI summary. Header fixed and the trial added to the explanation.
- Sung 2010: not re-searched. The text only says stopping aspirin after ulcer haemostasis raised mortality, and that is safe. Left unchanged.
- ASPEN 2022 (no supplemental PN before day 7, strong/high) and SCCM/ASHP 2024 (risk factors, either PPI or H2RA, either route, low dose, stop before ICU transfer out, neurocritical care, enterally fed patients) re-checked against the ASPEN factsheet and the sccm.org summary: the writer had them right.
- ACG–CAG 2022 (via AAFP summary): aspirin continued, platelet transfusion possibly harmful, vitamin K ineffective, PCC possibly beneficial, FFP worse. This agrees with the text.

## Changes made
Factual:
1. GIN-13a: ‘EASL notes cultures can be negative in up to 60%’ was credited to EASL 2018 → now credited to the EASL 2010 ascites guideline in its own words, with the reason lower figures exist (bedside inoculation into blood-culture bottles). Source: EASL 2010.
2. GIN-06e: ‘step-up halved major complications or death (PANTER)’ was an overstatement → now ‘69% to 40%’. Source: PANTER, NEJM 2010 (from memory; the figures are standard).
3. GIN-06a: ‘persistent organ failure mortality around 30%’ was too low → now ‘a third to a half of these patients die’. Source: Revised Atlanta 2012 (36–50%; from memory).
4. GIN-11d: ‘a non-viral cause predicts death’ was wrong (the King’s criterion is indeterminate/non-A non-B or drug-induced, which may well be viral) → now ‘an indeterminate or drug-induced cause’. Source: King’s College criteria.
5. Top-ups header: ‘OCEAN trial 2023’ → Goltstein, Gastroenterology 2024. Source: gi.org EBGI.

Minor (depth or precision):
6. GIN-08e: added why shock index works and what lactate means; says plainly that 0.9 and 2.5 are not guideline cut-offs and ESGE uses >1.
7. GIN-07c: added the real presenting signs of sigmoid volvulus and why it happens (redundant loop on a narrow mesentery; empty rectum; coffee-bean loop).
8. GIN-12c: Larsen 2016 expanded: mechanism, n 182, HR 0.56, survival 59% vs 48%, no gain if transplanted.
9. GIN-13b: Sort 1999 now gives n 126, says the death figure is in-hospital, and adds 3-month mortality.
10. T_2659f047 b: replaced ‘finds a source in over half’ with the ACG yield of 38–83%, best within 48–72 h.
11. T_2659f047 f: added the OCEAN result.
12. Header of hy6_learn.py: added a ‘second check’ block listing the verified figures and their sources.

No mnemonics or banned phrases found. Traps are kept, and their correct side was checked. Punchlines come last and are under the length limit.

## Final FLAGS
hy6_learn.py
- GIN-03: a — ventilation alone ‘not a firm risk factor’ (SCCM/ASHP 2024) is now incomplete after REVISE (UGIB 1.0% vs 3.5%, mortality unchanged).
- GIN-04: card correct; the DocT keys for perforated-ulcer ACS (‘after failure of conservative measures’) are wrong, and the right answer is immediate laparotomy. The CGT4 pancreatitis key ‘immediate’ is still the best option offered.
- GIN-05: card correct; the DocT key ‘no further imaging’ holds only for making the diagnosis, because ultrasound for gallstones is still advised.
- GIN-07 (new): c — ‘empty left iliac fossa’ not found in standard descriptions of sigmoid volvulus. The answer is unaffected.
- GIN-08: c — the PCC + vitamin K line follows ESGE 2021, while ACG–CAG 2022 suggests against vitamin K and FFP. e — shock index ≥0.9 and lactate >2.5 are not guideline cut-offs (ESGE uses >1).
- GIN-09: 1 — the terlipressin step is duplicated; the regimen is 2 mg 4-hourly for 48 h, then 1 mg 4-hourly, 2–5 days in all. 5 — Baveno VII says HVPG >20 (trivial).
- GIN-13 (softened): a — ‘negative in 30–40%’ is at the low end of the range (EASL 2010: up to 60%). Not wrong for the exam. c — the GT2 explanation uses the 2015 ICA 48-h rule.

hy6_topups_learn.py
- T_9fa98033: not a card error. The DocT key ‘continue DAPT’ is right for most patients; a brief P2Y12 hold applies only in life-threatening bleeding.
