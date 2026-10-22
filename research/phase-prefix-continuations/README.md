# Two saturated five-call prefixes and a uniform endpoint screen

This handoff records two literal programs on two independent inputs. Both pass all eight exact width5 hook tests at the full five-call potential400 and target joint448. They also pass sampled width6 lifted-hook tests. Nevertheless, neither specific preparation can finish both targets with only one further paid call in the fixed uniform word model. The obstruction is an exact free-module calculation, not a numerical rank failure.

No completed small unit, improved exponent, global no5-in14 theorem, or global no6-in17 theorem is claimed. The already selected repository frontier is unaffected.

The hook engine and original two-image prefix are from [PR4688](https://github.com/CrocSwap/integer-mult-bounds/pull/4688) by lee-phys; the phase repair and residual arithmetic are from [PR4710](https://github.com/CrocSwap/integer-mult-bounds/pull/4710). See [NOTICE.md](NOTICE.md) for attribution and [PINNED-SOURCES.json](PINNED-SOURCES.json) for exact commits and source hashes.

## Programs and evidence

| Program | Exact width5 | Sampled width6 | Exact word replay | Uniform endpoint screen |
|---|---|---|---|---|
| Mirrored pair | All8 cuts:80,160,240,320,400; joint448 | Mask2:640,1280,1920,2560,3200; joint3584 | Normalized Gaussian rationals at widths1/2; separate base-word identities | At least2 further paid calls |
| Staggered pair | All8 cuts:80,160,240,320,400; joint448 | Masks2/3:640,1280,1920,2560,3200; joint3584 | Normalized Gaussian rationals at widths1/2; separate base-word identities | At least2 further paid calls |

The width6 receipts are finite-field screens modulo65537 on the natural lifted hook H tensor V. They do not assert all-width saturation. The width1/2 literal controls are distinct from the all-width word identities: only equalities between individual base-letter products tensorize automatically. Coefficients such as2 and1/4 stay fixed after tensorization; a sum is never tensorized as if it were a base letter.

See `mirror/README.md` and the two directories' exact word fixtures/verifiers for definitions. Both programs retain the original independent inputs and every intermediate register. Information preservation is therefore explicit.

For the staggered program, let Cj=((1+i)I+(1-i)Xj)/2, K=C2 C1 C0, S=S0 S1 S2, U=CNOT(0->2), V=SWAP01, P=SUS, Q=SVS, Q2=S SWAP21 S, W=Z0Z2, N=Z1V, J=NC2, T=SWAP02, and L=NT. Its five paid calls are

1. u=C0x.
2. v=C0(P+2Q)u.
3. r=L^-1 J(Wv+Ty).
4. t=C0(P+2Q)r.
5. z=J(Wt+Q2r+Pv).

All other operations are free. In particular L^-1JT=C0 exactly.

## Why the hook tests do not imply a completion

For the lower bound enlarge the allowed free group to H, the finite group of all8x8 monomial matrices with fourth-root-of-unity entries, retaining central phases, and let A=C[H]. This contains the actual free letters, so an obstruction after this enlargement also applies to the original program. Fix a finite straight-line word model whose scalar coefficients are independent of tensor width. Width-dependent signs already represented by central phase letters are permitted. This handoff does **not** silently extend the theorem to arbitrary width-dependent scalar formulas.

A uniform identity between finite sums of tensorized actual base words is an identity in the group algebra. To see this, for distinct matrices g1,...,gn choose a complex linear functional ell taking distinct nonzero values on them. Such ell avoids finitely many proper hyperplanes. Applying ell^tensor(f) to a relation for f=1,...,n gives a nonsingular Vandermonde system, so every coefficient vanishes. Actual matrices differing by a central phase remain distinct elements throughout.

Projection of the group algebra onto any union of left H-cosets commutes with the left action of A. A retained register generates at most dim(A) dimensions under arbitrary free processing. One new paid call adds only one register, so it can increase the projected span by at most dim(A), even if arbitrarily many free copies and combinations follow.

For the mirrored program project onto

    (x,HK), (y,HK), (y,HC2), (x,HC1).

Only the two final registers survive. Their residual-coordinate block is diagonal with monomial-unit entries; their target-coordinate block is diagonal with monomial-unit entries. Their span is a graph, transverse to the pure two-target space.

For the staggered program project onto

    (x,HK), (y,HK), (x,HC2), (y,HC2).

Only r and z survive. Both the target and residual blocks are triangular with invertible monomial diagonals. The same graph conclusion follows.

In each case adjoining the two pure target directions to the old projected span increases dimension by2dim(A). Thus **at least two new paid calls are necessary**. The exact coset checkers verify every required membership/nonmembership using Gaussian-rational8x8 matrices; a word g belongs to Hh precisely when gh^-1 is a fourth-root monomial. The receipts retain permutations and fourth-root phases of the required units.

For three disjoint preparations, the direct-sum graph deficit is6dim(A), so the particular15-call preparation cannot be completed with only two more calls. This rules out that proposed6-in17 continuation, not6-in17 by other programs. The analogous two-pairs-plus-two-call-prefix preparation also fails the proposed5-in14 continuation, since even the two paired blocks already require four further registers in this projection.

## Open next questions: a concrete interface

Further hook maximization alone will repeat this failure. A useful next program must make distinct retained rows share a low-order residue coordinate with independently differing target coefficients, so a free combination can cancel residue; or use controlled sector coefficients with genuine kernels while preserving every independent input complement.

A simple full three-call owner pipeline cannot supply such a channel merely by adding old pair states. If its fresh owner z has coefficients C2, C1C2 and K in three successive registers, these have respective column support sizes2,4,8 and hence are distinct left H-cosets with unit coefficients. The projection onto z is injective on the A-span of those registers. No nonzero combination of them is supported only on the old inputs. The apparent spare16 hook directions of the last call therefore do not by themselves constitute a usable independent output channel. A promising partial-productive interface must break this injectivity explicitly.

## Reproduction

Standard Python3 suffices for the exact word, coset and width5 verifiers. Run from this directory, writing receipts to a fresh directory:

```sh
python3 -B reproduce.py --out /path/to/fresh-results
```

The optional width6 screens need NumPy and SciPy. They are deliberately separated from the exact standard-library gates. Examples:

```sh
OPENBLAS_NUM_THREADS=1 python3 -B mirror/verify_width6.py --out /path/to/mirror-width6-mask2.json
OPENBLAS_NUM_THREADS=1 python3 -B staggered/verify_width6.py --mask 2 --out /path/to/staggered-width6-mask2.json
OPENBLAS_NUM_THREADS=1 python3 -B staggered/verify_width6.py --mask 3 --out /path/to/staggered-width6-mask3.json
```

All executable dependencies are authenticated before compilation; their exact bytes are compiled directly rather than loaded through a bytecode cache. The vendored predecessor is unchanged. `MANIFEST.json` records the distributed bytes.
