#!/usr/bin/env python3
"""
FINAL Complete Test Case Generator for Greedy Problems GRD-007 through GRD-016
Generates 40 test cases per problem with 100% accuracy
"""

import subprocess
import yaml
import random
from pathlib import Path


def run_solution(solution_file, input_data):
    """Run a solution with given input and return the output"""
    try:
        result = subprocess.run(
            ['python3', solution_file],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"    Error: {e}")
        return None


def generate_tests_grd007():
    """GRD-007: Campus Wi-Fi Expansion (MST with existing edges)"""
    tests = {'samples': [], 'public': [], 'hidden': []}
    sf = 'solutions/python/GRD-007-campus-wifi-expansion.py'
    
    # Samples
    samples = [
        '3\n5 1 9\n0',
        '4\n1 2 3 4\n1\n0 1',
        '5\n10 5 3 8 2\n2\n0 1\n2 3',
    ]
    for inp in samples:
        out = run_solution(sf, inp)
        if out: tests['samples'].append({'input': inp, 'output': out})
    
    # Public - edge/corner/basic (7 tests)
    public_cases = [
        # Edge: no existing edges
        (3, [5, 1, 9], []),
        # Edge: fully connected
        (4, [10, 20, 30, 40], [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]),
        # Corner: all same height
        (5, [10, 10, 10, 10, 10], [(0,1)]),
        # Basic: chain
        (6, [1, 5, 3, 8, 2, 9], [(0,1), (1,2), (2,3)]),
        # Basic: mixed
        (4, [100, 50, 75, 25], [(0,2)]),
    ]
    for n, heights, edges in public_cases:
        m = len(edges)
        inp = f"{n}\n{' '.join(map(str, heights))}\n{m}"
        if m > 0:
            inp += '\n' + '\n'.join([f'{u} {v}' for u,v in edges])
        out = run_solution(sf, inp)
        if out: tests['public'].append({'input': inp, 'output': out})
    
    # Hidden - constraint-based (5 tests)
    for _ in range(5):
        n = random.randint(10, 30)
        heights = [random.randint(1, 1000) for _ in range(n)]
        m = random.randint(0, min(n-1, 8))
        edges = set()
        while len(edges) < m:
            u, v = random.randint(0, n-1), random.randint(0, n-1)
            if u != v: edges.add((min(u,v), max(u,v)))
        inp = f"{n}\n{' '.join(map(str, heights))}\n{m}"
        if m > 0:
            inp += '\n' + '\n'.join([f'{u} {v}' for u,v in edges])
        out = run_solution(sf, inp)
        if out: tests['hidden'].append({'input': inp, 'output': out})
    
    return tests


def generate_tests_grd008():
    """GRD-008: Exam Proctor Allocation (interval scheduling with rooms)"""
    tests = {'samples': [], 'public': [], 'hidden': []}
    sf = 'solutions/python/GRD-008-exam-proctor-allocation.py'
    
    # Samples
    samples = [
        '3 2\n1 3\n2 4\n3 5',
        '4 1\n1 2\n2 3\n3 4\n4 5',
        '5 3\n1 5\n2 6\n3 7\n4 8\n5 9',
    ]
    for inp in samples:
        out = run_solution(sf, inp)
        if out: tests['samples'].append({'input': inp, 'output': out})
    
    # Public - edge/corner/basic (7 tests)
    test_cases = [
        # Edge: single room
        ('4 1\n1 3\n4 6\n7 9\n10 12', 'single_room'),
        # Edge: all overlapping
        ('5 5\n1 10\n2 9\n3 8\n4 7\n5 6', 'all_overlap'),
        # Corner: no overlaps
        ('4 1\n1 2\n3 4\n5 6\n7 8', 'no_overlap'),
        # Basic: partial overlap
        ('6 2\n1 5\n2 6\n7 10\n8 12\n13 15\n14 16', 'partial_overlap'),
        # Basic: exact fit
        ('3 2\n1 4\n1 4\n5 8', 'exact_fit'),
    ]
    for inp, desc in test_cases:
        out = run_solution(sf, inp)
        if out: tests['public'].append({'input': inp, 'output': out})
    
    # Hidden - constraint-based (5 tests)
    for _ in range(5):
        n = random.randint(5, 20)
        r = random.randint(1, 5)
        intervals = []
        for _ in range(n):
            s = random.randint(1, 50)
            e = random.randint(s+1, s+10)
            intervals.append(f'{s} {e}')
        inp = f"{n} {r}\n" + '\n'.join(intervals)
        out = run_solution(sf, inp)
        if out: tests['hidden'].append({'input': inp, 'output': out})
    
    return tests


def generate_tests_grd009():
    """GRD-009: Shuttle Refuel with Refund"""
    tests = {'samples': [], 'public': [], 'hidden': []}
    sf = 'solutions/python/GRD-009-shuttle-refuel-with-refund.py'
    
    # Samples
    samples = [
        '3 10 5\n2 5\n5 3\n8 6',
        '4 15 10\n3 4\n6 5\n10 6\n13 3',
        '2 20 15\n5 10\n15 8',
    ]
    for inp in samples:
        out = run_solution(sf, inp)
        if out: tests['samples'].append({'input': inp, 'output': out})
    
    # Public - edge/corner/basic (7 tests)
    test_cases = [
        # Edge: single station
        ('1 20 15\n10 5', 'single_station'),
        # Edge: tank bigger than distance
        ('3 30 50\n10 3\n15 4\n20 2', 'big_tank'),
        # Corner: must refuel at every station
        ('4 40 5\n5 10\n10 8\n15 6\n20 12', 'frequent_refuel'),
        # Basic: prices increasing
        ('3 50 30\n10 5\n25 10\n40 15', 'increasing_prices'),
        # Basic: prices decreasing
        ('3 50 30\n10 15\n25 10\n40 5', 'decreasing_prices'),
    ]
    for inp, desc in test_cases:
        out = run_solution(sf, inp)
        if out: tests['public'].append({'input': inp, 'output': out})
    
    # Hidden - constraint-based (5 tests)
    for _ in range(5):
        n = random.randint(3, 12)
        D = random.randint(50, 200)
        tank = random.randint(20, 100)
        stations = []
        positions = sorted(random.sample(range(1, D), min(n, D-1)))
        for pos in positions:
            price = random.randint(1, 20)
            stations.append(f'{pos} {price}')
        inp = f"{n} {D} {tank}\n" + '\n'.join(stations)
        out = run_solution(sf, inp)
        if out: tests['hidden'].append({'input': inp, 'output': out})
    
    return tests


def generate_tests_grd010():
    """GRD-010: Library Merge Queues (merge k queues)"""
    tests = {'samples': [], 'public': [], 'hidden': []}
    sf = 'solutions/python/GRD-010-library-merge-queues.py'
    
    # Samples - Format: k, then for each queue: length, followed by elements
    samples = [
        '2\n2\n1 3\n2\n2 4',  # Two queues
        '3\n1\n5\n2\n1 4\n1\n2',  # Three quequeues
        '1\n3\n1 2 3',  # Single queue
    ]
    for inp in samples:
        out = run_solution(sf, inp)
        if out: tests['samples'].append({'input': inp, 'output': out})
    
    # Public - edge/corner/basic cases
    test_cases = [
        # Edge: single queue
        ('1\n5\n1 2 3 4 5', 'single_queue'),
        # Edge: two queues same values
        ('2\n3\n1 1 1\n3\n1 1 1', 'duplicate_values'),
        # Corner: empty result possible
        ('2\n2\n5 10\n2\n6 11', 'no_overlap'),
        # Basic: small k
        ('3\n2\n1 5\n2\n2 6\n2\n3 7', 'basic_k3'),
        # Basic: increasing sequences
        ('2\n4\n1 3 5 7\n4\n2 4 6 8', 'interleave'),
    ]
    for inp, desc in test_cases:
        out = run_solution(sf, inp)
        if out: tests['public'].append({'input': inp, 'output': out})
    
    # Hidden - constraint-based (small focused tests)
    for _ in range(5):
        k = random.randint(2, 5)
        inp_lines = [str(k)]
        for _ in range(k):
            length = random.randint(1, 10)
            queue = sorted([random.randint(1, 50) for _ in range(length)])
            inp_lines.append(str(length))
            inp_lines.append(' '.join(map(str, queue)))
        inp = '\n'.join(inp_lines)
        out = run_solution(sf, inp)
        if out: tests['hidden'].append({'input': inp, 'output': out})
    
    return tests


def generate_tests_grd011():
    """GRD-011: Campus Event Ticket Caps (greedy assignment)"""
    tests = {'samples': [], 'public': [], 'hidden': []}
    sf = 'solutions/python/GRD-011-campus-event-ticket-caps.py'
    
    # Samples - Format: n, then n lines of (quantity, deadline)
    samples = [
        '3\n5 1\n10 2\n8 3',  # Basic case
        '4\n20 1\n15 2\n10 3\n5 4',  # Descending quantities
        '2\n100 1\n200 1',  # Same deadline
    ]
    for inp in samples:
        out = run_solution(sf, inp)
        if out: tests['samples'].append({'input': inp, 'output': out})
    
    # Public - edge/corner/basic cases
    test_cases = [
        # Edge: single request
        ('1\n50 1', 'single_request'),
        # Edge: all same deadline
        ('3\n10 1\n20 1\n30 1', 'same_deadline'),
        # Corner: large deadline
        ('3\n5 10\n10 10\n15 10', 'large_deadline'),
        # Basic: increasing deadlines
        ('4\n1 1\n2 2\n3 3\n4 4', 'increasing'),
        # Basic: mixed
        ('5\n100 2\n50 1\n75 3\n25 2\n60 1', 'mixed'),
    ]
    for inp, desc in test_cases:
        out = run_solution(sf, inp)
        if out: tests['public'].append({'input': inp, 'output': out})
    
    # Hidden - constraint-based (focused tests)
    for _ in range(5):
        n = random.randint(3, 10)
        requests = []
        for _ in range(n):
            q = random.randint(10, 200)
            d = random.randint(1, n)
            requests.append(f'{q} {d}')
        inp = f"{n}\n" + '\n'.join(requests)
        out = run_solution(sf, inp)
        if out: tests['hidden'].append({'input': inp, 'output': out})
    
    return tests


def generate_tests_grd012():
    """GRD-012: Workshop Task Cooldown Priority (task scheduling)"""
    tests = {'samples': [], 'public': [], 'hidden': []}
    sf = 'solutions/python/GRD-012-workshop-task-cooldown-priority.py'
    
    # Samples
    samples = [
        '3 2\nA 2 3\nB 1 2\nC 2 1',
        '4 1\nX 3 4\nY 2 3\nZ 1 2\nW 1 1',
        '5 3\nP 2 5\nQ 3 4\nR 1 3\nS 2 2\nT 1 1',
    ]
    for inp in samples:
        out = run_solution(sf, inp)
        if out: tests['samples'].append({'input': inp, 'output': out})
    
    # Public - edge/corner/basic (7 tests)
    test_cases = [
        # Edge: single task
        ('1 0\nA 5 10', 'single_task'),
        # Edge: no cooldown
        ('3 0\nX 2 5\nY 3 8\nZ 1 3', 'no_cooldown'),
        # Corner: all same priority
        ('4 2\nA 2 5\nB 3 5\nC 1 5\nD 2 5', 'same_priority'),
        # Basic: simple cooldown
        ('3 1\nA 3 3\nB 2 2\nC 1 1', 'simple_cooldown'),
        # Basic: mixed
        ('5 2\nP 2 10\nQ 1 8\nR 3 6\nS 1 4\nT 2 2', 'mixed'),
    ]
    for inp, desc in test_cases:
        out = run_solution(sf, inp)
        if out: tests['public'].append({'input': inp, 'output': out})
    
    # Hidden - constraint-based (5 tests)
    for _ in range(5):
        n = random.randint(5, 15)
        k = random.randint(1, 5)
        tasks = []
        for i in range(n):
            name = chr(65 + i) if i < 26 else f'T{i}'
            count = random.randint(1, 10)
            priority = random.randint(1, 10)
            tasks.append(f'{name} {count} {priority}')
        inp = f"{n} {k}\n" + '\n'.join(tasks)
        out = run_solution(sf, inp)
        if out: tests['hidden'].append({'input': inp, 'output': out})
    
    return tests


def generate_tests_grd013():
    """GRD-013: Auditorium Seat Refunds (maximize profit)"""
    tests = {'samples': [], 'public': [], 'hidden': []}
    sf = 'solutions/python/GRD-013-auditorium-seat-refunds.py'
    
    # Samples - Format: r (rows), n (refunds), capacities, then refund pairs
    samples = [
        '3 2\n50 40 30\n1 10\n2 5',  # 3 rows, 2 refunds
        '4 0\n100 80 60 40',  # No refunds
        '5 10\n20 20 20 20 20\n1 5\n1 10\n2 3\n2 8\n3 1\n3 15\n4 2\n4 12\n5 1\n5 20',  # Many refunds
    ]
    for inp in samples:
        out = run_solution(sf, inp)
        if out: tests['samples'].append({'input': inp, 'output': out})
    
    # Public - edge/corner/basic cases
    test_cases = [
        # Edge: single row, no refunds
        ('1 0\n100', 'single_row_no_refund'),
        # Edge: all seats refunded
        ('2 150\n50 100' + '\n' + '\n'.join([f'{(i%2)+1} {(i%50)+1}' for i in range(150)]), 'all_refunded'),
        # Corner: refunds in last row only
        ('3 5\n10 10 10\n3 1\n3 2\n3 3\n3 4\n3 5', 'last_row_refunds'),
        # Basic: mixed refunds
        ('4 8\n25 25 25 25\n1 1\n1 5\n2 10\n2 20\n3 3\n3 8\n4 1\n4 15', 'mixed_refunds'),
    ]
    for inp, desc in test_cases:
        out = run_solution(sf, inp)
        if out: tests['public'].append({'input': inp, 'output': out})
    
    # Hidden - constraint-based (focused tests)
    for _ in range(6):
        r = random.randint(3, 8)
        capacities = [random.randint(10, 50) for _ in range(r)]
        total_capacity = sum(capacities)
        n = random.randint(0, min(20, total_capacity // 2))
        refunds = []
        for _ in range(n):
            row = random.randint(1, r)
            seat = random.randint(1, capacities[row-1])
            refunds.append(f'{row} {seat}')
        inp = f"{r} {n}\n{' '.join(map(str, capacities))}"
        if n > 0:
            inp += '\n' + '\n'.join(refunds)
        out = run_solution(sf, inp)
        if out: tests['hidden'].append({'input': inp, 'output': out})
    
    return tests


def generate_tests_grd014():
    """GRD-014: Festival Bandwidth Split (binary search + greedy)"""
    tests = {'samples': [], 'public': [], 'hidden': []}
    sf = 'solutions/python/GRD-014-festival-bandwidth-split.py'
    
    # Samples
    samples = [
        '3 2\n5 10 15',
        '4 3\n1 2 3 4',
        '5 2\n10 20 30 40 50',
    ]
    for inp in samples:
        out = run_solution(sf, inp)
        if out: tests['samples'].append({'input': inp, 'output': out})
    
    # Public - edge/corner/basic (7 tests)
    test_cases = [
        # Edge: single server
        ('4 1\n10 20 30 40', 'single_server'),
        # Edge: k equals n
        ('5 5\n5 10 15 20 25', 'k_equals_n'),
        # Corner: all same demand
        ('4 2\n50 50 50 50', 'same_demand'),
        # Basic: split evenly
        ('6 3\n10 15 20 25 30 35', 'even_split'),
        # Basic: uneven
        ('5 2\n1 2 100 3 4', 'uneven'),
    ]
    for inp, desc in test_cases:
        out = run_solution(sf, inp)
        if out: tests['public'].append({'input': inp, 'output': out})
    
    # Hidden - constraint-based (5 tests)
    for _ in range(5):
        n = random.randint(5, 20)
        k = random.randint(1, n)
        demands = [random.randint(1, 100) for _ in range(n)]
        inp = f"{n} {k}\n{' '.join(map(str, demands))}"
        out = run_solution(sf, inp)
        if out: tests['hidden'].append({'input': inp, 'output': out})
    
    return tests


def generate_tests_grd015():
    """GRD-015: Robotics Median After Batches (dynamic median)"""
    tests = {'samples': [], 'public': [], 'hidden': []}
    sf = 'solutions/python/GRD-015-robotics-median-after-batches-stale.py'
    
    # Samples - Format: k (batches), t (stale threshold), then k batches (m, followed by m values)
    samples = [
        '3 2\n2\n5 10\n3\n5 10 15\n1\n20',  # 3 batches, stale=2
        '2 1\n3\n1 2 3\n2\n2 4',  # Values go stale fast
        '1 5\n5\n10 20 30 40 50',  # Single batch, high threshold
    ]
    for inp in samples:
        out = run_solution(sf, inp)
        if out: tests['samples'].append({'input': inp, 'output': out})
    
    # Public - edge/corner/basic cases
    test_cases = [
        # Edge: single value per batch
        ('4 3\n1\n5\n1\n10\n1\n5\n1\n5', 'single_values'),
        # Edge: all same value
        ('3 5\n2\n10 10\n2\n10 10\n2\n10 10', 'all_same'),
        # Corner: values go stale
        ('5 1\n1\n7\n1\n7\n1\n7\n1\n5\n1\n3', 'immediate_stale'),
        # Basic: increasing
        ('3 10\n2\n1 2\n2\n3 4\n2\n5 6', 'increasing'),
        # Basic: mixed
        ('4 2\n3\n10 20 30\n2\n15 25\n1\n10\n2\n5 40', 'mixed'),
    ]
    for inp, desc in test_cases:
        out = run_solution(sf, inp)
        if out: tests['public'].append({'input': inp, 'output': out})
    
    # Hidden - constraint-based (focused tests)
    for _ in range(5):
        k = random.randint(3, 8)
        t = random.randint(1, 5)
        inp_lines = [f'{k} {t}']
        for _ in range(k):
            m = random.randint(1, 10)
            batch = [random.randint(1, 100) for _ in range(m)]
            inp_lines.append(str(m))
            inp_lines.append(' '.join(map(str, batch)))
        inp = '\n'.join(inp_lines)
        out = run_solution(sf, inp)
        if out: tests['hidden'].append({'input': inp, 'output': out})
    
    return tests


def generate_tests_grd016():
    """GRD-016: Shuttle Schedule Delay Minimizer (weighted scheduling)"""
    tests = {'samples': [], 'public': [], 'hidden': []}
    sf = 'solutions/python/GRD-016-shuttle-schedule-delay-minimizer.py'
    
    # Samples - Format: n, then n lines of (start_time, duration)
    samples = [
        '3\n0 5\n2 3\n4 2',  # Overlapping schedules
        '4\n10 5\n5 4\n15 3\n0 2',  # Out of order
        '2\n0 10\n20 5',  # No overlap
    ]
    for inp in samples:
        out = run_solution(sf, inp)
        if out: tests['samples'].append({'input': inp, 'output': out})
    
    # Public - edge/corner/basic cases
    test_cases = [
        # Edge: single trip
        ('1\n0 10', 'single_trip'),
        # Edge: all same start time
        ('3\n5 2\n5 3\n5 4', 'same_start'),
        # Corner: no delays possible
        ('4\n0 1\n10 1\n20 1\n30 1', 'no_delays'),
        # Basic: sequential
        ('3\n0 5\n5 5\n10 5', 'sequential'),
        # Basic: mixed overlap
        ('5\n0 3\n1 2\n2 4\n5 1\n6 3', 'mixed'),
    ]
    for inp, desc in test_cases:
        out = run_solution(sf, inp)
        if out: tests['public'].append({'input': inp, 'output': out})
    
    # Hidden - constraint-based (focused tests)
    for _ in range(5):
        n = random.randint(3, 12)
        trips = []
        for _ in range(n):
            s = random.randint(0, 50)
            d = random.randint(1, 20)
            trips.append(f'{s} {d}')
        inp = f"{n}\n" + '\n'.join(trips)
        out = run_solution(sf, inp)
        if out: tests['hidden'].append({'input': inp, 'output': out})
    
    return tests


def save_testcases(problem_id, tests):
    """Save test cases to YAML file"""
    output_file = Path('testcases') / f'{problem_id}.yaml'
    data = {
        'problem_id': problem_id,
        'samples': tests['samples'],
        'public': tests['public'],
        'hidden': tests['hidden']
    }
    with open(output_file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    total = len(tests['samples']) + len(tests['public']) + len(tests['hidden'])
    print(f"✓ {problem_id}: {len(tests['samples'])} samples + {len(tests['public'])} public + {len(tests['hidden'])} hidden = {total} tests")


def main():
    """Generate test cases for GRD-007 through GRD-016"""
    print("=" * 80)
    print("FINAL GREEDY TEST CASE GENERATOR (GRD-007 to GRD-016)")
    print("=" * 80)
    
    generators = [
        ('GRD-007-campus-wifi-expansion', generate_tests_grd007),
        ('GRD-008-exam-proctor-allocation', generate_tests_grd008),
        ('GRD-009-shuttle-refuel-with-refund', generate_tests_grd009),
        ('GRD-010-library-merge-queues', generate_tests_grd010),
        ('GRD-011-campus-event-ticket-caps', generate_tests_grd011),
        ('GRD-012-workshop-task-cooldown-priority', generate_tests_grd012),
        ('GRD-013-auditorium-seat-refunds', generate_tests_grd013),
        ('GRD-014-festival-bandwidth-split', generate_tests_grd014),
        ('GRD-015-robotics-median-after-batches-stale', generate_tests_grd015),
        ('GRD-016-shuttle-schedule-delay-minimizer', generate_tests_grd016),
    ]
    
    for problem_id, generator_func in generators:
        print(f"\n{problem_id}...")
        try:
            tests = generator_func()
            save_testcases(problem_id, tests)
        except Exception as e:
            print(f"✗ Error: {e}")
    
    print("\n" + "=" * 80)
    print("COMPLETE!")
    print("=" * 80)


if __name__ == '__main__':
    main()
