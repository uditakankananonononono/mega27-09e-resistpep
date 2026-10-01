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

## Pass 2 partial (same day)

7. Kintses/Lazar et al. 2019, Nat Commun 10.1038/s41467-019-13618-z
   (PMC6915728), chemical-genetic profiling: INELIGIBLE as a new dataset -
   its laboratory-evolution analysis re-uses the Spohn 2019 evolved lines
   (its ref 20). Derivative of an adopted dataset; its cross-resistance
   analyses may still be cited as context, never as new units.
8. Spohn 2019 (PMC6778101): ADOPTED under addendum A3 (ef2b29b), scored
   under A3.5 (5064a12). Moved from mining to the scored base.

Open: Habets 2012 (PMC3367763) full-text access (publisher/repository or
cloud-browser route); Spohn 2019 also evolved TPII/PXB on other strain
backgrounds (out of A3 scope; logged here for any future estimand);
colistin/polymyxin eligibility stays deferred.

## Habets 2012 access attempts (2026-10-01, all failed legally-available routes)

- royalsocietypublishing.org DOI page: 403 to plain fetch (bot wall).
- Europe PMC fullTextXML: 500 (not in OA XML subset; efetch returns
  metadata only).
- Unpaywall: is_oa=true but locations are the PMC HTML page (blocked) and
  a Manchester repository record (metadata only, no PDF/files linked).
- Remaining route: cloud browser (user profile) on the PMC HTML page or
  the publisher page - queued as first item next run. Note: even on
  access, 2012 RSBL format suggests figure-only MICs; if confirmed
  figure-only it joins the ineligible list with the ovispirin-pattern gap.

## Pass 3 (same day): citation-graph mining + tenecin cluster

Via Europe PMC CITES on the three core studies:
9. Bolten/Rolff trade-off paper 2025 (PMC11802329, pinned) + its source
   study Makarova et al. 2018, Sci Rep 10.1038/s41598-018-33593-7
   (PMC6193990, pinned + supplement zip). S. aureus SH1000, 5 independent
   lines under tenecin 1 (single sequence) WITH matched passaged
   procedural controls nested per line - the exact control structure the
   protocol wants. VERDICT: PARTIAL/INELIGIBLE as pinned - own-treatment
   (tenecin 1) per-line MICs are figure-only (Figs 1-2, log2 MIC);
   supplements carry cross-resistance MICs (Table S1: colistin/melittin/
   vancomycin per line) and mutated loci (Table S3), not the
   own-treatment series. The 2025 refubium deposit covers the 2025 in
   vivo figures, not the 2018 MIC series. Path to upgrade: author
   request or figure digitization (would need its own prereg decision on
   digitization error). Tenecin 1+2 combination excluded regardless.
10. Bac7 resistance genomics 2023 (PMC10145973): proline-rich AMP Bac7;
    genomic-focus; not shape-checked yet - queued.
11. Efflux-pump heterogeneity 2025 (PMC12226021): queued, not shape-checked.
Pass 3 yield: 0 newly eligible, 1 partial (Makarova 2018 - true matched
controls but figure-only own-treatment MICs), 2 queued.
