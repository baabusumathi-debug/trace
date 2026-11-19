# CVS05B review (independent fact-check, 19 Nov 2026)

27 cards + 3 Top-ups checked. Letters, bold restatements and qpack percentages/keys all match. `check_learn.py CVS05B` OK.

## Changes
Factual:
- ECHO-18 e: IVC measured "about 1–2 cm from the RA", plus an unsupported reason (it narrows at the diaphragm, the liver compresses it lower down) → now "just distal to the hepatic vein junction, 0.5–3.0 cm from the RA ostium", with a neutral reason (the diameter varies along the vessel and moves with the diaphragm, so the site must be fixed). Source: Lang 2015; ASE 2025 right heart guideline.
- ECHO-19 trap (ventilated): "a small IVC (about 12 mm or less) is the useful finding" (Rudski 2010 wording) → ASE 2025: in an intubated patient an IVC ≤2.1 cm accurately identifies RAP <10 mmHg, which fits the 17 mm stem. Source: ASE 2025 right heart guideline (replaces Rudski 2010).
- ECHO-19 b: "upgrade to 15 (with little collapse)" → downgrade to 3 / upgrade to 15 / otherwise stay at 8, as stated in ASE 2010 and kept in 2025. Source: ASE 2025.
- ECHO-19 c: added the real ASE list of secondary indices (RA enlargement, IAS bulging into the LA, restrictive RV filling, tricuspid E/e′ >6, HV systolic filling fraction <55%). RVH is not on the list, and the indices are used mainly for the intermediate band. Also added the new 20 mmHg band (IVC >2.5 cm, no variation). Source: ASE 2025.
- ECHO-20 c: "sinus rhythm" was given as a requirement for IVC distensibility. It is not; that requirement belongs to PPV → removed. Added Feissel ΔIVC >12% beside Barbier >18%.
- ECHO-37 b: "1.1–1.3 cm is mildly abnormal" was the male range only → men 1.1–1.3, women 1.0–1.2 cm. Source: Lang 2015.
- ECHO-39 c: "EPSS reads falsely high with a hypertrophied upper septum" (wrong direction) → EPSS is falsely raised in MS and AR; it is unreliable with asymmetric septal hypertrophy or a septal wall-motion abnormality.
- Top-up T_8cd6b5dd e: "an aorta >3 cm explains haemorrhagic shock" → >3 cm is aneurysmal; in shock, >5 cm is treated as rupture until proved otherwise; a flap means dissection. Source: WikEM RUSH page.
- Top-up T_11e87634 c: "varices are a contraindication" → absolute contraindications are perforation, stricture, tumour and recent oesophageal surgery; varices are relative.

Minor:
- ECHO-23 d: the anterolateral wall is often shared between the LCx and the LAD.
- ECHO-39 e: added the ASE 2025 TAPSE grades (mild 13–17, moderate 10–13, severe ≤10 mm).
- ECHO-38 c: RV cut-offs (basal >4.1 cm, mid >3.5 cm) are now also cited to ASE 2025.
- Header comments (both files): added the sources checked in this review. The prosthetic valve note now says the ASE 2024 update uses a VTI ratio of >2.5.

## Points settled (verified, no change needed)
- ASE 2015 LVIDd: men 4.2–5.8 cm, women 3.8–5.2 cm, correct (Table 2: 42.0–58.4 / 37.8–52.2 mm).
- Aortic sinus diameter, men 3.4 cm and women 3.0 cm: kept. I could not open the table to confirm it, but it matches the standard values.
- ESC 2019 PE: RV/LV ≥1.0 and TAPSE <16 mm, correct.
- ASE 2025 diastolic cut-offs, all correct as written:
  - e′ septal ≤6, lateral ≤7 cm/s
  - E/e′ average >14
  - TR ≥2.8 m/s
  - LAVI >34
  - LARS ≤18%
  - E/A ≤0.8 or ≥2
- AR cut-offs (ASE 2017) and prosthetic aortic <3 m/s / <20 mmHg, mitral <1.9 m/s / ≤5 mmHg: correct.
- RUSH IVC <1.5 cm collapsing = low CVP: correct.
- A2C is about 60° counter-clockwise from A4C, and A3C a further about 60° counter-clockwise (123sonography). This confirms the writer's flag on ECHO-31 and ECHO-32.
- Ventilated IVC cut-offs: distensibility >18% (Barbier) and ΔIVC >12% (Feissel) are correct.
- The traps on disputed keys are kept, and their "truth" side holds:
  - ventilated "collapsibility" wording
  - sinusoid sign as a "transudate" over-read
  - hyperdynamic LV = low SVR

## Final FLAGS
- ECHO-19: the card lists RVH among the secondary indices of raised RAP and ties them to the high band. ASE lists RA enlargement, IAS bulging, restrictive RV filling, tricuspid E/e′ >6 and HV SFF <55% (S/D <1), and uses them for the intermediate band. ASE 2025 adds a 20 mmHg band. (new)
- ECHO-21: "transudate is anechoic" is true, but an anechoic effusion can still be an exudate. The DocT key "transudate" for a sinusoid sign over-reads it.
- ECHO-31: A3C is "clockwise 60° from A2C" on the card; it is counter-clockwise (confirmed).
- ECHO-32: same issue for A3C. A2C at 90° without a direction is acceptable.
- ECHO-35: the FATE card puts PSAX at both the mitral and the aortic level in the extended views.
- ECHO-37: these are older values. ASE 2015 ranges are sex-specific (LVIDd, wall thickness, LVEF).
- ECHO-38: LA diameter and the old RV M-mode dimension are outdated. Use LAVI ≤34 mL/m² and RV basal >4.1 / mid >3.5 cm.
- ECHO-39: FATE EF bands differ from ASE 2015. The deck uses the ASE TAPSE normal of ≥17 mm.
- ECHO-40: "TVI" here means tissue velocity imaging. E/e′ <8–10 is the FATE normal; the current raised-pressure cut-off is >14. The IVC figure of 20 mm differs from the 2.1 cm used in ECHO-19.
