# Mirrored five-query, two-input partial state

This is a constructive partial state and an exact obstruction to completing its frozen preparation cheaply. It is **not** a complete five-in-fourteen or six-in-seventeen program, and it does not improve the live exponent.

`WORDS.json` contains the two independent input columns, every retained state's literal words, the five-query chronology, and the actual 8×8 monomial letters. Each letter is tensorized separately; the fixed rational coefficients are then added. No inverse is executed by the program. The original inputs are preserved.

Let `S=S0 S1 S2`, let `Vij` swap address bits i and j, and let `Uij` be CNOT i→j. Define

- `P01=S V01 S`, `P02=S V02 S`;
- `P2=S U20 S`, `Q2=S V21 S`, `LA=(P2+2 Q2) V02`;
- `P1=S U10 S`, `Q1=S V21 S`, `LB=(P1+2 Q1) V01`;
- `WA=Z0 Z2`, `WB=Z0 Z1`;
- `JA=Z1 V01 C2`, `JB=Z2 V02 C1`.

The actual calls are

```
u = C0 x
v = C0 y
r = C0(P01 u + P02 v)
s = JA(WA r + LA v/4)
t = JB(WB r + LB u/4).
```

Every occurrence of a letter above means its tensor power at the current width. In particular, `(P2+2Q2)_f` means `P2_f+2Q2_f`, never the tensor power of their sum.

The four individually verified base-word identities give, at every positive width,

```
s = K a x + D_A y
t = D_B x + K b y
D_A = MA C2 + JA P2 V02 C0/4 + JA Q2 V02 C0/2
D_B = MB C1 + JB P1 V01 C0/4 + JB Q1 V01 C0/2,
```

where `K=C0 C1 C2`, `a=Y0 Z1`, `b=Y0 Z2`, and the explicit free monomials `MA,MB` are in the fixture. Thus both independent inputs have genuine target-word components. The residual terms remain essential.

## Evidence

`EXACT.json` records exact Gaussian-rational width-five ranks on all eight source cuts: the successive state potentials are `[80,160,240,320,400]`, and adjoining both targets gives448. `WORD-REPLAY.json` separately records exact normalized matrix replay on independent input blocks at widths1 and2, plus all four individual base-word identities. Those identities, not agreement at finitely many widths, justify the stated all-width residual formula.

`SECTORS-EXACT.json` records the same exact result decomposed by two commuting involutions: `G=diag(b_f,a_f)` on the inputs, and `Pi(x,y)=(V21_f y,V21_f x)`. In the order `(G−,Pi−),(G−,Pi+),(G+,Pi−),(G+,Pi+)`, the target deficits are `[12,12,8,16]` on every width-five cut. Each G sign therefore has deficit24. Output Pauli signs tensorize as `(-1)^f`; the computation does not assume a base minus sign remains minus at even width.

`WIDTH6.json` is only a modular lower-bound screen at prime65537 on the natural lifted hook `H_5 tensor V_8`, cut mask2. It records `[640,1280,1920,2560,3200]` and target joint3584. It is not a full width-six exact audit, an all-cut width-six audit, or an all-width endpoint certificate.

`COSET.json` and `ENDPOINT-OBSTRUCTION.md` establish the stronger endpoint limitation. Projecting onto `(x,HK),(y,HK),(y,HC2),(x,HC1)` leaves two graph rows with independent unit residual coefficients. The target-only subspace is transverse to that old span. Under one fixed finite tensor-word program with fixed scalar coefficients, each extra query contributes at most one copy of the free group algebra, so **at least two further queries per independent pair are necessary**. Three disjoint copies of this frozen five-call state therefore cannot give six targets in seventeen calls. This does not prohibit changing earlier calls, coupling inputs earlier, or a different fixed-width/width-dependent contract.

## Replay

From the package root, using Python3 and its standard library:

```
python3 -B mirror/verify_words.py --out mirror/WORD-REPLAY.fresh.json
python3 -B mirror/verify_cosets.py --out mirror/COSET.fresh.json
python3 -B mirror/verify_exact.py --out mirror/EXACT.fresh.json
python3 -B mirror/verify_exact.py --sectors --out mirror/SECTORS.fresh.json
```

The first two scripts compile only the SHA256-authenticated sibling `arithmetic.py`. The exact hook verifier compiles only the SHA256-authenticated `vendor/pr4688/verify.py`. All accept explicit input paths, and no command accesses the network or imports candidate code from an external scratch path. `--mask 2` is an optional one-cut diagnostic, explicitly marked as incomplete in its receipt.

The optional width-six sample additionally requires NumPy and SciPy:

```
OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 python3 -B mirror/verify_width6.py --out mirror/WIDTH6.fresh.json
```

It reconstructs the literal fixture on `H5 tensor V8`, authenticates both the hook engine and root `modrank.py`, and records the runtime versions. It does not run an all-cut or all-width test.

The source hook engine and phase-repaired-prefix arithmetic are attributed in the package root's notices and source pins. This directory adds the mirrored literal partial word, independent normalized word replay, exact hook reconstruction from that fixture, and the four-coordinate obstruction. The useful next interface is a preparation whose target rows share lower-word residuals, or whose projected residual coefficients are genuine zero divisors; merely closing a finite hook-rank deficit is insufficient.
