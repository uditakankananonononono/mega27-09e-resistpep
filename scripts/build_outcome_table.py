"""Build normalized per-lineage outcome table per addendum A1.3.
No scoring. Records raw values, censor flags, and provenance per row."""
import json, re, openpyxl
from pathlib import Path
import importlib.util
spec=importlib.util.spec_from_file_location('audit','scripts/audit_resistance_support.py')
audit=importlib.util.module_from_spec(spec); spec.loader.exec_module(audit)
BASE=Path(__file__).resolve().parents[1]
rows=[]

def add(study, organism, treatment, line_id, role, assay_agent, raw, log2fc=None, fc=None, censor='none', note=''):
    rows.append({'study':study,'organism':organism,'treatment':treatment,'line_id':line_id,
        'role':role,'assay_agent':assay_agent,'raw_value':raw,'fold_change':fc,
        'log2_fold_change':log2fc,'censor':censor,'note':note})

# --- Antunes 2024: evolved + matched control, linear fold-change vs ancestor
wb=openpyxl.load_workbook(BASE/'data/raw/zenodo11209304_underlying_figures.xlsx',data_only=True)
ws=wb['Fig. 1 + 3']
import math
for name,fc in ws.iter_rows(min_row=2, values_only=True):
    if not name or fc is None: continue
    name=str(name); fc=float(fc)
    ctrl=name.startswith('Control ')
    treat=re.sub(r'\s*\d+\.\d+\s*$','',name).replace('Control ','').strip()
    if treat in ('p-FdK5','p-FdK5 20/80','FK20'):  # mixtures excluded from sequence task
        continue
    add('antunes2024','P. aeruginosa PA14',treat,name,'control' if ctrl else 'evolved',treat,
        str(fc),log2fc=math.log2(fc),fc=fc,
        note='linear fold-change vs ancestor, Fig1+3 sheet')

# --- Maron 2025: evolved lines only in pinned file; values already log2 vs ancestor
wb=openpyxl.load_workbook(BASE/'data/raw/zenodo15125182_resistance.xlsx',data_only=True)
ws=wb['resistance']
hdr=[c.value for c in ws[1]][1:]
map25={'Temp':'temporin','Mel':'melittin','Pex':'pexiganan'}
for r in ws.iter_rows(min_row=2, values_only=True):
    agent=r[0]
    if agent not in map25: continue
    for col,val in zip(hdr,r[1:]):
        if val is None: continue
        tkey=re.sub(r'\d+$','',str(col))
        if tkey not in map25: continue  # combination lines excluded
        own = (tkey == agent)
        add('maron2025','S. aureus JLA513',map25[tkey],str(col),
            'evolved' if own else 'cross_assay',map25[agent],
            str(val),log2fc=float(val),fc=2**float(val),
            note=('log2 fold-change vs ancestor, own-treatment assay' if own
                  else 'cross-resistance assay (secondary, excluded from primary aggregate)')
                   + '; NPSA matched control from maron2022 supplement Table S2')

# --- Maron NPSA matched controls (maron2022 PMC9430149 supplement Table S2):
# no-peptide-selected control strains, MIC unchanged vs ancestor in both experiments
# (Temporin 6.25/6.25, Melittin 6.25/6.25, Pexiganan 12.5/12.5 ug/ml) => log2fc = 0
for tkey,tname in map25.items():
    for exp in ('exp1','exp2'):
        add('maron2025','S. aureus JLA513',tname,f'NPSA-{exp}','control',tname,
            'unchanged',log2fc=0.0,fc=1.0,
            note='NPSA control MIC = ancestor MIC, maron2022 supplement Table S2 (same evolution experiment)')

# --- Prabhu 2013: lineage MICs after cycling (raw strings, censored) vs Table S1 WT
tables=audit.tables(BASE/'data/raw/pmc3720879.xml')
wt_mic={'LL-37':'12.5-50','CNY100HL':'5'}  # Table S1, refined LB, mg/L; LL-37 is itself a range
for r in tables['Table 2']['rows']:
    if len(r)<5: continue
    m=re.match(r'^(LL-37|CNY100HL|WGH)\s+(\d+)',r[0])
    if not m or m.group(1)=='WGH': continue
    pep=m.group(1)
    meas=audit.measurement(r[4])
    censor=meas['kind'] if meas['kind'] in ('right_censored','left_censored') else ('range' if meas['kind']=='range' else ('missing' if meas['kind'] in ('missing','unparsed') else 'none'))
    fc=None
    if meas['lower'] is not None and wt_mic[pep]!='12.5-50':
        fc=meas['lower']/float(wt_mic[pep])
    add('prabhu2013','S. typhimurium LT2',pep,r[0],'evolved',pep,r[4],
        log2fc=(math.log2(fc) if fc else None),fc=fc,censor=censor,
        note='MIC after cycling / Table S1 WT (refined LB); LL-37 WT is a 12.5-50 range so fc withheld; media-unit contradiction with Table 4 header flagged in audit')
    if censor=='missing': rows[-1]['fold_change']=None

# aggregate per treatment
agg={}
for row in rows:
    if row['role']!='evolved' or row['log2_fold_change'] is None: continue
    k=(row['study'],row['treatment'])
    agg.setdefault(k,[]).append(row['log2_fold_change'])
def med(v):
    v=sorted(v); n=len(v); return (v[n//2] if n%2 else (v[n//2-1]+v[n//2])/2)
treatments=[]
for (study,treat),vals in sorted(agg.items()):
    ctrl=[r['log2_fold_change'] for r in rows if r['study']==study and r['treatment']==treat and r['role']=='control' and r['log2_fold_change'] is not None]
    treatments.append({'study':study,'treatment':treat,'n_evolved':len(vals),
        'median_evolved_log2fc':round(med(vals),4),
        'n_control':len(ctrl),'median_control_log2fc':round(med(ctrl),4) if ctrl else None,
        'net_log2fc':round(med(vals)-(med(ctrl) if ctrl else 0.0),4) if ctrl else None,
        'control_status':'matched' if ctrl else 'control_absent_in_pinned_file'})
out={'addendum':'A1.3','lineage_rows':rows,'treatment_aggregates':treatments,
     'excluded':['WGH (mixture)','p-FdK5, p-FdK5 20/80, FK20 (random mixtures)','combination lines in maron2025'],
     'limitations':['prabhu2013 LL-37 WT MIC is a range (12.5-50); fold-change withheld pending prereg choice of bound',
                    'maron2022 ovispirin/aurein1.2/pardaxin evolved-line MICs are figure-only (no pinned numeric source); excluded from outcome table',
                    'maron2025 NPSA control log2fc taken as exactly 0 from supplement Table S2 (MIC identical to ancestor, both experiments)']}
dest=BASE/'results/outcome_table_a1.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'rows':len(rows),'treatments':len(treatments),'with_net':sum(t['net_log2fc'] is not None for t in treatments)}))
