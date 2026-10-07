# A5 cross-study mutation convergence result
Locked at 429b2ce3207bb4d022ed5fc0c2fdb84a3deade00 before reading Spohn
MOESM9 values. Blanco/Bac7 gene exposure disclosed in the lock.

## Headline (descriptive, hypothesis-generating)
sbmA is the only gene hit in >=2 of the 3 studies:
- Spohn 2019 (E. coli BW25113): PR39 5/10 lines (short deletions +
  large-deletion membership), BAC5 4/10 lines (large-deletion membership
  only - weaker, block co-deletion).
- Bac7 2023 (E. coli MDR 1057): 2/3 strains (IS-element insertion +
  point mutation), reported there as resistance-mediating.
Convergent signal: the SbmA transporter is recurrently hit under three
different proline-rich AMPs (PR-39, bactenecin-5, Bac7(1-22)) across two
independent studies and two E. coli strain backgrounds. Both source papers
report SbmA within their own study; the cross-study synthesis is this
lane's new descriptive contribution, not a new mechanism claim.
Negative context, direction-neutral: Blanco 2020 PR-39 lines in
S. maltophilia D457 show NO sbmA-named hit (their convergence is sspB,
6/8 lines). Whether S. maltophilia has an SbmA ortholog is not verifiable
from pinned sources; reported as absence-of-hit only, not absence-of-gene.

## Strong within-study recurrences (not solely large-deletion-driven)
- Blanco PR-39: sspB 6/8 lines (SNP/indel mix).
- Spohn PR39: sbmA 5/10 (short+large deletions), skp 2, macA 3,
  basS 2, ddlA 3, iraP 3, waaY 2, ybjX 2, yai clusters.
- Spohn CAP18: basS 4/10 (SNP+insertion).
- Spohn HBD3: basR 3/10 (SNP).
- Spohn LL37: lptC 3, pitA 3, wzzE 3, wecA 2 (mixed types).
- Spohn PEX: yejK/yejL intergenic 4/10.
- Spohn BAC5: waaY 3/10 (insertion+short deletion), aceE 2, pagP 2.
- Blanco LL-37: mraW 3/8 clones (deletions).
65 of 93 within-study recurrences are driven SOLELY by shared large
deletions (co-deleted blocks, e.g. yag/yai clusters); these count once
per event biologically and are flagged driven_by_large_deletion in JSON.
They are not treated as independent per-gene evidence.

## Name-family observation (unverified, not a counted match)
waaY (Spohn BAC5/PR39/HBD3) and waaP (Bac7) share the waa LPS-core gene
family, but functional equivalence cannot be established from annotations
present in the pinned sources (per A5.4b). Reported as an unverified
observation only.

## Verification
13 unit tests pass (extraction, control exclusion, recurrence, flags).
Second-pass independent recount identical. Every extracted gene string
verified verbatim against pinned source bytes. 405 records:
383 Spohn evolved, 16 Blanco evolved, 3 Blanco control (excluded from
counts), 3 Bac7. No MIC/outcome values used; mutation content only.
No enrichment p-value (deferred per lock). No model refit.
