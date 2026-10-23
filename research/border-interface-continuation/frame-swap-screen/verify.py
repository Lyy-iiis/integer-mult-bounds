#!/usr/bin/env python3
"""Source-bound frame-dimension screen; no native/physical admission.

Yiyang (@Lyy-iiis), with substantial OpenAI Codex assistance. Apache-2.0.
"""
import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

SOURCE_SHA = '7679daa4ec6a40f56fc7f0202379a6f454310e94945aba4f48beaaaafb838d05'
PAYLOAD_SHA = 'cfcd36b40326d7a5815e1db5313444379b3fb756b27d5201c561574c085cc0dd'
PROFILE = {1: 2201, 2: 412, 3: 510, 4: 127, 5: 40, 8: 8}


def need(ok, message):
    if not ok:
        raise ValueError(message)


def closure(basis):
    result = {0}
    for b in basis:
        result |= {x ^ b for x in tuple(result)}
    return result


def census(c, program):
    dims = list(map(len, c['frames']))
    spans = list(map(closure, c['frames']))
    current = list(c['start'])
    climbs, centers = Counter(), Counter()
    warp_delta = 0
    for event in program:
        op = event[0]
        if op == 'climb':
            _, _, role, old, new, rank = event
            need(current[role] == old, 'climb source frame')
            need(spans[old] < spans[new], 'strictly nested climb')
            need(rank == dims[new] - dims[old], 'charged climb rank')
            current[role] = new
            climbs[rank] += 1
        elif op == 'warp':
            _, role, _, old, new = event
            need(role[0] == 'L', 'persistent warp premise')
            need(current[role[1]] == old, 'warp source frame')
            need(dims[old] == dims[new], 'dimension-preserving warp premise')
            warp_delta += dims[new] - dims[old]
            current[role[1]] = new
        elif op == 'center':
            _, _, old, new, rank = event
            need(rank == abs(dims[new] - dims[old]), 'charged center rank')
            centers[rank] += 1
        elif op == 'weighted_swap':
            _, left, right, a, b = event
            need(a * b == -1, 'weighted swap signs')
            current[left], current[right] = current[right], current[left]
        elif op == 'scalar':
            gate, frame = event[1:]
            kind = gate[0]
            roles = gate[1:3] if kind in ('add', 'copy') else gate[1:2]
            for role in roles:
                if role[0] == 'L':
                    need(current[role[1]] == frame, 'persistent scalar contact frame')
        else:
            need(op in ('phase', 'adapter', 'residual_adapter'), 'known annotation')
    need(current == c['final'], 'terminal frames')
    start = sum(dims[x] for x in c['start'])
    final = sum(dims[x] for x in c['final'])
    mass = sum(rank * count for rank, count in climbs.items())
    need(mass == final - start - warp_delta, 'dimension telescoping')
    return {
        'initial_persistent_dimension_sum': start,
        'terminal_persistent_dimension_sum': final,
        'warp_dimension_delta': warp_delta,
        'paid_climb_mass': mass,
        'paid_center_mass': sum(rank * count for rank, count in centers.items()),
        'paid_profile': dict(sorted((climbs + centers).items())),
    }


def reconstruct(c, program):
    """Separate implementation of the published greedy frame-carrying rule.

    Source scalar frames and warp endpoints remain fixed. No source module is
    imported. Only frame/cost bookkeeping is replayed, not physical maps.
    """
    dims = list(map(len, c['frames']))
    spans = list(map(closure, c['frames']))
    current = list(c['start'])
    events = [deepcopy(e) for e in program if e[0] != 'climb']
    output = []
    swap_count = unequal = 0
    coefficients = set()

    def transport(role, frame):
        old = current[role]
        if old != frame:
            need(spans[old] < spans[frame], 'reconstruction upward premise')
            output.append(['climb', 'reconstructed', role, old, frame,
                           dims[frame] - dims[old]])
            current[role] = frame

    j = 0
    while j < len(events):
        triple = events[j:j+3]
        match = None
        if len(triple) == 3 and all(e[0] == 'scalar' and e[1][0] == 'add'
                                  and all(r[0] == 'L' for r in e[1][1:3])
                                  for e in triple):
            g, h, k = [e[1] for e in triple]
            a, b, aa = [Fraction(e[3], e[4]) for e in (g, h, k)]
            if g[1] == h[2] and g[2] == h[1] and g[1:3] == k[1:3] and a == aa and a*b == -1:
                match = g[1][1], g[2][1], a
        if match is not None:
            left, right, a = match
            unequal += current[left] != current[right]
            current[left], current[right] = current[right], current[left]
            output.append(['weighted_swap', left, right, a, -1/a])
            coefficients.add(a)
            swap_count += 1
            j += 3
            continue
        event = events[j]
        if event[0] == 'scalar':
            gate, frame = event[1:]
            if gate[0] == 'scale' and gate[1][0] == 'L':
                event[2] = current[gate[1][1]]
            else:
                roles = gate[1:3] if gate[0] in ('copy', 'add') else gate[1:2]
                for role in roles:
                    if role[0] == 'L':
                        transport(role[1], frame)
        elif event[0] == 'warp':
            transport(event[1][1], event[3])
            current[event[1][1]] = event[4]
        output.append(event)
        j += 1
    for role, frame in enumerate(c['final']):
        transport(role, frame)
    # Exact two-row linear identity for every coefficient actually encountered.
    for a in coefficients:
        left, right = [Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]
        left = [x + a*y for x, y in zip(left, right)]
        right = [y - x/a for x, y in zip(left, right)]
        left = [x + a*y for x, y in zip(left, right)]
        need(left == [0, a] and right == [-1/a, 0], 'weighted swap local identity')
    return output, {'swaps': swap_count, 'unequal_entry_frames': unequal,
                    'coefficients': sorted(map(str, coefficients))}


def rejected(fn):
    try:
        fn()
    except ValueError:
        return True
    raise ValueError('mutation accepted')


def run(source):
    raw = source.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == SOURCE_SHA, 'source compressed hash')
    payload = gzip.decompress(raw)
    need(hashlib.sha256(payload).hexdigest() == PAYLOAD_SHA, 'source payload hash')
    obj = json.loads(payload)
    c = obj['canonical']
    result = {'status': 'PASS_FIXED_ITINERARY_RANK_MASS_ONLY',
              'source_sha256': SOURCE_SHA, 'source_payload_sha256': PAYLOAD_SHA,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'orientations': {}}
    for direction in ('forward', 'backward'):
        program = obj['programs'][direction]
        before = census(c, program)
        rewritten, stats = reconstruct(c, program)
        after = census(c, rewritten)
        need(before == after, 'source versus carried-frame cost')
        need(before['paid_profile'] == PROFILE, 'retained profile')
        need(stats['swaps'] == 534 and stats['unequal_entry_frames'] == 43, 'published swap census')
        bad = deepcopy(program)
        next(e for e in bad if e[0] == 'climb')[-1] += 1
        rejected(lambda: census(c, bad))
        bad = deepcopy(program)
        next(e for e in bad if e[0] == 'center')[-1] -= 1
        rejected(lambda: census(c, bad))
        bad = deepcopy(c)
        bad['final'][0] = bad['start'][0]
        rejected(lambda: census(bad, program))
        bad = deepcopy(rewritten)
        next(e for e in bad if e[0] == 'weighted_swap')[-1] *= -1
        rejected(lambda: census(c, bad))
        result['orientations'][direction] = {'source': before, 'reconstruction': stats,
                                             'rejecting_controls': 4}
    target_mass = 10750
    paid_mass = 2*sum(r*n for r, n in PROFILE.items()) + 112
    need(paid_mass == 10766 and paid_mass > target_mass, 'strict split mass rejection')
    result['exact_border_repair'] = {
        'target_rank_mass': target_mass,
        'two_full_paid_rank_mass': paid_mass - 112,
        'extra_H1': 112,
        'repaired_paid_rank_mass': paid_mass,
        'rank_mass_deficit': paid_mass - target_mass,
        'strict_split_all_moment_ratio_bound': 'T_t/P_t <= (4/3)^(t-1) * 10750/10766 < 1 for 0 <= t <= 1',
    }
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-word', type=Path, required=True)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    answer = run(args.source_word)
    frozen = Path(__file__).with_name('RESULT.json')
    canonical = json.dumps(answer, indent=2, sort_keys=True) + '\n'
    if args.write:
        frozen.write_text(canonical)
    else:
        need(json.loads(canonical) == json.loads(frozen.read_text()), 'frozen receipt')
    print(answer['status'])
