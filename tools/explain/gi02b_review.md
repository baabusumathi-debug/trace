# GI02B review (second, independent check, 20 Nov 2026)

Files checked: gi02b_learn.py, gi02b_topups_learn.py (T_305a0e05) against cards/GI02B.jsonl, qpack/GI02B.md, gi_cardlayer.json, gi_topups.json["GI02B"]. `check_learn.py GI02B` OK.

## Changes
- PANC-14 extra (Ringer's calcium): the calcium figure was given without context → now "about 1.4 mmol/L in the US formulation, 2 mmol/L in Hartmann's; less than normal plasma total calcium, so the concern is theoretical" (standard pharmacopoeia values). *Minor factual.*
- PANC-14 trap: "commonest wrong choice" was made up (the qpack has no per-option data) → now just "69% chose the keyed Ringer's answer". *Minor.*
- PANC-17 f: "nasogastric preferred by ACG 2024" could not be verified from ACG 2024 summaries → now "as safe as nasojejunal (IAP/APA 2013, WSES 2019) and easier to place", with the reason. *Minor factual.*
- PANC-20 a: "enzymes reach the lung first through the venous return" was wrong (portal blood goes to the liver first) → now "portal blood and lymph; the thoracic duct makes the lung the first capillary bed reached". *Factual.*
- PANC-21 e: said Regli 2019 suggests "under 14" for IAH, implying the card's 15 was wrong → now says Regli's conclusions give a maximum of 15, the text calls under 14 "not unreasonable", and driving pressure should be used to avoid excessive PEEP (Regli, Ann Intensive Care 2019, full text). *Factual (it changed a FLAG).*
- PANC-21 d: added Regli's PEEP ≈ 50% of IAP (cmH2O), set by best compliance (same source). *Depth.*
- PANC-23 a: "about 40% of patients operated on for persistent unwellness have infected necrosis" could not be traced → removed. Now explains the reasoning: missed infection, and the collection has walled off by four weeks. *Unverifiable specific.*
- PANC-25 a: CytoSorb was "up to about 55–60 kDa" → now "up to about 60 kDa, by the manufacturer's figure" (cytosorbents.com). *Minor.*
- PANC-25 a: the 17-study haemofiltration meta-analysis could not be traced. It stays as the card's claim, set against the Cochrane CD012959 review (2020: 3 RCTs, 219 patients; effect on in-hospital death uncertain; little or no difference between high-volume and standard doses). *Depth/safety.*
- Header: WATERFALL primary RR was "1.28 (0.77–2.12)" → "adjusted RR 1.30 (0.78–2.18)"; overload RR 2.85 (1.36–5.94) added (Northwestern PCCM / ACP summaries of NEJM 2022). Replaced the "not checked" list with what was checked and how. *Minor (header only).*
- Topup T_305a0e05 a: "mortality over 40%" → "68 cohorts … pooled mortality 43%" (Intern Emerg Med 2023, 36892797). *Minor.*

## Verified as written (no change)
- WATERFALL: 249 randomised of 744 planned (ACP gives 248 at interim), 22.1% vs 17.3%, overload 20.5% vs 6.3%, 7.8 vs 5.5 L at 48 h, checkpoint at 3 h then 12/24/48/72 h. The protocol (Bolado, Front Med 2020) defines hypovolaemia as ≥1 criterion and overload as ≥2 of 3 criteria with ARDS excluded. It has **no** "suspected/definite" category, and the action is to reduce or stop LR.
- TENSION: n 98, 43% vs 45% for the primary endpoint; fistula and stay lower with endoscopy (5% vs 32% from the full paper; mortality 18% vs 13%).
- MERINO: 30-day mortality 23/187 (12.3%) vs 7/191 (3.7%).
- PROPATRIA: mortality 16% vs 6%; bowel ischaemia in 9 patients on probiotics (8 fatal) and none on placebo.
- PONCHO: 5% (6/128) vs 17% (23/136).
- EPIPAN: no difference in ventilator-free days; invasive ventilation 14 vs 6 days with epidural.
- ACG 2024: LR, 1.5 mL/kg/h, oral feeding within 24–48 h with a low-fat diet in mild AP, no prophylactic antibiotics, no FNA, delay ≥4 weeks, cholecystectomy before discharge.
- Regli 2019: transmission about 50% (20–60%); plateau formula and worked example of 37; inspiratory transpulmonary pressure under 25.
- Pancreatic encephalopathy: 11% pooled incidence across all AP, 43% mortality (68 cohorts). The card's 10–20% in severe AP is left as written.
- Traps kept. Their correct sides were checked: aggressive fluid and saline; NPO (bank key out of date); jejunal-only feeding; pip-tazo for ESBL; probiotics; early necrosectomy; PANTER mortality; TENSION "fewer complications"; reducing PEEP (bank key debatable); CytoSorb mortality and endotoxin.

## Final FLAGS
- PANC-15: the primary-outcome/interim line appears twice on the card. Minor: there is also a 3-hour overload check before the 12-hour checkpoint.
- PANC-16 c: in the WATERFALL protocol, overload means ≥2 of 3 criteria (ARDS excluded). "One = suspected" is not a protocol category. In a, the protocol also counts a rise in creatinine or BUN from the previous value.
- PANC-17: the card is correct. The Marrow "NPO" key is out of date. The card-layer cross note contradicts the qpack: it calls the Marrow key "early oral feeding" and says ACG 2024 gives "within 24 h", but ACG 2024 says 24–48 h (AGA 2018 says 24 h).
- PANC-21: the card is correct. The writer's driving-pressure flag was removed, because Regli's conclusions do give 15. The DocT key "reduce PEEP" is debatable.
- PANC-23: the card is correct (matches WSES 2019). IAP/APA 2013 times these differently: obstruction at 4–8 weeks, disconnected duct with a symptomatic collection at more than 8 weeks.

## Could not verify
- The card's 17-study high-volume haemofiltration meta-analysis (not traced; PMC was blocked).
- ACG 2024 "reassess within 6 hours" (kept; it is consistent with the guideline summaries).
- PubMed, NCBI eutils and PMC pages were blocked or behind a captcha this session. Secondary summaries (ACP, Northwestern, CIDRAP, institutional repositories, DOAJ) were used instead.
