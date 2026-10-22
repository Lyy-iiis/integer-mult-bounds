# A sharp local precision requirement for the Laurent border

Prepared by Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance.
SPDX-License-Identifier: Apache-2.0

This is a local error-model lemma. It is not a native compiler admission,
a lower bound for every possible implementation, or a new multiplication bound.

Let `0 < epsilon <= 1`, let `q` be unitary, and use ordinary block-matrix
multiplication. The two-query scalar word has the exact expression

```
F_epsilon(a,b) =
[ I - ab + a       (ab - I)/epsilon ]
[ epsilon(I - b)                b  ].
```

At the intended, coherently inverse queries `a=q`, `b=q^-1`, this is

```
Phi_epsilon(q) =
[ q                         0 ]
[ epsilon(I - q^-1)     q^-1 ].
```

Its distance from the declared diagonal target is exactly
`epsilon * ||I-q^-1||`, at most `2 epsilon`. At `q=-I`, it is exactly
`2 epsilon`.

Now keep the second query exact and perturb the first by an arbitrary
operator `Delta`, so `a=q+Delta`, `b=q^-1`. No commutation hypothesis on
`Delta` is used. Exact subtraction gives

```
F_epsilon(q+Delta,q^-1) - Phi_epsilon(q) =
[ Delta(I-q^-1)      Delta q^-1/epsilon ]
[ 0                                      0 ].
```

Consequently the error norm is at least `||Delta||/epsilon`. This is an
attained sensitivity of the displayed word, not a product-of-condition-
numbers estimate.

For example, at the scalar branch `q=-1` and `Delta=delta`, the error from
the diagonal target is

```
[ 2 delta       -delta/epsilon ]
[ 2 epsilon                   0 ].
```

Testing its two coordinate unit vectors proves the two separate necessary
conditions

```
2 epsilon <= tau,       delta/epsilon <= tau
```

for a uniform target-error guarantee `tau`. Therefore an independent
black-box query-error guarantee `||Delta|| <= delta` must satisfy

```
delta <= tau epsilon <= tau^2/2.
```

Writing `tau=2^-k` and `delta=2^-w`, this requires `w >= 2k+1` under this
normalization. An additional fixed guard margin is needed for allocating an
actual error budget among both queries and the surrounding scalar work.
The extra precision cannot in this error model be replaced by a fixed
number of guard bits independent of `k`.

For completeness, with two independent perturbations of norm at most
`delta <= 1`, direct block subtraction yields the conservative sufficient
bound

```
||F_epsilon(q+Delta_a,q^-1+Delta_b) - diag(q,q^-1)||
    <= 2 epsilon + 9 delta/epsilon.
```

Indeed the four block-error bounds are `3delta+delta^2`,
`(2delta+delta^2)/epsilon`, `epsilon delta`, and `delta`; their sum is at
most `9delta/epsilon`. Thus `epsilon <= tau/4` and
`delta <= tau epsilon/18` suffice before other numerical errors. This
matches the necessary doubling of precision up to a fixed additive number
of bits.

## Scope and possible escape

The lower bound applies when the two approximate queries may have
independent bounded operator errors. It does not prove that every paid
call inside the actual native supplier must individually receive twice the
precision. A source-level error-propagation or cancellation argument could
be sharper, and it must be priced using the real paid ranks and chronology.

In particular, if the ideal linear realizations are correlated so that the
second query is exactly the inverse of the first, `b=a^-1`, then `ab-I=0`
identically. The amplified block vanishes. This is a mathematically distinct
premise; independent approximations of `q` and `q^-1` do not establish it,
and rounding during execution still needs its own analysis.

The scalar branch `q=-1` used above is available in sufficiently large
all-column Fourier jobs; the one-bit normalized involution alone is
identity and would not witness this sensitivity. For the preferred raw
Laurent formulation no even Q4 adapter or alpha implementation is needed.
