# A6 - Event-tier robustness of the sbmA cross-study recurrence
Status: LOCKED 2026-10-07 before any computation of the metrics defined here.
Origin: judge round 1 (docs/JUDGE_ROUND_A5_CHATGPT_2026-10-07.md) minimum
upgrade path, items computable from already-pinned data. Chosen under the
user's 2026-09-28 agent-run judge ruling and 2026-10-07 20:51:49 IST standing
delegation ("never ask my opinion except for sending emails. Do what's best").

## Exposure disclosure (not blinded)
The A5 result already exposed per-gene mutation classes, so the direction of
the strict-set outcome is partially anticipated (Spohn PR39 includes direct
short deletions; Spohn BAC5 is large-deletion membership only; Bac7 is
IS + point mutation). Disclosed, not hidden. All thresholds and classifications
below are fixed before the script defining them is written.

## Question
Does the sbmA cross-study recurrence survive the judge's robustness cuts, and
is sbmA exceptional against the full distribution of recurrent genes?
Descriptive robustness re-cut of the locked A5 ledger; no new data source.

## Frozen inputs
results/mutation_convergence_a5.json (405 records, A5-locked extraction) and
the pinned primary sources it derives from. No new fetch, no MIC values.

## Locked protocol
1. Tier classification per record (fixed mapping, defined in code with tests):
   Tier A (direct disruption): mutation_type in {SNP, SNPs, point_mutation,
   insertion, IS insertion, short_deletion, small deletion, indel, Del/Ins of
   <=50 nt, intergenic}.
   Tier B (block membership only): mutation_type = large_deletion.
   Any unrecognized type string halts the run (no silent reclassification).
2. Strict cross-study recurrence: genes with Tier A records in >=2 of the 3
   studies. Report alongside the A5 all-tier result; report which genes drop
   out (expected: Spohn BAC5 sbmA line support drops to Tier B).
3. Event-independence classification where determinable from pinned tables:
   lines sharing an identical large-deletion block (same reported deletion)
   count as ONE structural event; direct Tier A hits on the same gene in
   different lines count as independent events unless the pinned table shows
   identical coordinates. If the pinned table lacks coordinates, report
   "not determinable from pinned tables" - no guessing.
4. All-recurrent-genes comparison: for every gene with within-study recurrence
   (A5 table), report n_studies, Tier A vs Tier B split, mutation classes, and
   whether cross-study. Descriptive ranking only. No p-value; the
   mutation-opportunity permutation null needs an external mutation-spectrum
   reference and is explicitly DEFERRED to the queued annotation unit.
5. Outputs: results/event_tier_robustness_a6.json; result doc
   docs/A6_EVENT_TIER_ROBUSTNESS_RESULT_2026-10-07.md.

## Verification
- Unit tests for the tier mapping (every observed mutation_type string covered
  or run halts), strict-set counting, event coalescing, and a negative test
  proving Tier-B-only support cannot create a strict cross-study match.
- Independent second-pass recount by a separate method; identical required.
- Recompute A5 totals from the ledger as a guard: must match committed A5
  counts exactly (405 / 383 / 16 / 3 / 3).
- Deviations logged in the result document, never silently.
