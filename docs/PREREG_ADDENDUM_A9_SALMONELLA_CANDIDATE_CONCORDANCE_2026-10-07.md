# Prereg Addendum A9 - concordance of Salmonella AMP-resistance candidate genes with E. coli Spohn lines (LOCK)

Date: 2026-10-07. Parent-approved unit (option a). Source: Lofton et al., PLOS ONE 2013, doi 10.1371/journal.pone.0068875 (Salmonella Typhimurium LT2, SRP023134), main text only; supplementary tables S3-S6 were not retrievable.

## What the Salmonella side provides (from the paper's text, read before this lock)
Four sequenced resistant clones: DA16874 (LL-37, hypermutator, >80 mutations), DA16875 (wheat germ histones), DA17847 (LL-37), DA17610 (CNY100HL). Named genes: waaY (and/or waaZ) in DA16874, DA16875, DA17847; pmrB in DA16874 and DA16875; phoP in DA17610. The three genes were chosen by the authors because they were hit, so the Salmonella side is NOT an independent test of anything; it only supplies a candidate list declared before the test below. The hypermutator's hits are not counted as independent support.

## Disclosed exposure
A5/A6 have shown Spohn recurrence lists, which may include waaY/waaP-family genes (A7 discussed waaY vs waaP). I have not tabulated Spohn Tier A events for waaY, phoP or basS before this lock.

## Candidate set and mapping (frozen before looking)
- Primary candidates: waaY and phoP (E. coli K-12 names identical to Salmonella). Orthology check, descriptive: global pairwise alignment (match +1, mismatch -1, gap -2, own implementation) of pinned UniProt sequences: WaaY P26472 (Salmonella, strain F98) vs P27240 (E. coli K-12); PhoP P0DM78 (Salmonella ATCC 14028) vs P23836 (E. coli K-12). A pair counts as ortholog if identity >=35% over >=80% of both lengths (A7 rule). Strain differences from LT2 are a disclosed limitation.
- Secondary candidate: Salmonella pmrB maps to E. coli basS by nomenclature only: UniProt P30844 (BASS_ECOLI) lists pmrB as a gene synonym. No Salmonella PmrB sequence is pinned, so this mapping is by name, not alignment; basS is reported but is NOT in the primary statistic.
- waaZ is not a candidate (not named as a clone-level hit).

## Test (Spohn side only)
Events: Tier A evolved Spohn records of results/mutation_convergence_a5.json (tier via scripts/event_tier_robustness_a6.py), unit = distinct (line, gene, mutation_type) as in A7b; Tier B large deletions excluded.
Statistic T = number of primary candidate genes (waaY, phoP) with >=1 Spohn Tier A event.
Null: A7b model restricted to Spohn: the Spohn mapped event count placed in the 4,290-gene universe (data/raw/ecoli_k12_U00096.3_cds_table.tsv, MG1655 CDS lengths) with probability proportional to CDS length; 100,000 reps, seed 20261009; one-sided p = P(null T >= observed). Per-gene hit counts and the independent lines/AMPs involved are reported descriptively, plus the same for basS and (descriptive) pmrA, phoQ.

## Limits fixed in advance
Candidate list comes from a different species; n=2 primary genes means the test can only reject at p<0.05 if both are hit (null p about 0.04 for two genes at 121 events, to be computed exactly, not assumed). Length-proportional null ignores selection-independent mutational hotspots. A hit in an E. coli line shows concordance of locus, not shared mechanism or peptide specificity. No candidate peptide, no named discovery (09d gate unchanged).

## Decision rule
If T = 2 and p < 0.05: the two Salmonella candidate loci are also hit in E. coli AMP-evolved lines beyond opportunity - descriptive cross-species concordance note. Otherwise report "no concordance beyond opportunity detectable". Either result is reported in full.
