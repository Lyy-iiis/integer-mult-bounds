#!/usr/bin/env python3
"""Exact phase-twist identities and missing-hypothesis controls.

Prepared by Yiyang with OpenAI Codex assistance. Standard library only.
Not a recursive/native supplier certificate.
"""
import argparse
import json
from pathlib import Path


class P:
    """Z[i][d,q,e]/(d^4-1,q^4-1), sparse exact Gaussian integers."""
    def __init__(self, terms=None):
        self.t = {k:v for k,v in (terms or {}).items() if v != (0,0)}
    @staticmethod
    def cast(x):
        return x if isinstance(x,P) else P({(0,0,0):(int(x),0)})
    def __add__(self, other):
        t=dict(self.t)
        for k,(a,b) in self.cast(other).t.items():
            c,d=t.get(k,(0,0)); t[k]=(a+c,b+d)
        return P(t)
    __radd__=__add__
    def __neg__(self):
        return P({k:(-a,-b) for k,(a,b) in self.t.items()})
    def __sub__(self, other): return self+-self.cast(other)
    def __rsub__(self, other): return self.cast(other)+-self
    def __mul__(self, other):
        t={}
        for (d,q,e),(a,b) in self.t.items():
            for (f,r,s),(c,h) in self.cast(other).t.items():
                k=((d+f)%4,(q+r)%4,e+s)
                x,y=t.get(k,(0,0));t[k]=(x+a*c-b*h,y+a*h+b*c)
        return P(t)
    __rmul__=__mul__
    def __pow__(self,n):
        ans=P.cast(1)
        for _ in range(n): ans=ans*self
        return ans
    def __eq__(self,other): return self.t==self.cast(other).t
    def receipt(self):
        return [{'exponents_d_q_e':list(k),'coefficient_re_im':list(v)}
                for k,v in sorted(self.t.items())]


I=P({(0,0,0):(0,1)})
D=P({(1,0,0):(1,0)})
Q=P({(0,1,0):(1,0)})
E=P({(0,0,1):(1,0)})


def eye(n): return [[P.cast(i==j) for j in range(n)] for i in range(n)]
def zero(n): return [[P.cast(0) for _ in range(n)] for _ in range(n)]
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(c,a): return [[c*x for x in row] for row in a]
def mm(a,b): return [[sum((x*y for x,y in zip(row,col)),P.cast(0)) for col in zip(*b)] for row in a]
def power(a,n):
    ans=eye(len(a))
    for _ in range(n): ans=mm(ans,a)
    return ans
def tr(a): return [list(c) for c in zip(*a)]
def block(a,b,c,d):
    return [x+y for x,y in zip(a,b)]+[x+y for x,y in zip(c,d)]
def require(test,msg):
    if not test: raise ValueError(msg)


def actual(q,d):
    n=len(q); ident=eye(n); z=zero(n)
    psi=block(q,z,scale(I,add(ident,scale(-1,power(q,3)))),scale(I,power(q,3)))
    a=mm(block(d,z,z,d),psi)
    j=block(z,ident,scale(-1,ident),z)
    corr=block(scale(-I,power(d,2)),z,z,scale(-I,power(d,2)))
    alleged=mm(mm(mm(corr,j),tr(a)),scale(-1,j))
    return a,psi,alleged


def run():
    psi=[[Q,P.cast(0)],[I*E*(1-Q**3),I*Q**3]]
    j=[[P.cast(0),P.cast(1)],[P.cast(-1),P.cast(0)]]
    require(power(psi,4)==eye(2),'formal fourth power')
    require(psi[0][0]*psi[1][1]-psi[0][1]*psi[1][0]==I,'formal determinant i')
    a=scale(D,psi)
    adj=mm(mm(j,tr(a)),scale(-1,j))
    inverse=scale(-I*D**2,adj)
    require(mm(a,inverse)==eye(2) and mm(inverse,a)==eye(2),'formal adjugate inverse')
    s=E*(Q**2-Q**3+I*Q-I)
    wanted_square=[[Q**2,P.cast(0)],[s,-Q**2]]
    require(power(psi,2)==wanted_square,'formal square')
    require(s!=0,'nonzero square lower block')
    require(power(a,4)==eye(2),'commuting d fourth power')
    # Avoid fractions: with formal e=2z, the diagonalizer has integral coefficients.
    psi_twice_e=[[Q,P.cast(0)],[2*I*E*(1-Q**3),I*Q**3]]
    r=E*(1-Q)*(1-I*Q**2)
    lower=[[P.cast(1),P.cast(0)],[r,P.cast(1)]]
    lower_inv=[[P.cast(1),P.cast(0)],[-r,P.cast(1)]]
    diagonal=[[Q,P.cast(0)],[P.cast(0),I*Q**3]]
    require(mm(mm(lower,diagonal),lower_inv)==psi_twice_e,'operator-valued diagonalization')

    # Symmetric order-four q,d, common commuting physical eigenbasis.
    q=[[P.cast(1),P.cast(0)],[P.cast(0),I]]
    d=[[P.cast(-1),P.cast(0)],[P.cast(0),-I]]
    good,physical_psi,good_inverse=actual(q,d)
    require(tr(q)==q and tr(d)==d and mm(q,d)==mm(d,q),'control hypotheses')
    require(mm(good,good_inverse)==eye(4),'valid physical transpose')
    require(power(physical_psi,4)==eye(4),'valid physical fourth power')

    # All operators individually symmetric order four, but noncommuting.
    swap=[[P.cast(0),P.cast(1)],[P.cast(1),P.cast(0)]]
    bad,_,bad_inverse=actual(swap,q)
    require(power(swap,4)==eye(2) and tr(swap)==swap,'noncommuting control setup')
    require(mm(q,swap)!=mm(swap,q),'noncommuting control premise')
    require(mm(bad,bad_inverse)!=eye(4),'noncommuting inverse fault escaped')
    require(power(bad,4)!=eye(4),'noncommuting fourth-power fault escaped')
    z=zero(2); j4=block(z,eye(2),scale(-1,eye(2)),z)
    correction=block(scale(-I,power(q,2)),z,z,scale(-I,power(q,2)))
    right_inverse=mm(mm(mm(j4,tr(bad)),scale(-1,j4)),correction)
    require(mm(bad,right_inverse)==eye(4) and mm(right_inverse,bad)==eye(4),'right correction under noncommutation')
    parity=power(q,2)
    require(mm(parity,swap)!=mm(swap,parity),'parity cannot cross arbitrary chart')

    # Order four alone does not identify physical and role transpose.
    rotation=[[P.cast(0),P.cast(-1)],[P.cast(1),P.cast(0)]]
    nonsymmetric,_,ns_inverse=actual(rotation,eye(2))
    require(power(rotation,4)==eye(2) and tr(rotation)!=rotation,'nonsymmetric control setup')
    require(mm(nonsymmetric,ns_inverse)!=eye(4),'physical transpose fault escaped')

    return {
        'status':'PASS_LOCAL_PHASE_TWIST_NOT_RECURSIVE_SUPPLIER',
        'formal_ring':'Z[i][d,q,e]/(d^4-1,q^4-1), commuting d,q,e',
        'formal_identities':['Psi^4=I','det_role(Psi)=i','A^-1=-i*d^2*J*A^(Trole)*J^-1','A^4=I','Psi=L(r)*diag(q,i*q^-1)*L(-r), r=(e/2)*(1-q)*(1-i*q^2)'],
        'Psi_squared_lower_left':s.receipt(),
        'physical_symmetric_commuting_case':'PASS',
        'physical_symmetric_noncommuting_right_correction':'PASS',
        'rejection_controls':{
            'symmetric_order_four_but_noncommuting_d_q':'REJECTED',
            'same_noncommuting_pair_A_fourth_power':'REJECTED',
            'moving_q_squared_parity_across_arbitrary_chart':'REJECTED',
            'physical_transpose_for_nonsymmetric_q':'REJECTED',
            'treating_Psi_squared_as_diagonal_parity':'REJECTED'},
        'unproved':['actual physical transposed supplier','matched paid/target interfaces','recursive closure','finite precision exact inverse']}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',type=Path);ap.add_argument('--compare',type=Path);args=ap.parse_args()
    result=run()
    if args.compare: require(json.loads(args.compare.read_text())==result,'frozen receipt mismatch')
    if args.write: args.write.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'controls':len(result['rejection_controls']),'receipt_compared':bool(args.compare)}))


if __name__=='__main__': main()
