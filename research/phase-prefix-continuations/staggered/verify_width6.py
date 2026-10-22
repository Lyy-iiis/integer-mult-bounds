import types,sys,json,time,argparse,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
import numpy as np
from scipy.sparse import csc_matrix,eye,kron,vstack,hstack
root=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser(description='Optional modular width6 staggered screen; requires NumPy and SciPy');ap.add_argument('--mask',type=int,choices=(2,3),required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
src=root/'vendor/pr4688/verify.py';raw=src.read_bytes()
if hashlib.sha256(raw).hexdigest()!='99ff0beccd9a4e94cc607e02114d62b8ce0ea57ee00748b07ce0a0af91aec85e': raise ValueError('engine hash mismatch')
m=types.ModuleType('m');exec(compile(raw,str(src),'exec'),m.__dict__)
rk=types.ModuleType('rk');src2=root/'modrank.py';rank_bytes=src2.read_bytes()
if hashlib.sha256(rank_bytes).hexdigest()!='f2b2e4c2ce5780d8c7cb0ae20ea0c8dd5f4587611cc6dc6f17b58d7cdb1bb4de': raise ValueError('modular rank helper hash mismatch')
exec(compile(rank_bytes,str(src2),'exec'),rk.__dict__)
p=65537;ii=256;n=4480

def md(a):
 a=a.tocsr();a.data%=p;a.eliminate_zeros();return a

def sparse(cols):
 row=[];col=[];data=[]
 for j,cs in enumerate(cols):
  for i,(a,b) in cs.items():row.append(i);col.append(j);data.append((a+ii*b)%p)
 return csc_matrix((np.array(data,dtype=np.int64),(row,col)),shape=(560,560)).tocsr()
def mono(perm,exps):
 cols=[]
 for x,subset in m.BASIS:
  dest=tuple(perm[t] for t in subset);sg=m.wedge_sign(dest);a,b=m.I_POWERS[(exps[x]+sum(exps[t] for t in subset))%4]
  cols.append({m.INDEX[perm[x],tuple(sorted(dest))]:(sg*a,sg*b)})
 g=csc_matrix((np.array([pow(ii,e%4,p) for e in exps],dtype=np.int64),(perm,list(range(8)))),shape=(8,8)).tocsr()
 return md(kron(sparse(cols),g))
def act(a,b):return md(a@b)
I8=eye(8,dtype=np.int64,format='csr');C=[]
for j in range(3):
 xx=csc_matrix((np.ones(8,dtype=np.int64),([x^(1<<j) for x in range(8)],list(range(8)))),shape=(8,8)).tocsr()
 D8=md(I8-ii*xx);D=sparse(m.lift_direction(1<<j));C.append(md(kron(D,D8)*(-ii*pow(8,-1,p)%p)))
S=mono(list(range(8)),[j.bit_count() for j in range(8)])
U=mono(m.U_PERM,[0]*8);V=mono(m.V_PERM,[0]*8)
P=act(S,act(U,S));Q=act(S,act(V,S));B=md(P+2*Q)
swap21=[((j&1)|((j&2)<<1)|((j&4)>>1)) for j in range(8)]
swap02=[((j&2)|((j&1)<<2)|((j&4)>>2)) for j in range(8)]
Q2=act(S,act(mono(swap21,[0]*8),S));T=mono(swap02,[0]*8)
N=mono(m.V_PERM,[2*((m.V_PERM[j]>>1)&1) for j in range(8)])
W=mono(list(range(8)),[2*(j&5).bit_count() for j in range(8)])
L=act(N,T);Linv=L.T;J=act(N,C[2]);K=act(C[2],act(C[1],C[0]));Z=csc_matrix((n,n),dtype=np.int64).tocsr()
U0=C[0];VF=act(C[0],act(B,C[0]));Rx=act(Linv,act(J,act(W,VF)));Ry=act(Linv,act(J,T))
Tx=act(C[0],act(B,Rx));Ty=act(C[0],act(B,Ry))
Zx=act(J,md(act(W,Tx)+act(Q2,Rx)+act(P,VF)));Zy=act(J,md(act(W,Ty)+act(Q2,Ry)))
states=[(U0,Z),(VF,Z),(Rx,Ry),(Tx,Ty),(Zx,Zy)]
records=[]
for mask in [args.mask]:
 ix=np.array([8*j+k for j in m.cut_indices(mask) for k in range(8)]);out=np.array([j for j in range(n) if j not in set(ix)]);basis=np.zeros((0,len(ix)*2),dtype=np.float64);ranks=[]
 def rows(a,b):return hstack([a[out][:,ix],b[out][:,ix]]).toarray()
 for index,(a,b) in enumerate(states):
  arr=rows(a,b);arr=arr[np.any(arr,axis=1)]
  print('start',index+1,'shape',arr.shape,'oldbasis',basis.shape,flush=True)
  basis=rk.rank(np.vstack([basis,arr]),return_basis=True)
  ranks.append(len(basis));print('stage',index+1,len(basis),flush=True)
 target=np.vstack([rows(K,Z),rows(Z,K)]);target=target[np.any(target,axis=1)]
 joint=rk.rank(np.vstack([basis,target]));print('joint',joint,flush=True)
 if ranks != [640,1280,1920,2560,3200] or joint != 3584: raise ValueError((mask,ranks,joint))
 records.append({'mask':mask,'stages':ranks,'target_joint':joint})
args.out.write_text(json.dumps({'prime':p,'scope':'modular screen on natural H tensor V lifted cut','records':records},indent=2)+'\n')
