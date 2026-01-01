---
problem_id: MTH_LARGEST_EIGENVALUE_POWER__2197
display_id: MTH-014
slug: largest-eigenvalue-power
title: "Largest Eigenvalue Power Method"
difficulty: Medium
difficulty_score: 58
topics:
  - MathAdvanced
  - Largest
tags:
  - math-advanced
  - eigenvalue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-014: Largest Eigenvalue Power Method

## Problem Statement

Approximate the largest eigenvalue (by absolute value) of a real matrix using the power iteration method. Continue until convergence within a specified tolerance.

![Problem Illustration](../images/MTH-014/problem-illustration.png)

## Input Format

- Line 1: Two integers `n` (matrix size) and `maxIter` (maximum iterations)
- Next n lines: n space-separated real numbers representing each row of the matrix
- Last line: A real number `epsilon` (convergence tolerance)

## Output Format

A single real number representing the approximate largest eigenvalue (6 decimal places).

## Constraints

- `1 <= n <= 500`
- `1 <= maxIter <= 10000`
- `10^-10 <= epsilon <= 10^-3`
- Matrix entries in range [-1000, 1000]

## Example

**Input:**
```
2 1000
2.0 0.0
0.0 1.0
0.000001
```

**Output:**
```
2.000000
```

**Explanation:**

Matrix:
[2  0]
[0  1]

Eigenvalues: 2 and 1
Largest eigenvalue: 2

Power method converges to 2.000000

![Example Visualization](../images/MTH-014/example-1.png)

## Notes

- Power method: v_{k+1} = A × v_k / ||A × v_k||
- Eigenvalue λ ≈ v^T × A × v
- Converges to largest eigenvalue by magnitude
- Convergence rate depends on eigenvalue gap
- May not converge if multiple eigenvalues have same magnitude

## Related Topics

eigenvalue, power-method, iterative-algorithm

---

## Solution Template

### Java


### Python


### C++


### JavaScript

