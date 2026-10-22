"""Finite-field row rank via bounded exact-in-double Schur panels (p=65537)."""
import numpy as np
P=65537

def rank(source,block=32,progress=None,return_basis=False):
 a=np.asarray(source,dtype=np.float64).copy()
 a%=P
 nr,nc=a.shape;row=0
 for start in range(0,nc,block):
  stop=min(nc,start+block);initial=row
  L=np.zeros((nr-row,min(block,nr-row)),dtype=np.float64)
  for col in range(start,stop):
   hits=np.flatnonzero(a[row:,col])
   if not len(hits):continue
   j=row+int(hits[0]);k=row-initial
   if j!=row:
    a[[row,j]]=a[[j,row]]
    L[[row-initial,j-initial],:k]=L[[j-initial,row-initial],:k]
   if k and stop<nc:
    a[row,stop:] = (a[row,stop:] - L[k,:k] @ a[initial:row,stop:])%P
   inv=pow(int(a[row,col]),-1,P)
   a[row,col:]=(a[row,col:]*inv)%P
   if row+1<nr:
    factors=a[row+1:,col].copy()
    L[row+1-initial:,k]=factors
    a[row+1:,col:stop]=(a[row+1:,col:stop]-factors[:,None]*a[row,col:stop])%P
   row+=1
   if row==nr:break
  k=row-initial
  if k and row<nr and stop<nc:
   a[row:,stop:]=(a[row:,stop:]-L[k:,:k] @ a[initial:row,stop:])%P
  if progress:progress(row,stop)
  if row==nr:break
 return a[:row] if return_basis else row

if __name__=='__main__':
 rng=np.random.default_rng(20261023)
 def simple(a):
  a=a.copy()%P;rr=0
  for c in range(a.shape[1]):
   nz=np.flatnonzero(a[rr:,c])
   if not len(nz):continue
   j=rr+int(nz[0]);a[[rr,j]]=a[[j,rr]]
   a[rr,c:]=a[rr,c:]*pow(int(a[rr,c]),-1,P)%P
   a[rr+1:,c:]=(a[rr+1:,c:]-a[rr+1:,c,None]*a[rr,c:])%P
   rr+=1
   if rr==len(a):break
  return rr
 for n,m,d in [(40,50,25),(100,55,40),(45,150,30),(150,150,80),(3,4,1),(1,1,0),(50,100,48)]:
  z=(rng.integers(P,size=(n,d),dtype=np.int64)@rng.integers(P,size=(d,m),dtype=np.int64))%P
  actual=rank(z);expect=simple(z)
  if actual!=expect:raise ValueError((n,m,d,actual,expect))
 print('PASS panels versus scalar finite-field elimination')
