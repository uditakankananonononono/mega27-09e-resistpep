# A2.3 mining log - 2026-10-01 pass 1
Protocol: locked in PREREG_ADDENDUM_A2 (eligibility: serial-passage /
experimental evolution under a single-sequence AMP, per-lineage MIC outcomes,
matched passage controls or defensible control contrast, exact sequence from
a pinnable primary source). Counts and availability only; no outcome values
logged for any candidate not yet ruled on.

Sources searched: Europe PMC REST (3 query families: "experimental evolution"
+ AMP resistance; serial passage + MIC lineages; named-AMP + replicate lines),
efetch/PMC full text for verification.

## Ruled INELIGIBLE (with reason)

1. Yu et al. 2025, mSystems 10.1128/msystems.01700-24 (PMC11915801),
   E. coli MG1655 vs antibiotics + AMPs (colistin, SAAP-148, SLAP-S25).
   Reason: one endpoint evolved strain per drug; replicate MIC assays are
   measurement replicates, not independent evolved lineages; no matched
   passage-control lineages. Side note: this resolves the 2026-09-30 flagged
   lead - the ASM page served spoofed UI text, but the paper is real and
   verified via Europe PMC full text.
2. "Adaptive Response of E. coli to Pexiganan" 2026 (PMC13603602).
   Reason: endpoint resistant population, no per-lineage MIC series, no
   matched passage controls; data = raw sequencing only (SRA PRJNA1484553).
3. Teixobactin prolonged exposure 2025 (PMC12691584), E. faecalis.
   Reason: evolved TOLERANCE, explicitly not resistance; 2 mutants per
   parental strain; no MIC fold-change series.

## CANDIDATE - ACCESS PENDING (no outcome values inspected)

4. Habets & Brockhurst 2012, Proc R Soc B 10.1098/rsbl.2011.1203
   (PMC3367763), S. aureus experimental evolution under pexiganan, multiple
   evolved populations, compensatory adaptation, cross-resistance to HNP-1.
   Blocker: full text not in PMC OA XML subset (efetch returns metadata
   only; Europe PMC fullTextXML 500; PMC HTML blocked to fetcher). Data
   shape unverified; 2012 short-format paper suggests figure-only MICs.
   Next: try publisher page / author repository / supplementary via DOI.

## Already known ineligible (from A1 audit, restated for completeness)

5. St Andrews / Dobson et al. 2020 (PMC7033599, pinned in data/raw):
   S. aureus AMP resistance pharmacodynamics; data = PRJNA399645 raw
   sequencing only, no per-lineage MIC matrix.
6. "Genomic Signatures..." 2016 (PMC4889650): same group, genomic focus;
   presumed same raw-sequencing-only limitation; to verify next pass.

## Leads queued for next pass

- Spohn et al. 2019 PNAS (DNA-encoded AMP screen + evolution) - not yet searched.
- Lazar et al. (E. coli AMP cross-resistance network) - not yet searched.
- Colistin/polymyxin evolution datasets: DEFERRED eligibility question -
  cyclic lipopeptides; sequence-feature definitions assume plain amino-acid
  sequences (A1 handled lipidation only via indicator). Decision belongs to
  the next estimand addendum, not this log.

Pass 1 yield: 0 eligible new datasets, 1 candidate pending access, 3 ruled
ineligible with reasons. Unit base remains 9 scored treatments.
