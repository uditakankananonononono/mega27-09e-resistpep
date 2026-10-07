"""A4 descriptive interval extraction. No prediction or imputed censor values."""
import json, math, re, statistics, subprocess
from pathlib import Path
from lxml import etree
BASE = Path(__file__).resolve().parents[1]

def parse(value):
    match = re.fullmatch(r'(>)?([0-9]+(?:\.[0-9]+)?)', value.strip())
    if not match or float(match[2]) <= 0:
        raise ValueError(f'Unsupported MIC: {value!r}')
    x = float(match[2])
    return {'lower': x, 'upper': None if match[1] else x,
            'lower_open': bool(match[1]), 'upper_open': bool(match[1])}

def transform(x, reference):
    if reference <= 0: raise ValueError('Nonpositive reference')
    return {**x, 'lower': math.log2(x['lower']/reference),
            'upper': None if x['upper'] is None else math.log2(x['upper']/reference)}

def median_interval(values):
    if not values: raise ValueError('Empty sample')
    n = len(values)
    indices = [(n-1)//2, n//2]
    lower = sorted(values, key=lambda x:(x['lower'], x['lower_open']))
    upper = sorted(values, key=lambda x:math.inf if x['upper'] is None else x['upper'])
    lo = sum(lower[i]['lower'] for i in indices)/2
    hi = None if any(upper[i]['upper'] is None for i in indices) else sum(upper[i]['upper'] for i in indices)/2
    return {'lower':lo, 'upper':hi,
            'lower_open':any(lower[i]['lower_open'] for i in indices),
            'upper_open':hi is None or any(upper[i]['upper_open'] for i in indices)}

def run():
    tree = etree.parse(str(BASE/'data/raw/pmc7529437.xml'))
    rows = [[' '.join(c.itertext()).strip() for c in r]
            for r in tree.xpath('//table-wrap[@id="tab1"]//tbody/tr')]
    assert len(rows)==29 and all(len(r)==8 for r in rows)
    ids=[r[0] for r in rows]; assert len(set(ids))==len(ids)
    ancestor=[r for r in rows if r[0]=='D457']; assert len(ancestor)==1
    controls=[r for r in rows if r[1]=='MIEM']
    assert {r[0] for r in controls}=={'DA61805','DA61806','DA61807','DA61808'}
    # PDF extraction is independent of XML; compare cells for ALL population rows.
    pdf=subprocess.check_output(['pdftotext','-layout',str(BASE/'data/raw/blanco2020_published.pdf'),'-'],text=True).replace('⬎','>')
    for r in rows:
        lines=[l.split() for l in pdf.splitlines() if l.split() and l.split()[0]==r[0]]
        assert lines, f'PDF row missing {r[0]}'
        expected=[x for x in r if x]
        assert expected in lines, f'PDF/XML mismatch {r[0]}'
    methods=' '.join(tree.xpath('//sec//p//text()'))
    seqs={'LL-37':'LLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES',
          'PR-39':'RRRPRPPYLPRPRPPPFFPPRLPPRIPPGFPPRFPPRFP'}
    assert all(s in methods for s in seqs.values()) and seqs['PR-39']+'-NH2' in methods
    sp=json.loads((BASE/'results/spohn_units_a3.json').read_text())['units']
    result={'prereg':'A4', 'source':'PMC7529437 Table 1', 'pdf_xml_verified_rows':len(rows),
            'controls_reported':4, 'unreported_controls_imputed':0,'treatments':[]}
    for drug,col,start in [('LL-37',4,61715),('PR-39',5,61723)]:
        chosen=[r for r in rows if r[1]==drug]
        assert {r[0] for r in chosen}=={f'DA{i}' for i in range(start,start+8)}
        c=[parse(r[col]) for r in controls]
        assert all(x['lower']==x['upper'] for x in c)
        ref=statistics.median(x['lower'] for x in c)
        anc=parse(ancestor[0][col]); assert anc['upper']==anc['lower']
        pop=[{'population':r[0],'raw_mic':r[col],'unit':'mg/liter',
              'mic_interval':parse(r[col]),'net_log2_interval':transform(parse(r[col]),ref),
              'ancestor_log2_interval':transform(parse(r[col]),anc['lower'])} for r in chosen]
        med=median_interval([x['net_log2_interval'] for x in pop])
        match=[x for x in sp if x['sequence']==seqs[drug]]; assert len(match)==1
        point=match[0]['net_log2fc']
        contains=(point>med['lower'] if med['lower_open'] else point>=med['lower']) and (med['upper'] is None or point<=med['upper'])
        direction='not_ordered'
        if point<med['lower'] or (point==med['lower'] and med['lower_open']):direction='Blanco_median_above_Spohn_point'
        elif med['upper'] is not None and med['upper']<point:direction='Spohn_point_above_Blanco_median'
        result['treatments'].append({'drug':drug,'sequence':seqs[drug],
            'chemistry':'C-terminal amidated' if drug=='PR-39' else 'terminal modification not explicitly specified',
            'control_rows':[{'population':r[0],'raw_mic':r[col]} for r in controls],
            'control_median_mic':ref,'ancestor_mic':anc['lower'],'populations':pop,
            'median_net_log2_interval':med,'Spohn_A3_point':point,'Spohn_point_in_interval':contains,
            'descriptive_order':direction,'comparison_caveat':'Different species/media; Spohn chemistry not adjudicated; A3 point rounded to 4 decimals'})
    (BASE/'results/blanco_intervals_a4.json').write_text(json.dumps(result,indent=2)+'\n')
    for t in result['treatments']:print(t['drug'],t['median_net_log2_interval'],t['descriptive_order'])

if __name__=='__main__':run()
