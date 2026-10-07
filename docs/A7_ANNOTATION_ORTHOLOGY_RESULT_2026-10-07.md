# A7 result - annotation and orthology (locked in 036e075)

## (i) waaY vs waaP
Pinned UniProt records (EBI Proteins API): P25741 WaaP = LPS core heptose(I) kinase, EC 2.7.1.235, phosphorylates HepI. P27240 WaaY = LPS core heptose(II) kinase, EC 2.7.1.-, phosphorylates HepII.
Lock rule: "same function class" only if same enzymatic activity. Result: NOT the same activity. Both are LPS inner-core heptose kinases acting on different heptose residues. Verdict: same pathway step family, not functionally equivalent. Any earlier wording treating waaY/waaP as interchangeable is withdrawn; counts stay unpooled (as locked).

## (ii) S. maltophilia SbmA orthology (judge item 3)
- KO K17938 pinned gene list: no Stenotrophomonas entries (Sinorhizobium bacA entries present, E. coli sbmA present).
- Live KEGG per-organism link queries for sml/smt/smz/sma/smaf returned empty content, but a positive control FAILED to discriminate: link/sml for K02004 (which contains Smlt4102) was also empty. So empty responses are uninformative here; rule (a) is inconclusive, not negative.
- Rule (b) (alignment >=35% id/>=80% length plus SbmA_BacA annotation) was not executable: no S. maltophilia SbmA candidate sequence could be obtained with the available routes. The pinned distribution paper (PMC12003926) has no S. maltophilia mention.
- Excluded candidates: Smlt4102 (B2FHX9, ABC permease), B2FT66 (TonB receptor).
Outcome per lock: "no ortholog identified with pinned sources". NOT evidence of absence. Judge item 3 stays OPEN. The sbmA recurrence finding applies to the E. coli lineages only; any claim extended to S. maltophilia remains unsupported.

## (iii) Mutation-opportunity null (item 4)
Not started. Requires an A7b lock first. Deferred.

## Deviations
None to the A7 lock. Added pins (P25741, P27240, PMC12003926) listed in SHA256SUMS; the lock allowed pins before use.
