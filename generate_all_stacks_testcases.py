#!/usr/bin/env python3
"""
Comprehensive test case generator for all 16 Stacks problems.
Generates test cases from verified solutions.
"""

import yaml
import subprocess
import random
from pathlib import Path
import glob

class TestGenerator:
    """Base class for test generation."""

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
            return f"ERROR"

    def add_test(self, category, test_input):
        """Add a test case with solution output."""
        output = self.run_solution(test_input)
        if output not in ["TIMEOUT", "ERROR"]:
            self.test_cases[category].append({
                'input': test_input,
                'output': output
            })
            return output
        return None

    def save_yaml(self, output_file):
        """Save test cases to YAML."""
        yaml_data = {'problem_id': self.problem_id}
        for category in ['samples', 'public', 'hidden']:
            yaml_data[category] = [
                {'input': c["input"], 'output': c["output"]}
                for c in self.test_cases[category]
            ]

        with open(output_file, 'w') as f:
            yaml.dump(yaml_data, f, default_flow_style=False, sort_keys=False,
                     allow_unicode=True, width=float('inf'))

# STK-001: Notebook Undo Simulator
class STK001Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '1\nPUSH 5\n')
        self.add_test('samples', '3\nPUSH 10\nTOP\nPOP\n')
        self.add_test('samples', '2\nPOP\nTOP\n')

        # Public
        ops_list = [
            '5\nPUSH 1\nPUSH 2\nTOP\nPOP\nPOP\n',
            '6\nPUSH 100\nPUSH 200\nTOP\nPOP\nTOP\nPOP\n',
            '4\nPOP\nPOP\nTOP\nPOP\n',
            '5\nPUSH 5\nPUSH 5\nTOP\nPOP\nTOP\n',
            '7\nPUSH 1\nPUSH 2\nPUSH 3\nPOP\nTOP\nPOP\nPOP\n',
        ]
        for ops in ops_list:
            self.add_test('public', ops)

        # Hidden
        for _ in range(30):
            m = random.randint(3, 20)
            ops = []
            for _ in range(m):
                op = random.choice(['PUSH', 'POP', 'TOP'])
                if op == 'PUSH':
                    ops.append(f'PUSH {random.randint(1, 1000)}')
                else:
                    ops.append(op)
            test_input = f'{m}\n' + '\n'.join(ops) + '\n'
            self.add_test('hidden', test_input)

# STK-002: Bracket Repair
class STK002Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '()\n')
        self.add_test('samples', '([)]\n')
        self.add_test('samples', '{{{\n')

        # Public
        brackets_list = [
            '(}[)))}(}}{',
            '{]((()){{',
            '{)}}}\n',
            '(([)))',
            '[({})]',
        ]
        for s in brackets_list:
            self.add_test('public', s + '\n')

        # Hidden
        for _ in range(30):
            length = random.randint(2, 30)
            s = ''.join(random.choice('()[]{}?') for _ in range(length))
            self.add_test('hidden', s + '\n')

# STK-003: Conveyor Weighted Deduplication
class STK003Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '0\n')
        self.add_test('samples', '2\na 2\na 3\n')
        self.add_test('samples', '3\nx 5\ny 5\nz 10\n')

        # Public
        for _ in range(5):
            n = random.randint(1, 10)
            test_input = f'{n}\n'
            for _ in range(n):
                char = chr(ord('a') + random.randint(0, 9))
                weight = random.randint(1, 100)
                test_input += f'{char} {weight}\n'
            self.add_test('public', test_input)

        # Hidden
        for _ in range(30):
            n = random.randint(0, 15)
            test_input = f'{n}\n'
            for _ in range(n):
                char = chr(ord('a') + random.randint(0, 25))
                weight = random.randint(1, 1000)
                test_input += f'{char} {weight}\n'
            self.add_test('hidden', test_input)

# STK-004: Rooftop Sunset Count
class STK004Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '5\n2 5 2 6 1\n')
        self.add_test('samples', '5\n1 2 3 4 5\n')
        self.add_test('samples', '5\n5 4 3 2 1\n')

        # Public
        for _ in range(5):
            n = random.randint(5, 15)
            heights = [random.randint(1, 100) for _ in range(n)]
            test_input = f'{n}\n' + ' '.join(map(str, heights)) + '\n'
            self.add_test('public', test_input)

        # Hidden
        for _ in range(30):
            n = random.randint(3, 30)
            pattern = random.choice(['inc', 'dec', 'valley', 'peak', 'random'])
            if pattern == 'inc':
                heights = sorted([random.randint(1, 100) for _ in range(n)])
            elif pattern == 'dec':
                heights = sorted([random.randint(1, 100) for _ in range(n)], reverse=True)
            elif pattern == 'valley':
                mid = n // 2
                heights = list(range(n, mid, -1)) + list(range(mid, 0, -1))
            elif pattern == 'peak':
                mid = n // 2
                heights = list(range(1, mid+1)) + list(range(mid, 0, -1))
            else:
                heights = [random.randint(1, 100) for _ in range(n)]
            test_input = f'{n}\n' + ' '.join(map(str, heights)) + '\n'
            self.add_test('hidden', test_input)

# STK-005: Workshop Next Taller Width
class STK005Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '4\n1 5 0 3\n2\n')
        self.add_test('samples', '5\n3 1 4 1 5\n2\n')
        self.add_test('samples', '3\n1 2 3\n1\n')

        # Public
        for _ in range(5):
            n = random.randint(5, 15)
            h = [random.randint(1, 100) for _ in range(n)]
            w = random.randint(1, n)
            test_input = f'{n}\n' + ' '.join(map(str, h)) + f'\n{w}\n'
            self.add_test('public', test_input)

        # Hidden
        for _ in range(30):
            n = random.randint(3, 30)
            h = [random.randint(1, 100) for _ in range(n)]
            w = random.randint(1, n)
            test_input = f'{n}\n' + ' '.join(map(str, h)) + f'\n{w}\n'
            self.add_test('hidden', test_input)

# STK-006: Assembly Previous Greater Parity
class STK006Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '5\n2 4 6 8 10\n')
        self.add_test('samples', '5\n1 3 5 7 9\n')
        self.add_test('samples', '5\n5 5 5 5 5\n')

        # Public
        for _ in range(5):
            n = random.randint(5, 15)
            arr = [random.randint(1, 100) for _ in range(n)]
            test_input = f'{n}\n' + ' '.join(map(str, arr)) + '\n'
            self.add_test('public', test_input)

        # Hidden
        for _ in range(30):
            n = random.randint(3, 30)
            arr = [random.randint(1, 100) for _ in range(n)]
            test_input = f'{n}\n' + ' '.join(map(str, arr)) + '\n'
            self.add_test('hidden', test_input)

# STK-007: Trading Desk Threshold Jump
class STK007Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '3\n1 3 2\n1\n')
        self.add_test('samples', '4\n5 5 5 5\n3\n')
        self.add_test('samples', '5\n1 2 3 4 5\n2\n')

        # Public
        for _ in range(5):
            n = random.randint(5, 15)
            prices = [random.randint(1, 100) for _ in range(n)]
            t = random.randint(1, 50)
            test_input = f'{n}\n' + ' '.join(map(str, prices)) + f'\n{t}\n'
            self.add_test('public', test_input)

        # Hidden
        for _ in range(30):
            n = random.randint(3, 20)
            prices = [random.randint(1, 100) for _ in range(n)]
            t = random.randint(1, 50)
            test_input = f'{n}\n' + ' '.join(map(str, prices)) + f'\n{t}\n'
            self.add_test('hidden', test_input)

# STK-008: Canteen Token Climb Span
class STK008Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '5\n3 1 2 2 5\n')
        self.add_test('samples', '4\n1 2 3 4\n')
        self.add_test('samples', '4\n4 3 2 1\n')

        # Public
        for _ in range(5):
            n = random.randint(5, 15)
            demand = [random.randint(1, 100) for _ in range(n)]
            test_input = f'{n}\n' + ' '.join(map(str, demand)) + '\n'
            self.add_test('public', test_input)

        # Hidden
        for _ in range(30):
            n = random.randint(3, 30)
            demand = [random.randint(1, 100) for _ in range(n)]
            test_input = f'{n}\n' + ' '.join(map(str, demand)) + '\n'
            self.add_test('hidden', test_input)

# STK-009: Sliding Min Stack
class STK009Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '3\nPUSH -3\nMIN 1\nPOP\n')
        self.add_test('samples', '2\nPUSH 5\nMIN 1\n')
        self.add_test('samples', '4\nPUSH 10\nPUSH 20\nMIN 2\nPOP\n')

        # Public
        ops_list = [
            '5\nPUSH 1\nPUSH 2\nMIN 2\nPOP\nMIN 1\n',
            '6\nPUSH 5\nPUSH 3\nMIN 2\nPOP\nMIN 1\nPOP\n',
            '4\nPUSH 10\nPUSH 10\nMIN 2\nMIN 1\n',
            '5\nPUSH 1\nPUSH 1\nMIN 1\nPOP\nMIN 1\n',
            '3\nPUSH 99\nMIN 1\nPOP\n',
        ]
        for ops in ops_list:
            self.add_test('public', ops + '\n')

        # Hidden
        for _ in range(30):
            m = random.randint(3, 20)
            ops = []
            for _ in range(m):
                op = random.choice(['PUSH', 'POP', 'MIN'])
                if op == 'PUSH':
                    ops.append(f'PUSH {random.randint(-100, 100)}')
                elif op == 'MIN':
                    ops.append(f'MIN {random.randint(1, 5)}')
                else:
                    ops.append('POP')
            test_input = f'{m}\n' + '\n'.join(ops) + '\n'
            self.add_test('hidden', test_input)

# STK-010: Stadium Max Tracker
class STK010Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '4\nPUSH 5\nGETMAX\nPUSH 10\nGETMAX\n')
        self.add_test('samples', '3\nPUSH 3\nTOP\nPOP\n')
        self.add_test('samples', '2\nGETMAX\nPOP\n')

        # Public
        ops_list = [
            '6\nPUSH 1\nPUSH 2\nGETMAX\nPOP\nGETMAX\nPOP\n',
            '5\nPUSH 5\nPUSH 5\nGETMAX\nPOP\nGETMAX\n',
            '4\nPUSH 10\nPUSH 20\nTOP\nGETMAX\n',
            '6\nPUSH 3\nTOP\nGETMAX\nPOP\nTOP\nGETMAX\n',
            '3\nPUSH 100\nGETMAX\nGETMAX\n',
        ]
        for ops in ops_list:
            self.add_test('public', ops + '\n')

        # Hidden
        for _ in range(30):
            m = random.randint(3, 20)
            ops = []
            for _ in range(m):
                op = random.choice(['PUSH', 'POP', 'TOP', 'GETMAX'])
                if op == 'PUSH':
                    ops.append(f'PUSH {random.randint(1, 100)}')
                else:
                    ops.append(op)
            test_input = f'{m}\n' + '\n'.join(ops) + '\n'
            self.add_test('hidden', test_input)

# STK-011: Circuit Postfix Variables
class STK011Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '2\na 5\nb 3\na b +\n')
        self.add_test('samples', '2\nx 10\ny 2\nx y -\n')
        self.add_test('samples', '1\nn 4\nn n *\n')

        # Public
        for _ in range(5):
            num_vars = random.randint(1, 3)
            test_input = f'{num_vars}\n'
            vars_dict = {}
            for _ in range(num_vars):
                var = chr(ord('a') + random.randint(0, 5))
                val = random.randint(1, 50)
                test_input += f'{var} {val}\n'
                vars_dict[var] = val

            ops = [var for var in vars_dict.keys()]
            if len(ops) >= 2:
                ops.append(random.choice(['+', '-', '*', '/']))
            test_input += ' '.join(ops) + '\n'
            self.add_test('public', test_input)

        # Hidden
        for _ in range(30):
            num_vars = random.randint(1, 3)
            test_input = f'{num_vars}\n'
            vars_dict = {}
            for i in range(num_vars):
                var = chr(ord('a') + i)
                val = random.randint(1, 100)
                test_input += f'{var} {val}\n'
                vars_dict[var] = val

            ops = list(vars_dict.keys())
            if len(ops) >= 2:
                ops.append(random.choice(['+', '-', '*', '/']))
            test_input += ' '.join(ops) + '\n'
            self.add_test('hidden', test_input)

# STK-012: Campus Expression Optimizer
class STK012Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', 'a+b\n')
        self.add_test('samples', '(a)\n')
        self.add_test('samples', 'a+b*c\n')

        # Public
        exprs = [
            '(a+b)',
            'a*b+c',
            'a+(b*c)',
            '((a))',
            'a+b+c',
        ]
        for expr in exprs:
            self.add_test('public', expr + '\n')

        # Hidden
        for _ in range(30):
            # Generate random valid expression
            vars = [chr(ord('a') + random.randint(0, 5)) for _ in range(random.randint(1, 5))]
            ops = [random.choice(['+', '-', '*', '/', '%', '^']) for _ in range(len(vars)-1)]
            expr = vars[0]
            for i, op in enumerate(ops):
                expr += op + vars[i+1]

            # Randomly add parentheses
            if random.random() > 0.5:
                expr = '(' + expr + ')'

            self.add_test('hidden', expr + '\n')

# STK-013: Auditorium Histogram Booster
class STK013Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '4\n2 1 5 6\n2\n')
        self.add_test('samples', '3\n3 3 3\n5\n')
        self.add_test('samples', '5\n1 2 3 2 1\n3\n')

        # Public
        for _ in range(5):
            n = random.randint(5, 15)
            h = [random.randint(1, 100) for _ in range(n)]
            b = random.randint(1, 50)
            test_input = f'{n}\n' + ' '.join(map(str, h)) + f'\n{b}\n'
            self.add_test('public', test_input)

        # Hidden
        for _ in range(30):
            n = random.randint(3, 20)
            h = [random.randint(1, 100) for _ in range(n)]
            b = random.randint(1, 100)
            test_input = f'{n}\n' + ' '.join(map(str, h)) + f'\n{b}\n'
            self.add_test('hidden', test_input)

# STK-014: Shuttle Validation Time Windows
class STK014Generator(TestGenerator):
    def generate(self):
        # Samples - Simple valid case
        self.add_test('samples', '1\n1 1\n1\n1 1\n0\n0\n')
        self.add_test('samples', '2\n1 0\n2 1\n2\n1 0\n2 1\n0\n0\n')
        self.add_test('samples', '1\n5 2\n1\n5 3\n0\n0\n')

        # Public
        for _ in range(5):
            num_push = random.randint(1, 3)
            test_input = f'{num_push}\n'
            for i in range(num_push):
                val = random.randint(1, 10)
                time = i
                test_input += f'{val} {time}\n'

            num_pop = num_push
            test_input += f'{num_pop}\n'
            for i in range(num_pop):
                test_input += f'{i+1} {i+1}\n'

            test_input += '0\n0\n'
            self.add_test('public', test_input)

        # Hidden
        for _ in range(30):
            num_push = random.randint(1, 5)
            test_input = f'{num_push}\n'
            for i in range(num_push):
                val = i + 1
                time = random.randint(0, 10)
                test_input += f'{val} {time}\n'

            num_pop = num_push
            test_input += f'{num_pop}\n'
            for i in range(num_pop):
                test_input += f'{i+1} {random.randint(i, i+5)}\n'

            test_input += '0\n0\n'
            self.add_test('hidden', test_input)

# STK-015: Bike Repair Plates
class STK015Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '4\n1 2 3 4\n')
        self.add_test('samples', '4\n4 3 2 1\n')
        self.add_test('samples', '5\n3 1 2 2 5\n')

        # Public
        for _ in range(5):
            n = random.randint(5, 15)
            d = [random.randint(1, 100) for _ in range(n)]
            test_input = f'{n}\n' + ' '.join(map(str, d)) + '\n'
            self.add_test('public', test_input)

        # Hidden
        for _ in range(30):
            n = random.randint(3, 30)
            d = [random.randint(1, 100) for _ in range(n)]
            test_input = f'{n}\n' + ' '.join(map(str, d)) + '\n'
            self.add_test('hidden', test_input)

# STK-016: Assembly Line Span Reset
class STK016Generator(TestGenerator):
    def generate(self):
        # Samples
        self.add_test('samples', '5\n3 1 2 2 5\n')
        self.add_test('samples', '4\n1 2 3 4\n')
        self.add_test('samples', '4\n4 3 2 1\n')

        # Public
        for _ in range(5):
            n = random.randint(5, 15)
            counts = [random.randint(1, 100) for _ in range(n)]
            test_input = f'{n}\n' + ' '.join(map(str, counts)) + '\n'
            self.add_test('public', test_input)

        # Hidden
        for _ in range(30):
            n = random.randint(3, 30)
            counts = [random.randint(1, 100) for _ in range(n)]
            test_input = f'{n}\n' + ' '.join(map(str, counts)) + '\n'
            self.add_test('hidden', test_input)

# Generator mapping
GENERATORS = {
    'STK-001': (STK001Generator, 'STK_NOTEBOOK_UNDO_SIMULATOR__4827'),
    'STK-002': (STK002Generator, 'STK_LAB_MIXED_BRACKET_REPAIR__7391'),
    'STK-003': (STK003Generator, 'STK_CONVEYOR_WEIGHTED_DEDUPLICATION__5623'),
    'STK-004': (STK004Generator, 'STK_ROOFTOP_SUNSET_COUNT__2974'),
    'STK-005': (STK005Generator, 'STK_WORKSHOP_NEXT_TALLER_WIDTH__3845'),
    'STK-006': (STK006Generator, 'STK_ASSEMBLY_PREVIOUS_GREATER_PARITY__6271'),
    'STK-007': (STK007Generator, 'STK_TRADING_DESK_THRESHOLD_JUMP__5432'),
    'STK-008': (STK008Generator, 'STK_CANTEEN_TOKEN_CLIMB_SPAN__6180'),
    'STK-009': (STK009Generator, 'STK_LAB_SLIDING_MIN_STACK__8194'),
    'STK-010': (STK010Generator, 'STK_STADIUM_MAX_TRACKER__4039'),
    'STK-011': (STK011Generator, 'STK_CIRCUIT_POSTFIX_VARIABLES__7563'),
    'STK-012': (STK012Generator, 'STK_CAMPUS_EXPRESSION_OPTIMIZER__6248'),
    'STK-013': (STK013Generator, 'STK_AUDITORIUM_HISTOGRAM_ONE_BOOSTER__8416'),
    'STK-014': (STK014Generator, 'STK_SHUTTLE_VALIDATION_TIME_WINDOWS__5182'),
    'STK-015': (STK015Generator, 'STK_BIKE_REPAIR_PLATES__7851'),
    'STK-016': (STK016Generator, 'STK_ASSEMBLY_LINE_SPAN_RESET__3965'),
}

def main():
    """Generate test cases for all 16 Stacks problems."""
    for problem_id, (gen_class, prob_id) in GENERATORS.items():
        solution_path = f"dsa-problems/Stacks/solutions/python/{problem_id}-*.py"
        files = glob.glob(solution_path)

        if not files:
            print(f"{problem_id}: Solution not found")
            continue

        solution_path = files[0]
        yaml_files = glob.glob(f"dsa-problems/Stacks/testcases/{problem_id}-*.yaml")

        if not yaml_files:
            print(f"{problem_id}: Test case file not found")
            continue

        output_file = yaml_files[0]

        print(f"Generating {problem_id}...", end=" ", flush=True)

        gen = gen_class(prob_id, solution_path)
        gen.generate()
        gen.save_yaml(output_file)

        total = len(gen.test_cases['samples']) + len(gen.test_cases['public']) + len(gen.test_cases['hidden'])
        print(f"✓ {total} tests ({len(gen.test_cases['samples'])}+{len(gen.test_cases['public'])}+{len(gen.test_cases['hidden'])})")

if __name__ == "__main__":
    main()
