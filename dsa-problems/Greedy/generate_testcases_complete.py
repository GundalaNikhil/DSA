#!/usr/bin/env python3
"""
Complete Test Case Generator for All Remaining Greedy Problems
GRD-007 through GRD-016
"""

import sys
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
        if result.returncode != 0:
            print(f"  Warning: Solution returned error: {result.stderr[:200]}")
            return None
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        print(f"  Warning: Solution timed out")
        return None
    except Exception as e:
        print(f"  Warning: Error running solution: {e}")
        return None


def generate_grd007_tests():
    """GRD-007: Campus Wi-Fi Expansion - MST with existing edges"""
    solution_file = 'solutions/python/GRD-007-campus-wifi-expansion.py'
    tests = {'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_cases = [
        ('3\n5 1 9\n0', 'from problem'),
        ('4\n10 20 30 40\n1\n0 1', 'with existing'),
        ('3\n5 10 15\n2\n0 1\n1 2', 'all connected'),
    ]
    
    for inp, desc in sample_cases:
        output = run_solution(solution_file, inp)
        if output:
            tests['samples'].append({'input': inp, 'output': output})
    
    # Public (15)
    public_cases = [
        '1\n100\n0',
        '2\n10 20\n0',
        '2\n10 20\n1\n0 1',
        '3\n1 2 3\n0',
        '4\n5 10 15 20\n0',
        '5\n50 40 30 20 10\n0',
        f'10\n{" ".join(map(str, range(1, 11)))}\n0',
        f'10\n{" ".join(map(str, [random.randint(1, 1000) for _ in range(10)]))}\n5\n' + '\n'.join([f'{i} {i+1}' for i in range(5)]),
        f'15\n{" ".join(map(str, range(10, 160, 10)))}\n0',
        f'20\n{" ".join(map(str, [random.randint(1, 10000) for _ in range(20)]))}\n10\n' + '\n'.join([f'{i} {i+10}' for i in range(10)]),
        f'25\n{" ".join(map(str, [random.randint(1, 100000) for _ in range(25)]))}\n0',
        f'30\n{" ".join(map(str, [random.randint(1, 1000000) for _ in range(30)]))}\n15\n' + '\n'.join([f'{i} {i+1}' for i in range(15)]),
        f'50\n{" ".join(map(str, [random.randint(1, 10**9) for _ in range(50)]))}\n0',
        f'100\n{" ".join(map(str, [random.randint(1, 10**9) for _ in range(100)]))}\n50\n' + '\n'.join([f'{random.randint(0, 99)} {random.randint(0, 99)}' for _ in range(50)]),
        f'200\n{" ".join(map(str, [random.randint(1, 10**9) for _ in range(200)]))}\n0',
    ]
    
    for inp in public_cases:
        output = run_solution(solution_file, inp)
        if output:
            tests['public'].append({'input': inp, 'output': output})
    
    # Hidden (22+)
    for _ in range(25):
        n = random.choice([500, 1000, 5000, 10000, 50000, 100000])
        heights = [random.randint(1, 10**9) for _ in range(n)]
        m = random.randint(0, min(n-1, n//2))
        edges = [f'{random.randint(0, n-1)} {random.randint(0, n-1)}' for _ in range(m)]
        
        input_str = f"{n}\n{' '.join(map(str, heights))}\n{m}\n{chr(10).join(edges)}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    return tests


def generate_grd008_tests():
    """GRD-008: Exam Proctor Allocation - Interval scheduling with capacity"""
    solution_file = 'solutions/python/GRD-008-exam-proctor-allocation.py'
    tests = {'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    tests['samples'].append({'input': '3 2\n0 10\n5 7\n6 9', 'output': run_solution(solution_file, '3 2\n0 10\n5 7\n6 9')})
    tests['samples'].append({'input': '4 1\n1 2\n2 3\n3 4\n4 5', 'output': run_solution(solution_file, '4 1\n1 2\n2 3\n3 4\n4 5')})
    tests['samples'].append({'input': '2 3\n1 5\n2 3', 'output': run_solution(solution_file, '2 3\n1 5\n2 3')})
    
    # Public (15)
    public_inputs = [
        '1 1\n1 2',
        '2 1\n1 2\n3 4',
        '2 2\n1 3\n2 4',
        '3 1\n1 4\n2 5\n3 6',
        '4 2\n1 2\n1 2\n1 2\n1 2',
        '5 3\n1 10\n2 3\n4 5\n6 7\n8 9',
        '6 2\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7',
        '10 5\n' + '\n'.join([f'{i} {i+2}' for i in range(1, 11)]),
        '15 3\n' + '\n'.join([f'{random.randint(1, 100)} {random.randint(101, 200)}' for _ in range(15)]),
        '20 10\n' + '\n'.join([f'{i} {i+10}' for i in range(1, 21)]),
        '25 5\n' + '\n'.join([f'{i} {i+1}' for i in range(1, 26)]),
        '50 25\n' + '\n'.join([f'{random.randint(1, 1000)} {random.randint(1001, 2000)}' for _ in range(50)]),
        '100 50\n' + '\n'.join([f'{random.randint(1, 10000)} {random.randint(10001, 20000)}' for _ in range(100)]),
        '200 100\n' + '\n'.join([f'{i*10} {i*10+5}' for i in range(1, 201)]),
        '500 250\n' + '\n'.join([f'{random.randint(1, 100000)} {random.randint(100001, 200000)}' for _ in range(500)]),
    ]
    
    for inp in public_inputs:
        output = run_solution(solution_file, inp)
        if output:
            tests['public'].append({'input': inp, 'output': output})
    
    # Hidden (22+)
    for _ in range(25):
        n = random.choice([1000, 5000, 10000, 50000, 100000])
        r = random.choice([1, 2, 5, 10, 100, 1000, 10000, n, 10**9])
        exams = [f'{random.randint(0, 10**9)} {random.randint(0, 10**9)}' for _ in range(n)]
        # Fix invalid intervals
        exams_fixed = []
        for exam in exams:
            parts = exam.split()
            s, e = int(parts[0]), int(parts[1])
            if s >= e:
                e = s + random.randint(1, 1000)
            exams_fixed.append(f'{s} {e}')
        
        input_str = f"{n} {r}\n{chr(10).join(exams_fixed)}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    return tests


def generate_grd009_tests():
    """GRD-009: Shuttle Refuel with Refund"""
    solution_file = 'solutions/python/GRD-009-shuttle-refuel-with-refund.py'
    tests = {'samples': [], 'public': [], 'hidden': []}
    
    # Use existing generation from part2 - it worked
    tests['samples'].append({'input': '3 10 5\n2 3\n5 2\n8 1', 'output': '7'})
    tests['samples'].append({'input': '2 10 5\n3 5\n7 3', 'output': '13'})
    tests['samples'].append({'input': '4 20 10\n5 2\n10 3\n15 1\n18 4', 'output': '12'})
    
    # Public (15)
    public_inputs = [
        '1 5 5\n3 10',
        '2 10 5\n5 1\n9 2',
        '3 15 5\n5 1\n10 2\n14 3',
        '4 20 10\n5 5\n10 4\n15 3\n19 2',
        '5 25 5\n5 10\n10 8\n15 6\n20 4\n24 2',
        '5 30 10\n6 1\n12 2\n18 3\n24 4\n29 5',
        '10 100 50\n' + '\n'.join([f'{(i+1)*10} {random.randint(1, 10)}' for i in range(10)]),
        '15 150 75\n' + '\n'.join([f'{(i+1)*10} {random.randint(1, 20)}' for i in range(15)]),
        '20 200 100\n' + '\n'.join([f'{(i+1)*10} {i+1}' for i in range(20)]),
        '25 250 125\n' + '\n'.join([f'{(i+1)*10} {random.randint(1, 15)}' for i in range(25)]),
        '50 500 250\n' + '\n'.join([f'{(i+1)*10} {random.randint(1, 50)}' for i in range(50)]),
        '100 1000 500\n' + '\n'.join([f'{(i+1)*10} {random.randint(1, 100)}' for _ in range(100)]),
        '200 2000 1000\n' + '\n'.join([f'{random.randint(1, 1999)} {random.randint(1, 100)}' for _ in range(200)]),
        '500 5000 2500\n' + '\n'.join([f'{random.randint(1, 4999)} {random.randint(1, 500)}' for _ in range(500)]),
        '1000 10000 5000\n' + '\n'.join([f'{random.randint(1, 9999)} {random.randint(1, 1000)}' for _ in range(1000)]),
    ]
    
    for inp in public_inputs:
        output = run_solution(solution_file, inp)
        if output:
            tests['public'].append({'input': inp, 'output': output})
    
    # Hidden (22+)
    for _ in range(25):
        n = random.choice([5000, 10000, 50000, 100000])
        D = random.randint(n * 10, n * 100)
        C = random.randint(D // 4, D // 2)
        stations = [f'{random.randint(1, D-1)} {random.randint(1, 1000)}' for _ in range(n)]
        
        input_str = f"{n} {D} {C}\n{chr(10).join(stations)}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    return tests


def generate_grd010_tests():
    """GRD-010: Library Merge Queues - Merge k sorted with constraint"""
    solution_file = 'solutions/python/GRD-010-library-merge-queues.py'
    tests = {'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    tests['samples'].append({'input': '3\n3 1 1 1\n2 1 2\n1 2', 'output': '1 1 1 2 2'})
    tests['samples'].append({'input': '2\n4 1 2 3 4\n3 2 3 4', 'output': '1 2 2 3 3 4 4'})
    tests['samples'].append({'input': '1\n5 1 1 1 1 1', 'output': '1 1'})
    
    # Public (15)
    public_inputs = [
        '1\n1 5',
        '1\n2 1 1',
        '2\n2 1 2\n2 3 4',
        '2\n3 1 1 1\n1 2',
        '3\n2 1 3\n2 2 4\n2 5 6',
        '3\n3 1 2 3\n3 2 3 4\n3 3 4 5',
        '4\n2 1 5\n2 2 6\n2 3 7\n2 4 8',
        '5\n1 1\n1 2\n1 3\n1 4\n1 5',
        '5\n2 1 1\n2 2 2\n2 3 3\n2 4 4\n2 5 5',
        '10\n' + '\n'.join([f'3 {i} {i} {i}' for i in range(1, 11)]),
        '10\n' + '\n'.join([f'5 {" ".join(map(str, [random.randint(1, 100) for _ in range(5)]))}' for _ in range(10)]),
        '20\n' + '\n'.join([f'2 {i} {i+1}' for i in range(1, 21)]),
        '50\n' + '\n'.join([f'1 {i}' for i in range(1, 51)]),
        '100\n' + '\n'.join([f'1 {random.randint(1, 1000)}' for _ in range(100)]),
        '100\n' + '\n'.join([f'2 {i} {i}' for i in range(1, 101)]),
    ]
    
    for inp in public_inputs:
        output = run_solution(solution_file, inp)
        if output:
            tests['public'].append({'input': inp, 'output': output})
    
    # Hidden (22+)
    for _ in range(25):
        k = random.choice([10, 20, 50, 100])
        queues = []
        for _ in range(k):
            length = random.randint(1, 2000 // k)
            queue = sorted([random.randint(1, 10**9) for _ in range(length)])
            queues.append(f'{length} {" ".join(map(str, queue))}')
        
        input_str = f"{k}\n{chr(10).join(queues)}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    return tests


def generate_grd011_tests():
    """GRD-011: Campus Event Ticket Caps"""
    # Already generated in part 2, just return the working version
    solution_file = 'solutions/python/GRD-011-campus-event-ticket-caps.py'
    tests = {'samples': [], 'public': [], 'hidden': []}
    
    tests['samples'].append({'input': '3 10\n5 3\n8 2\n6 4', 'output': '9'})
    tests['samples'].append({'input': '4 15\n10 5\n8 3\n6 2\n4 1', 'output': '11'})
    tests['samples'].append({'input': '2 5\n10 10\n5 5', 'output': '5'})
    
    # Public + Hidden - reuse working logic
    public_cases = [
        ('1 10\n5 3', 'single'),
        ('2 10\n5 3\n5 3', 'two same'),
        ('5 25\n10 5\n9 4\n8 3\n7 2\n6 1', 'desc'),
        ('10 100\n' + '\n'.join([f'{random.randint(5, 20)} {random.randint(1, 10)}' for _ in range(10)]), 'rand10'),
        ('20 200\n' + '\n'.join([f'{random.randint(1, 50)} {random.randint(1, 20)}' for _ in range(20)]), 'rand20'),
        ('50 500\n' + '\n'.join([f'10 5' for _ in range(50)]), 'same50'),
        ('100 1000\n' + '\n'.join([f'{random.randint(1, 200)} {random.randint(1, 100)}' for _ in range(100)]), 'rand100'),
        ('500 5000\n' + '\n'.join([f'{random.randint(1, 1000)} {random.randint(1, 500)}' for _ in range(500)]), 'rand500'),
        ('1000 10000\n' + '\n'.join([f'{random.randint(1, 5000)} {random.randint(1, 2500)}' for _ in range(1000)]), 'rand1000'),
        ('5000 50000\n' + '\n'.join([f'{random.randint(1, 10000)} {random.randint(1, 5000)}' for _ in range(5000)]), 'rand5k'),
        ('10000 100000\n' + '\n'.join([f'{random.randint(1, 20000)} {random.randint(1, 10000)}' for _ in range(10000)]), 'rand10k'),
        ('50000 500000\n' + '\n'.join([f'{random.randint(1, 100000)} {random.randint(1, 50000)}' for _ in range(50000)]), 'rand50k'),
        ('100000 1000000\n' + '\n'.join([f'{random.randint(1, 500000)} {random.randint(1, 250000)}' for _ in range(100000)]), 'rand100k'),
    ]
    
    # First 15 to public
    for inp, desc in public_cases[:10]:
        output = run_solution(solution_file, inp)
        if output:
            tests['public'].append({'input': inp, 'output': output})
    
    # Rest + more to hidden
    for inp, desc in public_cases[10:]:
        output = run_solution(solution_file, inp)
        if output:
            tests['hidden'].append({'input': inp, 'output': output})
    
    # Add more hidden
    for _ in range(15):
        n = random.choice([10000, 50000, 100000])
        T = random.randint(n * 5, n * 20)
        events = [f'{random.randint(1, 10000)} {random.randint(1, 5000)}' for _ in range(n)]
        input_str = f"{n} {T}\n{chr(10).join(events)}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    return tests


def generate_grd012_tests():
    """GRD-012: Workshop Task Cooldown Priority"""
    solution_file = 'solutions/python/GRD-012-workshop-task-cooldown-priority.py'
    tests = {'samples': [], 'public': [], 'hidden': []}
    
    tests['samples'].append({'input': '3 2\nA 5\nB 3\nA 2', 'output': '7'})
    tests['samples'].append({'input': '4 3\nX 10\nY 5\nX 3\nZ 8', 'output': '14'})
    tests['samples'].append({'input': '2 1\nA 5\nA 3', 'output': '4'})
    
    # Public (15)
    public_inputs = [
        '1 0\nA 10',
        '2 0\nA 5\nB 3',
        '3 0\nA 5\nA 3\nA 2',
        '3 2\nA 10\nB 8\nC 6',
        '4 1\nA 5\nA 5\nA 5\nA 5',
        '5 2\nA 10\nB 9\nC 8\nD 7\nE 6',
        '10 2\n' + '\n'.join([f'T{i%5} {random.randint(1, 20)}' for i in range(10)]),
        '20 4\n' + '\n'.join([f'T{i%10} {random.randint(10, 100)}' for i in range(20)]),
        '50 10\n' + '\n'.join([f'T{i%25} {random.randint(1, 10000)}' for i in range(50)]),
        '100 20\n' + '\n'.join([f'T{i%50} {random.randint(1, 100000)}' for i in range(100)]),
        '500 50\n' + '\n'.join([f'T{i%250} {random.randint(1, 1000000)}' for i in range(500)]),
        '1000 100\n' + '\n'.join([f'T{i%500} {random.randint(1, 10000000)}' for i in range(1000)]),
        '5000 500\n' + '\n'.join([f'T{i%2500} {random.randint(1, 100000000)}' for i in range(5000)]),
        '10000 1000\n' + '\n'.join([f'T{i%5000} {random.randint(1, 1000000000)}' for i in range(10000)]),
        '50000 5000\n' + '\n'.join([f'T{i%25000} {random.randint(1, 1000000000)}' for i in range(50000)]),
    ]
    
    for inp in public_inputs:
        output = run_solution(solution_file, inp)
        if output:
            tests['public'].append({'input': inp, 'output': output})
    
    # Hidden (22+)
    for _ in range(25):
        n = random.choice([10000, 50000, 100000])
        K = random.randint(0, min(n-1, 1000))
        num_types = random.randint(1, min(n, 50000))
        tasks = [f'T{random.randint(0, num_types-1)} {random.randint(1, 10**9)}' for _ in range(n)]
        
        input_str = f"{n} {K}\n{chr(10).join(tasks)}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    return tests


def save_testcases(problem_id, tests):
    """Save test cases to YAML file"""
    testcase_dir = Path('testcases')
    output_file = testcase_dir / f'{problem_id}.yaml'
    
    data = {
        'problem_id': problem_id,
        'samples': tests['samples'],
        'public': tests['public'],
        'hidden': tests['hidden']
    }
    
    with open(output_file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    total = len(tests['samples']) + len(tests['public']) + len(tests['hidden'])
    print(f"✓ {problem_id}: {len(tests['samples'])} samples + {len(tests['public'])} public + {len(tests['hidden'])} hidden = {total} total")


def main():
    """Generate test cases for GRD-007 through GRD-012"""
    print("=" * 80)
    print("GREEDY MODULE COMPLETE TEST CASE GENERATOR")
    print("Generating GRD-007 through GRD-012")
    print("=" * 80)
    print()
    
    generators = [
        ('GRD-007-campus-wifi-expansion', generate_grd007_tests),
        ('GRD-008-exam-proctor-allocation', generate_grd008_tests),
        ('GRD-009-shuttle-refuel-with-refund', generate_grd009_tests),
        ('GRD-010-library-merge-queues', generate_grd010_tests),
        ('GRD-011-campus-event-ticket-caps', generate_grd011_tests),
        ('GRD-012-workshop-task-cooldown-priority', generate_grd012_tests),
    ]
    
    for problem_id, generator_func in generators:
        print(f"\n[{problem_id}]")
        try:
            tests = generator_func()
            save_testcases(problem_id, tests)
        except Exception as e:
            print(f"✗ Error: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 80)
    print("Generation complete for GRD-007 through GRD-012!")
    print("=" * 80)


if __name__ == '__main__':
    main()
