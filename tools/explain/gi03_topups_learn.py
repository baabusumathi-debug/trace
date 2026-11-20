# GI03 top-up cards — Explain v3 ("Learn" depth), same fields and voice as gi03_learn.py.
# Fields: sub, step (index into gi03_learn.SPINE), intro, parts [(letter, text)] in the order of the top-up’s `a` list, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions read on 20 Nov 2026 from wd/map/doct_gt_distinct_all.jsonl (GT1o Q51, Q62; GT6 Q62, Q91; CGT1 Q53), wd/map/doct_qbank_all.jsonl (DocT Acute Abdomen & Peritoneum
# Q5, Q7, Q8) and QMap_full_932.csv (Marrow QB41-Q06).
# From standard references (confident): oesophageal perforation management (ESGE 2020 iatrogenic perforation position statement; WSES 2019 Boerhaave); erect chest film sensitivity for free
# gas about 75–85% after sitting upright 10 minutes; C. perfringens alpha-toxin (phospholipase C, lecithinase), penicillin plus clindamycin; visceral pain by embryological gut; diaphragmatic
# stomata and lymphatic lacunae; bacterial counts per segment; ISGPS 2007 post-pancreatectomy haemorrhage (early within 24 h, late after 24 h; sentinel bleed; gastroduodenal artery stump
# pseudoaneurysm; interventional radiology first for late bleeding).
# Independent review (20 Nov 2026): erect film sensitivity checked against Woodring & Heiser 1995 (BestBETs summary: upright PA chest 80%, upright lateral 98%, CT reference);
# ESGE 2020 and WSES 2019 positions, ISGPS 2007 timing, segmental bacterial counts and diaphragmatic stomata judged consistent with standard references; no card errors found.
T = {}

T['T_6e2cdcbd'] = dict(
  sub="Gut in critical illness → Emergencies → Contained oesophageal perforation",
  step=3,
  intro="Step 3 includes the surgical emergencies that reach the ICU. Oesophageal perforation is one where the decision is not always an operation: a small, contained leak in a stable patient can be closed from inside. Two DocT GT questions link here: the contained post-endoscopy perforation (stent, 55% right) and the corrosive ingestion that leads to posterior mediastinitis (59% right).",
  parts=[
    ('a', "**Non-operative: covered oesophageal stent (or endoscopic clip), nil by mouth, PPI.** A perforation found early after endoscopy, contained, with little mediastinal soiling and a stable patient, can be sealed endoscopically; the stent covers the hole while it heals and avoids a thoracotomy, whose mortality is high and rises steeply when treatment is delayed beyond about 24 hours."),
    ('b', "**Broad-spectrum antibiotics plus antifungal, nutrition (jejunal or parenteral), drain any collection.** Oral flora and Candida enter the mediastinum, so cover both. The patient cannot swallow, so feed beyond the leak. Any collection or pleural effusion is drained percutaneously or with a chest drain."),
    ('c', "**Surgery (primary repair and drainage; diversion or oesophagectomy if non-viable) for uncontained leaks, sepsis or instability.** Once contamination is free or the patient is septic, source control needs an operation. Primary repair is preferred when the tissue is viable; diversion or resection is for a necrotic or diseased oesophagus."),
    ('d', "**Boerhaave (barogenic, full-thickness, usually distal) is more often surgical.** The rupture follows vomiting against a closed glottis, usually in the left posterolateral distal oesophagus, and spills gastric contents under pressure, so contamination is wide and late diagnosis common."),
    ('e', "**Any full-thickness oesophageal perforation (caustic, instrumental, Boerhaave) causes acute posterior mediastinitis: chest pain, fever, sepsis, mediastinal air; anterior mediastinitis follows sternotomy.** The oesophagus lies in the posterior mediastinum, so its leak infects that compartment. Air-fluid levels along the oesophagus on CT after a corrosive ingestion mean perforation and abscess there."),
  ],
  mimic=[
    ("Posterior vs anterior mediastinitis", "Posterior: oesophageal perforation (instrumental, Boerhaave, corrosive, foreign body). Anterior: after sternotomy."),
    ("Posterior mediastinitis vs Ludwig’s angina", "Ludwig’s is submandibular space infection; it can descend into the mediastinum, but the source is dental, not oesophageal."),
  ],
  traps=[
    ("“Thoracotomy with primary repair for a small contained leak in a stable patient”", "That is for uncontained leaks, sepsis or instability; contained and stable gets a stent (45% chose otherwise)."),
    ("“Diversion or oesophagectomy first”", "Only for a non-viable or diseased oesophagus."),
    ("“Corrosive ingestion with oesophageal air-fluid levels is anterior mediastinitis”", "The oesophagus is posterior; anterior mediastinitis follows sternotomy."),
  ],
  decode=[
    ("Stable, small contained mid-oesophageal perforation after endoscopy, minimal soiling — initial therapy? [DocT GT]", "Oesophageal stent (55% right)."),
    ("Corrosive ingestion, chest pain, sepsis, air-fluid levels along the oesophagus on CT — diagnosis? [DocT GT]", "Acute posterior mediastinitis (59% right)."),
  ],
  punch="A contained, early, instrumental oesophageal leak in a stable patient is stented; a free leak, sepsis or instability goes to surgery. Any full-thickness oesophageal leak infects the posterior mediastinum.",
)

T['T_a1086ece'] = dict(
  sub="Gut in critical illness → Emergencies → Board-like abdomen: perforated ulcer vs bile peritonitis",
  step=3,
  intro="Step 3 also asks what a rigid abdomen means. Generalised peritonism has many causes, and the history usually names it: an ulcer history with sudden pain and shoulder-tip radiation means a perforated ulcer; a liver biopsy or cholecystectomy days earlier means bile. Two DocT GT questions link here, one for each.",
  parts=[
    ('a', "**Perforated ulcer: sudden severe epigastric pain, shoulder-tip pain (diaphragm, C3–5), ulcer or NSAID history, shock.** Acid and gastric contents flood the peritoneum at once, so the onset is abrupt and the abdomen becomes board-like; fluid under the diaphragm irritates phrenic afferents and the pain is referred to the shoulder."),
    ('b', "**Erect chest X-ray after 10 minutes upright shows free gas in about 75–85% (CT if negative); then resuscitate, NG tube, IV PPI, antibiotics, urgent omental-patch repair.** Ten minutes lets the gas rise under the diaphragm. A negative film does not exclude perforation: in one series the upright PA chest film found 80% of pneumoperitoneum and an upright lateral view 98%, and CT is the reference test. Repair is usually a Graham omental patch."),
    ('c', "**Bile peritonitis: days after cholecystectomy, liver biopsy or trauma; generalised pain, ascites, ileus, rising bilirubin.** Bile is less acutely irritant than acid, so the picture builds over days, and the peritoneum reabsorbs bilirubin, so the serum level rises."),
    ('d', "**Confirm by ultrasound or CT collection, HIDA leak or bile on aspiration; then percutaneous drainage and ERCP stent or sphincterotomy; surgery if generalised peritonitis.** Lowering the pressure in the bile duct with a stent lets the leak close; the collection is drained."),
  ],
  mimic=[
    ("Perforated ulcer vs acute pancreatitis", "Both give severe epigastric pain; pancreatitis has no free gas and has a raised lipase (GI02A)."),
    ("Perforated ulcer vs mesenteric ischaemia", "Ischaemia has pain out of proportion to a soft abdomen and no free gas early (GI04)."),
  ],
  traps=[
    ("“Rigid abdomen 3 days after liver biopsy — intestinal obstruction or cholecystitis”", "Generalised peritonism after a biopsy is bile peritonitis (88% right)."),
    ("“A negative erect chest film excludes perforation”", "It misses about one in five; do CT."),
  ],
  decode=[
    ("Ulcer history, sudden upper abdominal pain to both shoulders, rigid abdomen, upright chest film shown — diagnosis? [DocT GT]", "Perforated peptic ulcer."),
    ("Board-like abdomen 3 days after liver biopsy — diagnosis? [DocT GT]", "Bile peritonitis (88% right)."),
  ],
  punch="The history separates them: sudden pain with an ulcer history and free gas is a perforated ulcer needing a patch; slow generalised peritonism days after a biliary or liver procedure is bile, needing drainage and an ERCP stent.",
)

T['T_e215de25'] = dict(
  sub="Gut in critical illness → Emergencies → Clostridial gas gangrene of the abdomen",
  step=3,
  intro="Step 3 includes the abdomen that is septic and full of gas. Gas in the bowel wall, mesentery and abdominal wall with crepitus and shock in a diabetic points to a gas-forming organism that destroys tissue. The one DocT QBank question asks which organism (77% right).",
  parts=[
    ('a', "**Clostridium perfringens: anaerobic, spore-forming Gram-positive rod.** It grows in dead, poorly perfused tissue and ferments it, producing gas that tracks along tissue planes and gives crepitus."),
    ('b', "**Alpha-toxin (lecithinase) causes myonecrosis, haemolysis and shock.** Alpha-toxin is a phospholipase C that breaks down cell membranes, so muscle dies and red cells lyse; it also depresses the myocardium and causes profound shock."),
    ('c', "**Immediate radical debridement plus penicillin with clindamycin (stops toxin synthesis), with or without hyperbaric oxygen.** Antibiotics cannot reach dead tissue, so the dead tissue must go. Clindamycin inhibits protein synthesis and so stops toxin production even when bacteria are not dividing. Hyperbaric oxygen inhibits alpha-toxin production by this anaerobe, but must not delay surgery."),
    ('d', "**Gas without myonecrosis in diabetics (emphysematous pyelonephritis or cholecystitis) is usually E. coli or Klebsiella.** Gram-negative organisms ferment the high glucose in diabetic tissue and make gas, but they do not destroy muscle the way clostridia do."),
  ],
  mimic=[
    ("Clostridial myonecrosis vs polymicrobial necrotising fasciitis", "Clostridia: muscle necrosis, gas, haemolysis and rapid shock. Polymicrobial: fascial spread, mixed aerobes and anaerobes, needs broad cover."),
  ],
  traps=[
    ("“E. coli or Klebsiella” for gas-forming peritonitis with shock and crepitus", "They make gas in the kidney or gallbladder without myonecrosis; tissue destruction with shock is C. perfringens."),
  ],
  decode=[
    ("Diabetic, peritonitis, shock, abdominal-wall crepitus, gas in bowel wall, mesentery and soft tissue — organism? [DocT QBank]", "Clostridium perfringens (77% right)."),
  ],
  punch="Gas, crepitus, myonecrosis and shock mean C. perfringens: alpha-toxin kills tissue faster than antibiotics can reach it, so debride at once and give penicillin with clindamycin.",
)

T['T_ce178f52'] = dict(
  sub="Gut in critical illness → Assessment → Visceral abdominal pain map",
  step=3,
  intro="Step 3 starts at the bedside, and where the pain is felt tells you which part of the gut is involved. The one DocT QBank question is a match-the-following of gut segment to pain region (74% right).",
  parts=[
    ('a', "**Foregut (stomach, duodenum, biliary tree, pancreas): epigastrium.** Visceral afferents from each embryological segment enter the cord at the same levels as the skin of the region where the pain is felt: foregut about T5–T9."),
    ('b', "**Midgut (small bowel, appendix, colon to mid-transverse): periumbilical.** Midgut afferents enter at about T8–T11, the dermatomes of the umbilicus."),
    ('c', "**Hindgut (distal colon, rectum): hypogastrium.** Hindgut afferents enter at about T11–L1."),
    ('d', "**Visceral pain is dull and midline (bilateral autonomic afferents); parietal pain is sharp and localised, so appendicitis moves from umbilicus to RIF.** The gut is supplied from both sides, so its pain is central and poorly localised. The parietal peritoneum has somatic innervation, so once inflammation reaches it the pain becomes sharp, localised and worse on movement."),
  ],
  mimic=[
    ("Visceral vs somatoparietal pain", "Visceral: dull, midline, by embryological segment. Parietal: sharp, localised, worse with movement and cough."),
  ],
  traps=[
    ("“Appendicitis pain starts in the right iliac fossa”", "It starts periumbilical (midgut visceral) and moves to the RIF when the parietal peritoneum is involved."),
  ],
  decode=[
    ("Match foregut, midgut, hindgut and somatoparietal pain to their sites [DocT QBank]", "Epigastric, periumbilical, hypogastric, and sharp localised (74% right)."),
  ],
  punch="Visceral pain is felt in the midline by embryological gut: foregut epigastric, midgut periumbilical, hindgut hypogastric; it becomes sharp and localised when the parietal peritoneum is reached.",
)

T['T_142d1a37'] = dict(
  sub="Gut in critical illness → Pathophysiology → Peritoneal clearance by the diaphragm",
  step=2,
  intro="Step 2 explains how organisms that leave the gut reach the blood. The peritoneum drains mainly through the diaphragm, pumped by breathing. The one DocT QBank question tests which phase opens the stomata (65% right).",
  parts=[
    ('a', "**Expiration: the diaphragm relaxes, stomata on its peritoneal surface open, and fluid and bacteria enter lymphatic lacunae.** As the diaphragm relaxes and rises, the gaps between its mesothelial cells widen and peritoneal fluid, with any bacteria in it, is drawn into the lymphatic channels beneath."),
    ('b', "**Inspiration: it contracts and pushes lymph on to the thoracic duct.** Contraction squeezes the lacunae and closes the stomata, driving lymph towards the mediastinal nodes and the thoracic duct."),
    ('c', "**So peritoneal infection reaches the blood fast, and splinting (IAH, ventilation) slows clearance.** Bacteria can be in the blood within minutes of peritoneal contamination, which is why peritonitis causes early bacteraemia. Raised intra-abdominal pressure, a splinted diaphragm and positive-pressure ventilation change this pump."),
  ],
  mimic=[
    ("Stomata open vs lymph propelled", "Stomata open in expiration (relaxation); lymph is propelled in inspiration (contraction)."),
  ],
  traps=[
    ("“Contraction during exhalation propels lymph into the thoracic duct”", "The diaphragm contracts in inspiration, not exhalation; in exhalation it relaxes and the stomata open."),
  ],
  decode=[
    ("Mechanism by which the diaphragmatic pump moves peritoneal fluid? [DocT QBank]", "Relaxation in exhalation opens the stomata (65% right)."),
  ],
  punch="Breathing pumps the peritoneum: stomata open as the diaphragm relaxes in expiration and lymph is pushed to the thoracic duct as it contracts, so peritoneal bacteria reach the blood quickly.",
)

T['T_dc881b68'] = dict(
  sub="Gut in critical illness → Emergencies → Perforation site and contamination",
  step=3,
  intro="Step 3 includes what a perforation spills. The bacterial load rises by many orders of magnitude from stomach to colon, so the site of perforation predicts how dirty the peritonitis is. The one Marrow question asks which site gives the greatest infection: the distal colon.",
  parts=[
    ('a', "**Bacterial load rises down the gut: stomach under 10³/mL (acid), jejunum about 10⁴, ileum about 10⁷–10⁸, colon about 10¹¹–10¹².** Acid kills most swallowed organisms; transit keeps the jejunum relatively clean; stasis and the ileocaecal valve allow the colon to hold the densest bacterial population in the body."),
    ('b', "**Colon flora is anaerobe-dominant (Bacteroides about 1000:1 over aerobes).** That is why colonic peritonitis needs anaerobic cover."),
    ('c', "**So distal colonic perforation gives the heaviest polymicrobial contamination: source control plus cover for Gram-negatives and anaerobes.** Faecal peritonitis has the highest rate of abscess and septic shock."),
    ('d', "**Gastroduodenal perforation is initially chemical peritonitis with a low bacterial load.** The early injury is from acid and enzymes; infection follows if the leak is left, and is more likely when acid is suppressed."),
  ],
  mimic=[
    ("Gastric vs colonic perforation", "Gastric: early chemical peritonitis, few bacteria. Colonic: faecal peritonitis, dense anaerobes and Gram-negatives."),
  ],
  traps=[
    ("“Gastric perforation gives the worst infection because of the acid”", "Acid causes chemical injury but keeps the bacterial count low."),
  ],
  decode=[
    ("Pneumoperitoneum — which perforation site gives the greatest infection? [Marrow]", "Distal colon."),
  ],
  punch="The further down the gut, the more bacteria: the stomach is nearly sterile, the colon carries 10¹¹–10¹² per mL, mostly anaerobes, so colonic perforation is the dirtiest peritonitis.",
)

T['T_051129df'] = dict(
  sub="Gut in critical illness → Emergencies → Delayed post-pancreatectomy haemorrhage",
  step=3,
  intro="Step 3 ends with bleeding after major abdominal surgery, where timing decides the treatment. Late bleeding after a Whipple is from a vessel eroded by a pancreatic leak, which is best reached by interventional radiology. The one DocT GT question had only 24% right; most chose laparotomy.",
  parts=[
    ('a', "**Delayed post-pancreatectomy haemorrhage (over 24 h): usually a gastroduodenal-artery stump pseudoaneurysm eroded by a pancreatic leak.** Pancreatic juice from a leaking anastomosis digests the wall of the ligated gastroduodenal artery or nearby vessels, forming a pseudoaneurysm that ruptures days to weeks later."),
    ('b', "**Often heralded by a ‘sentinel bleed’ (blood in drain or NG).** A small bleed that stops is a warning of rupture, and should prompt CT angiography immediately."),
    ('c', "**Responds to resuscitation: urgent CT angiography and interventional radiology (embolisation or covered stent).** Re-operating in an inflamed, leaking field is difficult and dangerous; angiography finds the pseudoaneurysm and closes it from inside."),
    ('d', "**Unstable or IR fails: laparotomy; early (under 24 h) haemorrhage goes back to theatre.** Bleeding in the first 24 hours is usually technical (a slipped ligature or anastomotic bleed) and is fixed surgically."),
  ],
  mimic=[
    ("Early vs late post-pancreatectomy haemorrhage", "Early (under 24 h): technical, back to theatre. Late (over 24 h): pseudoaneurysm from a leak, interventional radiology first."),
  ],
  traps=[
    ("“Emergent exploratory laparotomy” two weeks after a Whipple with a transfusion-responsive bleed", "Late bleeding that responds to resuscitation goes to CT angiography and interventional radiology; laparotomy is for instability or failed embolisation. Only 24% got this right."),
    ("“Admit and observe”", "A responsive bleed is a sentinel; it will recur."),
  ],
  decode=[
    ("Two weeks after Whipple, tachycardic, hypotensive, free fluid, BP responds to blood — next? [DocT GT]", "Emergent interventional radiology (24% right)."),
  ],
  punch="Bleeding after a Whipple is timed: in the first 24 hours it is technical and goes back to theatre; days to weeks later it is a gastroduodenal-artery pseudoaneurysm eroded by a leak and goes to interventional radiology.",
)

FLAGS = {}
