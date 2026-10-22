# Two-full Laurent border and its coherent inverse target

Yiyang (@Lyy-iiis), with substantial OpenAI Codex and multi-agent assistance.
Apache-2.0. This is a local operator family and a changed precision premise,
not a new admitted multiplication exponent. PR4623 is relevant prior work on
border controllers, interpolation and recovery costs; no novelty claim is
made for border scaling itself.

The credited PR4623 source is Dillon (@dillona), frozen head
`fd5d3be12b9d6ee92c8fa089d95bd529c3236563`. The profile source is Cao Yifan's
PR4610 at the frozen head specified below. This package uses those pins and
does not claim to replay their entire native verification suites.

## Exact identity without involutivization

For any invertible operator q, put

    U(q) = [[1,q],[0,1]],       L(-q^-1) = [[1,0],[-q^-1,1]],
    B = [[1,-1],[1,0]],        S_epsilon = diag(1,epsilon).

The matrices use one operator and its actual inverse. They do not assume
q^2=1 or q^4=1. Direct multiplication in any unital operator ring gives

    U(q) L(-q^-1) B = [[q,0],[1-q^-1,q^-1]],

and therefore

    S_epsilon U(q) L(-q^-1) B S_epsilon^-1
      = [[q,0],[epsilon(1-q^-1),q^-1]].              (1)

Only the input boundary contains epsilon^-1; explicitly

    B S_epsilon^-1 = [[1,-epsilon^-1],[1,0]].

For epsilon=2^-k every coefficient is dyadic. The two native calls have fixed
query coefficients +1 and -1. This construction uses no alpha adapter and no
sector decomposition. At finite positive epsilon its lower off-diagonal
entry is not discarded or called zero.

## Source interface and complete optimistic recursive census

The inherited normalized native interfaces are D U(-Q) and D L(Q^-1),
with the same Q on every port. Conjugating main roles by diag(1,-1) changes
the signs and supplies the two factors in (1). Use two distinct fresh
eight-axis D1,D2 blocks, sharing only the central Q. They commute with Q and
the scalar boundaries. The exact main endpoint is

    D1 D2 [[Q,0],[epsilon(1-Q^-1),Q^-1]].           (2)

There are 112 copies of each main role. Both diagonal jobs have rank17;
their central orientations are explicitly opposite. The construction retains
both full native helper sets, with no thin paid query and no productive credit
for owned buffers. Using the pinned PR4610 profile at
`0ce1b5c9fb7163d0b2f0ac3db95fc418dbbcec62`,

    H={4:28,7:7,8:47,9:326},
    P={1:2201,2:412,3:510,4:127,5:40,8:8},

the optimistic recursive census is `target=2H+224 H17`, `paid=2P`, with rank
surplus96. Fixed scalar/route work, epsilon-dependent precision and recursive
product closure are separate costs and are not set to zero by this census.
The diagnostic raw moment root near0.00511047 is not a proved kappa. In
particular, the BIT admission is separate.

For unitary Q,D1,D2 the operator-norm defect in (2) is at most2epsilon.
The input boundary has norm O(epsilon^-1), while the output boundary has norm
at most1 for0<epsilon<=1. This implies a local logarithmic guard-bit bound;
it does not by itself prove that the fully compiled recursive word retains
the same asymptotic bill.

`verify_laurent_border.py` checks every Laurent coefficient, both fresh D
variables, the literal profiles and five rejection controls. Its result is
`LAURENT-BORDER.json`. `check_actual_matrices.py` independently uses the pinned
phase-preserving native Cgate interpreter at fiber widths1,2,3 and epsilon1/2,
1/4. All six actual matrix cases retain the nonzero residual and pass the
coherent inverse matrix check. The result is `ACTUAL-MATRICES.json`.

## Coherent inverse and the distinction from a parity shortcut

Write Phi(q) for the2-by-2 matrix in (1), and let

    J = [[0,1],[-1,0]].

For an actual symmetric canonical q=Q, all entries of Phi(q) belong to its
commuting symmetric operator algebra, and its determinant is1. Therefore

    Phi(q)^-1 = J Phi(q)^T J^-1.                  (3)

Here T transposes both the two role indices and the physical address matrices.
For an arbitrary recursively substituted q_tilde, physical transposition gives
Phi(q_tilde^T)^-1 on the right, not automatically Phi(q_tilde)^-1. A child
transpose-coherence construction is required to remove that distinction.
The native canonical Q,D matrices are symmetric, so at the retained exact
interface the address transpose does not change their coefficients. Equation
(3) is an actual inverse of the entire approximate matrix; it is not obtained
by applying an ideal inverse-Q Pauli correction to a newly generated noisy
supplier. That shortcut need not preserve q q^-1=1 and can leave a nonzero
constant term during product substitution.

There is a concrete coarse-supplier transpose implementation. First normalize
every helper's whole residual to its canonical Gaussian job with the retained
monomial input/output wrappers. The complete native endpoint is then block
diagonal between its main shear and its independent helper Gaussian jobs.
Each helper Gaussian is symmetric. Swapping the two main roles transposes the
main shear while keeping its common D and all helper jobs unchanged. Thus a
transposed full supplier can be executed as an ordinary native invocation
with the main roles exchanged. Reverse the order of the two invocations and
transpose the fixed scalar boundaries to obtain the complete border transpose.
This reverses the order of calls to verified suppliers; it does not reverse
the owned CLEAR/ERASE instructions inside them. Their normal owned setup and
cleanup still run.

For the complete main endpoint D1D2 Phi(q), the adjugate produces
D1D2 Phi(q)^-1. Its extra diagonal factor (D1D2)^2 is a retained Pauli, so the
actual inverse orientation is obtained by the free correction(D1D2)^-2.
Helper Gaussian inverse orientations likewise differ from their canonical
forward jobs by their squared Pauli. These observations supply a precise
endpoint construction target with the same recursive rank profile.

They do not automatically prove recursive inverse coherence. Once native
paid children are approximate, the transposed construction must call the
actual transpose of the SAME child realization. Calling a fresh nominal
opposite orientation is insufficient. A complete proof must bind the physical
transpose, all-owned-space embedding/projection, helper normalization phases,
fixed scalar/route/storage allowance, and the product matching. Neither
`ACTUAL-MATRICES.json` nor the symbolic identity certifies those missing steps.

## Product caution

Equal main ranks are useful, but equal rank alone does not prove that a product
of border controllers has the desired constant term. An inner residual can
meet a later outer boundary with a negative epsilon degree. A global grading
may bound pole order while still allowing a nonzero degree-zero cross term.
The previous involutive-core example exhibited such a term. For the Laurent
core, supplying an actual pair q_tilde,q_tilde^-1 makes identity(1) hold over
their operator ring and removes that particular defect. Full native paid-level
relations and compiler closure remain distinct obligations.

## A strict split invoice without tensor powering

The raw invoice can already obtain strict rank separation by splitting each
paid Gaussian along disjoint axes. Use the exact composition rules

    4 -> 3+1,     5 -> 3+2,     8 -> 3+3+2.

Retain all rank-one, rank-two and rank-three paid jobs. Applied to both full
native calls, these rules preserve the entire paid rank mass and give

    target = {4:56,7:14,8:94,9:652,17:224},
    paid   = {1:4656,2:920,3:1386}.

Now max(paid rank)=3 < min(target rank)=4. This removes a raw-invoice need for
tensor powering/completion; it does not remove the border residual or pay its
precision costs. `check_split_budget.py` uses exact rational enclosures of
logarithms and exponentials. It certifies a moment greater than28.65 at
C=0.0034 and encloses the unique raw crossing in

    (0.00485687557770921195326, 0.00485687557770921195327).

Uniqueness follows by dividing the signed moment by (7/2)^(1-C): every
positive rank exceeds7/2 and every negative rank lies below7/2, so the
quotient is strictly decreasing. This is a conditional invoice statement,
not a new admitted bound. The remaining concrete task is a fully charged,
uniform recursive precision/compiler theorem for the approximate supplier.

The split is a typed endpoint replacement, not just a rank identity. In the
retained lowering contract the complete paid operation has the form
`rmon.then(fourier(n, axes)).then(lmon)`. Retain its actual `rmon` and `lmon`
exactly once around the entire replacement. For every positive fiber width f,
partition the original rank*f Fourier axes into contiguous sets of sizes
part*f, in their original order. The pinned interpreter defines Fourier as
the ordered product of one Cgate per axis; concatenating these piece lists
gives the original literal circuit. This proves equality including absolute
phase and every input column for every f. In inverse orientation reverse the
piece order and adjoint each piece, giving the original adjoint circuit.

`check_split_endpoint.py` verifies that literal equality for the three split
rules at f=1,2,3, with nontrivial illustrative whole-job monomial boundaries
retained once. It also checks all304 basis columns at f=1 and rejects three
corruptions. The general argument retains arbitrary original boundaries; the
finite fixtures do not replay every original native transported frame or
owned-space embedding. The precision/compiler premise remains separate.

## Exact two-level Laurent diagnostic

The public `check_two_level.py` uses no finite-order relation for q. Put

    M_delta(q) = [[q,0],[delta(1-q^-1),q^-1]].

Substituting M_delta(q) for q in the outer two-query word and its actual
inverse for q^-1 makes (1) hold over the full operator ring. The resulting
error has strictly positive epsilon degree even at delta=epsilon. However,
substituting the fresh opposite-orientation approximation M_delta(q^-1)
instead leaves outer upper-right block

    (delta/epsilon) q^-1(2-q-q^-1) E21.

At q=-1 and delta=epsilon its one nonzero entry is exactly-4. Thus this is an
actual two-level constant-term obstruction for the literal query word, not
just a possible grading concern. Taking delta=epsilon^2 repairs this literal
endpoint limit, but no recursive precision or cost theorem is inferred.

The same checker uses a nonsymmetric numeric q=[[1,1],[0,1]] to reject the
claim that physical transpose plus signed role swap automatically implements
the actual inverse. This preserves the transpose-coherence caveat above.
