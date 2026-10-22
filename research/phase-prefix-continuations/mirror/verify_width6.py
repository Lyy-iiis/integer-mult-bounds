#!/usr/bin/env python3
"""Optional mask2 width-six modular screen from literal WORDS.json.

Requires NumPy and SciPy. This is a sampled natural H5 tensor V8 hook screen,
not an all-width endpoint certificate. Exact-in-double Schur panels operate
on bounded integer products; the field is F65537 with i=256.
"""
import argparse,hashlib,json,platform,sys,types
from pathlib import Path
sys.dont_write_bytecode=True
import numpy as np
import scipy
from scipy.sparse import csc_matrix,eye,kron,hstack
ROOT=Path(__file__).resolve().parent
ENGINE_SHA='99ff0beccd9a4e94cc607e02114d62b8ce0ea57ee00748b07ce0a0af91aec85e'
RANK_SHA='f2b2e4c2ce5780d8c7cb0ae20ea0c8dd5f4587611cc6dc6f17b58d7cdb1bb4de'
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--words',type=Path,default=ROOT/'WORDS.json')
ap.add_argument('--engine',type=Path,default=ROOT.parent/'vendor/pr4688/verify.py')
ap.add_argument('--rank-engine',type=Path,default=ROOT.parent/'modrank.py')
ap.add_argument('--mask',type=int,choices=(2,),default=2)
ap.add_argument('--out',type=Path,required=True)
args=ap.parse_args()
def load(path,digest,name):
 raw=path.read_bytes()
 if hashlib.sha256(raw).hexdigest()!=digest:raise ValueError(name+' dependency hash mismatch')
 module=types.ModuleType(name);exec(compile(raw,str(path),'exec'),module.__dict__);return module
m=load(args.engine,ENGINE_SHA,'hook_engine');rk=load(args.rank_engine,RANK_SHA,'rank_engine')
data=json.loads(args.words.read_text());p=65537;ii=256;n=4480

def md(a):
 a=a.tocsr();a.data%=p;a.eliminate_zeros();return a

def sparse(columns):
 row=[];col=[];values=[]
 for j,source in enumerate(columns):
  for i,(a,b) in source.items():row.append(i);col.append(j);values.append((a+ii*b)%p)
 return csc_matrix((np.array(values,dtype=np.int64),(row,col)),shape=(560,560)).tocsr()

def mono(perm,exps):
 columns=[]
 for x,subset in m.BASIS:
  dest=tuple(perm[t] for t in subset);sign=m.wedge_sign(dest)
  a,b=m.I_POWERS[(exps[x]+sum(exps[t] for t in subset))%4]
  columns.append({m.INDEX[perm[x],tuple(sorted(dest))]:(sign*a,sign*b)})
 base=csc_matrix((np.array([pow(ii,e%4,p) for e in exps],dtype=np.int64),(perm,list(range(8)))),shape=(8,8)).tocsr()
 return md(kron(sparse(columns),base))
letters={name:mono(v['permutation'],v['phase_i']) for name,v in data['free_base_letters'].items()}
I8=eye(8,dtype=np.int64,format='csr')
for j in range(3):
 X=csc_matrix((np.ones(8,dtype=np.int64),([x^(1<<j) for x in range(8)],list(range(8)))),shape=(8,8)).tocsr()
 D8=md(I8-ii*X);D5=sparse(m.lift_direction(1<<j))
 letters['C'+str(j)]=md(kron(D5,D8)*(-ii*pow(8,-1,p)%p))
Z=csc_matrix((n,n),dtype=np.int64).tocsr();cache={():eye(n,dtype=np.int64,format='csr')}
def expand(word):
 result=[]
 for a in word:result.extend(expand(data['derived_words'][a]) if a in data['derived_words'] else [a])
 return tuple(result)
def W(word):
 word=expand(word)
 if word not in cache:cache[word]=md(letters[word[0]]@W(word[1:]))
 return cache[word]
def assemble(terms):
 answer=[Z.copy(),Z.copy()]
 for t in terms:
  num,den=t['coefficient'];coefficient=num*pow(den,-1,p)%p
  answer[t['input']]=md(answer[t['input']]+W(t['word'])*coefficient)
 return answer
states=[assemble(data['retained_states'][name]) for name in ('u','v','r','s','t')];K=W(['K'])
inside=np.array([8*j+k for j in m.cut_indices(args.mask) for k in range(8)]);iset=set(inside);outside=np.array([j for j in range(n) if j not in iset])
def rows(a,b):return hstack([a[outside][:,inside],b[outside][:,inside]]).toarray()
basis=np.zeros((0,len(inside)*2),dtype=np.float64);ranks=[]
for index,(a,b) in enumerate(states):
 matrix=rows(a,b);matrix=matrix[np.any(matrix,axis=1)]
 basis=rk.rank(np.vstack([basis,matrix]),return_basis=True);ranks.append(len(basis))
 print(json.dumps({'mask':args.mask,'stage':index+1,'rank_mod':len(basis)}),flush=True)
target=np.vstack([rows(K,Z),rows(Z,K)]);target=target[np.any(target,axis=1)]
joint=rk.rank(np.vstack([basis,target]))
if ranks!=[640,1280,1920,2560,3200] or joint!=3584:raise ValueError((ranks,joint))
receipt={'status':'PASS','prime':p,'scope':'Only mask2, natural H5 tensor V8 lifted hook, modular lower-bound screen; no uniform endpoint claim.','words_sha256':hashlib.sha256(args.words.read_bytes()).hexdigest(),'source_engine_sha256':ENGINE_SHA,'rank_engine_sha256':RANK_SHA,'runtime':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'records':[{'mask':args.mask,'stages':ranks,'target_joint':joint,'call_cap':640}]}
args.out.write_text(json.dumps(receipt,indent=2)+'\n');print('PASS_MIRROR_WIDTH6_MASK2',flush=True)
