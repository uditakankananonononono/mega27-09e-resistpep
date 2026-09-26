# PRE-REGISTRATION DRAFT - mega27-09e (working title: ResistPep)
Status: LOCKED 2026-09-26 17:05 IST, before any outcome data was scored.
Source: ChatGPT ideation round 1 (2026-09-26), independently verified; user rules 1-7 apply.

## Question
Can evolutionary/robustness features distinguish AMPs with low resistance-emergence potential, and can that signal nominate NAMED candidates that are predicted antimicrobial AND evolutionarily robust?

## De-risked scope (locked)
Do NOT claim to predict resistance evolution directly (label sparsity). Locked proxy task: predict measured resistance-emergence outcomes in public serial-passage datasets, plus a robustness-proxy ranking (target conservation, evolutionary constraint, mutation accessibility) validated against those measurements.

## Data (public, verified to exist 2026-09-26)
- DBAASP (activity measurements), DRAMP.
- Serial-passage AMP resistance datasets: PLOS Figshare LL-37/CNY100HL/wheat-germ-histone resistance dataset (plos.figshare.com/articles/dataset/752076); St Andrews S. aureus AMP resistance-evolution dataset (research-portal.st-andrews.ac.uk; Frontiers fmicb.2020.00103).
- Bacterial genome context: NCBI/UniProt for target conservation.

## Benchmark gate
Sequence-only baseline models and any published AMP-resistance predictor on the identical frozen split; metrics AUROC + Spearman vs measured resistance fold-change. BEAT = exceeds the strongest eligible comparator on the primary metric.

## Discovery criterion (locked)
Named candidates satisfying: predicted antimicrobial activity (09a-family score or retrained), low k-mer similarity to known AMPs, targets conserved membrane features, predicted evolutionary robustness (proxy score top decile), active-spectrum plausibility across phylogenetically diverse pathogens. Zero-pass = documented negative + rule-6 pivot.

## Honest-negative protocol
Same as 09d.
