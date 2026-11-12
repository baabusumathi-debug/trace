# SPECIAL05A — independent review of special05a_learn.py and special05a_topups_learn.py (13 Nov 2026)

Checker: `python3 check_learn.py SPECIAL05A` → `SPECIAL05A 10 cards 10 entries OK`, `v3 spine 6 steps OK`.
Top-ups (no checker) checked by hand: all 10 present; every part starts with the bold restated answer and lines up with the card's answer lines in order; all mimic/trap/decode pairs have 2 items; punches 180–249 characters (limit 320); no banned phrases.

## Changes (card: what was wrong → what it says now; source)

### Factual
- POLY-08 c: "the 11th ATLS edition adds hypocalcaemia" to the lethal triad → "many authors now add hypocalcaemia (the ‘lethal diamond’)", with the citrate mechanism. Not in any ATLS 11 summary I could open (journalfeed, Mayo Clinic, SGEM, Afya); the writer had it from one secondary summary only.
- POLY-09 table: responder bands labelled "ATLS 10th edition" as rapid <20%, transient 20–40% → rapid <15% (10th), transient about 15–40% (10th), with the older 20/20–40% bands noted. Source: ATLS 10th response-to-fluid table as reproduced (anesthetist.org handout citing ACS 2018: minimal <15%, moderate and ongoing 15–40%, severe >40%); 9th-edition bands per tomwademd (ATLS 9th, pp. 72–74). Same finding as the OBS02B review.
- POLY-09 b: "in about a third of bleeding patients a relative bradycardia appears" → "in one large series about 29% of hypotensive trauma patients had a relative bradycardia". Source: Demetriades 1998 (28.9% of hypotensive patients).
- POLY-02: "each physiological criterion on its own carried a mortality of about 35–38%" → "over a third". Source: Pape 2014 (J Trauma Acute Care Surg) results give 35.3–38.8%, with coagulopathy 48.3% in the text vs 38.4% in Table 3, so a narrow range could not be kept.
- POLY-10 (part, trap): "noradrenaline is preferred" in neurogenic shock → "commonly/usually preferred … No guideline names a single agent of choice"; mechanism (β₁ support, reflex bradycardia with phenylephrine) made explicit. No guideline I could find names an agent of choice.
- T_bb4f16eb a: "a normal CXR has a negative predictive value of about 98%" (unsourced) → removed; now "no CXR finding is sensitive enough on its own". Source: MSD Manual, traumatic aortic disruption.
- T_bb4f16eb b: added that common anti-impulse targets are tighter than the card (HR 60–80, SBP ≤100). Source: MSD Manual. FLAG updated.
- T_bb4f16eb c: "arrhythmia almost always shows on the first ECG" and "NPV near 100%" → EAST 2012 wording: normal ECG + normal troponin I rules out BCI; normal ECG with raised troponin needs a monitored bed; echo for instability or persistent new arrhythmia. Source: EAST 2012 BCI guideline PDF.
- T_d82a3b56 c: anterior spinal artery infarct gives "flaccid paraplegia at the level" → "below the level", with dorsal-column sensation preserved. Standard neuroanatomy. FLAG added.
- T_eb298c8d d: "STASCIS found better neurological recovery" → cervical SCI, ≥2-grade AIS improvement 19.8% (<24 h) vs 8.8% (later). Source: Fehlings 2012, PLoS One (STASCIS abstract; OR 2.57).
- T_702a80b1 c: "Head-on collisions are now the commonest cause" → road traffic collisions, which usually add axial loading to hyperextension; hyperextension–distraction is the judicial-hanging mechanism. FLAG added.
- T_403270d5 a: "the first film can be normal" → most contusions visible within about 6 h (CT earlier and better), small ones missed, clearing over about a week. Source: LearningRadiology (contusion "almost always radiographically apparent within 6 hours"). FLAG updated.
- T_25010a36 d: extraperitoneal rupture "heals with drainage" → added the exceptions that need repair (bladder neck, bone fragments, rectal or vaginal injury). Source: MSD Manual, bladder trauma.
- T_8867bce4 a: "the humerus, being closer to the heart, flows faster than the tibia" → human data give about 150–165 mL/min under pressure at both sites, with no consistent humeral advantage, below a large-bore peripheral cannula; card's 16G comparison called generous. Source: BestBETs (Ong 2009: tibia 165, humerus 153 mL/min with pressure bag; Miller 2010 manufacturer abstract). FLAG rewritten.

### Structural / minor
- POLY-01 b: Trunkey's 50/30/20 split labelled "commonly quoted" (the original figure is graphical; Gunst 2010 does not give it numerically).
- POLY-01 c: added Gunst 2010 Dallas County data (61% immediate, 29% early, about 10% late; "bimodal"), which is the source of the card's bimodal claim. Source: Gunst 2010, Proc Bayl Univ Med Cent (PMC2943446).
- T_702a80b1 a: added CCR vs NEXUS specificity (45.1% vs 36.8%). Source: Stiell 2003 via AFP 2004 summary.
- T_dc8269d6 c: "most reproductions give over 110" → Gurd and Wilson give tachycardia >110 and fever >38.5 °C. Source: Gurd & Wilson criteria (Skyscape calculator reproduction).
- POLY-09 FLAG, header comments in both files: updated to the above.

### Checked and left unchanged
- WHO: 4.4 million injury deaths a year, nearly 8% of all deaths; road traffic injury, homicide and suicide are 3 of the top 5 causes at 5–29 years (WHO fact sheet). Card's ">5 million" correctly flagged as older.
- Demetriades 2005, LA County: 4,151 deaths; 50.2% in the first hour, 18.3% 1–6 h after admission, 7.6% after a week (abstract).
- Berlin definition: 28,211 patients, 18.7% mortality; SBP ≤90, GCS ≤8, BE ≤−6.0, INR ≥1.4 or PTT ≥40 s, age ≥70 (Pape 2014).
- EMTRAS: four variables each 0–3, total 0–12, validation AUC 0.828 (Raum 2009 abstract); no total cut-off published in the abstract, so "over 8" stays flagged.
- Cochrane CD012669 (2018): sensitivity 0.74, specificity 0.96; adults 0.78/0.97 (Cochrane summary).
- Shock index normal 0.5–0.7 (Koch 2019, Open Access Emerg Med).
- ATLS 11: xABCDE, crystalloid minimised as a bridge, TXA within 3 h 1 g + 1 g, selective spinal motion restriction (journalfeed); head and spine merged into D (SGEM); video laryngoscopy (Afya). The 11th-edition shock table could not be opened.
- Needle decompression: ATLS 10th 4th/5th ICS just anterior to the mid-axillary line (REBEL EM).
- Massive haemothorax: >1,500 mL initially or >200 mL/h for 2–4 h (MSD Manual).
- EAST 2015 EDT (Seamon): penetrating thoracic with signs of life strong; blunt without signs of life conditional against (EAST PDF).
- AO Spine/Praxis 2024: MAP above 75–80, not actively above 90–95, for 3–7 days (SpineLine summary). AANS/CNS 2013 85–90 for 7 days: standard, not reopened.
- Gurd and Wilson: 1 major + 4 minor; tachycardia >110 (card's >120 flagged).
- EAST 2012 BCI: sternal fracture alone does not predict BCI (EAST PDF).
- Retrograde cystography: at least 300 mL (MSD; AUA ≥300, EAU ≥350 commonly quoted), so "300–350 mL" holds.
- WSES 2017 spleen: NOM contraindicated with unresponsive instability; angioembolisation first-line for stable patients with a blush; vaccination. Writer's FLAG on "transient responder" stands.
- Jefferson: instability tied to transverse ligament rupture (lateral mass overhang about 7 mm); writer's FLAG stands.
- Not re-opened (standard teaching, consistent with references I know): RTS weights and coding, ISS regions and AIS 6 → 75, Deakin & Low BMJ 2000, field triage 2021 lists, DAS Plan D, anterior/central/Brown-Séquard cord syndromes, Denis columns, ESVS permissive hypotension in rAAA.

## Final FLAGS — special05a_learn.py
- POLY-01: a: ‘over 5 million deaths a year’ is the older WHO figure; the current WHO fact sheet gives about 4.4 million (nearly 8% of deaths), with injuries 3 of the top 5 causes of death at 5–29 years (the card says 15–29).
- POLY-04: Range: an injured patient’s ISS is 1–75 (0 only with no injury); the card’s 0–75 is acceptable but most references write 1–75.
- POLY-05: b: EMTRAS (age, GCS, base excess, prothrombin time, each 0–3) confirmed; the ‘over 8 = high mortality’ cut-off could not be traced to the source paper.
- POLY-06: Watch line uses ‘primary/secondary injury’ in the general sense (mechanical vs the physiological insult that follows); in blast injury ‘secondary’ means fragment injury. Explained to avoid confusion.
- POLY-08: a: ‘radial ≈ SBP 70’ in the notes differs from the traditional ATLS teaching (radial 80, femoral 70, carotid 60), and all overestimate (the watch line already says so). d: ‘mild 13–14’ is non-standard; mild TBI is GCS 13–15.
- POLY-09: The card prints the older numeric ATLS table (8th/9th editions). The 10th edition replaced the numbers with direction arrows and added base deficit (0 to −2, −2 to −6, −6 to −10, ≤−10) and need for blood products; I could not open the 11th-edition table. The RR rows overlap (III 30–40, IV over 35), inherited from the original table. Responder bands (explanation table, not on the card): 10th edition rapid <15%, transient 15–40%, none >40%; the DocT explanation’s <20% / 20–40% are the 9th-edition bands.
- POLY-10: d: Marrow keys phenylephrine for neurogenic shock (qbank fix cross-note); noradrenaline is preferred, especially with bradycardia. MAP target differs between AANS/CNS 2013 (85–90 for 7 days) and AO Spine 2024 (≥75–80, ≤90–95, 3–7 days). a: xABCDE puts catastrophic external bleeding first, but an obstructed airway still comes first (NEET 2025 stem).

## Final FLAGS — special05a_topups_learn.py
- T_0ef120e7: b: ‘stable OR transient responder’ for NOM is broader than most guidance; WSES/EAST reserve NOM for haemodynamically stable or stabilised patients, and a transient responder qualifies only where IR is immediately available. One linked key (GT6 Q129, BP 90/60, HR 102 → embolisation) depends on calling the patient a responder.
- T_dc8269d6: c: Gurd and Wilson give tachycardia over 110 a minute and pyrexia over 38.5 °C (card: over 120). Teaching versions vary (some list pulmonary oedema or hypoxia among the major criteria).
- T_bb4f16eb: b: anti-impulse targets vary; commonly quoted targets are HR 60–80 and SBP ≤100 mmHg (MSD Manual), tighter than the card’s HR under 100. c: EAST 2012 also says a normal ECG with raised troponin I needs a monitored bed; the 24–48 h duration is common practice, not an EAST figure.
- T_d82a3b56: c: in anterior spinal artery infarction the paraplegia is below the level of the lesion, not ‘at’ it. GT2o Q58 keys ‘flaccid paralysis at T8 with complete loss of sensory and motor function’ for anterior spinal artery infarction; strictly the dorsal columns are spared, so the sensory loss is not complete.
- T_eb298c8d: b: in Denis’s scheme a flexion–distraction (Chance) injury fails the middle and posterior columns in tension, with the anterior column sometimes acting as a hinge; ‘all three columns’ is the common teaching shorthand. d: STASCIS studied cervical cord injury only. GT7 Q8 key (bilateral jumped facets, hyperflexion–distraction) depends on an MRI image not seen; the stem’s backward fall in a 65-year-old fits hyperextension central cord better.
- T_702a80b1: c: hyperextension–distraction is the judicial-hanging mechanism; in road collisions hyperextension with axial loading is usual. a: the Canadian rule also has paraesthesia as a high-risk factor and five low-risk criteria before the rotation test. e: ‘both unstable’ is a safe working rule, but a minimally displaced hangman’s fracture (Levine–Edwards type I) and a Jefferson fracture with an intact transverse ligament are stable.
- T_403270d5: a: most contusions are visible on CXR within about 6 h (CT earlier); ‘may be absent on first CXR’ applies to small ones. DocT says they develop over 24–48 h; the card’s 24–72 h is the wider range. Resolution is usually within about a week (often 3–7 days).
- T_f27b84e1: a: ‘straight to theatre/EVAR’ — EVAR normally needs CT angiography for planning; in the unstable patient without CT, open repair or on-table angiography is used.
- T_8867bce4: a: ‘humeral flow approaches a 16G line under pressure’ is overstated: human data give about 150–165 mL/min under pressure for both humeral and tibial sites (Ong 2009), with no consistent humeral advantage (BestBETs); a 16G peripheral cannula flows faster.
