# RESP01B top-up cards — Explain v3 ("Learn" depth), same fields and voice as resp01b_learn.py.
# Fields: sub, step (index into resp01b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions come from map/out/all_rows.json and the DocT GT/QBank files (the top-up's own src) plus qpack/RESP01B.md.
T = {}

T['T_d7c5bd2c'] = dict(
  sub="Respiratory → Non-invasive support → CPAP, BiPAP and who must not get NIV",
  step=1,
  intro="Step 1 is support before the tube. Beside HFNC (ARDS-14), the two mask modes are CPAP and BiPAP, and they do different jobs: one pressure that holds the lung open, or two pressures that also help each breath in. The exam asks what each pressure does, then hands you a patient in whom any mask is the wrong answer.",
  parts=[
    ('a', "**CPAP = one continuous pressure: recruits alveoli, raises FRC and oxygenation (cardiogenic pulmonary oedema, OSA).** The same pressure in inspiration and expiration splints collapsed alveoli open and raises FRC, so shunt falls; in cardiogenic oedema it also lowers LV afterload and preload. It gives no inspiratory help, so it does little for CO₂."),
    ('b', "**BiPAP = IPAP + EPAP; pressure support (IPAP − EPAP) unloads breathing and clears CO₂, EPAP recruits and oxygenates (and offsets auto-PEEP).** The difference between the two levels is the inspiratory assist: it enlarges tidal volume and takes over muscle work, which is why it is the mode for hypercapnia. EPAP is simply CPAP at end-expiration; in COPD it also balances intrinsic PEEP so the patient triggers more easily (COPD-03)."),
    ('c', "**Contraindications: GCS <8 or cannot protect the airway, apnoea/arrest, vomiting or upper GI bleed, shock, agitation/non-cooperation, facial trauma, undrained pneumothorax.** A mask needs a patient who breathes, keeps the airway clear and tolerates it. Positive pressure into the stomach risks aspiration, raises intrathoracic pressure in a failing circulation, and enlarges an undrained pneumothorax."),
    ('d', "**Cardiogenic shock with confusion and hypoxaemic oedema → intubate, not NIV; overdose with GCS <8 and RR 6 → intubate.** Cardiogenic oedema is the best indication for CPAP, but shock and confusion turn it into a contraindication. The overdose patient cannot protect the airway or generate breaths for a mask to support."),
  ],
  mimic=[
    ("CPAP vs pressure support", "CPAP raises FRC and oxygenation; pressure support helps inspiration and tidal volume. For low FRC in a spontaneously breathing patient, CPAP is the answer."),
  ],
  traps=[
    ("“BiPAP works by decreasing lung compliance”", "It recruits lung and improves compliance; the distractor reverses the physiology."),
    ("“BiPAP delivers a constant volume”", "It is pressure-set; tidal volume varies with effort and mechanics."),
    ("“Hypoxaemic, low FRC, breathing spontaneously — pressure support”", "CPAP raises FRC; pressure support only adds inspiratory help (DocT GT)."),
    ("“Switch a ventilated severe ARDS patient to BiPAP”", "The DocT stem is clinically odd: NIV is reserved for mild ARDS (ARDS-04, ARDS-14); answer the pressure question it asks."),
  ],
  decode=[
    ("Characteristic feature of BiPAP [DocT; DocT GT]", "Two levels: higher inspiratory, lower expiratory pressure (80%)."),
    ("Primary advantage of BiPAP in this patient [DocT]", "Spontaneous breathing with support in both phases (91%)."),
    ("Spontaneously breathing, hypoxaemic from low FRC — best mode? [DocT GT]", "CPAP."),
    ("Propafenone overdose, GCS <8, RR 6; cardiogenic shock, confused, hypoxaemic oedema [Marrow]", "Intubate in both."),
  ],
  punch="CPAP holds the lung open, the gap between IPAP and EPAP breathes for the patient; and a patient who cannot protect the airway, breathe, cooperate or hold a blood pressure needs a tube, not a mask.",
)

FLAGS = {}
