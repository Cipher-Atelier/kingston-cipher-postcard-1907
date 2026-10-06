#!/usr/bin/env python3
"""New, read-only replay audit. Does not re-fit keys or certify manuscript truth.
Run from this reading packet: python3 replay.py
"""
from pathlib import Path
import json,csv,hashlib,re,string,sys
P=Path(__file__).resolve().parent
E=P/'evidence' if (P/'evidence').exists() else P/'repro_inventory_core'
REPORT={}
def txt(p):return p.read_text(encoding='utf-8')
def js(p):return json.loads(txt(p))
def sha(b):return hashlib.sha256(b).hexdigest()
def record(topic,**kw):REPORT[topic]={'status':'PASS','scope':'mechanical replay only',**kw}

if sys.flags.optimize:
 raise SystemExit('Run normal Python; assertion checks must remain enabled.')

# Kingston: compare every occurrence, including masked and unexplained slots.
k=E/'HCP1193_Verified_Reading';key=js(k/'geometry_key.json');rows=list(csv.DictReader((k/'transcription_and_reading.tsv').open(),delimiter='\t'));assigned=masked=unexplained=0
for r in rows:
 mm=re.fullmatch(r'([TLBR]+)([123])',r['post_review_glyph']);canon=(''.join(x for x in 'TLBR' if x in mm[1])+mm[2]) if mm else None
 out='?' if r['source_masked']=='True' else key.get(canon)
 if out is None:out='[27]' if canon=='TL3' else '?'
 assert out==r['strict_output'];assigned+=len(out)==1 and out!='?';masked+=out=='?';unexplained+=out=='[27]'
assert (len(rows),assigned,masked,unexplained)==(222,213,8,1)
record('kingston-1907',positions=222,mapped=assigned,unknown=masked,unexplained_slot27=unexplained,limit='213/222 is coverage, not accuracy.')

print(json.dumps(REPORT,ensure_ascii=False,indent=2))
