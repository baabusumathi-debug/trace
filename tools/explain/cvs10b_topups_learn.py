# CVS10B top-up cards — Explain v3 ("Learn" depth), same fields and voice as cvs10b_learn.py.
# Fields: sub, step (index into cvs10b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part (one part per answer line, in order); disagreements with a card go in FLAGS, not in the text.
# Source: cvs_topups.json → "CVS10B": T_bf76f00d (Wellens vs de Winter; Marrow QB21-Q14, QB21-Q27). The source stems were not opened; decode items follow the top-up question.
# Reviewer check, 19 Nov 2026: Wellens (StatPearls ‘Wellens Syndrome’): biphasic (about 25%) or deep symmetric (about 75%) T waves in V2–V3, ST isoelectric or <1 mm, preserved R
# progression, no precordial Q, recorded pain-free, markers normal or slightly raised; in the original de Zwaan series about 75% of medically treated patients had an anterior MI within
# weeks; stress testing can precipitate MI. de Winter (NEJM 2008, as summarised by ekgdx.com): 1–3 mm upsloping J-point ST depression in V1–V6 into tall symmetric T waves, 1–2 mm ST
# elevation in aVR, about 2% of proximal LAD occlusions; proposed mechanisms include delayed subendocardial repolarisation from failed ATP-sensitive K⁺ channel activation. ESC 2023 names
# Wellens’ sign (severe proximal LAD stenosis) in its NSTE-ACS ECG section and hyperacute T waves among ischaemic changes; it does not name de Winter, and AHA/ACC 2025 names neither.

T = {}

T['T_bf76f00d'] = dict(
  sub="ACS → ECG → Wellens vs de Winter (proximal LAD)",
  step=3,
  intro="Step 3 is occlusion or near-occlusion that the ST-elevation rule misses, and both of these patterns belong to the proximal LAD. Wellens is the footprint of an artery that occluded and reopened; de Winter is an artery that is occluded now. Two Marrow questions test telling them apart.",
  parts=[
    ('a', "**Wellens: deep symmetric or biphasic T waves in V2–V3 with isoelectric or <1 mm ST, preserved R waves and no Q waves, usually recorded pain-free → critical proximal LAD stenosis: angiography, avoid stress testing.** The T-wave changes are reperfusion changes after a transient occlusion, which is why they appear when the pain has gone and why R waves are preserved (little myocardium has died). The lesion is critical: in the original series about three-quarters of medically treated patients had an anterior MI within weeks, and a stress test can provoke it. ESC 2023 names Wellens’ sign among the NSTE-ACS ECG findings of severe proximal LAD stenosis."),
    ('b', "**de Winter: 1–3 mm UPsloping ST depression at the J point in V1–V6 with tall symmetric T waves and ~1 mm ST elevation in aVR → acute proximal LAD occlusion = STEMI equivalent → primary PCI.** The occlusion is present, but the injury current does not lift the ST segment; the mechanism is unsettled (delayed subendocardial repolarisation from failure of ATP-sensitive potassium channels to open, or an anatomical variant of the Purkinje fibres, have been proposed). The tall T waves are hyperacute. It is uncommon, about 2% of proximal LAD occlusions. It is treated as a STEMI despite not meeting the criteria."),
    ('c', "**ST elevation in aVR is not a Wellens feature.** aVR elevation belongs to de Winter (and to the left main / three-vessel pattern, MI-25); Wellens has an isoelectric ST and changes only in the T wave."),
  ],
  mimic=[
    ("Wellens vs de Winter", "Wellens: pain-free, T-wave inversion, no ST depression, a stenosis that needs urgent angiography; de Winter: ongoing pain, upsloping ST depression with tall T waves, an occlusion that needs primary PCI now."),
    ("de Winter vs NSTE-ACS ST depression", "NSTE-ACS depression is horizontal or downsloping with ordinary T waves; de Winter is upsloping with tall symmetric T waves across V1–V6."),
  ],
  traps=[
    ("“Wellens has ST elevation in aVR”", "That is de Winter or left main ischaemia; Wellens is a T-wave pattern with an isoelectric ST."),
    ("“Wellens is low risk because the patient is pain-free: arrange a stress test”", "Pain-free is the typical setting; the stenosis is critical, and stress testing can precipitate an infarct."),
  ],
  decode=[
    ("Pain-free, deep symmetric T inversion in V2–V3, preserved R, no Q waves [Marrow]", "Wellens: critical proximal LAD stenosis; angiography, no stress test."),
    ("Ongoing pain, upsloping J-point depression V1–V6 with tall T waves, aVR elevation [Marrow]", "de Winter: acute proximal LAD occlusion; primary PCI."),
  ],
  punch="Wellens is a pain-free T-wave pattern after a reopened LAD and needs angiography; de Winter is upsloping ST depression with tall T waves from an LAD that is shut now and needs primary PCI.",
)
