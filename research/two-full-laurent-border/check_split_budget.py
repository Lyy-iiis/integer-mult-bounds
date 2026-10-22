#!/usr/bin/env python3
"""Exact conditional moment screen for the two-full Laurent border.

SPDX-License-Identifier: Apache-2.0
Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance.
This checks an invoice, not the size-dependent precision/compiler premise.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def log_atanh(z):
    require(0 <= z <= F(1, 3), "bounded positive atanh argument")
    n = 48
    low = 2 * sum((z**(2*j+1) / (2*j+1) for j in range(n)), F())
    high = low + 2*z**(2*n+1) / ((2*n+1)*(1-z*z))
    return low, high


@lru_cache(None)
def log_integer(r):
    require(isinstance(r, int) and r >= 1, "positive integer rank")
    k = r.bit_length()-1
    x = F(r, 2**k)
    lo, hi = log_atanh((x-1)/(x+1))
    l2, h2 = log_atanh(F(1, 3))
    return lo+k*l2, hi+k*h2


def exp_negative(x):
    require(0 <= x < 1, "alternating-series range")
    term = total = F(1)
    for j in range(1, 17):
        term *= -x/j
        total += term
    return total + term*(-x/17), total


def power(r, c):
    lo, hi = log_integer(r)
    return r*exp_negative(c*hi)[0], r*exp_negative(c*lo)[1]


def moment(coeff, c):
    lo = hi = F()
    for r, count in coeff.items():
        a, b = power(r, c)
        lo += count*(a if count >= 0 else b)
        hi += count*(b if count >= 0 else a)
    return lo, hi


def outward(x, places=30):
    scale = 10**places
    k = x.numerator*scale//x.denominator
    return str(F(k, scale)), str(F(k+1, scale))


def interval(values):
    return [outward(values[0])[0], outward(values[1])[1]]


def run():
    h = {4:28, 7:7, 8:47, 9:326}
    p = {1:2201, 2:412, 3:510, 4:127, 5:40, 8:8}
    rules = {1:[1], 2:[2], 3:[3], 4:[3,1], 5:[3,2], 8:[3,3,2]}
    target = Counter({r:2*n for r,n in h.items()})
    target[17] += 224
    old = Counter({r:2*n for r,n in p.items()})
    paid = Counter()
    for r,n in old.items():
        require(sum(rules[r]) == r, "every split preserves rank mass")
        for piece in rules[r]:
            paid[piece] += n
    require(dict(paid) == {1:4656,2:920,3:1386}, "literal split invoice")
    require(max(paid) < min(target), "strict rank separation")
    require(sum(r*n for r,n in old.items()) == sum(r*n for r,n in paid.items()),
            "complete paid mass preserved")
    coeff = {r:target[r]-paid[r] for r in set(target)|set(paid)}
    original_coeff = {r:target[r]-old[r] for r in set(target)|set(old)}
    c = F(34, 10000)
    split_at_c = moment(coeff,c)
    original_at_c = moment(original_coeff,c)
    require(split_at_c[0] > 28, "fully split strict invoice remains positive at .0034")
    # Refine a predetermined safe coarse bracket using exact rational signs.
    a,b = F('0.0048568755'), F('0.0048568757')
    require(moment(coeff,a)[0] > 0 and moment(coeff,b)[1] < 0, "coarse root bracket")
    scale = 10**23
    left,right = int(a*scale),int(b*scale)
    while right-left > 1:
        middle = (left+right)//2
        lo,hi = moment(coeff,F(middle,scale))
        require(lo > 0 or hi < 0, "enclosure resolves bisection sign")
        if lo > 0:
            left=middle
        else:
            right=middle
    lower,upper=F(left,scale),F(right,scale)
    low_sign,high_sign=moment(coeff,lower),moment(coeff,upper)
    require(low_sign[0] > 0 and high_sign[1] < 0, "exact root enclosure")
    # Divide F(C) by (7/2)^(1-C). Every positive rank exceeds 7/2 and
    # every negative rank lies below it, so its derivative is strictly
    # negative. This proves uniqueness without numerically differentiating.
    separator=F(7,2)
    require(all((n>0 and r>separator) or (n<0 and r<separator)
                for r,n in coeff.items()), "strict signed separator")
    controls={
        'drop_last_rank2_split_piece_detected': sum([3,3]) != 8,
        'unsplit_rank4_breaks_separation': not max(set(paid)|{4}) < min(target),
        'suppress_all_split_penalty_detected': original_at_c[0] > split_at_c[1],
    }
    require(all(controls.values()), "targeted incorrect-invoice controls")
    return {
        'status':'PASS_EXACT_SPLIT_INVOICE_ONLY_NOT_A_BOUND',
        'profile_source':{'pr':4610,'head':'0ce1b5c9fb7163d0b2f0ac3db95fc418dbbcec62',
                          'authentication_scope':'Profile supplied by independently authenticated parent source audit; this arithmetic checker does not rerun the native source.'},
        'single_call_helpers':h,'single_call_paid':p,
        'target':dict(target),'paid_before_split':dict(old),'split_rules':rules,
        'paid_after_split':dict(paid),'paid_rank_mass':sum(r*n for r,n in paid.items()),
        'target_rank_mass':sum(r*n for r,n in target.items()),
        'strict_rank_separation':{'max_paid':max(paid),'min_target':min(target)},
        'test_C':str(c),'split_moment_interval':interval(split_at_c),
        'unsplit_moment_interval':interval(original_at_c),
        'split_penalty_interval':interval((original_at_c[0]-split_at_c[1],original_at_c[1]-split_at_c[0])),
        'root_lower':str(lower),'root_upper':str(upper),
        'root_decimal_lower':format(float(lower),'.17g'),
        'root_at_lower_interval':interval(low_sign),'root_at_upper_interval':interval(high_sign),
        'unique_root_separator':str(separator),
        'method':'48-term positive atanh logarithm with geometric remainder, alternating exp(-x) bounds at degrees17/16, exact Fraction arithmetic.',
        'controls':controls,
        'scope':'This removes the raw invoice need for tensor powering/completion. A paid Gaussian split is an exact composition on disjoint axes under retained whole-job normalizers. The border residual is nonzero. Size-dependent coefficients, recursive numerical precision, uniform compiler and BIT admission remain unproved. No new kappa is asserted.'}


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    require(not args.out.exists(), 'fresh output receipt')
    result=run()
    result['checker_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'root_lower':result['root_lower'],
                      'root_upper':result['root_upper'],'margin':result['split_moment_interval']}))
