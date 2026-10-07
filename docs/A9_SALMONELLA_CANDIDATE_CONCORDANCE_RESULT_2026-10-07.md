# A9 result - Salmonella candidate genes vs Spohn E. coli lines (lock 35256e19567241f303cc3ab615f6931490e38fbb)
Script scripts/candidate_concordance_a9.py; output results/candidate_concordance_a9.json; seed 20261009, 100,000 reps.

## Orthology (descriptive, locked rule identity >= 35%)
WaaY Salmonella P26472 vs E. coli P27240: 162/232 identical (69.8%). PhoP Salmonella P0DM78 vs E. coli P23836: 208/224 (92.9%). Both pass. Caveats: Salmonella records are strain F98 (WaaY) and ATCC 14028 (PhoP), not LT2; scoring is a simple own implementation (+1/-1/-2).

## Locked test
121 mapped Spohn Tier A events (10 records unmapped to the K-12 universe). Primary candidates waaY and phoP: **T = 1** (waaY hit, phoP not hit). Null: mean T 0.041; P(T >= 1) = 0.0406. Per-gene null hit probability about 2.1% (waaY) and 2.0% (phoP).
**Locked decision rule requires T = 2 with p < 0.05, so the rule is NOT met.** Reading under the lock: no cross-species concordance beyond opportunity established for the primary set. I note, as description only, that the nominal p for T >= 1 happens to be 0.041, but T = 2 was the pre-declared bar and I am not moving it.

## Descriptive Spohn hits (not tests)
- waaY: 8 Tier A events in 8 lines (BAC5_3, BAC5_7, BAC5_10, CAP18_8, HBD3_3, HBD3_10, PR39_1, PR39_2) across 4 AMPs; types SNPs, insertion, short_deletion. Five of those lines (BAC5_3/7/10, PR39_1/2) are also lines with sbmA-spanning large deletions, so these may not be independent of the A6/A8 breakpoint story; not examined here.
- basS (E. coli name for Salmonella pmrB per UniProt synonym; secondary by lock, mapping by name only): 9 events in 9 lines (CAP18_2/5/6/10, HBD3_3, PEX_4/7, PR39_1/2); null hit probability about 3.3% per gene.
- phoP, phoQ, pmrA, waaP, waaZ: 0 Tier A events.

## Meaning
This is a weak, partly overlapping concordance: the Salmonella waaY candidate locus is also recurrently hit in E. coli lines (8 lines of 120), and so is basS/pmrB (9 lines), but the locked primary test is not met because phoP is not hit, and the Salmonella list was chosen by the authors for being hit (no independent test on that side). Not a named discovery, no candidate peptide; 09d gate unchanged.

## Follow-up questions this raises (not run, would need a new prereg)
(1) Do waaY and basS events cluster in the same Spohn lines as each other or as the sbmA deletions (dependence)? (2) For basS, an alignment check once a Salmonella PmrB sequence is pinned. (3) waaY Tier A insertion events: IS-mediated, per the A8 mechanism?
