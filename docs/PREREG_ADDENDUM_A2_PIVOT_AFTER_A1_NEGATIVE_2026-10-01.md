# PREREGISTRATION ADDENDUM A2 - documented pivot after the A1 honest negative
Status: LOCKED 2026-10-01, after A1.4 scoring completed and before any new
modeling. Trigger: A1.4 produced an honest negative (results/score_a1.json).
House rules applied: negatives are never terminal, pivot under new prereg,
never a centerpiece, numbers never softened, negatives minority via steering.

## A2.1 The A1 negative, as measured (not softened)

- Model (full-descriptor ridge) LOSO Spearman = -0.547 (no lipid flag),
  -0.369 (with lipid flag). Baselines: two-feature -0.343, k-mer -0.623 /
  -0.521, global-median -0.898.
- BEAT fails both locked criteria: model does not exceed every baseline
  (two-feature baseline beats it) and 95% bootstrap CI includes 0
  ([-0.92, 0.12] and [-0.85, 0.35]).
- Permutation null p = 0.924; feature-scramble control 0.286; Maron NPSA
  controls exactly 0 by measurement.
- Claim boundary (A1.5) stands: no claim of predicting resistance for
  arbitrary unseen peptides; retrospective analysis only.

## A2.2 What is closed and what continues

- CLOSED: sequence-only predictive modeling of net resistance emergence on
  the current 9-unit base. Recorded as an honest negative; not retried under
  a relabeled metric.
- CONTINUES (already locked as descriptive secondary in A1.3; computed in
  results/descriptive_secondary_a1.json, no scoring, no gates):
  - Mixture-vs-single contrast (antunes2024): random mixtures net 0.5-1.5
    log2 vs single sequences net 0.5-3.5 log2. Descriptive only; mixtures
    carry no sequence-level label.
  - Cross-resistance asymmetry (maron2025): off-diagonal medians -1.13 to
    +2.0 log2 vs own-treatment 2.0-4.79 log2; asymmetric (e.g., melittin-
    evolved lines show +2.0 on temporin, temporin-evolved show -1.13 on
    pexiganan). Descriptive only.

## A2.3 Locked forward rule (literature mining before any further modeling)

1. No new model, metric, split, or scoring on any dataset until BOTH:
   (a) literature mining (below) has run and been logged, and (b) a new
   estimand and evaluation design are locked in a subsequent addendum
   BEFORE scoring on any enlarged base.
2. Mining protocol: sources PubMed/PMC/Europe PMC + Zenodo/Dryad/Figshare
   data records. Eligibility for enlarging the unit base: experimental
   evolution / serial passage under a single-sequence AMP with per-lineage
   MIC outcomes AND matched passage controls (or ancestor MIC enabling a
   defensible control contrast), with exact peptide sequence available from
   a pinnable primary source.
3. Every candidate dataset is logged with provenance URL, eligibility
   verdict, and exclusion reason if rejected. No outcome peeking: mining
   logs counts and availability only, never outcome values, until the next
   addendum locks the estimand for any enlarged base.
4. Ineligible-but-interesting records (figure-only outcomes, mixture-only
   treatments, no controls) are logged as gaps, mirroring the ovispirin /
  aurein 1.2 / pardaxin figure-only gap already documented.
