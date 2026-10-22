"""Independent normalized Gaussian-rational replay of staggered chronology."""
import argparse,types,sys,json,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--arithmetic',type=Path,default=Path(__file__).resolve().parents[1]/'arithmetic.py');ap.add_argument('--out',required=True,type=Path);args=ap.parse_args()
v=types.ModuleType('v');payload=args.arithmetic.read_bytes();
if hashlib.sha256(payload).hexdigest()!='0d277854396e4ceda1e0f26916bd576b6decb474c0692b6671ebf2595283ddb9': raise ValueError('immutable arithmetic mismatch')
exec(compile(payload,str(args.arithmetic),'exec'),v.__dict__)
C=[v.c_letter(j) for j in range(3)];S=v.s_letter(7);U=v.monomial([0,5,2,7,4,1,6,3]);V=v.monomial([0,2,1,3,4,6,5,7]);T=v.monomial([0,4,2,6,1,5,3,7]);V21=v.monomial([0,1,4,5,2,3,6,7])
P=v.word(S,U,S);Q=v.word(S,V,S);Q2=v.word(S,V21,S);W=v.pauli(0,5);N=v.word(v.pauli(0,2),V);L=v.word(N,T);J=v.word(N,C[2]);K=v.word(*C);A=v.pauli(1,3);M=v.monomial([2,0,3,1,4,6,5,7],[0,0,2,2,1,3,3,1])
v.require(v.word(v.adjoint(L),J,T)==C[0],'third y channel is C0')
v.require(v.word(J,W,C[0],P,C[0])==v.word(M,C[2]),'P residual')
v.require(v.word(J,W,C[0],Q,C[0])==v.word(K,A),'Q target')
def kron(a,b):
 n=len(b)
 return tuple(tuple(v.mul(a[i//n][j//n],b[i%n][j%n]) for j in range(len(a)*n)) for i in range(len(a)*n))
def lift(a,f):
 r=((v.ONE,),)
 for _ in range(f):r=kron(r,a)
 return r
records=[]
for f in (1,2):
 c0,c2,p,q,q2,w,n,l,j,t,k,a,mm=[lift(b,f) for b in [C[0],C[2],P,Q,Q2,W,N,L,J,T,K,A,M]]
 d=8**f;I=v.ident(d);Z=v.scale(v.ZERO,I);x=(I,Z);y=(Z,I)
 def left(a,pair):return tuple(v.mm(a,b) for b in pair)
 def add(a,b):return tuple(v.plus(c,e) for c,e in zip(a,b))
 def scale(c,a):return tuple(v.scale(v.q(c),b) for b in a)
 def branch(pair):return add(left(p,pair),scale(2,left(q,pair)))
 u=left(c0,x);vv=left(c0,branch(u));r=left(v.adjoint(l),left(j,add(left(w,vv),left(t,y))));tt=left(c0,branch(r));z=left(j,add(add(left(w,tt),left(q2,r)),left(p,vv)))
 F=v.word(c0,v.plus(p,v.scale(v.q(2),q)),c0)
 rx=v.word(v.adjoint(l),v.plus(v.word(mm,c2),v.scale(v.q(2),v.word(k,a))))
 v.require(vv==(F,Z),'first repaired prefix')
 v.require(r==(rx,c0),'third exact target-plus-residual')
 v.require(tt==(v.word(c0,v.plus(p,v.scale(v.q(2),q)),rx),F),'second repaired prefix')
 zy=v.plus(v.word(mm,c2),v.plus(v.scale(v.q(2),v.word(k,a)),v.word(j,q2,c0)))
 v.require(z[1]==zy,'fifth y exact target-plus-residual')
 # Retaining x,y makes the literal program injective; no inversion is executed.
 rec={'width':f,'dimension':d,'paid_calls':5,'r_x_target_coefficient':'2 L_f^-1 K_f a_f','z_y_target_coefficient':'2 K_f a_f','status':'PASS'}
 records.append(rec);print(json.dumps(rec),flush=True)
result={'status':'PASS','arithmetic':'Gaussian rational Fraction pairs','arithmetic_sha256':hashlib.sha256(payload).hexdigest(),'records':records,'all_width_justification':'The three base identities are single-word equalities; tensor them separately and keep mixing coefficients2 fixed. Width1/2 controls do not alone prove all-width ranks.','scope':'literal five-call prefix and target-coset entrances; no completed unit'}
args.out.write_text(json.dumps(result,indent=2)+'\n')
