#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance.
"""Exact, stdlib-only certificate for the restricted two-query obstruction."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
NAMES = ('q', 'a', 'b', 'u', 'v', 'w', 'z', 'c', 'chi', 'epsilon')
ZERO = (0,) * len(NAMES)


def require(condition, message):
    if not condition:
        raise ValueError(message)


class Ring:
    def __init__(self, order):
        self.order = order

    def clean(self, terms):
        result = {}
        for powers, coefficient in terms:
            if self.order:
                powers = (powers[0] % self.order,) + powers[1:]
            result[powers] = result.get(powers, 0) + coefficient
        return {p: c for p, c in result.items() if c}

    def constant(self, n):
        return self.clean([(ZERO, n)])

    def var(self, name, power=1):
        powers = list(ZERO)
        powers[NAMES.index(name)] = power
        return self.clean([(tuple(powers), 1)])

    def add(self, *polynomials):
        return self.clean(item for p in polynomials for item in p.items())

    def neg(self, p):
        return {powers: -coefficient for powers, coefficient in p.items()}

    def mul(self, *polynomials):
        out = self.constant(1)
        for p in polynomials:
            out = self.clean((tuple(a+b for a, b in zip(x, y)), c*d)
                             for x, c in out.items() for y, d in p.items())
        return out

    def mm(self, a, b):
        return [[self.add(*(self.mul(a[i][k], b[k][j]) for k in range(2)))
                 for j in range(2)] for i in range(2)]

    def det(self, a):
        return self.add(self.mul(a[0][0], a[1][1]),
                        self.neg(self.mul(a[0][1], a[1][0])))

    def even(self, a):
        return [[{p: c for p, c in entry.items() if p[0] % 2 == 0}
                 for entry in row] for row in a]


def check_ring(order):
    r = Ring(order)
    add, mul, neg, mm = r.add, r.mul, r.neg, r.mm
    o, zero = r.constant(1), r.constant(0)
    q, qi = r.var('q'), r.var('q', -1)
    a, b, u, v, w, z, c, chi, eps = [r.var(n) for n in NAMES[1:]]
    identity = [[o, zero], [zero, o]]
    null = [[zero, zero], [zero, zero]]
    upper = lambda x: [[o, x], [zero, o]]
    lower = lambda x: [[o, zero], [x, o]]
    middle = [[u, v], [w, z]]
    word = mm(mm(upper(mul(a, q)), middle), lower(mul(b, qi)))
    expanded = [[add(u, mul(a, b, z), mul(a, q, w), mul(b, qi, v)),
                 add(v, mul(a, q, z))], [add(w, mul(b, qi, z)), z]]
    checks = []

    def check(name, condition):
        require(condition, name)
        checks.append(name)

    check('universal_two_query_expansion', word == expanded)
    check('universal_even_component', r.even(word) == [[add(u, mul(a,b,z)), v], [w,z]])
    check('two_query_determinant', r.det(word) == r.det(middle))
    diagonal = [[q, zero], [zero, mul(chi, qi)]]
    target = mm(mm(lower(c), diagonal), lower(neg(c)))
    check('triangular_target', target == [[q,zero], [mul(c,add(q,neg(mul(chi,qi)))),mul(chi,qi)]])
    check('target_purely_odd', r.even(target) == null)
    check('target_determinant', r.det(target) == chi)
    three = mm(mm(mm(upper(q), lower(neg(qi))), upper(q)), [[zero,neg(o)],[o,zero]])
    check('three_query_positive_control', three == [[q,zero],[zero,qi]])
    border = [[q,zero], [mul(chi,eps,add(o,neg(qi))),mul(chi,qi)]]
    check('phased_border_even_residual', r.even(border) == [[zero,zero],[mul(chi,eps),zero]])
    # False claimed identities are rejected by nonzero exact polynomial witnesses.
    controls = {
        'discard_two_query_even_component': word != [[add(mul(a,q,w),mul(b,qi,v)),mul(a,q,z)],[mul(b,qi,z),zero]],
        'omit_third_query': mm(mm(upper(q),lower(neg(qi))),[[zero,neg(o)],[o,zero]]) != [[q,zero],[zero,qi]],
        'call_phased_border_purely_odd': r.even(border) != null,
    }
    require(all(controls.values()), 'a false identity was accepted')
    return {'ring': 'formal_Laurent' if order is None else 'q4_equals_1',
            'identities': checks, 'rejecting_controls': controls}


def check_noncommutative():
    # Reduce words in the free algebra by the monomial relations NN=MM=0.
    terms = [('N', 1), ('NNM', 1), ('N', -1)]
    reduced = {}
    for word, coefficient in terms:
        if 'NN' in word or 'MM' in word:
            continue
        reduced[word] = reduced.get(word, 0) + coefficient
    reduced = {word: c for word, c in reduced.items() if c}
    require(not reduced, 'N(I+NM)-N failed')
    return {'identity': 'N(I+NM)=N modulo N^2=M^2=0',
            'reduced_difference': reduced,
            'scope': 'any positive matrix dimension; purely odd target; invertible even boundaries'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path, help='fresh receipt path')
    args = parser.parse_args()
    require(not args.output.exists(), 'output must be fresh')
    script = Path(__file__).resolve()
    proof = script.with_name('PROOF.md')
    before = {'checker_sha256': digest(script), 'proof_sha256': digest(proof)}
    result = {'schema': 'two-query-even-obstruction-v1',
              'status': 'PASS_RESTRICTED_EXACT_TWO_QUERY_OBSTRUCTION',
              **before, 'commutative_checks': [check_ring(None), check_ring(4)],
              'noncommutative_check': check_noncommutative(),
              'limitations': ['local exact algebra only; no native or recursive compiler admission',
                              'odd-character determinant extension is two by two only',
                              'no bound improvement or free third-query claim']}
    require(before == {'checker_sha256': digest(script), 'proof_sha256': digest(proof)},
            'input changed during verification')
    with args.output.open('x', encoding='utf-8') as out:
        json.dump(result, out, sort_keys=True, indent=2)
        out.write('\n')
    print(result['status'])


if __name__ == '__main__':
    main()
