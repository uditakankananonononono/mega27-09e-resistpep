# Resistance-label support audit, October 1, 2026

This is a source-quality audit, not an outcome model, benchmark win, or replacement for the locked primary. No thresholds or primary outcomes have been changed.

`python3 scripts/audit_resistance_support.py` reads the pinned namespace-aware PMC XML, records hashes, original table rows and raw MIC strings, and preserves interval/right/left censoring rather than discarding inequality signs. The prior midpoint CSVs remain untouched and are not safe to use as uncensored training labels.

Current result: 45 source cells (19 exact, 12 ranges, 8 right-censored, 6 missing), not 45 independent peptide labels. Eight assertions checked exact/range/missing/left/right parsing, an inequality-containing range, table extraction and a real censored source entry.

- 2013 LL-37/CNY100HL/WGH study includes two named single peptide sequences and a mixture (WGH). Its evolved lineages, reconstructed clones and cross-resistance observations are nested biological units, not additional independent peptide identities. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3720879/
- The Table 4 header says mg/mL while surrounding methods use mg/L. Keep source strings and flag the discrepancy until independently reconciled; no silent unit conversion.
- 2020 study's main pharmacodynamic table concerns pexiganan-treated bacterial lines selected under different AMP conditions; selecting peptide is not automatically the assayed peptide. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC7033599/
- St Andrews's dataset page resolves to NCBI PRJNA399645 raw sequencing, not an independent downloadable MIC matrix: https://research-portal.st-andrews.ac.uk/en/datasets/resistance-evolution-against-antimicrobial-peptides-in-staphyloco/ (live checked October 1).

Before training: expand public evidence, distinguish treatment agent from assay agent, retain lineage/study/sequence IDs, specify censor handling and independent-unit support, then lock any new split/estimand before evaluation. These sources alone do not support a claim that a sequence model predicts resistance-emergence in unseen peptides or a named evolutionarily robust discovery.
