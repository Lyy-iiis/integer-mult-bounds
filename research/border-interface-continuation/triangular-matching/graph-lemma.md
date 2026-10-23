# Prefix-reset grading: exact envelope, cover obstruction, and boundary loss

Yiyang, with OpenAI Codex assistance. Local mathematical handoff; no source
paid audit, source modification, or claimed bound improvement.

This note reads the finite compiler contract in
`research/higher-moment-strictification/vendor/FINITE-PRECOMPILATION.md`.
Its relevant requirements are whole-job matching at equal integer ranks,
arbitrary productive inputs, finite acyclic lockstep execution, charged owned
storage, and no independent target credit for copies or blank fields. The
graph below is an additional proposed **error-support envelope**. The finite
compiler document does not itself prove that this envelope occurs.

## 1. Explicit graph and grading assumptions

Fix a depth `g>=0`. Vertices are binary words of length g, with `X=0,Y=1`.
An envelope edge from u to v is allowed if, for some coordinate i:

* all coordinates before i agree;
* `u_i=X` and `v_i=Y`;
* the coordinates after i may be arbitrary in both words.

An integer strict grading h must satisfy `h(v)>=h(u)+1` for every edge.
Its height is `max h-min h`, not the number of levels. This corresponds to
paying at least one positive epsilon valuation for each permitted residual
transfer. It assumes the transfer is present or must be robustly supported;
a term whose coefficient is known zero need not impose an edge.

The motivation for suffix freedom is that an enclosing scalar context can
reset a child's later local Y roles to X while an earlier prefix digit is
raised. This is an assumption about the allowed closure, not a native-word
fact established here.

## 2. Exact minimal height

**Theorem.** The envelope has minimum height

`H_g=2^g-1`.

**Proof.** Give a word its ordinary binary value

`b(u)=sum_i 2^(g-i) u_i`, with i from 1 through g.

An edge is exactly a strict lexicographic increase, hence exactly `b(u)<b(v)`.
Thus b is a feasible grading of span `2^g-1`. Conversely the vertices in
increasing binary order form a directed Hamiltonian path. Every feasible
integer grading increases by at least one on each of its `2^g-1` edges.
This proves both bounds, including `H_0=0`.

One does not need every envelope edge for the lower bound. It is enough to
have each binary-carry edge

`prefix X Y...Y -> prefix Y X...X`.

Those edges alone give the same Hamiltonian path. An actual-source witness
of all these carry edges would therefore establish the height lower bound;
absence of such a witness leaves it a sufficient-envelope calculation.

For additive grades `h(u)=sum_i w_i u_i`, interval separation requires

`w_i >= 1 + sum_(j>i) w_j`.

Equality from right to left yields weights `2^(g-i)`. Equivalently, two
copies of a depth-(g-1) interval must be separated by one step:

`H_g=2 H_(g-1)+1`.

This additive recurrence is not an extra restriction behind the lower
bound: the Hamiltonian-path proof applies to every integer grading.

## 3. What equal-multiplicity matching can and cannot change

Let `N=2^g`. Replace each vertex j on the carry chain by a fiber of L whole
jobs. Suppose every consecutive transition matches all L jobs bijectively
to the next fiber. Allow an arbitrary permutation for every transition;
there is no requirement that it preserve a lane index.

**Cover lemma.** This lifted graph contains L vertex-disjoint directed paths,
each with N vertices. Therefore every strict integer grading still has height
at least `N-1`.

**Proof.** Start from each job in the first fiber and follow the successive
bijections. Every path visits every layer once. Bijectivity makes paths
disjoint and exhausts every fiber.

Consequently, clearing Pascal batch denominators, permuting same-rank whole
jobs, adding identical lanes, or using cyclic Toeplitz translations does not
reduce height if it retains all these transitions as full bijections.
Adding sacrificial vertices without changing the existing edges cannot lower
height either. This is a topological obstruction, independent of how large
the fixed finite supplier is.

The assumption that each binary pattern is a matched whole-job layer needs
to be checked for a proposed Pascal realization. Patterns in a support
envelope are not automatically separately counted productive jobs.

## 4. Sacrificing slots: two different graphs give different answers

For the **full envelope on one copy**, retaining M vertices and their induced
edges leaves a complete ordered DAG, of minimum height `M-1`. Hence height
at most h retains at most h+1 of the original N vertices. If those vertices
are genuinely independent equal-cost target slots, deleting the rest loses
that target credit. Blank storage cannot replace it.

For the **carry chain only**, actual deletion can break paths. After deleting
s vertices from L disjoint N-vertex paths, there are at most `L+s` nonempty
remaining segments containing `NL-s` vertices. Therefore

`height >= ceil((NL-s)/(L+s))-1`.

To reduce this necessary lower bound to h requires

`s >= L*(N-h-1)/(h+2)`.

For N much larger than h this is a sacrificed vertex fraction approximately
`1/(h+2)`, rather than almost all vertices. Thus a small sacrificed fraction
could remove the long-chain obstruction in a sparse actual graph. This does
**not** work for the full envelope, whose forward bypass edges reconnect the
remaining vertices. It also fails if eliminating a sacrificed intermediate
variable creates its bypass dependencies, rather than genuinely cutting
them by a justified reset or independent input.

These are necessary graph bounds, not a valid paid/target invoice. A slot
erased after it has received useful work need not represent an independent
target loss, but proving that requires the actual field identity and lifetime
argument. It cannot be inferred from a vertex label.

## 5. Toeplitz translations and their exposed boundary bill

Consider a concrete noncyclic translation cover of the carry chain. At layer
j, lanes are integers t in `[0,L-1]`; the edge to layer j+1 sends

`t -> t+delta_j`

and is retained only when both lane indices are in range. Put `s_0=0` and
`s_j=sum_(i<j) delta_i`. There are exactly

`max(0,L-(max_j s_j-min_j s_j))`

complete N-vertex lifted paths. This follows by intersecting the intervals
`0<=t+s_j<L`. If the cumulative shift range is less than L, a full path
survives and the height lower bound remains `N-1`.

If the translations wrap modulo L, they are bijections and the cover lemma
applies with no boundary escape. If they do not wrap, transition j omits
`min(L,abs(delta_j))` pair matches. Destroying all complete paths requires
at least L omitted matches in total. These omissions need explicit unmatched
source/exit accounting, replacement work, or a proved genuinely sacrificial
slot interpretation. They are not unchanged pair job counts.

For example, `delta_j=1` at every transition gives height exactly
`min(N,L)-1`: each path advances its lane each time. But it omits one match
per transition, a `1/L` fraction of each L-job batch. This exhibits a real
graph tradeoff, not an impossibility theorem for all Toeplitz methods. If the
omissions can be implemented and fully charged at a tolerable fraction,
height can become independent of g. Additional envelope edges must also be
lifted and checked; arbitrary long jumps can have much larger boundary loss.

A still more general necessary bound counts cut edges in the L original
carry paths. Cutting them into components with at most h+1 vertices needs at
least

`L*(ceil(N/(h+1))-1)`

cuts. This lower bound says nothing about the price per cut. New source jobs,
owned buffers, or replaced paid calls have distinct invoices in the finite
compiler. Replacing epsilon by a Toeplitz shift matrix also needs an actual
operator and arbitrary-input interface argument; graph translation alone
does not furnish an adapter.

## 6. Consequence for the current investigation

There are three distinct statements:

1. **Proved envelope:** unrestricted prefix raise plus suffix reset requires
   exponential height `2^g-1`.
2. **Proved count-preserving cover obstruction:** if the actual support
   contains the carry chain and each matched layer transition remains a full
   equal-multiplicity bijection, replication and lane permutations cannot
   lower that height.
3. **Open constructive route:** demonstrate a sparser actual graph or an
   allowed boundary/cut implementation whose lost pair matches and any new
   scalar, precision, source, exit, or paid costs fit the full invoice.

Neither the source graph nor its paid response has been audited here. In
particular this note does not refute the finite precompilation theorem: that
theorem assumes admitted exact whole-job adapters; the present question is
whether this proposed approximate triangular adapter satisfies its premises.
