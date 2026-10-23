# Toy Laurent degree handoff

`FORMAL-DEGREE.md` proves the all-depth statements and states their limits.
`check_degree.py` is a portable standard-library exact corroboration, independent
of the source evaluators. `DEGREE-RECEIPT.json` retains its result.

The useful positive interface is a **polynomial pair consisting of one child
and its actual inverse**. The two-call recursion then remains a proper border
with degree at most its depth. Fresh opposite-orientation substitution instead
has a wrong constant term at depth2, despite a common gauge limiting its Laurent
degree to a linear interval. A multivariate/superincreasing repair works for the
synchronized toy word, with degree2^depth-1. A fixed valid border still has only
linear-degree growth under tensor powers; full native extraction costs remain
unproved.

Replay in an empty output location:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B check_degree.py --out /fresh/DEGREE-RECEIPT.json
PYTHONDONTWRITEBYTECODE=1 python3 -I -O -B check_degree.py --out /fresh/OPTIMIZED-RECEIPT.json
```

Every scientific check raises explicitly on failure and remains active under
`-O`. A corrupted actual inverse must be rejected. An earlier assertion-based
optimized run did not execute its scientific checks and is superseded by the
retained explicit-guard normal/optimized replay.

No third-party dependency, network, actual native replay or new bound is claimed.
