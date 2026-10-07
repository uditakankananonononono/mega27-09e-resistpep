# A10 result - line-level dependence (lock 7d0699e67224f60e38d8052f12500c4055277f60)
Script scripts/line_dependence_a10.py; output results/line_dependence_a10.json; seed 20261010, 100,000 permutations.

## Deviation from the lock, found while running
The lock says 120 Spohn lines (12 AMPs x 10). The A5 ledger holds mutation records for only SIX Spohn AMPs (BAC5, CAP18, HBD3, LL37, PEX, PR39; 28 distinct lines with at least one record). The script therefore used 60 candidate lines (6 AMPs x 10). Whether the other six adopted AMPs' lines were sequenced with zero called mutations or are simply absent from the pinned sheet is NOT established here. The primary AMP-stratified test is unaffected by 60 vs 120 (AMPs with no S or W lines contribute nothing to the within-AMP permutation); the unstratified hypergeometric depends on the universe, so it is given for 28 / 60 / 120 lines.

## Sets
S (sbmA-deletion lines, 8): BAC5_3, 5, 7, 10; PR39_1, 2, 7, 10. W (waaY Tier A lines, 8): BAC5_3, 7, 10; CAP18_8; HBD3_3, 10; PR39_1, 2. B (basS Tier A lines, 9): CAP18_2, 5, 6, 10; HBD3_3; PEX_4, 7; PR39_1, 2.

## Results (descriptive per lock; the overlap direction was known before the lock)
- **W n S = 5** (BAC5_3, BAC5_7, BAC5_10, PR39_1, PR39_2). AMP-stratified null mean 2.00, **p = 0.0046**. Hypergeometric p: 0.022 (28 lines), 0.0005 (60), 0.00002 (120). Locked reading rule (stratified p < 0.05): waaY hits are concentrated in sbmA-deletion lines beyond AMP exposure; the A5/A9 waaY recurrence is NOT an independent line of evidence from the sbmA deletion story. waaY events in those five lines: short_deletion (PR39_1, BAC5_10), insertion (BAC5_3, BAC5_7), SNPs (PR39_2).
- B n S = 2 (PR39_1, PR39_2): stratified p 0.135 (null mean 0.80). No dependence detected at this n (not proof of independence).
- W n B = 3 (HBD3_3, PR39_1, PR39_2): stratified p 0.040 (null mean 1.00). Note this is not multiplicity-corrected across the three tests and rests on 3 lines.
- Per AMP (S/W/B): BAC5 4/3/0, CAP18 0/1/4, HBD3 0/2/1, PEX 0/0/2, PR39 4/2/2.

## Meaning and limits
waaY hits cluster in lines that already carry sbmA deletions. Plausible readings, not tested: the same lines are hypermutable or carry linked rearrangements; the deletion lines had more sequencing/calling opportunity; or the waaY events are secondary adaptations in already-sbmA-deficient backgrounds. basS hits are mostly in other lines (CAP18, PEX). Counts are tiny (8-9 lines per set), same-AMP lines are not independent, three tests were run without correction, and the universe ambiguity above is unresolved. Consequence for the paper: do not present waaY recurrence as extra convergence evidence; keep the basS naming trap and this overlap as written caveats.
