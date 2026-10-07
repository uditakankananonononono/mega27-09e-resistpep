# A10 result - line-level dependence (lock 7d0699e67224f60e38d8052f12500c4055277f60)
Script scripts/line_dependence_a10.py; output results/line_dependence_a10.json; seed 20261010, 100,000 permutations.

## Deviation from the lock, found while running
The lock says 120 Spohn lines (12 AMPs x 10). The A5 ledger holds mutation records for only SIX Spohn AMPs (BAC5, CAP18, HBD3, LL37, PEX, PR39; 28 distinct lines with at least one record). The script therefore used 60 candidate lines (6 AMPs x 10). Whether the other six adopted AMPs' lines were sequenced with zero called mutations or are simply absent from the pinned sheet is NOT established here. The primary AMP-stratified test is unaffected by 60 vs 120 (AMPs with no S or W lines contribute nothing to the within-AMP permutation); the unstratified hypergeometric depends on the universe, so it is given for 28 / 60 / 120 lines.

## Sets
S (sbmA-deletion lines, 8): BAC5_3, 5, 7, 10; PR39_1, 2, 7, 10. W (waaY Tier A lines, 8): BAC5_3, 7, 10; CAP18_8; HBD3_3, 10; PR39_1, 2. B (basS Tier A lines, 9): CAP18_2, 5, 6, 10; HBD3_3; PEX_4, 7; PR39_1, 2.

## [SUPERSEDED - see CORRECTION at end] Results (descriptive per lock; the overlap direction was known before the lock)
- **W n S = 5** (BAC5_3, BAC5_7, BAC5_10, PR39_1, PR39_2). AMP-stratified null mean 2.00, **p = 0.0046**. Hypergeometric p: 0.022 (28 lines), 0.0005 (60), 0.00002 (120). Locked reading rule (stratified p < 0.05): waaY hits are concentrated in sbmA-deletion lines beyond AMP exposure; the A5/A9 waaY recurrence is NOT an independent line of evidence from the sbmA deletion story. waaY events in those five lines: short_deletion (PR39_1, BAC5_10), insertion (BAC5_3, BAC5_7), SNPs (PR39_2).
- B n S = 2 (PR39_1, PR39_2): stratified p 0.135 (null mean 0.80). No dependence detected at this n (not proof of independence).
- W n B = 3 (HBD3_3, PR39_1, PR39_2): stratified p 0.040 (null mean 1.00). Note this is not multiplicity-corrected across the three tests and rests on 3 lines.
- Per AMP (S/W/B): BAC5 4/3/0, CAP18 0/1/4, HBD3 0/2/1, PEX 0/0/2, PR39 4/2/2.

## Meaning and limits
waaY hits cluster in lines that already carry sbmA deletions. Plausible readings, not tested: the same lines are hypermutable or carry linked rearrangements; the deletion lines had more sequencing/calling opportunity; or the waaY events are secondary adaptations in already-sbmA-deficient backgrounds. basS hits are mostly in other lines (CAP18, PEX). Counts are tiny (8-9 lines per set), same-AMP lines are not independent, three tests were run without correction, and the universe ambiguity above is unresolved. Consequence for the paper: do not present waaY recurrence as extra convergence evidence; keep the basS naming trap and this overlap as written caveats.

---
## CORRECTION (same day, supersedes the "Results" and "Meaning" sections above; first-run numbers retained, not deleted)
The pinned Spohn Supplementary Data 5 header reads "Mutations identified in the 38 whole-genome sequenced AMP adapted E. coli K-12 BW25113 lines". Lines per AMP in the sheets: BAC5 4, CAP18 5, HBD3 4, LL37 5, PEX 5, PR39 5 (28 adopted-AMP lines; PROA 5 and PXB 5 are not adopted). So the sequenced universe is **28 lines (per-AMP sizes 4/5/4/5/5/5)**, not 120 (lock) and not 60 (first run). Line labels run to _10 but only 4-5 lines per AMP were sequenced; the 6-AMP x 10 universe was wrong because most of those lines do not exist in the data. Re-run with the 28-line universe (same seed, same code otherwise; results/line_dependence_a10_corrected_universe28.json; first run kept as results/line_dependence_a10_first_run_60lines.json):
- W n S = 5: hypergeometric p 0.022; **AMP-stratified p = 0.601** (null mean 4.60).
- B n S = 2: stratified p 0.601. W n B = 3: stratified p 0.331.
**Locked reading rule applied to the correct universe: stratified p >= 0.05, so NO dependence beyond AMP exposure is shown.** The earlier "waaY hits are concentrated in sbmA-deletion lines (p = 0.0046)" statement was an artifact of the wrong denominator and is withdrawn. Within BAC5 (4 lines) and PR39 (5 lines), waaY and sbmA-deletion lines overlap nearly completely by construction of tiny strata; the data cannot separate shared-line dependence from AMP exposure. The 5-of-8 overlap remains a descriptive caveat, not evidence of either dependence or independence. Counts are tiny and lines within an AMP are not independent. The unstratified hypergeometric (0.022) uses 28 lines and ignores AMP structure, so it is not the locked primary.
