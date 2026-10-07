# A4 Blanco descriptive replication
Locked at 2e39960ce55a0244007eba11b475a0738988c85c before structured
extraction/aggregation, after incidental numerical exposure (disclosed).

## Results
16 evolved population endpoints, 4 reported passaged-control populations.
Controls match ancestral MICs for both drugs; no missing controls imputed.

| Drug | Median net log2 MIC interval | Fold-change interpretation | Spohn A3 point | Ordering |
| --- | --- | --- | --- | --- |
| LL-37 | (1, infinity) | strictly greater than 2-fold | 4.3502 | Not orderable; point is inside the interval |
| PR-39 | (3, infinity) | strictly greater than 8-fold | 1.2925 | Blanco median is above the Spohn point |

These are finite-sample median bounds, not confidence intervals. LL-37 has
5/8 right-censored endpoints; PR-39 has 8/8. Do not replace lower bounds with
exact changes. PR-39 is explicitly C-terminal amidated in Blanco; LL-37's
terminal modification is not explicitly specified. Spohn chemistry has not
been adjudicated for equivalence; a residue match is not a chemistry match.
Different species, media and assay designs prohibit a causal/generalization
claim. Spohn points retain their existing 4-decimal rounding.

The result documents descriptive cross-study heterogeneity. It does not beat
a named predictive baseline, establish a novel mechanism, or enlarge/refit A3.
No discovery/win claim, p-value or significance gate. All intervals and both
directions are retained in results/blanco_intervals_a4.json.

## Verification
All 29 Table 1 population rows (including excluded colistin rows) matched
independent pdftotext output from the pinned published PDF. XML row/ID counts,
positive recognized MIC syntax, 4 exact controls, exact sequence strings and
PR-39 amidation annotation are asserted by the extraction script. Eight
unit tests cover exact/censored values, median openness, malformed syntax,
empty input and bad references. Source hashes checked before handoff.

## Sources
- https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7529437/fullTextXML
- https://digital.csic.es/bitstream/10261/228725/1/Antimicrobial_Blanco_PV_Art2020.pdf
- Spohn comparison: pinned results/spohn_units_a3.json and A3 prereg chain.
