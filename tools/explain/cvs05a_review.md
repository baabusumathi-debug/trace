# CVS05A review — independent fact-check (19 Nov 2026)

Files checked: cvs05a_learn.py (13 cards), cvs05a_topups_learn.py (T_4d72df8c). check_learn.py CVS05A: OK (13/13, spine 6).

## Points settled with sources
- Doppler equation Δf = 2·f₀·v·cosθ/c, measured = true × cosθ, error = 1 − cosθ (30° 13%, 45° 29%, 60° 50%, 90° 100%): arithmetic re-done, correct; 4.35 m/s → 76 mmHg vs 100 mmHg correct. ASE Doppler quantification (Quiñones 2002, asecho.org PDF): beam as parallel as possible, <20° deviation gives <10% error, angle correction not recommended. Writer’s text agrees.
- Nyquist limit = PRF/2; maximum PRF and so the Nyquist limit fall as sample-volume depth increases; PW usually cannot show >1.5–1.7 m/s (123sonography 1.8.1.1; ASE 2002 glossary). Writer’s ECHO-07 FLAG is correct.
- ASE/EACVI 2015 (ASE summary document): volumes from linear measurements should NOT be used for EF; biplane disks preferred; FS use discouraged, normal >25%. Writer’s ECHO-04 text and FLAG correct.
- Spencer et al. JACC 2001 (UTHSCSA abstract): 36 patients, four cardiologists; exam missed 59% overall and 43% major; miniaturised echo missed 29% and 21%. Correct.
- 77–93% intensivist–cardiologist agreement: no source paper found. Melamed 2009 (Chest; hand-held LV function by intensivists vs formal echo) 92% normal / 80% abnormal correct, kappa 0.72 — inside the band. Vignon 2007 reports kappas only.
- Probe manoeuvres (POCUS101): rock = toward/away from the indicator along the long axis (in-plane); tilt/fan = side to side along the short axis; rotate about the central axis (long ↔ short axis); compress. Top-up text correct. PLAX → PSAX 90° clockwise correct.
- ASE 2025 diastolic e′ (septal ≤6, lateral ≤7 cm/s) and E/e′ average >14: confirmed (Cleveland Clinic 2025 ASE slides, preliminary).

## Changes
- ECHO-01 c: “studies report agreement in this range for the core questions (LV and RV function, effusion, gross valve disease)” (unsourced, overstated) → states the range is the source’s, untraced, and gives Melamed 2009 (92%/80%) as an example in the band for simple LV/effusion questions. [minor factual — softened]
- ECHO-02 b: “The heart lies 10–20 cm from the chest wall” (wrong: the anterior heart is a few cm deep) → “Cardiac views need an imaging depth of about 15–20 cm (the apical view reaches the atria)”. [factual]
- ECHO-04 c: FS “normal about 25% or more” → “normal above 25%; ASE/EACVI 2015 discourages its use” (ASE 2015 summary). [minor]
- ECHO-06 a: added “ASE: angle correction is not recommended” (Quiñones 2002). [minor]
- ECHO-13 d: “raising the scale (within the Nyquist limit for PW)” (muddled: the scale sets the Nyquist limit) → “for PW only up to the maximum pulse repetition frequency the depth allows”. [minor factual]
- Header comments of both files: sources now checked recorded (ASE 2002, Melamed 2009, ASE 2015 FS, POCUS101).

No fidelity, letter-order, mnemonic or trap-format problems found; BART is the card’s own wording and is restated as such.

## Final FLAGS
- ECHO-07 c: “preset delay a.k.a. NYQUIST LIMIT” is wrong — the delay sets sample depth (range gating); Nyquist limit = PRF/2, the velocity ceiling before aliasing.
- ECHO-12 b: same error in the table (“preset delay (Nyquist limit)”).
- ECHO-04 c / watch: EF from M-mode is possible but not recommended (ASE/EACVI 2015: no EF from linear measurements); the watch line overstates that IVC, EF etc. come only from M-mode.
- ECHO-01: 59%/43% are from Spencer 2001 (cardiologists, 36 patients, not an ICU study); 77–93% source untraced. Note only, not an error.
- Top-up T_4d72df8c: no flags.
