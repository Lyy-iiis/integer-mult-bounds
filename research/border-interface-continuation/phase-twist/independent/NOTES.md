# Phase-twist arithmetic review

Prepared by Yiyang with OpenAI Codex assistance. This is an independent local
algebra handoff, not a native supplier certificate or an improved bound. No
main contribution package was edited.

Let `i²=-1`, let epsilon be a commuting scalar, and let `q⁴=I`. Write

\[
\Psi=\begin{pmatrix}q&0\\t&b\end{pmatrix},\qquad
t=i\epsilon(1-q^{-1}),\quad b=iq^{-1}.
\]

## Exact finite order

The diagonal blocks of the fourth power are identity. The lower-left block is

\[
t(q^3+q^2b+qb^2+b^3)
=t(q^3+iq-q^{-1}-iq^{-3})=0.
\]

Thus `Psi⁴=I` exactly, for every scalar epsilon. Its role determinant is `i`.
For an operator `d` commuting with `q` and satisfying `d⁴=I`, `A=d Psi` also
satisfies `A⁴=I`. Merely requiring `d` and `q` to be individually symmetric
and order four does not imply their commutation or `A⁴=I`.

## Adjugate and physical transpose

Set

\[
J=\begin{pmatrix}0&I\\-I&0\end{pmatrix}.
\]

Over the commuting operator ring, role transpose gives

\[
J A^{T_{\rm role}}J^{-1}=\operatorname{adj}(A),\qquad
A^{-1}=-i d^{-2}J A^{T_{\rm role}}J^{-1}.
\]

Physical transpose equals role transpose of these blocks if `qᵀ=q`, `dᵀ=d`,
and `dq=qd`. No complex conjugation occurs: this is ordinary transpose, not
Hermitian adjoint. Order four alone does not imply physical symmetry.

There is a useful weaker statement when `q,d` are physically symmetric but
need not commute. Put `D=diag(d,d)`, so `A=D Psi`. Then

\[
\Psi J\Psi^T=iJ,\qquad
AJA^T=iD^2J,
\qquad
A^{-1}=(JA^TJ^{-1})(-iD^{-2}).
\]

The correction is on the **right** in this last identity. Moving it to the
left requires `D²A=AD²`; `dq=qd` suffices. The verifier rejects the left-side
formula for `q=[[0,1],[1,0]]`, `d=diag(1,i)`, while verifying the right-side
formula. Both operators in this counterexample are symmetric and order four.

For a direct sum of this main block and exact symmetric order-four helper
blocks `H_h`, define `Jhat=diag(J,I_helpers)`. Under the commuting main-block
hypotheses, the whole inverse is

\[
G^{-1}=C\widehat J G^T\widehat J^{-1},\qquad
C=\operatorname{diag}(-i d^{-2}I_2, H_1^2,H_2^2,\ldots).
\]

When the factors in `C` are known physical phase/parity monomials, those
endpoint corrections add no recursive child calls. This statement still
requires an **actual physical transposed supplier with the required matched
interfaces**. It does not construct one, and does not establish an exact
inverse of a rounded approximation by substituting its transpose.

## Parity is not the entire square

The exact square is

\[
\Psi^2=\begin{pmatrix}
q^2&0\\
\epsilon(q^2-q^{-1}+iq-i)&-q^2
\end{pmatrix}.
\]

The lower-left polynomial is generally nonzero. Consequently the whole
`Psi²` is not established to be a free parity monomial. The polynomial is
zero on the `q=1` eigenspace but, for example, equals `(2-2i) epsilon` on the
`q=-1` eigenspace. Although `q²` commutes with polynomials in the same `q`, it
need not commute with a different operator chart. The exact control
`q=diag(1,i)` and a coordinate swap has noncommuting parity `q²` and chart.

One can diagonalize the twist by an operator-valued shear:

\[
\Psi=L(r)\operatorname{diag}(q,iq^{-1})L(-r),\qquad
r=\frac{\epsilon}{2}(1-q)(1-iq^2),\quad
L(r)=\begin{pmatrix}I&0\\r&I\end{pmatrix}.
\]

This uses `(q²-i)^(-1)=(q²+i)/2`. It explains finite order but is not a free
scalar or parity change of basis: `r` contains `q` and `q³`, whose whole-query
work is not automatically free.

## Evidence and scope

`verify.py` uses only the standard library. Its formal identities are exact
in `Z[i][d,q,e]/(d⁴-1,q⁴-1)`; all coefficients are integer pairs, with no
floating point. It separately checks physical matrices and five missing-
hypothesis/fault controls. Run:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -I -B -O verify.py --compare RESULT.json
```

The receipt does not establish recursive closure, admissible transposed
physical routing, matching target credit, or finite-precision inverse
identities. No paid invoice improvement is claimed.
