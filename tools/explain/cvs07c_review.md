# CVS07C review (second, independent check, 19 Nov 2026)

Sources checked: RCUK 2025 adult neuroprognostication algorithm (based on ERC–ESICM 2025) and RCUK 2025 post-resuscitation guideline page; RCUK/ERC–ESICM 2021 neuroprognostication algorithm; Sandroni ICM 2020 review (the basis for 2021: MRI 2–5 d); Frontiers Med 2026 review of ERC–ESICM 2025; AHA 2025 Part 11 web text and AHA 2025 neuroprognostication diagram; Westhall Neurology 2016 abstract; Merigo Ann Intensive Care 2025 (2021 fever >37.7 °C ≥72 h); WBDP 2020 abstract and OpenAnesthesia summary.

## Settled points
- Entry: ERC–ESICM 2021 = M ≤3 at ≥72 h; 2025 = M ≤5 (GCS motor <6) at ≥72 h after ROSC. Card and explanation correct.
- MRI: 2021 = 2–5 d (Sandroni 2020); ERC–ESICM 2025 and AHA 2025 = 2–7 d. The writer's FLAG on the card-layer cross line (which says 2025 = 2–5 d) is correct.
- CT: ERC–ESICM 2025 = marked GWR reduction; repeat CT at 72–96 h if the first is normal and the patient is still unconscious (confirmed). The RCUK 2025 algorithm gives CT "at any time"; "within 72 h" not confirmed (removed).
- NSE: >60 µg/L at 48 h and/or 72 h (2021 and 2025); serial 24/48/72 h; normal ≤17 µg/L within 72 h favourable. AHA 2025: high NSE or NfL within 72 h (2b). 33 µg/L = AAN 2006, days 1–3.
- AHA 2025: N20 at ≥48 h (ERC ≥24 h); consolidate ≥72 h after normothermia, typically ≥5 days after ROSC if cooled; withdrawal-or-better motor response favourable (diagram).
- WBDP 2020: apnoea positive when PaCO₂ ≥60 mmHg with pH <7.30 (≥20 above baseline in chronic retainers); SBP ≥100 or MAP ≥60; core temperature ≥36 °C.
- Untraced (card figures, already worded softly in the explanations, not flagged as wrong): NSE "47" (PCA-48), CT oedema "around 50%" (PCA-50), "5–10 days" waking (PCA-43).

## Changes
- PCA-43 a: "ERC–ESICM 2025: awakening usually within 3–4 days" (could not verify) → "most who wake do so within the first few days; late awakening well described; 5–10 days is the chapter's figure, not a guideline number". Same softening in FLAGS['PCA-43'] and the header.
- PCA-44 trap: "AHA 2025 (COR 3): preserved pupillary/corneal reflexes not useful for favourable prognosis" (COR not found in AHA 2025 text or diagram) → "AHA 2025 lists only absent reflexes; preserved reflexes are not a favourable sign" (AHA 2025 diagram). Header line removed.
- PCA-45 b: "all 38 with a highly malignant EEG" (derived number) → "37% of 103 patients (EEG at median 77 h), all poor outcome; specificity 100%, sensitivity 50%" (Westhall 2016 abstract).
- PCA-46 trap: "most patients with a preserved N20 still have a poor outcome" (overstated) → "many patients with a present N20 still have a poor outcome; high specificity, low sensitivity".
- PCA-47 b and table: "ILCOR 2025 suggests against S-100B" (unverified) → "ERC–ESICM 2025 does not recommend S-100B" (Frontiers 2026 review of ERC–ESICM 2025). Header adjusted.
- PCA-49 trap (GT1o option C): "NSE outside its window by day 6" → adds that the cut-off is validated for 48/72 h and that "not affected by cooling" is too strong.
- PCA-49 trap (GT6): vague "the option inside 2–7 days that best fits" (three options fit) → clear exam-day rule: 2–7 if offered; with these options, DocT's 3–7; 2–5 only for an explicitly ERC–ESICM 2021 stem.
- PCA-50 b: "ERC–ESICM 2025 uses a marked reduction within 72 h" → "marked reduction; repeat a normal early CT at 72–96 h" (RCUK 2025).
- PCA-53 f: "GWR reduction on CT within 72 h" → "marked GWR reduction on CT (repeated at 72–96 h if the first was normal)" (RCUK 2025).
- PCA-55 c: apnoea "PaCO₂ ≥60 or ≥20 above baseline", "systolic ≥100" → "PaCO₂ ≥60 with pH <7.30, or ≥20 above baseline in chronic CO₂ retainers; SBP ≥100 or MAP ≥60" (WBDP 2020). Header adjusted.
- PCA-51 d (minor, depth): bare restatement → adds the mechanism (anaerobic shift, glutamate release) and that it is a research/neurocritical-care tool, not part of the algorithm.
- FLAGS['PCA-41']: "'TTM at 36 °C' is the 2015 ERC–ESICM wording" → "reflects the TTM-trial era (ERC–ESICM 2015: constant 32–36 °C)"; the 2021 (>37.7 °C, ≥72 h) and 2025 (≤37.5 °C, 36–72 h) parts confirmed (Merigo 2025; RCUK 2025).
- Header: added a line listing the second-review sources.

check_learn.py CVS07C: OK (16 cards, 6 spine steps).

## Final FLAGS
- PCA-41: Card c 'TTM at 36 °C' reflects the TTM-trial era (ERC–ESICM 2015: constant 32–36 °C); ERC–ESICM 2021 recommended fever prevention (>37.7 °C) for ≥72 h only, and 2025 ≤37.5 °C for 36–72 h.
- PCA-43: Card d/e 'most robust predictors first (FPR <5%)' is the 2015 stepwise algorithm; since 2021 any two of six, no order. Card a '5–10 days' untraced; most who wake do so within the first few days, late awakening well described.
- PCA-49: Card correct (2–7 d = AHA 2025 and ERC–ESICM 2025; repeat CT 72–96 h = ERC–ESICM 2025). The card-layer cross line saying ERC–ESICM 2025 uses 2–5 days is wrong: 2–5 days is 2021.
- PCA-53: Watch line says 'reflexes and NSE at ≥72 h'; NSE is read at 48 h and/or 72 h (card answer right).
- PCA-54: Marrow key 'neither TTM option indicated yet' in a sedated comatose survivor is disputed: temperature control is for all comatose survivors; sedation delays prognosis, not cooling.
- PCA-56: Row c gives M ≤3 (2021); ERC–ESICM 2025 entry is M ≤5, as PCA-43 and PCA-52 say.
