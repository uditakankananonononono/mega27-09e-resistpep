"""A1.3-locked descriptive secondary analyses. No scoring, no gates, no model.
(a) mixture-vs-single-sequence contrast (antunes2024 RPMs vs single AMPs)
(b) cross-resistance asymmetry (maron2025 off-diagonal vs own-treatment)"""
import json, math, re
import openpyxl
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
def med(v):
    v=sorted(v); n=len(v); return v[n//2] if n%2 else (v[n//2-1]+v[n//2])/2

# (a) antunes2024 mixtures (kept out of sequence task; descriptive only)
wb=openpyxl.load_workbook(BASE/'data/raw/zenodo11209304_underlying_figures.xlsx',data_only=True)
ws=wb['Fig. 1 + 3']
evo={}; ctrl={}
for name,fc in ws.iter_rows(min_row=2, values_only=True):
    if not name or fc is None: continue
    name=str(name); fc=float(fc)
    t=re.sub(r'\s*\d+\.\d+\s*$','',name).replace('Control ','').strip()
    (ctrl if name.startswith('Control ') else evo).setdefault(t,[]).append(math.log2(fc))
mix={}
for t in ('p-FdK5','p-FdK5 20/80','FK20'):
    if t in evo:
        c=ctrl.get(t,[0.0])
        mix[t]={'n_evolved':len(evo[t]),'median_evolved_log2fc':round(med(evo[t]),4),
                'median_control_log2fc':round(med(c),4),'net_log2fc':round(med(evo[t])-med(c),4)}
out=json.loads((BASE/'results/outcome_table_a1.json').read_text())
single={t['treatment']:t['net_log2fc'] for t in out['treatment_aggregates']
        if t['study']=='antunes2024' and t['net_log2fc'] is not None}
# (b) maron2025 cross-resistance asymmetry from cross_assay rows
cross={}
for r in out['lineage_rows']:
    if r['study']=='maron2025' and r['role']=='cross_assay' and r['log2_fold_change'] is not None:
        cross.setdefault((r['treatment'],r['assay_agent']),[]).append(r['log2_fold_change'])
asym=[{'evolved_under':a,'assayed_on':b,'median_cross_log2fc':round(med(v),4)}
      for (a,b),v in sorted(cross.items())]
own={t['treatment']:t['median_evolved_log2fc'] for t in out['treatment_aggregates'] if t['study']=='maron2025'}
res={'addendum':'A1.3 locked secondary, descriptive only (no scoring, no gates)',
     'mixture_vs_single_antunes2024':{'mixtures':mix,'single_sequences':single,
        'note':'random peptide mixtures vs single sequences; descriptive contrast only, mixtures have no sequence-level label'},
     'cross_resistance_maron2025':{'own_treatment_median_log2fc':own,'off_diagonal':asym,
        'note':'median log2fc of lines evolved under one AMP assayed on another; NPSA control fc=0 for all three drugs (2022 supp Table S2)'}}
(BASE/'results/descriptive_secondary_a1.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
