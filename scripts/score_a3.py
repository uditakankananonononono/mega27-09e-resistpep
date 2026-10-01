"""A3.5 locked scoring on enlarged 21-unit base. Same pipeline/hyperparameters
as score_a1.py (locked A1.4): ridge alpha=1.0, train-fold standardization,
k-mer {2,3}, LOSO by sequence identity, Spearman, bootstrap seed 2002,
permutation 10000 seed 1001, feature-scramble seed 3003.
Subsets: full 21, spohn-only 12, matched-only 9. Indicator runs: lipid, disulfide."""
import json, math, itertools, random, importlib.util
import numpy as np
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('feat','scripts/build_sequence_features.py')
# reuse descriptor math without re-running its __main__ output section
import re
src=(BASE/'scripts/build_sequence_features.py').read_text()
head=src[:src.index('seqdata=')]
ns={'__file__':str(BASE/'scripts/build_sequence_features.py')}; exec(head,ns)
descriptors=ns['descriptors']
a1=json.loads((BASE/'results/sequence_features_a1.json').read_text())
sp=json.loads((BASE/'results/spohn_units_a3.json').read_text())
units=[]
for u in a1['units']:
    units.append({'study':u['study'],'sequence_id':u['sequence_id'],'sequence':u['sequence'],
                  'net':u['net_log2fc'],'lipid':u['lipidated'],'disulfide':False,'subset':'matched'})
for u in sp['units']:
    units.append({'study':'spohn2019','sequence_id':u['sequence_id'],'sequence':u['sequence'],
                  'net':u['net_log2fc'],'lipid':False,'disulfide':u['disulfide'],'subset':'spohn'})
def run(units,indicator=None,seed_boot=2002,seed_perm=1001,seed_scr=3003,n_boot=10000,n_perm=10000):
    y=np.array([u['net'] for u in units])
    groups=sorted({u['sequence_id'] for u in units})
    gid=[groups.index(u['sequence_id']) for u in units]
    F=list(units[0] and descriptors(units[0]['sequence']).keys())
    def kmer(seq,k):
        aa='ACDEFGHIKLMNPQRSTVWY'; idx={p:i for i,p in enumerate(itertools.product(aa,repeat=k))}
        v=np.zeros(len(idx))
        for i in range(len(seq)-k+1):
            key=tuple(seq[i:i+k])
            if key in idx: v[idx[key]]+=1
        return v/max(1,len(seq)-k+1)
    def Xmat(kind):
        if kind=='full': X=np.array([[d for d in descriptors(u['sequence']).values()] for u in units])
        elif kind=='two': X=np.array([[descriptors(u['sequence'])['net_charge'],descriptors(u['sequence'])['mean_kyte_doolittle']] for u in units])
        elif kind=='kmer': X=np.array([np.concatenate([kmer(u['sequence'],2),kmer(u['sequence'],3)]) for u in units])
        if indicator: X=np.column_stack([X,[1.0 if u.get(indicator) else 0.0 for u in units]])
        return X
    def rp(Xtr,ytr,Xte,alpha=1.0):
        mu=Xtr.mean(0); sd=Xtr.std(0); sd[sd==0]=1.0
        Xs=(Xtr-mu)/sd; yc=ytr-ytr.mean()
        if Xs.shape[1]>Xs.shape[0]:  # dual form, identical ridge solution
            w=np.linalg.solve(Xs@Xs.T+alpha*np.eye(Xs.shape[0]),yc)
            return ((Xte-mu)/sd)@(Xs.T@w)+ytr.mean()
        beta=np.linalg.solve(Xs.T@Xs+alpha*np.eye(Xs.shape[1]),Xs.T@yc)
        return ((Xte-mu)/sd)@beta+ytr.mean()
    def spear(a,b):
        def ranks(v):
            order=np.argsort(v,kind='stable'); sv=np.array(v)[order]; sr=np.arange(len(v))
            out=np.empty(len(v)); i=0
            while i<len(v):
                j=i
                while j+1<len(v) and sv[j+1]==sv[i]: j+=1
                out[order[i:j+1]]=sr[i:j+1].mean(); i=j+1
            return out
        ra,rb=ranks(a),ranks(b); ra=ra-ra.mean(); rb=rb-rb.mean()
        dn=math.sqrt((ra@ra)*(rb@rb)); return float(ra@rb/dn) if dn>0 else 0.0
    def loso(kind,yv):
        if kind=='median':
            p=np.empty(len(units))
            for g in range(len(groups)):
                te=[i for i in range(len(units)) if gid[i]==g]; tr=[i for i in range(len(units)) if gid[i]!=g]
                p[te]=float(np.median(yv[tr]))
            return p
        X=Xmat(kind); p=np.empty(len(units))
        for g in range(len(groups)):
            te=[i for i in range(len(units)) if gid[i]==g]; tr=[i for i in range(len(units)) if gid[i]!=g]
            p[te]=rp(X[tr],yv[tr],X[te])
        return p
    preds={k:loso(k,y) for k in ('full','median','two','kmer')}
    obs={k:spear(preds[k],y) for k in preds}
    rng=random.Random(seed_boot); boot=[]
    for _ in range(n_boot):
        idx=[rng.randrange(len(units)) for _ in range(len(units))]
        if len(set(gid[i] for i in idx))<3: continue
        boot.append(spear(preds['full'][idx],y[idx]))
    boot=sorted(boot); ci=(boot[int(0.025*len(boot))],boot[int(0.975*len(boot))])
    # precompute per-fold hat matrices for 'full' (X fixed; only y shuffles)
    Xf=Xmat('full'); folds=[]
    for g in range(len(groups)):
        te=np.array([i for i in range(len(units)) if gid[i]==g]); tr=np.array([i for i in range(len(units)) if gid[i]!=g])
        Xtr=Xf[tr]; mu=Xtr.mean(0); sd=Xtr.std(0); sd[sd==0]=1.0
        Xs=(Xtr-mu)/sd; B=np.linalg.inv(Xs.T@Xs+1.0*np.eye(Xs.shape[1]))
        H=((Xf[te]-mu)/sd)@B@Xs.T
        folds.append((te,tr,H))
    rng=random.Random(seed_perm); null=[]
    for _ in range(n_perm):
        yp=np.array(y)[rng.sample(range(len(units)),len(units))]
        pr=np.empty(len(units))
        for te,tr,H in folds:
            ytr=yp[tr]; pr[te]=H@(ytr-ytr.mean())+ytr.mean()
        null.append(spear(pr,yp))
    null=sorted(null); p_perm=sum(1 for v in null if v>=obs['full'])/len(null)
    rng=random.Random(seed_scr); X=Xmat('full'); perm=list(range(len(units))); rng.shuffle(perm); Xs=X[perm]
    p=np.empty(len(units))
    for g in range(len(groups)):
        te=[i for i in range(len(units)) if gid[i]==g]; tr=[i for i in range(len(units)) if gid[i]!=g]
        p[te]=rp(Xs[tr],y[tr],Xs[te])
    scr=spear(p,y)
    return {'n_units':len(units),'n_groups':len(groups),'loso_spearman':{k:round(v,4) for k,v in obs.items()},
            'boot_ci95':[round(ci[0],4),round(ci[1],4)],'perm_p_ge_model':p_perm,'feature_scramble':round(scr,4)}
res={'addendum':'A3.5 scoring','indicator_none':{},'subsets':{}}
allu=units
res['subsets']['full_21']=run(allu)
res['subsets']['full_21_lipid_disulfide_indicators']=run(allu,indicator=None)  # placeholder replaced below
res['subsets'].pop('full_21_lipid_disulfide_indicators')
res['indicator_runs']={'full_21_lipid':run(allu,indicator='lipid'),
                       'full_21_disulfide':run(allu,indicator='disulfide')}
res['subsets']['spohn_only_12']=run([u for u in units if u['subset']=='spohn'])
res['subsets']['matched_only_9']=run([u for u in units if u['subset']=='matched'])
res['beat_rule']='model LOSO Spearman > every baseline AND 95% CI excludes 0 (A1.4, unchanged)'
(BASE/'results/score_a3.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
