#!/usr/bin/env python3
"""Exact normalized literal program versus reduced residual words, widths1/2.
Stdlib only; imports only Fraction-pair matrix primitives from the frozen
residual verifier. Does not call its scientific verifier or hook-rank engine.
"""
import argparse,hashlib,json,sys,types
from pathlib import Path
sys.dont_write_bytecode=True
parser=argparse.ArgumentParser(description=__doc__)
ROOT=Path(__file__).resolve().parent
parser.add_argument('--arithmetic',default=ROOT.parent/'arithmetic.py',type=Path)
parser.add_argument('--words',default=ROOT/'WORDS.json',type=Path)
parser.add_argument('--out',type=Path)
args=parser.parse_args()
v=types.ModuleType('gaussian_arithmetic');payload=args.arithmetic.read_bytes()
if hashlib.sha256(payload).hexdigest()!='0d277854396e4ceda1e0f26916bd576b6decb474c0692b6671ebf2595283ddb9':
 raise ValueError('arithmetic dependency SHA256 mismatch')
exec(compile(payload,str(args.arithmetic),'exec'),v.__dict__)
data=json.loads(args.words.read_text())
def tensor(a,b):
 n=len(b)
 return tuple(tuple(v.mul(a[i//n][j//n],b[i%n][j%n]) for j in range(len(a)*n)) for i in range(len(a)*n))
def power(a,f):
 out=((v.ONE,),)
 for _ in range(f):out=tensor(out,a)
 return out
def expand(word):
 result=[]
 for a in word:result.extend(expand(data['derived_words'][a]) if a in data['derived_words'] else [a])
 return result
base={name:v.monomial(a['permutation'],a['phase_i']) for name,a in data['free_base_letters'].items()}
base.update({f'C{i}':v.c_letter(i) for i in range(3)})
def base_word(*word):
 return v.word(*(base[a] for a in expand(word)))
branch_identities=[
 (('JA','WA','C0','P01','C0'),('K','a')),
 (('JB','WB','C0','P02','C0'),('K','b')),
 (('JA','WA','C0','P02','C0'),('MA','C2')),
 (('JB','WB','C0','P01','C0'),('MB','C1')),
]
for left_word,right_word in branch_identities:
 v.require(base_word(*left_word)==base_word(*right_word),'individual base-word identity failed')
records=[]
for f in (1,2):
 n=8**f;I=v.ident(n);Z=v.scale(v.ZERO,I);letters={name:power(a,f) for name,a in base.items()};cache={}
 def W(*word):
  key=tuple(expand(word))
  if key not in cache:cache[key]=v.word(*(letters[a] for a in key)) if key else I
  return cache[key]
 def add(a,b):return tuple(v.plus(x,y) for x,y in zip(a,b))
 def scale(c,a):return tuple(v.scale(c,x) for x in a)
 def left(c,a):return tuple(v.mm(c,x) for x in a)
 x=(I,Z);y=(Z,I);quarter=v.q(v.F(1,4));two=v.q(2)
 u=left(W('C0'),x)
 vv=left(W('C0'),y)
 r=left(W('C0'),add(left(W('P01'),u),left(W('P02'),vv)))
 LA=v.plus(W('P2','V02'),v.scale(two,W('Q2','V02')))
 LB=v.plus(W('P1','V01'),v.scale(two,W('Q1','V01')))
 ss=left(W('JA'),add(left(W('WA'),r),scale(quarter,left(LA,vv))))
 tt=left(W('JB'),add(left(W('WB'),r),scale(quarter,left(LB,u))))
 actual={'u':u,'v':vv,'r':r,'s':ss,'t':tt}
 for name,terms in data['retained_states'].items():
  reduced=[Z,Z]
  for term in terms:
   c=v.q(v.F(*term['coefficient']));i=term['input'];reduced[i]=v.plus(reduced[i],v.scale(c,W(*term['word'])))
  v.require(tuple(reduced)==actual[name],'literal/reduced state mismatch '+name+' width'+str(f))
 v.require(v.word(v.adjoint(W('C0')),u[0])==I,'x information preserved')
 v.require(v.word(v.adjoint(W('C0')),vv[1])==I,'y information preserved')
 # These inverses justify information preservation; the program does not run them.
 rec={'width':f,'dimension':n,'status':'PASS','five_paid_queries':True,'two_independent_input_blocks':True,'five_retained_states_match_reduced_words':True}
 records.append(rec);print(json.dumps(rec),flush=True)
result={'status':'PASS','arithmetic':'exact Gaussian Fraction pairs','word_file_sha256':hashlib.sha256(args.words.read_bytes()).hexdigest(),'arithmetic_file_sha256':hashlib.sha256(payload).hexdigest(),'individual_base_word_identities_verified':branch_identities,'records':records,'all_width_proof':'All reduced identities are sums of separately verified base-letter word equalities; tensor each word before adding fixed rational coefficients. Width1/2 replays are controls, not the all-width proof by themselves.'}
if args.out:args.out.write_text(json.dumps(result,indent=2)+'\n')
