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

## Continuation 2026-10-07: recovered remote + queued structure checks

Recovery: cloned remote aeb645bd224fab2b55aa192ee4374bada9a47766.
All 21 source-manifest entries verify. Re-running the Spohn extraction exactly
reproduces results/spohn_units_a3.json. No new scoring or estimand change.

4. Habets 2012: primary full text still ACCESS PENDING. Browser attempt on
   PMC3367763 returned an empty page; publisher challenge cleared to an empty
   article-abstract redirect. Publisher web fetch gives site scaffolding;
   Paperity exposes partial secondary text, not enough to settle primary
   data availability. No payment/account action or author request made.
   Source: https://royalsocietypublishing.org/doi/10.1098/rsbl.2011.1203
   Secondary: https://paperity.org/p/38231798/therapeutic-antimicrobial-peptides-may-compromise-natural-immunity

10. Bac7 2023: PARTIAL, NOT ADOPTED. Primary full text explicitly reports
    drug-free serial passage controls and multiple selection paths under
    Bac7(1-22), split by salt-containing/salt-free medium and differing
    passage duration. Thus the prior genomic-focus shorthand is insufficient
    as an exclusion. Figure 1 holds passage trajectories; Table 2 includes
    own-treatment endpoint MIC cells for a subset of selected strains, with
    right censoring. Controls are described as unchanged but per-control
    lineage counts and endpoint rows are not established in the inspected
    text. Supplement description names Table S2 for exact peptide sequences;
    actual supplement access/sequence verification remains open. A complete
    per-lineage, matched-condition endpoint matrix has not been established.
    No outcome aggregation, selection by effect magnitude or modeling.
    Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10145973/
    Supplement pointer: https://www.mdpi.com/article/10.3390/membranes13040438/s1

11. Efflux-pump heterogeneity 2025: INELIGIBLE for the current evolutionary
    estimand. The primary article studies transient phenotypic variants of
    stationary-phase bacteria, acute peptide accumulation/survival and
    transcriptomics, not an independently evolved serial-passage MIC panel.
    PMC fetch returned no content; author repository copy of the published
    eLife paper supplied the methods and abstract. Useful mechanistic
    context, never new evolution units.
    Source: https://iris.unica.it/retrieve/9dd5ee58-0095-4301-8d0c-525ede36dc61/elife-99752.pdf
    Publisher: https://elifesciences.org/articles/99752

No-peeking deviation disclosed: full-page primary and secondary fetches
incidentally exposed numerical MIC/effect text for Bac7 and Habets. These
values were not extracted into a dataset, aggregated, modeled or used to
rank candidates. Any future adoption must disclose this exposure in its
pre-outcome estimand addendum; do not describe this continuation as blinded.

Next: inspect Bac7 supplementary sequence/control structure and widen to
Dryad/Figshare data deposits. No newly eligible dataset claimed in this pass.

## Pass 4 - 2026-10-07 evening: data-deposit broadening

12. Blanco et al. 2020, mSphere 10.1128/mSphere.00717-20 (PMC7529437):
    ELIGIBLE STRUCTURAL CANDIDATE, not adopted or scored. S. maltophilia D457,
    daily serial passage in NaCl-free MIEM for 25 days. Methods specify 8
    independent replicates per condition; Table 1 reports 8 evolved population
    rows per AMP and 4 no-AMP control population rows. Do not invent the other
    4 control rows. Table 2 is derived clones, not independent new lineages.
    Own-treatment MIC cells contain substantial right censoring; PR-39's
    own-treatment population endpoints are all right-censored. Exact LL-37
    and PR-39 sequences are in primary methods; PR-39 is C-terminal amidated.
    Colistin excluded from proposed adoption under the deferred lipopeptide
    rule. LL-37/PR-39 are organism replications, not new sequence identities.
    Possible lane: censor-aware descriptive replication, not point-label A3
    model extension. Parent asked to review that proposal before a new lock.
    No outcomes extracted into a dataset or aggregated. Primary XML pinned.
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7529437/fullTextXML
    Published-paper copy inspected:
    https://digital.csic.es/bitstream/10261/228725/1/Antimicrobial_Blanco_PV_Art2020.pdf

13. Dobson/Purves/Rolff 2014 Dryad f80bh: deposit lists host survival/CFU
    files and a small cross-resistance MIC file. OWN-TREATMENT LINEAGE PANEL
    UNVERIFIED; file download returned 403. Not adopted; absence of a panel
    has not been proved. https://datadryad.org/dataset/doi:10.5061/dryad.f80bh

10. Bac7 update: primary XML retrieved and pinned via Europe PMC. Supplement
    zip endpoint timed out, publisher supplement had timed out earlier and
    direct publisher HTML returned 403. Exact supplement sequence/control
    completeness remain unverified. Partial candidate status unchanged.
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10145973/fullTextXML

Existing Figshare 752076/Spohn records rediscovered, not new datasets.
No-peeking deviation continues: primary full-text/XML source inspection
exposes MIC cells. No endpoint numerical values logged here or analyzed;
any adoption addendum must acknowledge this pre-lock exposure, not claim
blinding. Candidate choice is driven by structure/availability, not effect.

## Pass 4 follow-through: Bac7 supplement recovered; A3 reproduction

- A3's complete score_a3.py rerun reproduces committed score_a3.json
  byte-for-byte (all subsets and indicator runs). This is verification of
  the existing result, not a new evaluation or retry under changed metrics.
- Bac7 Europe PMC supplementaryFiles download succeeded on a bounded retry.
  Archive and extracted primary supplement PDF pinned in data/raw with hashes.
  Supplement contains primer/sequence tables and mechanistic figures, not a
  full per-lineage own-treatment MIC/control matrix. Table S2 verifies the
  Bac7(1-22) sequence from the study's own supplement. The earlier access gap
  is closed, but missing complete selection-path endpoints/control rows is
  not. Bac7 remains partial, not adopted; no digitization or outcome scoring.
  Source endpoint:
  https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10145973/supplementaryFiles

## Pass 5 - targeted deposit and older-source checks

14. Figshare 1007001 (LL-37 mutagenesis/pathoadaptation): INELIGIBLE for
    present lineage-MIC estimand. Deposit describes mucoid conversion and
    mutagenesis in P. aeruginosa, not a serial-passage AMP MIC panel.
    https://plos.figshare.com/articles/dataset/_Cationic_Antimicrobial_Peptides_Promote_Microbial_Mutagenesis_and_Pathoadaptation_in_Chronic_Infections_/1007001
15. Royal Society Figshare 5955796: INELIGIBLE as experimental data.
    Deposit is additional theoretical simulation/pharmacodynamic concepts.
    https://rs.figshare.com/articles/journal_contribution/Additional_Simulation_Results_and_Pharamacodynamic_Concepts_from_Predicting_drug_resistance_evolution_insights_from_antimicrobial_peptides_and_antibiotics/5955796
6. Dobson 2016 follow-through corrects the earlier presumed limitation:
   primary text DOES describe five selection lines per treatment with
   unselected passage controls; study analyzes clones derived from Dobson
   2013. It cannot be called sequencing-only solely from its abstract.
   Primary supplementaryFiles returns a zip containing a zero-byte
   supp_g3.115.023622_TableS2.pdf, not an inspectable full supplement.
   Per-lineage primary MIC matrix remains unverified, not proved absent.
   Follow upstream Dobson 2013 rather than count a derivative as new units.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC4889650/
   https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4889650/supplementaryFiles

Query scope: domain-targeted Dryad/Figshare/Zenodo AMP serial-passage
resistance and general iseganan/melittin/pexiganan lineage panels.
Non-peptide antibiotics, honey, cyclic lipopeptide biocontrol and integron
records are off-scope search returns, not screened AMP datasets.

## Upstream Dobson 2013 primary-source follow-through

16. Dobson et al. 2013 PLoS ONE e76521 (PMC3799789): STRUCTURAL CANDIDATE,
    not adopted. Five parallel lines per treatment with unselected controls.
    Table 1 explicitly reports per-population/per-week MIC fold changes,
    contrary to the earlier presumed sequencing-only boundary for its
    derivative 2016 study. Primary XML and complete supplement archive pinned.
    Important design limits: six-hour growth-derived MIC definition, some
    post-hoc culture exclusions, week-3 incubator failure/restart, and omitted
    late pexiganan MIC estimates due to starting-density effects. Supplement
    Methods S1 documents these issues. Mixed PGML treatment excluded from
    any sequence-level adoption. Exact study-specific sequence/terminal
    chemistry proof and control-row mapping remain to be settled.
    Any adoption needs a new locked definition of endpoint/week and censor/
    missingness handling, with incidental pre-lock outcome exposure disclosed.
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3799789/fullTextXML
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3799789/supplementaryFiles

This closes the scheduled queue of access/structure/deposit searches for
this pass, not the scientific lane. Blanco and Dobson proposals require an
estimand decision before numerical extraction or evaluation. No new finding
or enlarged scored base is claimed.

### Dobson control audit (same pass)

Table 1 has 30 rows across 6 selected treatments, with 5 population labels
per treatment. It has NO unselected-control treatment rows. Methods describe
unselected controls, but the pinned endpoint table alone does not establish
numerical matched-control correction. Do not equate design-level control
presence with an available control MIC series. Exact peptide identity by name
is also insufficient for study-specific sequence/terminal chemistry proof.
Thus Blanco remains the more complete adoption proposal; Dobson remains a
partial structural lead and is not an automatic new scored unit source.

## Pass 6 - 2026-10-07 late: forward-citation mining (Europe PMC CITES: queries)

Forward citations of the lane's four core studies screened for new
evolution datasets: Spohn 2019 (PMID 31586049, 286 citers), Blanco 2020
(PMID 32999081, 13), Bac7 2023 (PMID 37103865, 4). Dobson 2013
(PMID 24204634) PMIDs resolved; citer screen not run this pass.
Structure-only screening; no outcomes extracted; no adoption proposed.

17. Maron et al. 2025 iScience (PMC12167497, cites Spohn): ALREADY ADOPTED
    in the A1 estimand (S. aureus JLA513, temporin/melittin/pexiganan,
    Zenodo 15125182 + PRJNA1116739 pinned). Rediscovery, not a new dataset.
18. Yu et al. 2025 mSystems (PMC11915801, cites Spohn): ALREADY RULED
    INELIGIBLE in earlier passes (endpoint strains, no lineages; fetch
    spoof noted). Rediscovery via citation graph, disposition unchanged.
19. Tetens/Rodriguez-Rojas-group RPM paper 2024 (PMC11218975, cites
    Spohn): "The evolution of antimicrobial peptide resistance in
    P. aeruginosa is severely constrained by random peptide mixtures".
    NEW PARTIAL STRUCTURAL LEAD. Main text carries only 1 table (peptide
    sequences/activity); no per-lineage MIC or mutation matrix in the
    pinned main-text XML. Single-AMP vs random-mixture evolution design
    is a new angle for the lane, but lineage-level panel availability is
    UNVERIFIED; supplement fetch is the next step if a deposit unit
    needs it. Not adopted.
20. AmpliFinder 2026 (PMC13423834, cites Spohn): method + meta-analysis
    of 10,347 lab-evolved E. coli/A. baumannii isolates (IS-associated
    amplifications). METHOD LEAD only, not an AMP panel; noted for the
    queued mutation-opportunity/annotation unit (amplification modes are
    a missing mutation class in our Tier A/B scheme).
21. PMC10961912 / mSpectrum 2022 (spectrum.00973-22, cites Blanco):
    serial-passage + quantitative proteomics METHODS paper (pinned as
    spectrum00973_supp.zip). Screened: protocol description, no lineage
    dataset. INELIGIBLE as a data source.
22. ESKAPE antibiotics-in-development 2025 (39805953) and Gram-positive
    candidates 2025 (39772773): antibiotic (non-peptide) evolution,
    OFF-SCOPE under A3.3. Bac7 citers (4) are reviews/chemistry, no new
    evolution datasets.

Pass 6 adds ZERO new eligible datasets. One new partial structural lead
(19, supplement check pending), one method lead (20). Deposit-host query
families (Dryad/Figshare/Zenodo + citation graph of all pinned cores) are
now exhausted at this screening depth; further yield likely requires the
queued pathway/annotation unit's external references rather than more
deposit queries.
