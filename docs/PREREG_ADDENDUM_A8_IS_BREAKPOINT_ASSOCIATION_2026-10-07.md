# Prereg Addendum A8 - IS-element association of Spohn large-deletion breakpoints (LOCK)

Date: 2026-10-07. Chain: ... A6 -> A7 -> A7b -> A8. Option (c) of the parent plan: a new analysis class (mechanism: IS/repeat-mediated structural events) on existing data. Motivated by the AmpliFinder lead (PMC13423834, mining pass 6) and the A6 finding that Spohn large deletions share breakpoints.

## Disclosed exposure
A6 already showed the block starts/lengths (e.g. 388,423 shared by three sbmA-spanning blocks; Delta 11,471 @ 275,642 in 11 lines). I have NOT looked at IS positions relative to these breakpoints before this lock. I only checked that the pinned BW25113 reference is in Spohn's coordinate system: sbmA is at 392,095-393,315 in CP009273.1, and the 5,466 bp block starting at 388,423 ends at 393,888, so it spans sbmA, consistent. (MG1655 U00096.3 coordinates are about 6.7 kb larger there and are NOT used for this question.)

## Frozen inputs
- data/raw/ecoli_bw25113_CP009273.1_features.tsv (sha256 in SHA256SUMS): complete CDS (4,313) and mobile_element (48, annotated "insertion sequence:IS...") features of E. coli BW25113 CP009273.1, assembled from 36 overlapping efetch windows (edge-truncated features recovered from overlaps; completeness not independently audited).
- Spohn large-deletion blocks via scripts/event_tier_robustness_a6.py spohn_blocks() (pinned MOESM9 sheet): Start and Length, end = Start + Length - 1.

## Hypothesis and test
H: Spohn large-deletion structural breakpoints lie near annotated IS elements more often than random genome positions.
- Breakpoint set: the distinct coordinates among all block starts and ends of the A6.3 coalesced events (shared coordinates counted once).
- Statistic T = number of distinct breakpoints whose position is within W = 200 bp of any mobile_element interval (distance 0 if inside).
- Null: the same number of positions drawn uniformly over 1..4,631,469; 100,000 replicates, numpy default_rng seed 20261008; one-sided p = P(null >= observed).
- Sensitivity (descriptive, not tests): W = 50, 500, 1000. Secondary definition of IS: CDS whose product matches transposase|IS[0-9]|insertion sequence, reported descriptively.
- Per-breakpoint table is reported either way (nearest IS name and distance).

## Limits fixed in advance
Only ~9 distinct breakpoints, and the sbmA blocks share one start, so effective independence is lower than the count; power is low and a non-significant result is "no evidence", not absence. IS positions are from the ancestor reference, not each evolved line's own assembly. Hotspot proximity to IS would suggest, not prove, IS-mediated recombination. Not a resistance-selection claim.

## Decision rule
p < 0.05 at W = 200: breakpoints associate with IS elements (descriptive mechanism note, still not a novelty claim by itself). Otherwise: no IS association detectable at this n. Either result is reported in full and does not change A5/A6/A7b conclusions.
