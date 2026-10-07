import json
from pathlib import Path
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parents[1]
d=json.load(open(B/'results/line_dependence_a10_corrected_universe28.json'))
led=json.load(open(B/'results/mutation_convergence_a5.json'))['records']
lines=sorted({r['line'] for r in led if r['study']=='spohn2019' and r.get('scope','evolved')=='evolved'},key=lambda l:(l.rsplit('_',1)[0],int(l.rsplit('_',1)[1])))
S,W,Bs=set(d['S_sbmA_deletion_lines']),set(d['W_waaY_lines']),set(d['B_basS_lines'])
fig,ax=plt.subplots(figsize=(6.4,3.0))
for i,l in enumerate(lines):
    for j,(s,c) in enumerate([(S,'#444444'),(W,'#1f77b4'),(Bs,'#d95f02')]):
        ax.add_patch(plt.Rectangle((i,j),0.9,0.9,color=c if l in s else '#eeeeee'))
ax.set_xlim(0,len(lines)); ax.set_ylim(0,3); ax.set_yticks([0.45,1.45,2.45]); ax.set_yticklabels(['sbmA deletion (S)','waaY Tier A (W)','basS Tier A (B)'],fontsize=7)
ax.set_xticks([i+0.45 for i in range(len(lines))]); ax.set_xticklabels(lines,rotation=90,fontsize=5.5)
for s in ('top','right'): ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(B/'paper/fig_line_grid.pdf'); print(len(lines))
