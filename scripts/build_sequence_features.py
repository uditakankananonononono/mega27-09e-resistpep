"""Build sequence-only physicochemical/compositional descriptors per addendum A1.4.
No outcomes, no labels, no scoring. Features from plain sequence only.
Lipidation indicator kept separate (runs with/without, both reported)."""
import json, math
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]

KD={'A':1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C':2.5,'Q':-3.5,'E':-3.5,'G':-0.4,
    'H':-3.2,'I':4.5,'L':3.8,'K':-3.9,'M':1.9,'F':2.8,'P':-1.6,'S':-0.8,
    'T':-0.7,'W':-0.9,'Y':-1.3,'V':4.2}
EIS={'A':0.620,'R':-2.530,'N':-0.780,'D':-0.900,'C':0.290,'Q':-0.850,'E':-0.740,
     'G':0.480,'H':-0.400,'I':1.380,'L':1.060,'K':-1.500,'M':0.640,'F':1.190,
     'P':0.120,'S':-0.180,'T':-0.050,'W':0.810,'Y':0.260,'V':1.080}
HPHOB=set('AILMFWV'); AROM=set('FWY'); POS=set('KR'); NEG=set('DE'); TINY=set('AGS')

def hmoment(seq,angle_deg=100.0):
    a=math.radians(angle_deg)
    sx=sum(EIS[r]*math.cos(a*i) for i,r in enumerate(seq))
    sy=sum(EIS[r]*math.sin(a*i) for i,r in enumerate(seq))
    return math.hypot(sx,sy)/len(seq)

def descriptors(seq):
    n=len(seq)
    net=sum(1 for r in seq if r in POS)-sum(1 for r in seq if r in NEG)
    return {'length':n,'net_charge':net,'charge_density':net/n,
            'pos_frac':sum(1 for r in seq if r in POS)/n,
            'neg_frac':sum(1 for r in seq if r in NEG)/n,
            'mean_kyte_doolittle':sum(KD[r] for r in seq)/n,
            'hydrophobic_frac':sum(1 for r in seq if r in HPHOB)/n,
            'aromatic_frac':sum(1 for r in seq if r in AROM)/n,
            'tiny_frac':sum(1 for r in seq if r in TINY)/n,
            'hydrophobic_moment_100':round(hmoment(seq),6)}

seqdata=json.loads((BASE/'data/derived/treatment_sequences.json').read_text())['sequences']
out=json.loads((BASE/'results/outcome_table_a1.json').read_text())
units=[]
for t in out['treatment_aggregates']:
    if t['net_log2fc'] is None:
        continue  # scored units only (A1.4: 9 units with matched-control net)
    name=t['treatment']
    canon={'temporin':'Temporin A','melittin':'Melittin','pexiganan':'Pexiganan'}.get(name,name)
    rec=next(s for s in seqdata if s['name']==canon)
    u={'study':t['study'],'treatment':name,'sequence_id':canon,
       'sequence':rec['sequence'],'lipidated':bool(rec['modification']),
       'net_log2fc':t['net_log2fc'],'features':descriptors(rec['sequence'])}
    units.append(u)
res={'addendum':'A1.4 feature build (no scoring)','n_units':len(units),
     'distinct_sequences':sorted({u['sequence_id'] for u in units}),
     'feature_names':list(units[0]['features'].keys()),'units':units,
     'notes':['sequence identity is the leakage barrier: melittin and pexiganan each appear as 2 units across studies',
              'lipidated indicator separate; model runs with and without it, both reported']}
(BASE/'results/sequence_features_a1.json').write_text(json.dumps(res,indent=2)+'\n')
for u in units:
    print(u['study'],u['sequence_id'],u['net_log2fc'],{k:round(v,3) for k,v in u['features'].items()})
