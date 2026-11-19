# CVS10E top-up cards — Explain v3 ("Learn" depth), same fields and voice as cvs10e_learn.py.
# Fields: sub, step (index into cvs10e_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part (one part per answer line, in order); disagreements with a card go in FLAGS, not in the text.
# Source: cvs_topups.json → "CVS10E": T_08cd9563 (retroperitoneal bleed after femoral access; Marrow QB59-Q12). The source stem was not opened; decode items follow the top-up question.
# From standard references without a fresh check (confident): retroperitoneal haematoma after femoral access in well under 1% of procedures; risk factors high (suprainguinal) puncture,
# female sex, low body weight, anticoagulation/GP IIb/IIIa, large sheaths; presentation hypotension, back/flank/abdominal pain, falling Hb, often no groin swelling; non-contrast CT
# abdomen/pelvis; most managed conservatively; endovascular covered stent or embolisation for ongoing bleeding; radial access 1, A in ACC/AHA 2025 (checked 19 Nov 2026, see cvs10e_learn.py).
T = {}

T['T_08cd9563'] = dict(
  sub="Cardiology → PCI complications → Retroperitoneal bleed after femoral access",
  step=5,
  intro="Step 5 says go radial, and this is the main reason: a femoral puncture above the inguinal ligament can bleed into the retroperitoneum, where nothing can be compressed and nothing shows at the groin. The question is a patient who becomes hypotensive hours after PCI with a clean groin.",
  parts=[
    ('a', "**Retroperitoneal haematoma: high puncture above the inguinal ligament; women, obesity, anticoagulation.** Above the ligament the external iliac artery lies behind the peritoneum with no femoral head behind it to press against, so blood tracks up into the retroperitoneal space instead of forming a visible groin haematoma. Women and patients at extremes of body size (low body weight is the classic risk; in obesity the ligament is hard to locate and punctures land high), full anticoagulation, GP IIb/IIIa inhibitors and large sheaths add to the risk."),
    ('b', "**Diagnose with CT abdomen/pelvis; resuscitate, stop/reverse anticoagulation.** Back, flank or lower abdominal pain with hypotension, tachycardia and a falling haemoglobin after femoral access is this until proved otherwise; CT of the abdomen and pelvis shows the haematoma, and a contrast phase shows whether it is still bleeding. Ultrasound of the groin is often normal and does not exclude it. Fluids and blood, stop the heparin (protamine if needed) and weigh stopping antiplatelets against the stent-thrombosis risk with the cardiologist. Most stop with these measures."),
    ('c', "**Covered stent or embolisation (or surgery) if ongoing bleeding.** Persistent instability or contrast leaking on CT means an active arterial bleed; an endovascular covered stent across the puncture or embolisation of a branch seals it, and open repair is the fallback."),
  ],
  mimic=[
    ("Retroperitoneal bleed vs groin haematoma or pseudoaneurysm", "A groin haematoma or pseudoaneurysm is visible or palpable at the groin (a pseudoaneurysm pulsates with a bruit, diagnosed by duplex); a retroperitoneal bleed has a quiet groin, back pain and shock."),
    ("Retroperitoneal bleed vs vagal reaction after sheath removal", "Vagal: bradycardia and hypotension at sheath pull, settles with atropine and fluids. Bleed: tachycardia, falling Hb, hours later."),
  ],
  traps=[
    ("“No groin haematoma, so the access site is not the cause”", "A high puncture bleeds backwards into the retroperitoneum; the groin is typically normal."),
    ("“Hypotension after PCI: give inotropes for pump failure”", "Check the haemoglobin and CT first; after femoral access the first cause to exclude is bleeding."),
  ],
  decode=[
    ("Hypotension with back/flank pain hours after femoral-access PCI, no visible groin haematoma [Marrow]", "Retroperitoneal haematoma: CT abdomen/pelvis, resuscitate, stop or reverse anticoagulation; covered stent or embolisation if it continues."),
  ],
  punch="Shock with back or flank pain after femoral PCI and a normal groin is a retroperitoneal bleed from a high puncture: CT, blood, stop the heparin, and seal it with a covered stent or embolisation if it keeps bleeding; radial access prevents it.",
)

FLAGS = {
  'T_08cd9563': "a: ‘obesity’ as a risk factor — the classic risk factor is LOW body weight (with female sex, high puncture, anticoagulation, large sheaths); obesity raises the chance of a high puncture because the ligament is hard to locate. Not wrong as a practical point; the explanation gives both.",
}
