# A7b result - mutation-opportunity null (lock 9e50efd7569b3e9e2ef95e4294cf826d03560f88)
Script: scripts/opportunity_null_a7b.py. Output: results/opportunity_null_a7b.json. Seed 20261007, 100,000 reps.

## Locked analysis
Tier A events mapped to the 4,290 named K-12 genes: Spohn 121, Blanco 7, Bac7 3 (14 Spohn/Blanco records with unmapped gene names excluded, listed in JSON).
- Observed S1 (genes hit in >=2 studies) = 1 (sbmA).
- Null mean 0.405; 95th percentile 2. **p(S1) = 0.339.** Under the fixed rule: consistent with mutation opportunity at the gene-agnostic level. The recurrence does NOT beat a length-proportional null when any cross-study gene counts.
- sbmA-specific P(>=2 studies) = 0.00011 (descriptive only, post hoc: sbmA was chosen after seeing data, so this is not a test).

## Problem found after lock (disclosed deviation)
Blanco 2020 is S. maltophilia D457 (smd_ locus tags), not E. coli. Placing its 7 mapped events into the E. coli K-12 universe is invalid. The sbmA cross-study recurrence is Spohn (E. coli BW25113) + Bac7 (E. coli MDR 1057), both E. coli. Sensitivity run excluding Blanco (not locked, so secondary): Spohn 121 + Bac7 3 events; observed S1 = 1; null mean 0.120; **p(S1) = 0.116**; sbmA-specific 5e-05 (post hoc). Same reading: gene-agnostic test not significant at 0.05, though the 0.116 is closer than 0.339.

## Interpretation
- Judge item 4 answered: the sbmA recurrence is not established as exceeding mutation opportunity by the pre-fixed gene-agnostic test. It stays a descriptive observation with a post hoc sbmA-specific tail probability that is tiny but selected.
- Weaknesses of the null: length-proportional is crude (IS insertion hotspots, known sbmA loss-of-function tolerance, selection are not modelled); Bac7 contributes only 3 events (2 in sbmA); "sbmA recurrence" rests on that small count.
- Not read as proof either way. Further power would need new E. coli AMP-evolution datasets (mining families exhausted at current depth).
- Also: the A7 orthology gap now matters less for the sbmA claim, since the claim is E. coli-only; Blanco's lack of an sbmA hit says nothing without an S. maltophilia ortholog.
