# Executed validation and limits

Prepared by Yiyang with substantial OpenAI Codex assistance, 2026-10-23.

The integrated command `python3 -I -B -O
research/border-interface-continuation/verify.py` passed on CPython 3.14.5.
All current registered subchecks passed, generated receipts matched typed
canonical JSON, and the package contents remained unchanged. Temporary
outputs and bytecode-cache prefixes were outside the package. An AST scan
found no Python `assert` statements in the included checker sources; the
toy-degree note records and supersedes its earlier unchecked optimized run.

`python3 scripts/research_package.py --package
research/border-interface-continuation --check-only` passed metadata and
Git/source pins. The manifest requests the repository's generic Python 3.12
environment; Python 3.12 was not available locally, and no hosted CI run is
claimed for this fork-only continuation.

The separate [PR #4966](https://github.com/CrocSwap/integer-mult-bounds/pull/4966)
passed its registered Python 3.12 replay and unchanged-input check in
[Actions run 39900321912](https://github.com/CrocSwap/integer-mult-bounds/actions/runs/39900321912)
at head `039b6ea51ab7a7efb38fc6851f345839683251b0`. That CI result applies to
its inverse/paid-precision package, not to the additional files here.

The phase-twist subdirectory retains an independent exact implementation
and byte-bound review. Other checks state their own implementation sharing
and proof scope. Neither separate agents nor local exact checks constitute
independent human acceptance or a formal-kernel proof. No selected cold
replay, complete physical Clifford lowering, Lean build, finite-precision
interpolation theorem, outer multiplication theorem or BIT admission was
run or established in this continuation.

Packaging removed a Markdown hard-break suffix from the toy proof license line and refreshed its two containing manifests. All checker and receipt bytes stayed unchanged; the scratch predecessor remains intact.
