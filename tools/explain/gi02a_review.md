# GI02A review (independent fact-check, 20 Nov 2026)

Files checked: gi02a_learn.py, gi02a_topups_learn.py (T_9299d85e) against cards/GI02A.jsonl, qpack/GI02A.md, gi_cardlayer.json and gi_topups.json["GI02A"]. Fidelity (bold restatements, letters) correct on all 13 cards and the top-up. `check_learn.py GI02A` OK.

## Writer's unverified items, now settled
- Modified Marshall cut-offs: confirmed (score 2 = P/F 201–300; creatinine 170–310 µmol/L, 1.9–3.6 mg/dL; SBP <90 not fluid-responsive; ≥2 = organ failure). Source: MSD Manual table after Banks, Gut 2013.
- Revised Atlanta mortality with persistent organ failure: about 36–50% confirmed (GPnotebook summary of Banks 2013). Card's 13–35% still untraceable (flag kept).
- APACHE II ≥8 and CRP >150 mg/L: confirmed as the standard cut-offs (Atlanta 1992; used by APEC 2020 to define predicted severe disease). IAP/APA 2013 recommends persistent SIRS instead, so the header's attribution to IAP/APA was wrong.
- APEC: confirmed. 232 patients, predicted severe gallstone AP without cholangitis, urgent ERCP with sphincterotomy within 24 h, death or major complications 38% vs 44% (RR 0.87, 0.64–1.18), cholangitis 2% vs 10% (Schepens, Lancet 2020, abstract).
- Gallstone Ranson: confirmed. Age >70, WBC >18,000, glucose >220, LDH >400, AST >250; haematocrit fall >10%, BUN rise >2, Ca <8, base deficit >4–5 (sources differ), fluid >4 L; no PaO₂ (Wikiwand summary of Ranson).
- Bruising-sign locations: confirmed. Grey Turner flank, Cullen periumbilical, Fox upper outer thigh below the inguinal ligament, Bryant scrotum (LITFL). Usual onset is 3–5 days, not 24–72 h. Dickson & Imrie 1984: 770 patients, 3%, mortality 37%.
- Urine trypsinogen-2: card's 80%/92% confirmed as the pooled figures of an 18-study meta-analysis (Hepatobiliary Pancreat Dis Int 2013;12:355–62).

## Changes
- Header (gi02a_learn.py): the items above moved from "not checked" to "checked online", with sources. "APACHE II/CRP (IAP/APA 2013)" → IAP/APA 2013 recommends persistent SIRS; ≥8 is the Atlanta 1992 cut-off. Urine trypsinogen-2 taken out of "not verified".
- PANC-01 c (minor): "hypercalcaemia activates trypsinogen inside the duct" → calcium raised in the acinar cell and pancreatic juice, which favours trypsinogen activation and duct stones.
- PANC-04 f (depth): mechanism added (trypsinogen-2 is filtered and poorly reabsorbed). The 80%/92% now carries its source (2013 meta-analysis), with the point that it is a bedside aid and does not replace lipase.
- PANC-08 c (factual detail): "gallstone version uses different cut-offs (for example, age >70)" → the full verified gallstone set (ten items, no PaO₂).
- PANC-11 a (depth): added that APEC 2020 still defined predicted severe disease as APACHE II ≥8, Imrie ≥3 or CRP >150.
- PANC-12 table (minor): EUS "mandatory over 40" → "especially over 40". ACG 2024 says a tumour should be considered after 40; it does not make EUS mandatory.
- PANC-13 intro (depth): added APEC's reduction in cholangitis (2% vs 10%), to show that ERCP treats the duct, not the pancreas.
- T_9299d85e a (factual): Grey Turner route "directly through the posterior abdominal wall" → anterior pararenal space through the lumbar triangle. Fox: "along the inguinal ligament" → beneath the inguinal ligament along the psoas and iliacus fascia. Bryant: through the inguinal canal. Added that Fox and Bryant signs also occur with a leaking AAA (LITFL).
- T_9299d85e b (factual): onset "often 24–72 hours" → usually several days (typically 3–5), so the signs are late (LITFL).
- T_9299d85e header: the reviewer's sources were added.

Traps were checked on their truth side and all are kept: post-ERCP mechanism, GT5 hepatic plus coagulation key, 3-week pseudocyst, CTSI 6 vs 7, MRCP vs EUS, CRP not in BISAP or Ranson, APACHE II 18.

## Final FLAGS
- PANC-01: card correct; the AIM1 "contrast toxicity" key is only the best option (the mechanism is mainly mechanical and hydrostatic).
- PANC-03 d: card's "13–35%" mortality for moderate or severe disease is untraceable; revised Atlanta gives about 36–50% for persistent organ failure.
- PANC-05: card correct; the GT5 key (hepatic plus coagulation most predictive of death) has no guideline basis.
- PANC-07: card correct; DocT's "pseudocyst" at 3 weeks is strictly an acute peripancreatic fluid collection.
- PANC-08: Ranson mortality bands vary by source; the gallstone criteria differ from the card's set.
- PANC-09: card correct; DocT's explanation wrongly puts CRP in Ranson.
- PANC-10: card correct; DocT's CTSI key of 6 scores a single collection as 2, but Balthazar scores it 3 (so the total is 7).
- PANC-11 a: card says "above 8"; the standard is 8 or more (minor).
- PANC-12: card correct; DocT keys MRCP alone, but EUS is at least equal and comes first over 40.
- T_9299d85e c: card says "<5% of severe AP"; the source gives about 3% of all AP (mortality 37%).

Not reachable (permission or captcha): pubmed.ncbi.nlm.nih.gov/22575591, Cochrane CD012010, gut.bmj.com Banks 2013 full text, PMC pages. Secondary sources were used instead.
