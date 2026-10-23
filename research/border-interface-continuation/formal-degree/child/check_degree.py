#!/usr/bin/env python3
"""Exact finite corroboration of the written Laurent-degree recurrences.

SPDX-License-Identifier: Apache-2.0
Yiyang (@Lyy-iiis), with substantial OpenAI Codex and multi-agent assistance.

Standard library only. These are toy full-matrix identities and witnesses,
not a replay or implementation of the actual native helper supplier.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def ident(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def add(a, b, s=Q(1)):
    return [[x + s * y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, x):
    return [[x * y for y in r] for r in a]


def mul(a, b):
    n = len(a)
    out = [[Q(0)] * n for _ in range(n)]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        out[i][j] += x * y
    return out


def block(a, b, c, d):
    return [x + y for x, y in zip(a, b)] + [x + y for x, y in zip(c, d)]


def F(a, b, e):
    I = ident(len(a))
    E = add(mul(a, b), I, -1)
    return block(add(a, E, -1), scale(E, 1 / e), scale(add(I, b, -1), e), b)


def coherent(a, inverse_a, e):
    n = len(a)
    I = ident(n)
    Z = scale(I, Q(0))
    return (block(a, Z, scale(add(I, inverse_a, -1), e), inverse_a),
            block(inverse_a, Z, scale(add(inverse_a, I, -1), e), a))


def gauge(a, weights, e):
    n = len(a)
    deg = [sum(w for j, w in enumerate(weights) if (i >> j) & 1) for i in range(n)]
    return [[x * e ** (deg[i] - deg[j]) for j, x in enumerate(row)] for i, row in enumerate(a)]


def support_record(a, weights):
    n = len(a)
    deg = [sum(w for j, w in enumerate(weights) if (i >> j) & 1) for i in range(n)]
    terms = [(deg[i] - deg[j], i, j, x) for i, row in enumerate(a) for j, x in enumerate(row) if x]
    off = [t for t in terms if t[1] != t[2]]
    return {'lowest_degree': min(t[0] for t in terms), 'highest_degree': max(t[0] for t in terms),
            'lowest_offdiagonal_degree': min((t[0] for t in off), default=None),
            'offdiagonal_constant_terms': sum(t[0] == 0 for t in off)}


def poly_add(a, b, s=Q(1)):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Q(0)) + s * v
        if not out[k]:
            del out[k]
    return out


def poly_mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, Q(0)) + x * y
    return {k: v for k, v in out.items() if v}


def shifts(a, s):
    return {k + s: v for k, v in a.items()}


def check_inverse(a, b):
    require(mul(a, b) == ident(len(a)), 'actual inverse: A times B must be identity')
    require(mul(b, a) == ident(len(a)), 'actual inverse: B times A must be identity')


def inverse_corruption_control():
    a, b = coherent([[Q(-1)]], [[Q(-1)]], Q(1, 2))
    check_inverse(a, b)
    corrupted = [row[:] for row in b]
    corrupted[1][0] += 1
    try:
        check_inverse(a, corrupted)
    except ValueError as exc:
        require('actual inverse:' in str(exc), 'corruption must fail the inverse identity')
        return {'name': 'changed_actual_inverse_lower_left_coefficient',
                'rejected': True, 'reason': str(exc)}
    raise ValueError('corrupted actual inverse was accepted')


def main(out):
    require(not out.exists(), 'receipt output must be fresh')
    # For q=-1, both fresh opposite orientations coincide at every level.
    # The epsilon=1 matrix and its diagonal gauge encode every Laurent term
    # exactly: each matrix entry has only one possible epsilon exponent.
    A = B = [[Q(-1)]]
    direct_a = direct_b = [[Q(-1)]]
    receipts = []
    for d in range(1, 6):
        A, B = F(A, B, Q(1)), F(B, A, Q(1))
        direct_a, direct_b = F(direct_a, direct_b, Q(1, 2)), F(direct_b, direct_a, Q(1, 2))
        weights = [1] * d
        require(direct_a == gauge(A, weights, Q(1, 2)), 'independent A equals its exact diagonal gauge')
        require(direct_b == gauge(B, weights, Q(1, 2)), 'independent B equals its exact diagonal gauge')
        uniform = support_record(A, weights)
        proper = support_record(A, [1 << j for j in range(d - 1, -1, -1)])
        require(uniform['lowest_degree'] == min(0, 2 - d), 'independent uniform lowest degree')
        require(uniform['highest_degree'] == d, 'independent uniform highest degree')
        require(proper['lowest_degree'] == 0, 'proper border has no negative degrees')
        require(proper['lowest_offdiagonal_degree'] == 1, 'proper border has no offdiagonal constant term')
        require(proper['highest_degree'] == (1 << d) - 1, 'proper border exact highest degree')
        witness_col = (1 << d) - 2
        require(A[1][witness_col] == 2 * (-2) ** (d - 1), 'exact extreme pole witness coefficient')
        require(all(A[i][i] == B[i][i] == -1 for i in range(1 << d)), 'all target diagonal coefficients')
        receipts.append({'depth': d, 'dimension': 1 << d, 'uniform_epsilon': uniform,
                         'proper_depth_weights_inner_to_outer': [1 << j for j in range(d - 1, -1, -1)],
                         'proper_border': proper,
                         'uniform_extreme_pole_witness': {'row': 1, 'column': witness_col,
                                                        'degree': 2 - d, 'coefficient': str(A[1][witness_col])}})
    coherent_records = []
    A = B = [[Q(-1)]]
    direct_a = direct_b = [[Q(-1)]]
    for d in range(1, 6):
        A, B = coherent(A, B, Q(1))
        direct_a, direct_b = coherent(direct_a, direct_b, Q(1, 2))
        check_inverse(direct_a, direct_b)
        require(direct_a == gauge(A, [1] * d, Q(1, 2)), 'coherent A equals its exact diagonal gauge')
        require(direct_b == gauge(B, [1] * d, Q(1, 2)), 'coherent inverse B equals its exact diagonal gauge')
        a_support, b_support = support_record(A, [1] * d), support_record(B, [1] * d)
        require(all(s['lowest_degree'] == 0 and s['highest_degree'] == d
                    and s['lowest_offdiagonal_degree'] == 1
                    and s['offdiagonal_constant_terms'] == 0 for s in [a_support, b_support]),
                'coherent pair is a proper border of exact linear degree')
        coherent_records.append({'depth': d, 'dimension': 1 << d,
                                 'A': a_support, 'actual_inverse_B': b_support,
                                 'both_inverse_products_exact_at_half': True})
    # A separate bounded scalar chronological recycling counterexample:
    # c_{d+1}=(c_d^2-1)/epsilon, c0=2. This is an upper-right F entry,
    # not the synchronized all-owner block recursion above.
    c = {0: Q(2)}
    recycling = []
    for d in range(1, 7):
        c = shifts(poly_add(poly_mul(c, c), {0: Q(1)}, -1), -1)
        require(min(c) == 1 - (1 << d), 'scalar recycling exact lowest degree')
        recycling.append({'depth': d, 'lowest_degree': min(c), 'highest_degree': max(c),
                          'extreme_coefficient': str(c[min(c)])})
    result = {'status': 'PASS_EXACT_TOY_LAURENT_GAUGE_AND_DEGREE_WITNESSES',
              'independent_substitution_q_minus_one': receipts,
              'coherent_actual_inverse_q_minus_one': coherent_records,
              'coordinate_recycling_counterexample': recycling,
              'negative_controls': [inverse_corruption_control()],
              'verification_guard': 'All scientific predicates use explicit require/ValueError and remain active under -O.',
              'verification_history': 'An earlier assert-based optimized run did not execute its scientific predicates; this explicit-guard replay supersedes that evidence.',
              'scope': 'Finite corroboration of FORMAL-DEGREE.md; no native helper, owned-storage, cost or compiler admission.'}
    result['checker_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(result['status'])


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    main(args.out)
