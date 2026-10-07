# Prereg Addendum A7 - gene-function annotation and orthology resolution (LOCK)

Date: 2026-10-07. Chain: PREREGISTRATION -> A1 ... A6 -> A7.
Purpose: resolve judge items 3 (S. maltophilia SbmA orthology) and, if feasible, 4 (mutation-opportunity null), plus waaY/waaP functional equivalence. This is annotation work, not outcome scoring. No A5/A6 counts change under A7; A7 only adds an annotation column.

## Disclosed exposure
A5 and A6 results (sbmA sole Tier A cross-study recurrence; breakpoint 388,423 hotspot) are already known. Judge round 1 (docs/JUDGE_ROUND_A5_CHATGPT_2026-10-07.md) raised items 3 and 4. No A7 query has been run beyond pinning sources.

## Frozen inputs (sha256 in data/SHA256SUMS.txt)
- data/raw/ebi_proteins_P0AFY6_sbmA_ecoli.txt - UniProt P0AFY6 (SBMA_ECOLI, 406 aa) via EBI Proteins API.
- data/raw/kegg_ko_K17938_genes.txt - KEGG ortholog K17938 gene list as returned by the fetch tool. Caveat: tool output overflowed once; completeness of the list is not guaranteed and is itself checked in (ii).
- Any additional source (S. maltophilia candidate sequences, waa-family UniProt/EcoCyc records) must be pinned with sha256 BEFORE it is used, and listed in the A7 result with the pin commit.

## Questions and decision rules
(i) waaY vs waaP: record UniProt/EcoCyc function text for both. Call "same function class" only if both records state the same enzymatic activity (core-heptose kinase). Otherwise "not established". No pooling of waaY and waaP counts is done either way; A7 only reports the label.
(ii) S. maltophilia SbmA: a candidate counts as ortholog only if (a) it is in the KO K17938 gene list for an S. maltophilia strain, or (b) a pinned pairwise global alignment to P0AFY6 gives >=35% identity over >=80% of both lengths AND it carries SbmA/BacA family annotation (Pfam SbmA_BacA). If neither is found, the outcome is "no ortholog identified with pinned sources" and is NOT read as proof of absence. Prior hit check already done: KEGG Smlt4102 (UniProt B2FHX9) is an ABC permease, not SbmA; EBI B2FT66 is a TonB receptor. Both are excluded.
(iii) Mutation-opportunity null (judge item 4): attempted only if (i) and (ii) finish; design to be stated in a separate A7b lock before any computation. Otherwise reported as deferred.

## Deviation rule
Any change to the above after this commit is recorded in the A7 result under "Deviations".
