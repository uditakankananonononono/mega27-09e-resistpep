# Judge round 1 - A5 sbmA cross-study recurrence (2026-10-07)

Surface: chatgpt.com, user's signed-in session (read lease, config-c).
Conversation: https://chatgpt.com/c/6ac6695a-8438-83ee-af81-8fdd881e8c72 ("Evaluate Convergence Claim").
Authority: user, WhatsApp 2026-09-28 07:18-07:20 IST (verified author=user):
"Don't wait for my chatgpt audit", "Do it yourself", "I meant u use chatgpt", "Not me" -
superseding the 2026-09-27 courier-paste requirement. See docs/JUDGE_ROUNDS.md.
Object reviewed: A5 cross-study mutation recurrence result
(docs/A5_MUTATION_CONVERGENCE_RESULT_2026-10-07.md, result commit 1d002f4).

## Exact prompt submitted

You are an independent scientific judge reviewing a completed, preregistered descriptive analysis. Be exacting. Your job: (1) verdict on whether the finding's stated claim strength is justified, (2) the weakest points, ranked, (3) concrete analyses or checks that would turn this from descriptive observation into a stronger claim, or kill it. Do not be polite; be accurate.

CONTEXT
Research lane: antimicrobial peptide (AMP) resistance evolution. Three independent published evolution experiments were re-analyzed under a locked preregistration addendum (locked BEFORE extracting mutation-table values; exposure of two smaller inputs disclosed in the lock document). The locked question: do independently evolved AMP-resistance lineages from DIFFERENT studies and organisms converge on the same genes? Mutation content only - no MIC/outcome values used. 405 mutation records: Spohn 2019 (E. coli BW25113, 12 AMPs x 10 lines, 383 records), Blanco 2020 (S. maltophilia D457, LL-37 and PR-39 clones, 16 records, 4 medium-adaptation control clones excluded per source paper's own logic), Bac7 2023 (E. coli MDR 1057, Bac7(1-22) strains B1-B3, 3 records). Every extracted gene string verified verbatim against pinned source bytes (sha256-pinned primary XML/supplements); 13 unit tests pass; independent second-pass recount identical.

HEADLINE FINDING (stated as descriptive, hypothesis-generating, explicitly NOT a mechanism claim)
sbmA is the only gene hit in >=2 of the 3 studies:
- Spohn 2019: PR39 5/10 lines (short deletions + large-deletion membership), BAC5 4/10 lines (large-deletion membership only - flagged weaker, block co-deletion).
- Bac7 2023: 2/3 strains (IS-element insertion + point mutation); the source paper itself reports sbmA as resistance-mediating for Bac7(1-22).
Synthesis: the SbmA transporter is recurrently hit under three different proline-rich AMPs (PR-39, bactenecin-5, Bac7(1-22)) across two independent studies and two E. coli strain backgrounds. Both source papers report SbmA within their own study; the cross-study synthesis is the new descriptive contribution.

NEGATIVE CONTEXT / HONEST COUNTER-EVIDENCE (reported in-document, not hidden)
- Blanco 2020 PR-39 lines in S. maltophilia show NO sbmA hit (their convergence is sspB, 6/8 lines). Whether S. maltophilia has an SbmA ortholog is unverified from pinned sources - reported as absence-of-hit, not absence-of-gene.
- 65 of 93 within-study gene recurrences are driven SOLELY by shared large deletions (co-deleted blocks); flagged driven_by_large_deletion and not treated as independent per-gene evidence. sbmA's Spohn PR39 recurrence is partly short-deletion driven (not solely large-deletion), but its BAC5 recurrence IS solely large-deletion membership.
- No enrichment p-value: deferred because gene-set sizes and annotation bias make a defensible null non-trivial.
- Name-family observation waaY/waaP (LPS core) reported as UNVERIFIED, not counted.
- Bac7 n=3 strains only. Selection regimes, organisms, and mutation spectra differ across studies.

QUESTIONS FOR YOU
1. Verdict: is "recurrent disruption of sbmA across independent proline-rich AMP evolution studies" a justified descriptive claim, an overclaim, or an underclaim? Grade it as if reviewing for a careful journal.
2. Ranked weaknesses: what are the strongest objections (statistical, biological, methodological)?
3. What specific, feasible analyses (using these datasets or public references) would most increase or destroy confidence? Prioritize by information gained per unit effort.
4. Is the large-deletion co-deletion flagging sufficient, or is there a better way to handle mutational target-size confounding across studies?
5. What would you require before the word "convergence" (versus "parallel recurrence" or weaker) is earned?

## Full response received (verbatim page text)

Verdict

The core claim is justified as a descriptive observation, but “convergence” is currently too strong if it is intended to imply non-random evolutionary convergence.

I would accept:

“sbmA was recurrently disrupted in independent evolution experiments involving proline-rich AMPs.”

I would also accept, with careful qualification:

“Parallel recurrence of sbmA disruption was observed across two independent E. coli AMP-evolution studies.”

I would not yet accept:

“AMP resistance evolution converges on sbmA.”

That formulation implies a stronger inference about preferential evolutionary targeting than the analysis currently establishes.

The interesting part is real: sbmA is the only gene recurring across ≥2 of the 3 studies, and the recurrence involves three proline-rich AMPs and two E. coli backgrounds. But the evidence is heterogeneous: 5/10 PR39 lines versus 4/10 BAC5 lines where the latter recurrence is entirely embedded in a large deletion, versus 2/3 Bac7 strains with direct mutations. Those are not equivalent observations.

1. Claim-strength grade
Claim	Verdict
“sbmA occurs in ≥2 independent studies”	PASS
“sbmA is recurrently disrupted across independent experiments”	PASS
“sbmA recurs under three proline-rich AMPs”	PASS, with qualification
“sbmA recurrence is independent of any single study”	PASS
“sbmA is a particularly recurrent target”	NOT YET ESTABLISHED
“AMP resistance evolution converges on sbmA”	OVERCLAIM
“parallel recurrence/convergence of sbmA disruption”	Plausible but needs qualification
“sbmA is a candidate recurrent evolutionary target”	PASS

The strongest defensible conclusion is therefore something like:

Across three independently published AMP-evolution datasets, sbmA was the only gene with reported disruption in at least two studies. Its recurrence involved three proline-rich AMPs and two E. coli backgrounds, although the evidence differs in mutation type and target-size independence across datasets.

That is scientifically stronger than trying to squeeze a causal/convergent interpretation out of the current evidence.

2. Ranked weaknesses
1. Target-size / mutation-opportunity confounding is the biggest unresolved problem

This is the central objection.

A gene being hit repeatedly does not automatically mean selection repeatedly targeted that gene.

You need to distinguish:

P(gene hit)=f(gene size,mutational accessibility,local sequence,structural variation,fitness effects,selection)

Your current analysis establishes recurrence, but not that the recurrence is more frequent than expected given opportunity to mutate.

This matters particularly for sbmA because the Spohn BAC5 observation comes entirely from a large deletion. A gene sitting inside a deletion has a very different probability of appearing in the mutation table than a gene requiring an independent point mutation.

Your large-deletion flag is therefore necessary but insufficient.

2. The three mutation observations are not equivalent evidence

This is a major interpretational issue.

You effectively have:

Spohn PR39: 5/10 lines, including short deletions.

Spohn BAC5: 4/10 lines, but only because they carry a shared large deletion.

Bac7: 2/3 strains, with an IS insertion + point mutation.

These should not simply be mentally converted into “11/23 lineages hit sbmA.”

That would exaggerate the evidentiary weight.

I would classify them separately:

Tier A — direct/local disruption

independent point mutation

IS insertion

small deletion

Tier B — structural-event membership

gene lies inside a large deletion

Then report both.

If sbmA remains recurrent under an analysis that excludes all block-membership observations, your claim becomes substantially stronger.

3. Only two studies actually contribute positive cross-study evidence

The three-study framing is slightly misleading.

Blanco contributes an important negative/contrastive observation, but the positive sbmA recurrence is:

Spohn → Bac7

Blanco does not independently reproduce sbmA.

That's not a flaw in the result—it is useful heterogeneity—but don't describe this as three independent confirmations.

The appropriate structure is:

“sbmA recurred in two independent E. coli evolution studies, while the S. maltophilia study did not report an sbmA hit.”

That is much harder to attack.

4. Bac7 n=3 is extremely small

2/3 sounds dramatic but statistically contains very little information.

One mutation changes the proportion from 2/3 to 1/3 or 3/3.

So the Bac7 dataset should be treated as replication of occurrence, not strong frequency evidence.

The fact that the source paper independently implicated SbmA is valuable, but it doesn't increase the independence of your observation. It actually means your analysis is partly rediscovering a known biological result.

That's fine—the novel component is the cross-study synthesis, not discovery that SbmA matters in Bac7.

5. Gene-level recurrence is vulnerable to annotation and mutation-spectrum bias

The 405 records are not 405 equivalent opportunities.

Different studies can have:

different sequencing technologies,

different mutation-calling thresholds,

different structural-variant detection,

different experimental durations,

different numbers of sampled clones,

different AMP exposures,

different starting genomes,

different background mutation rates.

Therefore:

“Only sbmA recurred across studies”

is an empirical statement about the reported mutation tables, not necessarily about the complete evolutionary mutational landscape.

Your source-byte verification is excellent for extraction integrity, but it does not solve ascertainment bias.

6. Independence of lineages needs careful definition

Ten lines from one experiment aren't equivalent to ten independent evolutionary populations across laboratories.

Your strongest unit of replication is:

study × organism/background × AMP regime

not individual mutation records.

The manuscript should never allow 383 Spohn records to visually overwhelm the 3 Bac7 observations.

7. The S. maltophilia comparison is biologically unresolved

You correctly avoided saying:

“S. maltophilia lacks sbmA.”

Good.

But until you establish whether a genuinely homologous SbmA exists—and whether its function is comparable—the negative result has limited mechanistic meaning.

This is an easy thing to fix.

3. Highest-value analyses

I would do these in roughly this order.

Analysis A — Remove every large-deletion membership event

This is the single most informative robustness test.

Define:

Strict recurrence set =

point mutations

IS insertions

small/local deletions

other mutations directly disrupting the gene

Exclude:

gene appears solely because it lies inside a large deletion.

Then ask:

Does sbmA still recur across studies?

From your description:

Spohn PR39: yes

Spohn BAC5: no

Bac7: yes

Therefore sbmA still appears in 2 independent studies.

That is important.

Your headline could then explicitly say:

“The recurrence persists when genes identified solely through large-deletion membership are excluded.”

That is a much stronger result than the current aggregate recurrence count.

Analysis B — Separate “event recurrence” from “gene recurrence”

For every sbmA observation, create something like:

Study	AMP	Lineages	Mutation class	Direct disruption?	Independent event?
Spohn	PR39	5/10	small deletion + deletion membership	partly yes	determine
Spohn	BAC5	4/10	large deletion	no	likely shared event
Bac7	Bac7(1-22)	2/3	IS + point mutation	yes	determine

Then count independent mutational events, not just affected lineages.

This could dramatically change the interpretation.

For example, five lineages carrying the same deletion are not necessarily five evolutionary hits.

If the 5/10 PR39 observations are one ancestral deletion followed by propagation, the evidence is much weaker than five independent deletions.

Conversely, five independently arising deletions would be much more compelling.

Determine whether the mutations are phylogenetically/event-wise independent.

This is probably the most important analysis after excluding block deletions.

Analysis C — Reconstruct the mutation opportunity for sbmA

For each study, calculate something like:

observed sbmA hits/expected sbmA hits

But don't use a naïve genome-length denominator.

Build the expected opportunity from the actual mutation spectrum.

For example, if point mutations are involved:

nucleotide composition

trinucleotide context

observed substitution spectrum

gene length

coding sequence

known mutational hotspots

For deletions:

gene length

local repeat structure

flanking homology

known deletion architecture

For IS insertions:

number/distribution of insertion sites

whether sbmA lies in an insertion-prone region

This gives you a much better question:

Was sbmA hit more often than its mutational opportunity predicts?

That is the bridge from observation → evolutionary inference.

Analysis D — Permutation/null model across the actual mutation tables

This is probably your best feasible statistical analysis.

Construct a null where mutations retain relevant properties but gene identity is randomized.

For example:

Null 1: mutation-type-preserving permutation

Randomly reassign mutations among genes while preserving:

mutation class

mutation size

study

organism

possibly genomic position constraints.

Then calculate:

number of genes recurring across ≥2 studies.

Repeat thousands of times.

Ask:

P(maximum cross-study recurrence≥observed)

More specifically:

P(a gene has recurrence pattern as extreme as sbmA)

If sbmA is common under the null, your “convergence” story weakens substantially.

If it is unusually rare, confidence increases.

Analysis E — Homology/orthology check for SbmA

Resolve the Blanco issue.

Identify whether S. maltophilia D457 contains:

an SbmA ortholog,

a divergent homolog,

no credible homolog.

Use a reproducible public-reference method and report sequence identity/coverage plus genomic context.

Three outcomes:

Ortholog exists

The Blanco negative becomes biologically meaningful.

Highly divergent homolog

Interpret cautiously.

No ortholog

Then the organismal difference itself becomes an informative explanation for the apparent restriction of recurrence to E. coli.

This could actually make the story more interesting.

Analysis F — Compare against all recurrent genes, not just sbmA

The reader needs to know whether sbmA is exceptional.

You have:

93 within-study gene recurrences.

Make a table of:

number of studies hit

number of independent events

direct vs block-derived

mutation classes

gene length

functional category.

Then ask:

Is sbmA unusually recurrent compared with the distribution of other genes?

If 40 genes recur twice and sbmA happens to be the only one crossing some arbitrary criterion because of how the datasets are structured, the headline becomes much less impressive.

If sbmA is genuinely an outlier, that is powerful.

4. Is your large-deletion flagging sufficient?

No.

It's good bookkeeping, but it isn't a complete solution to target-size confounding.

You are currently distinguishing:

direct mutation vs co-deleted gene.

You additionally need to distinguish:

independent evolutionary events vs repeated observations of the same structural event.

Those are different problems.

A better hierarchy would be:

Level 1 — mutation observation

A mutation table says sbmA is affected.

Level 2 — direct disruption

The mutation directly alters sbmA.

Level 3 — independent event

The disruption arose independently rather than being inherited/shared.

Level 4 — mutation-opportunity adjusted

The number of independent disruptions exceeds what mutational opportunity predicts.

Level 5 — selection-supported convergence

The recurrence is unlikely under the neutral/opportunity model and is biologically associated with resistance.

You're currently around Level 2–3.

Your desired “convergence” claim really belongs around Level 4–5.

5. The most important distinction: recurrence vs convergence

I'd be strict about terminology.

“Recurrence”

Safest.

sbmA was repeatedly disrupted.

Requires essentially no inference beyond the mutation data.

“Parallel recurrence”

Reasonable if independent evolutionary events can be established.

Independent lineages repeatedly acquired alterations affecting the same gene.

This is stronger and biologically meaningful.

“Parallel evolution”

Potentially justified if independent populations acquire similar genetic changes under comparable selective pressure.

Still somewhat broad.

“Convergence”

I would reserve this for evidence that different evolutionary trajectories repeatedly arrive at the same functional/genetic solution, preferably with evidence that this recurrence exceeds mutational expectation.

The fact that PR39, BAC5 and Bac7 are all proline-rich AMPs makes the biological argument interesting, but it does not itself demonstrate convergence.

What would make me upgrade the paper?

I would want four things.

Minimum upgrade

Exclude large-deletion-only observations.

Establish independent mutational events.

Resolve whether S. maltophilia has an SbmA ortholog.

Show a mutation-opportunity-aware null/permutation analysis.

If sbmA remains exceptional after those four, I would be comfortable with:

“parallel recurrence of sbmA disruption across independent AMP-resistance evolution experiments.”

Stronger upgrade

Add:

Mutation-spectrum-aware expected-hit model.

Comparison against all other recurrent genes.

Functional/pathway-level analysis.

Independent external AMP-evolution datasets not used to formulate the observation.

Then you can reasonably argue:

“The repeated disruption of sbmA is consistent with convergent evolutionary targeting under proline-rich AMP selection.”

Notice the wording: “consistent with”, not “proves.”

What could kill the finding?

These are the failure modes I'd actively try to falsify.

Kill condition 1

After removing large-deletion membership, sbmA no longer recurs across independent events.

Then the headline becomes much weaker.

Kill condition 2

The apparent PR39 recurrence is actually one ancestral/shared deletion rather than independent events.

That could substantially reduce the strongest Spohn evidence.

Kill condition 3

A mutation-opportunity null shows that sbmA's recurrence is completely ordinary.

Then you have an interesting descriptive fact, but not evidence for preferential targeting.

Kill condition 4

A broader, independently assembled AMP-evolution dataset shows dozens of genes recurring at equal or greater frequency.

Then “sbmA is unusually convergent” should be abandoned.

Kill condition 5

The Bac7 mutations are not independent or cannot be confidently attributed to sbmA disruption.

Then the cross-study evidence becomes considerably thinner.

My journal-style final judgment

Finding: Valid descriptive observation.

Claim strength: Appropriate if phrased as recurrence; too strong if phrased as established convergence.

Novelty: The likely novel component is not SbmA biology itself, because both contributing source papers already implicate it. The novel contribution is the cross-study synthesis demonstrating recurrence across independently generated AMP-evolution datasets and AMP backgrounds.

Most serious weakness: mutation opportunity and independence of mutational events.

Large-deletion handling: Good first-pass control, insufficient as the final treatment.

Highest-value next analysis:
Reclassify every sbmA observation by independent event + direct disruption, remove block-only observations, then run a mutation-spectrum/target-opportunity-aware permutation null.

If sbmA survives that—and remains an outlier relative to the rest of the genome—I would upgrade the result substantially.

Recommended headline

“Parallel recurrence of sbmA disruption across independent proline-rich antimicrobial peptide evolution experiments”

with the subtitle/qualification:

A preregistered cross-study mutation-table analysis identifies sbmA as the only gene recurrently disrupted across two independent E. coli AMP-evolution studies; recurrence persists when large-deletion-only membership is excluded, but mutation-opportunity and event-independence remain important constraints on convergence inference.

That is about as strong as I think the present evidence can honestly support.

## Verdict summary (agent-distilled; the verbatim text above governs)
- Finding: valid descriptive observation. Novelty is the cross-study synthesis,
  not SbmA biology itself (both source papers already implicate sbmA).
- "convergence" ruled an OVERCLAIM at current evidence; accepted formulations:
  "sbmA was recurrently disrupted in independent evolution experiments involving
  proline-rich AMPs" and "parallel recurrence of sbmA disruption".
- Framing correction: positive evidence is TWO independent E. coli studies;
  Blanco (S. maltophilia) is a negative/contrastive observation, not a third
  confirmation.
- Evidence tiers required: Tier A direct disruption (point mutation, IS
  insertion, small deletion) vs Tier B large-deletion membership only.
- Most serious weakness: mutation opportunity and independence of mutational
  events; large-deletion flag is necessary but insufficient.
- Minimum upgrade path (locked as prereg addendum A6): exclude
  large-deletion-only observations, establish independent mutational events,
  resolve S. maltophilia SbmA orthology, mutation-opportunity-aware null.
  The first two are computable from pinned data; the latter two need external
  references and are deferred to the queued pathway/annotation unit.
