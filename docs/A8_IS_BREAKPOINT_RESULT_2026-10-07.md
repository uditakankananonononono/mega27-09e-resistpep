# A8 result - IS association of Spohn large-deletion breakpoints (lock d60c91633498123605e05ecab3230559475e1440)
Script scripts/is_breakpoint_a8.py; output results/is_breakpoint_a8.json. Seed 20261008.

## Locked test
9 distinct breakpoints, 48 BW25113 IS (mobile_element) features. Within 200 bp of an IS: observed 4, null mean 0.131, 0 of 100,000 null draws >= 4 (p < 1e-5). Sensitivity W=50/500/1000: observed 4 each, p 0 / 0 / 1e-4 (20,000 reps, descriptive). Decision rule met: breakpoints associate with IS elements.

## Which breakpoints (table in JSON)
- 275,642 start (IS1B, 1 bp) and 287,112 end (IS1C, inside): the 11,471 bp deletion seen in 11 lines / 5 AMPs is flanked by IS1 copies at both ends. Pattern fits IS1-IS1 recombination; this is a fit, not a demonstration.
- 388,423 start shared by the three sbmA-spanning blocks: IS3B at 1 bp. The three ends (393,888 / 396,037 / 397,243) are NOT near IS, so those deletions are IS-bounded on one side only.
- 3,645,395 end shared by the 15,940 and 20,801 bp deletions: inside IS5T (1 bp). Their starts (3,629,456; 3,624,595) are not near an IS.
So 4 of 9 breakpoints, but they come from 3 independent loci.

## Caveats (stated before and found after)
- The null treats the 9 points as independent; they cluster in 3 regions. Post-lock conservative check (analytic, not part of the lock): unit = region, any breakpoint within 200 bp of IS. Random chance of an IS-near position is ~1.5% per point; for regions with 2, 4, 3 distinct points the chance of at least one hit is ~3.0%, ~6.0%, ~4.5%; all three together ~8e-5. Still small, but this rests on n = 3 loci.
- Reference-genome IS positions, not each evolved line's own assembly.
- This is a mechanism annotation for the Tier B hotspots (why the same deletions recur: IS-flanked loci recombine). It supports the A6 reading that Spohn block recurrence is breakpoint-driven rather than independent selection events, which weakens, not strengthens, treating the 8 sbmA block lines as 8 independent hits. It does not touch the strict Tier A sbmA result.
- Not a resistance claim.
