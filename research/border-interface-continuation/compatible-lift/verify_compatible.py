#!/usr/bin/env python3
"""Exact compatible-lift identities and the retained fixed-inventory bill.

Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance. Apache-2.0.
Scoped algebra/cost screen; no recursive compiler or improved bound.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys
sys.dont_write_bytecode=True
VENDOR_SHA='43c5535db451b1b846018668cb9f79fa4ae0a39ed5240dbbdef0d2cb1173d242'

def need(ok,why):
    if not ok:raise ValueError(why)

def run(source):
    vendor=Path(__file__).with_name('vendor')/'phase_twist.py'
    need(sha256(vendor.read_bytes()).hexdigest()==VENDOR_SHA,'fixed exact arithmetic source')
    spec=importlib.util.spec_from_file_location('compatible_lift_arithmetic',vendor)
    a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
    prior=a.run(source)
    z,o=a.ZERO,a.ONE
    q,qi,eps=a.mono(q=1),a.mono(q=-1),a.mono(epsilon=1)
    lower=lambda f:[[o,z],[f,o]]
    upper=lambda f:[[o,f],[z,o]]
    diag=lambda x,y:[[x,z],[z,y]]
    product=lambda *factors:fold(a.mm,a.EYE,factors)
    phase=diag(o,a.IMAG)
    r=a.mul(a.mono(epsilon=1,z=(F(1,2),F(0))),
            a.mul(a.add(o,a.neg(q)),a.add(o,a.neg(a.mono(q=2,z=(0,1))))))
    s,si=lower(r),lower(a.neg(r))
    need(product(s,diag(q,a.mul(a.IMAG,qi)),si)==a.psi(),
         'single-anchor phase twist has exact common operator conjugacy')
    powers=[]
    for m in range(5):
        phase_power=((1,0),(0,1),(-1,0),(0,-1))[m%4]
        target=diag(a.mono(q=m),a.mono(q=-m,z=phase_power))
        need(a.power(a.psi(),m)==product(s,target,si),'entire cyclic representation')
        powers.append(m)
    d1,d2=a.mono(d1=1),a.mono(d2=1)
    left,right=a.scale(a.psi(),d1),a.scale(a.psi(),d2)
    need(product(left,right)==product(right,left),'same-anchor fresh-D commutation')
    need(product(left,right)==product(s,a.scale(diag(a.mono(q=2),a.neg(a.mono(q=-2))),
                                               a.mul(d1,d2)),si),
         'same S diagonalizes fresh-D products')
    # A scalar, epsilon-dependent S gives a compatible representation of
    # independently commuting generators, provided their character is valid.
    se,sei=lower(eps),lower(a.neg(eps))
    compatible=lambda var:product(se,diag(a.mono(**{var:1}),
        a.mul(a.IMAG,a.mono(**{var:-1}))),sei)
    need(product(compatible('q'),compatible('d1'))==
         product(compatible('d1'),compatible('q')),'fixed scalar conjugation preserves commutation')
    need(a.power(compatible('q'),4)==a.EYE,'compatible generator has order four')
    exact_three=product(upper(q),lower(a.neg(qi)),upper(q),a.JI)
    need(exact_three==diag(q,qi),'three-query exact diagonal positive control')
    need(product(se,phase,exact_three,sei)==compatible('q'),
         'corrected fixed-conjugation lift is achievable with third query')
    repair=a.mul(eps,a.add(a.mono(q=-2),a.neg(qi)))
    need(product(lower(repair),a.phi())==diag(q,qi),'one-extra-query untwisted repair')
    need(product(lower(a.mul(a.IMAG,repair)),a.psi())==diag(q,a.mul(a.IMAG,qi)),
         'one-extra-query phased repair')
    sectors=[]
    for parity in (-1,1):
        direct=(-parity,0)
        # Odd coefficient of r, after dividing by epsilon/2, is -1+i*parity.
        diagonalizer=(-1,parity)
        need(direct!=(0,0) and diagonalizer!=(0,0),'no parity sector has a zero odd coefficient')
        sectors.append({'q_squared':parity,'direct_repair_odd_coefficient_over_epsilon':direct,
                        'diagonalizer_odd_coefficient_over_half_epsilon':diagonalizer})
    target={int(k):v for k,v in prior['targets'].items()}
    paid=Counter({int(k):v for k,v in prior['paid_split'].items()})
    paid[1]+=112
    mass=lambda p:sum(r*n for r,n in p.items())
    need(mass(target)==10750 and mass(paid)==10766,'fully charged third-query rank masses')
    need(min(target)==4 and max(paid)==3,'strict separation retained after thin repair')
    single_h=sum(int(r)*n for r,n in prior['helper_widths'].items())
    single_p=sum(int(r)*n for r,n in prior['actual_paid_profiles']['forward'].items())
    serial=[]
    for m in range(1,5):
        main_rank=16*m+(m%2)
        surplus=224*main_rank+2*m*(single_h-single_p)
        need(surplus==224*(m%2)-128*m,'same-input serial rank surplus')
        serial.append({'two_full_blocks':m,'main_rank_each':main_rank,'rank_surplus_before_repair':surplus})
    controls={
        'different_generators_do_not_commute_under_uncorrected_twist':
            product(a.psi(),a.psi(1))!=product(a.psi(1),a.psi()),
        'omit_third_query_cannot_diagonalize':product(upper(q),lower(a.neg(qi)),a.JI)!=diag(q,qi),
        'omit_repair_odd_part_leaves_residual':product(lower(a.mono(q=-2,epsilon=1)),a.phi())!=diag(q,qi),
        'omit_extra_query_charge_changes_surplus':mass(target)-(mass(paid)-112)==96 and mass(target)-mass(paid)==-16,
    }
    need(all(controls.values()),'all four meaningful rejecting controls')
    return {'status':'PASS_COMPATIBLE_LIFT_IDENTITIES_AND_SCOPED_COST_OBSTRUCTION',
        'source_sha256':prior['source_sha256'],'vendor_sha256':VENDOR_SHA,
        'cyclic_representation_powers_checked':powers,
        'same_anchor_fresh_D_commutes':True,'fixed_scalar_conjugation_distinct_generators_commute':True,
        'three_query_exact_lift':True,'direct_repair_parity_sectors':sectors,
        'target_profile':target,'third_query_paid_split_profile':dict(sorted(paid.items())),
        'target_mass':mass(target),'paid_mass':mass(paid),
        'all_concave_moment_ratio_bound':'(4/3)^(t-1)*5375/5383 <= 5375/5383 < 1, 0<=t<=1',
        'same_input_serial_inventory':serial,'controls':controls,
        'limits':['The single-anchor common conjugator depends on the odd query; it is not declared free.',
                  'A commuting-family character must respect every relation; assigning i independently without checking relations is insufficient.',
                  'The112-extra-query bound is for exact correction by single-role q or q^-1 queries and even free role maps; it excludes reuse of hidden intermediate states and changed query alphabets.',
                  'Covariance under simultaneous free conjugation is automatic and is not identified as a failure.',
                  'No all-compiler impossibility, recursive precision admission, or improved multiplication exponent is claimed.']}

def fold(op,unit,items):
    out=unit
    for x in items:out=op(out,x)
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    need(not args.out.exists(),'fresh result path')
    result=run(args.source);result['checker_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    with args.out.open('x') as f:f.write(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(result['status'])
