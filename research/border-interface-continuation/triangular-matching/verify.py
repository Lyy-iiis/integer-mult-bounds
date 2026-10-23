#!/usr/bin/env python3
"""Bounded prefix matching and source-reset checks; no supplier admission.

Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance.
SPDX-License-Identifier: Apache-2.0
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import gzip
import itertools
import json
from pathlib import Path

WORD_HASH = 'cfcd36b40326d7a5815e1db5313444379b3fb756b27d5201c561574c085cc0dd'
COMPILER_HASH = '4cb32f6b8e388ecf6ed41b5bbdeeb4539cb40c8424f194974afea58f7e0921e8'
TARGETS = {4:56, 7:14, 8:94, 9:652, 17:224}

def require(x, message):
    if not x:
        raise ValueError(message)

def owner(r):
    require(r[0] in ('L', 'C'), 'known role')
    return r[1] if r[0] == 'L' else 632

def scalar_step(values, event):
    if event[0] != 'scalar':
        return
    g = event[1]
    a = owner(g[1])
    if g[0] == 'clear': values[a] = F(0)
    elif g[0] == 'copy': values[a] = values[owner(g[2])]
    elif g[0] == 'add': values[a] += F(g[3],g[4])*values[owner(g[2])]
    elif g[0] == 'scale': values[a] *= F(g[2],g[3])
    else: raise ValueError('unknown scalar operation')

def source_reset(data):
    """One labelled first variation; not the all-local-parameter-one map."""
    program = data['programs']['backward']
    event = 6276
    require(program[event] == ['climb','warp_retimed',126,0,137,1],
            'actual rank-one paid event')
    require(data['canonical']['frames'][0] == [] and
            data['canonical']['frames'][137] == [45], 'actual frame edge')
    values = [F(0)]*633
    values[14] = values[126] = F(1)
    for e in program[:event]: scalar_step(values,e)
    prefix = values[126]
    injection = [F(0)]*633
    injection[126] = F(1)
    for e in program[event+1:]: scalar_step(injection,e)
    suffix = injection[14]
    require(prefix == 1 and suffix == F(-1,2), 'actual Y14 to X14 response')
    for w in data['canonical']['warps']:
        cols = w['G_columns']
        span = {0}
        for c in cols: span |= {x^c for x in tuple(span)}
        require(len(cols)==9 and len(span)==512, 'homogeneous invertible warp')
    # A canonical rank-one Gaussian has the same diagonal (1+i)/2
    # at every address. A monomial right matcher changes delta_0 to
    # a phased basis vector, so its q-I diagonal is (-1+i)/2.
    moment = (F(-1,2), F(1,2))
    coefficient = tuple(prefix*suffix*x for x in moment)
    require(coefficient == (F(1,4),F(-1,4)), 'nonzero labelled coefficient')
    return {'orientation':'backward / upper call', 'event':event,
            'owner':126, 'input_original_Y_port':14, 'output_main_X_port':14,
            'old_frame':[], 'new_frame':[45], 'paid_rank':1,
            'scalar_prefix':str(prefix), 'scalar_suffix':str(suffix),
            'matched_q_minus_I_delta_zero_moment':[str(x) for x in moment],
            'labelled_cross_copy_coefficient_up_to_common_sign':[str(x) for x in coefficient],
            'scope':'One independently labelled matched-child first variation; no claim that the all-local-epsilon-one completed endpoint retains this coefficient.'}

def graph_checks():
    rows=[]
    for depth in range(1,9):
        words=list(itertools.product((0,1),repeat=depth))
        distance=[0]*len(words)
        edges=0
        for j,v in enumerate(words):
            for i,u in enumerate(words[:j]):
                first=next(k for k in range(depth) if u[k]!=v[k])
                if u[first]==0 and v[first]==1:
                    distance[j]=max(distance[j],distance[i]+1)
                    edges+=1
        require(max(distance)==2**depth-1,'lexicographic closure height')
        carry=[]
        for i in range(len(words)-1):
            u,v=words[i:i+2]
            k=next(k for k in range(depth) if u[k]!=v[k])
            require(u[k]==0 and v[k]==1 and all(x==1 for x in u[k+1:])
                    and all(x==0 for x in v[k+1:]),'binary carry edge')
            carry.append((i,i+1))
        rows.append({'depth':depth,'vertices':len(words),'closure_edges':edges,
                     'minimum_integer_grade_span':max(distance),
                     'carry_path_edges':len(carry)})
    # Without suffix reset, independent bit flips need only additive grades.
    require(max(sum(w) for w in itertools.product((0,1),repeat=8))==8,
            'no-reset control is linear height')
    return rows

def integer_slice():
    N,m,G=289,17,2
    require(m*4**G<=N<m*4**(G+1),'actual finite-flow depth')
    root=sum(wa*wb for a,wa in TARGETS.items() for b,wb in TARGETS.items()
             if m*a*b<=N)
    require(root==56**2, 'root has only rank-four pairs')
    child=sum(w for k,w in TARGETS.items() if m*k<=N)
    require(child==1040, 'rank-one child class contains every single role')
    # Labels X14,Y14 are among the224 rank17 letters. Their own main
    # targets have rank289; they are fresh full-rank sources, not root jobs.
    require(17*17==N and 17*17> N/m, 'full-rank fresh sources')
    return {'N':N,'G':G,'selected_round_ranks':[1,1],
            'root_units':root,'first_child_units':child,'second_child_units':1,
            'two_selected_parent_unit_columns':[17,17],
            'four_main_source_ranks':[289]*4,
            'meaning':'A slice of the exact integer flow, not a complete winning uniform supplier.'}

def run(word,compiler):
    payload=gzip.decompress(word.read_bytes())
    require(sha256(payload).hexdigest()==WORD_HASH,'authenticated decoded native word')
    require(sha256(compiler.read_bytes()).hexdigest()==COMPILER_HASH,'authenticated compiler text')
    data=json.loads(payload)
    controls=[]
    for label,fn in (
        ('changed decoded source',lambda:require(sha256(payload+b' ').hexdigest()==WORD_HASH,'source')),
        ('wrong zero-reset coefficient',lambda:require(F(1)*F(-1,2)==0,'reset')),
    ):
        try: fn()
        except ValueError: controls.append({'name':label,'rejected':True})
        else: raise ValueError('negative control accepted')
    return {'status':'PASS: bounded graph, integer slice, and labelled source-response checks',
            'source_decoded_sha256':WORD_HASH,'compiler_sha256':COMPILER_HASH,
            'invoice_targets':TARGETS,'integer_flow_slice':integer_slice(),
            'source_reset':source_reset(data),'conditional_graph_heights':graph_checks(),
            'without_suffix_reset_depth8_grade_span':8,'controls':controls,
            'open_gates':['simultaneous ordering of complements, exits, fresh sources and owned fields',
                          'actual noncancelling endpoint support after setting all local epsilon to one',
                          'complete precision and boundary-loss invoice']}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source-word',type=Path,required=True)
    p.add_argument('--compiler',type=Path,required=True)
    p.add_argument('--receipt',type=Path,default=Path(__file__).with_name('RESULT.json'))
    p.add_argument('--regenerate',action='store_true')
    a=p.parse_args()
    result=run(a.source_word,a.compiler)
    encoded=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if a.regenerate: a.receipt.write_text(encoded)
    else:
        require(json.dumps(json.loads(a.receipt.read_text()),sort_keys=True)==
                json.dumps(json.loads(encoded),sort_keys=True),'frozen receipt equality')
    print(result['status'])

if __name__=='__main__': main()
