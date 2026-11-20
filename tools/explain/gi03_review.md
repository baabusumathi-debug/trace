# GI03 review (independent fact-check, 20 Nov 2026)

Files checked: gi03_learn.py (13 cards) and gi03_topups_learn.py (7 top-ups), against cards/GI03.jsonl, qpack/GI03.md, gi_cardlayer.json and gi_topups.json["GI03"]. check_learn.py GI03: OK (13/13, spine 6). Top-up part counts match the `a` lists.

## Changes

Factual
- GUT-12 d: ESICM 2017 "delay EN" list was incomplete and said "active" bleeding. It left out uncontrolled hypoxaemia and acidosis, bowel obstruction, and high-output fistula without distal access. Now gives the full list: uncontrolled shock, uncontrolled hypoxaemia and acidosis, uncontrolled upper GI bleeding, aspirate over 500 mL/6 h, bowel ischaemia, bowel obstruction, ACS, high-output fistula without distal access. Header updated to match. (Reintam Blaser, ESICM guideline, Intensive Care Med 2017;43:380, abstract)
- GUT-01 b: said nothing about the card's "duodenum: magnesium". Now says magnesium is absorbed mainly in the distal jejunum and ileum (paracellular) and the colon (TRPM6), which is why ileal resection and stomas cause low magnesium. FLAG added. (standard physiology texts)
- GUT-04 trap and GUT-08 a: implied that absent bowel sounds alone predict death. Now: in the 2013 multicentre study absent bowel sounds and GI bleeding were the symptoms most strongly linked to death, but no single symptom was an independent predictor. The number of symptoms is what counts. (Reintam Blaser, Intensive Care Med 2013;39:899, PubMed abstract)
- T_6e2cdcbd a: "mortality rises with each hour of delay" → "rises steeply when treatment is delayed beyond about 24 hours" (standard surgical teaching; the hour-by-hour claim was not supported)

Minor / depth
- GUT-03 c: added that portal blood in trauma patients rarely grows bacteria. That finding is why thinking moved from bacterial translocation to the gut–lymph route. (standard teaching, Moore/Deitch; no figures quoted)
- GUT-03 d: "enters at the left subclavian vein" → "through the thoracic duct at the left venous angle (where the left subclavian and internal jugular veins join)". Toxic lymph skips the liver, so the lung is the first capillary bed it meets. Confirmed. (anatomy)
- GUT-03 trap: an invented split of the wrong answers ("the 20% chose overgrowth or acid") → no split claimed; it now explains why overgrowth tempts people (80% right)
- GUT-08 b: an unsupported reason for the 3-day cut-off → called a pragmatic cut-off; the reason to exclude obstruction is that laxatives and prokinetics would be the wrong treatment for it
- GUT-07 c: "ASPEN/SCCM advise against routine residual checks altogether" → "advise against using residuals as part of routine monitoring" (ASPEN/SCCM 2016)
- T_a1086ece b: added figures for the "about 75–85%" claim: upright PA chest film 80%, upright lateral 98%, CT is the reference (Woodring & Heiser 1995, BestBETs summary). The top-up's 75–85% stands.
- T_051129df trap: "only 24% chose this" was unclear. Now it says that late bleeding which responds to resuscitation goes to CT angiography and IR, and laparotomy is for instability or failed IR (24% right).

## Writer's open items, settled
- Gut absorption sites: correct, except for magnesium (FLAG). Copper (stomach and duodenum), folate (proximal small bowel), B12 and bile salts (terminal ileum): correct.
- Gut–lymph hypothesis: the text is correct (Deitch). Detail sharpened as above.
- ESICM 2017 EN contraindications: fixed (see above).
- Erect CXR for free gas: 75–85% is supported (PA 80% in Woodring 1995). A lateral view raises it, and CT is definitive.
- Bacterial counts per segment (stomach <10³, jejunum ~10⁴, ileum 10⁷–10⁸, colon 10¹¹–10¹², anaerobes ~1000:1): consistent with standard texts. No change.
- Post-pancreatectomy haemorrhage: ISGPS 2007 sets early at ≤24 h and late at >24 h. Late bleeding is from a GDA-stump pseudoaneurysm, with a sentinel bleed, and IR comes first. Text is correct.
- Oesophageal perforation: matches ESGE 2020 (endoscopic closure or stent for early, contained iatrogenic leaks) and WSES 2019 (Boerhaave: mostly surgical). Only the delay wording was changed.

Also checked and correct: ESPEN 2023 (erythromycin first line, 100–250 mg three times daily for 24–48 h, stop after three days; post-pyloric feeding if prokinetics fail; ≤70% EE early, then 80–100% after day 3; SPN "suggested between days four and seven"); Reintam 2013 (two or more symptoms 20%, GI failure 6.4%, 28-day mortality 62.5% vs 28.9%); ESICM 2012 AGI grades and examples; caecal 3-6-9 and 12 cm. The traps were kept, and their true sides were checked.

## Final FLAGS
- GUT-01: magnesium is listed under duodenum; it is absorbed mainly in the distal jejunum, ileum and colon. Minor. (new)
- GUT-04 c: "more than 20% have three or four symptoms". The multicentre data give 20% for two or more, and 6.4% for three or more. (writer's flag, confirmed)
- GUT-07 d: "maximum 5 days" is longer than ESPEN 2023's stop at three days. The DocT GT key (venting gastrostomy) is wrong; the answer is B. (writer's flag, confirmed)
- GUT-08 a: ESICM 2012 says listen for at least 1 minute in two quadrants, repeated; the card says each of 4 quadrants. (writer's flag, kept)
- GUT-12 b/c: the 50–80% / 80–100% targets are not in ESICM 2012 (ESPEN 2023: ≤70% early, then 80–100% after day 3). ESICM 2012 advised no SPN in the first 7 days; the card's "day 4–7" matches ESPEN 2023. (writer's flag, confirmed)
- Top-ups: no flags.
