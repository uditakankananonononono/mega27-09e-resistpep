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
- DBAASP / DRAMP: reuse the 09a pinned pulls (cross-repo copies to be made
  with sha256 carried over).
- St Andrews S. aureus AMP resistance-evolution dataset
  (Frontiers fmicb.2020.00103): locate the actual deposit via
  research-portal.st-andrews.ac.uk - NOT yet fetched.
