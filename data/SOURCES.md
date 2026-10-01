# ResistPep data provenance (pinned)
- PLOS Figshare article 752076: "Mechanisms and Fitness Costs of Resistance
  to Antimicrobial Peptides LL-37, CNY100HL and Wheat Germ Histones"
  (S. typhimurium serial-passage resistance study). API-verified 2026-09-27.
  data/raw/figshare752076_Table_S1.docx (WT MICs, verified readable),
  Table_S2.docx (strain scar table). sha256 in data/SHA256SUMS.txt.
  Table S3-S6.docx (WGS mutation tables for LL-37 x2, WGH, CNY100HL
  resistant isolates) pinned + sha256. Resistance MIC/fold-change data is in
  MAIN TEXT, not supplements: PMC3720879 (PLOS ONE 2013, DOI
  10.1371/journal.pone.0068875) full-text XML pinned via NCBI OAI; parsed by
  scripts/parse_pmc_tables.py into data/processed/: table2 evolved-lineage MICs,
  table3 fitness costs, table4 AMP MICs + fold-changes vs DA6192 WT
  (WGH 6.25 / LL-37 6.25 / CNY100HL 2.5 mg/L), table5 antibiotic
  cross-resistance, table1 genotypes. Ranges mid-pointed (documented in script).
- DBAASP / DRAMP: cross-repo copies made from the 09a pinned pulls
  (mega27-09a data/raw/novelty_refs/, manifest docs/NOVELTY_REFS_MANIFEST.md).
  data/external/refs/dramp_natural_amps.txt sha256
  fbaebb527695785ec3e5c0d13cf6a4eb82aadfeeb5bca64e534fcfe22efd12aa (matches
  the 09a manifest exactly); dbaasp_all.fasta sha256
  8d5c7db2b3f647567c5a0dc36b7cf96f763215614d449a37fdb39e8aa96e0c10 (546
  canonical 5-150aa monomer sequences from the DBAASP API pull of 25,542
  records). Hashes re-verified after copy.
- St Andrews S. aureus AMP resistance-evolution study
  (Frontiers fmicb.2020.00103, PMC7033599): full-text XML pinned via NCBI OAI
  (sha256 above). Data availability: WGS at NCBI BioProject PRJNA399645 (raw
  reads, not fetched - large, optional). The single main-text table
  (pharmacodynamic parameter estimates) and MIC/curve data are mostly in
  figures; the St Andrews PURE dataset landing page
  (research-portal.st-andrews.ac.uk/en/datasets/resistance-evolution-against
  -antimicrobial-peptides-in-staphyloco/) is located but its file list is
  JS-rendered - needs a browser pass to enumerate actual files (queued).
- Antunes et al. 2024, PLOS Biology 22(7) e3002692 (P. aeruginosa PA14
  experimental evolution): paper verified live 2026-10-01
  (https://journals.plos.org/plosbiology/article?id=10.1371%2Fjournal.pbio.3002692).
  Data: Zenodo 10.5281/zenodo.11209304 (record page verified live). Pinned
  2026-10-01: Underlying figures data.xlsx + Pharmacodynamics_datasets.xlsx,
  sha256 in data/SHA256SUMS.txt. Design per paper text: 9 antimicrobials =
  6 single-sequence AMPs (Melittin, Pexiganan, Cecropin P1, PA-13, SLM1,
  SLM3) + 3 random peptide mixtures (p-FdK5, p-FdK5 20/80, FK20); 6 evolved
  lineages + 6 matched passage controls per treatment; primary readout MIC
  fold-change vs ancestor (figures sheet, 108 strain rows, range 0.125-128);
  cross-resistance matrix and pharmacodynamic curves also present. SLM1/SLM3
  are palmitic-acid-modified (lipo)peptides per Fig 2 caption - flag before
  treating as plain sequence labels.
