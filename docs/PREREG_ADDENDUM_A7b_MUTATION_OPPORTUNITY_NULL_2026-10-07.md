# Prereg Addendum A7b - mutation-opportunity null (DRAFT, not yet locked)

Status: DRAFT written locally while pushes are held (GitHub commit_refs incident). It becomes a lock only when committed and pushed BEFORE any computation. No computation has been run.

Question (judge item 4): is cross-study recurrence of sbmA among strict Tier A events more than expected from gene size / mutational opportunity alone?

Frozen inputs required (to pin with sha256 before use): CDS lengths for E. coli K-12 MG1655 genes in the A6 Tier A event ledger (results/event_tier_robustness_a6.json) and for the genome-wide gene set used as the null universe; source = KEGG/EBI record per gene, or the NCBI GenBank feature table if obtainable.

Null: each Tier A direct event (point/indel/IS) is assigned to a gene with probability proportional to CDS length; 100,000 permutations, seed 20261007. Statistic: number of genes with Tier A events in >=2 independent studies. Report the observed value, null distribution quantiles, and the exact p for sbmA's cross-study recurrence given its CDS length (1,221 bp from the 406 aa record).
Limits stated in advance: IS-mediated events are not uniform by length (insertion-hotspot bias), and Spohn large deletions are excluded (breakpoint-driven, see A6). A length-proportional null is a minimal baseline, not a full mutational spectrum model. A significant result would show only recurrence beyond length expectation, not selection for resistance.
Decision: result reported either way; a non-significant result downgrades sbmA to "recurrent, consistent with opportunity".
