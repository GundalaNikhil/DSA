#!/usr/bin/env python3
"""
Comprehensive Test Case Generator for Greedy Problems (Part 2: GRD-007 to GRD-016)
Generates 40 test cases per problem
"""

import sys
import os
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
            timeout=5
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error running solution: {e}")
        return None


def generate_grd007_tests():
    """GRD-007: Campus Wi-Fi Expansion - MST with existing edges"""
    solution_file = 'solutions/python/GRD-007-campus-wifi-expansion.py'
    
    tests = {'samples': [], 'public': [], 'hidden': []}
    
    # Sample 1: From problem statement
    tests['samples'].append({
        'input': '3\n5 1 9\n0',
        'output': '8'
    })
    
    # Sample 2: With existing cables
    tests['samples'].append({
        'input': '4\n10 20 30 40\n1\n0 1',
        'output': '20'
    })
    
    # Sample 3: All already connected
    tests['samples'].append({
        'input': '3\n5 10 15\n2\n0 1\n1 2',
        'output': '0'
    })
    
    # Public tests (15)
    public_cases = [
        # Edge cases
        ('1\n100\n0', 'single building'),
        ('2\n10 20\n0', 'two buildings no cables'),
        ('2\n10 20\n1\n0 1', 'two buildings connected'),
        
        # Small cases
        ('3\n1 2 3\n0', 'ascending heights'),
        ('3\n10 5 15\n0', 'unsorted heights'),
        ('4\n5 10 15 20\n0', 'evenly spaced'),
        ('4\n100 200 150 250\n1\n0 2', 'partial connection'),
        ('5\n1 10 100 1000 10000\n0', 'exponential heights'),
        
        # Medium cases
        ('5\n50 40 30 20 10\n0', 'descending'),
        ('6\n1 2 4 8 16 32\n2\n0 1\n2 3', 'powers of 2 partial'),
        ('8\n10 20 30 40 50 60 70 80\n3\n0 1\n2 3\n4 5', 'multiple components'),
        ('10\n' + ' '.join(map(str, range(1, 11))) + '\n0', 'sequence 1-10'),
        
        # More complex
        ('10\n' + ' '.join(map(str, [random.randint(1, 1000) for _ in range(10)])) + '\n5\n' +
         '\n'.join([f'{i} {i+1}' for i in range(5)]), 'random with chain'),
        ('15\n' + ' '.join(map(str, range(10, 160, 10))) + '\n0', 'evenly spaced 15'),
        ('20\n' + ' '.join(map(str, [random.randint(1, 10000) for _ in range(20)])) + '\n10\n' +
         '\n'.join([f'{i} {i+10}' for i in range(10)]), 'random 20 with pairs'),
    ]
    
    for inp, desc in public_cases:
        output = run_solution(solution_file, inp)
        if output:
            tests['public'].append({'input': inp, 'output': output})
    
    # Hidden tests (22)
    for _ in range(22):
        n = random.choice([50, 100, 500, 1000, 5000, 10000, 50000, 100000])
        heights = [random.randint(1, 10**9) for _ in range(n)]
        m = random.randint(0, min(n-1, n//2))
        
        # Generate random existing cables
        edges = []
        for _ in range(m):
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v:
                edges.append(f'{u} {v}')
        
        input_str = f"{n}\n{' '.join(map(str, heights))}\n{m}\n{chr(10).join(edges)}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    return tests


def generate_grd008_tests():
    """GRD-008: Exam Proctor Allocation - Interval scheduling"""
    solution_file = 'solutions/python/GRD-008-exam-proctor-allocation.py'
    
    tests = {'samples': [], 'public': [], 'hidden': []}
    
    # Sample tests
    tests['samples'].append({'input': '3\n1 3\n2 4\n3 5', 'output': '2'})
    tests['samples'].append({'input': '4\n1 2\n2 3\n3 4\n4 5', 'output': '1'})
    tests['samples'].append({'input': '2\n1 5\n2 3', 'output': '2'})
    
    # Public tests (15)
    public_cases = [
        ('1\n1 2', 'single exam'),
        ('2\n1 2\n3 4', 'no overlap'),
        ('2\n1 3\n2 4', 'partial overlap'),
        ('3\n1 4\n2 5\n3 6', 'all overlap'),
        ('4\n1 2\n1 2\n1 2\n1 2', 'all same'),
        ('5\n1 10\n2 3\n4 5\n6 7\n8 9', 'one covers all'),
        ('6\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7', 'consecutive'),
        ('8\n1 5\n2 6\n3 7\n4 8\n5 9\n6 10\n7 11\n8 12', 'cascade'),
        ('10\n' + '\n'.join([f'{i} {i+2}' for i in range(1, 11)]), 'overlapping pairs'),
        ('10\n' + '\n'.join([f'{i*10} {i*10+5}' for i in range(1, 11)]), 'no overlaps'),
        ('15\n' + '\n'.join([f'{random.randint(1, 100)} {random.randint(101, 200)}' for _ in range(15)]), 'random 15'),
        ('20\n' + '\n'.join([f'{i} {i+10}' for i in range(1, 21)]), 'long overlaps'),
        ('20\n' + '\n'.join([f'{1} {100}' for _ in range(20)]), 'all overlap completely'),
        ('25\n' + '\n'.join([f'{i} {i+1}' for i in range(1, 26)]), 'consecutive 25'),
        ('30\n' + '\n'.join([f'{random.randint(1, 1000)} {random.randint(1001, 2000)}' for _ in range(30)]), 'random 30'),
    ]
    
    for inp, desc in public_cases:
        output = run_solution(solution_file, inp)
        if output:
            tests['public'].append({'input': inp, 'output': output})
    
    # Hidden tests (22)
    for _ in range(22):
        n = random.choice([100, 500, 1000, 5000, 10000, 50000, 100000])
        exams = []
        for _ in range(n):
            start = random.randint(1, 10**9)
            end = random.randint(start, start + 10**6)
            exams.append(f'{start} {end}')
        
        input_str = f"{n}\n{chr(10).join(exams)}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    return tests


def generate_grd009_tests():
    """GRD-009: Shuttle Refuel with Refund - Greedy with refunds"""
    solution_file = 'solutions/python/GRD-009-shuttle-refuel-with-refund.py'
    
    tests = {'samples': [], 'public': [], 'hidden': []}
    
    # Sample tests
    tests['samples'].append({'input': '3 10 5\n2 3\n5 2\n8 1', 'output': '7'})
    tests['samples'].append({'input': '2 10 5\n3 5\n7 3', 'output': '13'})
    tests['samples'].append({'input': '4 20 10\n5 2\n10 3\n15 1\n18 4', 'output': '12'})
    
    # Public tests (15)
    public_cases = [
        ('1 5 5\n3 10', 'single station'),
        ('2 10 5\n5 1\n9 2', 'two stations'),
        ('3 15 5\n5 1\n10 2\n14 3', 'three stations'),
        ('4 20 10\n5 5\n10 4\n15 3\n19 2', 'descending costs'),
        ('5 25 5\n5 10\n10 8\n15 6\n20 4\n24 2', 'descending costs 5'),
        ('5 30 10\n6 1\n12 2\n18 3\n24 4\n29 5', 'ascending costs'),
        ('6 50 20\n10 5\n20 4\n30 6\n40 3\n45 7\n49 2', 'mixed costs'),
        ('10\n' + '100 50\n' + '\n'.join([f'{(i+1)*10} {random.randint(1, 10)}' for i in range(10)]), 'random 10'),
        ('15\n' + '150 75\n' + '\n'.join([f'{(i+1)*10} {random.randint(1, 20)}' for i in range(15)]), 'random 15'),
        ('20\n' + '200 100\n' + '\n'.join([f'{(i+1)*10} {i+1}' for i in range(20)]), 'ascending'),
        ('20\n' + '200 100\n' + '\n'.join([f'{(i+1)*10} {20-i}' for i in range(20)]), 'descending'),
        ('25\n' + '250 125\n' + '\n'.join([f'{(i+1)*10} {random.randint(1, 15)}' for i in range(25)]), 'random 25'),
        ('30\n' + '300 150\n' + '\n'.join([f'{(i+1)*10} {(i % 10) + 1}' for i in range(30)]), 'cyclic'),
        ('50\n' + '500 250\n' + '\n'.join([f'{(i+1)*10} {random.randint(1, 50)}' for i in range(50)]), 'random 50'),
        ('100\n' + '1000 500\n' + '\n'.join([f'{(i+1)*10} {random.randint(1, 100)}' for i in range(100)]), 'random 100'),
    ]
    
    for inp, desc in public_cases:
        output = run_solution(solution_file, inp)
        if output:
            tests['public'].append({'input': inp, 'output': output})
    
    # Hidden tests (22)
    for _ in range(22):
        n = random.choice([500, 1000, 5000, 10000, 50000, 100000])
        D = random.randint(n * 10, n * 100)
        C = random.randint(D // 4, D // 2)
        
        stations = []
        for i in range(n):
            pos = random.randint(1, D - 1)
            cost = random.randint(1, 1000)
            stations.append(f'{pos} {cost}')
        
        input_str = f"{n} {D} {C}\n{chr(10).join(stations)}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    return tests


def generate_grd010_tests():
    """GRD-010: Library Merge Queues - Huffman coding style"""
    solution_file = 'solutions/python/GRD-010-library-merge-queues.py'
    
    tests = {'samples': [], 'public': [], 'hidden': []}
    
    # Sample tests
    tests['samples'].append({'input': '3\n2 3 5', 'output': '15'})
    tests['samples'].append({'input': '4\n1 2 3 4', 'output': '19'})
    tests['samples'].append({'input': '2\n10 20', 'output': '30'})
    
    # Public tests (15)
    public_cases = [
        ('1\n100', 'single queue'),
        ('2\n1 1', 'two ones'),
        ('2\n10 10', 'two tens'),
        ('3\n1 1 1', 'three ones'),
        ('3\n5 10 15', 'ascending'),
        ('4\n10 10 10 10', 'all same'),
        ('5\n1 2 3 4 5', 'sequence 1-5'),
        ('5\n10 20 30 40 50', 'multiples of 10'),
        ('6\n1 1 1 1 1 1', 'six ones'),
        ('8\n' + ' '.join(map(str, range(1, 9))), 'sequence 1-8'),
        ('10\n' + ' '.join(map(str, [random.randint(1, 100) for _ in range(10)])), 'random 10'),
        ('15\n' + ' '.join(map(str, [i*10 for i in range(1, 16)])), 'multiples 15'),
        ('20\n' + ' '.join(map(str, [random.randint(1, 1000) for _ in range(20)])), 'random 20'),
        ('50\n' + ' '.join(map(str, [1] * 50)), 'fifty ones'),
        ('100\n' + ' '.join(map(str, [random.randint(1, 10000) for _ in range(100)])), 'random 100'),
    ]
    
    for inp, desc in public_cases:
        output = run_solution(solution_file, inp)
        if output:
            tests['public'].append({'input': inp, 'output': output})
    
    # Hidden tests (22)
    for _ in range(22):
        n = random.choice([500, 1000, 5000, 10000, 50000, 100000])
        queues = [random.randint(1, 10**9) for _ in range(n)]
        
        input_str = f"{n}\n{' '.join(map(str, queues))}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    return tests


def generate_grd011_tests():
    """GRD-011: Campus Event Ticket Caps - Greedy selection"""
    solution_file = 'solutions/python/GRD-011-campus-event-ticket-caps.py'
    
    tests = {'samples': [], 'public': [], 'hidden': []}
    
    # Sample tests  
    tests['samples'].append({'input': '3 10\n5 3\n8 2\n6 4', 'output': '9'})
    tests['samples'].append({'input': '4 15\n10 5\n8 3\n6 2\n4 1', 'output': '11'})
    tests['samples'].append({'input': '2 5\n10 10\n5 5', 'output': '5'})
    
    # Public tests (15)
    public_cases = [
        ('1 10\n5 3', 'single event'),
        ('1 5\n10 10', 'single event exceeds cap'),
        ('2 10\n5 3\n5 3', 'two same events'),
        ('3 15\n10 5\n10 5\n10 5', 'three same events'),
        ('4 20\n5 5\n5 5\n5 5\n5 5', 'four same events'),
        ('5 25\n10 5\n9 4\n8 3\n7 2\n6 1', 'descending'),
        ('5 30\n5 1\n10 2\n15 3\n20 4\n25 5', 'ascending'),
        ('6 50\n20 10\n15 8\n10 6\n8 4\n6 2\n4 1', 'varied'),
        ('10 100\n' + '\n'.join([f'{random.randint(5, 20)} {random.randint(1, 10)}' for _ in range(10)]), 'random 10'),
        ('15 150\n' + '\n'.join([f'{10*(i+1)} {i+1}' for i in range(15)]), 'structured 15'),
        ('20 200\n' + '\n'.join([f'{random.randint(1, 50)} {random.randint(1, 20)}' for _ in range(20)]), 'random 20'),
        ('25 250\n' + '\n'.join([f'{(i+1)*5} {(i+1)*2}' for i in range(25)]), 'structured 25'),
        ('30 300\n' + '\n'.join([f'{random.randint(10, 100)} {random.randint(5, 50)}' for _ in range(30)]), 'random 30'),
        ('50 500\n' + '\n'.join([f'{10} {5}' for _ in range(50)]), 'all same 50'),
        ('100 1000\n' + '\n'.join([f'{random.randint(1, 200)} {random.randint(1, 100)}' for _ in range(100)]), 'random 100'),
    ]
    
    for inp, desc in public_cases:
        output = run_solution(solution_file, inp)
        if output:
            tests['public'].append({'input': inp, 'output': output})
    
    # Hidden tests (22)
    for _ in range(22):
        n = random.choice([500, 1000, 5000, 10000, 50000, 100000])
        T = random.randint(n * 10, n * 100)
        
        events = []
        for _ in range(n):
            demand = random.randint(1, 1000)
            max_tickets = random.randint(1, 500)
            events.append(f'{demand} {max_tickets}')
        
        input_str = f"{n} {T}\n{chr(10).join(events)}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    return tests


def generate_grd012_tests():
    """GRD-012: Workshop Task Cooldown Priority - Task scheduling with cooldown"""
    solution_file = 'solutions/python/GRD-012-workshop-task-cooldown-priority.py'
    
    tests = {'samples': [], 'public': [], 'hidden': []}
    
    # Sample tests
    tests['samples'].append({'input': '3 2\nA 5\nB 3\nA 2', 'output': '7'})
    tests['samples'].append({'input': '4 3\nX 10\nY 5\nX 3\nZ 8', 'output': '14'})
    tests['samples'].append({'input': '2 1\nA 5\nA 3', 'output': '4'})
    
    # Public tests (15)
    public_cases = [
        ('1 0\nA 10', 'single task no cooldown'),
        ('1 5\nA 10', 'single task with cooldown'),
        ('2 0\nA 5\nB 3', 'two different no cooldown'),
        ('2 1\nA 5\nB 3', 'two different with cooldown'),
        ('3 0\nA 5\nA 3\nA 2', 'three same no cooldown'),
        ('3 2\nA 10\nB 8\nC 6', 'three different'),
        ('4 1\nA 5\nA 5\nA 5\nA 5', 'four same with cooldown'),
        ('5 2\nA 10\nB 9\nC 8\nD 7\nE 6', 'five different'),
        ('6 3\nA 10\nA 9\nB 8\nB 7\nC 6\nC 5', 'pairs with cooldown'),
        ('10 2\n' + '\n'.join([f'T{i%5} {random.randint(1, 20)}' for i in range(10)]), 'random 10'),
        ('15 3\n' + '\n'.join([f'T{i%7} {random.randint(5, 50)}' for i in range(15)]), 'random 15'),
        ('20 4\n' + '\n'.join([f'T{i%10} {random.randint(10, 100)}' for i in range(20)]), 'random 20'),
        ('25 5\n' + '\n'.join([f'T{i%15} {random.randint(1, 1000)}' for i in range(25)]), 'random 25'),
        ('50 10\n' + '\n'.join([f'T{i%25} {random.randint(1, 10000)}' for i in range(50)]), 'random 50'),
        ('100 20\n' + '\n'.join([f'T{i%50} {random.randint(1, 100000)}' for i in range(100)]), 'random 100'),
    ]
    
    for inp, desc in public_cases:
        output = run_solution(solution_file, inp)
        if output:
            tests['public'].append({'input': inp, 'output': output})
    
    # Hidden tests (22)
    for _ in range(22):
        n = random.choice([500, 1000, 5000, 10000, 50000, 100000])
        K = random.randint(0, min(n-1, 1000))
        
        tasks = []
        num_types = random.randint(1, min(n, 10000))
        for _ in range(n):
            task_type = f'T{random.randint(0, num_types-1)}'
            priority = random.randint(1, 10**9)
            tasks.append(f'{task_type} {priority}')
        
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
    print(f"✓ {problem_id}: {len(tests['samples'])} samples, {len(tests['public'])} public, {len(tests['hidden'])} hidden (Total: {total})")


def main():
    """Generate test cases for GRD-007 through GRD-012"""
    print("=" * 80)
    print("GREEDY MODULE TEST CASE GENERATOR (Part 2)")
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
        print(f"Generating tests for {problem_id}...")
        try:
            tests = generator_func()
            save_testcases(problem_id, tests)
        except Exception as e:
            print(f"✗ Error generating tests for {problem_id}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 80)
    print("Test case generation complete!")
    print("=" * 80)


if __name__ == '__main__':
    main()
