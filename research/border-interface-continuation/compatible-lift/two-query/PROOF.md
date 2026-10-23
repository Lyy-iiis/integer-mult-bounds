# Two query letters cannot produce an odd compatible lift

Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance.
SPDX-License-Identifier: Apache-2.0

This is a restricted exact algebra result. It neither rules out controllers
with a different query alphabet nor establishes a new multiplication bound.
It addresses the proposed repair of the two-full Laurent border interface
by changing only its free role boundaries.

Let K = Q(i), let q be central, and work in

    R = K[q]/(q^4 - 1),
    R0 = K[q^2]/(q^4 - 1).

There is a direct sum R = R0 + q R0: every element has unique even and odd
parts. The same argument works in the formal Laurent ring with its parity
grading. Coefficients may also depend on an auxiliary nonzero parameter
epsilon. All claimed inverses below must exist at the chosen epsilon.

“Even boundary” means an invertible role matrix with entries in R0. This
allows all Gaussian-rational scalar boundaries and the enlarged algebra of
q^2-dependent free boundaries. Allowing this larger algebra strengthens the
obstruction; physical implementation of every such matrix is not assumed.

## Exact obstruction

Consider any two-query word

    F(q) = L (I + q N0) C (I + q^-1 M0) R,

where L, C, R are invertible even boundaries and N0^2 = M0^2 = 0, with N0,
M0 even. These matrices can have any common positive dimension. Put

    A = L C,  N = C^-1 N0 C,  M = M0,  B = R.

Then N^2 = M^2 = 0 and

    F = A [I + NM + q N + q^-1 M] B.

Its even part is exactly A(I + NM)B. It cannot vanish: otherwise
I + NM = 0, and left multiplication by N gives

    0 = N(I + NM) = N + N^2 M = N.

Substitution back would give I = 0, a contradiction. Therefore F cannot be
purely odd. This argument does not use a rank estimate or a restriction to
pairwise role mixing.

The argument also works separately after fixing q^2 = +1 or q^2 = -1,
provided both signs of q in that sector are retained. Invertibility of an
R0 boundary implies invertibility on each sector. Thus the obstruction
cannot be avoided by doing the proposed exact repair on only one of the
two parity sectors while retaining both of its q eigenvalues.

In particular, for any invertible even S and any even unit chi,

    S diag(q, chi q^-1) S^-1

is purely odd, so no such two-query word equals it. This includes chi = i.
With S = [[1,0],[c,1]], the desired lower entry is c(q - chi q^-1).
Any even c, including epsilon-dependent c, is covered.

For a larger common-q main block, the same argument excludes every purely
odd target when the two query nilpotents remain square zero. Thus arbitrary
mixing of the common-q main roles does not evade this particular theorem.
It does not cover mixing additional helper interfaces whose query letters
or target parity differ.

The q^4 = 1 quotient does not identify even and odd elements. In the
retained canonical family q = Q_f, the rank-one factor has eigenvalues 1
and i. Tensor width f >= 3 contains all four fourth roots, so an identity
required at every tensor width must satisfy the above quotient identity.
The theorem need not hold after restriction to a single q eigenspace.

## Independent two by two coefficient certificate

For U(x) = [[1,x],[0,1]], L(y) = [[1,0],[y,1]], and an arbitrary even
middle matrix C = [[u,v],[w,z]], direct multiplication gives

    U(aq) C L(bq^-1)
      = [[u + ab z + aq w + bq^-1 v, v + aq z],
         [w + bq^-1 z,                z]].

Its even part is [[u + ab z, v],[w,z]]. If it were zero, first v = w = z = 0
and then u = 0, contradicting invertibility of C. Invertible even exterior
boundaries cannot turn a nonzero even part into zero. This is a separate
entrywise proof for the requested two by two normal form.

For a two by two target with chi having a nonzero odd part, a different
obstruction applies. Both query factors have determinant 1, and all
boundary determinants are even. Hence det F is even, whereas

    det(S diag(q, chi q^-1) S^-1) = chi.

Thus an odd or mixed-parity chi is also impossible in this two by two
grammar. This determinant argument is not asserted for a repeated
h-dimensional target: chi^h can be even even when chi is odd.

## Sharpness within the alphabet

Let J = [[0,1],[-1,0]]. There is an exact three-query identity

    U(q) L(-q^-1) U(q) J^-1 = diag(q,q^-1).

A fixed diagonal phase followed by fixed conjugation produces the desired
chi = i compatible target. This is an algebraic positive control, not a
claim that the extra query is free. The caller must charge that query and
all of its native implementation and precision costs.

The existing phased border

    Psi(q) = [[q,0],[chi epsilon(1-q^-1),chi q^-1]]

has even part chi epsilon E21, which is nonzero for nonzero epsilon and a
unit chi. Its exact order-four property at chi = i is consistent with this
obstruction: finite order does not make its basis change even. An odd
q-dependent boundary, an additional query, or a different interface
changes the hypotheses and remains outside the conclusion.

## Certificate and provenance

`verify.py` is a standalone standard-library certificate. It checks the
universal matrix expansion, parity projection, determinant identities, the
three-query positive control, and the existing border's nonzero even part,
both formally and modulo q^4 = 1. It also checks N(I+NM)=N in the free word
algebra modulo N^2=M^2=0. Three deliberately false identity claims are
rejected in both commutative rings. The receipt binds the checker and this
note by SHA256; output creation is exclusive.

    PYTHONDONTWRITEBYTECODE=1 python3 -I -B -O verify.py --output RESULT.json

Context is the inherited two-full Laurent interface and the local notes
`phase-twist/NOTES.md` and `phase-twist-review/NOTES.md` under
`/tmp/oct24-border-compiler`. Those notes distinguish exact finite order
from representation compatibility. This certificate proves only the
displayed local algebra; it does not rerun a native source or compiler.
