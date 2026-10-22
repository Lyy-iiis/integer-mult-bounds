# Two-query Laurent border: exact local evidence and a strict split invoice

This package proves a local approximate operator identity and checks a
conditional recursive invoice. **It does not prove an improved multiplication
bound.** At every positive epsilon the endpoint retains a nonzero error.

The central identity, for any invertible operator q, is

\[
\operatorname{diag}(1,\varepsilon)
\begin{pmatrix}1&q\\0&1\end{pmatrix}
\begin{pmatrix}1&0\\-q^{-1}&1\end{pmatrix}
\begin{pmatrix}1&-1\\1&0\end{pmatrix}
\operatorname{diag}(1,\varepsilon^{-1})
=\begin{pmatrix}q&0\\\varepsilon(1-q^{-1})&q^{-1}\end{pmatrix}.
\]

It uses two full native calls, in opposite query orientations, and no thin
query. Two independent fresh diagonal jobs multiply both outputs. The full
conditional target census is `{4:56,7:14,8:94,9:652,17:224}`. Splitting every
paid rank larger than three into disjoint-axis jobs gives
`{1:4656,2:920,3:1386}`, with paid ranks strictly below every target rank.
Exact rational interval arithmetic places this **invoice's** unique raw
crossing in
`(0.00485687557770921195326, 0.00485687557770921195327)`.
Its moment at `C=0.0034` exceeds 28.65.

That split removes a raw-invoice need for tensor powering and completion.
The concrete open question is whether the epsilon-dependent boundary and
nonzero residual can be compiled recursively with a fully charged precision,
storage and uniformity theorem. A raw crossing is not a certified saving, and
no new BIT admission is supplied. See [PROOF.md](PROOF.md) for exact scope.

[LAURENT-PRECISION.md](LAURENT-PRECISION.md) gives a sharp local warning:
independent query errors are amplified by epsilon^-1. Under its stated error
model, target accuracy 2^-k requires query accuracy at least 2^-(2k+1), up to
further fixed guards. Coherent inverse realizations cancel that amplified
block, but such coherence is a separate premise. The note does not establish
the precision bill of the actual native paid circuit.

## Reproduce

Python 3 and its standard library suffice. From this directory, choose a fresh
output directory and run:

```sh
mkdir replay
PYTHONDONTWRITEBYTECODE=1 python3 -B verify_laurent_border.py --out replay/LAURENT-BORDER.json
PYTHONDONTWRITEBYTECODE=1 python3 -B check_actual_matrices.py --out replay/ACTUAL-MATRICES.json
PYTHONDONTWRITEBYTECODE=1 python3 -B check_two_level.py --out replay/TWO-LEVEL-LAURENT.json
PYTHONDONTWRITEBYTECODE=1 python3 -B check_split_budget.py --out replay/SPLIT-BUDGET.json
PYTHONDONTWRITEBYTECODE=1 python3 -B check_split_endpoint.py --engine vendor/clifford_exact.py --out replay/SPLIT-ENDPOINT.json
PYTHONDONTWRITEBYTECODE=1 python3 -B check_dependency_pins.py --out replay/DEPENDENCY-PIN-CONTROLS.json
```

The first checker proves all Laurent coefficients and rejects five mutations.
The second checks six exact canonical native matrix cases, including absolute
phases, at fiber widths 1, 2, 3 and epsilon 1/2, 1/4. It authenticates both
vendored dependencies before importing either. The third checks a literal
two-level substitution and four controls. The fourth proves the complete
split census and interval signs, with three incorrect-invoice controls.
The fifth checks nine phase-preserving split circuit cases and 304 explicit
basis columns, with three controls; its axis-partition argument covers every
fiber width under the retained whole-job-normalizer contract.
The final checker rejects each corrupted dependency before executing it,
including under Python optimization.
Fresh receipts from these commands are in `evidence/`; the original receipts
are retained separately in `evidence/original/`.

The two-level diagnostic is deliberately limited. A fresh opposite-orientation
approximation is not the inverse of the same approximate child. Its unsafe
term is `(delta/epsilon) q^-1(2-q-q^-1)`, which equals −4 at q=−1 and
delta=epsilon. A coherent inverse eliminates this term; delta=epsilon² also
repairs this literal two-level limit. Neither observation establishes a full
native recursive precision theorem. In particular, physically transposing a
recursively substituted child need not produce its inverse. The checker has
an explicit nonsymmetric matrix control for that distinction.

## Open next questions

- **Source sensitivity census.** Propagate an error injected at each actual
  native paid child through the retained chronology, owned spaces and
  whole-job boundaries. Determine which children incur an epsilon-dependent
  amplification, and charge their individual precision and storage costs.
  The query-level precision note is not that source census.
- **Coherent inverse invariant or an approximate compiler.** Either prove a
  source-bound invariant that every inverse request uses the actual inverse
  of the same child realization, including physical transpose and owned-space
  handling, or build a uniform approximate compiler that pays the independent
  errors and necessary inner precision. Nominal opposite orientations and a
  correct constant term alone establish neither result.
- **Separate BIT gate.** Supply or explicitly retain an appropriate BIT
  admission independently. This complex operator identity and its invoice do
  not by themselves establish a BIT saving or a combined multiplication bound.

## Sources and attribution

Yiyang (@Lyy-iiis), with substantial OpenAI Codex and multi-agent assistance.
Apache-2.0; see [LICENSE](LICENSE).

The scientific main baseline is
`b58ad9ef4d4e861b0eaa5dba41742bdc072dca51`. The scoped coordination claim is
[Discussion4611](https://github.com/CrocSwap/integer-mult-bounds/discussions/4611#discussioncomment-19129674).
The parent agent's scoped overlap search read PR4623 at
`fd5d3be12b9d6ee92c8fa089d95bd529c3236563` and Discussion4611. It reported no
other active same-scope claim as of **2026-10-22 18:00 UTC**. This records that
bounded search, not a novelty guarantee or a claim about later activity.

- Dillon (@dillona), [PR4623](https://github.com/CrocSwap/integer-mult-bounds/pull/4623),
  frozen head `fd5d3be12b9d6ee92c8fa089d95bd529c3236563`: prior border
  controllers, interpolation and recovery costs. No novelty claim is made for
  border scaling itself.
- Cao Yifan, [PR4610](https://github.com/CrocSwap/integer-mult-bounds/pull/4610),
  frozen profile head `0ce1b5c9fb7163d0b2f0ac3db95fc418dbbcec62`: the
  productive-helper and paid profiles used here. This package is not a replay
  of that PR's complete native or Lean proof suite.
- The retained native/interface lineage includes Cinna Davis, DaysSky,
  Dugongue, zxv, Jacob Alan Sussman and the authors credited by the inherited
  Clifford/whole-job compiler sources. Vendored code is preserved byte for
  byte with exact provenance in [vendor/NOTICE.md](vendor/NOTICE.md).

`SOURCES.json` records pins and provenance; `MANIFEST.json` records package
file hashes. No source archive, solver search history, or claimed new exponent
is included.
