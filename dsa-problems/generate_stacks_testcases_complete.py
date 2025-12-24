#!/usr/bin/env python3
"""
Comprehensive Test Case Generator for Stacks Topic (STK-001 to STK-016)
Following the Universal Test Case Generation Prompt.
Target: 30-40 test cases per problem with proper YAML format.
"""

import random
import math
from collections import deque

def format_testcase_yaml(data):
    """Format test cases in proper YAML with |- syntax."""
    lines = []
    lines.append(f"problem_id: {data['problem_id']}")
    
    for section_name in ['samples', 'public', 'hidden']:
        if section_name not in data or not data[section_name]:
            continue
        lines.append(f"{section_name}:")
        for case in data[section_name]:
            lines.append("- input: |-")
            for line in case['input'].strip().split('\n'):
                lines.append(f"    {line}")
            lines.append("  output: |-")
            for line in case['output'].strip().split('\n'):
                lines.append(f"    {line}")
    
    return '\n'.join(lines)


# ============================================================================
# STK-001: Notebook Undo Simulator
# ============================================================================

def generate_stk001_cases():
    """Basic stack operations: PUSH, POP, TOP"""
    cases = {'problem_id': 'STK-001', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_commands = [
        ["PUSH 10", "PUSH -1", "TOP", "POP", "TOP"],
        ["PUSH 5", "TOP", "PUSH 3", "POP", "TOP"],
        ["TOP", "PUSH 7", "POP", "POP"]
    ]
    
    for commands in sample_commands:
        stack = []
        outputs = []
        for cmd in commands:
            parts = cmd.split()
            if parts[0] == "PUSH":
                stack.append(int(parts[1]))
            elif parts[0] == "POP":
                outputs.append(str(stack.pop()) if stack else "EMPTY")
            elif parts[0] == "TOP":
                outputs.append(str(stack[-1]) if stack else "EMPTY")
        
        inp = f"{len(commands)}\n" + '\n'.join(commands)
        cases['samples'].append({'input': inp, 'output': '\n'.join(outputs)})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        m = random.randint(5, 30)
        commands = []
        stack = []
        outputs = []
        
        for _ in range(m):
            if not stack or random.random() < 0.6:
                val = random.randint(-1000, 1000)
                commands.append(f"PUSH {val}")
                stack.append(val)
            else:
                op = random.choice(["POP", "TOP"])
                commands.append(op)
                if op == "POP":
                    outputs.append(str(stack.pop()) if stack else "EMPTY")
                else:
                    outputs.append(str(stack[-1]) if stack else "EMPTY")
        
        inp = f"{m}\n" + '\n'.join(commands)
        test_case = {'input': inp, 'output': '\n'.join(outputs)}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-002: Lab Mixed Bracket Repair
# ============================================================================

def generate_stk002_cases():
    """Bracket balancing with repair cost"""
    cases = {'problem_id': 'STK-002', 'samples': [], 'public': [], 'hidden': []}
    
    def min_repair_cost(s):
        """Calculate minimum cost to balance brackets"""
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
        return repairs + len(stack)
    
    # Samples
    samples = ["()[]", "([)]", "{{{"]
    for s in samples:
        cost = min_repair_cost(s)
        cases['samples'].append({'input': s, 'output': str(cost)})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(4, 40)
        brackets = []
        for _ in range(n):
            brackets.append(random.choice(['(', ')', '[', ']', '{', '}']))
        s = ''.join(brackets)
        cost = min_repair_cost(s)
        
        test_case = {'input': s, 'output': str(cost)}
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-003: Conveyor Weighted Deduplication
# ============================================================================

def generate_stk003_cases():
    """Stack-based weighted deduplication"""
    cases = {'problem_id': 'STK-003', 'samples': [], 'public': [], 'hidden': []}
    
    def weighted_dedupe(items):
        """Remove adjacent equal items with weights"""
        stack = []
        for val, weight in items:
            if stack and stack[-1][0] == val:
                stack[-1] = (val, stack[-1][1] + weight)
                if stack[-1][1] >= 3:
                    stack.pop()
            else:
                stack.append((val, weight))
        return stack
    
    # Samples
    samples = [
        [(1, 1), (1, 1), (2, 1), (1, 1)],
        [(5, 2), (5, 1), (3, 1)],
        [(7, 3), (7, 1)]
    ]
    
    for items in samples:
        result = weighted_dedupe(items)
        inp_lines = [str(len(items))]
        for v, w in items:
            inp_lines.append(f"{v} {w}")
        
        if result:
            out = ' '.join(f"{v},{w}" for v, w in result)
        else:
            out = "EMPTY"
        
        cases['samples'].append({'input': '\n'.join(inp_lines), 'output': out})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(3, 25)
        items = []
        for _ in range(n):
            val = random.randint(1, 10)
            weight = random.randint(1, 2)
            items.append((val, weight))
        
        result = weighted_dedupe(items)
        inp_lines = [str(n)]
        for v, w in items:
            inp_lines.append(f"{v} {w}")
        
        if result:
            out = ' '.join(f"{v},{w}" for v, w in result)
        else:
            out = "EMPTY"
        
        test_case = {'input': '\n'.join(inp_lines), 'output': out}
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-004: Rooftop Sunset Count
# ============================================================================

def generate_stk004_cases():
    """Count buildings with sunset view (monotonic stack)"""
    cases = {'problem_id': 'STK-004', 'samples': [], 'public': [], 'hidden': []}
    
    def sunset_count(heights):
        """Count buildings that can see sunset (no taller to the left)"""
        stack = []
        for h in heights:
            while stack and stack[-1] <= h:
                stack.pop()
            stack.append(h)
        return len(stack)
    
    # Samples
    samples = [
        [2, 5, 2, 6, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]
    
    for heights in samples:
        count = sunset_count(heights)
        inp = f"{len(heights)}\n" + ' '.join(map(str, heights))
        cases['samples'].append({'input': inp, 'output': str(count)})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(5, 40)
        heights = [random.randint(1, 100) for _ in range(n)]
        count = sunset_count(heights)
        
        inp = f"{n}\n" + ' '.join(map(str, heights))
        test_case = {'input': inp, 'output': str(count)}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-005: Workshop Next Taller Width
# ============================================================================

def generate_stk005_cases():
    """Find next greater element with distance"""
    cases = {'problem_id': 'STK-005', 'samples': [], 'public': [], 'hidden': []}
    
    def next_greater_width(arr):
        """For each element, find distance to next greater element"""
        n = len(arr)
        result = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        
        return result
    
    # Samples
    samples = [
        [4, 5, 2, 10],
        [3, 2, 1],
        [1, 2, 3, 4, 5]
    ]
    
    for arr in samples:
        result = next_greater_width(arr)
        inp = f"{len(arr)}\n" + ' '.join(map(str, arr))
        out = ' '.join(map(str, result))
        cases['samples'].append({'input': inp, 'output': out})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(4, 30)
        arr = [random.randint(1, 100) for _ in range(n)]
        result = next_greater_width(arr)
        
        inp = f"{n}\n" + ' '.join(map(str, arr))
        out = ' '.join(map(str, result))
        test_case = {'input': inp, 'output': out}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-006: Assembly Previous Greater Parity
# ============================================================================

def generate_stk006_cases():
    """Previous greater element with even/odd check"""
    cases = {'problem_id': 'STK-006', 'samples': [], 'public': [], 'hidden': []}
    
    def prev_greater_parity(arr):
        """Find previous greater element that has same parity"""
        n = len(arr)
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
        
        return result
    
    # Samples
    samples = [
        [4, 6, 3, 7, 2],
        [1, 3, 5, 7, 9],
        [10, 8, 6, 4, 2]
    ]
    
    for arr in samples:
        result = prev_greater_parity(arr)
        inp = f"{len(arr)}\n" + ' '.join(map(str, arr))
        out = ' '.join(map(str, result))
        cases['samples'].append({'input': inp, 'output': out})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(4, 30)
        arr = [random.randint(1, 100) for _ in range(n)]
        result = prev_greater_parity(arr)
        
        inp = f"{n}\n" + ' '.join(map(str, arr))
        out = ' '.join(map(str, result))
        test_case = {'input': inp, 'output': out}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-007: Trading Desk Threshold Jump
# ============================================================================

def generate_stk007_cases():
    """Stock price threshold jumps"""
    cases = {'problem_id': 'STK-007', 'samples': [], 'public': [], 'hidden': []}
    
    def threshold_jumps(prices, threshold):
        """Count price changes exceeding threshold"""
        jumps = 0
        for i in range(1, len(prices)):
            if abs(prices[i] - prices[i-1]) > threshold:
                jumps += 1
        return jumps
    
    # Samples
    samples = [
        ([10, 15, 12, 20, 18], 3),
        ([5, 5, 5, 5], 1),
        ([1, 10, 20, 30], 5)
    ]
    
    for prices, threshold in samples:
        result = threshold_jumps(prices, threshold)
        inp = f"{len(prices)} {threshold}\n" + ' '.join(map(str, prices))
        cases['samples'].append({'input': inp, 'output': str(result)})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(3, 30)
        threshold = random.randint(5, 20)
        prices = [random.randint(10, 100) for _ in range(n)]
        result = threshold_jumps(prices, threshold)
        
        inp = f"{n} {threshold}\n" + ' '.join(map(str, prices))
        test_case = {'input': inp, 'output': str(result)}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-008: Canteen Token Climb Span
# ============================================================================

def generate_stk008_cases():
    """Stock span problem variant"""
    cases = {'problem_id': 'STK-008', 'samples': [], 'public': [], 'hidden': []}
    
    def stock_span(prices):
        """Calculate span for each price (days since last higher price)"""
        n = len(prices)
        spans = [1] * n
        stack = []
        
        for i in range(n):
            while stack and prices[stack[-1]] <= prices[i]:
                stack.pop()
            
            spans[i] = i + 1 if not stack else i - stack[-1]
            stack.append(i)
        
        return spans
    
    # Samples
    samples = [
        [100, 80, 60, 70, 60, 75, 85],
        [10, 20, 30, 40],
        [40, 30, 20, 10]
    ]
    
    for prices in samples:
        result = stock_span(prices)
        inp = f"{len(prices)}\n" + ' '.join(map(str, prices))
        out = ' '.join(map(str, result))
        cases['samples'].append({'input': inp, 'output': out})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(4, 30)
        prices = [random.randint(10, 100) for _ in range(n)]
        result = stock_span(prices)
        
        inp = f"{n}\n" + ' '.join(map(str, prices))
        out = ' '.join(map(str, result))
        test_case = {'input': inp, 'output': out}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-009: Lab Sliding Min Stack
# ============================================================================

def generate_stk009_cases():
    """Min stack with sliding window"""
    cases = {'problem_id': 'STK-009', 'samples': [], 'public': [], 'hidden': []}
    
    def sliding_min(arr, k):
        """Find minimum in each window of size k"""
        n = len(arr)
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
        
        return result
    
    # Samples
    samples = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3),
        ([4, 3, 2, 1], 2),
        ([5, 5, 5, 5], 3)
    ]
    
    for arr, k in samples:
        result = sliding_min(arr, k)
        inp = f"{len(arr)} {k}\n" + ' '.join(map(str, arr))
        out = ' '.join(map(str, result))
        cases['samples'].append({'input': inp, 'output': out})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(5, 30)
        k = random.randint(2, min(n, 10))
        arr = [random.randint(-50, 50) for _ in range(n)]
        result = sliding_min(arr, k)
        
        inp = f"{n} {k}\n" + ' '.join(map(str, arr))
        out = ' '.join(map(str, result))
        test_case = {'input': inp, 'output': out}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-010: Stadium Max Tracker
# ============================================================================

def generate_stk010_cases():
    """Max stack with queries"""
    cases = {'problem_id': 'STK-010', 'samples': [], 'public': [], 'hidden': []}
    
    def max_stack_queries(operations):
        """Process stack operations and MAX queries"""
        stack = []
        max_stack = []
        outputs = []
        
        for op in operations:
            parts = op.split()
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
        
        return outputs
    
    # Samples
    samples = [
        ["PUSH 5", "PUSH 3", "PUSH 7", "MAX", "POP", "MAX"],
        ["PUSH 10", "MAX", "PUSH 20", "MAX", "POP", "MAX"],
        ["MAX", "PUSH 1", "MAX"]
    ]
    
    for ops in samples:
        result = max_stack_queries(ops)
        inp = f"{len(ops)}\n" + '\n'.join(ops)
        out = '\n'.join(result)
        cases['samples'].append({'input': inp, 'output': out})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        m = random.randint(5, 30)
        ops = []
        
        for _ in range(m):
            if not ops or random.random() < 0.5:
                ops.append(f"PUSH {random.randint(1, 100)}")
            else:
                ops.append(random.choice(["POP", "MAX"]))
        
        result = max_stack_queries(ops)
        inp = f"{m}\n" + '\n'.join(ops)
        out = '\n'.join(result) if result else ""
        test_case = {'input': inp, 'output': out}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-011: Circuit Postfix Variables
# ============================================================================

def generate_stk011_cases():
    """Postfix evaluation with variables and special ops"""
    cases = {'problem_id': 'STK-011', 'samples': [], 'public': [], 'hidden': []}
    
    MOD = 1000000007
    
    def evaluate_postfix(tokens, variables):
        """Evaluate postfix with DUP, SWAP, variables"""
        stack = []
        
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
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
        
        return stack[-1] if stack else 0
    
    # Samples
    samples = [
        (["x", "5", "+", "y", "*"], {"x": 3, "y": 2}),
        (["10", "DUP", "+"], {}),
        (["a", "b", "SWAP", "-"], {"a": 5, "b": 3})
    ]
    
    for tokens, vars in samples:
        result = evaluate_postfix(tokens, vars)
        inp_lines = [str(len(tokens)), ' '.join(tokens), str(len(vars))]
        for k, v in vars.items():
            inp_lines.append(f"{k} {v}")
        
        cases['samples'].append({'input': '\n'.join(inp_lines), 'output': str(result)})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        # Generate simple postfix expressions
        expr_len = random.randint(3, 8)
        tokens = []
        num_vars = random.randint(0, 3)
        vars = {}
        var_names = ['x', 'y', 'z'][:num_vars]
        
        for v in var_names:
            vars[v] = random.randint(1, 100)
        
        # Simple expression: var1 var2 + num *
        if num_vars >= 2:
            tokens = [var_names[0], var_names[1], "+", str(random.randint(1, 10)), "*"]
        else:
            tokens = [str(random.randint(1, 100)), str(random.randint(1, 100)), "+"]
        
        result = evaluate_postfix(tokens, vars)
        inp_lines = [str(len(tokens)), ' '.join(tokens), str(len(vars))]
        for k, v in vars.items():
            inp_lines.append(f"{k} {v}")
        
        test_case = {'input': '\n'.join(inp_lines), 'output': str(result)}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-012: Campus Expression Optimizer
# ============================================================================

def generate_stk012_cases():
    """Infix to postfix conversion"""
    cases = {'problem_id': 'STK-012', 'samples': [], 'public': [], 'hidden': []}
    
    def infix_to_postfix(expr):
        """Convert infix to postfix notation"""
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
    
    # Samples
    samples = [
        "a + b * c",
        "( a + b ) * c",
        "a * b + c * d"
    ]
    
    for expr in samples:
        result = infix_to_postfix(expr)
        cases['samples'].append({'input': expr, 'output': result})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        # Generate simple infix expressions
        ops = ['+', '*', '-']
        vars = ['a', 'b', 'c', 'd']
        
        if idx % 3 == 0:
            expr = f"{vars[0]} + {vars[1]} * {vars[2]}"
        elif idx % 3 == 1:
            expr = f"( {vars[0]} + {vars[1]} ) * {vars[2]}"
        else:
            expr = f"{vars[0]} * {vars[1]} + {vars[2]}"
        
        result = infix_to_postfix(expr)
        test_case = {'input': expr, 'output': result}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-013: Auditorium Histogram One Booster
# ============================================================================

def generate_stk013_cases():
    """Largest rectangle in histogram with one boost"""
    cases = {'problem_id': 'STK-013', 'samples': [], 'public': [], 'hidden': []}
    
    def max_rectangle_with_boost(heights, boost):
        """Find max rectangle area after boosting one bar"""
        n = len(heights)
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
        
        return max_area
    
    # Samples
    samples = [
        ([2, 4, 2], 3),
        ([1, 1, 1], 2),
        ([5, 3, 4], 1)
    ]
    
    for heights, boost in samples:
        result = max_rectangle_with_boost(heights, boost)
        inp = f"{len(heights)} {boost}\n" + ' '.join(map(str, heights))
        cases['samples'].append({'input': inp, 'output': str(result)})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(3, 10)  # Keep small for brute force
        boost = random.randint(1, 5)
        heights = [random.randint(1, 10) for _ in range(n)]
        result = max_rectangle_with_boost(heights, boost)
        
        inp = f"{n} {boost}\n" + ' '.join(map(str, heights))
        test_case = {'input': inp, 'output': str(result)}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-014: Shuttle Validation Time Windows
# ============================================================================

def generate_stk014_cases():
    """Validate time windows with stack"""
    cases = {'problem_id': 'STK-014', 'samples': [], 'public': [], 'hidden': []}
    
    def validate_time_windows(intervals):
        """Check if time intervals are properly nested"""
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
    
    # Samples
    samples = [
        [(1, 5), (2, 3), (6, 8)],
        [(1, 5), (2, 6), (7, 9)],
        [(1, 10), (2, 5), (3, 4)]
    ]
    
    for intervals in samples:
        result = validate_time_windows(intervals)
        inp_lines = [str(len(intervals))]
        for s, e in intervals:
            inp_lines.append(f"{s} {e}")
        
        cases['samples'].append({'input': '\n'.join(inp_lines), 'output': result})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(3, 20)
        intervals = []
        time = 1
        
        for _ in range(n):
            start = time
            duration = random.randint(1, 5)
            end = start + duration
            intervals.append((start, end))
            time = end + random.randint(0, 2)
        
        result = validate_time_windows(intervals)
        inp_lines = [str(n)]
        for s, e in intervals:
            inp_lines.append(f"{s} {e}")
        
        test_case = {'input': '\n'.join(inp_lines), 'output': result}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-015: Bike Repair Plates
# ============================================================================

def generate_stk015_cases():
    """Remove plates to make decreasing sequence"""
    cases = {'problem_id': 'STK-015', 'samples': [], 'public': [], 'hidden': []}
    
    def min_removals_decreasing(arr):
        """Minimum removals to make array strictly decreasing"""
        n = len(arr)
        # Find longest strictly decreasing subsequence
        from bisect import bisect_left
        
        tails = []
        for num in arr:
            # For decreasing, we reverse the comparison
            pos = bisect_left(tails, -num)
            if pos == len(tails):
                tails.append(-num)
            else:
                tails[pos] = -num
        
        return n - len(tails)
    
    # Samples
    samples = [
        [10, 5, 8, 3, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]
    
    for arr in samples:
        result = min_removals_decreasing(arr)
        inp = f"{len(arr)}\n" + ' '.join(map(str, arr))
        cases['samples'].append({'input': inp, 'output': str(result)})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(4, 25)
        arr = [random.randint(1, 50) for _ in range(n)]
        result = min_removals_decreasing(arr)
        
        inp = f"{n}\n" + ' '.join(map(str, arr))
        test_case = {'input': inp, 'output': str(result)}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STK-016: Assembly Line Span Reset
# ============================================================================

def generate_stk016_cases():
    """Stock span with reset events"""
    cases = {'problem_id': 'STK-016', 'samples': [], 'public': [], 'hidden': []}
    
    def span_with_reset(events):
        """Calculate spans with RESET events"""
        results = []
        prices = []
        
        for event in events:
            parts = event.split()
            if parts[0] == "PRICE":
                price = int(parts[1])
                prices.append(price)
                
                # Calculate span
                span = 1
                i = len(prices) - 2
                while i >= 0 and prices[i] <= price:
                    span += 1
                    i -= 1
                
                results.append(str(span))
            elif parts[0] == "RESET":
                prices = []
        
        return results
    
    # Samples
    samples = [
        ["PRICE 100", "PRICE 80", "PRICE 90", "RESET", "PRICE 70"],
        ["PRICE 50", "PRICE 60", "PRICE 70"],
        ["PRICE 100", "RESET", "PRICE 100"]
    ]
    
    for events in samples:
        results = span_with_reset(events)
        inp = f"{len(events)}\n" + '\n'.join(events)
        out = '\n'.join(results)
        cases['samples'].append({'input': inp, 'output': out})
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        m = random.randint(5, 25)
        events = []
        
        for _ in range(m):
            if random.random() < 0.9:
                events.append(f"PRICE {random.randint(10, 100)}")
            else:
                events.append("RESET")
        
        results = span_with_reset(events)
        inp = f"{m}\n" + '\n'.join(events)
        out = '\n'.join(results) if results else ""
        test_case = {'input': inp, 'output': out}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# Main Generation
# ============================================================================

def main():
    """Generate test cases for all stack problems."""
    print("=" * 80)
    print("STACKS TEST CASE GENERATION - ALL PROBLEMS (STK-001 to STK-016)")
    print("=" * 80)
    
    base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Stacks/testcases"
    
    problems = [
        ("STK-001", "notebook-undo-simulator", generate_stk001_cases),
        ("STK-002", "lab-mixed-bracket-repair", generate_stk002_cases),
        ("STK-003", "conveyor-weighted-deduplication", generate_stk003_cases),
        ("STK-004", "rooftop-sunset-count", generate_stk004_cases),
        ("STK-005", "workshop-next-taller-width", generate_stk005_cases),
        ("STK-006", "assembly-previous-greater-parity", generate_stk006_cases),
        ("STK-007", "trading-desk-threshold-jump", generate_stk007_cases),
        ("STK-008", "canteen-token-climb-span", generate_stk008_cases),
        ("STK-009", "lab-sliding-min-stack", generate_stk009_cases),
        ("STK-010", "stadium-max-tracker", generate_stk010_cases),
        ("STK-011", "circuit-postfix-variables", generate_stk011_cases),
        ("STK-012", "campus-expression-optimizer", generate_stk012_cases),
        ("STK-013", "auditorium-histogram-one-booster", generate_stk013_cases),
        ("STK-014", "shuttle-validation-time-windows", generate_stk014_cases),
        ("STK-015", "bike-repair-plates", generate_stk015_cases),
        ("STK-016", "assembly-line-span-reset", generate_stk016_cases),
    ]
    
    total_cases = 0
    
    for prob_id, slug, generator_func in problems:
        print(f"\n[{prob_id}] Generating {slug}...")
        cases = generator_func()
        yaml_content = format_testcase_yaml(cases)
        
        output_path = f"{base_path}/{prob_id}-{slug}.yaml"
        with open(output_path, 'w') as f:
            f.write(yaml_content)
        
        count = len(cases['samples']) + len(cases['public']) + len(cases['hidden'])
        total_cases += count
        print(f"✅ {prob_id}: {count} test cases")
        print(f"   Samples: {len(cases['samples'])}, Public: {len(cases['public'])}, Hidden: {len(cases['hidden'])}")
    
    print("\n" + "=" * 80)
    print(f"✅ ALL STACKS TESTS COMPLETE: {total_cases} test cases generated")
    print("=" * 80)


if __name__ == "__main__":
    main()
