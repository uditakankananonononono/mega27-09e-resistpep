import json,re,time,urllib.request,urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path
B=Path(__file__).resolve().parents[1]; LOCK='8b31b6a0a6221733e557036a02cd1e59aecde703'
AMP='("LL-37" OR cathelicidin OR CAP18 OR "antimicrobial peptide" OR defensin)'
ORG='(Escherichia OR Salmonella OR Enterobacter OR Klebsiella)'
Q={'Q1':f'(basS OR pmrB) AND ("LL-37" OR cathelicidin OR CAP18 OR "antimicrobial peptide") AND {ORG}',
'Q2':f'(basR OR pmrA) AND (defensin OR "LL-37" OR cathelicidin OR "antimicrobial peptide") AND {ORG}',
'Q3':f'lptC AND {AMP}','Q4':f'(wzzE OR "wzz(ECA)" OR "ECA chain length") AND {AMP}'}
def get(u):
    for i in range(3):
        try: return urllib.request.urlopen(u,timeout=60).read()
        except Exception as e: time.sleep(2)
    raise
base='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
ids={};counts={}
for k,q in Q.items():
    d=json.loads(get(base+'esearch.fcgi?'+urllib.parse.urlencode({'db':'pmc','term':q,'retmax':200,'retmode':'json'})))['esearchresult']
    counts[k]=int(d['count']); 
    for i in d['idlist']: ids.setdefault(i,[]).append(k)
    time.sleep(0.4)
genes=re.compile(r'\b(basS|basR|pmrA|pmrB|lptC|wzzE)\b'); amp=re.compile(r'LL-37|cathelicidin|CAP18|defensin|hBD3|antimicrobial peptide')
pert=re.compile(r'mutant|mutation|deletion|knockout|delta|\u0394|overexpress|knockdown')
kept={};log=[]
for n,(i,qs) in enumerate(ids.items()):
    try: x=get(base+'efetch.fcgi?db=pmc&id=%s&retmode=xml'%i)
    except Exception as e: log.append({'pmcid':i,'error':str(e)}); continue
    try: root=ET.fromstring(x)
    except Exception as e: log.append({'pmcid':i,'error':'parse'}); continue
    title=''.join(root.find('.//article-title').itertext()) if root.find('.//article-title') is not None else ''
    pm=[a.text for a in root.iter('article-id') if a.get('pub-id-type')=='pmid']
    paras=[''.join(p.itertext()) for p in root.iter('p')]
    hits=[p for p in paras if genes.search(p) and amp.search(p) and pert.search(p)]
    log.append({'pmcid':i,'pmid':pm[:1],'title':title[:150],'queries':qs,'n_hit_paras':len(hits)})
    if hits: kept[i]={'title':title,'pmid':pm[:1],'queries':qs,'paras':hits[:6]}
    time.sleep(0.4)
json.dump({'lock_commit':LOCK,'counts':counts,'n_fetched':len(ids),'n_kept':len(kept),'log':log},open(B/'results/fulltext_sweep_a17.json','w'),indent=1)
json.dump(kept,open(B/'results/fulltext_sweep_a17_kept_paragraphs.json','w'),indent=1)
print(counts,len(ids),len(kept))
