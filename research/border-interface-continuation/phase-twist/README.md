# Order-four phase twist of the two-full border

Multiplying the second main output of the retained Laurent border by the
free scalar i gives the exact identity

    Psi_e(q) = [[q,0],[i e(1-q^-1),i q^-1]],
    q^4=I  =>  Psi_e(q)^4=I.

This local invariant holds for every e, including nonzero e. Commuting fresh
Gaussian factors D1,D2 and all816 independent canonical helpers preserve it
at the whole normalized two-full endpoint. The scalar phase changes no paid
rank count. **This is a continuation checkpoint, not a new bound, native
admission, or recursive-precision theorem.**

[NOTES.md](NOTES.md) states the proof, exact interface, invoice and limits.
[verify.py](verify.py) checks every coefficient with Gaussian-integer
polynomials, reads the actual source word to bind both paid profiles and
all408 helper widths, and checks five rejection controls and an explicit
commuting-input counterexample. [RESULT.json](RESULT.json) is its frozen
receipt. Default verification does not rewrite files.

The known same-profile adjugate inverse survives with an extra -i correction;
that inverse mechanism was already available for the untwisted border and
is not claimed as new. The new order-four relation still does not give a
free parity square or a Gaussian representation:

    Psi_e(q)^2 lower entry = e(q^2-q^-1+i q-i),
    [Psi_e(1),Psi_e(i)] lower entry = -2 i e.

The first expression is generally nonzero; the second shows that commuting
inputs need not give commuting twisted maps. Those failures prevent using
finite order alone as a recursive closure theorem.

## Reproduce

From this directory, supply the unchanged repository source explicitly:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -I -B -O verify.py \
  --source-word REPO/research/kappa-round3-warp-20261022/ACTUAL-WORD.json.gz
```

Only Python's standard library is required. The source SHA256 is
`7679daa4ec6a40f56fc7f0202379a6f454310e94945aba4f48beaaaafb838d05`;
its Git blob is `46d929df83817b85a5387bcdb9745e0627d6366e`. The source is
unchanged at the preceding border pin
`0ce1b5c9fb7163d0b2f0ac3db95fc418dbbcec62` and research base
`cef4b52f2a59009865bf8eabde1be3f159063703`.

## Open next question

Find a compatible multiplication/caller invariant retaining this phased
interface across the actual paid-site chronology, with consistent free
frame/warp operations and a charged scalar and precision budget. An
approximate child may destroy the native D-times-two-role factorization;
this check does not repair that problem. Finite order of isolated returned
maps and inverse pairs alone are insufficient.

## Credit

Dillon (@dillona), PR4623, supplies the preceding border/recovery question.
Cao Yifan supplies the actual round-three word in the PR4610 lineage and
its paid/helper invoice. The earlier [two-full Laurent-border checkpoint](https://github.com/Lyy-iiis/integer-mult-bounds/tree/e0bebf54d8cf8549ead24aef929fc40e44313bc0/research/two-full-laurent-border)
supplies the raw endpoint, normalization hypotheses and adjugate construction.
Their native, Clifford, helper, owner and compiler lineage retains its credit.
This phase-twist check was prepared by Yiyang (@Lyy-iiis), with substantial
OpenAI Codex and separate-agent assistance. Apache-2.0.
