#!/usr/bin/env python3
"""Bounded exact continuation replay; not a recursive compiler certificate.

Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance.
SPDX-License-Identifier: Apache-2.0
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(path):
    # Preserve JSON type distinctions (in particular, true versus 1).
    return json.dumps(json.loads(path.read_text()), sort_keys=True,
                      separators=(",", ":"), ensure_ascii=False)


def inventory(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file()
            and "__pycache__" not in p.parts}


def main():
    package = Path(__file__).resolve().parent
    repo = package.parents[1]
    source = repo / "research/kappa-round3-warp-20261022/ACTUAL-WORD.json.gz"
    before = inventory(package)
    with tempfile.TemporaryDirectory(prefix="border-interface-replay-") as work:
        temp = Path(work)

        def run(script, args=(), receipt=None):
            argv = [sys.executable, "-I", "-B", "-O", "-X",
                    "pycache_prefix=" + str(temp / "pycache"),
                    str(package / script), *map(str, args)]
            subprocess.run(argv, cwd=repo, check=True, timeout=90)
            if receipt is not None:
                generated, frozen = receipt
                require(canonical(generated) == canonical(package / frozen),
                        "frozen receipt mismatch: " + frozen)

        run("phase-twist/verify.py", ["--source-word", source])
        run("phase-twist/independent/verify.py", ["--compare",
            package / "phase-twist/independent/RESULT.json"])
        generated = temp / "compatible.json"
        run("compatible-lift/verify_compatible.py",
            ["--source", source, "--out", generated],
            (generated, "compatible-lift/RESULT.json"))
        generated = temp / "two-query.json"
        run("compatible-lift/two-query/verify.py", ["--output", generated],
            (generated, "compatible-lift/two-query/FINAL-RESULT.json"))
        generated = temp / "source-degree.json"
        run("formal-degree/check_source_degree.py",
            ["--source-word", source, "--out", generated],
            (generated, "formal-degree/SOURCE-DEGREE.json"))
        generated = temp / "toy-degree.json"
        run("formal-degree/child/check_degree.py", ["--out", generated],
            (generated, "formal-degree/child/DEGREE-RECEIPT.json"))
        run("frame-swap-screen/verify.py", ["--source-word", source])
        run("triangular-matching/verify.py", ["--source-word", source,
            "--compiler", repo / "research/higher-moment-strictification/vendor/FINITE-PRECOMPILATION.md"])
    require(before == inventory(package), "replay modified package files")
    print("PASS_BORDER_INTERFACE_CONTINUATION_NO_NEW_BOUND")


if __name__ == "__main__":
    main()
