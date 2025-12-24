# Universal Test Case Generation Prompt

**Purpose:** Generate comprehensive, correct test cases for any DSA problem in a single pass.

---

## 🎯 Instructions for AI

You are an expert test case designer. Your task is to generate complete, correct test cases for a DSA problem. Follow these guidelines strictly:

### 1. **Understand the Problem First**

Before generating test cases:

- Read the problem statement carefully
- Identify input format and constraints
- Understand the expected output format exactly
- Note any special edge cases from the problem description

### 2. **Test Case Categories**

Generate test cases in THREE categories:

#### **A. Samples (2-3 test cases)**

- Used in problem description
- Simple, illustrative examples
- Help users understand the problem
- **Must be hand-verified and correct**

#### **B. Public (3-5 test cases)**

- Visible to users for debugging
- Cover basic scenarios:
  - Minimum constraints (n=1, empty arrays, etc.)
  - Simple valid cases
  - One boundary case
- Users can see both input and output

#### **C. Hidden (20-30 test cases)**

- Not visible to users
- Comprehensive coverage:
  - **Edge Cases:** (4-6 test cases)
    - Minimum values (n=1, k=0, empty)
    - Maximum constraints
    - All zeros, all ones
    - Single element
  - **Boundary Cases:** (4-6 test cases)
    - Just below/above limits
    - Powers of 2
    - Prime numbers if relevant
  - **Negative Test Cases:** (3-5 test cases)
    - Invalid/impossible scenarios (e.g., no solution exists)
    - Contradictory constraints
    - Edge case where answer is -1, empty, or "NO"
    - Cases that should return error states
  - **Special Constraint Cases:** (3-5 test cases)
    - Test specific constraints mentioned in problem
    - Cases exploiting constraint boundaries
    - Unique problem-specific scenarios
    - Cases testing algorithm correctness under constraints
  - **Normal Cases:** (4-8 test cases)
    - Small inputs (n=5-10)
    - Medium inputs (n=50-100)
  - **Stress Cases:** (3-4 test cases)
    - Maximum n, maximum values
    - Worst-case time complexity
    - Random large inputs

### 3. **Output Format Requirements**

**CRITICAL:** Match the exact output format specified:

```yaml
# Example format:
samples:
  - input: |-
      5 3
      1 2 3 4 5
    output: |-
      3
      1 2 3
```

**Common Pitfalls to AVOID:**

- ❌ Extra blank lines when output should have none
- ❌ Missing newlines between values
- ❌ Trailing spaces
- ❌ Wrong ordering (when order matters)
- ❌ Inconsistent formatting across languages

**Format Rules:**

- Use `|-` for multi-line strings (preserves newlines)
- Use `>-` for single-line strings (folds newlines)
- NO trailing newlines unless specified
- ONE newline between output values unless specified otherwise
- When there are 0 items, print just "0" (no extra blank line)

### 4. **Verification Steps**

For EVERY test case:

1. **Run the reference solution** (Python/C++/Java)
2. **Verify output format** exactly matches specification
3. **Check edge case behavior**:
   - Empty inputs
   - Single element
   - All same values
   - Maximum constraints
4. **Ensure determinism**: Same input → same output every time

### 5. **Language Consistency**

If generating solutions in multiple languages, ensure:

- **Identical output format** across C++, Java, Python
- **Same whitespace handling**
- **Same ordering** (sorted vs unsorted)
- **Same edge case handling** (empty, -1, etc.)

---

## 📝 Test Case Generation Template

Use this structure when generating test cases:

```yaml
problem_id: [CATEGORY]_[PROBLEM_NAME]__[4_DIGIT_ID]
samples:
  - input: |-
      [sample_input_1]
    output: |-
      [sample_output_1]
  - input: |-
      [sample_input_2]
    output: |-
      [sample_output_2]

public:
  # Edge: Minimum
  - input: |-
      [minimum_constraint_input]
    output: |-
      [expected_output]

  # Edge: Empty/Zero
  - input: |-
      [empty_or_zero_input]
    output: |-
      [expected_output]

  # Basic: Simple case
  - input: |-
      [simple_input]
    output: |-
      [expected_output]

  # Boundary: Just within limits
  - input: |-
      [boundary_input]
    output: |-
      [expected_output]

hidden:
  # Edge Cases (4-6)
  - input: |-
      [edge_case_1]
    output: |-
      [correct_output]
  - input: |-
      [edge_case_2]
    output: |-
      [correct_output]

  # Boundary Cases (4-6)
  - input: |-
      [boundary_case_1]
    output: |-
      [correct_output]
  - input: |-
      [boundary_case_2]
    output: |-
      [correct_output]

  # Negative Cases (3-5) - No solution / Invalid scenarios
  - input: |-
      [impossible_case]
    output: |-
      -1
  - input: |-
      [no_solution_case]
    output: |-
      NO
  - input: |-
      [contradictory_case]
    output: |-
      []  # or empty output as per problem

  # Special Constraint Cases (3-5) - Problem-specific
  - input: |-
      [constraint_test_1]
    output: |-
      [output_testing_specific_constraint]
  - input: |-
      [constraint_test_2]
    output: |-
      [output_exploiting_constraint_boundary]

  # Normal Cases (4-8)
  - input: |-
      [normal_case_1]
    output: |-
      [correct_output]
  - input: |-
      [normal_case_2]
    output: |-
      [correct_output]

  # Stress Cases (3-4)
  - input: |-
      [stress_case_1]
    output: |-
      [correct_output]
```

---

## 🔧 Problem-Specific Checklist

### For Graph Problems:

- ✅ Disconnected components
- ✅ Single node
- ✅ Cycle vs tree
- ✅ Self-loops (if allowed)
- ✅ Maximum edges
- ✅ **Negative:** No path exists
- ✅ **Special:** Exactly at degree/capacity limit

### For Array Problems:

- ✅ Empty array
- ✅ Single element
- ✅ All same values
- ✅ Sorted/reverse sorted
- ✅ Random order
- ✅ **Negative:** No valid subarray/pair
- ✅ **Special:** All negative numbers, mix of +/-

### For Tree Problems:

- ✅ Single node
- ✅ Linear chain
- ✅ Complete binary tree
- ✅ Skewed tree
- ✅ Maximum depth
- ✅ **Negative:** Invalid tree structure query
- ✅ **Special:** All nodes have same value

### For String Problems:

- ✅ Empty string
- ✅ Single character
- ✅ All same characters
- ✅ Maximum length
- ✅ Special characters
- ✅ **Negative:** No pattern match
- ✅ **Special:** Palindrome, repeated patterns

### For Dynamic Programming:

- ✅ Base cases (n=0, n=1)
- ✅ Small inputs for verification
- ✅ Large inputs for stress test
- ✅ Cases hitting memoization
- ✅ **Negative:** Impossible to achieve target
- ✅ **Special:** Optimal solution at boundary

### For Number Theory:

- ✅ n=1
- ✅ Prime numbers
- ✅ Powers of 2
- ✅ Large primes
- ✅ Composite numbers
- ✅ **Negative:** No solution (e.g., gcd impossible)
- ✅ **Special:** Coprime numbers, perfect squares

### For Searching/Sorting:

- ✅ Already sorted
- ✅ Reverse sorted
- ✅ All duplicates
- ✅ **Negative:** Element not found
- ✅ **Special:** Target at first/last position

### For Greedy/Optimization:

- ✅ Minimum cost is 0
- ✅ Maximum benefit impossible
- ✅ **Negative:** No feasible solution
- ✅ **Special:** Multiple optimal solutions

### For Bit Manipulation:

- ✅ All bits 0
- ✅ All bits 1
- ✅ Single bit set
- ✅ **Negative:** No valid bit configuration
- ✅ **Special:** Power of 2, alternating bits

---

## 🎯 Negative Test Cases - CRITICAL

**Purpose:** Test when NO solution exists or invalid/impossible scenarios.

**Why Important:**

- Catches bugs in error handling
- Tests edge case logic
- Ensures solution doesn't hang or crash
- Validates "no answer" scenarios

**Examples by Category:**

### Array/Search Problems:

```yaml
# Two Sum - no pair sums to target
- input: |-
    5 100
    1 2 3 4 5
  output: |-
    -1

# Subarray Sum - impossible sum
- input: |-
    3 1000
    1 2 3
  output: |-
    -1
```

### Graph Problems:

```yaml
# Shortest Path - no path exists
- input: |-
    4 2
    0 1
    2 3
    0 3
  output: |-
    -1

# Cycle Detection - no cycle
- input: |-
    3 2
    0 1
    1 2
  output: |-
    NO
```

### String Problems:

```yaml
# Pattern Match - pattern not found
- input: |-
    hello
    xyz
  output: |-
    -1

# Anagram - cannot form anagram
- input: |-
    abc
    def
  output: |-
    NO
```

### DP/Optimization:

```yaml
# Knapsack - items too heavy
- input: |-
    2 10
    100 200
  output: |-
    0

# Coin Change - cannot make amount
- input: |-
    3 1
    2 5 10
  output: |-
    -1
```

---

## 🔬 Special Constraint Test Cases - CRITICAL

**Purpose:** Test cases specifically designed around problem constraints.

**Why Important:**

- Validates constraint handling
- Tests boundary behavior
- Catches off-by-one errors
- Ensures correctness at limits

**Examples by Constraint Type:**

### Range Constraints:

```yaml
# If constraint: 1 ≤ n ≤ 10^5, 1 ≤ k ≤ n
# Test: k = n (boundary)
- input: |-
    5 5
    1 2 3 4 5
  output: |-
    [all elements selected]

# Test: k = 1 (minimum)
- input: |-
    5 1
    1 2 3 4 5
  output: |-
    [single element]
```

### Value Constraints:

```yaml
# If constraint: -10^9 ≤ a[i] ≤ 10^9
# Test: All negative
- input: |-
    3
    -100 -50 -10
  output: |-
    -10

# Test: Mix of positive/negative
- input: |-
    4
    -5 10 -3 7
  output: |-
    [based on problem logic]

# Test: All zeros
- input: |-
    3
    0 0 0
  output: |-
    0
```

### Structural Constraints:

```yaml
# If constraint: Tree with n-1 edges
# Test: Linear tree (worst case)
- input: |-
    5
    0 1
    1 2
    2 3
    3 4
  output: |-
    [tests depth handling]

# If constraint: Connected graph
# Test: Just connected (n-1 edges)
- input: |-
    4 3
    0 1
    1 2
    2 3
  output: |-
    [minimum connectivity]
```

### Frequency/Count Constraints:

```yaml
# If constraint: Frequency of element ≤ k
# Test: All elements at max frequency k
- input: |-
    6 2
    1 1 2 2 3 3
  output: |-
    [tests max frequency handling]

# If constraint: At most m distinct elements
# Test: Exactly m distinct
- input: |-
    5 3
    1 2 3 1 2
  output: |-
    [tests distinct count limit]
```

### Time/Complexity Constraints:

```yaml
# If constraint: O(n log n) solution required
# Test: n = 10^5 (max) to verify time limit
- input: |-
    100000
    [random array of 100000 elements]
  output: |-
    [verified output]
```

---

## ⚠️ Critical Reminders

1. **VERIFY EVERY OUTPUT** - Don't guess, run the solution!
2. **EXACT FORMAT** - One wrong space/newline = failed test
3. **EDGE CASES FIRST** - These catch most bugs
4. **NEGATIVE CASES ARE MANDATORY** - Every problem must have "no solution" tests
5. **TEST CONSTRAINTS EXPLICITLY** - Create cases that hit each constraint boundary
6. **NO ASSUMPTIONS** - If unsure, ask or generate both variants
7. **CONSISTENCY** - All languages must produce identical output

---

## 📋 Specific Instructions for This Problem

### Problem: [PROBLEM_NAME]

**Category:** [Arrays/Graphs/DP/Trees/etc.]

**Constraints:**

- n: [min] to [max]
- values: [min] to [max]
- [other constraints]

**Output Format:**

```
[Exact format with examples]
```

**Edge Cases to Cover:**

1. [Specific edge case 1]
2. [Specific edge case 2]
3. [Specific edge case 3]

**Negative Cases to Cover:**

1. [No solution exists scenario]
2. [Invalid/impossible input combination]
3. [Contradictory constraints]

**Special Constraint Cases to Cover:**

1. [Test at exact constraint boundary]
2. [Test maximum allowed frequency/count]
3. [Test minimum/maximum value combinations]

**Special Considerations:**

- [Any ordering requirements]
- [Any tie-breaking rules]
- [Any impossible case handling]

---

## 🎯 Output Checklist

Before submitting, verify:

- [ ] All test cases have input and output
- [ ] Output format is EXACTLY as specified
- [ ] At least 2 samples
- [ ] At least 3 public test cases
- [ ] At least 20 hidden test cases (including negative & special)
- [ ] Edge cases covered (min, max, empty, single)
- [ ] **At least 3 negative test cases** (no solution scenarios)
- [ ] **At least 3 special constraint test cases**
- [ ] All outputs verified by running solution
- [ ] No extra blank lines or spaces
- [ ] Consistent formatting across all test cases
- [ ] YAML syntax is valid

---

## Example: Complete Test Case Generation

### Problem: Two Sum

**Given an array of integers and a target, find two indices that sum to target.**

```yaml
problem_id: ARR_TWO_SUM__0001
samples:
  - input: |-
      4 9
      2 7 11 15
    output: |-
      0 1
  - input: |-
      3 6
      3 2 4
    output: |-
      1 2

public:
  - input: |-
      2 5
      2 3
    output: |-
      0 1
  - input: |-
      3 10
      5 5 0
    output: |-
      -1
  - input: |-
      5 15
      1 2 3 4 5
    output: |-
      -1

hidden:
  # Edge: minimum n
  - input: |-
      2 10
      5 5
    output: |-
      0 1

  # Edge: maximum n at boundary
  - input: |-
      100000 1000000000
      [array where two elements sum to target]
    output: |-
      [indices]

  # Boundary: target at array limits
  - input: |-
      3 6
      1 2 3
    output: |-
      1 2

  # Negative: no pair exists
  - input: |-
      3 100
      1 2 3
    output: |-
      -1

  # Negative: single element duplicates but need 2 indices
  - input: |-
      4 10
      5 5 5 5
    output: |-
      0 1

  # Negative: all elements same, target impossible
  - input: |-
      5 15
      1 1 1 1 1
    output: |-
      -1

  # Special Constraint: negative numbers
  - input: |-
      4 0
      -1 2 -2 1
    output: |-
      0 2

  # Special Constraint: target is 0
  - input: |-
      3 0
      -5 0 5
    output: |-
      0 2

  # Special Constraint: all negative
  - input: |-
      3 -10
      -5 -3 -7
    output: |-
      1 2

  # Normal: found at beginning
  - input: |-
      5 3
      1 2 3 4 5
    output: |-
      0 1

  # Normal: found at end
  - input: |-
      5 10
      1 2 3 4 6
    output: |-
      3 4

  # Normal: found in middle
  - input: |-
      7 13
      1 5 3 7 9 2 6
    output: |-
      3 5

  # Stress: large array
  - input: |-
      1000 999
      [1000 numbers where 500 + 499 = 999]
    output: |-
      498 499

  # Stress: maximum values
  - input: |-
      100000 2000000000
      [100000 elements with two summing to target]
    output: |-
      [indices]
```

---

## 🚀 Ready to Generate

With this prompt, you should be able to generate complete, correct test cases for any DSA problem in one pass. Always prioritize:

1. **Correctness** over quantity
2. **Format precision** over approximation
3. **Edge case coverage** over normal cases
4. **Negative cases** - Every problem MUST have "no solution" tests
5. **Special constraint cases** - Test boundaries and limits explicitly
6. **Verification** over assumption

---

## 📊 Test Case Distribution Summary

For a problem with **25-30 total hidden test cases**:

```
📁 Hidden Test Cases (25-30)
├── 🔴 Edge Cases (4-6)
│   ├── Minimum constraints (n=1, empty, zero)
│   ├── Maximum constraints
│   ├── Single element
│   └── All same values
│
├── 🟡 Boundary Cases (4-6)
│   ├── Just below max
│   ├── Just above min
│   ├── Powers of 2
│   └── Prime numbers (if relevant)
│
├── ❌ Negative Cases (3-5) **MANDATORY**
│   ├── No solution exists
│   ├── Impossible target/goal
│   ├── Contradictory constraints
│   └── Invalid configuration
│
├── ⚡ Special Constraint Cases (3-5) **MANDATORY**
│   ├── At exact constraint boundary
│   ├── All negative/positive
│   ├── Frequency at maximum
│   └── Problem-specific edge behavior
│
├── 🟢 Normal Cases (4-8)
│   ├── Small inputs (n=5-10)
│   ├── Medium inputs (n=50-100)
│   ├── Various valid scenarios
│   └── Different orderings
│
└── 💪 Stress Cases (3-4)
    ├── Maximum n
    ├── Maximum values
    ├── Worst-case complexity
    └── Random large inputs
```

---

## ⚠️ CRITICAL: Don't Forget

### ❌ Negative Test Cases (MANDATORY)

Every problem **MUST** include at least 3 test cases where:

- No valid solution exists
- Answer is -1, "NO", "IMPOSSIBLE", or empty
- Tests error handling and edge logic

**Examples:**

- Array: No pair sums to target
- Graph: No path between nodes
- String: Pattern not found
- DP: Cannot achieve target sum
- Tree: Query for non-existent node

### ⚡ Special Constraint Cases (MANDATORY)

Every problem **MUST** include at least 3 test cases that:

- Hit exact constraint boundaries
- Test problem-specific limits
- Validate constraint adherence

**Examples:**

- If `1 ≤ k ≤ n`: Test k=1 and k=n
- If `-10^9 ≤ val ≤ 10^9`: Test all negative, all positive
- If `frequency ≤ k`: Test all elements at frequency k
- If `tree with n-1 edges`: Test linear chain (worst case)

---

## 🎯 Final Reminder

**Remember:** A single incorrect test case can break the entire judging system!

### Before Submitting:

1. ✅ Run reference solution on ALL test cases
2. ✅ Verify output format EXACTLY
3. ✅ Include negative cases (no solution)
4. ✅ Include special constraint cases
5. ✅ Check for trailing spaces/newlines
6. ✅ Validate YAML syntax
7. ✅ Test across all languages (C++, Java, Python)

**Quality > Quantity**: 20 correct, diverse test cases are better than 50 similar ones!
