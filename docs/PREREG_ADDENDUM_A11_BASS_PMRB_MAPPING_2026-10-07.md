# A11 prereg (locked before the alignment is computed) - E. coli basS vs Salmonella PmrB mapping
Question: is E. coli K-12 BasS (UniProt P30844, pinned) the ortholog of Salmonella typhimurium LT2 PmrB (UniProt P36557, pinned data/raw/ebi_proteins_P36557.txt; its UniProt gene names list basS, parB, pmrB, STM4291)?
Method: global Needleman-Wunsch (BLOSUM62, gap open 10 / extend 1) identity over the aligned length, as in A9, between P30844 and P36557 sequences read from the pinned files.
Rule: mapping CONFIRMED at the name level if identity >= 70% and length ratio >= 0.9; otherwise UNCONFIRMED. A9 reported PhoP 92.9% and WaaY 69.8% as references only; no threshold is changed.
Scope: this only firms the basS naming bridge. It does not change A9 (rule not met) or A10 (no dependence shown). Salmonella strain is LT2 here; A9 used F98/ATCC 14028 for other genes - noted.
