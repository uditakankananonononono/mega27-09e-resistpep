"""Locked scoring per addendum A1.4. Run only after feature table commit b819c72.
Fixed before outcome contact: ridge alpha=1.0 (all ridges), train-fold
standardization, k-mer k in {2,3} normalized counts, lipid indicator 0/1,
permutation null 10000 draws seed 1001, bootstrap 10000 draws seed 2002
(percentile 95% CI). Sequence identity is the leakage barrier (7 folds)."""
import json, math, itertools, random
import numpy as np
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
d=json.loads((BASE/'results/sequence_features_a1.json').read_text())
units=d['units']; F=d['feature_names']
y=np.array([u['net_log2fc'] for u in units])
groups=sorted({u['sequence_id'] for u in units})
gid=[groups.index(u['sequence_id']) for u in units]

def kmer_counts(seq,k):
    aa='ACDEFGHIKLMNPQRSTVWY'
    idx={p:i for i,p in enumerate(itertools.product(aa,repeat=k))}
    v=np.zeros(len(idx))
    for i in range(len(seq)-k+1):
        key=tuple(seq[i:i+k])
        if key in idx: v[idx[key]]+=1
    return v/max(1,len(seq)-k+1)

def Xmat(kind,lipid):
    if kind=='full':
        X=np.array([[u['features'][f] for f in F] for u in units])
    elif kind=='two':
        X=np.array([[u['features']['net_charge'],u['features']['mean_kyte_doolittle']] for u in units])
    elif kind=='kmer':
        X=np.array([np.concatenate([kmer_counts(u['sequence'],2),kmer_counts(u['sequence'],3)]) for u in units])
    if lipid:
        X=np.column_stack([X,[1.0 if u['lipidated'] else 0.0 for u in units]])
    return X

def ridge_fit_predict(Xtr,ytr,Xte,alpha=1.0):
    mu=Xtr.mean(0); sd=Xtr.std(0); sd[sd==0]=1.0
    Xs=(Xtr-mu)/sd; yc=ytr-ytr.mean()
    beta=np.linalg.solve(Xs.T@Xs+alpha*np.eye(Xs.shape[1]),Xs.T@yc)
    return ((Xte-mu)/sd)@beta+ytr.mean()

def spearman(a,b):
    def ranks(v):
        order=np.argsort(v,kind='stable'); r=np.empty(len(v)); r[order]=np.arange(len(v))
        # average ranks for ties
        out=np.empty(len(v),float); i=0
        sv=np.array(v)[order]; sr=np.arange(len(v))
        i=0
        while i<len(v):
            j=i
            while j+1<len(v) and sv[j+1]==sv[i]: j+=1
            out[order[i:j+1]]=sr[i:j+1].mean(); i=j+1
        return out
    ra,rb=ranks(a),ranks(b)
    ra=ra-ra.mean(); rb=rb-rb.mean()
    denom=math.sqrt((ra@ra)*(rb@rb))
    return float(ra@rb/denom) if denom>0 else 0.0

def loso_preds(kind,lipid,yv):
    if kind=='median':
        preds=np.empty(len(units))
        for g in range(len(groups)):
            te=[i for i in range(len(units)) if gid[i]==g]
            tr=[i for i in range(len(units)) if gid[i]!=g]
            m=float(np.median(yv[tr]))
            for i in te: preds[i]=m
        return preds
    X=Xmat(kind,lipid)
    preds=np.empty(len(units))
    for g in range(len(groups)):
        te=[i for i in range(len(units)) if gid[i]==g]
        tr=[i for i in range(len(units)) if gid[i]!=g]
        preds[te]=ridge_fit_predict(X[tr],yv[tr],X[te])
    return preds

def evaluate(yv,seed_perm=None):
    res={}
    for lipid in (False,True):
        for kind in ('full','median','two','kmer'):
            preds=loso_preds(kind,lipid,yv)
            res[f'{"model" if kind=="full" else "baseline_"+kind}{"_lipid" if lipid else ""}']=spearman(preds,yv)
    return res

observed=evaluate(y)
# bootstrap 95% CI for model (no-lipid and lipid) over 9 units
rng=random.Random(2002)
boots={'model':[],'model_lipid':[]}
for _ in range(10000):
    idx=[rng.randrange(len(units)) for _ in range(len(units))]
    if len(set(gid[i] for i in idx))<3: continue
    for lipid,key in ((False,'model'),(True,'model_lipid')):
        preds=loso_preds('full',lipid,y)[idx]
        boots[key].append(spearman(preds,y[idx]))
ci={k:(sorted(v)[int(0.025*len(v))],sorted(v)[int(0.975*len(v))]) for k,v in boots.items()}
# label-permutation null, 10000 draws seed 1001 (model, no lipid)
rng=random.Random(1001)
null=[]
for _ in range(10000):
    yp=list(y); rng.shuffle(yp)
    null.append(spearman(loso_preds('full',False,np.array(yp)),np.array(yp)))
null=sorted(null)
p_perm=sum(1 for v in null if v>=observed['model'])/len(null)
# feature-scramble control: permute feature rows against labels
rng=random.Random(3003)
X=Xmat('full',False); perm=list(range(len(units))); rng.shuffle(perm)
Xs=X[perm]
preds=np.empty(len(units))
for g in range(len(groups)):
    te=[i for i in range(len(units)) if gid[i]==g]; tr=[i for i in range(len(units)) if gid[i]!=g]
    preds[te]=ridge_fit_predict(Xs[tr],y[tr],Xs[te])
scramble=spearman(preds,y)
out={'addendum':'A1.4 scoring','n_units':len(units),'n_folds':len(groups),
     'loso_spearman':observed,
     'bootstrap_ci_95':{k:[round(a,4),round(b,4)] for k,(a,b) in ci.items()},
     'permutation_null':{'draws':10000,'seed':1001,'p_ge_observed':p_perm,
        'null_median':null[len(null)//2],'null_p95':null[int(0.95*len(null))]},
     'feature_scramble_spearman':scramble,
     'ancestor_control_check':'maron2025 NPSA controls net exactly 0 by measurement; antunes2024 passage-control medians (Cecropin 2.5, SLM1 1.0, SLM3 1.0, others 0.0) are the reason matched-control netting is the locked estimand',
     'beat_rule':'model LOSO Spearman > every baseline LOSO Spearman AND 95% bootstrap CI excludes 0'}
(BASE/'results/score_a1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
