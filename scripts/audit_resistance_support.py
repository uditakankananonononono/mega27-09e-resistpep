"""Source-preserving support audit. Does not score or replace locked outputs."""
import hashlib,json,re,xml.etree.ElementTree as ET
from pathlib import Path

def local(e):return e.tag.split('}')[-1]
def text(e):return ' '.join(''.join(e.itertext()).split())
def measurement(raw):
    s=raw.strip().replace('\u2013','-').replace('\u2212','-')
    if s.upper() in {'ND','NA','N/A',''}:return {'raw':raw,'kind':'missing','lower':None,'upper':None}
    vals=[float(v) for v in re.findall(r'\d+(?:\.\d+)?',s)]
    if not vals:return {'raw':raw,'kind':'unparsed','lower':None,'upper':None}
    if '>' in s:return {'raw':raw,'kind':'right_censored','lower':min(vals),'upper':None}
    if '<' in s:return {'raw':raw,'kind':'left_censored','lower':None,'upper':max(vals)}
    return {'raw':raw,'kind':'range' if len(vals)>1 else 'exact','lower':min(vals),'upper':max(vals)}

def tables(path):
    root=ET.parse(path).getroot(); out={}
    for t in root.iter():
        if local(t)!='table-wrap':continue
        label=next((text(e) for e in t if local(e)=='label'),'unlabelled')
        rows=[]
        for row in t.iter():
            if local(row)=='tr':rows.append([text(c) for c in row if local(c) in {'td','th'}])
        out[label]={'rows':rows,'verbatim':text(t)}
    return out

def run(base):
    files={p.stem: {'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'tables':tables(p)} for p in (base/'data/raw').glob('pmc*.xml')}
    source=files['pmc3720879']['tables']; observations=[]
    for label in ['Table 2','Table 4']:
        for r in source[label]['rows']:
            if label=='Table 2' and len(r)>=5 and any(r[0].startswith(x) for x in ['LL-37 ','WGH ','CNY100HL ']):
                observations.append({'table':label,'unit_id':r[0],'endpoint':'evolved_population_MIC','mic':measurement(r[4]),'original_row':r})
            if label=='Table 4' and len(r)>=4 and r[0].startswith('DA'):
                for peptide,val in zip(['WGH','LL-37','CNY100HL'],r[1:4]):
                    observations.append({'table':label,'unit_id':r[0],'assay_agent':peptide,'endpoint':'clone_cross_resistance_MIC','mic':measurement(val),'original_row':r})
    return {'audit_type':'outcome-label support, not model evaluation','sources':files,'observations':observations,
      'limits':['WGH is a mixture, not one sequence-level label.','Clone cross-resistance measurements are not independent peptide resistance-emergence labels.','2013 study includes only two named single sequences and one mixture; lineage count cannot expand peptide sample size.','2020 table reports pharmacodynamics across selected bacterial lines tested with pexiganan, not one resistance endpoint per selecting AMP.','Table 4 header says mg/mL while surrounding methods use mg/L: retain raw unit and flag contradiction; do not silently normalize.','No AUROC, split, candidate ranking or named discovery is licensed by this audit.']}
if __name__=='__main__':
    base=Path(__file__).resolve().parents[1]; result=run(base)
    dest=base/'results/resistance_support_audit.json'; dest.parent.mkdir(exist_ok=True); dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'path':str(dest),'observations':len(result['observations']),'measurement_kinds':{k:sum(o['mic']['kind']==k for o in result['observations']) for k in sorted({o['mic']['kind'] for o in result['observations']})}}))
