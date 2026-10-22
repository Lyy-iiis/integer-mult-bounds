#!/usr/bin/env python3
"""Exact two-full opposite-orientation Laurent border controller.
Apache-2.0; Yiyang (@Lyy-iiis), substantial OpenAI Codex assistance.
This is an approximate endpoint family, not an admitted exponent claim.
"""
import argparse,json,sys
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
sys.dont_write_bytecode=True
def need(x,m):
 if not x:raise ValueError(m)
# Monomial keys: (Q exponent, epsilon exponent, independent fresh-D mask).
def m(c=1,q=0,e=0,d=0):return {(q,e,d):F(c)} if c else {}
def add(a,b):
 out=dict(a)
 for k,v in b.items():
  out[k]=out.get(k,F(0))+v
  if not out[k]:del out[k]
 return out
def mul(a,b):
 out={}
 for (q,e,d),v in a.items():
  for (r,f,c),w in b.items():
   need(not d&c,'Independent fresh D variable repeated')
   k=(q+r,e+f,d|c);out[k]=out.get(k,F(0))+v*w
 return {k:v for k,v in out.items() if v}
def total(xs):
 out={}
 for x in xs:out=add(out,x)
 return out
def mm(A,B):return [[total(mul(x,y) for x,y in zip(r,c)) for c in zip(*B)] for r in A]
def diag(a,b):return [[a,{}],[{},b]]
def product(xs):
 out=diag(m(),m())
 for x in xs:out=mm(out,x)
 return out
def enc(A):return [[[[q,e,d,str(v)] for (q,e,d),v in sorted(x.items())] for x in r] for r in A]
def run():
 S=diag(m(),m(e=1));Si=diag(m(),m(e=-1));B=[[m(),m(-1)],[m(),{}]]
 U=[[m(),m(q=1)],[{},m()]];L=[[m(),{}],[m(-1,q=-1),m()]]
 D1=diag(m(d=1),m(d=1));D2=diag(m(d=2),m(d=2))
 word=[S,D1,U,D2,L,B,Si]
 out=product(word)
 wanted=[[m(q=1,d=3),{}],[add(m(e=1,d=3),m(-1,q=-1,e=1,d=3)),m(q=-1,d=3)]]
 need(out==wanted,'Exact Laurent Q, epsilon and both independent-D endpoint')
 core=product([U,L,B])
 need(core==[[m(q=1),{}],[add(m(),m(-1,q=-1)),m(q=-1)]],'Triangular unscaled core')
 controls={
  'omit_constant_right_boundary':product([S,D1,U,D2,L,Si])!=wanted,
  'replace_lower_query_by_wrong_Q_direction':product([S,D1,U,D2,[[m(),{}],[m(-1,q=1),m()]],B,Si])!=wanted,
  'delete_second_fresh_native_D':product([S,D1,U,L,B,Si])!=wanted,
  'erase_nonzero_residual':out!=diag(m(q=1,d=3),m(q=-1,d=3)),
  'epsilon_zero_not_a_legal_input_chart':any(e<0 for row in Si for x in row for q,e,d in x)
 }
 need(all(controls.values()),'Every targeted mutation rejected')
 H={4:28,7:7,8:47,9:326};P={1:2201,2:412,3:510,4:127,5:40,8:8}
 target={r:2*v for r,v in H.items()};target[17]=224;paid={r:2*v for r,v in P.items()}
 need(sum(r*v for r,v in target.items())-sum(r*v for r,v in paid.items())==96,'Fully counted optimistic recursive rank mass')
 return {'status':'PASS_EXACT_LAURENT_BORDER_IDENTITY_NOT_A_BOUND','ring':'Q[Q,Q^-1,epsilon,epsilon^-1,D1,D2] with independent once-used D variables',
  'endpoint':enc(out),'factors_algebraic_order':[enc(x) for x in word],
  'input_boundary':enc(mm(B,Si)),'output_boundary':enc(S),
  'native_orientation_binding':{'upper':'Sign conjugate of retained backward U(-Q), on fresh D1','lower':'Sign conjugate of retained forward L(Q^-1), on fresh D2'},
  'main_jobs':[{'count':112,'central_Q_exponent':1,'rank':17},{'count':112,'central_Q_exponent':-1,'rank':17}],
  'helpers':{r:2*v for r,v in H.items()},'target_profile':target,'paid_profile':paid,'rank_surplus_before_new_precision_cost':96,
  'profile_source_head':'0ce1b5c9fb7163d0b2f0ac3db95fc418dbbcec62',
  'thin_recursive_queries':0,'controls':controls,
  'scope':'Literal Laurent identity with a NONZERO epsilon residual; no involutivization or alpha adapter is used. Complete recursive profiles are conditional on inherited forward/backward native interfaces. Epsilon-dependent precision, compiler closure, whole-product endpoint and BIT admission are not proved. PR4623 is relevant prior border-controller work; no novelty claim for border scaling.'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();need(not a.out.exists(),'Fresh receipt');r=run();r['checker_sha256']=sha256(Path(__file__).read_bytes()).hexdigest();a.out.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':r['status'],'controls':len(r['controls']),'rank_surplus':r['rank_surplus_before_new_precision_cost']}))
