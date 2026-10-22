#!/usr/bin/env python3
"""Replay exact literal, coset, and all-eight-cut width5 gates; stdlib only."""
import argparse,hashlib,json,os,subprocess,sys
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',required=True,type=Path);ap.add_argument('--quick',action='store_true',help='word/coset controls only; not the complete width5 replay');args=ap.parse_args()
if args.out.exists() and any(args.out.iterdir()):raise ValueError('output directory must be fresh or empty')
args.out.mkdir(parents=True,exist_ok=True)
manifest=json.loads((ROOT/'MANIFEST.json').read_text())
for name,digest in manifest['files'].items():
 if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:raise ValueError('changed distributed artifact: '+name)
commands=[('mirror/verify_words.py','mirror-WORD-REPLAY.json'),('mirror/verify_cosets.py','mirror-COSET.json'),('staggered/verify_word.py','staggered-WORD-REPLAY.json'),('staggered/verify_cosets.py','staggered-COSET-PROJECTION.json')]
if not args.quick:commands += [('mirror/verify_exact.py','mirror-EXACT.json'),('staggered/verify_exact.py','staggered-EXACT.json')]
env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
for script,name in commands:
 command=[sys.executable,'-B',str(ROOT/script),'--out',str(args.out/name)]
 print('REPLAY '+script,flush=True);subprocess.run(command,check=True,env=env)
 expected={'mirror/verify_words.py':'mirror/WORD-REPLAY.json','mirror/verify_cosets.py':'mirror/COSET.json','staggered/verify_word.py':'staggered/WORD-REPLAY.json','staggered/verify_cosets.py':'staggered/COSET-PROJECTION.json','mirror/verify_exact.py':'mirror/EXACT.json','staggered/verify_exact.py':'staggered/EXACT.json'}
 if json.loads((args.out/name).read_text())!=json.loads((ROOT/expected[script]).read_text()):raise ValueError('fresh receipt differs from distributed evidence: '+script)
receipt={'status':'PASS','scope':'literal word and graph controls only' if args.quick else 'literal word/coset controls and exact all8 width5 hook checks','commands':[s for s,_ in commands],'width6':'optional finite-field screens not run by this default exact replay'}
(args.out/'REPLAY.json').write_text(json.dumps(receipt,indent=2)+'\n');print('PASS_PHASE_CONTINUATION_HANDOFF',flush=True)
