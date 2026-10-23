# Read-only review of the phase-twist checkpoint

Prepared by Yiyang with separate OpenAI Codex agent assistance, 2026-10-23.
Scope: bounded independent mathematical and source-code review, not actual
native revalidation. No primary contribution files were modified.

**Conclusion:** no blocking issue was found in the reviewed local formulas
or their stated scope. This conclusion is tied to the exact bytes below.

## Reviewed primary files

Relative to `phase-twist/`:

| File | SHA256 |
| --- | --- |
| `verify.py` | `43c5535db451b1b846018668cb9f79fa4ae0a39ed5240dbbdef0d2cb1173d242` |
| `NOTES.md` | `2003b99efba1e9a2f265fa509e6da64ca8cda186aef6a22e3573ac4480be40c9` |
| `README.md` | `a8f56bcb53f908cda7710d8169408e82e5aca186338a9a83b6694f47901a688e` |
| `RESULT.json` | `1a7ac6ec8adb4637a605a7be93b1aaf08d3df0fe1506483773706bd63963186d` |

The primary frozen receipt's `checker_sha256` matches the reviewed checker.
I read the primary three requested files, checked that binding, and inspected
the receipt status. I did **not** rerun the native source program, its physical
wrapper certificates, or the repository admission suite in this review.

## Independent mathematical evidence

These unchanged files are the separate implementation, relative to this
review's directory (or its copied `independent/` directory):

| File | SHA256 |
| --- | --- |
| `verify.py` | `8bef5e9edd99d2325e099309dc8a88dd1834e70d68abed2b0ab6d91e7da74b89` |
| `NOTES.md` | `8b07f8ec90ceac79ef8d8d08baf923367f42580eb8c3a4c803e42a104e761b6b` |
| `RESULT.json` | `e0ff55bcc3e4374fa5981f7011cd2ff5dd965c714e9eeb26ef92c50f41ec92a2` |

The independent checker imports no primary implementation. Its previously
executed frozen comparison passed under Python `-I -B -O`, using exact
Gaussian-integer polynomial coefficients and separate physical-matrix fault
controls. It proves `Psi^4=I`, determinant `i`, the commuting adjugate inverse,
the nontrivial square, and the stated noncommuting correction-order issue.

For this narrow final review I additionally checked the displayed scalar
counterexample with the independent matrix arithmetic, without changing those
three files:

`Psi(1)Psi(i) - Psi(i)Psi(1)` has sole nonzero entry
`(row 2,column 1) = -2*i*epsilon`.

## Formula and scope findings

1. The fourth-power cancellation is valid for a commuting scalar epsilon and
   `q^4=I`. A commuting fresh factor `d` with `d^4=I` preserves fourth power.
   The normalized-interface restriction is necessary and clearly stated.
2. The adjugate formula includes the required `-i` factor. Its replacement of
   role transpose by physical transpose requires the stated symmetric,
   commuting blocks. The noncommuting variant correctly puts the correction
   on the right. This inverse mechanism is correctly attributed to the prior
   border construction rather than claimed as a new consequence of twisting.
3. The square's lower polynomial and explicit commutation counterexample are
   correct. They prevent treating this local finite-order result as a free
   parity square or a representation of all native Gaussian relations.
4. The paid and split profiles in the prose agree arithmetically with the
   code's displayed source-profile expectations and helper-width counts.
   The code authenticates source bytes before deriving those counts. Counting
   widths is not itself proof of independent target credit or physical
   feasibility; those remain inherited interface hypotheses.
5. The zero extra recursive-call count refers to the final scalar phase only.
   It does not settle scalar cost, precision, physical transpose availability,
   caller matching, or closure for approximate recursive children. The main
   notes expressly preserve those limitations and claim no improved bound.

The primary receipt is source-bound evidence of the code's own checks; this
review's independent evidence is the local mathematics described above.
Neither is a substitute for actual-native replay or a recursive compiler.
