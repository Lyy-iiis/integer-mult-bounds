# Two-full border: exact interfaces and formal-degree continuation

This checkpoint continues the donor-selected Laurent border whose strict
invoice crosses near `C=0.0048568755777092`. **That number remains a formal
invoice crossing, not an admitted multiplication bound.** The selected
frontier is unchanged. The completed inverse/paid-precision contribution
is separately scoped in [PR #4966](https://github.com/CrocSwap/integer-mult-bounds/pull/4966);
this continuation is a fork handoff, not a second PR.

The useful positive target is now precise: a completed child and its **actual
polynomial inverse** can preserve the two-query border with the correct
constant coefficient and degree growing only linearly with recursion depth.
The missing part is an actual native caller that retains that invariant on
all independent main/helper fields and pays its scalar, storage and bit costs.

| Check | Result and limit | Evidence |
|---|---|---|
| Scalar phase on the second output | Exact fourth power is identity; rank counts unchanged. Commutation and free parity-square relations still fail. | [Phase proof and independent review](phase-twist/README.md) |
| Compatible triangular lift | A finite-group cocycle condition gives a common conjugation. Same central Q with fresh commuting D factors works; arbitrary Gaussian generators need not. | [Compatibility proof](compatible-lift/NOTES.md) |
| Exact repair of the residual | A third query works, but its 112 H1 charge gives paid mass 10,766 versus target 10,750. Every concave moment fails for this bill. A two-query obstruction is confined to the stated even-boundary alphabet. | [Exact identities and scoped obstruction](compatible-lift/two-query/PROOF.md) |
| Formal degree and interpolation | Actual inverse pairing has linear degree in the toy core. Independently generated opposite orientations already have the wrong constant term at depth two. Actual source chronology gives the upper envelope 23D, not a degree lower bound or an admitted compiler recurrence. | [Degree proof and exact checks](formal-degree/README.md) |
| Ordered matching | Prefix intervals are a constructive local rule. Global diagonal scaling is a valid conditional route; the exponential height result applies to a stated support envelope, not the measured completed matrix. | [Matching proof and source witness](triangular-matching/README.md) |
| Carried-frame swaps | PR #4971 preserves the fixed dimension potential: 5,263 persistent rank units plus 64 center units per call. That change alone cannot fund the direct repair. Changed warps, centers and target interfaces remain outside this screen. | [Source-bound cost screen](frame-swap-screen/NOTES.md) |

## Reproduce

From the repository root:

```sh
python3 -I -B -O research/border-interface-continuation/verify.py
python3 scripts/research_package.py --package research/border-interface-continuation --check-only
```

The root replay runs the eight declared exact checks, compares generated
receipts using typed canonical JSON, uses fresh temporary outputs and
bytecode-cache namespaces, and checks that package files remain unchanged.
Only the standard library is needed. The live external inputs are the
retained round-three `ACTUAL-WORD.json.gz` and the finite-precompiler note;
their exact source pins are in SOURCES.json.
Subdirectories retain their scoped proofs, frozen receipts, source pins and
review notes; VALIDATION.md records one proof-header whitespace normalization. The independent phase implementation imports no primary
arithmetic; the compatible-lift checker explicitly vendors the primary
phase arithmetic. Independence is not claimed for that reused implementation.

See [VALIDATION.md](VALIDATION.md) for the actual runtime and unrun checks,
[OVERLAP.md](OVERLAP.md) for bounded overlap coverage, and [TASK.json](TASK.json)
for the changed task premise and structured next questions. Source-authenticated
arithmetic is not a full physical Clifford replay, a Lean proof, a numerical
interpolation theorem, or a BIT admission.

## Open next questions

1. Realize the polynomial child/actual-inverse pair across the actual native
   paid-site chronology, including fresh D factors, all helpers, workspace
   restoration and whole-job frames. Isolated inverse macros and isolated
   fourth-order endpoints do not give that structured caller.
2. Finish the ordered-matching construction and a sufficiently small global
   triangular grade range, then price extraction of every independent output. Triangular
   contamination cannot be silently credited as clean productive output.
3. A cheaper exact correction must change a stated premise of the two-query
   or dimension-potential screens, such as use of intermediate states, center
   calls, or the allowed physical operation family. A new unpaid term is not
   supplied by unchanged frame retiming.

## Credit and coordination

Dillon (@dillona), PR #4623, supplied the preceding border/recovery questions;
Cao Yifan supplied the actual round-three native word in the PR #4610 lineage;
Jacob Alan Sussman and the finite-precompiler contributors supplied the
inherited compilation framework. Dugongue's PR #4971 supplied the new
carried-frame representation checked in the cost screen. Cinna Davis,
DaysSky, Dugongue, zxv and the retained native/Clifford/helper lineage keep
their attribution. The cocycle averaging, three-shear identity and dimension
telescoping are classical arguments, not claimed as new general methods.

Prepared by Yiyang (@Lyy-iiis), with substantial OpenAI Codex and parallel-agent
assistance, Apache-2.0. Separate-agent checks are not independent human or
formal-kernel acceptance. The [canonical handoff](https://github.com/CrocSwap/integer-mult-bounds/discussions/4611#discussioncomment-19129674)
links the earlier [two-full border](https://github.com/Lyy-iiis/integer-mult-bounds/tree/e0bebf54d8cf8549ead24aef929fc40e44313bc0/research/two-full-laurent-border)
and this continuation. Base main is `b91956876e5b4122fd89179f1b57557ff8378f15`,
priority revision 7. No merge or selected-frontier change is requested.
