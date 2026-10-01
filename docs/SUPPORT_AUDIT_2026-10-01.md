# Resistance-label support audit, October 1, 2026

This is a source-quality audit, not an outcome model, benchmark win, or replacement for the locked primary. No thresholds or primary outcomes have been changed.

`python3 scripts/audit_resistance_support.py` reads the pinned namespace-aware PMC XML, records hashes, original table rows and raw MIC strings, and preserves interval/right/left censoring rather than discarding inequality signs. The prior midpoint CSVs remain untouched and are not safe to use as uncensored training labels.

Current result: 45 source cells (19 exact, 12 ranges, 8 right-censored, 6 missing), not 45 independent peptide labels. Eight assertions checked exact/range/missing/left/right parsing, an inequality-containing range, table extraction and a real censored source entry.

- 2013 LL-37/CNY100HL/WGH study includes two named single peptide sequences and a mixture (WGH). Its evolved lineages, reconstructed clones and cross-resistance observations are nested biological units, not additional independent peptide identities. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3720879/
- The Table 4 header says mg/mL while surrounding methods use mg/L. Keep source strings and flag the discrepancy until independently reconciled; no silent unit conversion.
- 2020 study's main pharmacodynamic table concerns pexiganan-treated bacterial lines selected under different AMP conditions; selecting peptide is not automatically the assayed peptide. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC7033599/
- St Andrews's dataset page resolves to NCBI PRJNA399645 raw sequencing, not an independent downloadable MIC matrix: https://research-portal.st-andrews.ac.uk/en/datasets/resistance-evolution-against-antimicrobial-peptides-in-staphyloco/ (live checked October 1).

## Update: 2024 multi-peptide source verified and pinned

Antunes et al. 2024 (PLOS Biology, P. aeruginosa PA14; https://journals.plos.org/plosbiology/article?id=10.1371%2Fjournal.pbio.3002692) with data at Zenodo 10.5281/zenodo.11209304 supplies 6 single-sequence AMPs (Melittin, Pexiganan, Cecropin P1, PA-13, SLM1, SLM3) and 3 random mixtures, each with 6 evolved lineages + 6 matched passage controls, MIC fold-change vs ancestor (108 strain rows, 0.125-128x). Files pinned with sha256 (data/SHA256SUMS.txt). Combined with the 2013 study's LL-37 and CNY100HL, the verified single-sequence support base is now 8 distinct sequences - still small for any unseen-sequence generalization claim, and SLM1/SLM3 are lipidated (flag before plain-sequence use). The 2020 S. aureus study remains pharmacodynamic-only as described above.

Before training: the estimand, split, treatment-vs-assay-agent mapping, censor handling and independent-unit support must be locked in a new prereg addendum before any scoring. Current sources still do not by themselves support a named evolutionarily-robust discovery claim. A further lead (iScience 2025, temporin/melittin/pexiganan single + combination evolution, https://www.cell.com/iscience/fulltext/S2589-0042(25)00932-0) is located but its underlying data are not yet verified.
