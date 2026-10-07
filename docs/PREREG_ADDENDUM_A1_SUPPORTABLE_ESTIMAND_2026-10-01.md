# PREREGISTRATION ADDENDUM A1 - supportable estimand and evaluation design
Status: LOCKED 2026-10-01 before any scoring, split creation, or model fitting on
the resistance-evolution outcome data. Trigger: SUPPORT_AUDIT_2026-10-01.md found
the locked-primary datasets do not support the originally assumed label structure.
Deviations from docs/PREREGISTRATION.md are disclosed here, per house rule 4.

## A1.1 What the verified evidence base is (counts, not outcomes)

Three studies, three organisms, pinned with sha256 (data/SHA256SUMS.txt):

- Lofton et al. 2013 (PLOS ONE, PMC3720879, doi 10.1371/journal.pone.0068875), S. typhimurium LT2 [NOTE 2026-10-08: this study was labelled "Prabhu 2013" in this addendum and in some later files; that alias was wrong, the PMC and DOI are the Lofton et al. paper. Scripts and result files may still use the old key]: LL-37, CNY100HL
  (single sequences) + WGH (mixture, excluded from sequence-level labels).
  6 lineages per treatment; cross-resistance clone assays. Raw MIC strings
  include ranges and right-censoring; Table 4 header unit contradicts methods
  (mg/mL vs mg/L) - raw strings retained, no silent conversion.
- Antunes 2024 (PLOS Biology, Zenodo 11209304), P. aeruginosa PA14: 6
  single-sequence AMPs (Melittin, Pexiganan, Cecropin P1, PA-13, SLM1, SLM3)
  + 3 random mixtures (mixtures excluded from sequence-level labels).
  6 evolved + 6 matched passage-control lines per treatment; MIC fold-change
  vs ancestor. SLM1/SLM3 are palmitoylated - flagged as modified peptides.
- Maron 2025 (iScience, PMC12167497, Zenodo 15125182), S. aureus JLA513:
  temporin, melittin, pexiganan, single + combinations (combinations excluded
  from sequence-level labels). 6 lines per treatment; per-line log2 MIC
  fold-change including cross-resistance assays.

Distinct plain single sequences with resistance-emergence outcomes: 9
(LL-37, CNY100HL, melittin, pexiganan, cecropin P1, PA-13, SLM1, SLM3,
temporin), of which melittin and pexiganan appear in two organisms
(independent replication, not new sequence support).

## A1.2 Disclosed deviation from the locked primary

The locked primary assumed public serial-passage datasets support a
sequence-level predictive task with AUROC + Spearman gates vs a published
comparator. The audit shows:

1. No public benchmark of the assumed shape exists in these sources: labels
   are lineage-level MIC fold-changes nested within treatment and study, not
   independent peptide-level binary labels. AUROC on 9 sequences is not a
   meaningful metric and is dropped with disclosure.
2. No published AMP-resistance-emergence predictor with a comparable frozen
   split was identified in the verified sources; the comparator gate degrades
   to sequence-only baselines defined below (disclosed, not silently waived).
3. WGH and the 3 random mixtures cannot carry sequence-level labels and are
   excluded from the sequence task (kept for descriptive mixture-vs-single
   contrast only).

## A1.3 Locked estimand

Primary estimand: the treatment-level median net log2 MIC fold-change of
evolved lines relative to matched passage controls, per (study, organism,
plain single-sequence treatment). Net = evolved minus matched-control median
within the same assay agent. Unit of analysis for inference: the treatment
(9 units), NOT the lineage (lineages are technical/nested replicates).

Secondary (descriptive only): per-lineage fold-change distributions,
cross-resistance asymmetries, mixture-vs-single-sequence contrast.

## A1.4 Locked evaluation design

- Sequence-held-out evaluation: leave-one-sequence-out across the 9 units.
  With 9 folds and 1 held-out unit each, variance is high; this is stated as
  a power limit, not hidden.
- Study-held-out sensitivity check: leave-one-study-out (3 folds). Because
  melittin/pexiganan appear in two studies, sequence identity (not study) is
  the leakage barrier; both checks run and are reported together.
- Features: sequence-only physicochemical/compositional descriptors computed
  from the plain sequence (no labels, no leakage from outcomes). Lipidated
  SLM1/SLM3 run with and without a modification indicator; both reported.
- Baselines (locked before scoring): (a) global-median predictor; (b) net
  charge + mean hydrophobicity two-feature ridge; (c) k-mer (k=2,3) ridge.
  BEAT = the model's LOSO Spearman vs measured net fold-change exceeds every
  baseline's LOSO Spearman AND its 95% bootstrap CI over 9 units excludes 0.
  With 9 units a CI excluding 0 is demanding by design; failure is a
  documented honest negative, not terminal (rule 6).
- Censoring: right-censored raw MICs contribute their lower bound and a
  censor flag; primary analysis uses rank-based statistics only (Spearman),
  which is censor-robust within ties; no midpoint imputation of censored
  values. The 2013 mid-point CSVs are quarantined from training.
- Negative controls: (a) label-permutation null (10000 draws, seed 1001);
  (b) ancestor/ancestor contrast where available must yield ~0 net change;
  (c) feature-scramble control.

## A1.5 What this cannot claim

- No claim of predicting resistance for arbitrary unseen peptides: 9 units
  across 3 organisms cannot support that.
- No clinical or design guidance: this is retrospective analysis of published
  data.
- No named discovery: the locked discovery criterion's independent evidence
  layers are untouched and still binding.
- No benchmark-beat claim against a published resistance predictor (none
  eligible was verified); baseline-beats only, as defined.

## A1.6 Judge-round status

This addendum is methodological discipline, not a completed finding. It does
not trigger the one ChatGPT round for 09e; that round fires only when a
completed finding exists and the repo ledger confirms no round consumed
(current ledger: 0 consumed).
