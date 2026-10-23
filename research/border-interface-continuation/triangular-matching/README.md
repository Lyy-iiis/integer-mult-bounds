# Triangular matching: a constructive condition and its grading cost

Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance.
SPDX-License-Identifier: Apache-2.0

This is a bounded continuation of the two-full Laurent border investigation.
It supplies a matching convention, an exact conditional graph calculation,
and one actual native response. **It does not construct an admitted uniform
supplier, improve the multiplication bound, or prove that every matching
has exponential precision cost.** The potential positive route is to finish
the finite compiler with a triangular endpoint at local parameter one, and
apply a single new global diagonal scaling afterward.

The finite compiler is Jacob Alan Sussman's Theorem1G flow, upstream commit
`563b4e6e913625637f36ba7869bf5fcd0dd4975a` / PR4268, in the repository's
source-bound `FINITE-PRECOMPILATION.md`. The Laurent border and actual paid
sensitivity analysis precede this note. The source response below uses the
round-three Cao Yifan native word in the PR4610 lineage; its serialized word
is unchanged at repository commit `cef4b52f2a59009865bf8eabde1be3f159063703`.
This checker independently replays a single scalar column rather than
importing the preceding paid-sensitivity implementation.

## 1. A natural Pascal matching with intervals

The direct split invoice is

```
targets {4:56,7:14,8:94,9:652,17:224}
paid    {1:4656,2:920,3:1386}.
```

Use one distinct alphabet letter for every productive target role, retaining
its rank. The multinomial unit count in the compiler is precisely the number
of words with each rank multiplicity. A parent unit labelled `wa` sends its
paid-round-j job to target role `a` of child unit `w`. If the parent class
dilation is rho, then these two jobs have the same rank

`r_j * rho * c(w) * rank(a)`.

Thus deleting the last letter realizes the integer Pascal bijection without
fractional jobs. Use this convention at every round. Order words first by
their prefix, then by their last letter, choosing every X role before its
paired Y role. All targets of one child unit then lie in a contiguous block
of parent-unit labels. More precisely, the following is a sufficient local
condition for arbitrary scalar mixing inside a child unit:

`child u before child v => every parent slot of u before every parent slot of v`.

This interval condition is stronger than merely putting each paired X before
Y. If a lower-level error moves from unit u to unit v, subsequent scalar
operations inside either unit cannot turn that into a move to an earlier
parent block. Autonomous helper targets must belong to the interval too;
their exact local endpoint does not prevent a descendant fault from reaching
them through a parent context.

This describes a matching **inside a class**. It does not yet provide the
simultaneous ordering of the whole finite compiler. Unmatched child targets
are fresh arbitrary source arrays, and must receive compatible labels. The
smaller programs completing source complements and exits also need a
compatible order. Owned centers are not new independent outputs; a child
receives their actual correlated values, must complete before the parent
reads or clears them, and must respect the same ordering. Whole-job adapters
must remain field-local in this order. The inverse orientation must either
use an actual coherent inverse preserving the order, or supply a separate
proof; a nominal opposite Gaussian is not automatically that inverse.

## 2. Why global scaling is a real new possibility

Work first with exact linear arithmetic, before imposing a rounding policy.
Suppose a complete finite program at local epsilon=1 has endpoint W whose
diagonal blocks are exactly the desired independent Gaussian jobs, and whose
off-diagonal blocks form an acyclic directed graph. Give its vertices integer
grades h, increasing by at least one along each nonzero off-diagonal block.
For `D_delta=diag(delta^h)`, the actual circuit

`D_delta W D_delta^-1`

has the same desired diagonal and every off-diagonal block is multiplied by
`delta^(h_out-h_in)`. It therefore converges to the desired endpoint as
delta tends to zero. This is direct scaling of the whole finite program;
it does not extract its diagonal for free. In particular an off-diagonal
term constant in the old local epsilon does not by itself refute this route.

The cost question moves to the grade span H and the actual internal
sensitivity. Normalize the smallest grade to zero. The input scaling can
have norm delta^-H. A generic sufficient
independent-error policy then asks for `(H+1)k+O(f+1)` internal bits to achieve
k output bits, provided the fixed-word norm constants have logarithm O(f+1).
This is only a conservative sufficient policy, not a necessary tariff at
every paid site. Finiteness of H alone does not make H*k an additive guard.
A sharper paid-site or correlated execution proof could have a lower price.

## 3. The exact conditional height, and an honest boundary escape

If raising a prefix X to Y permits resetting all later role digits, then
binary words of length g form the lexicographic support graph. Its minimum
integer grade span is exactly `2^g-1`, not g. The smaller set of binary-carry
edges already forces the same height. `graph-lemma.md` proves this and the
following distinctions:

* Equal-multiplicity bijective covers, lane permutations, and cyclic shifts
  retain the chain height.
* In a sparse carry-chain graph, genuine cuts can reduce height; noncyclic
  lane translation by one gives height at most L-1 at the cost of omitting
  one match per L-job batch.
* In the full lexicographic envelope, forward bypass edges defeat that
  simple sparse-chain argument. Every omitted match still needs actual
  source, exit, replacement-work, and productive-credit accounting.

These are conditional graph results. They are **not** the measured support
or height of the actual all-epsilon-one completed matrix. Correlated
contributions from different paid sites can cancel. Conversely, merely
ordering each local X/Y pair proves neither a small global height nor the
required cancellation.

## 4. One concrete source reset and an integer-flow location

The checker authenticates the actual word and reads the backward program's
event6276:

```
["climb","warp_retimed",126,0,137,1]
frame0 = [] ; frame137 = [45].
```

At this upper-call site, the selected original Y14 input gives scalar
prefix coefficient1 on register126, while a unit injection there has final
X14 coefficient−1/2. This is the same chosen input normalization used by the
actual Laurent-wrapper sensitivity analysis: set the common input to
`Y14=Q D_lower^-1 delta_0`, up to the common sign. The source input logical
X14 and Y14 then both equal delta_0. The final observation includes the
known invertible output chart; no physical input chart is silently dropped.

Now normalize a child's two main outputs to the same forward Gaussian
`G=dq`, using free parity on its second output. Its cross-copy defect is
`eta G(q-I)`. At an old-frame-zero rank-one parent climb, the complete
Gaussian factorization has the form `G=L q R`, with monomial right matcher
R. In moving output coordinates the relative defect is
`eta R^-1(q-I)R`. Any monomial sends delta_0 to a phased basis vector. The
canonical rank-one Gaussian has diagonal `(1+i)/2` at every basis vector,
so this defect has delta_0 coefficient `eta(-1+i)/2` regardless of the
matcher's offset or phase. This remains true with arbitrary spectator axes.

All subsequent ideal climbs are identity in moving logical coordinates.
The actual homogeneous linear/quadratic warp maps fix address zero and
cannot send a nonzero address to zero. The scalar suffix therefore gives
the nonzero labelled coefficient

`1 * (-1/2) * (-1+i)/2 = (1-i)/4`, up to the common wrapper sign.

This binds one actual Y-to-X response, rather than treating a rank count as
an adapter. It is a **single independently labelled child-defect coefficient**.
It does not prove that the sum of all descendant defects at epsilon=1 is
nonzero, nor establish every carry edge needed at arbitrary depth.

The response can occur in a literal finite-flow slice already at N=289.
Here m=17 and G=2. The root has56² rank-four-pair units; a rank-one child
class has all1040 one-letter units. In particular it contains the rank17
units X14 and Y14. At their selected rank-one paid round, the next child
class pairs these units as its X14/Y14 targets. Each parent has its own
rank289 main outputs. These four arrays are fresh full-rank sources of the
flow, not blank storage or free duplicate output credit. The checker verifies
these integer counts; it does not enumerate a complete winning compiler.

## 5. What would make the continuation actionable

A positive next certificate needs the complete matching, including source
complements and exits, plus the actual noncancelling block support at local
epsilon=1. It should report a feasible global grading and the precision
tariff at the remaining paid leaves. A boundary construction must charge
every omitted match and any extra arrays. The raw .0034 moment margin is
only about0.269% of paid moment, so a proposed loss fraction is a screening
number rather than permission to omit its invoice.

Run the read-only check:

```
PYTHONDONTWRITEBYTECODE=1 python3 -I -B -O verify.py \
  --source-word REPO/research/kappa-round3-warp-20261022/ACTUAL-WORD.json.gz \
  --compiler REPO/research/higher-moment-strictification/vendor/FINITE-PRECOMPILATION.md
```

The default compares the full frozen receipt. `--regenerate` is explicit.
The verifier uses only the standard library and does not import predecessor
checkers. Source pins are decoded-payload SHA-256 for the gzip word and byte
SHA-256 for the compiler text; `SOURCE-PINS.json` records both.
