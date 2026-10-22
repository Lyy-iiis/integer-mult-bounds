#!/usr/bin/env python3
"""Two source-pin controls for the portable exact-matrix checker.

SPDX-License-Identifier: Apache-2.0
Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance.
"""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


def require(ok, message):
    if not ok:
        raise ValueError(message)


def run():
    here = Path(__file__).resolve().parent
    checker = here / 'check_actual_matrices.py'
    cases = [('arithmetic', 'check_border_native_matrices.py', 'Exact arithmetic source pin'),
             ('engine', 'clifford_exact.py', 'Inherited exact phase source pin')]
    rows = []
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    with tempfile.TemporaryDirectory(prefix='laurent-source-controls-') as tmp:
        for flag, name, expected in cases:
            original = here / 'vendor' / name
            raw = original.read_bytes()
            altered = Path(tmp) / name
            altered.write_bytes(raw + b'\nraise RuntimeError("MUTATED_SOURCE_EXECUTED")\n')
            out = Path(tmp) / (flag + '.json')
            child = subprocess.run(
                [sys.executable, '-I', '-O', '-B', str(checker),
                 '--' + flag, str(altered), '--out', str(out)],
                capture_output=True, text=True, env=env, timeout=30)
            require(child.returncode != 0 and expected in child.stderr,
                    'Mutation rejected by the intended source pin')
            require('MUTATED_SOURCE_EXECUTED' not in child.stderr,
                    'Mutated dependency never executes')
            require(not out.exists(), 'No successful receipt after a source mutation')
            require(original.read_bytes() == raw, 'Original dependency remains untouched')
            rows.append({'dependency': name, 'original_sha256': sha256(raw).hexdigest(),
                         'rejected_by': expected, 'rejects_before_execution': True,
                         'successful_receipt_created': False})
    return {'status': 'PASS_TWO_DEPENDENCY_PIN_CONTROLS', 'controls': rows,
            'matrix_checker_sha256': sha256(checker.read_bytes()).hexdigest(),
            'scope': 'Integrity controls for vendored source loading, not a native proof replay.'}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    require(not args.out.exists(), 'Fresh receipt path required')
    result = run()
    result['checker_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'status': result['status'], 'controls': len(result['controls'])}))
