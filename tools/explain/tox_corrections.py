# T-084: corrections to the Toxicology card text, found by the Explain v2 writers and independent reviewers (5 Nov 2026).
# Naven approved showing them (5 Nov: "wherever you find corrections, put it there… with a mention in the explanation").
# Card text itself is never edited: each item shows as a CORRECTION box on the card's answer and in the Explain pane.
# Format: FIX[deck][code] = [(what the card says, what is right — with the source)]
FIX = {
 'TOX02': {
  'APAP-01': [("WATCH: pesticides “dominate”", "Pesticides dominate poisoning deaths in India, but acute liver failure in India is mostly viral hepatitis (HEV, HBV) and anti-TB drug injury.")],
  'APAP-03': [("Anticonvulsants listed as CYP2E1 inducers", "Only isoniazid and alcohol act mainly on CYP2E1; phenytoin, carbamazepine, phenobarbital and rifampicin induce other CYP isoforms. The evidence that inducers raise risk is weak (the UK dropped its high-risk line in 2012).")],
  'APAP-04': [("Repeated ingestion: 7.5 g, or 4 g with risk factors, in 24 h", "Guidelines use ≥10 g or 200 mg/kg in 24 h, or ≥6 g or 150 mg/kg a day for ≥48 h (US consensus 2006, Australia–NZ); Australia–NZ adds ≥4 g or 100 mg/kg in 24 h with risk factors. The level >20 µg/mL and ALT >50 triggers are right.")],
  'APAP-05': [("Stage IV usually complete by day 7", "Recovery runs from about day 4–5 to 2 weeks; the liver tissue takes up to 3 months to heal (Goldfrank’s).")],
  'APAP-08': [("Charcoal within 4 hours", "The usual window is 1 hour; Australia–NZ uses 2 hours for a toxic dose and up to 4 hours only for >30 g or modified-release tablets.")],
  'APAP-11': [("Lactate after 1 hour of fluid resuscitation", "Bernal 2002: lactate >3.5 mmol/L about 4 h after admission, or >3.0 mmol/L about 12 h after full fluid resuscitation.")],
 },
 'TOX03A': {
  'PEST-01': [("Up to 300,000 deaths a year from organophosphates", "About 250,000–370,000 deaths a year are from all pesticide self-poisoning, organophosphates the largest share.")],
  'PEST-11': [("Pralidoxime works if given in time", "The evidence is insufficient either way (Cochrane): the Sri Lankan placebo-controlled trial of the WHO regimen showed no benefit, a small Indian trial of 1 g/h for 48 h showed fewer deaths. WHO regimen: 30 mg/kg (~2 g) over 30 min, then 8 mg/kg/h.")],
  'PEST-12': [("FFP: harmful", "The only randomised pilot (Vellore 2010) showed no benefit, not proven harm: FFP is not recommended. For the exam’s ‘which is harmful’ it is still the intended answer."),
              ("Magnesium: no scientific data", "There are four small randomised trials and cohorts with a possible mortality benefit (Brvar 2018), but the evidence is still insufficient to recommend it.")],
 },
 'TOX03B': {
  'PEST-15': [("Shock and multi-organ failure within 30 minutes", "Vomiting starts within minutes, but shock usually develops over 1–6 hours and most deaths come within 24 hours.")],
  'PEST-16': [("WATCH: vegetable oil lavage", "Digestible oils increase phosphorus absorption; older texts used liquid paraffin (not absorbed). Gastric lavage of any kind is not routine now.")],
  'PEST-17': [("A 4-hydroxycoumarin level covers the superwarfarins", "Chlorophacinone is an indandione, not a 4-hydroxycoumarin. The INR rises at 24–48 h, but bleeding may only appear days later.")],
  'PEST-19': [("Skin contact is not life-threatening", "True for intact skin and diluted spray; fatal poisoning has been reported after prolonged contact of the concentrate with damaged skin.")],
 },
 'TOX04': {
  'REC-01': [("In children: inhalants", "Inhalants are the only class used more by children than by adults (about 1.17% vs 0.58%, 2019 national survey); they are not the commonest substance in children.")],
  'REC-03': [("Naloxone to a maximum of 2 mg", "2 mg is not a ceiling: up to about 10 mg is given before opioid toxicity is ruled out (more often needed with fentanyl analogues).")],
  'REC-09': [("Flunitrazepam is detected as a benzodiazepine; lasts 4–6 hours", "Routine urine benzodiazepine screens often miss it (specific assays needed), and sedation and amnesia often last 8–12 hours or more.")],
  'REC-13': [("Cyproheptadine 2 mg per dose to a maximum of 12 mg", "Standard regimen (Boyer & Shannon, NEJM 2005): 12 mg first, then 2 mg every 2 hours while symptoms persist, then 8 mg 6-hourly — about 12–32 mg a day.")],
  'REC-15': [("WATCH: temperature climbs 1 °C every 10 minutes; all inhaled agents except nitrous oxide", "In fulminant malignant hyperthermia the temperature rises about 1–2 °C every 5 minutes. Triggers are the volatile agents and suxamethonium (nitrous oxide and xenon do not trigger); most cases start in theatre or within about an hour after.")],
 },
 'TOX05': {
  'SNAKE-01': [("35,000–50,000 deaths a year", "The Indian guideline 2017 estimates about 45,900 a year; the Million Death Study (2020) about 58,000 a year.")],
  'SNAKE-02': [("Sea snakes: Hydrophidae, myotoxic", "Sea snakes are now classed within Elapidae, and their venom is neurotoxic as well as myotoxic.")],
  'SNAKE-03': [("Hyaluronidase: tissue destruction", "Hyaluronidase is the spreading factor; the tissue destruction comes mainly from metalloproteinases, phospholipase A₂ and cytotoxins.")],
  'SNAKE-09': [("20WBCT every 30 min for 3 h, then hourly", "That is the 2009 protocol. Indian guideline 2017: 6 hours after the loading dose of ASV, and in suspected bites hourly for 3 h, then 6-hourly up to 24 h.")],
  'SNAKE-10': [("Neostigmine 0.5–2 mg IM", "Indian guideline 2017: atropine 0.6 mg, then neostigmine 1.5 mg IV; then 0.5 mg with atropine every 30 min for 5 doses (child: atropine 0.05 mg/kg, neostigmine 0.04 mg/kg, repeat 0.01 mg/kg). Positive test: ≥50% recovery of ptosis at 1 hour. WHO gives neostigmine IM (about 0.02 mg/kg).")],
  'SNAKE-11': [("Premedication not stated as routine", "SC adrenaline 0.25 mg is now advised routinely before ASV (WHO SEARO 2016; Indian 2017 except known hypertensives). Freeze-dried ASV keeps 3–5 years.")],
  'SNAKE-13': [("Repeat 5–10 vials 6-hourly", "Indian guideline 2017: neurotoxic — 10 vials over 30 min, another 10 at 1 h if no better (maximum 20). Haemotoxic low-dose — 10 vials (Russell’s) or 6 (saw-scaled), then 2 vials 6-hourly; high-dose — 10, then 6 vials 6-hourly.")],
  'SNAKE-15': [("IM adrenaline if severe", "IM adrenaline 0.5 mg (child 0.01 mg/kg) comes first, at the earliest sign of anaphylaxis; chlorphenamine and hydrocortisone follow as add-ons.")],
 },
 'TOX06': {
  'ONC-06': [("Tocilizumab: maximum 3 doses", "At most 3 doses in 24 hours and 4 doses in total.")],
  'ONC-09': [("Grade 4 ICANS: as grade 3", "Grade 4 needs high-dose methylprednisolone 1 g a day (usually 3 days), not dexamethasone alone (ASCO/NCCN).")],
  'ONC-10': [("Steroid-refractory: no response in 5–7 days", "Now: no improvement after about 48–72 hours of high-dose steroids (ASCO/ESMO)."),
             ("Grade 3–4: stop permanently", "Permanent for grade 4 and for myocarditis of any grade; after some grade 3 events (e.g. anti-PD-1 colitis) the drug can be restarted once the event settles to grade 1.")],
  'ONC-11': [("Trastuzumab causes ACS", "Trastuzumab causes (usually reversible) left-ventricular dysfunction, not ACS. The ACS drugs are 5-FU/capecitabine (coronary spasm) and bevacizumab (arterial thrombosis)."),
             ("Checkpoint myocarditis row", "Add: stop the checkpoint inhibitor permanently at any grade, and give methylprednisolone 500–1000 mg a day.")],
 },
 'RESP01A': {
  'ARDS-04': [("WATCH: PEEP below 5 and not on HFNO", "Two definitions are mixed here. Berlin 2012 needs invasive ventilation or CPAP/NIV with PEEP ≥5 (CPAP allowed for mild only) and never accepts HFNO; the 2023 global definition accepts HFNO ≥30 L/min, but does not grade non-intubated patients.")],
  'ARDS-07': [("Transfusion (TRALI) listed as a direct cause", "Standard sources (Ware & Matthay; the Berlin risk-factor list) put transfusion with the indirect causes: the injury reaches the lung through the blood.")],
 },
}
