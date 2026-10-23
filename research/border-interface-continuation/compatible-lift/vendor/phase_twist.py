#!/usr/bin/env python3
"""Exact order-four phase twist; exploratory local algebra, not admission.

Yiyang (@Lyy-iiis), substantial OpenAI Codex assistance. Apache-2.0.
"""
import argparse
from collections import Counter
import gzip
from hashlib import sha256
import json
from pathlib import Path

SOURCE_SHA = '7679daa4ec6a40f56fc7f0202379a6f454310e94945aba4f48beaaaafb838d05'


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


# Gaussian-integer polynomials in commuting q,d1,d2,epsilon, modulo the
# independent relations q^4=d1^4=d2^4=1. Epsilon remains an indeterminate.
def mono(q=0, d1=0, d2=0, epsilon=0, z=(1, 0)):
    return {} if z == (0, 0) else {(q % 4, d1 % 4, d2 % 4, epsilon): z}


def add(a, b):
    c = dict(a)
    for k, z in b.items():
        old = c.get(k, (0, 0))
        c[k] = (old[0] + z[0], old[1] + z[1])
        if c[k] == (0, 0):
            del c[k]
    return c


def neg(a):
    return {k: (-z[0], -z[1]) for k, z in a.items()}


def mul(a, b):
    c = {}
    for ka, za in a.items():
        for kb, zb in b.items():
            k = tuple((ka[j] + kb[j]) % 4 for j in range(3)) + (ka[3] + kb[3],)
            z = (za[0] * zb[0] - za[1] * zb[1], za[0] * zb[1] + za[1] * zb[0])
            c = add(c, {k: z})
    return c


ZERO = {}
ONE = mono()
IMAG = mono(z=(0, 1))
EYE = [[ONE, ZERO], [ZERO, ONE]]
J = [[ZERO, ONE], [neg(ONE), ZERO]]
JI = [[ZERO, neg(ONE)], [ONE, ZERO]]


def mm(a, b):
    return [[add(mul(a[i][0], b[0][j]), mul(a[i][1], b[1][j]))
             for j in range(2)] for i in range(2)]


def scale(a, s):
    return [[mul(s, x) for x in row] for row in a]


def power(a, n):
    r = EYE
    for _ in range(n):
        r = mm(r, a)
    return r


def transpose(a):
    # ROLE transpose only; physical-transpose hypotheses are stated in NOTES.
    return [[a[j][i] for j in range(2)] for i in range(2)]


def phi(variable=0):
    exps = [0, 0, 0]
    exps[variable] = 1
    q = mono(*exps)
    exps[variable] = -1
    qi = mono(*exps)
    return [[q, ZERO], [mul(mono(epsilon=1), add(ONE, neg(qi))), qi]]


def psi(variable=0):
    return mm([[ONE, ZERO], [ZERO, IMAG]], phi(variable))


def psi_at_fourth_root(k):
    roots = ((1, 0), (0, 1), (-1, 0), (0, -1))
    q = mono(z=roots[k % 4]); qi = mono(z=roots[-k % 4])
    return [[q, ZERO], [mul(IMAG, mul(mono(epsilon=1), add(ONE, neg(qi)))), mul(IMAG, qi)]]


def encoded(a):
    return [[[[*k, *z] for k, z in sorted(x.items())] for x in row] for row in a]


def run(source):
    raw = source.read_bytes()
    need(sha256(raw).hexdigest() == SOURCE_SHA, 'actual round-three source bytes')
    src = json.loads(gzip.decompress(raw))
    c = src['canonical']
    need(c['v'] == 112 and c['h'] == 9, 'retained common interface')
    profiles = {}
    for name, p in src['programs'].items():
        profiles[name] = dict(sorted(Counter(e[-1] for e in p if e[0] in ('climb', 'center')).items()))
    expected = {1:2201, 2:412, 3:510, 4:127, 5:40, 8:8}
    need(set(profiles) == {'forward', 'backward'} and all(p == expected for p in profiles.values()), 'both actual paid profiles')
    helpers = dict(sorted(Counter(len(c['frames'][c['final'][r]]) - len(c['frames'][c['start'][r]])
                                 for r in range(224, 632)).items()))
    need(helpers == {4:28, 7:7, 8:47, 9:326}, 'all actual independent helper widths')
    p = psi()
    need(power(p, 4) == EYE, 'phase twist has exact order dividing four')
    need(add(mul(p[0][0], p[1][1]), neg(mul(p[0][1], p[1][0]))) == IMAG, 'role determinant i')
    d = mono(d1=1, d2=1)
    a = scale(p, d)
    need(power(a, 4) == EYE, 'fresh D1 D2 commute and have order four')
    adj = mm(mm(J, transpose(a)), JI)
    inv = scale(adj, mono(d1=-2, d2=-2, z=(0, -1)))
    need(mm(a, inv) == mm(inv, a) == EYE, 'same-cost formal adjugate inverse')
    need(inv == power(a, 3), 'adjugate agrees with cube, without paying three executions')
    need(mm(mm(transpose(a), J), a) == scale(J, mono(d1=2, d2=2, z=(0, 1))), 'conformal symplectic multiplier')
    controls = {}
    controls['omitted_phase'] = power(phi(), 4) != EYE
    controls['wrong_phase_minus_one'] = power(mm([[ONE, ZERO], [ZERO, neg(ONE)]], phi()), 4) != EYE
    controls['square_is_not_free_diagonal_parity'] = power(p, 2) != [[mono(q=2), ZERO], [ZERO, neg(mono(q=2))]]
    controls['omitted_inverse_minus_i'] = mm(a, scale(adj, mono(d1=-2, d2=-2))) != EYE
    controls['commuting_inputs_do_not_give_commuting_twists'] = mm(p, psi(1)) != mm(psi(1), p)
    need(all(controls.values()), 'all rejecting controls')
    left = mm(psi_at_fourth_root(0), psi_at_fourth_root(1))
    right = mm(psi_at_fourth_root(1), psi_at_fourth_root(0))
    commutator = [[add(left[i][j], neg(right[i][j])) for j in range(2)] for i in range(2)]
    need(commutator == [[ZERO, ZERO], [mono(epsilon=1,z=(0,-2)), ZERO]], 'explicit q1=1,q2=i commutator')
    target = {r: 2*n for r,n in helpers.items()}
    target[17] = 224
    paid = Counter({r: 2*n for r,n in expected.items()})
    split = Counter()
    pieces = {4:(3,1), 5:(3,2), 8:(3,3,2)}
    for r,n in paid.items():
        for s in pieces.get(r, (r,)):
            split[s] += n
    need(dict(sorted(split.items())) == {1:4656,2:920,3:1386}, 'unchanged strict split invoice')
    return {'status':'PASS_LOCAL_PHASE_TWIST_NOT_RECURSIVE_CLOSURE',
            'source_sha256':SOURCE_SHA,
            'source_path':'research/kappa-round3-warp-20261022/ACTUAL-WORD.json.gz',
            'ring':'Z[i][q,d1,d2,epsilon]/(q^4-1,d1^4-1,d2^4-1), all variables commute',
            'psi_fourth_power':encoded(power(p,4)), 'psi_square':encoded(power(p,2)),
            'explicit_commutator_q1_1_q2_i':encoded(commutator),
            'main_endpoint_order_four':True,'adjugate_both_orders':True,
            'helper_order_four_scope':'Each canonical Gaussian helper separately has order four; direct sum needs no cross-helper commutation.',
            'actual_paid_profiles':profiles,'helper_widths':helpers,
            'targets':dict(sorted(target.items())), 'paid_unsplit':dict(sorted(paid.items())),
            'paid_split':dict(sorted(split.items())),
            'extra_rank_calls':0,'extra_forward_scalar_phase_roles':112,
            'controls':controls,
            'limitations':['Endpoint is the retained normalized main/helper interface, not an arbitrary physical-frame native map.',
                           'Physical transpose additionally needs symmetric address blocks and actual whole-supplier transpose implementation.',
                           'Fresh D factors must commute with the central query for the order-four assertion.',
                           'The phase-twisted square is not the retained free parity; unrelated twists need not commute.',
                           'Approximate paid children may destroy the native endpoint factorization; no recursive closure or precision improvement is proved.',
                           'Raw moment root and BIT admission are unchanged; no improved bound is claimed.']}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--source-word', type=Path, required=True)
    ap.add_argument('--regenerate', action='store_true')
    args = ap.parse_args()
    result = run(args.source_word)
    result['checker_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    payload = (json.dumps(result, sort_keys=True, indent=2)+'\n').encode()
    path = Path(__file__).with_name('RESULT.json')
    if args.regenerate:
        path.write_bytes(payload)
    else:
        need(path.read_bytes() == payload, 'frozen exact receipt')
    print(result['status'])
