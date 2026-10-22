import sys,types,json,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
sys.dont_write_bytecode=True
ap=argparse.ArgumentParser(description='Exact Clifford left-coset graph obstruction for the literal staggered prefix');ap.add_argument('--out',required=True,type=Path);args=ap.parse_args()
p=Path(__file__).resolve().parents[1]/'arithmetic.py';payload=p.read_bytes()
if hashlib.sha256(payload).hexdigest()!='0d277854396e4ceda1e0f26916bd576b6decb474c0692b6671ebf2595283ddb9': raise ValueError('immutable arithmetic mismatch')
v=types.ModuleType('v');exec(compile(payload,str(p),'exec'),v.__dict__)
C=[v.c_letter(j) for j in range(3)];S=v.s_letter(7);U=v.monomial([0,5,2,7,4,1,6,3]);V=v.monomial([0,2,1,3,4,6,5,7]);T=v.monomial([0,4,2,6,1,5,3,7]);V21=v.monomial([0,1,4,5,2,3,6,7]);P=v.word(S,U,S);Q=v.word(S,V,S);Q2=v.word(S,V21,S);W=v.pauli(0,5);N=v.word(v.pauli(0,2),V);L=v.word(N,T);J=v.word(N,C[2]);K=v.word(*C)
I=v.ident()
def plus(*rows):
 r={}
 for a in rows:
  for key,c in a.items():r[key]=r.get(key,F(0))+c
 return {key:c for key,c in r.items() if c}
def left(M,row,scale=F(1)):
 return {(i,v.mm(M,g)):c*scale for (i,g),c in row.items()}
x={(0,I):F(1)};y={(1,I):F(1)}
u=left(C[0],x);vv=left(C[0],plus(left(P,u),left(Q,u,2)));r=left(v.word(v.adjoint(L),J),plus(left(W,vv),left(T,y)));tt=left(C[0],plus(left(P,r),left(Q,r,2)));z=left(J,plus(left(W,tt),left(Q2,r),left(P,vv)))
rows={'x':x,'y':y,'u':u,'v':vv,'r':r,'t':tt,'z':z}
refs={'K':K,'C0':C[0],'C1':C[1],'C2':C[2]}
def monomial(M):
 return all(sum(t!=v.ZERO for t in row)==1 for row in M) and all(sum(M[i][j]!=v.ZERO for i in range(8))==1 for j in range(8))
def desc(M):
 per=[];ph=[]
 for j in range(8):
  i=next(i for i in range(8) if M[i][j]!=v.ZERO);per.append(i);ph.append(v.I_POWERS.index(M[i][j]))
 return {'permutation':per,'phase_i':ph}
reports={}
for name,row in rows.items():
 out=[]
 for (i,g),c in row.items():
  classes=[]
  for label,h in refs.items():
   f=v.word(g,v.adjoint(h))
   if monomial(f):classes.append({'coset':label,'free_left':desc(f)})
  out.append({'input':i,'coef':str(c),'row_support':sorted(set(sum(t!=v.ZERO for t in row) for row in g)),'classes':classes})
 reports[name]=out
def selected(name):
 return [(t['input'],t['coef'],c['coset']) for t in reports[name] for c in t['classes'] if c['coset'] in ('K','C2')]
for name in ('x','y','u','v','t'):
 if selected(name): raise ValueError('unexpected projected old register: '+name)
if selected('r') != [(0,'1','C2'),(0,'2','K')]: raise ValueError('r is not the asserted unit graph')
if [term for term in selected('z') if term[0]==1] != [(1,'1','C2'),(1,'2','K')]: raise ValueError('z y diagonal is not the asserted unit graph')
reports['graph_certificate']={'status':'PASS','old_nonzero_projected_registers':['r','z'],'residue_matrix':'triangular with monomial-unit diagonal coefficients1','target_matrix':'triangular with monomial-unit diagonal coefficients2','target_deficit_in_units_of_dim_A':2,'uniform_additional_paid_call_lower_bound_per_pair':2,'scope':'this literal preparation, fixed uniform word coefficients; not a fixed-width or global small-unit impossibility'}
args.out.write_text(json.dumps(reports,indent=2)+'\n')
print('PASS_STAGGERED_GRAPH_OBSTRUCTION')
