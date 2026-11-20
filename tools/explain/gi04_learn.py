# GI04 — Explain v3 ("Learn" depth): mesenteric ischaemia — the three arteries and their territories, collaterals and watershed points, splanchnic physiology, ischaemia–reperfusion,
# classification, risk factors and history, pain by type, small bowel vs colonic ischaemia, laboratory tests, gastrointestinal tonometry, imaging, general management,
# treatment by cause and peritonitis, open vs endovascular repair, thrombotic/venous/non-occlusive disease, true/false sweep.
# No mnemonics or hooks. Driven by qpack/GI04.md (22 question links; MES-06 risk factors and MES-08 small bowel vs colon asked 5 times each, MES-11 imaging 4, MES-10 tonometry 3,
# MES-15 2; MES-02, MES-07, MES-13 once each). MES-01, 03, 04, 05, 09, 12, 14, 16 have no linked question and get short explanations with [pattern] decode items.
# Fields as TOX01, plus SPINE, PRIMER and step. Table cards (no lettered parts) take parts a, b, c… in the order of the card’s rows. No Top-up cards for GI04.
# No `fix` entries exist for GI04 in trace/test/data/qbank.json (checked 20 Nov 2026); the gi_cardlayer.json `lines` for MES-06, MES-11 and MES-13 were read and are agreed with.
# Checked online on 20 Nov 2026:
#  - WSES 2022 AMI update (Bala, World J Emerg Surg 2022;17:54): incidence 0.09–0.2% of acute admissions; embolism about 50% classically, falling to about 25% in recent series;
#    thrombosis 15–25%, recently up to 40%; NOMI about 20–25%; MVT under 10% (5–15%); pain out of proportion → assume AMI (1C); plain film not recommended (1B); no lab test accurate enough
#    (2B); CTA without delay (1A), even with acute kidney injury; oral contrast ‘not indicated and even harmful’; portal/mesenteric venous gas strongly suggests infarction; fluids, electrolytes,
#    gastric decompression (1B), broad-spectrum antibiotics (1C); prompt laparotomy/laparoscopy with peritonitis (1C); endovascular first for arterial occlusion where available (1C); damage control
#    with temporary closure when resection is needed (1B); second look usually at 24–48 h; UFH for MVT (1B); vasopressors with caution; dobutamine, low-dose dopamine, milrinone have least effect on
#    mesenteric flow; noradrenaline + dobutamine preferred to vasopressin; noradrenaline, adrenaline, vasopressin and digoxin may worsen mucosal perfusion; papaverine/PGE1 for NOMI.
#  - ESVS 2025 mesenteric guideline (Eur J Vasc Endovasc Surg 2025; full text read in part): a single lactate or D-dimer must not be used to confirm or exclude AMI (Class III — replaces the
#    2017 advice that a normal D-dimer may rule it out); urgent CTA in arterial and venous phases regardless of renal function (Class I); endovascular revascularisation first-line for embolic or
#    thrombotic SMA occlusion (IIa); revascularise before resection, resect without primary anastomosis and plan a second look (IIa); retrograde open mesenteric stenting when percutaneous
#    stenting fails (IIb); NOMI: suspect in shock with CT signs and no significant SMA stenosis (IIa), intra-arterial papaverine or prostaglandin under heparin (IIb), decompression laparotomy when
#    NOMI accompanies abdominal compartment syndrome (I), mortality about 70%; MVT: UFH or LMWH first line (I), 3–6 months VKA or LMWH (I), DOAC may be considered (IIb), indefinite if idiopathic or
#    permanent risk factor (I), thrombolysis/thrombectomy if deteriorating on anticoagulation (IIb); chronic MI: post-prandial pain, food fear, weight loss; >50% stenosis of the SMA and another artery.
#  - Cudnik 2013 meta-analysis (Acad Emerg Med): D-dimer sensitivity 96%, specificity 40%; L-lactate 86% / 44%; CT 94% / 95%.
#  - Treskes 2017 meta-analysis (Intern Emerg Med): I-FABP 79% / 91% (one assay) and 75% / 79% (another); D-lactate 72% / 74%; alpha-GST 68% / 84%.
#  - Beaulieu 2014 (J Vasc Surg 59:159; NIS 2005–2009): 23,744 AMI admissions, 4,665 treated, 679 revascularised — 514 open (75.7%), 165 endovascular (24.3%); mortality 39.3% vs 24.9%;
#    bowel resection 33.4% vs 14.4%; TPN 24.4% vs 13.7%.
#  - Belgian ICU series (BMC Gastroenterol 2019, 214 ICU patients with arterial AMI, 2000–2017): 30-day mortality 71%; revascularisation in 17 (≈8%), 47% of whom died; NOMI particularly common;
#    higher vasopressor dose and rising lactate predicted death, anticoagulation lower mortality.
#  - ACG 2015 colon ischaemia (Brandt): CT with IV and oral contrast as first imaging; colonoscopy within 48 h to confirm (avoid with peritonitis or gangrene); multiphasic CTA for isolated right colon
#    ischaemia or when AMI cannot be excluded; antibiotics for moderate or severe disease; most cases resolve.
# From standard references without a fresh check (confident unless said): arterial anatomy and collaterals (Bühler, Riolan, Drummond, Griffiths, Sudeck), the SMA embolus lodging beyond the middle colic,
# rectal sparing via the internal iliac supply; xanthine oxidase reperfusion injury; the card’s physiology numbers on MES-03 and tonometry numbers on MES-10 (from Naven’s notes; not re-verified);
# MES-06 a ‘17% aortic wall thrombus’ (not traced); MVT with a personal or family history of DVT/PE in about half (Kumar, NEJM 2001).

# Independent review (20 Nov 2026): Treskes 2017 abstract re-read (I-FABP Uden 79.0/91.3, Osaka 75.0/79.2; D-lactate 71.7/74.2; α-GST 67.8/84.2: confirmed);
#  Oldenburg 2004 (Arch Intern Med) — splanchnic share about 25% resting, 35% post-prandial; Ackland 2000 (Crit Care 4:269) — hepatosplanchnic 30% of output, mucosal pH falls below ~50% of
#  baseline SMA flow, supply dependency possible after a 30% fall; 75% reduction for up to 12 h is the classical review figure; MAP 45 mmHg NOT traced (softened);
#  Mensink 2006 thesis (Erasmus) — gastric–arterial PCO₂ gradient upper limit 0.8 kPa after exercise; tonometry the only proven test for reversible ischaemia; jejunal 1.4 kPa NOT traced;
#  Acosta 2005 (Ann Surg 241:516, 213 autopsies) — embolic source found in 80%, residual cardiac thrombus 48%, synchronous emboli 68%; the card’s ‘17% proximal aortic thrombus’ NOT traced.
SPINE = [
  ("Three arteries and their watersheds", "The coeliac, superior and inferior mesenteric arteries supply fixed territories joined by collaterals, and the joins at the splenic flexure and rectosigmoid are where low flow strikes first."),
  ("Low flow, then reperfusion injury", "The gut tolerates a large fall in flow by extracting more oxygen, but the villus tip dies first, and restoring flow adds a second, free-radical injury with systemic effects."),
  ("Four causes, four stories", "Embolism, thrombosis, non-occlusive vasospasm and venous thrombosis each have a typical patient and a typical pain, and colonic ischaemia is a separate, milder disease."),
  ("CT angiography makes the diagnosis", "No blood test confirms or excludes it, so a suspicion based on pain out of proportion goes straight to biphasic CT angiography, and peritonitis goes straight to theatre."),
  ("Treat the cause, then the bowel", "Resuscitate, anticoagulate and avoid vasoconstrictors; revascularise by the cause, endovascularly if there is no peritonitis; resect only dead bowel and look again."),
]

PRIMER = "Mesenteric ischaemia is uncommon (about 0.1–0.2% of emergency admissions) but kills most of those in whom it is missed, because the window between reversible mucosal ischaemia and transmural infarction is measured in hours. The early patient has severe pain and a soft abdomen; by the time there is guarding, lactate and gas in the bowel wall, the bowel is dead. The ICU sees it in two ways: as the cause of an acute abdomen, and as a complication of shock and vasopressors (non-occlusive disease) in a sedated patient who cannot describe pain. This deck runs from anatomy to the operating table."

L = {}

L['MES-01'] = dict(
  sub="Mesenteric ischaemia → Anatomy → Three arteries, three territories",
  step=1,
  intro="Step 1 starts with which artery feeds which bowel, because the pattern of ischaemic bowel on CT or at laparotomy tells you where the block is.",
  parts=[
    ('a', "**Coeliac: stomach, liver, part of the pancreas, proximal duodenum.** The foregut. Its territory is rarely infarcted because it is richly collateralised and the liver has the portal vein as well."),
    ('b', "**Superior mesenteric: distal duodenum, the entire small bowel, ascending colon, proximal transverse colon.** The midgut, and the artery that matters in acute mesenteric ischaemia. It leaves the aorta at an acute angle in line with the flow, so emboli enter it easily and lodge a few centimetres in, usually just beyond the middle colic branch. That spares the proximal jejunum and the transverse colon. A thrombosis at the origin (on atheroma) instead kills the whole territory from the duodenojejunal flexure to the mid transverse colon."),
    ('c', "**Inferior mesenteric: distal transverse colon, descending colon, to the upper rectum.** The hindgut. Its occlusion is usually silent because the arc of Riolan and the marginal artery refill it from the SMA (MES-02); it matters when the IMA is sacrificed in aortic surgery and those collaterals are poor."),
  ],
  mimic=[
    ("Embolic vs thrombotic SMA occlusion at laparotomy", "Embolus: proximal jejunum and transverse colon spared. Thrombosis: ischaemia from the first jejunal loop onwards."),
  ],
  traps=[
    ("“The SMA supplies the whole colon”", "Only to the proximal two-thirds of the transverse colon; beyond that is the IMA."),
  ],
  decode=[
    ("Ischaemic small bowel with a viable proximal jejunum — likely cause? [pattern]", "SMA embolus lodged beyond the middle colic origin."),
  ],
  punch="The SMA feeds all the small bowel and the right colon. An embolus lodges beyond the middle colic and spares the proximal jejunum; a thrombosis at the origin does not.",
)

L['MES-02'] = dict(
  sub="Mesenteric ischaemia → Anatomy → Collaterals and watershed points",
  step=1,
  intro="Step 1 continues with the joins between the three territories. Where collaterals are good, one artery can close silently; where they are thin, the bowel at the join is the first to suffer in low flow. The one real question, which only 34% got right, put a hypotensive ICU patient’s ulcers at the splenic flexure.",
  parts=[
    ('a', "**Coeliac to superior mesenteric: the arc of Bühler (and the pancreaticoduodenal arcades).** The pancreaticoduodenal arcades (superior from the gastroduodenal artery, inferior from the SMA) are the main route and enlarge when one origin narrows. The arc of Bühler is a rare embryological remnant running directly between the two trunks. Good collateral here is why one-vessel disease is usually asymptomatic, and why chronic mesenteric ischaemia generally needs two arteries affected."),
    ('b', "**Superior to inferior mesenteric: the arc of Riolan and the marginal artery (of Drummond).** Riolan’s arc joins the middle colic to the left colic close to the root of the mesentery; the marginal artery runs along the colon’s border. A visibly enlarged arc of Riolan on angiography means one of the two trunks is narrowed."),
    ('c', "**Griffiths’ point: the splenic flexure.** Here the marginal artery between the SMA and IMA territories is thin or absent in some people, so in shock the splenic flexure is the first part of the colon to become ischaemic."),
    ('d', "**Sudeck’s point: the rectosigmoid junction.** The join between the last sigmoid artery and the superior rectal artery. Below it the rectum is also fed by the middle and inferior rectal arteries from the internal iliacs, which is why ischaemic colitis usually spares the rectum."),
  ],
  mimic=[
    ("Ischaemic colitis vs pseudomembranous colitis at endoscopy", "Ischaemia: segmental, pale or dusky mucosa with linear ulcers at a watershed, rectum spared. C. difficile: raised yellow-white plaques, often throughout the colon."),
    ("Ischaemic colitis vs Crohn’s or infective proctitis", "Crohn’s: chronic, skip lesions, aphthous and deep ulcers, often terminal ileum. Proctitis: the rectum itself, which ischaemia spares."),
  ],
  traps=[
    ("“An ICU patient on antibiotics with bloody diarrhoea has C. difficile”", "The hypotension, the sudden onset and pale mucosa with linear ulcers at the splenic flexure point to ischaemia; only 34% chose ischaemic colitis on DocT QBank."),
    ("“Sudeck’s point is the splenic flexure”", "Griffiths’ point is the splenic flexure; Sudeck’s is the rectosigmoid (MES-16 a)."),
  ],
  decode=[
    ("Hypotensive ICU patient, sudden pain and bloody diarrhoea, pale mucosa and linear ulcers at the splenic flexure — diagnosis? [DocT QBank]", "Ischaemic colitis: a watershed site after low flow (34% right)."),
    ("Watershed between SMA and IMA territories / at the rectosigmoid? [pattern]", "Griffiths’ point (splenic flexure) / Sudeck’s point."),
  ],
  punch="The colon fails first where two territories meet: the splenic flexure (Griffiths) and the rectosigmoid (Sudeck). A hypotensive patient with bloody diarrhoea and ulcers at the splenic flexure has ischaemic colitis.",
)

L['MES-03'] = dict(
  sub="Mesenteric ischaemia → Physiology → Splanchnic flow and oxygen",
  step=2,
  intro="Step 2 explains why the gut can tolerate a big fall in flow for a while and why, when it finally fails, the mucosa goes first.",
  parts=[
    ('a', "**10–35% of cardiac output, rising after a meal.** Published figures sit in this range: about 25% of resting and 35% of post-prandial output to the splanchnic bed (Oldenburg 2004), about 30% to the hepatosplanchnic circulation as a whole (Ackland 2000). The bed is a large, adjustable reservoir; in shock the sympathetic system shuts it down early to protect the brain and heart, which is the root of non-occlusive ischaemia."),
    ('b', "**Extraction is low at rest, so a 50% fall in flow is tolerated before oxygen delivery suffers.** The gut normally takes only a small share of the oxygen delivered, so it can raise extraction a long way before consumption falls. In the experimental model in which SMA inflow alone is restricted, mucosal pH falls only once flow is below about half of baseline; in real hypovolaemia, with sympathetic and hormonal vasoconstriction added, supply dependency can start after a smaller fall (Ackland 2000)."),
    ('c', "**Ischaemic injury does not begin until MAP is under 45 mmHg.** This figure comes from the notes; no primary source for it could be traced, so treat it as approximate. Its point is that intestinal autoregulation holds flow over a wide range of pressure, while atheroma, vasopressors and raised intra-abdominal pressure all make the gut fail at a higher MAP."),
    ('d', "**A 75% reduction in flow is tolerated for up to 12 hours, by raising extraction and opening collaterals.** This is the classical figure in reviews of AMI, attributed to collateral flow; it is the time window that makes early diagnosis worthwhile."),
    ('e', "**The colon has less flow than small bowel, but its epithelium is more resistant.** So colonic ischaemia is common in low flow yet usually mucosal and reversible (MES-08)."),
  ],
  mimic=[
    ("Mucosa vs serosa", "The villus tip is hypoxic first: arterioles and venules run side by side in the villus, so oxygen shunts across before reaching the tip (counter-current exchange). The serosa survives longest, which is why the outside of the bowel can look viable while the mucosa is dead."),
  ],
  traps=[
    ("“A normal blood pressure excludes gut ischaemia”", "Vasoconstriction in shock and vasopressors cut splanchnic flow while the MAP is maintained."),
  ],
  decode=[
    ("Which layer of the bowel is most vulnerable to ischaemia, and why? [pattern]", "The mucosa (villus tips): high metabolic demand and counter-current oxygen exchange."),
  ],
  punch="The gut can lose half its flow, and survive a 75% fall for hours, by extracting more oxygen; but the villus tip is hypoxic first, so the mucosa dies while the serosa still looks pink.",
)

L['MES-04'] = dict(
  sub="Mesenteric ischaemia → Physiology → Ischaemia and reperfusion",
  step=2,
  intro="Step 2 ends with the second injury: what happens when blood comes back. This is why revascularisation in theatre or the angiography suite is followed by a dangerous hour in the ICU.",
  parts=[
    ('a', "**Ischaemic phase: ATP depletion; tight junctions fail; membrane pumps fail.** Without ATP the Na⁺/K⁺ pump stops, cells swell, and the junctions that seal the epithelium open."),
    ('b', "**Consequence: raised mucosal permeability and bacterial translocation.** Bacteria and endotoxin cross into the portal blood and lymph, which feeds sepsis and multi-organ failure even before infarction."),
    ('c', "**Enzyme of reperfusion injury: xanthine oxidase, generating oxygen free radicals.** During ischaemia ATP breaks down to hypoxanthine and xanthine dehydrogenase is converted to xanthine oxidase. When oxygen returns, xanthine oxidase uses it on the accumulated hypoxanthine and produces superoxide. The gut mucosa is rich in this enzyme, so its reperfusion injury is severe."),
    ('d', "**Systemic effects: toxic products, pro-inflammatory cytokines and activated neutrophils cause distant organ injury.** The lung is the commonest distant target (ARDS), then the kidney and the heart."),
    ('e', "**After revascularisation expect hyperkalaemia, acidosis and haemodynamic instability.** The ischaemic bowel’s venous blood, rich in potassium, lactate and mediators, is washed into the circulation at once; be ready with calcium, bicarbonate, vasopressors and possibly dialysis."),
  ],
  mimic=[
    ("Reperfusion syndrome vs ongoing infarction", "Reperfusion: abrupt hyperkalaemia, acidosis and hypotension at the moment flow returns. Ongoing infarction: lactate and sepsis keep rising over hours; look for dead bowel at the second look."),
  ],
  traps=[
    ("“Restoring flow ends the injury”", "Reperfusion adds a free-radical and inflammatory injury of its own, locally and in distant organs."),
  ],
  decode=[
    ("Enzyme responsible for reperfusion injury in the gut? [pattern]", "Xanthine oxidase."),
    ("Immediately after SMA revascularisation the patient becomes hypotensive with a high potassium — why? [pattern]", "Washout of ischaemic venous blood: potassium, acid and mediators."),
  ],
  punch="Ischaemia opens the mucosal barrier; reperfusion then turns xanthine oxidase loose on oxygen. Expect potassium, acid and hypotension the moment flow returns.",
)

L['MES-05'] = dict(
  sub="Mesenteric ischaemia → Types → Classification",
  step=3,
  intro="Step 3 sorts the disease into its causes, because each cause has a different patient, a different pain and a different treatment.",
  parts=[
    ('a', "**Intestinal ischaemia is mesenteric (acute or chronic) or colonic; acute mesenteric ischaemia is arterial or venous.** Colonic ischaemia is a different disease: commoner, milder, usually non-occlusive and mostly self-limiting (MES-08)."),
    ('b', "**Arterial embolism 25–50%: atrial fibrillation, valve disease, endocarditis, LV aneurysm.** The classical largest group; recent series put it lower, at about 25% (WSES 2022)."),
    ('c', "**Arterial thrombosis 15–40%: atherosclerosis; prior post-prandial pain.** Thrombus forms on an ostial plaque that has often caused chronic symptoms; its share is rising with an ageing population (WSES 2022: up to 40%)."),
    ('d', "**Non-occlusive 20–25%: shock, high-dose vasopressors, cardiac surgery, dialysis.** Vessels are open but in spasm; this is the ICU type, with the worst outcome (mortality about 70%, ESVS 2025)."),
    ('e', "**Venous thrombosis under 10%: thrombophilia, cirrhosis, pancreatitis, malignancy.** Outflow block causes congestion, oedema and haemorrhagic infarction, usually more slowly."),
  ],
  mimic=[
    ("Acute mesenteric vs colonic ischaemia", "AMI: small bowel, a clear precipitant, severely ill, CTA. Colonic: elderly, usually no precipitant, bloody diarrhoea, colonoscopy (MES-08)."),
  ],
  traps=[
    ("“Mesenteric venous thrombosis is the commonest type”", "It is the least common, under 10%."),
  ],
  decode=[
    ("Commonest type of acute mesenteric ischaemia? [pattern]", "Arterial embolism classically; recent series put thrombosis close to or above it."),
  ],
  punch="Embolism, thrombosis, non-occlusive spasm and venous thrombosis, roughly in falling order of frequency; non-occlusive disease is the ICU’s own and the deadliest.",
)

L['MES-06'] = dict(
  sub="Mesenteric ischaemia → Types → Risk factors and history",
  step=3,
  intro="Step 3 continues with the clues in the history. Five real questions hang on this card: two DocT GTs put AF and sudden pain together, one put bloody stools after high-dose noradrenaline, one asked which listed factor is NOT a cause of non-occlusive ischaemia (30% right), and Marrow asked the chronic triad.",
  parts=[
    ('a', "**Most emboli come from the heart; 17% have thrombus on the proximal aortic wall.** Left atrial appendage thrombus in atrial fibrillation is the usual source, then mural thrombus after MI or in an LV aneurysm, and vegetations. Some arise from thrombus in the aorta itself. The card’s 17% figure for proximal aortic thrombus could not be traced to a primary source: the main autopsy series (Acosta 2005, 213 patients) found an embolic source in 80% and residual cardiac thrombus in 48%, and reported aortic wall thrombosis only as a borderline association with thrombotic, not embolic, occlusion. A patient with an SMA embolus often has emboli elsewhere (limbs, kidneys, spleen) at the same time."),
    ('b', "**Patient factors: advanced age, atherosclerosis, smoking, atrial fibrillation.** AF with sudden severe pain is the commonest exam picture of embolic disease."),
    ('c', "**ICU settings: after abdominal vascular surgery (especially ruptured aortic aneurysm), bowel obstruction, high-dose vasopressors.** Non-occlusive ischaemia follows anything that makes the splanchnic bed constrict: shock of any kind, cardiogenic shock and acute MI, cardiac surgery on bypass, cardiac arrest, haemodialysis with fluid removal, burns, high-dose vasopressors, digoxin and cocaine. Aortic surgery is different: tying off the IMA, plus the shock of rupture, causes ischaemic colitis of the left colon rather than non-occlusive small bowel ischaemia."),
    ('d', "**Post-prandial pain, weight loss and food aversion point to thrombosis: chronic mesenteric ischaemia.** Eating raises gut demand that a narrowed artery cannot meet, so pain comes 15–60 minutes after food, the patient eats less and loses weight. An abdominal bruit may be heard. Acute thrombosis on such a plaque is ‘acute on chronic’ disease."),
    ('e', "**Venous thrombosis: a personal or family history of DVT or PE in 50%.** Ask about previous clots, oestrogen, cirrhosis, pancreatitis and cancer; a thrombophilia screen is part of the work-up."),
  ],
  mimic=[
    ("AMI vs perforated ulcer, pancreatitis or ruptured aneurysm", "Perforation and pancreatitis give guarding early; a ruptured AAA gives back pain, a mass and collapse. AMI gives severe pain with a soft abdomen."),
    ("NOMI vs embolism in a septic patient", "Embolism needs a source (AF, new irregular rhythm) and starts suddenly; NOMI follows high-dose vasopressors or low flow, often after the shock has settled."),
  ],
  traps=[
    ("“Aorto-bifemoral bypass is a cause of NOMI”", "It is the exception: it causes ischaemic colitis because the IMA is sacrificed. Burns, haemodialysis and acute MI all cause NOMI through low splanchnic flow. Only 30% got this on DocT GT."),
    ("“Bloody stools and distension after sepsis mean C. difficile or an embolus”", "High-dose noradrenaline, a regular rhythm and onset as the shock settles point to NOMI (71% right on DocT GT)."),
    ("“Severe pain with minimal tenderness in AF is pancreatitis or a perforated ulcer”", "Pain out of proportion to the findings is AMI until proved otherwise (77–89% right)."),
  ],
  decode=[
    ("Which is NOT a risk factor for NOMI — aorto-bifemoral bypass, haemodialysis, acute MI, burns? [DocT GT]", "Aorto-bifemoral bypass (30% right)."),
    ("AF, ICU day 2 with sepsis, severe diffuse pain, minimal tenderness, raised lactate — diagnosis? [DocT GT]", "Acute mesenteric ischaemia (77% and 89% right)."),
    ("Septic shock on high-dose noradrenaline, weaned 12 h ago, now pain, distension, bloody stools, regular rhythm — diagnosis? [DocT GT]", "Non-occlusive mesenteric ischaemia (71% right)."),
    ("Post-prandial pain, weight loss, abdominal bruit? [Marrow]", "Chronic mesenteric ischaemia."),
  ],
  punch="AF and sudden pain mean embolism; post-prandial pain and weight loss mean thrombosis; shock and vasopressors mean NOMI; prior clots mean venous thrombosis. Aortic surgery causes ischaemic colitis, not NOMI.",
)

L['MES-07'] = dict(
  sub="Mesenteric ischaemia → Types → Pain by type",
  step=3,
  intro="Step 3 turns to the pain, the one clue present early. The real question gives the classic picture, pain out of proportion in AF, and asks for the test.",
  parts=[
    ('a', "**Embolic: sudden, severe, periumbilical, with vomiting and bowel emptying.** The block is complete and abrupt, with no collaterals ready; the gut contracts violently (vomiting, diarrhoea) while the abdomen is still soft."),
    ('b', "**Thrombotic: worsening post-prandial pain, then as embolic.** Collaterals have developed over years, so the final occlusion may be less dramatic, but the history of pain after food gives it away."),
    ('c', "**Venous: waxing and waning over days; hard to diagnose.** Congestion builds slowly; patients often present after several days of vague pain, sometimes with GI bleeding."),
    ('d', "**Non-occlusive: variable in site and severity; often masked by sedation.** In the ventilated patient the clues are feed intolerance, distension, rising lactate or vasopressor need, and GI bleeding."),
    ('e', "**Colonic: mild, left-sided, tender; bloody diarrhoea within 24 hours.** The mucosa sloughs early, so bleeding comes quickly, unlike small bowel ischaemia."),
  ],
  mimic=[
    ("Early vs late AMI", "Early: pain out of proportion, soft abdomen. Late: guarding, rigidity, shock — transmural infarction; peritonism means dead bowel."),
  ],
  traps=[
    ("“A soft abdomen makes serious pathology unlikely”", "In AMI the visceral pain precedes peritoneal signs by hours; a soft abdomen with severe pain is the warning."),
    ("“The plain film is the first test”", "It is normal early and is not recommended (WSES 1B); go to CT angiography."),
  ],
  decode=[
    ("AF, severe pain disproportionate to examination, raised lactate — most sensitive early test? [DocT GT]", "CT angiography."),
    ("Sedated ICU patient with rising vasopressor need, distension and feed intolerance after shock — suspect? [pattern]", "Non-occlusive mesenteric ischaemia."),
  ],
  punch="Pain out of proportion to a soft abdomen is acute mesenteric ischaemia until CT angiography says otherwise; by the time there is peritonism the bowel is dead.",
)

L['MES-08'] = dict(
  sub="Mesenteric ischaemia → Types → Small bowel vs colonic ischaemia",
  step=3,
  intro="Step 3 closes by separating the two diseases that share the word ischaemia. They differ in who gets them, how ill the patient looks, whether there is blood, and which test confirms them. Five real questions sit here, including a colitis management question that 56% got right.",
  parts=[
    ('a', "**Age: small bowel varies with cause; colon 90% over 60.** Colonic ischaemia is a disease of the elderly with vascular disease, often after a transient fall in flow."),
    ('b', "**Precipitant: typical for small bowel, rare for colon.** AMI usually has a clear source (AF, shock); most colonic ischaemia has no obvious trigger and the vessels are patent."),
    ('c', "**Appearance: small bowel severely ill; colon not severely ill.** The colon tolerates low flow better (MES-03), so most colonic ischaemia is mucosal and settles."),
    ('d', "**Pain and tenderness: small bowel severe pain with little early tenderness; colon mild pain with tenderness present.** Colonic disease is tender over the affected segment from the start."),
    ('e', "**Bleeding: small bowel uncommon until late; colon rectal bleeding and bloody diarrhoea.** Colonic mucosa sloughs early and the blood reaches the rectum quickly."),
    ('f', "**Test of choice: small bowel CT angiography; colon colonoscopy.** ACG 2015 uses CT (IV and oral contrast) as the first imaging in suspected colonic ischaemia, to show the segment and exclude other causes, and colonoscopy within 48 hours to confirm it: segmental oedema, pale or dusky mucosa, the single-stripe sign. Avoid colonoscopy with peritonitis or gangrene. Barium enema is contraindicated: it risks perforation and spoils later imaging."),
  ],
  mimic=[
    ("Left-sided vs isolated right colon ischaemia", "Right-sided colonic ischaemia shares the SMA supply and may herald AMI; ACG says do CT angiography and treat it as more severe."),
  ],
  traps=[
    ("“Colitis on CT with bloody diarrhoea: stool cultures and IV antibiotics are enough”", "In an elderly ICU patient with colonic wall thickening the BEST confirming step is colonoscopy, with decompression and antibiotics; only 56% chose it on DocT GT."),
    ("“Colonic ischaemia needs laparotomy”", "Most settle with supportive care; surgery is for peritonitis, gangrene, pneumatosis or failure to improve."),
    ("“CT angiography is the test of choice for colonic ischaemia”", "Colonoscopy confirms it; CTA is for AMI and for right-sided disease (MES-16 e)."),
  ],
  decode=[
    ("Elderly COPD patient with pneumonia, blood-tinged diarrhoea, colonic wall thickening on CT — best way to confirm and begin treatment? [DocT GT]", "Nasogastric decompression, IV antibiotics and urgent colonoscopy (56% right)."),
    ("Hypotensive ICU patient, bloody diarrhoea, linear ulcers at the splenic flexure? [DocT QBank]", "Ischaemic colitis (34% right)."),
    ("AF, severe diffuse pain, minimal tenderness, raised lactate — diagnosis / most sensitive early test? [DocT GT]", "Acute mesenteric ischaemia (77–89% right) / CT angiography."),
  ],
  punch="Small bowel ischaemia: a very sick patient, severe pain, no blood, CT angiography. Colonic ischaemia: an older, less sick patient, mild left-sided tenderness, early bloody diarrhoea, colonoscopy.",
)

L['MES-09'] = dict(
  sub="Mesenteric ischaemia → Diagnosis → Laboratory tests",
  step=4,
  intro="Step 4 opens with the blood tests, mainly to show why none of them can be used to decide.",
  parts=[
    ('a', "**D-lactate: sensitivity 90%, specificity 40%.** Made by gut bacteria and absorbed when the mucosa breaks down; not measured by the usual lactate analyser. A later meta-analysis (Treskes 2017) found about 72% and 74%."),
    ('b', "**L-lactate: 86% and 44%.** The ordinary lactate rises from all hypoperfused tissue, so it is non-specific, and it rises late, with transmural infarction, because the portal blood is cleared by the liver until the liver is overwhelmed."),
    ('c', "**D-dimer: 96% and 40%.** Highly sensitive but non-specific. ESVS 2017 allowed a normal D-dimer to rule AMI out; ESVS 2025 no longer does: no single lactate or D-dimer may confirm or exclude it."),
    ('d', "**Glutathione S-transferase: 68% and 85%.** An enzyme released from damaged enterocytes; a research test."),
    ('e', "**Intestinal fatty acid-binding protein: 70% and 93%.** The most specific blood marker, released from the villus tips; still not accurate or available enough to decide (meta-analytic figures about 75–79% and 79–91%)."),
    ('f', "**Multidetector CT: 94% and 95%.** The comparison that matters: imaging is far better than any blood test, which is why the next step is CT angiography (MES-11)."),
  ],
  mimic=[
    ("D-lactate vs L-lactate", "D-lactate is bacterial and gut-specific but needs a special assay; L-lactate is the ordinary analyser lactate, from any hypoperfused tissue."),
  ],
  traps=[
    ("“A normal lactate rules out AMI”", "Lactate rises late; a normal value early means nothing."),
    ("“A normal D-dimer excludes it”", "ESVS 2025 explicitly withdrew that advice."),
  ],
  decode=[
    ("Most sensitive / most specific blood marker for AMI? [pattern]", "D-dimer / I-FABP; neither is used to decide."),
  ],
  punch="D-dimer is sensitive but non-specific, I-FABP specific but insensitive, and lactate late; no blood test confirms or excludes AMI, and CT does both.",
)

L['MES-10'] = dict(
  sub="Mesenteric ischaemia → Diagnosis → Gastrointestinal tonometry",
  step=4,
  intro="Step 4 then looks at the one bedside measure of gut perfusion. It is rarely used, but three DocT GTs asked what a rising regional PCO₂ means in abdominal compartment syndrome.",
  parts=[
    ('a', "**Principle: ischaemic tissue makes lactic acid; local bicarbonate buffers it, releasing CO₂.** The other half of the story is flow: when flow falls, the CO₂ that tissue produces is not washed away, so mucosal PCO₂ rises above arterial PCO₂. The regional-to-arterial gap therefore tracks how poorly the mucosa is perfused."),
    ('b', "**Measurement: CO₂ diffuses freely, so luminal PCO₂ = mucosal PCO₂, measured with a balloon-tipped catheter.** The balloon sits in the stomach (or jejunum); saline or air in it equilibrates with the mucosa and its PCO₂ (PrCO₂) is read."),
    ('c', "**Normal: gastric-to-arterial PCO₂ gap under 0.9 kPa (7 mmHg); jejunum 1.4 kPa.** A widening gap means mucosal hypoperfusion before lactate rises elsewhere. Cut-offs depend on the method (saline or air tonometry, fasting, acid suppression): the Dutch tonometry group uses 0.8 kPa as the upper limit of normal for the gastric–arterial gradient after exercise (Mensink 2006), close to the card’s 0.9 kPa; the jejunal 1.4 kPa figure could not be confirmed from a primary source."),
    ('d', "**Your notes describe it as the only valid test for detecting GI ischaemia.** The tonometry literature says much the same: gastric (or sigmoid) tonometry is the only functional test proven to detect ischaemia while it is still reversible (Mensink 2006), and its main use now is in chronic mesenteric ischaemia work-up. It is rarely used in the ICU: slow to equilibrate, and falsely raised by feeds and by acid (gastric acid meeting bicarbonate releases CO₂, so acid suppression is needed)."),
  ],
  mimic=[
    ("Rising PrCO₂ vs rising PaCO₂", "PrCO₂ is the gut’s own CO₂; it rises with local low flow even when arterial PCO₂ is unchanged, so it is the gap that matters."),
  ],
  traps=[
    ("“In abdominal compartment syndrome with worsening hypoxia, rising PrCO₂ means pulmonary embolism”", "PrCO₂ is gastric or intestinal mucosal CO₂: it means gut ischaemia. The hypoxia comes from the high abdominal pressure splinting the diaphragm (69–77% right)."),
    ("“A raised PrCO₂ reflects renal ischaemia or metabolic alkalosis”", "It is a gut measurement; alkalosis would not raise it."),
  ],
  decode=[
    ("Ventilated patient with abdominal compartment syndrome, rising PrCO₂ and worsening hypoxia despite resuscitation — what does PrCO₂ indicate? [DocT GT, three tests]", "Gut ischaemia (69% and 77% right)."),
  ],
  punch="Tonometry reads the mucosa’s own CO₂: when gut flow falls, CO₂ is not washed out and the regional-to-arterial gap widens. A rising PrCO₂ means gut ischaemia.",
)

L['MES-11'] = dict(
  sub="Mesenteric ischaemia → Diagnosis → Imaging",
  step=4,
  intro="Step 4 reaches the test that decides. Four real questions sit here: two ask the test of choice, one asks what portal venous gas means, and one asks to name gas in the bowel wall.",
  parts=[
    ('a', "**Plain film: ileus, wall thickening; pneumatosis intestinalis (late, transmural infarction).** It is normal early and is not recommended for diagnosis (WSES 1B). Gas in the bowel wall means the mucosa has broken down and gas-forming bacteria have entered: in ischaemia that is transmural infarction."),
    ('b', "**Doppler ultrasound: limited by gas and distal occlusions.** Useful for proximal stenosis in chronic disease, not in the acute distended abdomen."),
    ('c', "**Test of choice: biphasic CT angiography, sensitivity 94%, specificity 95%.** The arterial phase shows emboli and thrombosis; the portal venous phase shows venous thrombosis and how the bowel wall enhances. ESVS 2025: urgent CTA in arterial and venous phases, regardless of renal function."),
    ('d', "**No oral contrast: it hides vessels and wall enhancement.** Dense luminal contrast hides mucosal enhancement and delays the scan; WSES calls it ‘not indicated and even harmful’. The exception is suspected colonic ischaemia, where ACG 2015 uses CT with IV and oral contrast to show the affected segment (MES-08)."),
    ('e', "**CT signs: arterial filling defect, non-enhancing or thick wall, dilatation, pneumatosis with portal venous gas.** A non-enhancing thin wall is arterial infarction; a thick, oedematous wall suggests venous congestion or reperfusion. Pneumatosis with portal venous gas means transmural infarction, mortality about 75–85%, and is a near-universal indication for laparotomy."),
    ('f', "**Normal CT but high suspicion: catheter angiography (DSA), especially for non-occlusive disease.** In NOMI the trunk is open; DSA shows the beaded, pruned spasm of the branches and lets papaverine be infused at once (MES-15)."),
    ('g', "**Peritonitis: no imaging, laparotomy.** Peritonism means dead bowel; imaging only delays the operation."),
  ],
  mimic=[
    ("Pneumatosis vs portal venous gas", "Pneumatosis is gas in the bowel wall; portal venous gas branches to the periphery of the liver. Biliary gas (pneumobilia) stays central, near the hilum."),
  ],
  traps=[
    ("“Portal venous gas means mesenteric venous thrombosis, or early reversible ischaemia”", "It means transmural infarction with high mortality and urgent laparotomy (72% right on DocT GT); it is not specific for venous disease."),
    ("“Hold the CT contrast because the creatinine is raised”", "Do the CTA: delay kills bowel, contrast rarely harms the kidney (ESVS 2025, WSES 2022)."),
    ("“Duplex ultrasound first because it avoids contrast”", "Gas and distal occlusions defeat it; CTA is the test (Marrow)."),
  ],
  decode=[
    ("Portal venous gas in suspected AMI — implication? [DocT GT]", "Transmural infarction, high mortality, near-universal need for urgent surgery (72% right)."),
    ("Severe colitis, progressive pancolonic dilatation with intramural gas — imaging diagnosis? [DocT GT]", "Pneumatosis intestinalis."),
    ("Sudden pain out of proportion, new AF — confirmatory test? [Marrow]", "CT angiography."),
    ("Crohn’s with antiphospholipid syndrome, severe pain, rising lactate — next step? [Marrow]", "Biphasic CT mesenteric angiography."),
  ],
  punch="Suspect AMI, scan at once with biphasic CT angiography, no oral contrast, whatever the creatinine. Pneumatosis with portal venous gas means dead bowel, and peritonitis goes to theatre without a scan.",
)

L['MES-12'] = dict(
  sub="Mesenteric ischaemia → Management → General measures",
  step=5,
  intro="Step 5 begins with what every patient gets while the definitive treatment is arranged.",
  parts=[
    ('a', "**Initial measures: fluids, haemodynamic monitoring, nasogastric decompression, broad-spectrum antibiotics.** Fluids restore splanchnic flow; decompression lowers wall tension and intraluminal pressure; antibiotics cover the translocation that starts early (WSES 1B and 1C)."),
    ('b', "**Avoid vasopressors (vasopressin, high-dose noradrenaline) and digitalis.** Vasopressin is a powerful splanchnic constrictor (which is why it lowers portal pressure); digoxin directly constricts mesenteric vessels. If a vasopressor is unavoidable, WSES prefers noradrenaline with dobutamine to vasopressin."),
    ('c', "**If an inotrope is needed: dobutamine, low-dose dopamine, milrinone, which have the least effect on mesenteric flow.** They raise cardiac output without constricting the splanchnic bed, and milrinone dilates it."),
    ('d', "**Anticoagulation: weight-based unfractionated heparin, for arterial occlusion, venous thrombosis and non-occlusive disease.** It stops thrombus propagating into collaterals and the microcirculation; UFH is chosen because it is short-acting, reversible before theatre and safe in kidney injury."),
    ('e', "**Withhold it for bleeding, as in colonic ischaemia.** Where the mucosa is sloughing and bleeding, heparin adds harm without treating a thrombus."),
    ('f', "**Pain: parenteral opioids.** Analgesia does not mask the diagnosis; the decision rests on CT."),
  ],
  mimic=[
    ("Inodilators vs vasopressors in AMI", "Dobutamine and milrinone raise output and open the splanchnic bed; vasopressin and high-dose noradrenaline close it."),
  ],
  traps=[
    ("“Digoxin is useful for rate control in NOMI”", "It constricts the mesenteric bed; avoid it (MES-16 f)."),
  ],
  decode=[
    ("Inotrope with the least effect on mesenteric flow? / drugs to avoid in NOMI? [pattern]", "Dobutamine, low-dose dopamine, milrinone / vasopressin, high-dose noradrenaline, digoxin."),
  ],
  punch="Resuscitate, decompress, give antibiotics and heparin, and keep the splanchnic bed open: inodilators yes, vasopressin and digoxin no.",
)

L['MES-13'] = dict(
  sub="Mesenteric ischaemia → Management → By cause and by peritonitis",
  step=5,
  intro="Step 5 then sets out the decision that matters most: is there peritonitis? It decides between the angiography suite and the operating theatre. The one real question (Marrow) is about an intussusception, but tests the same rule.",
  parts=[
    ('a', "**No peritonitis: embolism by endovascular aspiration or open embolectomy; thrombosis by endovascular stenting or bypass.** Embolus is soft and fresh, so it can be aspirated or pulled out; thrombosis sits on a plaque that must be stented or bypassed. ESVS 2025 makes endovascular repair first-line for both (IIa)."),
    ('b', "**Peritonitis, stable: laparotomy, with surgical embolectomy and resection of dead bowel (embolism) or retrograde open stenting or bypass (thrombosis).** Revascularise first, then judge viability, because bowel that looks doubtful often recovers once flow returns."),
    ('c', "**Peritonitis with septic shock: damage-control surgery with exploration of the artery, plus stenting or bypass.** Resect only clearly dead bowel, leave it in discontinuity, close temporarily and come back in 24–48 hours for a second look."),
  ],
  mimic=[
    ("Endovascular vs open in AMI", "No peritonitis: endovascular first. Peritonitis: open, because dead bowel has to be seen and removed."),
  ],
  traps=[
    ("“Get a CT angiogram first in an obstructed patient with sepsis signs”", "Obstruction (including adult intussusception) with fever, tachycardia and pain out of proportion means threatened bowel: emergency surgery (Marrow)."),
    ("“Stenting is first-line even with peritonitis”", "Endovascular repair has no role once peritonitis is present (MES-16 g)."),
  ],
  decode=[
    ("70-year-old, intussusception on CT, fever, tachycardia, pain out of proportion — next? [Marrow]", "Emergency surgery."),
    ("Embolic SMA occlusion without peritonitis — first-line? [pattern]", "Endovascular aspiration (or open embolectomy)."),
  ],
  punch="Peritonitis decides the route: without it, revascularise endovascularly; with it, open the abdomen, restore flow first, resect only dead bowel and come back for a second look.",
)

L['MES-14'] = dict(
  sub="Mesenteric ischaemia → Management → Open vs endovascular",
  step=5,
  intro="Step 5 continues with the evidence behind endovascular-first. It is observational, and the comparison is of different patients.",
  parts=[
    ('a', "**Data: a 5-year retrospective of 23,744 patients.** This is Beaulieu 2014 (US Nationwide Inpatient Sample, 2005–2009). 23,744 was the number of AMI admissions; only 679 were revascularised, and the comparison is between those."),
    ('b', "**75.7% open, 24.3% endovascular.** The endovascular share rose over the five years of the study, and ESVS 2025 now makes endovascular repair first-line where there is no peritonitis (MES-13)."),
    ('c', "**Mortality 25% vs 40%, favouring endovascular.** Exactly 24.9% vs 39.3%. The patients were not randomised: those with peritonitis needed laparotomy and were sicker, so part of the gap is selection."),
    ('d', "**Bowel resection after endovascular repair: 14.4%.** Against 33.4% after open repair; TPN was also less often needed (13.7% vs 24.4%)."),
    ('e', "**Suitable: only patients who do not need emergency laparotomy.** That is, no peritonitis. In ICU-acquired AMI the outlook is far worse: a Belgian series of 214 had 71% 30-day mortality, and revascularisation was possible in only about 8%."),
  ],
  mimic=[
    ("Endovascular-first vs open-first patient", "No peritonitis and stable: endovascular. Peritonitis: laparotomy, with open or hybrid revascularisation."),
  ],
  traps=[
    ("“The 23,744 patients were randomised between open and endovascular repair”", "It was administrative data; 679 were revascularised and none were randomised."),
  ],
  decode=[
    ("Mortality of endovascular vs open revascularisation for AMI in the NIS study? [pattern]", "About 25% vs 39%."),
  ],
  punch="Endovascular repair in selected patients without peritonitis halves bowel resection and lowers mortality to about a quarter, but the data are observational and ICU-acquired disease still kills most patients.",
)

L['MES-15'] = dict(
  sub="Mesenteric ischaemia → Management → Thrombotic, venous and non-occlusive disease",
  step=5,
  intro="Step 5 finishes with the three causes that are not simple emboli. The two linked DocT GTs are about recognising non-occlusive disease: who gets it, and the patient weaned off noradrenaline who then bleeds.",
  parts=[
    ('a', "**Thrombotic: antegrade bypass from the supracoeliac aorta to beyond the occlusion; endarterectomy if disease is confined to the origin.** The supracoeliac aorta is usually free of atheroma and gives a short, straight graft with good flow. In the emergency, retrograde bypass from the iliac artery or retrograde open stenting (ESVS 2025, IIb) is quicker and avoids a supracoeliac clamp in an unstable patient; without peritonitis, endovascular stenting comes first."),
    ('b', "**Graft: saphenous vein; avoid PTFE in a contaminated field.** If bowel is resected or perforated, prosthetic material risks infection."),
    ('c', "**Venous thrombosis: anticoagulation and stabilisation; resect only for infarction.** Heparin stops the clot extending and most recover; thrombolysis or thrombectomy is reserved for those who deteriorate on heparin (ESVS 2025, IIb)."),
    ('d', "**Anticoagulation for at least 3–6 months; lifelong with thrombophilia.** ESVS 2025: 3–6 months of a VKA or LMWH (Class I), DOAC as an alternative (IIb), indefinite if idiopathic or a permanent risk factor (Class I)."),
    ('e', "**Non-occlusive: restore flow — fluids, treat heart failure and arrhythmia, stop vasoconstrictors.** The vessels are open but in spasm, so the treatment is the cause of the low flow. If NOMI accompanies abdominal compartment syndrome, decompression laparotomy is recommended (ESVS 2025)."),
    ('f', "**Non-occlusive vasodilator: intra-arterial papaverine or nitroglycerine through the angiography catheter.** Infused into the SMA, it relaxes the spasm locally without dropping the systemic pressure; ESVS 2025 allows papaverine or prostaglandin (IIb). Mortality is still about 70%."),
  ],
  mimic=[
    ("NOMI vs ischaemic colitis after aortic surgery", "NOMI: low-flow small bowel ischaemia, shock or vasopressors. After aorto-bifemoral or aneurysm surgery: left colon ischaemia from IMA loss."),
  ],
  traps=[
    ("“Aorto-bifemoral bypass, like burns and dialysis, predisposes to NOMI”", "It causes ischaemic colitis, not NOMI (30% right)."),
    ("“Bloody stools once vasopressors are weaned exclude a vasopressor cause”", "NOMI often declares itself after the shock has settled, when the injured mucosa sloughs (71% right)."),
  ],
  decode=[
    ("Which is NOT a risk factor for NOMI? [DocT GT]", "Infrarenal aorto-bifemoral bypass (30% right)."),
    ("Sepsis on high-dose noradrenaline, now weaned; pain, distension, bloody stools, small bowel air-fluid levels — diagnosis? [DocT GT]", "Non-occlusive mesenteric ischaemia (71% right)."),
  ],
  punch="Thrombosis needs a bypass or a stent; venous thrombosis needs heparin and months of anticoagulation; NOMI needs flow restored, vasoconstrictors stopped and papaverine into the SMA.",
)

L['MES-16'] = dict(
  sub="Mesenteric ischaemia → Review → True or false",
  step=5,
  intro="Step 5 ends with a sweep of the deck’s commonest errors.",
  parts=[
    ('a', "**False: Sudeck’s point is the rectosigmoid; Griffiths’ is the splenic flexure.** (MES-02)"),
    ('b', "**False: lactate rises late.** It rises with transmural infarction, so a normal value early does not exclude AMI (MES-09)."),
    ('c', "**False: oral contrast obscures the vessels.** It hides mucosal enhancement and delays the scan (MES-11)."),
    ('d', "**True: pneumatosis is a late sign.** It means transmural infarction, especially with portal venous gas."),
    ('e', "**False: colonoscopy is the test of choice for colonic ischaemia.** CT is the first imaging and CTA is needed for right-sided disease, but colonoscopy confirms it (MES-08)."),
    ('f', "**False: avoid digoxin in non-occlusive ischaemia.** It constricts the mesenteric bed (MES-12)."),
    ('g', "**False: stenting has no role with peritonitis.** Peritonitis means laparotomy (MES-13)."),
    ('h', "**True: venous thrombosis is treated mainly with heparin.** UFH or LMWH first line; surgery only for infarction (MES-15)."),
  ],
  mimic=[
    ("Griffiths’ point vs Sudeck’s point", "Griffiths: splenic flexure, SMA–IMA join. Sudeck: rectosigmoid, sigmoid–superior rectal join."),
  ],
  traps=[
    ("“A normal D-dimer still rules out AMI”", "ESVS 2025 no longer accepts it (MES-09)."),
  ],
  decode=[
    ("True/false sweep: watershed names, lactate timing, oral contrast, colonic test, digoxin, stenting with peritonitis [pattern]", "Rectosigmoid is Sudeck; lactate late; no oral contrast; colonoscopy; avoid digoxin; no stenting with peritonitis."),
  ],
  punch="Lactate is late, oral contrast hides the answer, digoxin and vasopressin constrict the gut, and peritonitis means laparotomy, not a stent.",
)

FLAGS = {
  'MES-14': "a: ‘23,744 patients’ were all AMI admissions in the NIS 2005–2009 (Beaulieu, J Vasc Surg 2014); only 679 were revascularised (514 open, 165 endovascular), and the 75.7/24.3%, 24.9 vs 39.3% mortality and 14.4% (vs 33.4%) resection figures refer to those 679. The explanation says so.",
  'MES-09': "a and e: figures vary by source. The Cudnik 2013 meta-analysis confirms D-dimer 96/40, L-lactate 86/44 and CT 94/95; the Treskes 2017 meta-analysis gives D-lactate about 72/74 (card 90/40) and I-FABP 75–79/79–91 (card 70/93). The explanation keeps the card’s figures and notes the later ones.",
  'MES-15': "a: antegrade supracoeliac bypass is the classic operation for elective chronic disease; in the acute setting ESVS 2025 prefers endovascular stenting first and retrograde open mesenteric stenting (or retrograde iliac bypass) at laparotomy. The explanation adds this.",
  'MES-06': "a: the ‘17% have thrombus on the proximal aortic wall’ figure could not be traced. The largest autopsy series of SMA thromboembolism (Acosta, Ann Surg 2005; 213 patients) gives an embolic source in 80% and residual cardiac thrombus in 48%, and reports aortic wall thrombosis only as a borderline association (P = 0.08) with thrombotic, not embolic, occlusion. Treat the 17% as unverified; the explanation says so.",
  'MES-10': "c: the gastric gap of 0.9 kPa (7 mmHg) is close to the published upper limit (0.8 kPa after exercise; Mensink/Kolkman, Erasmus 2006), but the jejunal 1.4 kPa could not be traced, and cut-offs vary with method. Unverified rather than wrong.",
  'MES-03': "c: ‘ischaemic injury not until MAP is under 45 mmHg’ could not be traced to a primary source; a (10–35%) is wider at the lower end than the usual 25% resting / 35% post-prandial (Oldenburg 2004). Unverified, not shown wrong; the explanation softens c.",
}
