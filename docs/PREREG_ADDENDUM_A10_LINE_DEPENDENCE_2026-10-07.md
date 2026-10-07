# Prereg Addendum A10 - line-level dependence of waaY / basS hits with sbmA-deletion lines (LOCK)

Date: 2026-10-07. Parent-approved follow-up (1) to A9.

## Disclosed exposure (this makes the test descriptive, not confirmatory)
A9 printed the waaY line set (8 lines: BAC5_3, BAC5_7, BAC5_10, CAP18_8, HBD3_3, HBD3_10, PR39_1, PR39_2) and the basS line set (9 lines: CAP18_2, CAP18_5, CAP18_6, CAP18_10, HBD3_3, PEX_4, PEX_7, PR39_1, PR39_2), and I noted 5 of 8 waaY lines are sbmA-deletion lines. So the direction of the overlap is already known; this addendum fixes the null and the reading before the p-values are computed. Results are reported as descriptive dependence structure, whatever p comes out.

## Sets (Spohn 2019, 12 AMPs x 10 lines = 120 lines; all taken from pinned sheets via existing code)
- S: lines carrying a Tier B large deletion whose deleted-gene list includes sbmA (scripts/event_tier_robustness_a6.py spohn_blocks()).
- W: lines with >= 1 Tier A evolved event in waaY. B: lines with >= 1 Tier A event in basS (A9 definitions, same tier rule).

## Tests
Statistic = size of intersection. Primary: |W n S|. Secondary: |B n S| and |W n B|.
Null 1 (unstratified): hypergeometric exact over 120 lines.
Null 2 (AMP-stratified, primary reading): the lines of each AMP (10 per AMP) are permuted, keeping, within every AMP, the number of W lines and the number of S lines; 100,000 permutations, numpy default_rng seed 20261010; one-sided p = P(null >= observed). This asks whether overlap exceeds what shared AMP exposure alone would give.
Also report, descriptively: per-AMP counts of S, W, B; and whether the five overlapping lines' waaY events are of which type.

## Limits fixed in advance
S has about 8 lines, W 8, B 9; tiny counts, wide uncertainty. Lines of the same AMP are not independent of each other (shared medium/handling); AMP stratification only partly handles that. A dependence finding says the waaY (and basS) hits are not an independent line of evidence from the sbmA deletion story; it does not say they are non-causal or artefacts. A null finding does not prove independence.

## Reading rule (fixed)
Stratified p < 0.05 for |W n S|: report "waaY hits are concentrated in sbmA-deletion lines beyond AMP exposure; treat the A5/A9 waaY recurrence as dependent on the same lines". Otherwise: "no dependence beyond AMP exposure detectable at this n". Both are reported with the numbers.
