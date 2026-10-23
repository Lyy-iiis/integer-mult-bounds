# Frame-carrying swaps cannot lower the fixed itinerary's paid rank mass

Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance. Apache-2.0.
This is a bounded cost screen for the proposed exact repair of the two-full
border. It is not a criticism of the scope claimed by the predecessor, a
physical native replay, a new bound, or a prohibition on changed itineraries.

## The new representation and the relevant question

Dugongue's [PR #4971](https://github.com/CrocSwap/integer-mult-bounds/pull/4971),
at `0130b196145a43a7d305de41f49e56e8e8556378`, replaces 534 three-ADD patterns
in each orientation by direct weighted field exchanges, carrying the frame
labels with the fields. Of these, 43 enter at unequal frames. Its own claim
is explicitly an unchanged recursive profile, with joint schedule/frame
optimization left open.

The identity is the classical signed exchange

\[
d\leftarrow d+a s,\quad s\leftarrow s-d/a,\quad d\leftarrow d+a s
\quad\Longrightarrow\quad(d,s)=(a s_0,-d_0/a).
\]

The question checked here is narrower than that open optimization problem:
can just removing the common-frame contacts fund the 112 rank-one queries
needed to eliminate the residual in the existing two-full border, while
retaining the source's persistent endpoints and dimension-preserving warps?
The answer is **no under this fixed itinerary contract**, by an exact
dimension potential.

## Rank-mass conservation

Let `dim(F_r)` be the dimension of persistent field `r`'s current frame and
let `P = sum_r dim(F_r)`. A scalar contact and a scale do not change `P`.
A frame-carrying exchange permutes two terms and does not change `P`.
A paid climb from `F` to a containing frame `G` changes `P` by its paid rank
`dim(G)-dim(F)`. A retained warp contributes its specified dimension change.
Consequently every legal schedule of these operations satisfies

\[
\sum_{\text{persistent climbs}} r
=P_{\rm final}-P_{\rm start}
-\sum_{\text{warps}}\bigl(\dim F_{\rm out}-\dim F_{\rm in}\bigr).
\]

This does not rely on where the climbs are placed, which scalar contacts
were replaced by exchanges, or which ranks the climbs are grouped into.
The retained source has 632 persistent fields. For both orientations the
exact census gives

| Quantity | Value |
| --- | ---: |
| Initial persistent dimension sum | 171 |
| Final persistent dimension sum | 5,434 |
| Each of the 240 warp dimension changes | 0 |
| Necessary persistent climb rank mass | 5,263 |
| Retained eight owned-center calls | 8 × 8 = 64 |
| Complete paid rank mass | 5,327 |

The owned center is deliberately outside this persistent-field potential:
its CLEAR operations can reset its dimension. Its eight rank-eight calls
are retained as a separate explicit premise. Modifying those calls is a
different optimization question. The argument also excludes neither new
dimension-changing free maps nor changed productive endpoints.

The independently written frame walk reproduces all 534 exchanges and
43 unequal entries, rechecks every persistent scalar contact, upward
transport and warp boundary, and returns exactly the retained histogram
`{1:2201, 2:412, 3:510, 4:127, 5:40, 8:8}`. It verifies the signed exchange
on symbolic two-input rows for all encountered rational coefficients. This
is **not** a second full physical or all-input native interpreter.

## Consequence for the exact two-full repair

The original border endpoint has main block

\[
\Phi_\epsilon(q)=
\begin{pmatrix}q&0\\\epsilon(1-q^{-1})&q^{-1}\end{pmatrix}.
\]

Left multiplication by
`L(epsilon*(q^-2-q^-1))` removes its lower residual exactly. Under the
retained parity convention `q^-2` is free, while this direct construction
uses one additional rank-one query on each of the 112 independent main
pairs. This is a price for this implementation, **not** a lower bound on
every possible repair mechanism.

The target rank mass is 10,750. Two full source calls cost 10,654. Adding
112 rank-one queries costs 10,766, exceeding the target by 16. The exchange
rewrite cannot recover those 16 rank units under the potential's premises.

After the retained strict split, every paid rank is at most three and
every target rank is at least four. For every `0 <= t <= 1`,

\[
\frac{T_t}{P_t}
\le \left(\frac43\right)^{t-1}\frac{10750}{10766}<1.
\]

Thus **every concave moment fails for this completed strict-split bill**.
The statement is stronger than failure at one proposed decimal exponent,
but remains tied to this exact repair and fixed endpoint/warp contract.

## Reproduce and limits

From this directory:

```sh
python3 -I -B -O verify.py \
  --source-word REPO/research/kappa-round3-warp-20261022/ACTUAL-WORD.json.gz
```

Only the standard library is used. Source compressed and payload hashes
are checked before execution. Default verification compares the frozen
receipt without rewriting files. `--write` explicitly regenerates it.
Four rejecting controls per orientation cover a changed climb charge,
changed center charge, changed final frame and wrong signed exchange.
The exact proof is the potential identity above; the finite checks bind
its hypotheses and numbers to this source.

`SOURCES.json` pins the read predecessor and actual source. The predecessor
files are not imported at runtime. Existing native physical correctness,
all-input endpoint replay and physical exchange costs remain inherited or
unproved here. No actual paid transition has been removed by this check.

## Open next question

To lower rank mass, change a term of the potential: productive endpoint
dimensions, a paid center call, or the allowed dimension-changing
interface. To change only the concave rank moment, seek a larger-rank
transport schedule and price its complete strictification; a strictly
separated invoice retaining these total rank masses still fails the
inequality above.
An explicit changed operation with a charged consumer is the first useful
test. Repeating the same monotone frame-retiming scan cannot decide it.

Credit Dugongue for the new carried-frame representation, Cao Yifan for the
round-three word beyond #4610, Cinna Davis and the scalar/helper lineage,
and zxv, Jacob Alan Sussman and all retained native/Clifford authors. The
border and direct repair context belongs to the preceding Yiyang/Dillon
Laurent-border investigation. This small conservation screen makes no
novelty claim for dimension telescoping.
