# CVS03 top-up cards — Explain v3 ("Learn" depth), same fields and voice as cvs03_learn.py.
# Fields: sub, step (index into cvs03_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions: the top-up's own src (DocT Heart Failure Q8, Q14, Q18, Q19, Q25; DocT GT AIM1 Q17), read from doct_qbank_all.jsonl and doct_gt_distinct_all.jsonl on 19 Nov 2026.
# Checked online 19 Nov 2026: ESC 2023 HF focused update — SGLT2 inhibitors class I-A in HFmrEF and HFpEF; intensive initiation and rapid up-titration after an HF admission I-B.
# From standard references without a fresh check: ESC 2021 LVEF classes; PARADIGM-HF (sacubitril/valsartan vs enalapril, HR about 0.80 for CV death or HF admission); EMPEROR-Preserved,
# DELIVER; DIG (digoxin: no mortality change, fewer HF admissions); V-HeFT I and A-HeFT (hydralazine–isosorbide dinitrate); PROMISE (oral milrinone raised mortality), OPTIME-CHF (IV milrinone:
# no benefit, more hypotension and arrhythmia).
T = {}

T['T_62274f28'] = dict(
  sub="Cardiogenic shock → After the shock → Chronic HF drugs by LVEF",
  step=5,
  intro="Step 5 ends where the shock does: the survivor goes home with heart failure, and the drugs that change survival are not the ones used in the ICU. The ejection fraction sorts the patient, and the exam asks which drugs prolong life and which only relieve symptoms. Six DocT questions, one of them answered correctly by fewer than a third.",
  parts=[
    ('a', "**Classes: HFrEF ≤40%, HFmrEF 41–49%, HFpEF ≥50% (plus a structural or diastolic abnormality or raised natriuretic peptides).** The cut-offs are ESC 2021. A normal EF alone does not make the diagnosis; HFpEF needs objective evidence of raised filling pressure or a stiff ventricle, because breathlessness with a normal EF has many other causes."),
    ('b', "**HFrEF: four pillars started together, before discharge once stable after a decompensation — ARNI (sacubitril/valsartan beat enalapril in PARADIGM-HF) or ACEi/ARB, β-blocker, MRA, SGLT2 inhibitor; each cuts death and HF admission.** Each blocks a different limb of the spiral on CS-17: RAAS (ACEi, ARB, ARNI, MRA), the sympathetic system (β-blocker), and sodium and glucose handling (SGLT2 inhibitor), while neprilysin inhibition boosts the natriuretic peptides. Their benefits add up, so the old ‘start one, titrate, then add the next’ sequence has been replaced by starting all four quickly (ESC 2023: rapid up-titration after an admission, I-B)."),
    ('c', "**HFpEF/HFmrEF: an SGLT2 inhibitor is the class I outcome drug (EMPEROR-Preserved, DELIVER); treat BP, AF and comorbidities.** The benefit is mainly fewer HF admissions (with CV death in the composite); ESC 2023 made it class I-A. ACE inhibitors and β-blockers have no proven outcome benefit in HFpEF."),
    ('d', "**Loop diuretics relieve congestion in every class but do not change survival.** They are the first treatment for the wet patient (CS-26) but not a prognostic drug."),
    ('e', "**No mortality benefit: digoxin (fewer admissions only), nitrates; IV inotropes (milrinone) raise mortality.** Digoxin in DIG reduced HF admissions without changing death. Nitrates alone do not prolong life (hydralazine with isosorbide dinitrate does, in ACE-inhibitor-intolerant and in self-identified Black patients). Chronic or repeated inotropes raise oxygen demand and arrhythmia: oral milrinone increased mortality (PROMISE), and IV milrinone gave no benefit with more hypotension and AF (OPTIME-CHF)."),
  ],
  mimic=[("Prognostic vs symptomatic drugs", "Prognostic: ARNI/ACEi/ARB, β-blocker, MRA, SGLT2 inhibitor; symptomatic: diuretics, digoxin, nitrates."),
         ("HFrEF vs HFpEF treatment", "HFrEF has four prognostic pillars; HFpEF has one (SGLT2 inhibitor) plus diuretics and comorbidity control.")],
  traps=[("“HFrEF, EF 30%: which drug reduces mortality — ACE inhibitor (not β-blocker)” (DocT key)", "Both reduce mortality (class I); DocT keys the ACE inhibitor because it is ‘typically started first’, which is outdated (only 30% chose the key). Choose ‘both’ or ARNI if offered; if forced, DocT’s key is the ACE inhibitor."),
         ("“HFpEF: diuretics improve symptoms and prognosis”", "DocT keys diuretics (82% and 73%) because no SGLT2 inhibitor is offered; diuretics only treat symptoms. On a current paper, the prognostic drug is the SGLT2 inhibitor."),
         ("“IV milrinone reduces rehospitalisation”", "It does not; ACE inhibitors and β-blockers do (87%).")],
  decode=[("HFrEF stabilised after decompensation: which therapy improves long-term survival? [DocT GT]", "Sacubitril/valsartan (90%)."),
          ("HFrEF, EF 30%, stable: which drug reduces mortality? [DocT QBank]", "DocT: ACE inhibitor (30%); really ACEi and β-blocker both."),
          ("HFrEF, EF 35%: what reduces rehospitalisation? [DocT QBank]", "ACE inhibitors and β-blockers (87%)."),
          ("HFpEF with congestion, BP 140/85 or 160/95 [DocT QBank ×2]", "Diuretics as the least-wrong option (82%, 73%).")],
  punch="In HFrEF four drugs — ARNI or ACEi, β-blocker, MRA, SGLT2 inhibitor — all prolong life and start together; in HFpEF only the SGLT2 inhibitor changes outcome, and diuretics, digoxin and inotropes never do.",
)
