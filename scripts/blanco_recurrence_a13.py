import json,re
from pathlib import Path
from collections import defaultdict
import numpy as np
B=Path(__file__).resolve().parents[1]; LOCK='36fe1c224923b90fa04bcdf0220a92969bf55d98+A13b f27e8cfce2abc3ae8f9be2eae37012ec9a27b97d'
# parse feature table: gene features give gene name + old_locus_tag; CDS features give length
lines=(B/'data/raw/smaltophilia_D457_NC_017671.1_features.ft').read_text().split('\n')
feats=[];cur=None
for l in lines:
    if l and not l.startswith('\t') and not l.startswith('>'):
        p=l.split('\t'); cur={'s':int(re.sub(r'\D','',p[0])),'e':int(re.sub(r'\D','',p[1])),'type':p[2] if len(p)>2 else '','q':{}}; feats.append(cur)
    elif l.startswith('\t\t\t') and cur is not None:
        k,_,v=l.strip().partition('\t'); cur['q'].setdefault(k,v)
genes={}  # key -> length
allcds=[]
for i,f in enumerate(feats):
    if f['type']=='CDS':
        L=abs(f['e']-f['s'])+1; q=f['q']
        # name from preceding gene feature
        g=feats[i-1] if i>0 and feats[i-1]['type']=='gene' else {'q':{}}
        names=set(x.lower() for x in (g['q'].get('gene'),g['q'].get('old_locus_tag'),g['q'].get('locus_tag'),q.get('gene'),q.get('old_locus_tag')) if x)
        idx=len(allcds); allcds.append(L)
        if q.get('product')=='ClpXP protease specificity-enhancing factor': names.add('sspb')
        if g['q'].get('gene')=='rsmH': names.add('mraw')
        for n in names: genes.setdefault(n,idx)
w=np.array(allcds,float); w/=w.sum(); cum=np.cumsum(w); cum[-1]=1
led=json.load(open(B/'results/mutation_convergence_a5.json'))['records']
ev=defaultdict(set); amp={}; unm=[]
for r in led:
    if r['study']!='blanco2020' or r.get('scope')!='evolved': continue
    amp[r['line']]=r['amp']; k=genes.get(r['gene'].lower())
    if k is None: unm.append([r['line'],r['gene']])
    else: ev[r['line']].add(k)
def T(ev):
    c=defaultdict(set)
    for l,gs in ev.items():
        for g in gs: c[(amp[l],g)].add(l)
    return sum(1 for v in c.values() if len(v)>=3),{f"{k[0]}:{k[1]}":len(v) for k,v in c.items() if len(v)>=3}
obs,contrib=T(ev); n={l:len(g) for l,g in ev.items()}
rng=np.random.default_rng(20261014); R=100000; cnt=0; nulls=[]
def draw(k):
    s=set()
    while len(s)<k: s.add(int(np.searchsorted(cum,rng.random())))
    return s
for _ in range(R):
    t=T({l:draw(k) for l,k in n.items()})[0]; nulls.append(t); cnt+=t>=obs
name={v:k for k,v in genes.items()}
out={'lock_commit':LOCK,'n_cds':len(allcds),'lines':len(n),'events_mapped':sum(n.values()),'unmapped':unm,'T_obs':obs,'contrib':contrib,'null_mean':float(np.mean(nulls)),'p':cnt/R}
json.dump(out,open(B/'results/blanco_recurrence_a13b_amended.json','w'),indent=1); print(json.dumps(out))
