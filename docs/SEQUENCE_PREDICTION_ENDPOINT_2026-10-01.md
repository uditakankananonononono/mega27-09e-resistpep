# Sequence-prediction question: documented endpoint (2026-10-01)
Steer (parent, 2026-10-01): accept the 21-unit result as the endpoint of the
sequence-prediction question; lane value continues in descriptive contrasts,
Habets access, and mining for datasets with true matched controls. No A4
relabeling. New estimands only as proposals grounded in newly mined data.

## Final measured results (unsoftened)

A1 base (9 units, 3 studies, matched controls; results/score_a1.json):
model LOSO Spearman -0.547 / -0.369 (lipid indicator); baselines: two-feature
-0.343, k-mer -0.623/-0.521, global-median -0.898. BEAT fails both criteria.

A3 enlarged base (21 units, 4 studies/organisms, 17 sequence groups;
results/score_a3.json):
- Full 21: 0.111, CI [-0.275, 0.490]; lipid indicator 0.314,
  CI [-0.102, 0.661]; disulfide indicator -0.030.
- Spohn-only 12: 0.467, CI [-0.115, 0.824].
- Matched-only 9: -0.547 (exact A1 reproduction - pipeline consistency proof).
BEAT fails the CI criterion in every configuration. Direction moved positive
with more units; signal remains within noise. The CI criterion did its job.

## What stands as valid output of this lane

1. The audited, pinned, provenance-complete dataset base (3 studies + Spohn,
   sha256-pinned, 45-cell MIC audit, quarantine rules, censor handling).
2. The A1.3 descriptive secondaries (results/descriptive_secondary_a1.json):
   mixtures vs singles, cross-resistance asymmetry.
3. The prereg chain PREREGISTRATION.md -> A1 -> A2 -> A3 with every
   deviation disclosed in-document.
4. The mining log with eligibility verdicts and open access items.
