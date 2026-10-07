import sys,json,csv
from pathlib import Path
from collections import defaultdict,Counter
import numpy as np
sys.path.insert(0,str(Path(__file__).parent))
import event_tier_robustness_a6 as a6
B=Path(__file__).resolve().parents[1]; LOCK='16f815612b2223d586dfae887b02d9b3090772b7'
S=set(json.load(open(B/'results/line_dependence_a10_corrected_universe28.json'))['S_sbmA_deletion_lines'])
led=json.load(open(B/'results/mutation_convergence_a5.json'))
evo=[r for r in led['records'] if r.get('scope','evolved')=='evolved' and r['study']=='spohn2019']
rows=list(csv.DictReader(open(B/'data/raw/ecoli_k12_U00096.3_cds_table.tsv'),delimiter='\t'))
cds={r['gene'].lower():i for i,r in enumerate(rows)}
# neighborhoods: runs of consecutive CDS (table order), same strand, gap<=1000
nb=[];cur=0
for i,r in enumerate(rows):
    if i>0:
        p=rows[i-1]
        if not(r['strand']==p['strand'] and int(r['start'])-int(p['end'])<=1000): cur+=1
    nb.append(cur)
ev=defaultdict(set);amp={}
for r in evo:
    if r['line'] in S or r['mutation_type']=='intergenic mutation' or a6.tier(r['mutation_type'])!='A': continue
    amp[r['line']]=r['amp']; g=r['gene'].lower()
    if g in cds: ev[r['line']].add(g)
lines=sorted(ev)
def Tstat(sets):
    c=defaultdict(set)
    for l,gs in sets.items():
        for g in gs: c[(amp[l],g)].add(l)
    return sum(1 for v in c.values() if len(v)>=3)
def curveball(sets,seed,R=100000,burn=5000,thin=50):
    rng=np.random.default_rng(seed)
    cur={l:set(sets[l]) for l in lines}
    def trade():
        a,b=rng.choice(len(lines),2,replace=False); A=cur[lines[a]];Bs=cur[lines[b]]
        ao=list(A-Bs);bo=list(Bs-A)
        if not ao or not bo: return
        u=ao+bo; rng.shuffle(u); k=len(ao)
        sa=set(u[:k]);sb=set(u[k:]); cur[lines[a]]=(A&Bs)|sa; cur[lines[b]]=(A&Bs)|sb
    for _ in range(burn): trade()
    out=[]
    for _ in range(R):
        for _ in range(thin): trade()
        out.append(Tstat(cur))
    return np.array(out)
def summarize(name,obs,nulls):
    h=Counter(nulls.tolist())
    return {'T_obs':obs,'null_mean':float(nulls.mean()),'p95':float(np.percentile(nulls,95)),'p99':float(np.percentile(nulls,99)),'p_perm':(1+int((nulls>=obs).sum()))/(1+len(nulls)),'hist':{int(k):v for k,v in sorted(h.items())}}
obsA=Tstat(ev); assert obsA==4,obsA
evB={l:{nb[cds[g]] for g in gs} for l,gs in ev.items()}
obsB=Tstat(evB)
out={'lock_commit':LOCK,'lines':len(lines),'events':sum(len(v) for v in ev.values()),
 'A':summarize('A',obsA,curveball(ev,20261016)),
 'B':summarize('B',obsB,curveball(evB,20261016))}
json.dump(out,open(B/'results/conditional_permutation_a16.json','w'),indent=1); print(json.dumps(out,indent=1))
