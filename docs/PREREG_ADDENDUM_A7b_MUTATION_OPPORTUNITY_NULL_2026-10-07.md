# Prereg Addendum A7b - mutation-opportunity null (LOCK)

Status: LOCKED by the commit that contains this text, pushed before any computation. No A7b computation has been run.

Question (judge item 4): is cross-study recurrence of sbmA among strict Tier A events more than expected from gene size / mutational opportunity alone?

Frozen inputs required (to pin with sha256 before use): CDS lengths for E. coli K-12 MG1655 genes in the A6 Tier A event ledger (results/event_tier_robustness_a6.json) and for the genome-wide gene set used as the null universe; source = KEGG/EBI record per gene, or the NCBI GenBank feature table if obtainable.

Null: each Tier A direct event (point/indel/IS) is assigned to a gene with probability proportional to CDS length; 100,000 permutations, seed 20261007. Statistic: number of genes with Tier A events in >=2 independent studies. Report the observed value, null distribution quantiles, and the exact p for sbmA's cross-study recurrence given its CDS length (1,221 bp from the 406 aa record).
Limits stated in advance: IS-mediated events are not uniform by length (insertion-hotspot bias), and Spohn large deletions are excluded (breakpoint-driven, see A6). A length-proportional null is a minimal baseline, not a full mutational spectrum model. A significant result would show only recurrence beyond length expectation, not selection for resistance.
Decision: result reported either way; a non-significant result downgrades sbmA to "recurrent, consistent with opportunity".

## Locked specifics (added at lock)
- Frozen universe: data/raw/ecoli_k12_U00096.3_cds_table.tsv (4,318 complete CDS from NCBI U00096.3 feature table assembled from 36 overlapping efetch windows; sha256 in SHA256SUMS; sbmA = 1,221 bp, matches UniProt 406 aa). Edge-truncated features (< or >) were dropped per window and recovered from overlaps; completeness vs the true annotation (~4.3k CDS) not independently audited.
- Observed events: Tier A evolved records of results/mutation_convergence_a5.json (tier via scripts/event_tier_robustness_a6.py), one event per distinct event_id as in A6.3; gene names matched case-insensitively to the universe. Records whose gene is absent from the universe (intergenic, mis-named, other strain genes) are listed, excluded from both observed and null, and counted.
- Null: for each study separately, its number of mapped Tier A events is placed in universe genes with probability proportional to CDS length, independently; 100,000 replicates, numpy default_rng seed 20261007.
- Statistics: S1 = number of genes hit by Tier A events in >=2 studies (observed vs null, one-sided p = P(null >= observed)). S2 = P(null recurrence of sbmA specifically in >=2 studies), reported as descriptive only because sbmA was selected after seeing data (post hoc).
- Interpretation fixed in advance: p(S1)<0.05 = recurrence exceeds length expectation; otherwise "consistent with mutation opportunity". Caveat fixed: strains differ between studies (reference genome identity not verified for Blanco/Bac7), and Spohn coordinates were not used for mapping (gene names only).
