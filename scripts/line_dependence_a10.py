import sys,json
from pathlib import Path
from collections import defaultdict
import numpy as np
from math import comb
sys.path.insert(0,str(Path(__file__).parent))
import event_tier_robustness_a6 as a6
BASE=Path(__file__).resolve().parents[1]; LOCK='7d0699e67224f60e38d8052f12500c4055277f60'
led=json.load(open(BASE/'results/mutation_convergence_a5.json'))
evo=[r for r in led['records'] if r.get('scope','evolved')=='evolved' and r['study']=='spohn2019']
lines=sorted({r['line'] for r in evo}); amp={r['line']:r['amp'] for r in evo}
blocks=a6.spohn_blocks()
S=set()
for (ln,st),b in blocks.items():
    if any(g.lower()=='sbma' for g in b['genes']): S|=set(b['lines'])
def tierA(g):
    return {r['line'] for r in evo if r['gene'].lower()==g and a6.tier(r['mutation_type'])=='A'}
W=tierA('waay'); B=tierA('bass')
# all 120 lines (some lines may have no records)
allines=sorted({r['line'] for r in evo if r['study']=='spohn2019'}|S|W|B)  # corrected: sequenced lines per Spohn Suppl. Data 5 (38 lines; 28 adopted-AMP)
L=len(allines)
def hyper(k,a,b,n=L):
    return sum(comb(a,i)*comb(n-a,b-i) for i in range(k,min(a,b)+1))/comb(n,b)
rng=np.random.default_rng(20261010); R=100000
amps=sorted({l.rsplit('_',1)[0] for l in allines}); by={a:[l for l in allines if l.rsplit('_',1)[0]==a] for a in amps}
def strat(X,Y):
    obs=len(X&Y); null=np.zeros(R,int)
    for k in range(R):
        c=0
        for a in amps:
            ls=by[a]; x=sum(l in X for l in ls); y=sum(l in Y for l in ls)
            if x and y:
                c+=len(set(rng.choice(len(ls),size=x,replace=False))&set(rng.choice(len(ls),size=y,replace=False)))
        null[k]=c
    return obs,float(null.mean()),float((null>=obs).mean())
out={'lock_commit':LOCK,'n_lines':L,'S_sbmA_deletion_lines':sorted(S),'W_waaY_lines':sorted(W),'B_basS_lines':sorted(B)}
for name,(X,Y) in {'W_and_S':(W,S),'B_and_S':(B,S),'W_and_B':(W,B)}.items():
    o,m,p=strat(X,Y)
    out[name]={'observed':o,'overlap_lines':sorted(X&Y),'hypergeometric_p':hyper(o,len(X),len(Y)),'amp_stratified_null_mean':m,'amp_stratified_p':p}
out['per_amp']={a:{'S':sum(l in S for l in by[a]),'W':sum(l in W for l in by[a]),'B':sum(l in B for l in by[a])} for a in amps if any(l in S|W|B for l in by[a])}
tw=defaultdict(list)
for r in evo:
    if r['gene'].lower()=='waay' and a6.tier(r['mutation_type'])=='A' and r['line'] in S: tw[r['line']].append(r['mutation_type'])
out['waaY_types_in_S_lines']=dict(tw)
json.dump(out,open(BASE/'results/line_dependence_a10.json','w'),indent=1); print(json.dumps(out,indent=1))
