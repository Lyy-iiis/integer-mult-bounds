#!/usr/bin/env python3
"""Exact Laurent two-level substitution diagnostic; no exponent claim.

SPDX-License-Identifier: Apache-2.0
Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance.
All calculations use rational coefficients. No q^2 or q^4 relation is imposed.
"""
import argparse
import json
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import sys

sys.dont_write_bytecode = True


def require(value, message):
    if not value:
        raise ValueError(message)


# Monomial exponents are (q, outer epsilon, inner delta).
def mon(c=1, q=0, e=0, d=0):
    return {(q, e, d): F(c)} if c else {}


def add(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, F(0)) + value
        if not out[key]:
            del out[key]
    return out


def scale(a, c):
    return {key: value * c for key, value in a.items() if value * c}


def mul(a, b):
    out = {}
    for x, v in a.items():
        for y, w in b.items():
            key = tuple(i + j for i, j in zip(x, y))
            out[key] = out.get(key, F(0)) + v * w
    return {key: value for key, value in out.items() if value}


def total(values):
    out = {}
    for value in values:
        out = add(out, value)
    return out


def mm(a, b):
    return [[total(mul(x, y) for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def eye(n):
    return [[mon(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(n):
    return [[{} for _ in range(n)] for _ in range(n)]


def ms(a, c):
    return [[mul(c, x) for x in row] for row in a]


def ma(a, b, sign=1):
    return [[add(x, scale(y, sign)) for x, y in zip(r, s)]
            for r, s in zip(a, b)]


def block(a, b, c, d):
    return [x + y for x, y in zip(a, b)] + [x + y for x, y in zip(c, d)]


def product(items):
    out = eye(len(items[0]))
    for item in items:
        out = mm(out, item)
    return out


def encode(a):
    return [[[[*key, str(v)] for key, v in sorted(x.items())]
             for x in row] for row in a]


def specialize_scale(a, power):
    """Substitute delta = epsilon**power without changing q."""
    return [[total(mon(v, q=q, e=e + power*d)
                   for (q, e, d), v in x.items()) for x in row] for row in a]


def positive_order(a):
    return all(e > 0 for row in a for x in row for q, e, d in x)


def constant_at_q_minus_one(a):
    return [[sum(v * (-1 if q % 2 else 1)
                 for (q, e, d), v in x.items() if e == 0 and d == 0)
             for x in row] for row in a]


def numeric_transpose_control():
    """An ordinary physical transpose differs from role-only adjugation."""
    def num_mm(a, b):
        return [[sum(x*y for x, y in zip(row, col))
                 for col in zip(*b)] for row in a]
    def num_eye(n):
        return [[F(i == j) for j in range(n)] for i in range(n)]
    def num_add(a, b, s=1):
        return [[x + s*y for x, y in zip(r, t)] for r, t in zip(a, b)]
    def num_scale(a, c):
        return [[c*x for x in row] for row in a]
    q = [[F(1), F(1)], [F(0), F(1)]]
    qi = [[F(1), F(-1)], [F(0), F(1)]]
    i = num_eye(2)
    z = [[F(0), F(0)], [F(0), F(0)]]
    residual = num_scale(num_add(i, qi, -1), F(1, 2))
    phi = block(q, z, residual, qi)
    true_inverse = block(qi, z, num_scale(residual, -1), q)
    j = block(z, i, num_scale(i, -1), z)
    jt = num_scale(j, -1)
    physical_transpose = [list(row) for row in zip(*phi)]
    candidate = num_mm(num_mm(j, physical_transpose), jt)
    require(num_mm(phi, true_inverse) == num_eye(4), 'Actual numeric inverse')
    require(candidate != true_inverse, 'Non-symmetric physical transpose control')
    return {'q': [[str(x) for x in row] for row in q],
            'epsilon': '1/2',
            'physical_transpose_signed_swap_is_not_inverse': True}


def run():
    i, z = eye(2), zeros(2)
    q, qi = mon(q=1), mon(q=-1)
    residual = add(mon(d=1), mon(-1, q=-1, d=1))
    m = [[q, {}], [residual, qi]]
    mi = [[qi, {}], [scale(residual, -1), q]]
    fresh_opposite = [[qi, {}],
                      [add(mon(d=1), mon(-1, q=1, d=1)), q]]
    require(mm(m, mi) == i and mm(mi, m) == i,
            'Coherent inverse of the SAME approximate realization')

    def outer(n):
        s = block(i, z, z, ms(i, mon(e=1)))
        si = block(i, z, z, ms(i, mon(e=-1)))
        u = block(i, m, z, i)
        lower = block(i, z, ms(n, mon(-1)), i)
        b = block(i, ms(i, mon(-1)), i, z)
        return product([s, u, lower, b, si])

    coherent = outer(mi)
    expected = block(m, z, ms(ma(i, mi, -1), mon(e=1)), mi)
    require(coherent == expected, 'Literal operator identity for coherent inverse')
    bad = outer(fresh_opposite)
    bad_upper_right = [row[2:] for row in bad[:2]]
    defect = total([mon(2, q=-1, e=-1, d=1),
                    mon(-1, e=-1, d=1), mon(-1, q=-2, e=-1, d=1)])
    require(bad_upper_right == [[{}, {}], [defect, {}]],
            'Exact unsafe coefficient delta/epsilon q^-1 (2-q-q^-1)')
    target = [[mon(q=v) if j == k else {} for j in range(4)]
              for k, v in enumerate((1, -1, -1, 1))]
    coherent_error = ma(coherent, target, -1)
    bad_error = ma(bad, target, -1)
    require(positive_order(specialize_scale(coherent_error, 1)),
            'Coherent inverse has positive error order at equal scales')
    require(positive_order(specialize_scale(bad_error, 2)),
            'Nested smaller scale cures this literal two-level endpoint')
    constant = constant_at_q_minus_one(specialize_scale(bad_error, 1))
    require(constant[1][2] == -4 and
            sum(x != 0 for row in constant for x in row) == 1,
            'Equal-scale fresh-opposite defect survives as exactly minus four')
    physical_control = numeric_transpose_control()
    controls = {
        'fresh_opposite_is_not_the_actual_inverse': mm(m, fresh_opposite) != i,
        'equal_scales_do_not_remove_fresh_opposite_defect':
            not positive_order(specialize_scale(bad_error, 1)),
        'finite_coherent_endpoint_is_not_exact_target': coherent != target,
        'physical_transpose_without_child_coherence_is_rejected':
            physical_control['physical_transpose_signed_swap_is_not_inverse'],
    }
    require(all(controls.values()), 'All four targeted controls reject')
    return {
        'status': 'PASS_EXACT_TWO_LEVEL_LAURENT_DIAGNOSTIC_NOT_A_BOUND',
        'ring': 'Q[q,q^-1,epsilon,epsilon^-1,delta]',
        'inner': encode(m), 'actual_inner_inverse': encode(mi),
        'fresh_opposite_inner': encode(fresh_opposite),
        'coherent_endpoint': encode(coherent),
        'unsafe_upper_right': encode(bad_upper_right),
        'target_limit': encode(target),
        'equal_scale_q_minus_one_constant_error':
            [[str(x) for x in row] for row in constant],
        'coherent_inverse_equal_scales_positive_error_order': True,
        'fresh_opposite_delta_equals_epsilon_squared_positive_error_order': True,
        'physical_transpose_control': physical_control,
        'controls': controls,
        'scope': 'Exact literal Laurent query-core substitution. Fresh opposite orientation '
                 'is not an inverse of the same approximate child. True inverse or a '
                 'strictly smaller inner scale repairs this two-level endpoint only. '
                 'This does not verify native owned-space transposition, the recursive '
                 'paid-word compiler, precision/storage costs, or a multiplication bound.'
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    require(not args.out.exists(), 'Fresh receipt path required')
    result = run()
    result['checker_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'status': result['status'], 'controls': len(result['controls'])}))
