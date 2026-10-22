# Vendored dependencies

These two files are retained byte for byte. Existing headers are preserved;
the repository's Apache-2.0 license is supplied at `../LICENSE`.

`check_border_native_matrices.py`

- Author: Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance. The
  frozen file's original attribution header is preserved byte for byte.
- SHA256: `119d89830ebc28ba66bdff8a4fbeaa18a3a5d746f9f70d32652cd067e72077ea`.
- This package imports only its exact Gaussian-rational matrix arithmetic and
  source-reader helpers. Its retained standalone historical CLI is not run by
  this package. The public replay uses the Laurent identity, without an alpha
  adapter or sector decomposition.

`clifford_exact.py`

- SHA256: `2982ead07721e83358dc67c6f49c2b4c16a236a6bebdfd72f58221be1f5d0962`.
- Exact inherited repository path, as retained by PR4654:
  `research/native-quotient-interface/v/research/t74-native-fast/vendor/native/new/code/borrow/vendor/clifford/clifford_exact.py`.
- Its original header describes an exact Gaussian-dyadic compiler with literal
  circuits retaining global phases. No individual author is newly assigned by
  this package. Credit the retained Clifford/native compiler lineage and its
  source authors, including zxv and the authors named in upstream notices.

The PR4654 interface notice credits DaysSky; Cao Yifan's PR4610 helper/map
search; Ryanson Jonathan's PR4604 endpoint objection; Cinna Davis and the
DreamingOfClouds/eumemic, PR589 and PR4470 supplier/controller lineage; Rohan
Arun and PR4636; Dugongue; lm1909; Dillon; zxv; Jacob Alan Sussman; and all
authors named in the retained Clifford and whole-job compiler sources. This
notice preserves that attribution without claiming independent human review.
