"""A3 extraction: Spohn 2019 per-line MIC fold-changes from pinned supplement.
Runs only after A3 lock (ef2b29b). Ancestor-only contrast per A3.2."""
import json, math, zipfile, io
import openpyxl
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
INCLUDE={'BAC5':'Bactenecin 5','CAP18':'CAP18','CP1':'Cecropin P1','HBD3':'HBD-3',
 'IND':'Indolicidin','LL37':'LL-37','PEX':'Pexiganan','PGLA':'PGLa','PLEU':'Pleurocidin',
 'PR39':'PR-39','R8':'R8','TPII':'Tachyplesin II'}
SEQ={'BAC5':'RFRPPIRRPPIRPPFYPPFRPPIRPPIFPPIRPPFRPPLGPFP','CAP18':'GLRKRLRKFRNKIKEKLKKIGQKIQGFVPKLAPRTDY',
 'CP1':'SWLSKTAKKLENSAKKRISEGIAIAIQGGPR','HBD3':'GIINTLQKYYRVRGGRAVLSLPKEEQIGKSTRGRKRRKK',
 'IND':'ILPWKWPWWPWRR','LL37':'LLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES','PEX':'GIGKFLKKAKKFGKAFVKILKK',
 'PGLA':'GMASKAGAIAGKIAKVALKAL','PLEU':'GWGSFFKKAAHVGKHVGKAALTHYL',
 'PR39':'RRRPRPPYLPRPRPPPFFPPRLPPRIPPGFPPRFPPRFP','R8':'FLGKVFKLASKVFKAVFGKV','TPII':'RWCFRVCYRGICYRKCR'}
DISULFIDE={'TPII','HBD3'}
z=zipfile.ZipFile(BASE/'data/raw/spohn2019_supp.zip')
wb=openpyxl.load_workbook(io.BytesIO(z.read('41467_2019_12364_MOESM14_ESM.xlsx')),read_only=True)
ws=wb['Figure 1A']
lines={}
for r in ws.iter_rows(min_row=8,values_only=True):
    if not r or r[0] is None: continue
    dtype,drug,line,fc=r[0],r[1],r[2],r[3]
    if drug in INCLUDE and fc is not None:
        try: fc=float(fc)
        except (TypeError,ValueError): continue
        lines.setdefault(drug,[]).append((line,fc))
def med(v):
    v=sorted(v); n=len(v); return v[n//2] if n%2 else (v[n//2-1]+v[n//2])/2
units=[]
for abbr,vals in sorted(lines.items()):
    l2=[math.log2(fc) for _,fc in vals if fc>0]
    units.append({'study':'spohn2019','treatment':INCLUDE[abbr],'abbr':abbr,
        'sequence_id':INCLUDE[abbr],'sequence':SEQ[abbr],'disulfide':abbr in DISULFIDE,
        'n_lines':len(vals),'median_log2fc':round(med(l2),4),
        'control_log2fc':0.0,'control_status':'ancestor_only_A3.2','net_log2fc':round(med(l2),4)})
out={'addendum':'A3 extraction','organism':'E. coli K-12 BW25113',
     'excluded':{'PXB':'cyclic lipopeptide (A3.3)','PROA':'heterogeneous protamine preparation (A3.3)'},
     'units':units}
(BASE/'results/spohn_units_a3.json').write_text(json.dumps(out,indent=2)+'\n')
for u in units: print(u['abbr'],u['n_lines'],u['median_log2fc'])
print('total units:',len(units))
