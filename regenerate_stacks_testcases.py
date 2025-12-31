#!/usr/bin/env python3
"""
Regenerate Stacks test cases from verified solutions.

For each problem:
1. Create sample test cases (3: basic, simple, edge)
2. Create public test cases (5-7: moderate complexity)
3. Create hidden test cases (25-30: edge/corner/constraint-based)

Uses the solution as the source of truth for expected outputs.
"""

import yaml
import subprocess
import random
from pathlib import Path

class StacksTestGenerator:
    """Generate test cases for Stacks problems."""

    def __init__(self, problem_id, solution_path):
        self.problem_id = problem_id
        self.solution_path = solution_path
        self.test_cases = {'samples': [], 'public': [], 'hidden': []}

    def run_solution(self, test_input):
        """Run solution and capture output."""
        try:
            result = subprocess.run(
                ['python3', self.solution_path],
                input=test_input,
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            return "TIMEOUT"
        except Exception as e:
            return f"ERROR: {str(e)}"

    def add_test(self, category, test_input):
        """Add a test case and get expected output from solution."""
        output = self.run_solution(test_input)
        self.test_cases[category].append({
            'input': test_input,
            'output': output
        })
        return output

    def save_yaml(self, output_file):
        """Save test cases to YAML file."""
        yaml_data = {'problem_id': self.problem_id}
        for category in ['samples', 'public', 'hidden']:
            yaml_data[category] = [
                {'input': f'|-\n{c["input"]}', 'output': f'|-\n{c["output"]}'}
                for c in self.test_cases[category]
            ]

        with open(output_file, 'w') as f:
            yaml.dump(yaml_data, f, default_flow_style=False, sort_keys=False)

# Test case generators for each problem type

def generate_stk001_tests(gen):
    """STK-001: Notebook Undo Simulator (Stack Operations)"""
    # Sample: PUSH, TOP on single element
    gen.add_test('samples', '1\nPUSH 5\n')
    # Sample: Mix of operations
    gen.add_test('samples', '3\nPUSH 1\nPOP\nTOP\n')
    # Sample: Empty stack operations
    gen.add_test('samples', '2\nPOP\nTOP\n')

    # Public: Various operation sequences
    for _ in range(5):
        ops = ['PUSH 10', 'PUSH 20', 'TOP', 'POP', 'PUSH 30', 'POP', 'TOP']
        m = len(ops)
        test_input = f'{m}\n' + '\n'.join(ops) + '\n'
        gen.add_test('public', test_input)

    # Hidden: Generate 30 varied test cases
    for _ in range(30):
        m = random.randint(5, 20)
        ops = []
        for _ in range(m):
            op_type = random.choice(['PUSH', 'POP', 'TOP'])
            if op_type == 'PUSH':
                ops.append(f'PUSH {random.randint(1, 100)}')
            else:
                ops.append(op_type)
        test_input = f'{m}\n' + '\n'.join(ops) + '\n'
        gen.add_test('hidden', test_input)

def generate_stk004_tests(gen):
    """STK-004: Rooftop Sunset Count (Monotonic Stack)"""
    # Sample cases
    gen.add_test('samples', '5\n2 5 2 6 1\n')
    gen.add_test('samples', '4\n1 2 3 4\n')
    gen.add_test('samples', '4\n4 3 2 1\n')

    # Public: various patterns
    for _ in range(5):
        n = random.randint(5, 10)
        heights = [random.randint(1, 100) for _ in range(n)]
        test_input = f'{n}\n' + ' '.join(map(str, heights)) + '\n'
        gen.add_test('public', test_input)

    # Hidden: 30 test cases with various patterns
    for _ in range(30):
        n = random.randint(3, 20)
        pattern = random.choice(['increasing', 'decreasing', 'random', 'all_same'])

        if pattern == 'increasing':
            heights = list(range(1, n+1))
        elif pattern == 'decreasing':
            heights = list(range(n, 0, -1))
        elif pattern == 'all_same':
            heights = [5] * n
        else:
            heights = [random.randint(1, 100) for _ in range(n)]

        random.shuffle(heights) if pattern not in ['increasing', 'decreasing'] else None
        test_input = f'{n}\n' + ' '.join(map(str, heights)) + '\n'
        gen.add_test('hidden', test_input)

def generate_stk008_tests(gen):
    """STK-008: Canteen Token Climb Span"""
    # Sample
    gen.add_test('samples', '7\n1 1 1 2 1 4 6\n')
    gen.add_test('samples', '4\n1 2 3 4\n')
    gen.add_test('samples', '4\n4 3 2 1\n')

    # Public
    for _ in range(5):
        n = random.randint(5, 10)
        demand = [random.randint(1, 100) for _ in range(n)]
        test_input = f'{n}\n' + ' '.join(map(str, demand)) + '\n'
        gen.add_test('public', test_input)

    # Hidden
    for _ in range(30):
        n = random.randint(3, 20)
        demand = [random.randint(1, 100) for _ in range(n)]
        test_input = f'{n}\n' + ' '.join(map(str, demand)) + '\n'
        gen.add_test('hidden', test_input)

def generate_stk016_tests(gen):
    """STK-016: Assembly Line Span Reset"""
    # Sample
    gen.add_test('samples', '7\n1 1 1 2 1 4 6\n')
    gen.add_test('samples', '4\n1 2 3 4\n')
    gen.add_test('samples', '4\n4 3 2 1\n')

    # Public
    for _ in range(5):
        n = random.randint(5, 10)
        counts = [random.randint(1, 100) for _ in range(n)]
        test_input = f'{n}\n' + ' '.join(map(str, counts)) + '\n'
        gen.add_test('public', test_input)

    # Hidden
    for _ in range(30):
        n = random.randint(3, 20)
        counts = [random.randint(1, 100) for _ in range(n)]
        test_input = f'{n}\n' + ' '.join(map(str, counts)) + '\n'
        gen.add_test('hidden', test_input)

def generate_stk003_tests(gen):
    """STK-003: Conveyor Weighted Deduplication"""
    # Sample
    gen.add_test('samples', '3\n2\na 1\nb 2\nc 1\n')
    gen.add_test('samples', '2\n2\nd 3\ne 1\n')
    gen.add_test('samples', '0\n')

    # Public
    for _ in range(5):
        n = random.randint(1, 10)
        test_input = f'{n}\n'
        for _ in range(n):
            char = chr(ord('a') + random.randint(0, 9))
            weight = random.randint(1, 100)
            test_input += f'{char} {weight}\n'
        gen.add_test('public', test_input)

    # Hidden
    for _ in range(30):
        n = random.randint(0, 15)
        test_input = f'{n}\n'
        for _ in range(n):
            char = chr(ord('a') + random.randint(0, 25))
            weight = random.randint(1, 1000000)
            test_input += f'{char} {weight}\n'
        gen.add_test('hidden', test_input)

def main():
    """Generate test cases for all Stacks problems."""
    generators = [
        ('STK-001', 'dsa-problems/Stacks/solutions/python/STK-001-notebook-undo-simulator.py', generate_stk001_tests),
        ('STK-003', 'dsa-problems/Stacks/solutions/python/STK-003-conveyor-weighted-deduplication.py', generate_stk003_tests),
        ('STK-004', 'dsa-problems/Stacks/solutions/python/STK-004-rooftop-sunset-count.py', generate_stk004_tests),
        ('STK-008', 'dsa-problems/Stacks/solutions/python/STK-008-canteen-token-climb-span.py', generate_stk008_tests),
        ('STK-016', 'dsa-problems/Stacks/solutions/python/STK-016-assembly-line-span-reset.py', generate_stk016_tests),
    ]

    for problem_id, solution_path, generator_func in generators:
        if not Path(solution_path).exists():
            print(f"{problem_id}: Solution file not found")
            continue

        print(f"Generating tests for {problem_id}...", end=" ")

        # Get the actual problem_id from YAML
        import glob
        yaml_files = glob.glob(f"dsa-problems/Stacks/testcases/{problem_id}-*.yaml")
        if yaml_files:
            with open(yaml_files[0], 'r') as f:
                old_data = yaml.safe_load(f)
                actual_problem_id = old_data.get('problem_id', problem_id)
        else:
            actual_problem_id = problem_id

        gen = StacksTestGenerator(actual_problem_id, solution_path)
        generator_func(gen)

        # Save to file
        output_file = f"dsa-problems/Stacks/testcases/{problem_id}-*.yaml"
        import glob
        files = glob.glob(output_file)
        if files:
            output_file = files[0]
        else:
            output_file = f"dsa-problems/Stacks/testcases/{problem_id}-temp.yaml"

        gen.save_yaml(output_file)
        print(f"✓ ({len(gen.test_cases['samples'])} + {len(gen.test_cases['public'])} + {len(gen.test_cases['hidden'])} tests)")

if __name__ == "__main__":
    main()
