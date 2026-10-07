import sys,json,re
sys.path.insert(0,'scripts')
from pathlib import Path
import candidate_concordance_a9 as a9
BASE=Path('.')
a=a9.seq('P30844')
t=Path('data/raw/ebi_proteins_P36557.txt').read_text()
b=''.join(re.sub(r'[^A-Z]','',l) for l in t.split('\nSQ ')[1].split('\n')[1:] if l.startswith(' '))
ident,alen=a9.nw(a,b); L=max(len(a),len(b))
r={'len_ecoli_P30844':len(a),'len_salm_P36557':len(b),'identical':int(ident),'identity_over_longer':round(ident/L,4),'length_ratio':round(min(len(a),len(b))/L,3)}
r['verdict']='CONFIRMED' if r['identity_over_longer']>=0.70 and r['length_ratio']>=0.9 else 'UNCONFIRMED'
json.dump(r,open('results/pmrb_mapping_a11.json','w'),indent=1); print(r)
