# A5 - Cross-study mutation convergence audit
Status: LOCKED 2026-10-07 before any extraction of mutation-table values.
Chosen under the user's 2026-10-07 20:51:49 IST standing delegation
(wamid.HBgMOTE4MTM0MDk4NTcxFQIAEhggQUNBNDA3OTJFQjZGMjBBNUQ4OEQ4NUU5RjNDOTdCMDcA,
"never ask my opinion except for sending emails. Do what's best").

## Question (novel to this lane)
Do independently evolved AMP-resistance lineages from DIFFERENT studies and
organisms converge on the same genes or pathways? No single pinned paper
answers this cross-study question; each reports only its own mutations.
This is a descriptive synthesis, not a predictive model, not a mechanism
proof. A recurrence count is a hypothesis-generating observation, not a
discovery claim; any stronger claim requires the reserved judge courier.

## Frozen inputs (all already pinned, sha256-verified)
1. Spohn 2019 (PMC6778101): MOESM9 mutation tables (SNPs, short/large
   deletions, insertions, intergenic) per evolved E. coli BW25113 line.
   Scope: the 12 adopted AMP treatments only (A3.3 exclusions stand:
   PXB, PROA lines excluded; antibiotic lines excluded).
2. Blanco 2020 (PMC7529437): Table 3 mutations per evolved
   S. maltophilia D457 clone. Scope: LL-37 and PR-39 clones only;
   colistin clones excluded (A3.3 lipopeptide rule); the 4 control
   clones used ONLY as medium-adaptation background filter, as the
   source paper itself does.
3. Bac7 2023 (PMC10145973): Table 1 mutations per resistant strain.
   Scope: Bac7(1-22) strains B1-B3 only; polymyxin B strains excluded.
All three datasets use population-derived clones/lines already locked in
scope. No new data source is fetched for this audit.

## Exposure disclosure (not blinded)
Blanco Table 3 and Bac7 Table 1 gene names were visible during prior
structure verification (mraW/rluD in Blanco LL-37 clones; sbmA/waaP in
Bac7 strains). Spohn MOESM9 values NOT yet read (sheet headers only).
The convergence question was chosen before reading Spohn mutation values;
it is therefore hypothesis-driven with respect to the largest input, but
partially informed by two smaller inputs. Disclosed, not hidden.

## Locked protocol
1. Extract per-line gene names verbatim from each pinned table. Record
   line ID, selecting AMP, organism, mutation type. No outcome values
   (MICs) enter this audit; it is mutation-content only.
2. Blanco control-clone mutations are tagged 'medium adaptation' and
   excluded from convergence counts (per source paper's own logic).
3. Within-study recurrence: genes hit in >=2 independent lines under the
   same AMP.
4. Cross-study recurrence:
   a. Exact gene-name/ortholog matches across studies. Ortholog mapping
      by gene name only (b-number to gene-name via the tables' own
      annotations where present); no external database fetch in this
      audit. Unresolved names stay unmapped and are reported as such.
   b. Pathway-level recurrence using ONLY functional annotations already
      present in the pinned tables (e.g. Blanco's 'potential contribution'
      column, Bac7's product column). No new annotations invented; where
      absent, the gene is reported unannotated rather than guessed.
5. Outputs: (i) full extracted mutation ledger JSON; (ii) within-study
   recurrence table; (iii) cross-study exact matches; (iv) cross-study
   pathway-level matches with the annotation provenance per match;
   (v) explicit list of genes that recur in >=2 of the 3 studies.
6. Direction-neutral reporting: all genes reported, not only recurrent
   ones. No p-values, no enrichment test (gene-set sizes and annotation
   bias make a defensible null non-trivial; testing is deferred to a
   future estimand if proposed). No model refit, no claim of mechanism.

## Verification
- Assert expected line counts per study (Spohn: 12 AMPs x 10 lines minus
  lines with no called mutation, reported as extracted; Blanco: 16
  peptide + 4 control clones; Bac7: 3 Bac7 strains).
- Extracted gene names must appear verbatim in the pinned source bytes;
  the script re-reads sources, it never accepts hand-typed genes.
- Unit tests for extraction, filtering, and recurrence counting,
  including a negative test proving control-clone exclusion works.
- Independent second pass: recount recurrences with a separate method
  (counter vs grouped iteration) and require identical results.
- Any discrepancy blocks the result; deviations logged in-document.
