# A4 - Blanco 2020 censor-aware descriptive replication
Status: LOCKED 2026-10-07 before structured extraction/aggregation.

## Authority and exposure
Owner delegated the pick in authenticated WhatsApp at 20:39:11 IST, replying
to the queue including the Blanco bounds-preserved/4-controls proposal:
wamid.HBgMOTE4MTM0MDk4NTcxFQIAEhggQUNENEM0N0VBN0E5NzQyQTAzMDYxNTQ4Rjg4RDg2NzIA.
Parent selected this proposal at 20:39:55. Prior inspection exposed numerical
MIC cells, including censoring patterns. This is NOT a blinded preregistration.
No structured outcome extraction/aggregation preceded this lock.

## Scope and units
Blanco et al. 2020, mSphere 10.1128/mSphere.00717-20, pinned PMC7529437 XML.
Table 1 population endpoints only: LL-37 and PR-39, eight populations each.
D457 is the ancestor. Only four reported MIEM no-AMP population rows enter
the measured control contrast. Eight controls were described in methods but
four endpoints are reported; no imputation. Table 2 derived clones, colistin
and mechanistic endpoints excluded. Do not pool with or refit A3.
Keep exact sequence and terminal chemistry: PR-39 C-terminal amidation;
LL-37 no terminal modification explicitly specified in methods (unknown,
not inferred). Same residue strings elsewhere do not prove same chemistry.

## Extraction and estimand
Retain original cell text, population ID, assay drug, MIC units mg/liter,
source table, and lower/upper interval endpoints with open/closed flags.
Numeric cell x is [x,x]. A >x cell is (x,infinity). Do not substitute cutoff,
midpoint, or assay maximum as an exact measurement. Unrecognized cells fail.

Per population, report net log2 MIC change relative to the median of the
four reported same-drug passaged control MICs. Check controls are exact;
if not, stop for an interval-control amendment before aggregation.
Ancestor-relative intervals also reported separately as a diagnostic.
Monotone transform preserves open lower bounds. Treatment-level median of
8 intervals uses the arithmetic mean of ordered 4th and 5th endpoints in
log2 space; upper bound infinity if either middle upper endpoint is infinite.
Lower-bound openness propagates if either contributing middle endpoint is
open. This estimates a finite-sample descriptive median, not a population
confidence interval. No bootstrap, prediction, p-value, gate or baseline win.

## Cross-study replication and claims
Compare only the LL-37/PR-39 residue identities to Spohn's pinned A3 units.
Report whether A4 median intervals contain the corresponding A3 point and
which study has a provably larger median, if interval bounds allow it.
These are descriptive checks across different species/media/chemistry,
not causal, generalization, assay-equivalence or new-sequence discoveries.
Chemistry mismatch/unknown is visible beside any comparison.
Report all intervals and all directions, not favorable examples only.

## Verification and stop rules
Assert exact expected population/control/ancestor counts and identities,
positive MICs, recognized censor syntax and exact control values. Validate
Table 1 XML cells against an independent published-paper PDF extraction.
Test interval parsing, even-sample median/open-bound handling, and monotone
log transforms, including deliberate malformed inputs. Source hashes pass.
Any discrepancy blocks the affected result. Every deviation logged explicitly.
