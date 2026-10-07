# mega27-09e-resistpep (working title: ResistPep)

MEGA-PROGRAM-27 item 9, project 5: evolution-guided discovery of antimicrobial
peptides predicted to remain effective under resistance pressure. De-risked,
preregistered scope: predict measured resistance-emergence outcomes in public
serial-passage datasets and build a robustness-proxy ranking (target
conservation, evolutionary constraint, mutation accessibility) validated against
those measurements - then nominate NAMED candidates that are predicted
antimicrobial AND evolutionarily robust, across independent evidence layers.

Status (2026-10-07): preregistration locked (docs/PREREGISTRATION.md); outcomes have since been scored under the dated addenda in docs/, and the results so far are negative or inconclusive. A1 (9 units, leave-one-study-out): model Spearman -0.547, bootstrap 95% CI [-0.915, 0.116], permutation p=0.924 (results/score_a1.json). A3 enlarged base (21 units): Spearman 0.112, CI [-0.275, 0.490], permutation p=0.281 (results/score_a3.json). A7b mutation-opportunity null: p=0.34 locked, 0.116 E. coli-only sensitivity, with the Blanco dataset being S. maltophilia (deviation disclosed; results/opportunity_null_a7b.json). A5/A6 (descriptive, judge-reviewed 1 of 1): sbmA is the one gene with strict Tier A mutation recurrence across independent studies (E. coli Spohn 2019 + Bac7 2023); the A7b null does not show this exceeds mutation opportunity, so it stays a descriptive observation, and a ChatGPT judge round cut the original 'convergence' wording to 'parallel recurrence' (docs/JUDGE_ROUND_A5_CHATGPT_2026-10-07.md). No candidate peptide is nominated and no robustness-proxy validation is established.
Origin: user rules 1-8 (2026-09-26)
session (untrusted advice, all dataset claims independently verified: DBAASP,
DRAMP, PLOS Figshare 752076 LL-37 resistance dataset, St Andrews S. aureus AMP
resistance-evolution dataset). Rules of the house: real public data only, locked
splits before outcomes, honest negatives preserved and never terminal (rule-6
pivots), minimum 1 user-provided judge verdict (rule updated 2026-09-27) producing a concrete novelty
change (rule 8), 50+ text-page paper.

Note (2026-10-08): Spohn 2019 denominators are sequenced lines only (28 adopted-AMP lines; BAC5 4, CAP18 5, HBD3 4, LL37 5, PEX 5, PR39 5). Older "x/10" figures in docs/A5 are corrected there. The 2013 LL-37 study is Lofton et al. (earlier alias "Prabhu 2013"). Current claim state: docs/CLAIM_STATE_2026-10-08.md; manuscript: paper/resistpep.pdf (8 pages; the 50+ page requirement is unmet).
