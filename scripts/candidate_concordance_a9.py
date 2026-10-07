import sys,csv,json,re
from pathlib import Path
from collections import defaultdict, Counter
import numpy as np
sys.path.insert(0,str(Path(__file__).parent))
from event_tier_robustness_a6 import tier
BASE=Path(__file__).resolve().parents[1]; LOCK='35256e19567241f303cc3ab615f6931490e38fbb'
def seq(a):
    t=(BASE/f'data/raw/ebi_proteins_{a}.txt').read_text()
    return re.search(r'"sequence":\{"version":\d+,"length":\d+,"mass":\d+,"modified":"[^"]+","sequence":"([A-Z]+)"',t).group(1)
def nw(a,b,m=1,x=-1,g=-2):
    n,k=len(a),len(b); S=np.zeros((n+1,k+1),int); T=np.zeros((n+1,k+1),int)
    S[:,0]=np.arange(n+1)*g; S[0,:]=np.arange(k+1)*g; T[1:,0]=1; T[0,1:]=2
    for i in range(1,n+1):
        for j in range(1,k+1):
            c=[S[i-1,j-1]+(m if a[i-1]==b[j-1] else x),S[i-1,j]+g,S[i,j-1]+g]; q=int(np.argmax(c)); S[i,j]=c[q]; T[i,j]=q
    i,j=n,k; ident=0; alen=0
    while i>0 or j>0:
        q=T[i,j]
        if i>0 and j>0 and q==0: ident+= a[i-1]==b[j-1]; i-=1;j-=1
        elif i>0 and (q==1 or j==0): i-=1
        else: j-=1
        alen+=1
    return ident,alen
pairs={'waaY':('P26472','P27240'),'phoP':('P0DM78','P23836')}
orth={}
for g,(s,e) in pairs.items():
    a,b=seq(s),seq(e); ident,alen=nw(a,b)
    cov=min(1.0,alen/max(len(a),len(b)))  # alignment spans; coverage of shorter and longer both ~ via global alignment
    orth[g]={'sal':s,'eco':e,'len_sal':len(a),'len_eco':len(b),'identities':int(ident),'identity_over_longer':ident/max(len(a),len(b)),'identity_over_alignment':ident/alen,'ortholog_by_rule':bool(ident/alen>=0.35)}
uni={}
for r in csv.DictReader(open(BASE/'data/raw/ecoli_k12_U00096.3_cds_table.tsv'),delimiter='\t'):
    if r['gene']: uni[r['gene'].lower()]=int(r['length_bp'])
led=json.load(open(BASE/'results/mutation_convergence_a5.json'))
evo=[r for r in led['records'] if r.get('scope','evolved')=='evolved' and r['study']=='spohn2019']
ev=set(); unm=0
hits=defaultdict(list)
for r in evo:
    if tier(r['mutation_type'])!='A': continue
    g=r['gene'].lower()
    if g not in uni: unm+=1; continue
    ev.add((r['line'],g,r['mutation_type']))
for l,g,t in sorted(ev): hits[g].append((l,t))
n=len(ev); names=list(uni); w=np.array([uni[x] for x in names],float); w/=w.sum()
prim=['waay','phop']; idx=[names.index(p) for p in prim]
obs=sum(1 for p in prim if hits.get(p))
rng=np.random.default_rng(20261009); R=100000
Tn=np.zeros(R,int)
for k in range(R):
    s=set(rng.choice(len(names),size=n,p=w)); Tn[k]=sum(1 for i in idx if i in s)
perg={p:float(1-(1-w[names.index(p)])**n) for p in prim+['bass']}
desc={g:{'n_events':len(hits.get(g,[])),'lines':sorted({l for l,_ in hits.get(g,[])}),'types':sorted({t for _,t in hits.get(g,[])})} for g in ['waay','phop','bass','pmrb','pmra','phoq','waap','waaz']}
out={'lock_commit':LOCK,'orthology_descriptive':orth,'n_spohn_tierA_mapped_events':n,'unmapped':unm,'observed_T':obs,'null_T_mean':float(Tn.mean()),'p_T_ge_obs':float((Tn>=obs).mean()),'per_gene_null_hit_prob':perg,'descriptive_spohn_hits':desc}
json.dump(out,open(BASE/'results/candidate_concordance_a9.json','w'),indent=1); print(json.dumps(out,indent=1))
