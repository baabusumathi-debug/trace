# GI05 — Explain v3 ("Learn" depth): intra-abdominal hypertension and abdominal compartment syndrome — intra-abdominal pressure, bladder measurement (modified Kron), definitions and
# grades, abdominal perfusion pressure and the filtration gradient, primary/secondary/recurrent compartment syndrome, trauma epidemiology and predictors, causes, end-organ effects,
# misleading filling pressures, medical management, the WSACS algorithm, outcomes, true/false sweep.
# No mnemonics or hooks. Driven by qpack/GI05.md (28 question links; IAH-03 definitions and IAH-11 algorithm 7 each, IAH-10 medical management 4, IAH-04 and IAH-08 3 each).
# IAH-05, IAH-06, IAH-07, IAH-09 and IAH-12 have no linked question and get short explanations with [pattern] decode items. No Top-up cards for GI05.
# No `fix` entries exist for GI05 in trace/test/data/qbank.json (checked 20 Nov 2026). gi_cardlayer.json: IAH-11 `lines` (TAC closure 48–72 h vs 4–7 days) and `cross`
# (DocT ‘after failure of conservative measures’ key is wrong for the perforated ulcer) were read; the explanation agrees with both.
# Checked online on 20 Nov 2026:
#  - WSACS 2013 consensus definitions and guidelines (Kirkpatrick, Intensive Care Med 2013;39:1190–1206; Springer abstract and recommendation list; WSACS 2013 slide set):
#    IAP = steady-state pressure concealed within the abdominal cavity; normal about 5–7 mmHg in critically ill adults; reference standard intermittent trans-vesical with at most 25 mL saline;
#    mmHg, end-expiration, supine, no abdominal muscle contraction, zeroed at the mid-axillary line (iliac crest); IAH sustained or repeated IAP ≥12; grades I 12–15, II 16–20, III 21–25, IV >25;
#    ACS sustained IAP >20 (with or without APP <60) with new organ dysfunction/failure; primary = abdomino-pelvic origin, often needing early surgery or interventional radiology;
#    secondary = not originating in the abdomino-pelvic region; recurrent = recurs after surgical or medical treatment of primary or secondary ACS; APP = MAP − IAP; FG = MAP − 2 × IAP;
#    polycompartment syndrome; abdominal compliance = change in volume per change in pressure.
#    Recommendations: measure IAP with any risk factor (1C); protocolised monitoring and management (1C); avoid sustained IAH (1C); decompressive laparotomy for overt ACS (1D);
#    early or same-hospital-stay fascial closure (1D); negative-pressure wound therapy for the open abdomen (1C). Suggestions: analgesia and sedation (2D); brief NMB trial (2D); body position (2D);
#    liberal NG/rectal decompression when the stomach or colon is dilated (1D); neostigmine for refractory colonic ileus (2D); protocol to avoid positive cumulative fluid balance (2C);
#    enhanced plasma:red cell ratio in massive haemorrhage (2D); percutaneous catheter drainage vs nothing (2C) and vs immediate decompressive laparotomy (2D); prophylactic open abdomen after
#    trauma laparotomy with physiological exhaustion (2D); not routine open abdomen for intra-abdominal sepsis (2B). No recommendation: APP as a resuscitation end-point; diuretics, RRT or albumin
#    to mobilise fluid; component separation.
#  - WSACS 2007 summary page (wsacs.org): APP above 50–60 mmHg (1C) and hypertonic/colloid resuscitation (1C) were 2007 statements, dropped to ‘no recommendation’ in 2013.
#  - Paediatric (LITFL, citing WSACS 2013): normal IAP about 4–10 mmHg, IAH >10 mmHg, instillation 1 mL/kg, minimum 3 mL, maximum 25 mL.
#  - LITFL: transmural CVP = CVP − 0.5 × IAP; LITFL subtracts the whole IAP for transmural plateau pressure (the card’s 0.5 × IAP is the Malbrain teaching; transmission varies, roughly 20–80%).
#  - FICM case of the month (IAH): measure IAP every 4–6 hours, target IAP under 15 mmHg, decompression for treatment failure or refractory cardiorespiratory failure.
#  - Cheatham & Safcsak, Crit Care Med 2010 (478 consecutive patients, IAH/ACS management algorithm): survival to discharge 50% → 72% (p 0.015); same-admission primary fascial closure 59% → 81%.
# Second, independent review (20 Nov 2026), checked online: WSACS 2013 text (Springer; WSACS-hosted PDF: paediatric 1 mL/kg, min 3, max 25 mL; ‘early or at least same-hospital-stay’
#  fascial closure 1D; no recommendation on APP); WSES 2018 open abdomen (Coccolini, WJES 13:7): close as soon as possible (1C), early closure 1B, ‘early fascial closure is commonly
#  defined as within 4–7 days’ (text, not graded), re-exploration no later than 24–48 h (1C); Balogh 2003 J Trauma abstract (188 shocked torso-trauma patients, ACS 14%: 6% primary,
#  8% secondary); Hong 2002 Br J Surg (706 trauma ICU patients, IAH 2%, ACS 1%); StatPearls ACS (oliguria at 15, anuria at 30 mmHg); OpenAnesthesia ICU one-pager and a WSACS-based
#  trauma protocol (VUMC: q4–6 h, discontinue when under 12); LA County burn protocol reproducing the WSACS 2007 four-group risk table; Mahjoub 2010 and Beurton 2019 via Ann Transl
#  Med 2019 commentary (PLR false negatives at IAP ≥16; AUROC 0.60 vs 0.98).
# Not re-opened: the WSACS 2013 algorithm figure itself (PMC blocked); the Balogh 2003 numeric cut-offs (full text only; card figures kept); the 9% of Balogh 2002; LITFL plateau formula;
#  decompression reperfusion syndrome (standard teaching).

SPINE = [
  ("Measuring abdominal pressure properly", "Abdominal pressure is read through the bladder with the patient flat, zeroed at the mid-axillary line, with no more than 25 mL of saline, at end-expiration and with the abdominal wall relaxed."),
  ("Hypertension versus compartment syndrome", "Twelve or more is intra-abdominal hypertension, graded I to IV, but compartment syndrome needs a sustained pressure over 20 plus new organ failure, and perfusion pressure is MAP minus IAP."),
  ("Why the pressure rises", "Pressure rises when the abdomen holds more (fluid, blood, oedema, gas) or the wall gives less, and capillary leak from large-volume resuscitation is the commonest route to secondary disease."),
  ("What the pressure does", "Raised pressure squeezes the cava, kidneys and gut, pushes up the diaphragm and is partly transmitted to the chest, so cardiac output and urine fall while CVP and airway pressures read falsely high."),
  ("Medical first, then decompress", "Hypertension is treated medically in steps, a surgical cause or refractory compartment syndrome is decompressed by laparotomy, and protocolised care improves survival."),
]

PRIMER = "The abdomen is a closed box whose walls stretch only so far: once its compliance is used up, a small rise in volume produces a large rise in pressure. That pressure is passed on to everything inside (kidneys, gut, liver, the inferior vena cava) and, through the diaphragm, to the chest. Perfusion of an abdominal organ depends on the gap between arterial pressure and the pressure around it, just as cerebral perfusion depends on MAP minus ICP. All figures in this deck are in mmHg; 1 mmHg is about 1.36 cmH2O."

L = {}

L['IAH-01'] = dict(
  sub="Intra-abdominal hypertension → Measurement → Intra-abdominal pressure",
  step=1,
  intro="Step 1 starts with what is being measured and how often. The one real question gives a septic abdomen with rising pressure and new breathlessness and asks for the next diagnostic step; only 43% chose the bladder pressure.",
  parts=[
    ('a', "**The steady-state pressure within the abdominal cavity.** It is the pressure at rest, not the brief spikes of coughing or straining, which is why readings are taken at end-expiration with the wall relaxed."),
    ('b', "**5–7 mmHg in critically ill adults.** A healthy person lying flat is near zero; ventilation, recent surgery and oedema lift the ICU baseline a little. It is not zero, which IAH-13 tests."),
    ('c', "**Obesity and pregnancy (rises with BMI), without organ effects.** The rise is slow, so the wall stretches and adapts and the organs tolerate it. The same number reached acutely in a stiff post-operative abdomen can cause organ failure, which is why the definition of compartment syndrome needs new organ dysfunction, not a number alone."),
    ('d', "**Trans-vesical (bladder) pressure.** The bladder wall is passive at low volume and transmits the surrounding pressure; it is cheap, bedside and repeatable. CT or ultrasound can suggest a tense abdomen (round belly sign, compressed cava, ascites) but cannot give the pressure."),
    ('e', "**Every 4 hours while critically ill.** WSACS-based algorithms measure at least every 4–6 hours, or continuously, once IAH is present. WSACS 2013 recommends measuring whenever any known risk factor is present (1C); the 2007 algorithm used two or more risk factors, or new or worsening organ failure, as the trigger."),
  ],
  mimic=[
    ("Chronic raised IAP (obesity, pregnancy) vs acute IAH", "Chronic: slow rise, adapted wall, no organ failure. Acute: rapid rise in a non-compliant abdomen, organ failure at the same number."),
  ],
  traps=[
    ("“Get a CT abdomen first when IAP is rising”", "CT cannot measure pressure and means transporting an unstable patient; the bedside bladder pressure is the diagnostic step (43% right on DocT)."),
    ("“Go back to theatre on suspicion alone”", "Re-laparotomy is a treatment decision made after the pressure is measured and organ failure is linked to it."),
  ],
  decode=[
    ("Septic abdomen after source control, day 3, new respiratory distress and rising IAP: next diagnostic step? [DocT QBank]", "Bladder pressure measurement (43% right)."),
    ("Normal IAP in a ventilated ICU adult? [pattern]", "5–7 mmHg, not zero."),
  ],
  punch="Abdominal pressure is a number you measure through the bladder, not a judgement from the belly or the CT; normal in the ICU is 5–7 mmHg.",
)

L['IAH-02'] = dict(
  sub="Intra-abdominal hypertension → Measurement → Bladder pressure (modified Kron)",
  step=1,
  intro="Step 1 is the technique, because a badly taken reading leads to the wrong grade. Two real questions; the one about the transducer was answered right by only 54%, the distractors being the symphysis pubis, prone position and a 500 mL bladder volume.",
  parts=[
    ('a', "**Patient supine, flat.** Head-up and prone positions raise the reading because the abdominal contents press down on the bladder; WSACS standardises the supine position so serial readings can be compared."),
    ('b', "**Transducer zeroed at the mid-axillary line.** WSACS 2013 specifies the mid-axillary line at the level of the iliac crest. Kron’s original 1984 method zeroed at the symphysis pubis, which is why that distractor looks familiar; the pubis lies above the bladder in a supine patient and gives a falsely low value."),
    ('c', "**Catheter clamped; an 18G cannula in the aspiration port.** Clamping distal to the port makes the bladder and tubing one fluid column with the transducer."),
    ('d', "**Instil at most 25 mL sterile saline.** Just enough to make a fluid column. Larger volumes stretch the bladder wall so it adds its own tension, and the reading rises falsely; the 500 mL distractor would grossly overestimate IAP. In children the volume is 1 mL/kg, minimum 3 mL, maximum 25 mL (the card’s watch line; your notes print 0.5 mL/kg)."),
    ('e', "**Wait 30–60 seconds (detrusor relaxation).** Cold saline makes the detrusor contract briefly; reading too early adds that contraction."),
    ('f', "**Read at end-expiration, with no abdominal muscle contraction; express in mmHg.** Inspiration pushes the diaphragm down and raises IAP; an active expiration or a straining patient tightens the wall. End-expiration gives the lowest steady reading. Results are in mmHg; a value given in cmH2O must be divided by 1.36."),
  ],
  mimic=[
    ("Mid-axillary line (WSACS) vs symphysis pubis (original Kron)", "The standard now is the mid-axillary line at the iliac crest; the pubis is the old reference."),
  ],
  traps=[
    ("“Zero the transducer at the symphysis pubis”", "That was the original Kron method; WSACS 2013 zeroes at the mid-axillary line. It is the first distractor in the DocT question that only 54% got right."),
    ("“Measure in the prone position” or “instil 500 mL”", "Supine and at most 25 mL; both changes raise the reading falsely."),
  ],
  decode=[
    ("Transducer placed for bladder pressure: which is TRUE? [DocT QBank]", "End-expiration (54% right); not the symphysis, not prone, not 500 mL."),
    ("Rising IAP in a septic abdomen: next diagnostic step? [DocT QBank]", "Bladder pressure measurement."),
  ],
  punch="Supine, mid-axillary zero, 25 mL or less, wait 30–60 seconds, read at end-expiration with a relaxed wall: every departure from this pushes the reading up.",
)

L['IAH-03'] = dict(
  sub="Intra-abdominal hypertension → Definitions → IAH grades and compartment syndrome",
  step=2,
  intro="Step 2 turns the number into a diagnosis. This card is asked seven times, and the questions test two things: the thresholds themselves (12 for IAH, over 20 for compartment syndrome, not 25 or 15), and the fact that compartment syndrome needs new organ failure, which the 34% question shows people miss in reverse.",
  parts=[
    ('a', "**Intra-abdominal hypertension: sustained or repeated IAP of 12 or more.** A single high reading during coughing or a badly taken measurement does not count; the pressure must be sustained or recur."),
    ('b', "**Grade I 12–15.** Organ effects are usually subtle; treat the cause and watch."),
    ('c', "**Grade II 16–20.** Oliguria begins around 15 mmHg (IAH-08), so organ dysfunction can appear here; with organ failure at 16–20 it is still not compartment syndrome by definition, and medical measures are escalated."),
    ('d', "**Grade III 21–25.** Pressure is now in the range where compartment syndrome is diagnosed if a new organ failure is present."),
    ('e', "**Grade IV over 25.** The highest grade of IAH, but it is still a pressure band, not a diagnosis of compartment syndrome."),
    ('f', "**Abdominal compartment syndrome: sustained IAP over 20 mmHg with new organ dysfunction.** WSACS adds ‘with or without APP under 60’. The organ failure is what makes it a syndrome: oliguria, rising peak airway pressure, hypoxia, hypotension or acidosis that is new and attributable to the pressure. A patient at 22 mmHg breathing comfortably with a good urine output has grade III IAH, not compartment syndrome."),
  ],
  mimic=[
    ("Grade IV IAH vs abdominal compartment syndrome", "Grade IV is a number (over 25); compartment syndrome is over 20 plus new organ failure. A patient can have either without the other."),
    ("IAH grade II with organ dysfunction vs ACS", "Under 20 is not ACS even with falling urine; treat medically and escalate (the 34% DocT question)."),
  ],
  traps=[
    ("“ACS requires IAP over 25 mmHg”", "Over 20 with new organ failure; this was the false statement keyed in the NEET 2025 recall."),
    ("“ACS is IAP over 15 with organ failure”", "Over 20; Marrow’s false statement."),
    ("“IAP 19 with poor compliance and falling urine needs surgical decompression”", "19 is grade II; it is not compartment syndrome, so the next step is medical (neuromuscular blockade; DocT key, only 34% right). See IAH-10."),
    ("“Bladder pressure 22 cmH2O is over 20, so it is ACS”", "22 cmH2O is about 16 mmHg (divide by 1.36), so taken literally none of options A–C reaches the ACS threshold; the question almost certainly means mmHg. ‘Most consistent’ is then decided by organ failure: the keyed patient (C) has oliguria, peak pressure 40 and FiO2 0.6 after massive transfusion, despite an open abdomen, because an open abdomen does not exclude recurrent ACS. The 22 mmHg burn patient (D) on 2 L oxygen with a good urine output has grade III IAH only."),
    ("“Perforated ulcer with IAP 26 and oliguria: laparotomy after conservative measures fail” (DocT key C)", "The key is wrong. A surgical cause needs immediate laparotomy (B), as DocT’s own explanation and its identical question say. See IAH-11."),
  ],
  decode=[
    ("IAH is defined as sustained IAP of: >10 / >12 / >15 / >20? [DocT GT, CGT2]", "12 or more (keyed ‘>12’)."),
    ("Perforated diverticulitis, IAP 22, oliguric, rising peak pressures: best description? [DocT QBank]", "Abdominal compartment syndrome (90% right)."),
    ("Which scenario is most consistent with ACS? [DocT GT, GT1o]", "The one with new organ failure, read in mmHg not cmH2O (75% right)."),
    ("ACS: all true except… [NEET 2025, Marrow]", "‘Requires IAP over 25’ and ‘over 15 with organ failure’ are false; retroperitoneal surgery as a primary cause and decompressive laparotomy as treatment are true."),
  ],
  punch="IAH is a pressure of 12 or more, graded in bands of five; compartment syndrome is a sustained pressure over 20 with a new organ failing, and without that failure even grade IV is only hypertension.",
)

L['IAH-04'] = dict(
  sub="Intra-abdominal hypertension → Definitions → Abdominal perfusion pressure and filtration gradient",
  step=2,
  intro="Step 2 continues with the perfusion pressure, which explains why the kidney fails first. Three questions: two (one repeated in a Grand Test) ask the mechanism of oliguria with a good cardiac output, and one asks the APP threshold, answered right by only 44%.",
  parts=[
    ('a', "**MAP − IAP.** The abdominal organs sit inside the pressurised box, so the pressure driving blood through them is arterial pressure minus the pressure around them, the same logic as cerebral perfusion pressure."),
    ('b', "**60 mmHg or more: associated with better survival.** Observational data (Cheatham) found APP a better predictor of survival than IAP or MAP alone. WSACS 2007 suggested keeping APP above 50–60; WSACS 2013 made no recommendation on using it as a resuscitation end-point. For the exam, under 60 is compromised perfusion."),
    ('c', "**Kidney: filtration gradient = MAP − 2 × IAP.** Glomerular filtration pressure is roughly MAP minus IAP, and the proximal tubular pressure that opposes filtration is roughly equal to IAP, so IAP counts twice. A rise of 10 mmHg in IAP cuts the filtration gradient by 20. That is why urine falls even when cardiac output is preserved: renal vein and parenchymal compression, not pump failure or tubular necrosis. Urine sodium is low because the kidney is underperfused, not damaged."),
  ],
  mimic=[
    ("Oliguria from IAH vs acute tubular necrosis", "IAH: low urine sodium, preserved cardiac output, falls in the filtration gradient, reversible with decompression. ATN: high urine sodium, casts."),
  ],
  traps=[
    ("“APP below 45 is the threshold of compromise”", "Below 60; only 44% chose it on DocT. In that stem the APP is 55, already compromised."),
    ("“Oliguria with stable cardiac output is from tubular necrosis or low contractility”", "It is the pressure itself (88% right): IAP counts twice against filtration."),
  ],
  decode=[
    ("IAP 28, falling GFR, low urine sodium, stable cardiac output: main driver? [DocT QBank, CGT1]", "Raised intra-abdominal pressure (88% right)."),
    ("APP 55 after laparotomy: which value means compromised perfusion? [DocT QBank]", "Below 60 mmHg (44% right)."),
  ],
  punch="Organ perfusion in the abdomen is MAP minus IAP, and the kidney feels IAP twice (MAP − 2 × IAP), so it fails first, with low urine sodium and a normal cardiac output.",
)

L['IAH-05'] = dict(
  sub="Intra-abdominal hypertension → Causes → Primary, secondary and recurrent",
  step=3,
  intro="Step 3 sorts compartment syndrome by where the cause lies, which decides who opens the abdomen. No question is linked directly, but the GT scenarios (perforation vs pancreatitis vs burns) all hinge on this split.",
  parts=[
    ('a', "**Origin: primary = injury or disease in the abdomen or pelvis; secondary = outside the abdomen.** WSACS defines primary as abdomino-pelvic in origin, often needing early surgery or interventional radiology. Retroperitoneal surgery, perforation and pelvic bleeding are primary."),
    ('b', "**Setting: primary after damage-control laparotomy or failed non-operative organ injury; secondary after massive resuscitation for shock (burns, pelvic or limb fractures, chest injury).** Secondary disease follows capillary leak from large volumes of crystalloid given for a problem elsewhere."),
    ('c', "**Mechanism: primary = bleeding, packs, bowel oedema; secondary = bowel and retroperitoneal oedema, ascites.**"),
    ('d', "**Diagnosis: primary is expected; secondary is elusive and delayed.** The surgeon watches a damage-control abdomen; nobody expects the burns or limb-injury patient to develop it, so it is found late unless at-risk patients are measured."),
    ('e', "**Treatment: primary = early surgery or radiology; secondary = medical first.** A primary cause (bleeding, perforation) usually needs the abdomen opened or embolised; secondary disease is treated with the IAH-10 measures and decompressed only if organ failure persists."),
  ],
  mimic=[
    ("Recurrent (formerly tertiary) vs primary", "Recurrent returns after treatment of either type, even with an open abdomen."),
  ],
  traps=[
    ("“Burns cause primary ACS”", "Burns are outside the abdomen: secondary (IAH-13)."),
  ],
  decode=[
    ("Burns resuscitation with tense abdomen and oliguria: type of ACS? [pattern]", "Secondary."),
    ("ACS returning in a patient with an open abdomen: name? [pattern]", "Recurrent ACS."),
  ],
  punch="Primary starts in the abdomen and usually needs a surgeon; secondary is made by resuscitation elsewhere and is treated medically first.",
)

L['IAH-06'] = dict(
  sub="Intra-abdominal hypertension → Causes → Trauma epidemiology and predictors",
  step=3,
  intro="Step 3 in trauma: who gets it, and how early it can be predicted. No real question is linked; the point that would be asked is that crystalloid volume predicts both types.",
  parts=[
    ('a', "**1% of all trauma ICU admissions; 14% of torso trauma.** Uncommon overall, frequent in the severely injured torso."),
    ('b', "**9%.** Secondary compartment syndrome in patients resuscitated for shock, from Balogh’s Houston series (2002). In his 2003 cohort of 188 shocked torso-trauma patients, 14% developed ACS: 6% primary and 8% secondary, which is where the 14% in part a comes from; the 1% of all trauma ICU admissions is from a separate prospective study of 706 patients (Hong 2002). Later series report less ACS as damage-control resuscitation cut crystalloid volumes."),
    ('c', "**Primary: ED to theatre under 75 min, crystalloid 3 L or more; ICU temperature 34 °C or less, haemoglobin 8 or less, base deficit 12 or more, gastric–arterial CO2 gap 16 or more.** These mark the exsanguinating patient with the lethal triad, whose abdomen is packed and oedematous. In Balogh 2003 haemoglobin, CO2 gap, temperature and base deficit were the early ICU predictors of primary ACS."),
    ('d', "**Secondary: ED crystalloid 3 L or more, red cells 3 units or more; ICU crystalloid 7.5 L or more, urine 150 mL or less, CO2 gap 16 or more.** Volume is the driver: the gut leaks and swells as crystalloid accumulates. In Balogh 2003 crystalloid volume, urine output and CO2 gap were the early predictors of secondary ACS, which came earlier in the ICU course and after more crystalloid than primary ACS."),
  ],
  mimic=[
    ("Primary vs secondary predictors", "Both share crystalloid of 3 L or more in the ED; primary adds markers of the lethal triad, secondary adds the ICU crystalloid total of 7.5 L."),
  ],
  traps=[
    ("“Secondary ACS is unpredictable”", "Crystalloid volume and gut hypoperfusion predict it early."),
  ],
  decode=[
    ("Common predictor of primary and secondary ACS after injury? [pattern]", "Crystalloid 3 L or more in the emergency department."),
  ],
  punch="In trauma, compartment syndrome is largely made by crystalloid; 3 L in the emergency department predicts both types.",
)

L['IAH-07'] = dict(
  sub="Intra-abdominal hypertension → Causes → More contents, less room",
  step=3,
  intro="Step 3 lists the causes by mechanism: the box either holds more or stretches less. No question is linked; the WSACS risk-factor groups are the likely question.",
  parts=[
    ('a', "**More contents: ascites, haemoperitoneum; visceral and retroperitoneal oedema (pancreatitis); abdominal packs; ileus, obstruction, gastric distension; pelvic or retroperitoneal haematoma; chronic obesity, pregnancy, tumour.** Each adds volume to a box near the limit of its compliance."),
    ('b', "**Less room: tight closure of a large hernia or wall defect; circumferential abdominal burn eschar; positive-pressure ventilation, high PEEP.** These stiffen the wall or push the diaphragm down. A circumferential torso eschar is the case where escharotomy, not laparotomy, is the first treatment."),
    ('c', "**The four WSACS groups: reduced wall compliance, more intraluminal contents, more abdominal contents, capillary leak with fluid resuscitation.** This is the WSACS 2007 risk-factor table. Its last group (massive fluid resuscitation over 5 L in 24 h, polytransfusion, acidosis, hypothermia, coagulopathy, sepsis, pancreatitis, damage-control laparotomy) is the commonest route to secondary disease. The same table puts head of bed over 30 degrees, prone positioning, high BMI and respiratory failure with high intrathoracic pressure under reduced wall compliance."),
  ],
  mimic=[
    ("Intraluminal (gas, gastric content) vs abdominal (ascites, blood) contents", "Intraluminal is emptied by NG and rectal tubes; abdominal fluid by paracentesis or percutaneous drainage."),
  ],
  traps=[
    ("“PEEP lowers IAP by recruiting lung”", "High PEEP and raised intrathoracic pressure push the diaphragm down and raise IAP."),
  ],
  decode=[
    ("Which of these is a WSACS risk factor for IAH? [pattern]", "Any of the four groups, including head up over 30 degrees, high BMI and massive transfusion."),
  ],
  punch="Pressure rises when the abdomen holds more or the wall gives less; sorting the cause into those groups tells you which treatment empties it.",
)

L['IAH-08'] = dict(
  sub="Intra-abdominal hypertension → Organ effects → End-organ effects",
  step=4,
  intro="Step 4 is what the pressure does. Three questions: the kidney mechanism (88% right), an ‘all except’ in which a third missed that airway pressures rise, and the Marrow question on the lung in a ventilated patient.",
  parts=[
    ('a', "**Heart: venous return falls (caval compression); raised diaphragm impairs ventricular compliance; CVP and wedge pressure read falsely high.** Preload falls and afterload rises (compressed vascular beds raise systemic resistance), so cardiac output falls. The pressure transmitted to the chest raises CVP even though the ventricle is underfilled (IAH-09)."),
    ('b', "**Lung: low compliance and FRC, atelectasis: hypoxia, hypercapnia, high peak and plateau pressures.** The diaphragm is pushed up, the chest wall becomes stiff, and the respiratory system compliance falls, so the same tidal volume needs higher pressure. Ventilation pressures rise, not fall."),
    ('c', "**Kidney: oliguria at 15 mmHg; anuria at 30 mmHg.** Renal vein compression, direct parenchymal compression and the filtration gradient (MAP − 2 × IAP, IAH-04) reduce filtration; low cardiac output and renin–angiotensin activation add to it."),
    ('d', "**Gut: mesenteric and mucosal flow fall; venous stasis and oedema raise the pressure further; translocation.** Gut perfusion falls early, at moderate pressures, often before urine output falls: mucosal acidosis and oedema add volume and raise IAP more, so the problem feeds itself, and bacterial translocation drives sepsis and multi-organ failure. The liver loses arterial and portal flow, so lactate clearance falls."),
    ('e', "**Brain: raised intrathoracic pressure impedes venous drainage: ICP rises.** Jugular venous outflow is impeded; decompressive laparotomy has lowered refractory intracranial hypertension in head-injured patients with IAH."),
  ],
  mimic=[
    ("High CVP in IAH vs high CVP in volume overload", "In IAH the transmural CVP is low and the ventricle underfilled; giving fluid on a high CVP is wrong in both, but for different reasons."),
  ],
  traps=[
    ("“Raised IAP decreases ventilation pressure”", "Peak and plateau pressures rise; this is the exception in the GT7 ‘all except’ (66% right)."),
    ("“Oliguria in ACS is from low contractility or ATN”", "It is the pressure (renal vein and parenchymal compression, filtration gradient)."),
  ],
  decode=[
    ("Effects of raised IAP: all except… [DocT GT, GT7]", "Decreased ventilation pressure (66% right); visceral perfusion falls, ICP rises, cardiac output falls."),
    ("Ventilated patient with ACS: pulmonary manifestation? [Marrow]", "Increased peak airway pressure."),
    ("IAP 28, falling GFR, low urine sodium, stable cardiac output: cause? [DocT QBank]", "Raised intra-abdominal pressure."),
  ],
  punch="Raised abdominal pressure lowers cardiac output, urine and gut flow while it raises CVP, airway pressure and ICP; the numbers that rise are the ones that mislead.",
)

L['IAH-09'] = dict(
  sub="Intra-abdominal hypertension → Organ effects → Misleading filling pressures",
  step=4,
  intro="Step 4 includes the trap at the bedside: pressures measured inside the chest include part of the abdominal pressure. No question is linked; it is asked as ‘high CVP, give fluid?’.",
  parts=[
    ('a', "**About half of the abdominal pressure is transmitted to the chest.** The diaphragm passes on part of the pressure; the share varies widely (roughly 20–80%), half is the working figure."),
    ('b', "**Transmural CVP = CVP − 0.5 × IAP; same for wedge pressure.** What fills the heart is the pressure inside minus the pressure outside. A CVP of 18 with an IAP of 20 is a transmural CVP of about 8."),
    ('c', "**Transmural plateau pressure = plateau − 0.5 × IAP.** A high plateau pressure in IAH partly reflects a stiff chest wall, not overstretched lung, so the lung may tolerate it. Some sources (LITFL) subtract the whole IAP; the principle is the same."),
    ('d', "**Volumetric preload indices.** Global end-diastolic volume by transpulmonary thermodilution or echocardiographic volumes are not distorted by pressure transmission. Dynamic tests are affected too. Passive leg raising can give false negatives when IAP is high, because the compressed cava limits the shift of blood from the legs: in Mahjoub 2010 an IAP of 16 mmHg or more was the only factor linked to a false-negative test, and in Beurton 2019 the test’s accuracy fell (AUROC about 0.60 with IAH vs 0.98 without). Measure IAP before relying on a negative leg raise."),
  ],
  mimic=[
    ("Raised CVP from IAH vs from fluid overload", "In IAH the transmural pressure and the ventricular volume are low."),
  ],
  traps=[
    ("“CVP reads falsely low in IAH”", "Falsely high (IAH-13)."),
  ],
  decode=[
    ("IAH with CVP 18 and falling urine output: is the patient full? [pattern]", "Not necessarily; the transmural CVP is about CVP − 0.5 × IAP."),
  ],
  punch="In IAH a high CVP or wedge pressure does not mean the heart is full: subtract half the abdominal pressure, or use volumes instead.",
)

L['IAH-10'] = dict(
  sub="Intra-abdominal hypertension → Management → Five medical options",
  step=5,
  intro="Step 5 begins with what is done before any surgeon is called. Four questions; the hardest (34% right) was the grade II patient with falling compliance in whom the right answer is neuromuscular blockade, not decompression.",
  parts=[
    ('a', "**Improve wall compliance: sedation, analgesia, neuromuscular blockade; avoid head of bed over 30 degrees.** Pain and agitation tighten the abdominal wall; WSACS suggests analgesia and sedation and a brief trial of neuromuscular blockade as a temporising measure (2D). Paralysis can lower IAP by several mmHg within minutes, which buys time in grade II–III IAH. Remove tight dressings; an abdominal eschar needs escharotomy."),
    ('b', "**Evacuate intraluminal contents: nasogastric and rectal decompression, prokinetics.** WSACS suggests liberal NG and rectal decompression when the stomach or colon is dilated, and neostigmine for refractory colonic ileus (2D). This is the first, least invasive step (the Marrow post-splenectomy question)."),
    ('c', "**Evacuate abdominal collections: paracentesis, percutaneous drainage.** Percutaneous catheter drainage is suggested over doing nothing (2C) and even over immediate decompressive laparotomy (2D) when there is obvious free fluid, for example ascites in pancreatitis or burns. It is therapeutic, not just diagnostic, and is not contraindicated in ACS."),
    ('d', "**Correct positive fluid balance: avoid excess fluid; diuretics, colloid, ultrafiltration.** WSACS suggests a protocol to avoid a positive cumulative balance after resuscitation (2C) and a high plasma:red cell ratio in massive haemorrhage (2D). It makes no recommendation on diuretics, albumin or RRT, so furosemide is not the answer for an oliguric patient whose kidneys are compressed."),
    ('e', "**Organ support: optimise ventilation; use transmural pressures.** Set PEEP to counter the pressure on the lung bases, interpret CVP and plateau transmurally (IAH-09), and aim for APP of at least 60 (an observational target; WSACS 2013 makes no recommendation on APP)."),
  ],
  mimic=[
    ("Percutaneous drainage vs decompressive laparotomy", "Drainage when free fluid is the cause and organ failure is not immediately life-threatening; laparotomy for a surgical cause or failure of medical measures."),
  ],
  traps=[
    ("“IAP 19 after laparotomy, poor compliance, falling urine: surgical decompression”", "19 is grade II, not ACS; a brief trial of neuromuscular blockade is the keyed answer (only 34% right). Furosemide does not treat compression, and antibiotics treat nothing here."),
    ("“Percutaneous drainage is only diagnostic” or “contraindicated in ACS”", "It is a valid non-surgical decompression (77% right)."),
    ("“Immediate laparotomy for septic free fluid with organ dysfunction”", "If the fluid can be drained, ultrasound-guided percutaneous drainage comes first (72% right)."),
  ],
  decode=[
    ("Day 2 after trauma laparotomy, bladder pressure 19, compliance falling, urine falling: next? [DocT QBank]", "Neuromuscular blockade (34% right)."),
    ("Percutaneous catheter drainage in IAH after bowel surgery: true statement? [DocT QBank]", "A valid step in non-surgical decompression (77%)."),
    ("Abdominal sepsis, free fluid on ultrasound, worsening organ dysfunction: next step? [DocT QBank]", "Ultrasound-guided percutaneous drainage (72%)."),
    ("Post-splenectomy day 3, tense abdomen, IAP 24: next? [Marrow]", "Nasogastric tube decompression."),
  ],
  punch="Before anyone opens the abdomen, relax the wall, empty the gut, drain the fluid and stop the positive balance; each lowers IAP by removing a cause.",
)

L['IAH-11'] = dict(
  sub="Intra-abdominal hypertension → Management → WSACS algorithm",
  step=5,
  intro="Step 5 is the decision to open the abdomen. Seven questions, and the most repeated one (a perforated ulcer with IAP 26, oliguria and hypotension) is keyed wrongly by DocT in three places; the cohort split 41–65% because the key is wrong.",
  parts=[
    ('a', "**IAP 12 or more: start medical treatment; measure IAP at least every 4 hours; avoid excess fluid.** The WSACS algorithm says at least every 4–6 hours or continuously, titrating therapy to keep IAP at 15 or less."),
    ('b', "**IAP over 20 with new organ failure: abdominal compartment syndrome: find the cause.** The cause decides the route: a surgical cause (perforation, bleeding, ischaemic bowel, packed abdomen) or a medical one (capillary leak, ascites, pancreatitis)."),
    ('c', "**Primary compartment syndrome: decompressive laparotomy with temporary abdominal closure.** WSACS recommends decompressive laparotomy for overt ACS (1D). With a perforation, laparotomy also controls the source, so it is done at once, not after conservative measures fail. The abdomen is left open with a temporary closure, ideally negative-pressure therapy (1C), and the fascia is closed as early as physiology allows (1D)."),
    ('d', "**Secondary or recurrent: continue medical options; decompress if organ failure progresses.** In pancreatitis or resuscitation-induced ACS, NG and rectal decompression, sedation and paralysis, percutaneous drainage and a negative balance come first; refractory ACS is decompressed. In a burn patient with ACS from intra-abdominal fluid, percutaneous drainage is a reasonable first step when the fluid is drainable, and decompressive laparotomy follows if organ failure persists; escharotomy only helps when a circumferential torso eschar is the restriction."),
    ('e', "**IAP consistently under 12: stop measuring, observe.** Below 12 the patient no longer has IAH by definition, so WSACS-based protocols stop routine measurement and observe, and measurement resumes if the patient deteriorates clinically or a new risk factor appears."),
  ],
  mimic=[
    ("Surgical-cause ACS vs medical-cause ACS", "Perforation or bleeding: laparotomy now. Pancreatitis or fluid overload: medical measures and percutaneous drainage first, laparotomy if refractory."),
  ],
  traps=[
    ("“Perforated duodenal ulcer, IAP 26, oliguric, hypotensive: decompressive laparotomy after failure of conservative measures” (DocT key C; QBank, CGT4, GT6)", "The key is wrong. This is ACS with an unsourced perforation: immediate laparotomy (B), for source control and decompression together, as DocT’s own explanation and its identical Q11 say. Pick immediate laparotomy whenever ACS has a surgical cause."),
    ("“Temporary abdominal closure increases ACS risk” or “is used only for damage control”", "It prevents recurrent ACS and is used in damage control, severe peritonitis and ACS decompression. DocT keys closure ‘within 48–72 h’ (39% right): no guideline fixes that number for closure. WSACS 2013 asks for early or at least same-admission fascial closure (1D); WSES 2018 says close as soon as possible (1C), with early closure commonly defined as within 4–7 days of the index operation. The 24–48 h figure in WSES is the interval for re-looking at the open abdomen, not for closing it. Pick 48–72 h when it is the only true option."),
    ("“Burns ACS: escharotomy”", "Escharotomy treats a restrictive eschar; ACS from intra-abdominal fluid needs the abdomen decompressed, and of the options given that is decompressive laparotomy (53% right on GT1o)."),
    ("“Pancreatitis ACS, IAP 24, APP 41: immediate laparotomy” (CGT4 key)", "Best of the options given (APP is under 60, A and C are wrong), but the guidance is stepwise: NG decompression, sedation and paralysis, percutaneous drainage, then laparotomy if ACS persists."),
  ],
  decode=[
    ("Perforated ulcer, IAP 26, oliguric and hypotensive: next step? [DocT QBank, CGT4, GT6]", "Immediate laparotomy (keyed C wrongly; 41–65% right)."),
    ("Sudden pain, septic shock, IAP 25, falling urine, high airway pressures: next? [DocT QBank]", "Immediate laparotomy and decompression (64%)."),
    ("Burn on Parkland, oliguric, peak 45, IAP 25: diagnosis and treatment? [DocT GT, GT1o]", "ACS, decompressive laparotomy (53%)."),
    ("Open abdomen with temporary closure: true statement? [DocT QBank]", "Close early (keyed 48–72 h; 39%)."),
  ],
  extra=[
    dict(q="How is the open abdomen managed after decompression?", a="Negative-pressure wound therapy is the recommended temporary closure (WSACS 1C); IAP is still measured because recurrent ACS can occur with an open abdomen; the abdomen is re-explored every 24–48 h (WSES 2018) and the fascia closed during the same admission as soon as physiology allows, early closure meaning within about 4–7 days, because closure rates fall and fistula, infection and ‘frozen abdomen’ rise with each day."),
  ],
  punch="Medical measures for IAH; for compartment syndrome, find the cause: a perforation or bleed is opened now, while fluid-driven disease is drained and dried first and opened only if organ failure persists.",
)

L['IAH-12'] = dict(
  sub="Intra-abdominal hypertension → Management → Outcomes",
  step=5,
  intro="Step 5 ends with outcomes: what the pressure predicts and what protocolised care achieved. No question is linked; the Cheatham figures are the likely question.",
  parts=[
    ('a', "**Hypertension alone: not by itself a predictor of organ failure.** The same pressure is tolerated by an obese patient and fatal in a stiff post-operative abdomen; what matters is organ dysfunction and perfusion pressure."),
    ('b', "**In compartment syndrome, the probability of death rises with the actual pressure.** Once organ failure is present, higher pressures mean worse outcomes, which is why the algorithm escalates by grade."),
    ('c', "**Following the WSACS guideline raised survival to discharge from 50% to 72% (478 patients).** Cheatham and Safcsak (Crit Care Med 2010) introduced a continually revised management algorithm; same-admission primary fascial closure also rose, from 59% to 81%. This underpins WSACS’s recommendation for protocolised monitoring and management (1C)."),
  ],
  mimic=[
    ("After decompression: reperfusion syndrome vs bleeding", "Reperfusion syndrome is sudden hypotension, hyperkalaemia and acidosis as ischaemic tissue is reperfused and systemic resistance falls; fill and prepare vasopressors before the fascia is opened."),
  ],
  traps=[
    ("“Protocolised care raised survival from 72% to 50%”", "The other way: 50% to 72% (your notes transpose them)."),
  ],
  decode=[
    ("Effect of the WSACS protocol on survival to discharge? [pattern]", "50% to 72% (Cheatham 2010)."),
  ],
  punch="Pressure alone predicts little, but once organs fail, mortality climbs with the pressure, and protocolised care raised survival from half to nearly three-quarters.",
)

L['IAH-13'] = dict(
  sub="Intra-abdominal hypertension → Sweep → True or false",
  step=2,
  intro="The sweep collects the deck’s commonest errors in one place. Its one linked question is the transducer item (54% right).",
  parts=[
    ('a', "**False: normal is 5–7 mmHg.** Not zero in the critically ill (IAH-01)."),
    ('b', "**False: IAH starts at 12 or more.** Over 20 is the compartment syndrome threshold, not IAH."),
    ('c', "**False: compartment syndrome is over 20 plus organ dysfunction.** Grade IV is a pressure band, not a syndrome (IAH-03)."),
    ('d', "**False: 25 mL.** More over-stretches the bladder and raises the reading (IAH-02)."),
    ('e', "**False: mid-axillary line, supine.** The symphysis was the original Kron reference; head-up raises the reading."),
    ('f', "**True: APP = MAP − IAP.** And the filtration gradient is MAP − 2 × IAP (IAH-04)."),
    ('g', "**False: oliguria begins at 15 mmHg.** Anuria is at about 30."),
    ('h', "**False: CVP reads falsely high.** Part of the abdominal pressure is transmitted to the chest (IAH-09)."),
    ('i', "**False: burns cause secondary compartment syndrome.** The cause lies outside the abdomen (IAH-05)."),
  ],
  mimic=[
    ("Oliguria at 15 vs anuria at 30", "The kidney fails progressively; urine falls well before compartment syndrome is defined."),
  ],
  traps=[
    ("“Zero at the symphysis pubis”", "Mid-axillary line (DocT, 54% right)."),
  ],
  decode=[
    ("Bladder pressure measurement: which is TRUE? [DocT QBank]", "Measured at end-expiration."),
    ("ACS threshold vs IAH threshold? [pattern]", "Over 20 with organ failure vs 12 or more."),
  ],
  punch="Normal 5–7, IAH 12, ACS over 20 with organ failure; 25 mL, supine, mid-axillary, end-expiration; CVP falsely high; burns are secondary.",
)

FLAGS = {}
FLAGS['IAH-03'] = "Card is correct. The linked DocT question (perforated ulcer, IAP 26, oliguria, hypotension) keys ‘decompressive laparotomy after failure of conservative measures’; the right answer is immediate laparotomy (taught under IAH-11). GT1o prints bladder pressures in cmH2O for options A–C (22 cmH2O ≈ 16 mmHg), so taken literally the keyed patient C is below the ACS threshold; the question almost certainly means mmHg, and C wins on organ failure."
FLAGS['IAH-11'] = "Card is correct (a: WSACS-based algorithms say at least every 4–6 hours, card says 4; harmless; e: stopping below 12 matches WSACS-based protocols, the WSACS 2013 figure itself was not re-opened). DocT key C for the perforated-ulcer question (QBank, CGT4 Q33, GT6 Q105) is wrong: immediate laparotomy (B). DocT’s TAC key ‘closed within 48–72 h’ is not a guideline figure; WSACS says early or same-admission (1D), WSES 2018 says as soon as possible, with early closure ‘commonly defined’ as within 4–7 days (text, not a graded recommendation; the card-layer line’s ‘ideally’ slightly overstates it), and its 24–48 h figure is the re-look interval. CGT4 pancreatitis key ‘immediate laparotomy’ overstates the stepwise guidance but is the best option given."
FLAGS['IAH-04'] = "Card is correct. b: APP ≥60 is observational (Cheatham); WSACS 2013 makes no recommendation on APP as a target (the 2007 guideline suggested 50–60), as the watch line says."
FLAGS['IAH-09'] = "c: transmural plateau = plateau − 0.5 × IAP is the Malbrain teaching; some sources (LITFL) subtract the whole IAP. Transmission varies (about 20–80%); not an error, noted in the explanation."
FLAGS['IAH-06'] = "Minor attribution: a combines two studies (1% of all trauma ICU admissions is Hong 2002, 706 patients; 14% of shocked torso trauma is Balogh 2003, 188 patients, of whom 8% had secondary ACS); b’s 9% is Balogh 2002. The predictor cut-offs in c–d come from the Balogh 2003 full text and could not be re-checked online."
