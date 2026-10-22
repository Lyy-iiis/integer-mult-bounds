#!/usr/bin/env python3
"""Exact Gaussian-rational hook audit of the literal staggered five-call word."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import types
sys.dont_write_bytecode = True

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--engine', type=Path, default=Path(__file__).resolve().parents[1]/'vendor/pr4688/verify.py')
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    raw = args.engine.read_bytes()
    if hashlib.sha256(raw).hexdigest() != '99ff0beccd9a4e94cc607e02114d62b8ce0ea57ee00748b07ce0a0af91aec85e':
        raise ValueError('immutable PR4688 engine mismatch')
    m = types.ModuleType('authenticated_pr4688')
    exec(compile(raw, str(args.engine), 'exec'), m.__dict__)
    def mono(perm, exps):
        cols = []
        for x, subset in m.BASIS:
            dest = tuple(perm[t] for t in subset)
            sign = m.wedge_sign(dest)
            a,b = m.I_POWERS[(exps[x] + sum(exps[t] for t in subset)) % 4]
            cols.append({m.INDEX[perm[x],tuple(sorted(dest))]:(sign*a,sign*b)})
        return cols
    def scale(a,c):
        return [{i:m.mul(c,v) for i,v in col.items()} for col in a]
    add, comp = m.add_columns, m.compose
    D = [m.lift_direction(1<<j) for j in range(3)]
    S = mono(list(range(8)), [j.bit_count() for j in range(8)])
    P = comp(S,m.apply_permutation(m.U_PERM,S))
    Q = comp(S,m.apply_permutation(m.V_PERM,S))
    B = add(P,m.scale_columns(Q,2))
    swap21 = [((j&1)|((j&2)<<1)|((j&4)>>1)) for j in range(8)]
    swap02 = [((j&2)|((j&1)<<2)|((j&4)>>2)) for j in range(8)]
    Q2 = comp(S,m.apply_permutation(swap21,S))
    T = mono(swap02,[0]*8)
    N = mono(m.V_PERM,[2*((m.V_PERM[j]>>1)&1) for j in range(8)])
    W = mono(list(range(8)),[2*(j&5).bit_count() for j in range(8)])
    L = comp(N,T)
    # L is a signed monomial, so transpose equals its actual inverse.
    Linv = [{} for _ in range(560)]
    for j,col in enumerate(L):
        for i,v in col.items(): Linv[i][j]=v
    J = comp(N,D[2])
    K = comp(D[2],comp(D[1],D[0]))
    beta = (-4,4)  # inverse of alpha=((1+i)/2)^5=-(1+i)/8
    b2,b3 = m.mul(beta,beta),m.mul(m.mul(beta,beta),beta)
    V = comp(D[0],comp(B,D[0]))
    Rx = comp(Linv,comp(J,comp(W,V)))
    Ry = comp(Linv,comp(J,T))
    if Ry != D[0]: raise ValueError('literal third-call y channel is not C0')
    Tx = comp(D[0],comp(B,Rx))
    Ty = V
    Zx = add(comp(J,comp(W,Tx)),add(scale(comp(J,comp(Q2,Rx)),beta),scale(comp(J,comp(P,V)),b2)))
    Zy = add(scale(comp(J,comp(W,Ty)),b2),scale(comp(J,comp(Q2,D[0])),b3))
    zero = [{} for _ in range(560)]
    # Row scaling by alpha^-j removes only one nonzero scalar from each register.
    stages = [(D[0],zero),(V,zero),(Rx,scale(D[0],b2)),(Tx,scale(Ty,b2)),(Zx,Zy)]
    def joined(a,b,inside):
        left,right=m.project(a,inside),m.project(b,inside)
        width=len(inside)
        return [dict(list(l.items())+[(j+width,v) for j,v in r.items()]) for l,r in zip(left,right)]
    records=[]
    for mask in m.CUTS:
        inside=m.cut_indices(mask)
        rows=[joined(a,b,inside) for a,b in stages]
        targets=joined(K,zero,inside)+joined(zero,K,inside)
        ranks=[m.rank_exact(sum(rows[:j],[])) for j in range(1,6)]
        joint=m.rank_exact(targets+sum(rows,[]))
        rec={'mask':mask,'stages':ranks,'target_joint':joint}
        if ranks != [80,160,240,320,400] or joint != 448: raise ValueError(rec)
        records.append(rec)
        print(json.dumps(rec),flush=True)
    report={'status':'PASS','source_pr4688':'264c4b3cb13c82d171de352ecf60486dfb8d2bd4',
            'arithmetic':'exact Gaussian integer elimination over Q(i)',
            'scope':'literal five-call two-input prefix, width5 eight hook cuts only; no completed unit',
            'normalization':'physical C_j=((1+i)/2)I+((1-i)/2)X_j; each whole register scaled by a nonzero common scalar only',
            'word':['u=C0 x','v=C0(P+2Q)u','r=(NT)^-1 J(Wv+Ty)','t=C0(P+2Q)r','z=J(Wt+Q2r+Pv)'],
            'records':records}
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS_STAGGERED_LITERAL_HOOKS',flush=True)

if __name__=='__main__': main()
