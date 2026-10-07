import sys,json,csv
from pathlib import Path
from collections import defaultdict
import numpy as np
sys.path.insert(0,str(Path(__file__).parent))
import event_tier_robustness_a6 as a6
B=Path(__file__).resolve().parents[1]; LOCK='57e242cda46d17d75bb5e4336905181e7375860b'
S=set(json.load(open(B/'results/line_dependence_a10_corrected_universe28.json'))['S_sbmA_deletion_lines'])
led=json.load(open(B/'results/mutation_convergence_a5.json'))
evo=[r for r in led['records'] if r.get('scope','evolved')=='evolved' and r['study']=='spohn2019']
cds={}
for r in csv.DictReader(open(B/'data/raw/ecoli_k12_U00096.3_cds_table.tsv'),delimiter='\t'): cds[r['gene'].lower()]=int(r['length_bp'])
genes=list(cds); w=np.array([cds[g] for g in genes],float); w/=w.sum()
ev=defaultdict(set); unm=set(); amp={}
for r in evo:
    if r['line'] in S or r['mutation_type']=='intergenic mutation' or a6.tier(r['mutation_type'])!='A': continue
    amp[r['line']]=r['amp']; g=r['gene'].lower()
    if g in cds: ev[r['line']].add(g)
    else: unm.add((r['line'],r['gene']))
def T(ev):
    c=defaultdict(set)
    for l,gs in ev.items():
        for g in gs: c[(amp[l],g)].add(l)
    return sum(1 for v in c.values() if len(v)>=3),{f"{k[0]}:{k[1]}":len(v) for k,v in c.items() if len(v)>=3}
obs,contrib=T(ev)
rng=np.random.default_rng(20261012); R=100000; n={l:len(g) for l,g in ev.items()}
cum=np.cumsum(w); cum[-1]=1.0
def draw(k):
    s=set()
    while len(s)<k: s.add(genes[int(np.searchsorted(cum,rng.random()))])
    return s
cnt=0; nulls=[]
for _ in range(R):
    sim={l:draw(k) for l,k in n.items()}
    t=T(sim)[0]; nulls.append(t); cnt+= t>=obs
out={'lock_commit':LOCK,'non_S_lines':len(n),'events_mapped':sum(n.values()),'unmapped_gene_events':sorted(map(list,unm)),'T_obs':obs,'contributing_pairs_lines':contrib,'null_mean':float(np.mean(nulls)),'p':cnt/R,'lines_per_amp':{a:sum(1 for l in n if amp[l]==a) for a in set(amp.values())}}
json.dump(out,open(B/'results/sbma_independent_a12.json','w'),indent=1); print(json.dumps(out,indent=1))
