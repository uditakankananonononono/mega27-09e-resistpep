# A6 event-tier robustness result
Locked at 8769356e6204dec1291720f5fa843a0755a2f01e before computation
(prereg docs/PREREG_ADDENDUM_A6_EVENT_TIER_ROBUSTNESS_2026-10-07.md).
Origin: judge round 1 minimum upgrade path (items computable from pinned
data). Re-cut of the locked A5 ledger only; no new data; no MIC values.

## Guards
A5 totals reproduced exactly (405 / 383 / 16 / 3 / 3) and the full A5
within-study recurrence table recomputed identical from the ledger.
19 unit tests pass (tier mapping, unknown-type halt, real-data block
coalescing, no-false-cross, guards, result structure). Independent
second-pass strict recount identical.

## 1. Strict Tier A cross-study recurrence (judge upgrade item 1)
Removing all large-deletion-membership-only observations, exactly one gene
recurs across studies: sbmA (unchanged from the all-tier cut). Direct
disruption evidence:
- Spohn 2019 PR39 line PR39_5: short deletion Delta1 bp at 392,493.
- Bac7 2023 strain B1: IC3-like IS element insertion (1.4 kb).
- Bac7 2023 strain B2: single nucleotide polymorphism.
Three independent direct events in two independent E. coli studies.
Judge kill condition 1 (recurrence dies without block membership): FAILED
to kill the finding.

## 2. Event coalescing exposes a shared-breakpoint structural hotspot
The 8 Spohn lines carrying sbmA via large deletions coalesce to 3 structural
events, and ALL THREE share the same start breakpoint 388,423:
- Delta5,466 bp (PR39_2)
- Delta7,615 bp (BAC5_7)
- Delta8,821 bp (PR39_1, PR39_7, PR39_10, BAC5_3, BAC5_5, BAC5_10)
The 6-line Delta8,821 block with identical boundaries under two different
proline-rich AMPs is consistent with a recurrent deletion hotspot and/or an
early shared variant, not six independent selections of sbmA. Judge kill
condition 2 (recurrence as shared structural event) therefore PARTIALLY
materializes for Tier B: the block evidence is breakpoint-driven, and is
reported as locus-level, not gene-targeted, evidence. Note the direct
PR39_5 hit (392,493) lies INSIDE the spanned locus (388,423-397,244):
direct and structural disruption point at the same locus.

## 3. A second hotspot explains most block-driven recurrence
Delta11,471 bp @ 275,642 appears in 11 lines across FIVE AMPs (PR39, BAC5,
CAP18, HBD3, PEX), spanning the yag/argF/ins block. Together with the
388,423 locus, two breakpoint hotspots account for the bulk of the 65
solely-large-deletion-driven within-study recurrences flagged in A5.
Two ars-locus blocks (@ 3,624,595 / 3,629,456) are single-line events.

## 4. All-recurrent-genes comparison (descriptive; full table in JSON)
93 within-study recurrences reclassified: 65 solely block-driven, 29 with
at least one Tier A line (one row counted under both cuts). sbmA is the
ONLY gene recurring across studies under either cut. Strongest direct-tier
within-study recurrences: sspB (Blanco PR-39, 6 lines / 6 direct events),
basS (Spohn CAP18, 4 lines / 9 direct events), waaY (Spohn BAC5, 3 lines /
6 direct events), macA (PR39, 3 lines / 5), lptC (LL37, 3 / 4), basR (HBD3,
3 / 3), mraW (Blanco LL-37, 3 / 3), wzzE (LL37, 3 / 3), pitA (LL37, 3 / 4),
yejK/yejL intergenic (PEX, 4 lines / 2 events). In the all_recurrent_genes
JSON table, tierA_lines/tierB_lines/direct_events/block_events/n_studies
are GENE-GLOBAL statistics repeated on each (study,amp) row; n_lines and
mutation_types are per (study,amp).

## 5. Claim status after A6 (per judge amendment wording)
"Parallel recurrence of sbmA disruption across independent proline-rich AMP
evolution experiments" is supported: direct-disruption evidence in two
independent E. coli studies plus a shared-breakpoint structural hotspot at
the sbmA locus in Spohn. "Convergence" remains UNEARNED: the
mutation-opportunity null (judge upgrade item 4) and the S. maltophilia
SbmA orthology resolution (item 3) require external references and are
deferred to the queued annotation unit. No p-values by design (A6.4).

## Disclosed limitations
- Coordinate-identity checks were extractable for Spohn only (MOESM9
  Start bp); Blanco/Bac7 direct events are counted per independent
  strain/clone as designed, coordinates not extracted (A6.3 disclosure).
- Tier B blocks coalesced globally per study (conservative: minimizes
  event counts); a within-amp coalescing view would not change any
  cross-study conclusion.
- The shared 388,423 breakpoint has two live explanations (mutational
  hotspot vs early/ancestral variant); pinned sources do not distinguish.
