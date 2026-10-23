#!/usr/bin/env python3
"""Source-bound chronological Laurent degree upper envelope, not exact degree.

Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance.
SPDX-License-Identifier: Apache-2.0
"""
import argparse
from collections import Counter
from hashlib import sha256
import gzip
import json
from pathlib import Path

PIN = '7679daa4ec6a40f56fc7f0202379a6f454310e94945aba4f48beaaaafb838d05'
SPLIT = {1:[1],2:[2],3:[3],4:[3,1],5:[3,2],8:[3,3,2]}
PROFILE = {1:2201,2:412,3:510,4:127,5:40,8:8}


def need(test, msg):
    if not test:
        raise ValueError(msg)


def owner(r):
    need(r[0] in ['L','C'], 'owner schema')
    return r[1] if r[0]=='L' else 632


def union(a,b):
    c=dict(a)
    for shift,depth in b.items():
        c[shift]=max(c.get(shift,-1),depth)
    return c


def run(program, state):
    state=[dict(s) for s in state]
    profile=Counter(); centers=clears=0
    maxima=[]
    for ix,e in enumerate(program):
        kind=e[0]
        if kind in ('climb','center'):
            a=e[2] if kind=='climb' else 632
            rank=e[-1];profile[rank]+=1
            count=len(SPLIT[rank])
            # Any fresh source supplied by the matched child batch has
            # degree-zero input here and must not be silently absent.
            state[a]=union(state[a], {0:0})
            state[a]={b:k+count for b,k in state[a].items()}
            maxima.append(max(state[a].values(),default=0))
            centers += kind=='center'
        elif kind=='scalar':
            g=e[1];a=owner(g[1]);op=g[0]
            if op=='clear':
                need(a==632,'only owned C0 cleared')
                state[a]={};clears+=1
            elif op=='copy':
                state[a]=dict(state[owner(g[2])])
            elif op=='add':
                if g[3]:state[a]=union(state[a],state[owner(g[2])])
            elif op=='scale':
                if not g[2]:state[a]={}
            else:raise ValueError('unknown scalar')
        else:
            need(kind in ('warp','phase','adapter','residual_adapter'), 'known source event')
    need(dict(profile)==PROFILE,'complete original paid profile')
    need(clears==16 and centers==8,'owned lifetime counts')
    need(not state[632],'owned final state is zero')
    return state, {'events':len(program),'paid_profile':dict(profile),
                   'split_jobs':sum(n*len(SPLIT[r]) for r,n in profile.items()),
                   'owned_centers':centers,'owned_clears':clears,
                   'max_intermediate_split_depth':max(maxima)}


def bound(poly,D):
    if not poly:return None
    return [min(b-k*D for b,k in poly.items()),max(b+k*D for b,k in poly.items())]


def compute(raw):
    need(sha256(raw).hexdigest()==PIN,'source container pin')
    src=json.loads(gzip.decompress(raw))
    # Store each surviving boundary exponent b and largest number k of
    # split-child factors along a structural dependency path. Its safe
    # Laurent support is contained in [b-kD,b+kD]. Scalar cancellations
    # are deliberately not credited.
    st=[{0:0} for _ in range(632)]+[{}]
    for i in range(112):
        st[i]={-1:0,0:0}  # X - epsilon^-1 Y
        st[112+i]={0:0}   # original X, after B S^-1
    lower,lr=run(src['programs']['forward'],st)
    first_helpers=lower[224:632]
    st=lower[:224]+[{0:0} for _ in range(408)]+[{}]
    upper,ur=run(src['programs']['backward'],st)
    for i in range(112,224):
        upper[i]={b+1:k for b,k in upper[i].items()} # S on the final Y
    outputs=upper[:224]+first_helpers+upper[224:632]
    need(len(outputs)==1040,'all main and both helper families')
    envelope={}
    for p in outputs:envelope=union(envelope,p)
    critical=max(envelope.values())
    need(envelope=={-1:22,0:23,1:20},'pinned structural support envelope')
    need(lr['split_jobs']==ur['split_jobs']==3481,'all split factors retained')
    counts=Counter(max(x.values(),default=0) for x in outputs)
    # Independent structural sanity controls.
    need(bound({-1:3,0:2},2)==[-7,5],'Laurent interval control')
    need(union({0:4},{0:2,1:3})=={0:4,1:3},'ADD is max, not sum')
    one=[{0:0} for _ in range(632)]+[{}]
    for e in src['programs']['forward']:
        if e[0]=='scalar' and e[1][0]=='clear':
            need(owner(e[1][1])==632,'CLEAR cannot erase helper')
    return {'status':'PASS_CHRONOLOGICAL_UPPER_ENVELOPE_ONLY',
      'source_sha256':PIN,'source_decoded_sha256':sha256(gzip.decompress(raw)).hexdigest(),
      'target_role_count':1040,'helper_outputs_retained':816,
      'calls':[lr,ur],
      'degree_envelope_boundary_shift_to_max_split_path':envelope,
      'max_split_factors_on_structural_output_path':critical,
      'output_path_depth_histogram':dict(sorted(counts.items())),
      'sample_child_support_bounds':{str(D):[min(bound(x,D)[0] for x in outputs),max(bound(x,D)[1] for x in outputs)] for D in (0,1,2,4,8)},
      'safe_recursion':f'D_1 <= 1; D_(l+1) <= {critical}*D_l for integer D_l >= 1, for this homogeneous nested raw-unit envelope with synchronized lockstep owner matching and degree-zero fresh source inputs. A full mixed precompiler must additionally track complementary-source programs.',
      'scope':'Structural support upper bound, including every retained helper and owned CLEAR. Scalar cancellation and child transpose/inverse coherence are not used. It is NOT a lower bound on actual degree, NOT proof that the constant coefficient is the desired endpoint, and NOT a compiled-bound certificate.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--source-word',type=Path)
    group.add_argument('--source-root',type=Path)
    ap.add_argument('--out',required=True,type=Path)
    a=ap.parse_args()
    source=a.source_word or a.source_root/'research/kappa-round3-warp-20261022/ACTUAL-WORD.json.gz'
    out=compute(source.read_bytes())
    a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['status'],out['max_split_factors_on_structural_output_path'])

if __name__=='__main__':main()
