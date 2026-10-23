# A phase twist restores exact order four at the retained border endpoint

Yiyang (@Lyy-iiis), with substantial OpenAI Codex and parallel-agent assistance.
Apache-2.0. Exploratory continuation; no new bound or recursive compiler claim.

This starts from the two-full Laurent endpoint already recorded in
`research/two-full-laurent-border`, following Dillon's PR4623 border question
and Cao Yifan's round-three native word in the PR4610 lineage. The source
word is pinned by SHA256 in `verify.py`; the paid counts and all408 helper
widths are independently read from those bytes. The local endpoint theorem
and its physical wrapper hypotheses remain inherited, not re-proved here.

## Exact new invariant

Write e for epsilon, q for the common central Gaussian, and

    Phi(q) = [[q,0],[e(1-q^-1),q^-1]],
    Psi(q) = diag(1,i) Phi(q)
           = [[q,0],[i e(1-q^-1),i q^-1]].

Assume q^4=I. Put b=i q^-1 and t=i e(1-q^-1). The lower entry in Psi^4 is

    t(q^3 + q^2 b + q b^2 + b^3)
      = t(q^3 + i q - q^-1 - i q^-3) = 0.

Both diagonal fourth powers are I, hence **Psi^4=I for every e**. This is
an exact polynomial identity, not a limiting argument. It removes the old
Jordan obstruction of the untwisted Phi at q=-1. For instance, Psi(-1)
has distinct eigenvalues -1 and -i even when e is nonzero.

If d=D1D2, the two fresh disjoint Gaussian blocks have d^4=I and commute
with q. Thus A=d Psi also has A^4=I. At the retained **normalized interface**,
the complete endpoint is a direct sum of112 such main pairs and816 independent
canonical helper Gaussians. The one-axis gate is
`C=(I+X)/2+i(I-X)/2`, with eigenvalues1 and i. Hence C^4=I, and each tensor
product of disjoint such gates is separately of order four. Thus the entire
normalized endpoint has fourth power I. Arbitrary physical
input/output charts need not be conjugate charts; the statement does not
automatically apply to the unnormalized serialized native map.

The scalar phase on112 second-main roles adds no recursive Gaussian request.
The formal profiles remain

    targets = {4:56,7:14,8:94,9:652,17:224},
    paid    = {1:4402,2:824,3:1020,4:254,5:80,8:16},
    split paid = {1:4656,2:920,3:1386}.

The target second-main job now includes a fixed scalar i. Undoing that phase
is free scalar work but returns the untwisted Phi and loses this order-four
invariant. A future caller must retain and account for the phased interface.
Scalar, routing, magnitude and precision work remain chargeable; unchanged
rank counts are not a fully costed algorithm.

## Same-profile adjugate at the exact canonical interface

Let J=[[0,1],[-1,0]]. Since det_role(Psi)=i, in the commuting operator ring

    A^-1 = -i d^-2 J A^(Trole) J^-1.                 (1)

For canonical q and disjoint d, all address blocks are symmetric and commute.
Consequently full physical transposition equals role transposition of this
block matrix. The factor d^-2 is a known free even-Gaussian parity and -i is
a fixed scalar phase. This correction does **not** use Psi^2 as a free map.
The associated conformal symplectic identity is

    A^T J A = i d^2 J.

For the complete normalized supplier W, let P exchange main roles with J
and act identically on helper roles. If the canonical helper jobs are F_h,
then

    W^-1 = L P W^T P^-1,
    L = diag(-i d^-2 I_main, F_h^-2 on each helper).

All factors of L are retained free parities/scalar phases. The exact coarse
transpose recipe reverses the two full invocations, exchanges their main
roles, transposes their scalar boundaries, and retains each normal helper
setup and cleanup. It does not reverse owned CLEAR instructions. Under this
inherited exact-interface implementation, the inverse has the same two-full
profile. Computing W^3 also gives the inverse, but would pay three executions
and is not the claimed same-profile construction.

The adjugate argument and coarse-supplier transpose were already available
for the untwisted Phi in the preceding Laurent-border work. They are not
new benefits of this phase twist; the new checked local invariant is order
four. Here the inherited inverse formula simply acquires the scalar -i.

Ordering matters outside the commuting hypothesis. If q and d are symmetric
but do not commute, the role-block determinant argument is not available.
The physical-transpose factorization nevertheless gives

    A^-1 = (J A^T J^-1) (-i d^-2 I).

The correction is on the **right**. Moving it left requires commutation with
d^2. Such a noncommuting A need not have order four. The retained fresh-D
case satisfies the stronger commuting hypothesis used in(1).

## Concrete limits and next test

The exact square is

    Psi^2 = [[q^2,0],
             [e(q^2-q^-1+i q-i),-q^2]].

Its lower entry is generally nonzero and Gaussian-dependent. For q=-1 it
equals2e(1-i). Therefore Psi^2 cannot be substituted for the inherited free
Pauli diag(q^2,-q^2). Nor does this construction preserve commutations:
Psi(q) and Psi(r) can fail to commute for commuting fourth roots q,r. The
explicit scalar example q=1,r=i gives

    Psi(1)Psi(i) - Psi(i)Psi(1) = [[0,0],[-2 i e,0]].

The checker retains these as rejecting controls. Exact finite order is one
relation, not the complete native Gaussian/frame representation.

An arbitrary approximate recursive child may destroy the D-times-two-role
factorization, the commuting q algebra, physical symmetry, helper Gaussian
blocks, or whole-supplier transpose coherence. The new invariant does not
prove those properties and does not repair the independent-error poles.
The smallest useful next task is one actual caller preserving the phased
interface and the needed relations across its real paid-site chronology,
with the complete precision and scalar bill. Merely enforcing fourth power I
on each endpoint is insufficient.

## Reproduction

With the repository source file supplied explicitly:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -I -B -O verify.py \
  --source-word REPO/research/kappa-round3-warp-20261022/ACTUAL-WORD.json.gz
```

The standard-library checker treats e as an indeterminate, checks every
Laurent coefficient modulo the three separate fourth-order relations,
authenticates the actual native word, and rederives the unchanged profiles.
Default execution compares the frozen receipt without rewriting it;
`--regenerate` explicitly replaces that receipt. Five controls reject omitted
phase, a wrong real phase, an uncharged free-parity square, omission of the
inverse scalar correction, and presumed preservation of commutation.
