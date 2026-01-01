---
problem_id: MTH_MATRIX_EXP_LINEAR_RECURRENCE__6283
display_id: MTH-007
slug: matrix-exp-linear-recurrence
title: "Matrix Exponentiation for Linear Recurrence"
difficulty: Medium
difficulty_score: 58
topics:
  - MathAdvanced
  - Matrix
tags:
  - math-advanced
  - matrix-exponentiation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-007: Matrix Exponentiation for Linear Recurrence

## Problem Statement

Given a linear recurrence relation of order k with coefficients and initial terms, compute the nth term modulo a prime using matrix exponentiation.

![Problem Illustration](../images/MTH-007/problem-illustration.png)

## Input Format

- Line 1: Three integers `k` (recurrence order), `n` (target term), and `MOD` (modulus)
- Line 2: k space-separated integers representing recurrence coefficients c_0 to c_{k-1}
- Line 3: k space-separated integers representing initial terms a_0 to a_{k-1}

## Output Format

A single integer representing the nth term of the sequence modulo MOD.

## Constraints

- `1 <= k <= 50`
- `0 <= n <= 10^18`
- `0 <= c_i, a_i < MOD`
- MOD is prime (typically 10^9 + 7)

## Example

**Input:**
```
2 5 1000000007
1 1
0 1
```

**Output:**
```
5
```

**Explanation:**

Fibonacci sequence: a_n = a_{n-1} + a_{n-2}
Coefficients: [1, 1]
Initial: [0, 1]

Sequence: 0, 1, 1, 2, 3, 5, ...
a_5 = 5

![Example Visualization](../images/MTH-007/example-1.png)

## Notes

- Build k×k transition matrix
- Use fast matrix exponentiation: O(k³ log n)
- Handles very large n efficiently
- Common for Fibonacci-like sequences
- Can solve any linear recurrence

## Related Topics

matrix-exponentiation, linear-recurrence, fast-exponentiation

---

## Solution Template

### Java


### Python


### C++


### JavaScript

