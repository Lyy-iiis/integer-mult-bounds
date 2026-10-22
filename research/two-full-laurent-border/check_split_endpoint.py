#!/usr/bin/env python3
"""Literal source-Cgate proof that the direct paid splitter preserves phases.
SPDX-License-Identifier: Apache-2.0
Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import sys
import types
sys.dont_write_bytecode=True
PIN='2982ead07721e83358dc67c6f49c2b4c16a236a6bebdfd72f58221be1f5d0962'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    raw=path.read_bytes()
    require(sha256(raw).hexdigest()==PIN,'phase-preserving engine pin')
    mod=types.ModuleType('paid_split_exact_engine')
    sys.modules[mod.__name__]=mod
    exec(compile(raw,str(path),'exec'),mod.__dict__)
    return mod


def run(ce):
    rules={4:[3,1],5:[3,2],8:[3,3,2]}
    rows=[]
    for rank,parts in rules.items():
        for f in (1,2,3):
            n=rank*f
            whole=ce.fourier(n)
            split=ce.ident(n)
            offset=0
            piece_ops=[]
            for part in parts:
                axes=range(offset,offset+part*f)
                op=ce.fourier(n,axes)
                split=split.then(op)
                piece_ops.append(op)
                offset+=part*f
            require(offset==n, 'every original coordinate assigned once')
            require(split.circuit==whole.circuit and split.tab==whole.tab,
                    'identical literal circuit, including absolute phases')
            inverse_split=ce.ident(n)
            for op in reversed(piece_ops):
                inverse_split=inverse_split.then(op.adjoint())
            require(inverse_split.circuit==whole.adjoint().circuit
                    and inverse_split.tab==whole.adjoint().tab,
                    'inverse orientation reverses both pieces and each circuit')
            # Nontrivial illustrative monomial boundaries are executed once,
            # around the complete replacement, never once per split piece.
            swap_rows=tuple(1<<((i+1)%n) for i in range(n))
            left=ce.perm(n,swap_rows).then(ce.xgate(n,1))
            right=ce.diag(n,tuple(1<<i for i in range(n)))
            wrapped=right.then(whole).then(left)
            wrapped_split=right.then(split).then(left)
            require(wrapped.circuit==wrapped_split.circuit,
                    'original whole-job normalizers retained once')
            columns=0
            if f==1:
                for col in range(1<<n):
                    require(split.zero_state(col)==whole.zero_state(col),
                            'every complex basis column, exact numerator/denominator')
                    columns+=1
            rows.append({'rank':rank,'fiber_columns':f,'pieces':parts,
                         'literal_forward_and_inverse_circuits_equal':True,
                         'nontrivial_whole_boundaries_unchanged':True,
                         'explicit_basis_columns':columns})
    full=ce.fourier(8)
    missing=ce.fourier(8,range(6))
    wrong_sign=ce.fourier(8,range(6)).then(ce.fourier(8,range(6,8)).adjoint())
    controls={
        'drop_last_rank2_piece_rejected':full.tab!=missing.tab,
        'wrong_last_piece_orientation_rejected':full.tab!=wrong_sign.tab,
        'duplicate_whole_normalizer_changes_endpoint':
            ce.fourier(4).then(ce.xgate(4,1)).tab != ce.fourier(4).tab,
    }
    require(all(controls.values()), 'targeted split controls')
    return {'status':'PASS_LITERAL_PHASE_PRESERVING_PAID_SPLIT',
            'engine_sha256':PIN,'split_rules':rules,'rows':rows,'controls':controls,
            'all_column_argument':'For any positive f the contiguous coordinate sets of sizes part*f partition the original rank*f axes. In the pinned engine fourier is exactly the ordered product of Cgate(axis); concatenating the piece circuits gives the same literal list. Reverse list and adjoint each Cgate for inverse orientation. Therefore every phase and every input column agree for arbitrary f, not only tested widths.',
            'source_contract':'Retain the original left/right whole-job normalizers around the entire replacement. The inherited lower_child implementation returns compiled=rmon.then(fourier(n,range(r))).then(lmon). Splitting its middle Fourier axes retains exactly those boundary calls.',
            'scope':'Exact canonical paid endpoint replacement under the retained native whole-job-normalizer contract. This does not replay every original native transport, prove the border precision model, or assert a multiplication bound.'}


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--engine',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    require(not args.out.exists(),'fresh receipt')
    result=run(load(args.engine))
    result['checker_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'cases':len(result['rows']),
                      'basis_columns':sum(r['explicit_basis_columns'] for r in result['rows'])}))
