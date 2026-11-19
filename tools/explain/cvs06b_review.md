# CVS06B review: second, independent check (19 Nov 2026)

24 cards checked against cards/CVS06B.jsonl and cvs_cardlayer.json; check_learn.py CVS06B OK (24/24, spine 6 steps). No Top-up cards.

## Changes
- RVF-25 b (factual): ESC/ERS 2022 BNP/NT-proBNP high-risk cut-offs given as BNP >300 / NT-proBNP >1400 ng/L (these are the 2015 figures) → now BNP >800 / NT-proBNP >1100 ng/L high risk, <50 / <300 low risk, with the 2015 values named as older. Source: ESC/ERS 2022 three-strata table, via the SEC (secardiologia.es) risk-stratification document; four-strata 50–199 / 200–800 and 300–649 / 650–1100 recorded in the header.
- RVF-25 a (factual, minor): CT PA:aorta "ratio >1" given as the guideline figure → now ESC/ERS 2022 quotes PA:aorta >0.9 and PA ≥30 mm (with RVOT wall ≥6 mm and septal deviation ≥140° or RV:LV ≥1) as highly predictive; ratio >1 kept as the figure most often quoted. Echo PA >25 mm confirmed (Table 10). Source: ESC/ERS 2022 full text, §5.1.7 and Table 10.
- RVF-28 c (factual): "after LVAD, CVP/PCWP >0.63 is the usual RV failure criterion" → before implantation, CVP/PCWP >0.63 predicts RV failure afterwards (Kormos 2010); PAPi <1.85 likewise worded as predicting post-LVAD RV failure (Kang 2016). PAPi <0.9 in inferior MI (Korabathina 2012) kept.
- RVF-31 d (factual, minor): "proximal RVOT up to 3.0 cm in PLAX" mixed two measurements → RVOT PLAX ≤3.0 cm, proximal RVOT (short axis) ≤3.5 cm, distal ≤2.7 cm (ASE 2015 Table). FLAG text corrected to match.
- RVF-44 b (factual, minor): flow "rated to about 4–4.6 L/min" → manufacturer rates >4 L/min, up to 14 days; added that the Impella RP Flex goes in via the internal jugular with its inlet in the RA. Inlet IVC / outlet PA confirmed. Source: Abiomed/J&J Impella RP product page. FLAG text corrected to match.
- RVF-44 e (unverifiable figure): "haemolysis in about 5–10% in the first day" removed → haemolysis described as the typical shear-stress complication, monitored by plasma free haemoglobin and managed by lower speed or repositioning.
- RVF-26 b (minor): V4R ST elevation "fades within 12–24 hours" → transient, gone within about 12 hours in roughly half of patients (standard teaching, Braat).
- Header comment: ESC/ERS 2022 anticoagulation line corrected (no general recommendation; may be harmful in SSc-PAH; "HIV-PAH not recommended" could not be confirmed and was removed); review sources and dates added; wrong BNP strata replaced.

## Settled as correct (no change)
- ASE 2015: TAPSE <17 mm, S′ <9.5 cm/s, FAC <35%, RIMP >0.43 pulsed / >0.54 tissue, 3D RVEF <45%, free-wall strain less negative than −20% (normal about −29%), basal >41 mm, mid >35 mm, length >83 mm.
- ASE 2010 (Rudski): TAPSE <16 mm, S′ <10 cm/s, RIMP >0.40 / >0.55, 3D RVEF <44%, 2D RVEF not recommended, IVA no cut-off. ASE 2005 (Lang) ranges match RVF-31.
- 60/60 sign (PA acceleration time <60 ms with TR gradient <60 mmHg); McConnell's original specificity about 94%, also seen in RV infarction (Casazza 2005).
- HFA/ESC 2016 doses and the >200 mL / 15–30 min volume challenge are as printed on the cards (full statement not opened; figures consistent with standard summaries). ESC 2021 HF diuretic dosing (20–40 mg IV naive; 1–2× oral dose) correct.
- Traps on disputed keys kept: RVF-36 IPAH anticoagulation (ESC/ERS 2022: no general recommendation, individualise) and RVF-30 McConnell vs 60/60; truth side confirmed.

## Final FLAGS (unchanged in substance)
- RVF-25: "regional oligaemia → pulmonary oedema" reads as causal; oedema only with left heart disease.
- RVF-26: Q waves in V1–V3 non-specific; III > II and V1 ST elevation missing.
- RVF-31: ASE 2005 ranges; ASE 2015 basal >4.1, mid >3.5, length >8.3, RVOT PLAX >3.0 / proximal >3.5 / distal >2.7 cm; "mid wider than basal" wrong for current view.
- RVF-32: mixed 2010/2015 thresholds (S′, RIMP, 3D RVEF); ASE 2015 values given.
- RVF-34: watch line tells you to quote the older (2010) function table; TAPSE 17 vs 16 mm are two editions; table TAPSE <1.6 cm conflicts with RVF-32's <1.7 cm.
- RVF-36: card correct; linked DocT GT key (lifelong anticoagulation in IPAH) disputed under ESC/ERS 2022.
- RVF-41: watch line "levosimendan is the agent of choice" not supported by any guideline.
- RVF-42: "hypotension and hypoxia" are IV prostacyclin effects; iNO rebound on withdrawal missing.
- RVF-44: inlet is IVC–RA, not RV; flow >4 L/min; answer letters shifted against question.

## Not verified
- HFA/ESC 2016 (Harjola) full text not opened (journal sites blocked); its numbers are taken from the card as printed.
- ASE 2025 right-heart severity bands not read.
