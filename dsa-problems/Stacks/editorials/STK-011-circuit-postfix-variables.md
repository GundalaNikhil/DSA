---
title: Circuit Postfix Evaluator with Variables
slug: circuit-postfix-variables
difficulty: Medium
difficulty_score: 55
tags:
- Stack
- Postfix Evaluation
- Parsing
problem_id: STK_CIRCUIT_POSTFIX_VARIABLES__7493
display_id: STK-011
topics:
- Stack
- Expression Evaluation
- Parsing
---
# Circuit Postfix Evaluator with Variables - Editorial

## Problem Summary

Evaluate a postfix expression (Reverse Polish Notation) containing:
-   Integers and Variables (single letters).
-   Operators: `+`, `-`, `*`, `/`, `%`.
-   Stack Operations: `DUP` (duplicate top), `SWAP` (swap top two).
-   All calculations are modulo `10^9 + 7`.
-   Division uses "integer division after modulo normalization".
-   If `a` and `b` are normalized to `[0, MOD-1]`, then `a/b` is just `floor(a/b)`.


## Constraints

- `1 <= t <= 10000`
- `0 <= m <= 26`
- Variable values fit in 64-bit signed integer
## Real-World Scenario

Imagine you are designing a **Programmable Circuit Controller**.
-   The controller receives instructions in a compact "stack-based" bytecode (like Java Bytecode or PostScript).
-   Variables represent sensor inputs (e.g., `t` for temperature, `p` for pressure).
-   The instructions tell the controller how to combine these inputs to calculate a control signal.
-   `DUP` and `SWAP` allow efficient data manipulation without re-reading sensors.

## Problem Exploration

### 1. Postfix Evaluation
-   Standard algorithm: Iterate through tokens.
-   If operand (number/variable): Push to stack.
-   If operator: Pop required operands, compute, push result.
-   This works perfectly for `+ - * / %`.

### 2. Variables
-   We are given a map of variable values.
-   When we encounter a variable token (e.g., "x"), we look up its value and push that.

### 3. Stack Operations
-   `DUP`: Pop `x`, push `x`, push `x`. (Or just `peek` and push).
-   `SWAP`: Pop `a`, pop `b`, push `a`, push `b`.

### 4. Modulo Arithmetic
-   `MOD = 1000000007`.
-   Addition: `(a + b) % MOD`.
-   Subtraction: `(a - b + MOD) % MOD`. (Crucial to handle negative results).
-   Multiplication: `(a * b) % MOD`.
-   Modulo: `a % b`. (Since inputs are normalized, this is just `a % b`. But `b` could be 0? Problem assumes valid expression).
-   Division: "integer division after modulo normalization".
    -   This likely means: `val1 = stack.pop()`, `val2 = stack.pop()`.
    -   `res = (val2 % MOD) / (val1 % MOD)`.
    -   Since we store values already modulo'd, it's just `val2 / val1`.
    -   Note: In standard modular arithmetic fields, division is `val2 * modInverse(val1)`. But the problem explicitly says "integer division". This is a specific rule for this problem.

## Approaches

### Approach 1: Stack Simulation
-   Use a stack of `long` (64-bit integers) to prevent overflow before modulo.
-   Iterate tokens.
-   Handle each type.
-   Complexity: `O(T)` time, `O(T)` space.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `x 5 + y *`, `x=3, y=2`

1.  `x`: Push `3`. Stack `[3]`.
2.  `5`: Push `5`. Stack `[3, 5]`.
3.  `+`: Pop `5`, `3`. `3 + 5 = 8`. Push `8`. Stack `[8]`.
4.  `y`: Push `2`. Stack `[8, 2]`.
5.  `*`: Pop `2`, `8`. `8 * 2 = 16`. Push `16`. Stack `[16]`.

**Result:** `16`.

## Proof of Correctness

-   **Postfix Property**: Postfix expressions are unambiguously evaluated using a stack.
-   **Modulo Operations**: Applying modulo at each step (except division, as specified) keeps numbers within range and satisfies the problem constraints.
-   **Stack Ops**: `DUP` and `SWAP` are correctly implemented as stack manipulations.

## Interview Extensions

1.  **Infix to Postfix**: Convert `(x + 5) * y` to postfix first.
    -   *Hint*: Shunting Yard Algorithm.
2.  **Error Handling**: What if division by zero?
    -   *Hint*: Check `b == 0` before dividing.

### Common Mistakes

-   **Negative Modulo**: `(a - b) % MOD` can be negative in C++/Java. Use `(a - b + MOD) % MOD`.
-   **Division**: Using modular inverse when "integer division" is requested.
-   **Variable Lookup**: Forgetting to check the map for variables.
