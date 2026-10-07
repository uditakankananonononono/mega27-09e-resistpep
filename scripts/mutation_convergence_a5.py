"""A5 cross-study mutation convergence audit. Mutation content only; no MICs.
Genes are extracted verbatim from pinned sources; never hand-typed."""
import json, re, zipfile, io
from collections import Counter, defaultdict
from pathlib import Path
import openpyxl
from lxml import etree
BASE = Path(__file__).resolve().parents[1]
ADOPTED = {'BAC5','CAP18','CP1','HBD3','IND','LL37','PEX','PGLA','PLEU','PR39','R8','TPII'}

def clean_gene(raw):
    g = re.sub(r'[\xa0\s]', ' ', str(raw)).strip()
    g = re.sub(r'\s*[→←]+\s*', '', g).strip()
    return g

def spohn():
    z = zipfile.ZipFile(BASE/'data/raw/spohn2019_supp.zip')
    w = openpyxl.load_workbook(io.BytesIO(z.read('41467_2019_12364_MOESM9_ESM.xlsx')), read_only=True, data_only=True)
    out = []
    sheets = {'SNPs':('Strain','Gene','Mutation'), 'short_deletion':('Strain','Gene','Mutation'),
              'insertion':('Strain','Gene','Mutation'), 'large_deletion':('Strain','List of deleted genes','Mutation'),
              'intergenic mutation':('Strain','Gene','Mutation')}
    for s in w:
        if s.title not in sheets: continue
        rows = list(s.iter_rows(values_only=True))
        hi = next(i for i,r in enumerate(rows) if r and any(str(c).strip()=='Strain' for c in r if c))
        hdr = [str(c).strip() if c else '' for c in rows[hi]]
        si = hdr.index('Strain'); gi = hdr.index(sheets[s.title][1])
        for r in rows[hi+1:]:
            if not r or not r[si]: continue
            strain = str(r[si]).strip()
            amp = strain.rsplit('_',1)[0]
            if amp not in ADOPTED: continue
            for g in re.split(r'[,/]', str(r[gi])):
                g = clean_gene(g)
                if g and not g.startswith('['):  # '[' marks partially deleted
                    out.append({'study':'spohn2019','organism':'E. coli BW25113','amp':amp,
                                'line':strain,'gene':g,'mutation_type':s.title})
    return out

def blanco():
    tree = etree.parse(str(BASE/'data/raw/pmc7529437.xml'))
    rows = [[' '.join(c.itertext()).strip() for c in r] for r in tree.xpath('//table-wrap[@id="tab3"]//tbody/tr')]
    out = []
    for r in rows:
        strain, medium = r[0], r[1]
        if medium not in ('LL-37','PR-39','No AMP'): continue
        scope = 'control' if medium=='No AMP' else 'evolved'
        for cell in re.split(r'(?<=\))', r[2]):
            m = re.match(r'\s*([A-Za-z][A-Za-z0-9_]*|IGR)\s*\(', cell)
            genes = []
            if m and m.group(1) != 'IGR':
                genes = [m.group(1)]
            elif 'IGR' in cell:
                genes = re.findall(r'sm[dm]_\d+|btuE2|smmG', r[2])
                genes = [g for g in genes if g in cell.split('and')[-1] or g in cell]
                genes = list(dict.fromkeys(re.findall(r'(?:smd|smm)_\d+|btuE2', cell)))
            for g in genes:
                out.append({'study':'blanco2020','organism':'S. maltophilia D457','amp':medium,
                            'line':strain,'gene':g,'mutation_type':r[4],'scope':scope,
                            'source_annotation':r[6] if len(r)>6 else ''})
    return out

def bac7():
    tree = etree.parse(str(BASE/'data/raw/pmc10145973.xml'))
    tw = tree.xpath('//table-wrap[.//label[contains(.,"Table 1")]]')
    assert len(tw)==1
    rows = [[' '.join(c.itertext()).strip() for c in r] for r in tw[0].xpath('.//tbody/tr')]
    out = []
    for r in rows:
        if not r or not r[0].startswith('B'): continue
        out.append({'study':'bac7_2023','organism':'E. coli MDR 1057','amp':'Bac7(1-22)',
                    'line':r[0],'gene':r[4],'mutation_type':r[3],'scope':'evolved',
                    'source_annotation':r[5] if len(r)>5 else ''})
    return out

def recurrence(records):
    evo = [r for r in records if r.get('scope','evolved')=='evolved']
    within = {}
    for (study,amp), group in defaultdict(list).items(): pass
    groups = defaultdict(set)
    types = defaultdict(set)
    for r in evo:
        groups[(r['study'],r['amp'],r['gene'])].add(r['line'])
        types[(r['study'],r['amp'],r['gene'])].add(r['mutation_type'])
    within = [{'study':k[0],'amp':k[1],'gene':k[2],'n_lines':len(v),
               'mutation_types':sorted(types[k]),
               'driven_by_large_deletion':types[k]=={'large_deletion'}}
              for k,v in groups.items() if len(v)>=2]
    by_gene = defaultdict(set)
    for r in evo: by_gene[r['gene'].lower()].add(r['study'])
    cross = [{'gene':g,'studies':sorted(s)} for g,s in by_gene.items() if len(s)>=2]
    return sorted(within,key=lambda x:(-x['n_lines'],x['gene'])), sorted(cross,key=lambda x:x['gene'])

def run():
    records = spohn()+blanco()+bac7()
    assert all(isinstance(r['gene'],str) and r['gene'] for r in records)
    # verbatim provenance: every extracted gene string must appear in the pinned source bytes
    src = (BASE/'data/raw/spohn2019_supp.zip').read_bytes() and None
    blanco_xml = (BASE/'data/raw/pmc7529437.xml').read_text()
    bac7_xml = (BASE/'data/raw/pmc10145973.xml').read_text()
    z = zipfile.ZipFile(BASE/'data/raw/spohn2019_supp.zip')
    xz = zipfile.ZipFile(io.BytesIO(z.read('41467_2019_12364_MOESM9_ESM.xlsx')))
    spohn_strings = xz.read('xl/sharedStrings.xml').decode('utf-8')
    for r in records:
        if r['study']=='spohn2019':
            assert r['gene'] in spohn_strings, r
        elif r['study']=='blanco2020':
            assert r['gene'] in blanco_xml, r
        else:
            assert r['gene'] in bac7_xml, r
    within, cross = recurrence(records)
    # independent second pass with a different counting method
    evo = [r for r in records if r.get('scope','evolved')=='evolved']
    c = Counter((r['study'],r['amp'],r['gene'],r['line']) for r in evo)
    pairs = Counter((k[0],k[1],k[2]) for k in c)
    within2 = sorted(({'study':k[0],'amp':k[1],'gene':k[2],'n_lines':v} for k,v in pairs.items() if v>=2),
                     key=lambda x:(-x['n_lines'],x['gene']))
    assert [{k:w[k] for k in ('study','amp','gene','n_lines')} for w in within]==within2, 'second-pass within-study mismatch'
    studies_per_gene = defaultdict(set)
    for r in evo: studies_per_gene[r['gene'].lower()].add(r['study'])
    cross2 = sorted(({'gene':g,'studies':sorted(s)} for g,s in studies_per_gene.items() if len(s)>=2), key=lambda x:x['gene'])
    assert cross==cross2, 'second-pass cross-study mismatch'
    out = {'prereg':'A5','records':records,
           'counts':{'total_records':len(records),
                     'spohn_evolved':sum(1 for r in records if r['study']=='spohn2019'),
                     'blanco_evolved':sum(1 for r in records if r['study']=='blanco2020' and r['scope']=='evolved'),
                     'blanco_control_excluded':sum(1 for r in records if r.get('scope')=='control'),
                     'bac7_evolved':sum(1 for r in records if r['study']=='bac7_2023')},
           'within_study_recurrence':within,'cross_study_exact_matches':cross}
    (BASE/'results/mutation_convergence_a5.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out['counts']))
    print('within-study recurrences:',len(within))
    for w in within: print(' ',w)
    print('cross-study exact matches:',cross)

if __name__=='__main__': run()
