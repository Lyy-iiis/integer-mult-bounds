# Compatible triangular lifts: a positive invariant and the two-query limit

Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance. Apache-2.0.
This is a bounded theory continuation of the Laurent-border and phase-twist
handoffs. It changes no repository branch and claims no improved exponent.

## 1. The exact compatibility condition

Let G be a finite abelian group represented by commuting invertible operators
`a(g)`, and let `chi:G->C*` be an actual character respecting every relation.
Set `b(g)=chi(g)a(g)^-1`. A triangular lift

`R(g)=[[a(g),0],[f(g),b(g)]]`

is a representation exactly when

`f(gh)=f(g)a(h)+b(g)f(h)`.

Over characteristic zero every such extension is a fixed conjugation. To see
this directly, put `c(g)=f(g)a(g)^-1` and let the group act on operators by
`g.R=b(g)R a(g)^-1`. Then `c(gh)=c(g)+g.c(h)`. Averaging over h gives

`R0=|G|^-1 sum_h c(h)`, and `c(g)=R0-g.R0`.

Therefore

`f(g)=R0 a(g)-b(g)R0`,

and `R(g)=L(R0) diag(a(g),b(g)) L(-R0)`. Conversely, every fixed conjugation
has all the required relations. The averaged R0 is an algebraic operator;
this argument does not declare it a free or inexpensive circuit.

For a free scalar choice `R0=epsilon*c*I`, the corrected off-diagonal is

`f(q)=epsilon*c*(q-chi(q)q^-1)`.

This supplies a precise sufficient invariant. A common scalar conjugation
preserves inverses, commutation and multiplication automatically. Assigning
the constant i to every Gaussian expression is not itself a character;
each genuine group relation must be respected.

## 2. What the phase twist already preserves

The retained twist is

`Psi(q)=[[q,0],[i*epsilon*(1-q^-1),i*q^-1]]`, with `q^4=I`.

It is exactly conjugate to `diag(q,i*q^-1)` by

`S(q)=L(r(q))`,

`r(q)=(epsilon/2)*(1-q)*(1-i*q^2)`.

Consequently, for a **single fixed central Q** and any fresh disjoint D_j
commuting with Q, the operators `D_j Psi(Q)` commute, and the same S(Q)
diagonalizes all of them. More precisely, defining the image of powers by
`rho(Q^k)=Psi(Q)^k` gives a representation of the cyclic group, together
with the commuting D_j factors. This uses powers of Psi(Q), not the generally
different expression Psi(Q^k).

Thus fresh D factors alone are not the relation failure. Individual free
frame covariance is also automatic:

`Psi(F q F^-1)=diag(F,F) Psi(q) diag(F^-1,F^-1)`.

The missing property appears when independently commuting Gaussian
generators must coexist. For disjoint Q1,Q2, the original operators commute,
but their twists need not. On the joint spectral branch `Q1=1,Q2=i`, the
lower entry of `Psi(Q1)Psi(Q2)-Psi(Q2)Psi(Q1)` is `-2i*epsilon`.
That branch occurs in the actual disjoint rank-one canonical Gaussian
family: the single-axis Cgate has eigenvalues 1 and i. Covariance of each
operator separately does not repair this simultaneous relation.

The common conjugator S(Q) in the fixed-anchor family is not an allowed
scalar/parity map: its odd-Q coefficient is

`-(epsilon/2)*(1-i*Q^2)`.

On `Q^2=+1` and `Q^2=-1` it is respectively
`-(epsilon/2)*(1-i)` and `-(epsilon/2)*(1+i)`, nonzero in both sectors.

## 3. Why two queries cannot supply the desired free conjugation

The detailed proof and exact finite certificate are in `two-query/`.
Its alphabet allows arbitrary invertible scalar-role boundaries over

`R_even=K[q^2]/(q^4-1)`, with `K` of characteristic zero containing i and
epsilon-dependent coefficients. A query letter is a square-zero shear
`I+qN` or `I+q^-1M`. Arbitrary intervening even boundaries can be absorbed
by conjugation, preserving square-zero nilpotence. Thus a two-query word has
the form

`A (I+qN)(I+q^-1M) B`, with `N^2=M^2=0` and A,B invertible/even.

Its even part is `A(I+NM)B`. It cannot vanish: if `NM=-I`, then left
multiplication by N gives `0=-N`, a contradiction. This argument needs no
rank assumption, so arbitrary cross-port scalar mixing does not evade it.

Every fixed even-basis conjugate of `diag(q,chi*q^-1)`, for an invertible
even chi (including i and all fixed scalar phases), is purely odd under
`q -> -q`. Hence it cannot equal this two-query word. This includes a free
scalar S_epsilon, any free even-Q S_epsilon, and their epsilon-dependent
versions. Fresh D1D2 commute with these boundaries and factor out, so they
do not change this obstruction.

This is an alphabet-specific exact statement. It does not cover additional
queries, q-odd physical boundary operations, a different coupled supplier,
or a general recursive compiler. In particular, the general averaged
operator R0 in section1 need not belong to the permitted even algebra.

There is also a limited extension with extra helper channels. If N has rank h
in a parity sector, `ker(I+NM)` is contained in `im(N)`, since every kernel
vector satisfies `v=-NMv`. Its nullity is at most h. An exact target having
2h purely odd main roles has even-part nullity at least2h, regardless of its
other block-diagonal helper outputs. Consequently q-even invertible helper
factors absorbed into the boundaries do not resolve the rank deficit. The
actual native helper factors have not been classified by this q parity;
no conclusion about arbitrary helper mixing is inferred from this extension.

## 4. Three queries give an exact compatible construction

There is a simple positive control:

`U(q)L(-q^-1)U(q)J^-1=diag(q,q^-1)`,

where `J=[[0,1],[-1,0]]`. Applying `diag(1,chi)` and the desired fixed
conjugation gives the compatible lift in section1. Choosing
`S_epsilon=L(epsilon*c)` has bounded coefficients and bounded inverse as
epsilon tends to zero; this construction itself needs no epsilon^-1 input
boundary. It is the ordinary exact three-query construction in another
basis, rather than a two-query cost saving.

Equivalently, the completed two-query Laurent endpoint can be corrected
on the left by

`L(epsilon*(q^-2-q^-1)) Phi(q)=diag(q,q^-1)`.

For Psi, multiply that correction's lower coefficient by i. The q^-2 term
is an even parity; the remaining q^-1 term is a genuine query in both parity
sectors.

## 5. A scoped lower bound for this final correction

Allow a linear correction circuit with arbitrary q-even free role maps,
linear copies and owned zero buffers, and single-role q or q^-1 queries.
Compare its matrices at q=lambda and q=-lambda within one fixed parity
sector. Each query changes by a rank-one role matrix. A telescoping product
identity, including any fixed input injection/output projection, gives

`rank(F(lambda)-F(-lambda)) <= number of queries`.

For the required lower correction on h independent main pairs, this
difference has lower block `-2*epsilon*lambda^-1*I_h`, of rank h. Thus at
least h such queries are required. The same argument applies separately
to both parity sectors, where the odd coefficient is nonzero. Merely
keeping one parity sector leaves the other uncorrected; sector decomposition
does not erase the query dependence.

This bound is for this exact final-correction alphabet. It does not rule
out reuse of internal supplier state, new mixed-rank providers, nonlinear
encodings, or other physical free-operation contracts. It does not identify
rank of an operator matrix with general multiplication cost.

For the retained h=112 interface, one additional canonical rank-one query
per pair yields this fully charged split invoice:

| Inventory | Profile | Rank mass |
|---|---|---:|
| Targets | `{4:56,7:14,8:94,9:652,17:224}` | 10750 |
| Two full calls, split | `{1:4656,2:920,3:1386}` | 10654 |
| Third query/correction included | `{1:4768,2:920,3:1386}` | 10766 |

The added112 H1 exceeds the original rank surplus96. More strongly, since
all target ranks are at least4 and all paid ranks at most3, for every
`0<=t<=1`,

`T_t/P_t <= (4/3)^(t-1) * 5375/5383 <= 5375/5383 < 1`.

No concave moment survives this particular exact repair with the retained
inventory. This price does not suppress helper outputs or owned-center work.

## 6. Same-anchor serial amortization is not funded here

The common S(Q) might suggest amortizing its query work across m two-full
blocks on the same112 main pairs. That fixed-input series produces central
Q^m, so the main rank is `16m+1` for odd m and `16m` for even m (Q^2 is free
parity). Keeping all2m helper packets and paid calls, its uncorrected rank
surplus is

`224*(m mod2)-128m`.

It is96 at m=1 and strictly negative for every m>=2, before any final
conjugator is charged. This does not address genuinely different input
routing or a changed native word; it only prices the direct serial idea.

## Evidence and limitations

`verify_compatible.py` uses pinned, byte-preserved standard-library exact
arithmetic from the phase-twist checker. It checks every coefficient in the
fourth-order polynomial ring, the fixed-anchor powers and commutation,
the corrected commuting lift, the exact three-query and repair identities,
both parity coefficients, literal source-derived profiles and four rejecting
controls. `RESULT.json` records the executed run. It does not run a new
native supplier suite or prove recursive numerical stability.

The source native word remains pinned to compressed SHA256
`7679daa4ec6a40f56fc7f0202379a6f454310e94945aba4f48beaaaafb838d05`,
the round-three word in Cao Yifan's PR4610 lineage. The Laurent and border
recovery lineage remains credited to the prior Yiyang handoff and Dillon's
PR4623. No broad impossibility or new bound is asserted.
