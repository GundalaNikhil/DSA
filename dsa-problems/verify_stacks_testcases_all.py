#!/usr/bin/env python3
"""
Comprehensive Verification Script for Stacks Topic (STK-001 to STK-016)
Verifies all 608 test cases against editorial solutions.
"""

import yaml
import os
import sys
from collections import deque
from bisect import bisect_left

# Color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# ============================================================================
# Editorial Solutions - MATCHING GENERATION SCRIPT EXACTLY
# ============================================================================

def solve_stk001(input_lines):
    """STK-001: Basic stack with PUSH, POP, TOP"""
    m = int(input_lines[0])
    stack = []
    outputs = []
    
    for i in range(1, m + 1):
        parts = input_lines[i].split()
        if parts[0] == "PUSH":
            stack.append(int(parts[1]))
        elif parts[0] == "POP":
            outputs.append(str(stack.pop()) if stack else "EMPTY")
        elif parts[0] == "TOP":
            outputs.append(str(stack[-1]) if stack else "EMPTY")
    
    return '\n'.join(outputs) if outputs else ""

def solve_stk002(input_lines):
    """STK-002: Bracket repair cost"""
    s = input_lines[0]
    stack = []
    repairs = 0
    
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            matching = {')':'(', ']':'[', '}':'{'}
            if stack and stack[-1] == matching[ch]:
                stack.pop()
            else:
                repairs += 1
    
    return str(repairs + len(stack))

def solve_stk003(input_lines):
    """STK-003: Weighted deduplication"""
    n = int(input_lines[0])
    stack = []
    
    for i in range(1, n + 1):
        val, weight = map(int, input_lines[i].split())
        if stack and stack[-1][0] == val:
            stack[-1] = (val, stack[-1][1] + weight)
            if stack[-1][1] >= 3:
                stack.pop()
        else:
            stack.append((val, weight))
    
    if stack:
        return ' '.join(f"{v},{w}" for v, w in stack)
    return "EMPTY"

def solve_stk004(input_lines):
    """STK-004: Sunset count (monotonic stack)"""
    n = int(input_lines[0])
    heights = list(map(int, input_lines[1].split()))
    
    stack = []
    for h in heights:
        while stack and stack[-1] <= h:
            stack.pop()
        stack.append(h)
    
    return str(len(stack))

def solve_stk005(input_lines):
    """STK-005: Next greater element width"""
    n = int(input_lines[0])
    arr = list(map(int, input_lines[1].split()))
    
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    
    return ' '.join(map(str, result))

def solve_stk006(input_lines):
    """STK-006: Previous greater with same parity"""
    n = int(input_lines[0])
    arr = list(map(int, input_lines[1].split()))
    
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        
        # Find previous greater with same parity
        for j in range(len(stack) - 1, -1, -1):
            if arr[stack[j]] % 2 == arr[i] % 2:
                result[i] = stack[j]
                break
        
        stack.append(i)
    
    return ' '.join(map(str, result))

def solve_stk007(input_lines):
    """STK-007: Threshold jumps"""
    n, threshold = map(int, input_lines[0].split())
    prices = list(map(int, input_lines[1].split()))
    
    jumps = 0
    for i in range(1, len(prices)):
        if abs(prices[i] - prices[i-1]) > threshold:
            jumps += 1
    
    return str(jumps)

def solve_stk008(input_lines):
    """STK-008: Stock span"""
    n = int(input_lines[0])
    prices = list(map(int, input_lines[1].split()))
    
    spans = [1] * n
    stack = []
    
    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        
        spans[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    
    return ' '.join(map(str, spans))

def solve_stk009(input_lines):
    """STK-009: Sliding window minimum"""
    n, k = map(int, input_lines[0].split())
    arr = list(map(int, input_lines[1].split()))
    
    result = []
    dq = deque()
    
    for i in range(n):
        # Remove elements out of window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove larger elements
        while dq and arr[dq[-1]] >= arr[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return ' '.join(map(str, result))

def solve_stk010(input_lines):
    """STK-010: Max stack"""
    m = int(input_lines[0])
    stack = []
    max_stack = []
    outputs = []
    
    for i in range(1, m + 1):
        parts = input_lines[i].split()
        if parts[0] == "PUSH":
            val = int(parts[1])
            stack.append(val)
            if not max_stack:
                max_stack.append(val)
            else:
                max_stack.append(max(val, max_stack[-1]))
        elif parts[0] == "POP":
            if stack:
                stack.pop()
                max_stack.pop()
        elif parts[0] == "MAX":
            if max_stack:
                outputs.append(str(max_stack[-1]))
            else:
                outputs.append("EMPTY")
    
    return '\n'.join(outputs) if outputs else ""

def solve_stk011(input_lines):
    """STK-011: Postfix evaluation with variables"""
    MOD = 1000000007
    
    t = int(input_lines[0])
    tokens = input_lines[1].split()
    m = int(input_lines[2])
    
    variables = {}
    for i in range(3, 3 + m):
        parts = input_lines[i].split()
        variables[parts[0]] = int(parts[1])
    
    stack = []
    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token) % MOD)
        elif token.isalpha() and len(token) == 1:
            stack.append(variables.get(token, 0) % MOD)
        elif token == "DUP":
            if stack:
                stack.append(stack[-1])
        elif token == "SWAP":
            if len(stack) >= 2:
                stack[-1], stack[-2] = stack[-2], stack[-1]
        elif token in "+-*/%":
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append((a + b) % MOD)
                elif token == '-':
                    stack.append((a - b) % MOD)
                elif token == '*':
                    stack.append((a * b) % MOD)
                elif token == '/':
                    stack.append((a // b) % MOD if b != 0 else 0)
                elif token == '%':
                    stack.append((a % b) % MOD if b != 0 else 0)
    
    return str(stack[-1] if stack else 0)

def solve_stk012(input_lines):
    """STK-012: Infix to postfix"""
    expr = input_lines[0]
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
    stack = []
    output = []
    
    tokens = expr.split()
    for token in tokens:
        if token.isdigit() or token.isalpha():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:
                stack.pop()
        elif token in precedence:
            while (stack and stack[-1] != '(' and 
                   stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
    
    return ' '.join(output)

def solve_stk013(input_lines):
    """STK-013: Max rectangle with boost"""
    n, boost = map(int, input_lines[0].split())
    heights = list(map(int, input_lines[1].split()))
    
    max_area = 0
    
    # Try boosting each bar
    for boost_idx in range(n):
        # Try different boost amounts
        for b in range(boost + 1):
            temp_heights = heights[:]
            temp_heights[boost_idx] += b
            
            # Calculate max rectangle
            for i in range(n):
                min_h = float('inf')
                for j in range(i, n):
                    min_h = min(min_h, temp_heights[j])
                    area = min_h * (j - i + 1)
                    max_area = max(max_area, area)
    
    return str(max_area)

def solve_stk014(input_lines):
    """STK-014: Validate time windows"""
    n = int(input_lines[0])
    intervals = []
    for i in range(1, n + 1):
        start, end = map(int, input_lines[i].split())
        intervals.append((start, end))
    
    stack = []
    for start, end in intervals:
        # Remove intervals that have ended
        while stack and stack[-1][1] < start:
            stack.pop()
        
        # Check if current interval is valid
        if stack and start < stack[-1][1] and end > stack[-1][1]:
            return "INVALID"
        
        stack.append((start, end))
    
    return "VALID"

def solve_stk015(input_lines):
    """STK-015: Min removals for decreasing sequence"""
    n = int(input_lines[0])
    arr = list(map(int, input_lines[1].split()))
    
    # Find longest strictly decreasing subsequence
    tails = []
    for num in arr:
        pos = bisect_left(tails, -num)
        if pos == len(tails):
            tails.append(-num)
        else:
            tails[pos] = -num
    
    return str(n - len(tails))

def solve_stk016(input_lines):
    """STK-016: Stock span with reset"""
    m = int(input_lines[0])
    prices = []
    results = []
    
    for i in range(1, m + 1):
        parts = input_lines[i].split()
        if parts[0] == "PRICE":
            price = int(parts[1])
            prices.append(price)
            
            # Calculate span
            span = 1
            j = len(prices) - 2
            while j >= 0 and prices[j] <= price:
                span += 1
                j -= 1
            
            results.append(str(span))
        elif parts[0] == "RESET":
            prices = []
    
    return '\n'.join(results) if results else ""

# ============================================================================
# Test Case Verification
# ============================================================================

def parse_yaml_file(filepath):
    """Parse YAML test case file."""
    with open(filepath, 'r') as f:
        content = f.read()
    return yaml.safe_load(content)

def verify_problem(problem_id, testcases):
    """Verify all test cases for a problem."""
    stats = {'total': 0, 'passed': 0, 'failed': 0, 'errors': []}
    
    solver_map = {
        'STK-001': solve_stk001,
        'STK-002': solve_stk002,
        'STK-003': solve_stk003,
        'STK-004': solve_stk004,
        'STK-005': solve_stk005,
        'STK-006': solve_stk006,
        'STK-007': solve_stk007,
        'STK-008': solve_stk008,
        'STK-009': solve_stk009,
        'STK-010': solve_stk010,
        'STK-011': solve_stk011,
        'STK-012': solve_stk012,
        'STK-013': solve_stk013,
        'STK-014': solve_stk014,
        'STK-015': solve_stk015,
        'STK-016': solve_stk016
    }
    
    solve_func = solver_map.get(problem_id)
    if not solve_func:
        return stats
    
    for section in ['samples', 'public', 'hidden']:
        if section not in testcases:
            continue
        
        for idx, case in enumerate(testcases[section]):
            stats['total'] += 1
            input_lines = case['input'].strip().split('\n')
            expected_output = case['output'].strip()
            
            try:
                actual = solve_func(input_lines).strip()
                
                if actual == expected_output:
                    stats['passed'] += 1
                else:
                    stats['failed'] += 1
                    stats['errors'].append({
                        'section': section,
                        'index': idx,
                        'expected': expected_output,
                        'actual': actual
                    })
            
            except Exception as e:
                stats['failed'] += 1
                stats['errors'].append({
                    'section': section,
                    'index': idx,
                    'error': str(e)
                })
    
    return stats

def main():
    """Main verification function."""
    print("=" * 80)
    print("STACKS TEST CASE VERIFICATION - ALL PROBLEMS")
    print("=" * 80)
    print()
    
    testcases_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Stacks/testcases"
    
    problems = [
        ('STK-001', 'notebook-undo-simulator'),
        ('STK-002', 'lab-mixed-bracket-repair'),
        ('STK-003', 'conveyor-weighted-deduplication'),
        ('STK-004', 'rooftop-sunset-count'),
        ('STK-005', 'workshop-next-taller-width'),
        ('STK-006', 'assembly-previous-greater-parity'),
        ('STK-007', 'trading-desk-threshold-jump'),
        ('STK-008', 'canteen-token-climb-span'),
        ('STK-009', 'lab-sliding-min-stack'),
        ('STK-010', 'stadium-max-tracker'),
        ('STK-011', 'circuit-postfix-variables'),
        ('STK-012', 'campus-expression-optimizer'),
        ('STK-013', 'auditorium-histogram-one-booster'),
        ('STK-014', 'shuttle-validation-time-windows'),
        ('STK-015', 'bike-repair-plates'),
        ('STK-016', 'assembly-line-span-reset')
    ]
    
    total_stats = {'total': 0, 'passed': 0, 'failed': 0}
    problem_results = []
    
    for problem_id, problem_name in problems:
        filepath = os.path.join(testcases_dir, f"{problem_id}-{problem_name}.yaml")
        
        if not os.path.exists(filepath):
            print(f"{RED}✗ {problem_id}: File not found{RESET}")
            continue
        
        testcases = parse_yaml_file(filepath)
        stats = verify_problem(problem_id, testcases)
        
        total_stats['total'] += stats['total']
        total_stats['passed'] += stats['passed']
        total_stats['failed'] += stats['failed']
        
        pass_rate = (stats['passed'] / stats['total'] * 100) if stats['total'] > 0 else 0
        
        status = GREEN + '✓' if stats['failed'] == 0 else RED + '✗'
        print(f"{status} {problem_id}: {stats['passed']}/{stats['total']} passed ({pass_rate:.1f}%){RESET}")
        
        problem_results.append({
            'id': problem_id,
            'stats': stats,
            'pass_rate': pass_rate
        })
        
        # Show first few errors for debugging
        if stats['errors'] and len(stats['errors']) <= 5:
            for err in stats['errors'][:3]:
                print(f"  {YELLOW}Error in {err.get('section', 'unknown')}[{err.get('index', '?')}]{RESET}")
                if 'error' in err:
                    print(f"    Exception: {err['error']}")
    
    print()
    print("=" * 80)
    overall_rate = (total_stats['passed'] / total_stats['total'] * 100) if total_stats['total'] > 0 else 0
    
    if total_stats['failed'] == 0:
        print(f"{GREEN}✅ ALL TESTS PASSED: {total_stats['passed']}/{total_stats['total']} ({overall_rate:.1f}%){RESET}")
    else:
        print(f"{YELLOW}RESULTS: {total_stats['passed']}/{total_stats['total']} passed ({overall_rate:.1f}%){RESET}")
        print(f"{RED}Failed: {total_stats['failed']} test cases{RESET}")
    
    print("=" * 80)
    
    return total_stats['failed'] == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
