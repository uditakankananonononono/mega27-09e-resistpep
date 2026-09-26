"""Parse PLOS ONE PMC3720879 main-text tables (pinned XML) into processed CSVs.
Outputs: table2_evolved_lineage_mics.csv, table3_fitness.csv, table4_amp_mics.csv,
table5_antibiotic_cross_resistance.csv, table1_genotypes.csv.
Fold-changes computed vs DA6192 WT MICs from Table 4 (midpoint of ranges, documented).
"""
import re, csv, json

x = open('data/raw/pmc3720879.xml').read()

def tables(x):
    out = {}
    for m in re.finditer(r'<table-wrap[^>]*>(.*?)</table-wrap>', x, re.S):
        t = m.group(1)
        lab = re.search(r'<label>(.*?)</label>', t)
        if not lab: continue
        rows = []
        for rm in re.finditer(r'<tr[^>]*>(.*?)</tr>', t, re.S):
            cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', rm.group(1), re.S)
            cells = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]
            rows.append(cells)
        out[lab.group(1)] = rows
    return out

T = tables(x)

def clean(s):
    return (s.replace('&#8211;', '-').replace('&gt;', '>').replace('&#8202;', ' '))

def mid(s):
    s = clean(s).replace('>', '').strip()
    parts = [p for p in re.split(r'[-\s]+', s) if p]
    try:
        vals = [float(p) for p in parts]
        return sum(vals) / len(vals)
    except ValueError:
        return None

# Table 4: AMP MICs + fold-change vs WT row
wt = {}
t4 = T['Table 4']
data = [r for r in t4 if r and r[0].startswith('DA')]
for r in data:
    if 'DA6192' in r[0]:
        wt = {'WGH': mid(r[1]), 'LL-37': mid(r[2]), 'CNY100HL': mid(r[3])}
with open('data/processed/table4_amp_mics.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['strain', 'WGH_mic', 'LL37_mic', 'CNY100HL_mic',
                'WGH_fc', 'LL37_fc', 'CNY100HL_fc'])
    for r in data:
        mics = [mid(r[1]), mid(r[2]), mid(r[3])]
        fcs = [round(m / wt[k], 3) if m is not None and wt.get(k) else None
               for m, k in zip(mics, ['WGH', 'LL-37', 'CNY100HL'])]
        w.writerow([r[0]] + mics + fcs)

# Table 2: evolved lineages
with open('data/processed/table2_evolved_lineage_mics.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['lineage', 'start_amp_conc_mgL', 'end_amp_conc_mgL', 'generations', 'mic_after_cycling_mgL'])
    for r in T['Table 2'][1:]:
        w.writerow([r[0], r[1], r[2], r[3], clean(r[4])])

# Table 3: fitness
with open('data/processed/table3_fitness.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['strain', 'growth_rate_refined_LB', 'growth_rate_MH', 'growth_rate_NaPB', 'competition_NaPB'])
    for r in T['Table 3'][3:]:
        w.writerow(r[:5])

# Table 5: antibiotic cross-resistance
with open('data/processed/table5_antibiotic_cross_resistance.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['strain', 'CR', 'FEP', 'MEM', 'CST', 'MEC', 'TGC', 'NAL'])
    for r in T['Table 5'][2:]:
        w.writerow(r[:8])

# Table 1: genotypes (strain -> genotype string)
with open('data/processed/table1_genotypes.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['strain', 'genotype', 'origin'])
    for r in T['Table 1'][1:]:
        if len(r) >= 3:
            w.writerow([clean(r[0]), clean(r[1]), clean(r[2])])

print(json.dumps({k: len(v) for k, v in T.items()}))
print('WT MICs (Table 4 DA6192):', wt)
