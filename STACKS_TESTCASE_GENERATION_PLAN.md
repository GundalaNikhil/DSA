# Stacks Module: Test Case Regeneration Plan

## Overview
This document outlines the strategy for regenerating test cases for all 16 Stacks problems (STK-001 to STK-016) after fixing the solution algorithms.

**Goal**: Create robust test suites with:
- 3 sample test cases (basic + simple + edge)
- 5-7 public test cases
- 25-30 hidden test cases (mix of edge, corner, and constraint-based)
- Total: ~38 test cases per problem

---

## Test Case Categories

### 1. **Sample Cases (3 cases)**
- **Basic**: Simplest valid input that demonstrates the core functionality
- **Simple**: Slightly more complex but still straightforward
- **Edge**: First edge case that might be tricky

### 2. **Public Cases (5-7 cases)**
- Variations of common patterns
- Moderate complexity
- Should be solvable by understanding the basics

### 3. **Hidden Cases (25-30 cases)**
- Edge cases (minimum/maximum input sizes, empty, single element)
- Corner cases (all same values, alternating patterns, etc.)
- Constraint-based (hitting problem constraints)
- Boundary testing

---

## Problem-Specific Test Case Guidelines

### **STK-001: Notebook Undo Simulator**
**Operation-based; Stack fundamentals**
- Basic: PUSH, TOP on single element
- Simple: Mix of PUSH, POP, TOP
- Edges: Empty stack operations, multiple same values
- Constraints: m up to 100,000; large value ranges
- Generation: Random operations with controlled probability of each type

### **STK-002: Bracket Repair**
**Bracket matching with wildcards; Count changes needed**
- Basic: Already balanced string `()()`
- Simple: One mismatched pair `([)]`
- Edges: All same type `{{{`, all wildcards `???`
- Constraints: String up to 100,000; all bracket types
- Generation: Build from valid strings, then introduce mismatches

### **STK-003: Conveyor Weighted Deduplication**
**Stack + weights; Even sum removal**
- Basic: Single pair with even weight
- Simple: Multiple pairs, selective removal
- Edges: All same character, no removal, all removed
- Constraints: n up to 100,000; weights up to 10^9
- Generation: Create character+weight pairs; control sums

### **STK-004: Rooftop Sunset Count**
**Monotonic stack; Find visible buildings**
- Basic: Increasing heights
- Simple: Decreasing, then one tall building
- Edges: All same height, single building
- Constraints: n up to 200,000; heights up to 10^9
- Generation: Build specific patterns (increasing, decreasing, valley, peak)

### **STK-005: Workshop Next Taller**
**NGE with distance constraint**
- Basic: All increasing within width
- Simple: Taller element exists but outside width
- Edges: No taller element, exact width boundary
- Constraints: n up to 100,000; w varies
- Generation: Place target elements at specific distances

### **STK-006: Assembly Previous Greater**
**Previous greater with parity constraint**
- Basic: Simple increasing/decreasing patterns
- Simple: Mixed with parity changes
- Edges: All even/all odd, alternating
- Constraints: Large n; value ranges
- Generation: Control parity while varying values

### **STK-007-008**: Complex Stack Operations
**Monotonic stack patterns; Spans, thresholds**
- Similar approach: basic patterns → edge cases → boundary conditions

### **STK-009**: Sliding Min Stack
**Range minimum queries with push/pop**
- Basic: Simple operations maintaining minimum
- Edges: All same values, single element queries
- Constraints: Operations up to 100,000

### **STK-010**: Stadium Max Tracker
**Auxiliary max stack**
- Basic: Simple PUSH/POP maintaining max
- Similar structure to STK-001

### **STK-011-012**: Expression Evaluation
**Postfix/Infix evaluation; Variable handling**
- Basic: Simple two-operand expressions
- Edges: Division by boundaries, operator precedence
- Constraints: Expression complexity, variable ranges

### **STK-013**: Histogram with Booster
**Largest rectangle + optimization**
- Basic: Simple histogram pattern
- Edges: Increasing/decreasing sequences
- Constraints: Large heights, small/large boosts

### **STK-014**: Shuttle Validation
**Stack simulation with time/priority constraints**
- Basic: Simple push/pop in order
- Edges: Boundary time windows, priority violations
- Constraints: Time/priority interactions

### **STK-015**: Bike Repair Plates
**Stack simulation; Reveal unsafe plates**
- Basic: Simple height sequence revealing unsafe
- Edges: All increasing/all decreasing
- Constraints: Large plate counts, large diameters

### **STK-016**: Assembly Line Span Reset
**Stock span with reset condition**
- Similar to STK-004/008: Span tracking with reset

---

## Test Case Generation Strategy

### Phase 1: Validate Fixed Solutions
```python
# For each problem:
1. Create 2-3 manual test cases (basic + simple)
2. Run against fixed solution
3. Verify output correctness
4. Document expected outputs
```

### Phase 2: Generate Edge Cases
```python
# For each problem type:
1. Identify edge case categories (empty, single, max size, etc.)
2. Generate test cases for each category
3. Run against solution
4. Include in edge test set
```

### Phase 3: Generate Public Test Cases
```python
# 5-7 test cases covering:
1. Common patterns
2. Moderate complexity
3. Variations on sample cases
4. One to two edge cases
```

### Phase 4: Generate Hidden Test Cases
```python
# 25-30 test cases:
1. Randomized within constraints (40% of total)
2. Boundary condition tests (20%)
3. Complex edge cases (20%)
4. Stress tests (near max constraints) (20%)
```

---

## YAML Test Case Format

```yaml
problem_id: STK_EXAMPLE__1234
samples:
- input: |-
    <sample-1-input>
  output: |-
    <sample-1-output>
- input: |-
    <sample-2-input>
  output: |-
    <sample-2-output>
- input: |-
    <sample-3-input>
  output: |-
    <sample-3-output>
public:
- input: |-
    <public-1-input>
  output: |-
    <public-1-output>
# ... 4-6 more public cases
hidden:
- input: |-
    <hidden-1-input>
  output: |-
    <hidden-1-output>
# ... 24-29 more hidden cases
```

---

## Python Helper Script Template

```python
#!/usr/bin/env python3
import subprocess
import yaml
import random

class StackTestGenerator:
    def __init__(self, problem_id, solution_path):
        self.problem_id = problem_id
        self.solution_path = solution_path
        self.cases = {'samples': [], 'public': [], 'hidden': []}

    def generate_test_case(self, input_data):
        """Run solution and capture output"""
        result = subprocess.run(
            ['python3', self.solution_path],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip()

    def add_case(self, category, input_data):
        """Add test case and get expected output"""
        output = self.generate_test_case(input_data)
        self.cases[category].append({
            'input': input_data,
            'output': output
        })
        return output

    def save_yaml(self, output_file):
        """Save test cases to YAML"""
        yaml_data = {'problem_id': self.problem_id}
        for category in ['samples', 'public', 'hidden']:
            yaml_data[category] = [
                {'input': f"|- \\n{c['input']}", 'output': f"|- \\n{c['output']}"}
                for c in self.cases[category]
            ]

        with open(output_file, 'w') as f:
            yaml.dump(yaml_data, f, default_flow_style=False)

# Example usage for STK-001:
if __name__ == "__main__":
    gen = StackTestGenerator(
        'STK_NOTEBOOK_UNDO_SIMULATOR__4827',
        '/path/to/STK-001-notebook-undo-simulator.py'
    )

    # Sample cases
    gen.add_case('samples', '1\\nPUSH 5\\n')
    gen.add_case('samples', '3\\nPUSH 1\\nPOP\\nTOP\\n')

    # Public cases
    for i in range(5):
        # Generate random operations
        ops = generate_random_operations()
        gen.add_case('public', ops)

    # Hidden cases
    for i in range(30):
        ops = generate_random_operations(more_complex=True)
        gen.add_case('hidden', ops)

    gen.save_yaml('output.yaml')
```

---

## Execution Order

1. **STK-001**: Simplest - test script generation
2. **STK-004, STK-010, STK-016**: Monotonic stack patterns
3. **STK-003, STK-015**: Weight/element tracking
4. **STK-002, STK-005, STK-006, STK-007, STK-008**: Bracket/Next/Previous patterns
5. **STK-009**: Range queries
6. **STK-011, STK-012**: Expression evaluation
7. **STK-013, STK-014**: Complex multi-constraint

---

## Validation Checklist

For each problem:
- [ ] All sample test cases produce correct output
- [ ] Public test cases cover diverse patterns
- [ ] Hidden test cases include boundary conditions
- [ ] Total test count: ~38 tests
- [ ] YAML format is valid
- [ ] Solution runs within time limits
- [ ] Edge case coverage documented

---

## Next Steps

1. Create test generator script for each problem type
2. Generate test cases in parallel (samples → public → hidden)
3. Validate all test cases against fixed solutions
4. Commit regenerated test case YAML files
5. Verify 100% accuracy on all tests
