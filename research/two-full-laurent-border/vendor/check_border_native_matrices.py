#!/usr/bin/env python3
"""Independent exact source-Cgate matrix replay of the two-full border word.
Apache-2.0; Yiyang Lu (@Lyy-iiis), substantial OpenAI Codex assistance.
The nonzero residual is retained. This checker does not prove a precision theorem.
"""
import argparse,json,sys,types
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
sys.dont_write_bytecode=True
PIN='2982ead07721e83358dc67c6f49c2b4c16a236a6bebdfd72f58221be1f5d0962'
def need(x,m):
 if not x:raise ValueError(m)
def g(a=0,b=0):return F(a),F(b)
def ga(x,y):return x[0]+y[0],x[1]+y[1]
def gm(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def eye(n):return [[g(i==j) for j in range(n)] for i in range(n)]
def zero(n):return [[g() for j in range(n)] for i in range(n)]
def scale(A,c):
 c=c if isinstance(c,tuple) else g(c)
 return [[gm(c,x) for x in r] for r in A]
def add(A,B,c=1):return [[ga(x,gm(g(c),y)) for x,y in zip(r,s)] for r,s in zip(A,B)]
def mm(A,B):
 out=[]
 for row in A:
  rr=[]
  for col in zip(*B):
   v=g()
   for x,y in zip(row,col):
    if any(x) and any(y):v=ga(v,gm(x,y))
   rr.append(v)
  out.append(rr)
 return out
def adj(A):return [[(a,-b) for a,b in r] for r in zip(*A)]
def kron(A,B):return [[gm(a,b) for a in ra for b in rb] for ra in A for rb in B]
def block(A,B,C,D):return [x+y for x,y in zip(A,B)]+[x+y for x,y in zip(C,D)]
def scalar_block(a,b,c,d,n):return block(scale(eye(n),a),scale(eye(n),b),scale(eye(n),c),scale(eye(n),d))
def actual(op):
 cols=[]
 for j in range(1<<op.n):
  v,d=op.zero_state(j);cols.append([(F(a,1<<d),F(b,1<<d)) for a,b in v])
 return [list(r) for r in zip(*cols)]
def digest_matrix(M):return sha256(json.dumps([[[str(a),str(b)] for a,b in r] for r in M],separators=(',',':')).encode()).hexdigest()
def run(engine):
 raw=engine.read_bytes();need(sha256(raw).hexdigest()==PIN,'Exact inherited Cgate source pin')
 ce=types.ModuleType('border_exact_source_cgate');sys.modules[ce.__name__]=ce;exec(compile(raw,str(engine),'exec'),ce.__dict__)
 # Build D1,D2 from the source's actual phase-preserving circuit interpreter.
 d1=actual(ce.cgate(2,1));d2=actual(ce.cgate(2,2));D=mm(d1,d2)
 need(mm(D,adj(D))==eye(4),'Two distinct fresh D model factors are unitary')
 rows=[];rejects=[]
 for f in (1,2,3):
  q=actual(ce.fourier(f));n=1<<f;I=eye(n);Z=zero(n);J=mm(q,q)
  need(mm(J,J)==I and mm(q,adj(q))==I,'Actual all-character Q is unitary/order4')
  need(J==actual(ce.xgate(f,(1<<f)-1)),'Actual Q_f square is the retained Pauli shift')
  alpha=add(scale(I,g(F(1,2),F(-1,2))),scale(J,g(F(1,2),F(1,2))))
  ai=adj(alpha);R=mm(alpha,q)
  need(mm(alpha,ai)==I and mm(R,R)==I,'Actual sparse alpha is unitary and alpha Q involutive')
  # All fresh D factors share no central axis. Compare the actual joint source
  # circuit, including absolute phase, with the separately constructed tensor.
  joint=actual(ce.fourier(f+2));need(joint==kron(D,q),'Actual source full-axis phase tensor factorization')
  X=add(I,R,-1)
  GU=block(I,X,Z,I);GL=block(I,Z,scale(X,-1),I)
  for eps in (F(1,2),F(1,4)):
   C=scalar_block(eps,0,-1,1,n);Ci=scalar_block(1/eps,0,1/eps,1,n)
   need(mm(C,Ci)==eye(2*n),'Exact dyadic forward/inverse field charts')
   core=mm(mm(mm(C,GU),GL),Ci)
   out=mm(block(ai,Z,Z,ai),core)
   residual=scale(add(ai,q,-1),eps)
   wanted=block(q,residual,Z,q)
   need(out==wanted,'Actual source matrices retain precisely the declared nonzero residual')
   # Explicit physical tensor target D1D2 on every field, with no duplicated
   # arbitrary input or copied productive credit.
   phys=block(kron(D,[r[:n] for r in out[:n]]),kron(D,[r[n:] for r in out[:n]]),
              kron(D,[r[:n] for r in out[n:]]),kron(D,[r[n:] for r in out[n:]]))
   expected=block(joint,kron(D,residual),zero(4*n),joint)
   need(phys==expected,'Both actual main jobs have exactly the same fresh D1D2 and Q endpoint')
   rows.append({'fiber_width':f,'epsilon':str(eps),'central_dimension':n,'physical_pair_dimension':8*n,
                'Q_f_square_is_Pauli':True,'exact_residual_included':True,
                'residual_nonzero':residual!=Z,'physical_matrix_sha256':digest_matrix(phys)})
   if f>=2:
    need(residual!=Z,'Reject claiming exact endpoint for finite positive epsilon')
    rejects.append({'fiber_width':f,'epsilon':str(eps),'false_exact_endpoint_rejected':True})
 return {'status':'PASS_EXACT_NATIVE_PHASE_TENSOR_BORDER_MATRICES_NOT_A_BOUND','engine_sha256':PIN,
         'engine_path':str(engine),'rows':rows,'rejecting_controls':rejects,
         'endpoint':'D1D2 [Q I + epsilon(alpha_inverse-Q) E01]',
         'fresh_axis_test_scope':'Explicit two distinct rank-one fresh D model factors. Arbitrary rank-eight/full-width D1,D2 follow only by the separately stated tensor-commutation identity, not by materializing their enormous matrices.',
         'scope':'Exact actual inherited Cgate phases at fiber widths1,2,3 and finite epsilon. Nonzero residual is never waived. Does not supply size-dependent precision, recursive costs, compiler, BIT admission or an improved bound.'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--engine',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();need(not a.out.exists(),'Fresh result path');r=run(a.engine);r['script_sha256']=sha256(Path(__file__).read_bytes()).hexdigest();a.out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'exact_actual_matrix_cases':len(r['rows']),'controls':len(r['rejecting_controls'])}))
