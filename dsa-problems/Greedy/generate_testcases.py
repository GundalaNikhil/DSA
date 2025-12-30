#!/usr/bin/env python3
"""
Comprehensive Test Case Generator for Greedy Problems
Generates 40 test cases per problem (2-3 samples + 15-18 public + 20-22 hidden)
"""

import sys
import os
import subprocess
import yaml
import random
from pathlib import Path

# Ensure we can import the solution modules
sys.path.insert(0, str(Path(__file__).parent / 'solutions' / 'python'))


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


def generate_grd004_tests():
    """GRD-004: Library Power Backup - Minimize battery swaps"""
    solution_file = 'solutions/python/GRD-004-library-power-backup.py'
    
    tests = {
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Sample 1: From problem statement
    tests['samples'].append({
        'input': '3 7\n3 5 2',
        'output': '1'
    })
    
    # Sample 2: Impossible case
    tests['samples'].append({
        'input': '2 10\n3 4',
        'output': '-1'
    })
    
    # Sample 3: No swaps needed
    tests['samples'].append({
        'input': '1 5\n10',
        'output': '0'
    })
    
    # Public test cases (15 tests)
    public_cases = [
        # Edge cases
        ('1 1\n1', 'single battery exact match'),
        ('1 1\n2', 'single battery excess'),
        ('2 5\n5 5', 'all same capacity'),
        ('3 10\n10 10 10', 'large identical batteries'),
        
        # Small cases
        ('2 5\n2 3', 'two batteries exact sum'),
        ('3 5\n1 2 2', 'multiple small batteries'),
        ('4 10\n1 2 3 4', 'ascending capacities'),
        ('4 10\n4 3 2 1', 'descending capacities'),
        
        # Medium cases
        ('5 20\n5 5 5 5 5', 'many equal batteries'),
        ('5 15\n10 3 2 1 1', 'one large dominant'),
        ('6 30\n10 9 8 7 6 5', 'descending sequence'),
        ('7 25\n1 2 3 4 5 6 7', 'ascending sequence'),
        
        # Boundary cases
        ('10 50\n5 5 5 5 5 5 5 5 5 5', 'exactly enough'),
        ('10 51\n5 5 5 5 5 5 5 5 5 5', 'one short - impossible'),
        ('10 100\n15 14 13 12 11 10 9 8 7 6', 'large batteries'),
    ]
    
    for input_str, description in public_cases:
        output = run_solution(solution_file, input_str)
        if output:
            tests['public'].append({'input': input_str, 'output': output})
    
    # Hidden test cases (22 tests)
    hidden_configs = [
        # Edge cases
        (1, 1000000000, [1000000000]),
        (1, 1000000000, [999999999]),
        
        # Random small
        (5, 20, None),
        (5, 30, None),
        (8, 50, None),
        (10, 75, None),
        
        # Random medium
        (50, 500, None),
        (100, 1000, None),
        (100, 5000, None),
        
        # Large with patterns
        (1000, 10000, None),
        (1000, 50000, None),
        (5000, 100000, None),
        
        # Large random
        (10000, 1000000, None),
        (50000, 10000000, None),
        (100000, 100000000, None),
        
        # Large edge cases
        (100000, 1000000000, [10000] * 100000),
        (100000, 999999999, [10000] * 100000),
        
        # All ones (worst case)
        (1000, 500, [1] * 1000),
        (5000, 2500, [1] * 5000),
        
        # Extreme differences
        (10, 1000000000, [999999990, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
        (20, 2000000000, [100000000] * 20),
        
        # Mixed patterns
        (100, 10000, None),
    ]
    
    for config in hidden_configs:
        n, T = config[0], config[1]
        if config[2]:
            capacities = config[2]
        else:
            # Generate random capacities
            capacities = [random.randint(1, min(T, 10000)) for _ in range(n)]
        
        input_str = f"{n} {T}\n{' '.join(map(str, capacities))}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    return tests


def generate_grd005_tests():
    """GRD-005: Shuttle Overtime Minimizer"""
    solution_file = 'solutions/python/GRD-005-shuttle-overtime-minimizer.py'
    
    tests = {
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Sample tests
    sample_inputs = [
        '2 8\n4 3\n6 5',
        '3 10\n5 2\n5 3\n5 1',
        '1 10\n0 5',
    ]
    
    for inp in sample_inputs:
        output = run_solution(solution_file, inp)
        if output:
            tests['samples'].append({'input': inp, 'output': output})
    
    # Public test cases (15 tests)
    public_inputs = [
        # Edge cases
        '1 5\n5 1',
        '1 5\n10 1',
        '2 10\n5 1\n5 2',
        '2 10\n10 1\n10 2',
        
        # Small cases
        '3 15\n5 1\n5 2\n5 3',
        '3 20\n10 5\n5 3\n5 2',
        '4 25\n5 1\n10 2\n15 3\n20 4',
        '5 50\n10 1\n10 2\n10 3\n10 4\n10 5',
        
        # Medium cases
        '10 100\n' + '\n'.join([f'{10} {i+1}' for i in range(10)]),
        '10 150\n' + '\n'.join([f'{15} {i+1}' for i in range(10)]),
        '20 200\n' + '\n'.join([f'{10} {i+1}' for i in range(20)]),
        
        # Large standard hours
        '5 100\n30 10\n30 5\n30 3\n30 2\n30 1',
        '5 50\n20 1\n20 2\n20 3\n20 4\n20 5',
        
        # Zero standard hours
        '3 20\n0 1\n0 2\n0 3',
        '5 100\n0 5\n0 4\n0 3\n0 2\n0 1',
    ]
    
    for inp in public_inputs:
        output = run_solution(solution_file, inp)
        if output:
            tests['public'].append({'input': inp, 'output': output})
    
    # Hidden test cases (22 tests)
    hidden_configs = [
        (10, 50, None),
        (20, 100, None),
        (50, 500, None),
        (100, 1000, None),
        (100, 10000, None),
        (500, 5000, None),
        (1000, 10000, None),
        (1000, 100000, None),
        (5000, 50000, None),
        (10000, 1000000, None),
        (10000, 10000000, None),
        (50000, 100000000, None),
        (100000, 1000000000, None),
        (100000, 1000000000000, None),
    ]
    
    for n, H, _ in hidden_configs:
        shifts = []
        for _ in range(n):
            l = random.randint(0, min(H // n + 10, 1000))
            p = random.randint(1, 100)
            shifts.append(f'{l} {p}')
        input_str = f"{n} {H}\n" + '\n'.join(shifts)
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    # Add more edge cases
    edge_cases = [
        (f'1 1000000000\n0 1', 'all overtime'),
        (f'2 1000000000\n500000000 1\n500000000 2', 'large hours no overtime'),
        (f'10 1000\n' + '\n'.join([f'100 {i+1}' for i in range(10)]), 'exact coverage'),
        (f'10 1001\n' + '\n'.join([f'100 {i+1}' for i in range(10)]), 'minimal overtime'),
        (f'100 10000\n' + '\n'.join([f'100 {100-i}' for i in range(100)]), 'reverse costs'),
        (f'100 5000\n' + '\n'.join([f'100 {i+1}' for i in range(100)]), 'excess capacity'),
        (f'1000 100000\n' + '\n'.join([f'{random.randint(0, 200)} {random.randint(1, 1000)}' for _ in range(1000)]), 'large random 1'),
        (f'1000 1000000\n' + '\n'.join([f'{random.randint(0, 2000)} {random.randint(1, 1000)}' for _ in range(1000)]), 'large random 2'),
    ]
    
    for inp, desc in edge_cases:
        output = run_solution(solution_file, inp)
        if output:
            tests['hidden'].append({'input': inp, 'output': output})
    
    return tests


def generate_grd006_tests():
    """GRD-006: Robotics Component Bundling"""
    solution_file = 'solutions/python/GRD-006-robotics-component-bundling-loss-quality.py'
    
    tests = {
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Sample tests
    sample_inputs = [
        '3 5\n10 20 30\n8 7 6',
        '2 10\n100 200\n5 3',
        '3 8\n50 50 50\n9 9 9',
    ]
    
    for inp in sample_inputs:
        output = run_solution(solution_file, inp)
        if output:
            tests['samples'].append({'input': inp, 'output': output})
    
    # Public test cases (15 tests)
    public_configs = [
        # Edge cases
        (1, 1, [100], [10]),
        (2, 1, [100, 200], [5, 5]),
        (2, 5, [100, 200], [5, 5]),
        
        # Small cases
        (3, 5, [10, 20, 30], [10, 10, 10]),
        (3, 8, [50, 50, 50], [10, 10, 10]),
        (4, 5, [100, 200, 300, 400], [10, 9, 8, 7]),
        (5, 10, [50, 60, 70, 80, 90], [15, 14, 13, 12, 11]),
        
        # Medium cases
        (10, 5, list(range(10, 110, 10)), [10] * 10),
        (10, 15, list(range(100, 200, 10)), list(range(20, 10, -1))),
        (20, 10, [random.randint(10, 1000) for _ in range(20)], [random.randint(10, 50) for _ in range(20)]),
        
        # High quality threshold
        (5, 95, [1000, 2000, 3000, 4000, 5000], [100, 100, 100, 100, 100]),
        (5, 99, [1000, 2000, 3000, 4000, 5000], [100, 100, 100, 100, 100]),
        
        # Low quality
        (5, 1, [100, 200, 300, 400, 500], [5, 4, 3, 2, 1]),
        (10, 1, [random.randint(1, 100) for _ in range(10)], [random.randint(1, 10) for _ in range(10)]),
        
        # Impossible case
        (3, 10, [100, 200, 300], [5, 6, 7]),
    ]
    
    for config in public_configs:
        n, T = config[0], config[1]
        weights = config[2] if len(config) > 2 else [random.randint(1, 1000) for _ in range(n)]
        qualities = config[3] if len(config) > 3 else [random.randint(1, 100) for _ in range(n)]
        
        input_str = f"{n} {T}\n{' '.join(map(str, weights))}\n{' '.join(map(str, qualities))}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['public'].append({'input': input_str, 'output': output})
    
    # Hidden test cases (22 tests)
    hidden_configs = [
        (50, 10, None, None),
        (100, 20, None, None),
        (500, 15, None, None),
        (1000, 25, None, None),
        (5000, 30, None, None),
        (10000, 10, None, None),
        (50000, 5, None, None),
        (100000, 1, None, None),
        (100000, 50, None, None),
        (100000, 99, None, None),
    ]
    
    for n, T, _, _ in hidden_configs:
        weights = [random.randint(1, 1000000000) for _ in range(n)]
        qualities = [random.randint(T, 100) for _ in range(n)]  # Ensure some are valid
        
        input_str = f"{n} {T}\n{' '.join(map(str, weights))}\n{' '.join(map(str, qualities))}"
        output = run_solution(solution_file, input_str)
        if output:
            tests['hidden'].append({'input': input_str, 'output': output})
    
    # Additional edge cases
    for _ in range(12):
        n = random.randint(1000, 50000)
        T = random.randint(1, 99)
        weights = [random.randint(1, 10**9) for _ in range(n)]
        qualities = [random.randint(1, 100) for _ in range(n)]
        
        input_str = f"{n} {T}\n{' '.join(map(str, weights))}\n{' '.join(map(str, qualities))}"
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
    
    print(f"✓ Generated {len(tests['samples'])} samples, {len(tests['public'])} public, {len(tests['hidden'])} hidden tests for {problem_id}")
    print(f"  Total: {len(tests['samples']) + len(tests['public']) + len(tests['hidden'])} tests")


def main():
    """Generate test cases for all Greedy problems"""
    print("=" * 80)
    print("GREEDY MODULE TEST CASE GENERATOR")
    print("=" * 80)
    print()
    
    generators = [
        ('GRD-004-library-power-backup', generate_grd004_tests),
        ('GRD-005-shuttle-overtime-minimizer', generate_grd005_tests),
        ('GRD-006-robotics-component-bundling-loss-quality', generate_grd006_tests),
    ]
    
    for problem_id, generator_func in generators:
        print(f"\nGenerating tests for {problem_id}...")
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
