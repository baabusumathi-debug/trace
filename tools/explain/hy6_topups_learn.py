# HY6 top-up cards — Explain v3 ("Learn" depth), same fields and voice as hy6_learn.py.
# Fields: sub, step (index into hy6_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions come from each top-up's own src (DocT QBank, DocT Grand Tests, Marrow) plus qpack/HY6.md.
# Checked online on 20 Nov 2026: ACG–CAG 2022 antithrombotics in GI bleeding (do not hold secondary-prevention aspirin; resume the day haemostasis is confirmed; suggest against platelet transfusion).
# From standard references without a fresh check: ACG 2015 small-bowel bleeding guideline (Gerson); detection rates of red-cell scintigraphy (0.1–0.5 mL/min), CTA (0.3–0.5) and catheter angiography
# (0.5–1 mL/min); Laine and Peterson 1994 Forrest rebleed rates; ESGE 2021 NVUGIH (dual therapy, high-dose PPI for 72 h, intermittent bolus non-inferior to infusion — Sachar 2014; DAPT: continue aspirin,
# interrupt the P2Y12 inhibitor and resume within 5 days); Heyde syndrome.
# Second check (20 Nov 2026): ACG 2015 small-bowel bleeding (capsule yield 38–83%, best within 48–72 h; Medtronic-hosted ACG summary); OCEAN = Goltstein, Gastroenterology 2024 (n 62, octreotide LAR
# 40 mg 4-weekly, mean 11.0 vs 21.2 units transfused; gi.org EBGI summary); ACG–CAG 2022 via AAFP summary (aspirin continued, platelets possibly harmful, vitamin K ineffective).
T = {}

T['T_2659f047'] = dict(
  sub="GI → Bleeding → Suspected small-bowel (obscure) bleeding",
  step=4,
  intro="Step 4 has a gap between the two scopes: the bleed that OGD and colonoscopy both miss. Most of these sources lie in the small bowel, out of reach of standard endoscopes, so the pathway is about which test can see there and which can treat. Five bank questions test the order of tests and the commonest lesion.",
  parts=[
    ('a', "**Treat as suspected small-bowel bleeding (~5–10% of GI bleeds); repeat a scope only if the first was inadequate.** The old term ‘obscure’ GI bleeding is now ‘suspected small-bowel bleeding’. A second look is worth it when the first scope was poor (blood obscuring the view, poor prep), because many ‘small-bowel’ sources turn out to be missed lesions within reach (Cameron erosions, Dieulafoy, angiodysplasia)."),
    ('b', "**Stable → capsule endoscopy first (highest yield, non-invasive).** The capsule sees the whole small bowel in up to 90% of patients, with a diagnostic yield of 38–83% (ACG 2015), highest when it is swallowed within 48–72 h of an overt bleed, while the lesion is still bleeding or freshly marked. It cannot treat, and it is avoided if a stricture is suspected (retention)."),
    ('c', "**Capsule positive → device-assisted (balloon) enteroscopy to treat the lesion.** Single- or double-balloon enteroscopy pleats the small bowel over the scope, so the lesion the capsule found can be burnt, clipped or biopsied."),
    ('d', "**Brisk bleeding or unstable → CT angiography, then catheter embolisation.** A capsule takes hours; the unstable patient needs a test that finds active extravasation (about 0.3–0.5 mL/min) within minutes and guides embolisation, as in GIN-10."),
    ('e', "**Stable, slow intermittent bleed (0.1–0.5 mL/min) with negative scopes → Tc-99m red-cell scintigraphy: most sensitive and images for up to 24 h, but localises poorly.** Labelled red cells stay in the circulation, so delayed images can catch a bleed that starts and stops; but blood moves along the bowel between images, so the site is only approximate and it cannot treat."),
    ('f', "**Commonest lesion in the elderly: angiodysplasia (right colon/small bowel; CKD, vWD, aortic stenosis = Heyde); recurrent bleeding despite endotherapy and unfit for surgery → octreotide (or thalidomide).** In aortic stenosis, shear stress across the valve breaks up the largest von Willebrand multimers (acquired type 2A vWD), so these fragile vessels bleed; valve replacement often stops it. Octreotide reduces splanchnic flow and angiogenesis; in OCEAN (Goltstein, Gastroenterology 2024; 62 transfusion-dependent patients), long-acting octreotide 40 mg every 4 weeks for a year cut transfusion needs from about 21 to 11 units. Thalidomide blocks VEGF. In younger patients, tumours and Meckel’s diverticulum are commoner."),
  ],
  table=dict(title="Which test sees which bleeding rate",
    head=["Test", "Detects", "Treats?"],
    rows=[["Red-cell scintigraphy", "0.1–0.5 mL/min (most sensitive, up to 24 h)", "No; poor localisation"],
          ["CT angiography", "0.3–0.5 mL/min", "No, but guides embolisation"],
          ["Catheter angiography", "0.5–1 mL/min", "Yes (embolisation)"],
          ["Capsule endoscopy", "Mucosal lesions of the whole small bowel", "No"],
          ["Balloon enteroscopy", "Lesions the capsule found", "Yes"]]),
  mimic=[
    ("Capsule vs enteroscopy", "The capsule finds; the balloon enteroscope treats. Capsule first in the stable patient."),
    ("Scintigraphy vs CTA", "Scintigraphy for slow, intermittent bleeding in a stable patient; CTA for brisk bleeding or instability."),
  ],
  traps=[
    ("“Stable, negative OGD and colonoscopy — push straight to mesenteric angiography”", "Angiography needs a brisk active bleed and is invasive; the stable patient gets capsule endoscopy first."),
    ("“Red-cell scan localises the bleed precisely enough for surgery”", "It is the most sensitive but localises poorly; a positive scan is followed by CTA or angiography."),
  ],
  decode=[
    ("Recurrent bleeding, normal OGD and colonoscopy, stable — next test? [DocT, Marrow]", "Capsule endoscopy."),
    ("Stable, intermittent slow bleed, scopes negative — most sensitive localising test? [DocT GT]", "Tc-99m labelled red-cell scintigraphy."),
    ("Elderly with aortic stenosis and recurrent GI bleeding — lesion and syndrome? [DocT GT]", "Angiodysplasia; Heyde syndrome (acquired vWD)."),
  ],
  punch="When both scopes are negative, look in the small bowel: capsule first if stable, balloon enteroscopy to treat, CTA and embolisation if brisk, red-cell scan for slow intermittent bleeding, and think angiodysplasia in the elderly.",
)

T['T_b3c4366a'] = dict(
  sub="GI → Bleeding → Forrest classification of bleeding ulcers",
  step=4,
  intro="Step 4 at the endoscope: once an ulcer is found, what it looks like predicts whether it will bleed again, and that decides whether to treat it. The Forrest grades are ordered by rebleeding risk, and the two bank questions test where treatment stops.",
  parts=[
    ('a', "**Ia spurting / Ib oozing: active bleeding → endoscopic therapy (dual: adrenaline + clip or thermal).** Adrenaline alone constricts and tamponades only for a while; adding a mechanical clip or thermal coagulation closes the vessel and lowers rebleeding. Untreated, active bleeding rebleeds in over half."),
    ('b', "**IIa visible vessel: rebleed ~40–50% → endoscopic therapy.** The ‘vessel’ is a pigmented protuberance, the plug in the side of an artery; its high rebleeding rate makes it as much an indication as active bleeding."),
    ('c', "**IIb adherent clot: ~20–30% → remove clot and treat the base if possible (high-dose PPI alone is acceptable).** A clot that resists washing may hide a visible vessel; lifting it and treating what lies beneath lowers rebleeding, but intensive PPI without removal is an accepted alternative."),
    ('d', "**IIc flat pigmented spot (~10%) and III clean base (<5%) → no endotherapy, oral PPI, early feeding.** These lesions are low risk; endoscopic therapy adds risk without benefit, and the patient can eat and often go home early."),
    ('e', "**After endotherapy of Ia–IIb: high-dose PPI for 72 h (intermittent IV bolus is non-inferior to infusion).** A gastric pH above 6 keeps the clot stable (pepsin and acid dissolve it); 72 h covers the period when most rebleeding happens. Intermittent high-dose boluses are as good as a continuous infusion."),
  ],
  table=dict(title="Forrest class, rebleeding risk and action",
    head=["Class", "Finding", "Rebleed", "Endotherapy?"],
    rows=[["Ia / Ib", "Spurting / oozing", "Over 50% untreated", "Yes"],
          ["IIa", "Non-bleeding visible vessel", "~40–50%", "Yes"],
          ["IIb", "Adherent clot", "~20–30%", "Remove clot, treat base (or PPI alone)"],
          ["IIc", "Flat pigmented spot", "~10%", "No"],
          ["III", "Clean base", "<5%", "No"]]),
  mimic=[
    ("IIa vs IIc", "A raised visible vessel (IIa) is treated; a flat spot (IIc) is not."),
  ],
  traps=[
    ("“Flat pigmented spot — clip it to be safe”", "IIc rebleeds in about 10%; endotherapy is not indicated."),
    ("“Adrenaline injection alone for a spurting vessel”", "Monotherapy with adrenaline is inferior; combine it with a clip or thermal therapy."),
  ],
  decode=[
    ("Ulcer with a non-bleeding visible vessel — Forrest class and management? [DocT]", "IIa; endoscopic therapy then high-dose PPI."),
    ("Which Forrest class does not need endoscopic therapy? [DocT GT]", "IIc and III."),
  ],
  punch="Treat Forrest Ia, Ib and IIa at the scope with dual therapy, lift and treat IIb if possible, leave IIc and III alone, and follow endotherapy with 72 hours of high-dose PPI.",
)

T['T_9fa98033'] = dict(
  sub="GI → Bleeding → Antiplatelets after GI bleeding with a recent stent",
  step=4,
  intro="Step 4 meets cardiology: the patient whose bleeding treatment risks killing him by another route. A drug-eluting stent placed 20 days ago is not yet covered by endothelium, so stopping both antiplatelets invites stent thrombosis, which is often a fatal MI. The bank question tests what to keep.",
  parts=[
    ('a', "**Never stop aspirin: stopping DAPT in the first month after a stent carries a high risk of stent thrombosis (often fatal MI).** The stent struts stay bare to platelets until endothelium covers them; that risk is highest in the first 30 days. A GI bleed can usually be controlled endoscopically, whereas stent thrombosis carries a high mortality."),
    ('b', "**DocT keys: continue DAPT.** In the exam, ‘continue DAPT’ is the answer for a recent stent with a GI bleed being controlled at endoscopy."),
    ('c', "**ESGE 2021 / ACG–CAG 2022: if bleeding is life-threatening with high-risk stigmata, interrupt the P2Y12 inhibitor briefly and resume within ≤5 days, with cardiology input.** Aspirin is never stopped; the P2Y12 inhibitor (clopidogrel, ticagrelor, prasugrel) may be held for a short time when the bleed is severe, because the risk of a few days without it is smaller than continued haemorrhage."),
    ('d', "**Control the bleed: urgent endoscopic haemostasis + high-dose IV PPI; platelet transfusion does not help.** Transfused platelets are inhibited by circulating drug (especially ticagrelor) and observational data link them to higher mortality; ACG–CAG suggests against them."),
    ('e', "**Primary-prevention aspirin can be stopped; secondary-prevention aspirin restarts as soon as haemostasis is secure.** For secondary prevention, ACG–CAG suggests not holding aspirin at all, and if it was held, restarting it on the day haemostasis is confirmed; in Sung 2010, stopping aspirin after ulcer haemostasis raised mortality."),
  ],
  mimic=[
    ("Recent stent (under 1 month) vs remote stent or primary prevention", "Recent stent: keep aspirin and usually the P2Y12 inhibitor; primary prevention: stop aspirin."),
  ],
  traps=[
    ("“Stop both antiplatelets until the ulcer heals”", "Stent thrombosis is more lethal than the bleed; aspirin is never stopped and DAPT is continued if possible."),
    ("“Give platelets to reverse clopidogrel”", "No benefit and possible harm; control the bleed endoscopically."),
  ],
  decode=[
    ("GI bleed on aspirin + clopidogrel, stent 20 days ago — antiplatelets? [DocT GT]", "Continue DAPT (never stop aspirin)."),
  ],
  punch="With a stent placed in the last month, never stop aspirin and keep DAPT if possible, hold the P2Y12 inhibitor for at most 5 days only for life-threatening bleeding, stop endoscopically, and do not give platelets.",
)

FLAGS = {
  'T_9fa98033': "Not a card error: the DocT key ‘continue DAPT’ is right for most patients; ESGE 2021 and ACG–CAG 2022 allow a brief P2Y12 interruption (resume within 5 days) in life-threatening bleeding with high-risk stigmata, which the card already states. ACG–CAG’s DAPT advice (interrupt P2Y12, continue aspirin) is worded for elective endoscopy.",
}
