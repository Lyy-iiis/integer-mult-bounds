# Formal degree and coefficient extraction for the two-full border

Yiyang (@Lyy-iiis), with substantial OpenAI Codex and multi-agent assistance.
SPDX-License-Identifier: Apache-2.0

This is a local algebra/compiler screen. It gives no new admitted exponent.
The raw strict-invoice crossing near `C=0.0048568755777092` is conditional.
The triangular-matching investigation is separate.

## 1. The appropriate degree recurrence is chronological

Let every entry of a completed child matrix have Laurent support in
`[-D,D]`. Its application to a register whose coefficients have support in
`[l,u]` has support in `[l-D,u+D]`. More generally, if the child mixes a
batch of parent fields, take the union of their input supports first.
A scalar ADD takes the union of supports, not their Minkowski sum. A COPY
copies support; a nonzero constant SCALE preserves it; an owned CLEAR gives
the empty support. Only sequential operator composition adds degrees.
Degree-zero monomial boundary maps preserve supports. These rules are
valid over any operator coefficient ring, without commutativity between
operator coefficients.

In the source compiler a paid round suspends all instances of a class,
completes its matched child class and resumes them. The requested field is
the same prototype owner in every instance. Thus the maximum support among
instances of that owner can be propagated through the prototype's literal
chronology. Fresh independent inputs must be included; they are not zero
or omitted helper fields. Previously completed complementary source
programs need their own support charge in a complete mixed compilation.

The authenticated two-call word has 42,898 records, 6,596 unsplit paid jobs
and 6,962 split factors. Its structural longest output dependency path
crosses **23 split factors**, not all 6,962. The checker retains all 224
main outputs, both sets of 408 helper outputs and all 32 owned CLEARs.
For each root-boundary exponent b, it records the largest number k of
split factors on a path with that boundary exponent:

| b | k |
|---:|---:|
| -1 | 22 |
| 0 | 23 |
| 1 | 20 |

Consequently the returned support is contained in the union of
`[b-kD,b+kD]` over these three rows. If D is an integer at least one this
is contained in `[-23D,23D]`. At D=0 the conservative structural box is
`[-1,1]`; exact local cancellation improves the actual complete endpoint
to `[0,1]`.

For a homogeneous nesting of raw units under these contracts, the safe
bound is therefore `D_1<=1`, `D_(d+1)<=23 D_d`, hence `D_d<=23^(d-1)`.
This is an **upper bound only**. It does not show that a degree is attained,
that the coefficient at zero is correct, or that a full mixed compiler has
this recurrence after its source complements are installed. In particular,
this is not the ordinary recursion of an already fixed rank-N uniform
template; that template has its own larger chronological dependency graph
and requires its own degree propagation. It shows why
counting all serial calls is too pessimistic and why treating every call
as parallel is unjustified. No physical phase suite is rerun by this
structural degree check.

## 2. Small support does not imply the desired coefficient

Write

`F_e(a,b)=[[1-ab+a,(ab-I)/e],[e(I-b),b]]`.

The synchronized two-query recursion starts at `A_0=q, B_0=q^-1` and sets
`A_(d+1)=F_e(A_d,B_d)`, `B_(d+1)=F_e(B_d,A_d)`. Its exact common diagonal
gauge gives support within `[-d,d]`, despite serial products. Nevertheless,
the constant coefficient is already wrong at depth two: on q=-1 the
known upper-right residual has coefficient -4. Interpolation of this
single-parameter recursion recovers the wrong coefficient exactly.

See `child/FORMAL-DEGREE.md` and its executable receipt for the precise gauge,
multivariate variant, and which finite instances were checked. A true
inverse recursion is a different premise: if

`M_e(A)=[[A,0],[e(I-A^-1),A^-1]]`,

then

`M_e(A)^-1=[[A^-1,0],[e(A^-1-I),A]]`.

If both A and its actual inverse have degree box `[-D,D]`, these formulas
have box `[-D-1,D+1]`. Starting from a degree-zero exact q and its inverse
therefore gives an O(d) envelope, correct constant term and polynomial
inverse at every level. This is a constructive *query-core* invariant.
It does not supply the actual native inverse/transpose implementation,
all helper endpoints or scalar rounding needed to use that invariant in
the paid-word compiler.

Giving each recursive level its own variable also avoids the incorrect
single-parameter collision. Substituting one scalar variable with
superincreasing level weights can keep distinct multivariate degrees from
colliding; in the toy Boolean role grading, weights `1,2,4,...` give range
`2^d-1`. That is exponential in recursive depth, not a free relabeling.
No claim is made that this weighting is necessary for every native word.

## 3. What interpolation would cost

For an operator Laurent polynomial supported on `[-D,D]`, ordinary
interpolation at `2D+1` distinct nonzero points recovers every coefficient,
including the constant one. It applies entrywise, so it does not require
expanding an exponentially large operator matrix. Each evaluation is a
complete execution on its own retained arbitrary inputs and owned fields;
all helper outputs are included. The scalar combinations and storage are
additional work. Algebraic point counts alone do not prove bit-complexity,
conditioning or fixed-tape admission.

For a universal black-box extraction formula over this whole support box,
at least D+1 nonzero evaluation points are necessary: if m<=D points are
used, the polynomial `product_j(e-e_j)` vanishes at those points and has a
nonzero constant coefficient. This lower bound is about such a universal
evaluation formula, not an exploitation of extra structure of this border.
Special roots of unity can reduce the sufficient point count but require
permitted exact coefficients or their own numerical analysis.

If an actual rank-multiplicative recursive construction on rank `N^d` had
correct constant coefficient, degree `poly(d)` and the desired leaf bill,
interpolation would add only `poly(log n)` executions at rank n=N^d. At
the algebraic operation-count level that would preserve its saving. This
is the concrete positive criterion worth trying to prove; the coherent
query-core recursion above satisfies the degree part of that criterion.

An exponential envelope `D_d=c^d` instead certifies an evaluation overhead
of order `n^(log_N c)`. An upper envelope of that size does not prove the
actual degree cannot be smaller. It does show that citing this envelope
alone cannot justify a subpolynomial interpolation charge. At the raw
minimum target-rank scale 4, even the toy weight factor 2 gives
`log_4(2)=1/2`, far larger than the raw invoice saving. The actual mixed
precompiler is not a homogeneous rank-four recursion, so this is a scale
comparison, not a new compiler lower bound.

## 4. Why the standard tensor-power slogan is insufficient here

For a fixed polynomial matrix A(e), `A(e)^(tensor h)` has degree at most h
times the original degree. This elementary Bini-style fact is valid. But
tensoring a rank-N transform h times makes **rank hN**, because rank counts
coordinate axes; it does not make rank `N^h`.

For example, suppose a fixed exact or approximate uniform supplier has W
role arrays and P rank-one paid rounds. The straightforward tensor-product
execution on W^h roles applies the original program along each of the h
role factors. It costs `h P W^(h-1)` rank-one array jobs, hence `h P/W` per output,
for target rank hN. Even before interpolation this grows linearly in h,
not `(hN)^(1-C)` for any fixed positive C as h tends to infinity. Adding
interpolation points cannot repair that particular accounting.

Ordinary recursion is different: it lifts each coordinate of a fixed rank-N
word to f coordinates and substitutes whole child programs at chronological
paid rounds. The source precompiler expressly does not tensor-power the
logical scalar role program. A Bini reduction must therefore give a new
product/scheduling theorem with rank-multiplicative growth and charge its
complete role and helper interface; the textbook degree statement by
itself supplies neither.

## Open next questions

The most concrete positive task is a coherent completed-child invariant
that preserves both actual inverse realization and polynomial-in-depth
Laurent degree, or an ordered matching that makes all off-diagonal defects
strictly triangular without creating degree-zero cross terms. Such a
matching must cover every round, fresh source, helper, inverse orientation
and source complement. Triangularity does not let one declare contaminated
outputs independently productive: the extraction or cleanup must be costed.

This note rules out neither coherent formal compilation nor every
interpolation construction. The two established failures are narrower:
shared-parameter nominal opposite orientations have the wrong constant
coefficient, and the straightforward tensor-power execution has the wrong
rank/cost scaling for a fixed positive polynomial-in-rank saving.
