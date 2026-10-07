import json,csv,sys
from pathlib import Path
from collections import defaultdict, Counter
import numpy as np
sys.path.insert(0,str(Path(__file__).parent))
from event_tier_robustness_a6 import tier
BASE=Path(__file__).resolve().parents[1]
LOCK='9e50efd7569b3e9e2ef95e4294cf826d03560f88'
uni={}
for r in csv.DictReader(open(BASE/'data/raw/ecoli_k12_U00096.3_cds_table.tsv'),delimiter='\t'):
    if r['gene']: uni[r['gene'].lower()]=int(r['length_bp'])
led=json.load(open(BASE/'results/mutation_convergence_a5.json'))
evo=[r for r in led['records'] if r.get('scope','evolved')=='evolved']
# one event per (study, gene, tier-A) event id: use A6.3 keys approximately via (study,line,gene,type) except spohn direct events keyed by line/type/gene too
ev=defaultdict(set); unmapped=defaultdict(int)
for r in evo:
    if tier(r['mutation_type'])!='A': continue
    g=r['gene'].lower()
    if g not in uni: unmapped[(r['study'],r['gene'])]+=1; continue
    ev[r['study']].add((g,r['line'],r['mutation_type']))
obs_genes=defaultdict(set)
for s,es in ev.items():
    for g,_,_ in es: obs_genes[g].add(s)
S1=sum(1 for g,s in obs_genes.items() if len(s)>=2)
names=list(uni); w=np.array([uni[n] for n in names],float); w/=w.sum()
n_by={s:len(es) for s,es in ev.items()}
rng=np.random.default_rng(20261007); R=100000
studies=sorted(n_by); cnt=np.zeros(R,int); sb=0; i_sb=names.index('sbma')
for k in range(R):
    hits=[set(rng.choice(len(names),size=n_by[s],p=w)) for s in studies]
    from collections import Counter
    c=Counter(x for h in hits for x in h)
    cnt[k]=sum(1 for v in c.values() if v>=2)
    if c.get(i_sb,0)>=2: sb+=1
# POST-LOCK SENSITIVITY (deviation, disclosed): Blanco is S. maltophilia D457, not E. coli; exclude it
studies2=[s for s in studies if s!='blanco2020']
cnt2=np.zeros(R,int); sb2=0
rng2=np.random.default_rng(20261007)
S1b=sum(1 for g,s in obs_genes.items() if len({x for x in s if x!='blanco2020'})>=2)
for k in range(R):
    hits=[set(rng2.choice(len(names),size=n_by[s],p=w)) for s in studies2]
    c=Counter(x for h in hits for x in h)
    cnt2[k]=sum(1 for v in c.values() if v>=2)
    if c.get(i_sb,0)>=2: sb2+=1
sens={'n_events_by_study':{s:n_by[s] for s in studies2},'observed_S1':S1b,'null_S1_mean':float(cnt2.mean()),'p_S1':float((cnt2>=S1b).mean()),'p_sbmA_specific_descriptive':sb2/R}
out={'lock_commit':LOCK,'n_events_by_study':n_by,'unmapped_records':{f'{a}|{b}':v for (a,b),v in unmapped.items()},
 'observed_S1':S1,'observed_genes_ge2_studies':sorted(g for g,s in obs_genes.items() if len(s)>=2),
 'null_S1_mean':float(cnt.mean()),'null_S1_quantiles':{str(q):float(np.quantile(cnt,q)) for q in (.5,.95,.99)},
 'p_S1':float((cnt>=S1).mean()),'p_sbmA_specific_descriptive':sb/R,'sbmA_len':uni['sbma'],'universe_n':len(uni),'reps':R,'post_lock_sensitivity_ecoli_only':sens}
json.dump(out,open(BASE/'results/opportunity_null_a7b.json','w'),indent=1)
print(json.dumps(out,indent=1))
