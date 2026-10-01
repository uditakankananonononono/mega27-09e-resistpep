# PREREGISTRATION ADDENDUM A3 - enlarged base adopting Spohn 2019
Status: LOCKED 2026-10-01, BEFORE any extraction of outcome values from the
pinned Spohn 2019 files. Trigger: A2.3 mining pass 1 found one
eligible-candidate; parent authorized adoption with explicit adjudications.

## A3.1 What is adopted

Spohn et al. 2019, Nat Commun 10.1038/s41467-019-12364-6 (PMC6778101).
Pinned: data/raw/pmc6778101.xml and data/raw/spohn2019_supp.zip (sha256 in
data/SHA256SUMS.txt). Scope: the E. coli K-12 BW25113 panel only - 14 AMPs
x 10 independent evolved populations (~120 generations). The clinical-
isolate / mutD5 panels (TPII, PXB on other strain backgrounds) are OUT of
scope for A3 (disclosed narrowing; one strain background per study keeps
the unit structure homogeneous).

## A3.2 Control-structure adjudication (explicit, as required)

Verified from the pinned full text (Methods, "Laboratory-evolution
experiment"): 10 parallel populations per drug; NO no-drug passage-control
populations; resistance is measured as MIC fold-change of each evolved line
vs the wild-type ancestor. Matched passage controls are absent.

Decision: INCLUDE Spohn units with an ancestor-only contrast (control
log2 fold-change = 0 assumed), as a disclosed deviation, because:
1. The same assumption is MEASURED true in the existing base: Maron 2022
   supplement Table S2 NPSA controls show MIC identical to ancestor in both
   independent experiments for all three drugs.
2. Passage adaptation alone does not trivially inflate MIC: Spohn's own
   antibiotic panel shows strongly drug-specific, heterogeneous fold-changes
   (no uniform uplift), and A1's Antunes controls sit at 0 for 3 of 6
   treatments.
Guardrail: Spohn (ancestor-only) units are ALWAYS reported as their own
subset, separately from matched-control units, in every scored output; a
pooled number never hides the assumption. If any downstream analysis shows
the assumption failing, these units leave the base with the reason logged.

## A3.3 Exclusions logged (as required)

- PXB (polymyxin B): cyclic lipopeptide with a fatty-acyl tail; the listed
  "KTKKKFLKKT" is only its linear peptide portion. Sequence-feature
  definitions (A1.4) cover plain amino-acid sequences only. OUT.
- PROA (protamine): heterogeneous natural peptide preparation; the listed
  sequence is one component. No single-sequence label. OUT.
Remaining 12 AMPs: BAC5, CAP18, CP1, HBD3, IND, LL37, PEX, PGLA, PLEU,
PR39, R8, TPII (sequences pinned from Supplementary Table 1, MOESM1).

## A3.4 Cross-study replication flags and structural caveats

- CP1, PEX, LL37 are cross-study replication units (cecropin P1 and
  pexiganan already scored in other organisms; LL-37 was unscored in
  prabhu2013 - Spohn provides its first scored unit). Sequence identity
  remains the leakage barrier: replication units join their existing
  sequence groups in LOSO folds.
- TPII and HBD3 are disulfide-bonded; plain-sequence descriptors cannot
  see disulfide structure. Same handling as A1.4 lipidation: a
  disulfide indicator, runs reported with and without.

## A3.5 Enlarged base and evaluation design (locked)

- Units: 9 (A1 base) + 12 (Spohn) = 21 treatment units; 16
  sequence-distinct LOSO groups.
- Estimand: unchanged from A1.3 (treatment-level median net log2 MIC
  fold-change vs matched control; Spohn units carry the A3.2 ancestor-only
  contrast, flagged).
- Pipeline: unchanged locked A1.4 pipeline - same descriptors, baselines
  (global-median, 2-feature ridge, k-mer ridge), ridge alpha 1.0, train-fold
  standardization, LOSO by sequence identity, Spearman, bootstrap 95% CI
  (seed 2002), permutation null 10000 draws seed 1001, feature-scramble.
  Reported for: full 21-unit base, Spohn-only subset, matched-control-only
  subset (the original 9). BEAT rule unchanged.
- Published-comparator disclosure: Spohn Fig 2 itself reports
  physicochemical-correlate Spearman correlations on the same 14 treatment
  means (polar fraction rho 0.58, positive-charge fraction 0.62,
  hydropathicity rho -0.73; N=14). This is prior art overlapping the A1
  model question, disclosed here; A3's LOSO held-out design is stricter
  than their in-sample treatment-mean correlations and no pass/fail gate
  is derived from their values.

## A3.6 Erratum (same day, before any reporting of counts)

A3.5 states 16 sequence-distinct LOSO groups; the correct count is 17
(I omitted LL-37, which is a NEW scored group - its prabhu2013 unit was
unscored). Scored pipeline confirms 21 units / 17 groups. No other change.
