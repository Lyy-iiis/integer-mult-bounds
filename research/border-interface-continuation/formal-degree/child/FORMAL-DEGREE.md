# Laurent degree: synchronized toy recursion versus an actual supplier

SPDX-License-Identifier: Apache-2.0
Yiyang (@Lyy-iiis), with substantial OpenAI Codex and multi-agent assistance.

This is an independent algebraic audit of the two-query core. It proves useful
positive degree invariants and a failure of naive constant-term extraction.
It does not construct the full native supplier or claim a multiplication bound.

Write, over any unital operator ring,

\[
F_{z^w}(a,b)=
\begin{pmatrix}a-E&z^{-w}E\\z^w(I-b)&b\end{pmatrix},
\qquad E=ab-I,\quad w>0.
\]

The variables commute with all operators. Matrix multiplication order is the
displayed order; no commutativity of a and b is assumed.

## 1. General exact recurrence and its limitation

For a nonzero Laurent matrix X let v(X) and h(X) be its lowest and highest
nonzero powers, across all entries; put v(0)=+infinity and h(0)=-infinity.
The exact recurrence, retaining possible cancellations, is

\[
v(F)=\min\{v(a-E),v(E)-w,w+v(I-b),v(b)\},
\]
\[
h(F)=\max\{h(a-E),h(E)-w,w+h(I-b),h(b)\}.
\]

If a,b only have the common known degree interval [-L,H], where L,H>=0,
then the safe interval is

\[
[-(2L+w),\ \max(2H,H+w)].
\]

These are degree bounds, not generally equalities. They are especially loose
when the inputs share a compatible diagonal grading. A chronological program
cannot be treated as a tensor product merely because its children have the
same degree bounds: multiplication adds their degrees, and inserted routing
can destroy a common grading.

A bounded scalar example shows exponential pole growth is possible when
outputs are recycled without that common all-owner invariant. Set c0=2 and
`c_(d+1)=(c_d^2-1)/z`, the upper-right entry of F_z(c_d,c_d).
Then v(c_d)=-(2^d-1), by induction on the unique lowest term. This is a
counterexample to a general linear-in-depth degree assertion, **not** a model
of the complete native supplier or of the synchronized recursion below.

## 2. Independent synchronized substitution has an exact common gauge

Let A0=q, B0=q^-1, with q independent of z, and define

\[
A_d=F_z(A_{d-1},B_{d-1}),\qquad
B_d=F_z(B_{d-1},A_{d-1}).
\]

The two right-hand sides use the previous level, not an in-place update.
The previous owner layout is retained identically in both operands. Let
D0=I and D_d=diag(D_(d-1), z D_(d-1)). Direct substitution proves

\[
A_d(z)=D_d A_d(1)D_d^{-1},\qquad
B_d(z)=D_d B_d(1)D_d^{-1}.
\]

In the ordinary binary block indexing, D_d has diagonal z^popcount(i).
Consequently every matrix entry has exactly one possible Laurent exponent,
popcount(row)-popcount(column), and the complete degree interval is contained
in [-d,d]. This is a genuine all-depth identity, not a numerical degree guess.

**Linear degree does not make the constant term correct.** At q=-1 the two
orientations coincide. For every d>=1, the entry at row1, column2^d-2 is

\[
2(-2)^{d-1}z^{2-d}.
\]

For d=2 it is the nonzero constant -4. For d=3 it is 8/z. Meanwhile the entry
at row2^d-1,column0 has nonzero degree d. Thus the exact whole-matrix interval
in this example is `[min(0,2-d),d]`. The receipt checks d=1,...,5 with exact
rational matrices, including equality to the direct recursive evaluation at
z=1/2. The first witness can also be proved inductively: it is an adjacent
off-diagonal entry in the bit-reversed triangular order, so squaring the
previous matrix multiplies its coefficient by -2.

Tensoring an invalid Laurent endpoint does not repair it. Even if a Laurent
matrix happened to have constant coefficient T, negative and positive powers
could combine to make extra constant terms in its tensor square. One needs a
proper border `T+zR(z)` before identifying the tensor-power constant term with
T tensor-power t.

## 3. Multivariate grading gives a proper toy border, at a degree price

Give level j its own variable x_j. The same proof gives diagonal entries
`product_j x_j^(bit_j(i))` in the common gauge. The full multivariate constant
term therefore discards every off-diagonal owner block. Its diagonal blocks
are q or q^-1: induction uses that the diagonal blocks of A_(d-1) and
B_(d-1) are mutually inverse, so `ab-I` has zero diagonal there.

More precisely, in the order that prioritizes the earliest/innermost owner
bit, both matrices are lower triangular. The base one-level identity is lower
triangular; at the next level the top-right block ab-I has strictly lower
old-owner index, while its lower-left block may advance the new outer bit.
This proves the claimed triangularity and diagonal formula in any operator
ring containing the fixed inverse pair q,q^-1.

For a fixed depth d, assign integer exponents from inner to outer as

\[
(w_1,\ldots,w_d)=(2^{d-1},2^{d-2},\ldots,1),\qquad x_j=z^{w_j}.
\]

The first changed owner bit dominates all later bits. Every nonzero
off-diagonal entry then has positive degree, and

\[
A_d(z)=\operatorname{diag}(q^{\pm1})+zR_d(z),
\qquad \deg A_d\le 2^d-1.
\]

Equivalently, the outermost local parameter is z, its child parameter is z^2,
the next child's is z^4, and so on. Reversing that order is not the same
construction and need not give a proper border. At q=-1 the minimum positive
degree is exactly1 and maximum degree is exactly2^d-1; the exact receipt checks
both. These bounds coincide with the independent-error precision-doubling
intuition, but here they follow from an explicit complete toy grading.

Alternatively, since each individual x_j has degree in {-1,0,1}, averaging
over all2^d assignments x_j in {+1,-1} extracts the multivariate constant term
exactly, using only the dyadic coefficient2^-d. This evaluation count is
exponential in depth. It is an algebraic toy extraction, not a priced native
schedule with preserved independent helpers.

## 4. Coherent actual inverse gives a stronger positive invariant

Now define B_d to be the **actual inverse** of A_d, rather than a fresh
opposite-orientation approximation. Starting with A0=q, B0=q^-1, set

\[
A_d=\begin{pmatrix}A_{d-1}&0\\
z^{w_d}(I-B_{d-1})&B_{d-1}\end{pmatrix},\qquad
B_d=\begin{pmatrix}B_{d-1}&0\\
z^{w_d}(B_{d-1}-I)&A_{d-1}\end{pmatrix}.
\]

Multiplication in both orders gives the identity, assuming only
A_(d-1)B_(d-1)=B_(d-1)A_(d-1)=I. This is also exactly
`F_(z^w_d)(A_(d-1),B_(d-1))` in the first formula. Both matrices are
polynomials; their inverse relation does not introduce an unbounded rational
denominator. Their degrees satisfy

\[
v(A_d),v(B_d)\ge0,\qquad
\max(h(A_d),h(B_d))\le\sum_{j=1}^d w_j.
\]

For all w_j=1, both are proper borders of degree at most d, with the desired
diagonal constant blocks q or q^-1. The q=-1 fixture has degree exactly d and
no off-diagonal constant terms; both inverse products are checked exactly at
z=1/2 through depth5. The all-depth proof is the explicit block multiplication,
not those finite checks.

This is the positive formal closure target. Merely knowing that a numerical
approximation is invertible would not suffice: the inverse of a generic
polynomial, such as1+z, need not be a finite Laurent polynomial. The explicit
polynomial inverse pair above is substantially stronger. Likewise, replacing
B_d by `F_z(B_(d-1),A_(d-1))` loses this property and gives Section2's defect.

## 5. What coefficient extraction does, and does not, imply

For a valid fixed polynomial border P(z)=T+zR(z) of degree D,

\[
P(z)^{\otimes t}=T^{\otimes t}+z\widetilde R_t(z),
\qquad \deg P^{\otimes t}\le tD.
\]

Ordinary exact interpolation therefore extracts the target using at most
tD+1 distinct nonzero evaluations and a linear combination. For fixed D this
evaluation overhead is subexponential in t. This is the elementary degree
argument underlying the Bini-style escape from a fixed border degree.

The order of quantifiers matters:

| Family considered | Sufficient extraction evaluation count |
| --- | --- |
| One coherent depth-d toy word | d+1 |
| One independently substituted depth-d word repaired by the grading above | 2^d |
| t tensor copies of any one **fixed** valid degree-D border | tD+1 |
| A simultaneously deepening family with D=2^d-1 | At most t(2^d-1)+1; this guarantee is not subexponential in d |

The last row is not a lower bound against every more structured extraction.
Conversely, an exponentially large but fixed D does **not** refute the
fixed-border tensor-power argument: first fixing d and then letting t grow
still gives subexponential overhead in t.

None of these evaluation counts is a complete multiplication-cost theorem.
The exact scalar coefficients of ordinary interpolation can have odd
denominators, and the actual model must implement and price them. Tensorization
must also preserve arbitrary independent owner inputs, helper outputs, routing,
owned storage and the productive/paid invoice. In particular, a statement about
tensor-power degree alone does not import a bilinear-complexity exponent theorem
into this Gaussian supplier model.

## 6. The exact missing native premise

The common diagonal D_d assumes that both child operands retain the same full
owner layout and all intermediate routing respects that grading. The actual
source has heterogeneous productive ranks, thousands of chronological paid
children, helper borrowing, center ownership and interclass matching. No result
here proves one global grading survives those interfaces.

The coherent construction requires the actual inverse of the same realized
child on the full operator space. A fresh nominal inverse orientation,
transposition without address coherence, or inversion only on the two main
roles is not enough. It also does not justify reversing owned CLEAR operations.
The producer's full normalized helper endpoint and all arbitrary-input
ownership obligations must be retained.

Accordingly the reusable positive theorem is conditional: **a synchronized
polynomial inverse-pair interface has linear formal degree and a proper border
under arbitrary recursive depth.** A real native interface realizing this
condition, or a complete source-compatible triangular grading, remains the
scientific task. The strict split invoice and its raw crossing are unchanged;
this audit supplies no admitted new bound.

Source context: the two-full Laurent border's `PROOF.md` and the precision
audit's `WEIGHTED-COMPILER-GATE.md` were read; their provenance basenames and
hashes are recorded in MANIFEST.json. No source files were modified.
Prepared with substantial OpenAI Codex assistance within the same author
process; no independent human or proof-kernel acceptance is claimed.
