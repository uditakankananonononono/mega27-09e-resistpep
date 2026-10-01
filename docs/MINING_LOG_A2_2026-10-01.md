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

## Pass 1 addendum (same day): Spohn et al. 2019 - ELIGIBLE-CANDIDATE

Spohn et al. 2019, Nat Commun 10.1038/s41467-019-12364-6 (PMC6778101),
E. coli K-12 BW25113, 14 chemically diverse AMPs x 10 independent evolved
populations each (~120 generations), plus 12 antibiotics. Verified via
Europe PMC full text + supplementary zip (shape check only, no outcome
values read, per the locked no-peeking rule):
- Supplementary Data 1 (MOESM5): fold-change MIC table per AMP.
- Source Data Fig 1A (MOESM14): per-line relative resistance levels,
  ~275 rows (140 AMP + 120 antibiotic adapted lines + headers).
- Supplementary Data 3 (MOESM7): physicochemical variable table; exact
  sequences to pin from Supplementary Table 1 (MOESM1 PDF) at adoption time.
- Overlaps with current base: cecropin P1 and pexiganan (independent
  replication in E. coli, a new organism for both). PXB is a lipopeptide -
  covered by the deferred eligibility question. PROA (protamine) is a
  heterogeneous peptide preparation - flagged for the estimand addendum.
- OPEN adjudication for the next estimand addendum (not decided here):
  matched passage-control structure. The published design compares adapted
  lines to the wild-type ancestor; presence of no-drug passage controls is
  unverified. A2.3 allows "ancestor MIC enabling a defensible control
  contrast"; whether that is defensible for this dataset is a prereg
  decision, not a mining decision.
If adopted, this roughly doubles-plus the sequence-distinct unit base
(~12 new single-sequence AMPs with per-lineage MICs in a fourth organism).

Updated pass 1 yield: 1 eligible-candidate (Spohn 2019, control-structure
adjudication pending), 1 candidate access-pending (Habets 2012), 3 ruled
ineligible. Lazar 2019 (PMC6915728, chemical-genetic profiling) queued,
not yet shape-checked.
