import sys,csv,json,re
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).parent))
import event_tier_robustness_a6 as a6
BASE=Path(__file__).resolve().parents[1]; LOCK='d60c91633498123605e05ecab3230559475e1440'; G=4631469
feat=list(csv.DictReader(open(BASE/'data/raw/ecoli_bw25113_CP009273.1_features.tsv'),delimiter='\t'))
IS=[(int(r['start']),int(r['end']),r['product_or_note']) for r in feat if r['type']=='mobile_element']
TP=[(int(r['start']),int(r['end']),r['product_or_note']) for r in feat if r['type']=='CDS' and re.search(r'(?i)transposase|IS[0-9]|insertion sequence',r['product_or_note'])]
def dist(p,iv):
    return min((0 if s<=p<=e else min(abs(p-s),abs(p-e)),n) for s,e,n in iv)
blocks=a6.spohn_blocks(); bps={}
for (ln,st),v in sorted(blocks.items()):
    s=int(str(st).replace(',','')); l=int(str(ln).replace(',',''))
    for p,kind in ((s,'start'),(s+l-1,'end')): bps.setdefault(p,[]).append(f'{kind} of {l}bp@{s}')
pts=sorted(bps); table=[]
for p in pts:
    d,n=dist(p,IS); d2,n2=dist(p,TP)
    table.append({'pos':p,'blocks':bps[p],'nearest_IS':n,'dist_IS':d,'nearest_transposase_CDS':n2,'dist_transposase':d2})
isarr=np.array([(s,e) for s,e,_ in IS]); 
def near(pos,W):  # vectorised distance to nearest IS interval
    pos=np.asarray(pos)[:,None]; s=isarr[:,0][None]; e=isarr[:,1][None]
    d=np.where((pos>=s)&(pos<=e),0,np.minimum(abs(pos-s),abs(pos-e))); return d.min(1)<=W
rng=np.random.default_rng(20261008); R=100000; n=len(pts); res={}
for W in (200,50,500,1000):
    obs=int(near(pts,W).sum()); null=np.array([near(rng.integers(1,G+1,n),W).sum() for _ in range(R)]) if W==200 else None
    if W!=200:
        null=np.array([near(rng.integers(1,G+1,n),W).sum() for _ in range(20000)])
    res[str(W)]={'observed':obs,'null_mean':float(null.mean()),'p_ge':float((null>=obs).mean()),'reps':len(null)}
cov=int(sum(e-s+1 for s,e,_ in IS))
out={'lock_commit':LOCK,'n_distinct_breakpoints':n,'n_IS_features':len(IS),'IS_bp_covered':cov,'primary_W200':res['200'],'sensitivity':{k:v for k,v in res.items() if k!='200'},'table':table}
json.dump(out,open(BASE/'results/is_breakpoint_a8.json','w'),indent=1); print(json.dumps(out,indent=1))
