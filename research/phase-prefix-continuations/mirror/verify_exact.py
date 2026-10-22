#!/usr/bin/env python3
"""Exact Q(i) width-five hook replay from literal normalized tensor words.

Requires Python standard library only. Each entire base word is lifted termwise;
fixed rational coefficients are added only after lifting. Each retained row is
scaled by one nonzero Gaussian scalar before integer Gaussian elimination.
"""
import argparse,hashlib,json,sys,types
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
ENGINE_SHA='99ff0beccd9a4e94cc607e02114d62b8ce0ea57ee00748b07ce0a0af91aec85e'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--engine',type=Path,default=ROOT.parent/'vendor/pr4688/verify.py')
parser.add_argument('--words',type=Path,default=ROOT/'WORDS.json')
parser.add_argument('--out',type=Path)
parser.add_argument('--mask',type=int,choices=[2,3,6,7,8,9,12,13],help='One-cut diagnostic; default verifies all eight cuts.')
parser.add_argument('--sectors',action='store_true',help='Also compute the four exact common-Pauli/input-swap sectors.')
args=parser.parse_args()
payload=args.engine.read_bytes()
if hashlib.sha256(payload).hexdigest()!=ENGINE_SHA:raise ValueError('source engine SHA256 mismatch')
m=types.ModuleType('pinned_pr4688');exec(compile(payload,str(args.engine),'exec'),m.__dict__)
data=json.loads(args.words.read_text())
if data['schema']!='literal_tensor_word_state_v1':raise ValueError('unsupported word schema')

def monomial(perm,exps):
 columns=[]
 for x,sub in m.BASIS:
  images=tuple(perm[t] for t in sub);sign=m.wedge_sign(images)
  a,b=m.I_POWERS[(exps[x]+sum(exps[t] for t in sub))%4]
  columns.append({m.INDEX[perm[x],tuple(sorted(images))]:(sign*a,sign*b)})
 return columns
letters={name:monomial(v['permutation'],v['phase_i']) for name,v in data['free_base_letters'].items()}
letters.update({f'C{i}':m.lift_direction(1<<i) for i in range(3)})
I=[{j:(1,0)} for j in range(560)]
cache={():I}
def expand(word):
 result=[]
 for a in word:result.extend(expand(data['derived_words'][a]) if a in data['derived_words'] else [a])
 return tuple(result)
def word_lift(word):
 word=expand(word)
 if word not in cache:
  cache[word]=m.compose(letters[word[0]],word_lift(word[1:]))
 return cache[word]
def gaussian_power(z,n):
 answer=(1,0)
 for _ in range(n):answer=m.mul(answer,z)
 return answer

def assemble(terms):
 """Scale a row of max-depth d by c^(-5d), c=(1+i)/2.

 rho_5(C_i)=c^5 rho_5(I-iX_i), and c^(-5)=-4+4i. Thus
 each term of depth e gets exact multiplier coeff*(-4+4i)^(d-e).
 The chosen denominators divide these Gaussian integers; otherwise reject.
 """
 depths=[sum(a in ('C0','C1','C2') for a in expand(t['word'])) for t in terms]
 depth=max(depths,default=0);result=[[{} for _ in range(560)] for _ in range(2)]
 for t,e in zip(terms,depths):
  num,den=t['coefficient'];z=gaussian_power((-4,4),depth-e)
  a,b=num*z[0],num*z[1]
  if a%den or b%den:raise ValueError('nonintegral row normalization')
  z=(a//den,b//den)
  lifted=[{i:m.mul(z,value) for i,value in col.items()} for col in word_lift(t['word'])]
  result[t['input']]=m.add_columns(result[t['input']],lifted)
 return result
states=[assemble(data['retained_states'][name]) for name in ('u','v','r','s','t')]
K=word_lift(['K'])
def pairrows(left,right,inside):
 n=len(inside);a=m.project(left,inside);b=m.project(right,inside)
 return [dict(list(x.items())+[(j+n,z) for j,z in y.items()]) for x,y in zip(a,b)]
zero=[{} for _ in range(560)];records=[]
def restrict_monomial(columns,inside):
 lookup={j:k for k,j in enumerate(inside)};perm=[];phase=[]
 for j in inside:
  if len(columns[j])!=1:raise ValueError('input symmetry is not monomial')
  dest,z=next(iter(columns[j].items()))
  if dest not in lookup:raise ValueError('input symmetry fails cut invariance')
  perm.append(lookup[dest]);phase.append(z)
 return perm,phase
def projector(rows,action,sign):
 perm,phase=action;inv={j:k for k,j in enumerate(perm)};result=[]
 for source in rows:
  row=source.copy()
  for j,z in source.items():
   k=inv[j];a,b=m.mul(z,phase[k]);m.accumulate(row,k,(sign*a,sign*b))
  result.append(row)
 return result
for mask in ([args.mask] if args.mask is not None else m.CUTS):
 inside=m.cut_indices(mask);blocks=[pairrows(a,b,inside) for a,b in states]
 targets=pairrows(K,zero,inside)+pairrows(zero,K,inside)
 ranks=[m.rank_exact(sum(blocks[:j],[])) for j in range(1,6)]
 joint=m.rank_exact(sum(blocks,[])+targets)
 rec={'mask':mask,'stage_potentials_exact':ranks,'target_joint_exact':joint}
 if ranks!=[80,160,240,320,400] or joint!=448:raise ValueError(rec)
 if args.sectors:
  n=len(inside);bp,bz=restrict_monomial(letters['b'],inside);ap,az=restrict_monomial(letters['a'],inside);pp,pz=restrict_monomial(letters['V21'],inside)
  G=(bp+[n+j for j in ap],bz+az);Pi=([n+j for j in pp]+pp,pz+pz);sectors=[]
  for e in (-1,1):
   for h in (-1,1):
    state=projector(projector(sum(blocks,[]),G,e),Pi,h);target=projector(projector(targets,G,e),Pi,h)
    sr=m.rank_exact(state);jr=m.rank_exact(state+target);tr=m.rank_exact(target)
    sectors.append({'G_sign':e,'Pi_sign':h,'state':sr,'target':tr,'joint':jr,'deficit':jr-sr})
  if [(z['state'],z['target'],z['joint']) for z in sectors]!=[(100,112,112),(100,112,112),(104,112,112),(96,112,112)]:raise ValueError(sectors)
  rec['sectors']=sectors
 records.append(rec);print(json.dumps(rec),flush=True)
result={'status':'PASS','field':'Q(i)','width':5,'full_eight_cut_replay':args.mask is None,'source_engine_sha256':ENGINE_SHA,'words_sha256':hashlib.sha256(args.words.read_bytes()).hexdigest(),'records':records,'scope':'Literal normalized word hook ranks only; no uniform endpoint completion or improved exponent is claimed.'}
if args.out:args.out.write_text(json.dumps(result,indent=2)+'\n')
