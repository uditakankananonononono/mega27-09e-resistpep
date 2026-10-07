# A16 result - observed-margin conditional permutation (lock 16f8156)
Script scripts/conditional_permutation_a16.py; output results/conditional_permutation_a16.json. Executed as locked, no deviations. T_obs reproduced A12 (4). Not blind: see lock disclosure.
## Null A (primary): row and column sums of the 20-line x gene matrix fixed, curveball, 100,000 samples
T_obs=4; null mean 0.959; 95th pct 2; 99th pct 3; null hist 0:28743 1:49985 2:18168 3:2859 4:240 5:5. p_A = 0.00246.
Locked reading (p_A <= 0.01): within-AMP recurrence exceeds what the observed gene-frequency and line-burden margins produce. Note this null is much less extreme than A12's (240 of 100,000 draws reach 4, versus 0 under the length-weighted redraw), so A12's p<1e-5 overstated the strength; p=0.0025 is the better figure.
## Sensitivity B (neighborhoods, same-strand CDS runs with gap <= 1,000 bp)
T_B_obs=5 (merging genes into neighborhoods created an additional recurring pair rather than removing any); null mean 3.09, 95th pct 5, 99th pct 6; p_B = 0.078. Under B the observed recurrence does NOT stand out.
## Combined honest reading
The primary locked endpoint is met narrowly (T=4 sits at about the 99.8th percentile of the margin-preserving null), but the neighborhood-collapsed sensitivity shows nothing unusual (p_B=0.078). Because B is a secondary sensitivity and not a second endpoint, the primary reading stands, yet the claim should be stated as: modest, margin-conditional excess that is not robust to collapsing linked genes. Still a hypothesis-generating descriptive pattern; 09d gate remains UNMET. Caveats: not blind to the data; lines within an AMP are not independent; the margin null can erase real signal; the 1,000 bp rule was fixed beforehand and is not retuned.
