---
problem_id: MTH_LAGRANGE_INTERPOLATION_MOD__3542
display_id: MTH-005
slug: lagrange-interpolation-mod
title: "Lagrange Interpolation Mod Prime"
difficulty: Medium
difficulty_score: 60
topics:
  - MathAdvanced
  - Lagrange
tags:
  - math-advanced
  - lagrange-interpolation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-005: Lagrange Interpolation Mod Prime

## Problem Statement

Given k points (x_i, y_i) with distinct x_i values, find the value of the unique interpolating polynomial of degree at most k-1 at a query point X, all modulo a prime.

![Problem Illustration](../images/MTH-005/problem-illustration.png)

## Input Format

- Line 1: Two integers `k` (number of points) and `X` (query point)
- Line 2: An integer `MOD` (prime modulus)
- Next k lines: Two integers `x_i` and `y_i` representing each point

## Output Format

A single integer representing P(X) modulo MOD, where P is the interpolating polynomial.

## Constraints

- `1 <= k <= 200000`
- `0 <= x_i, y_i, X < MOD`
- All x_i are distinct
- MOD is prime (typically 10^9 + 7)

## Example

**Input:**
```
2 2
1000000007
0 1
1 3
```

**Output:**
```
5
```

**Explanation:**

Points: (0, 1) and (1, 3)

The interpolating polynomial through these points is:
P(x) = 1 + 2x

P(2) = 1 + 2(2) = 5

![Example Visualization](../images/MTH-005/example-1.png)

## Notes

- Use Lagrange interpolation formula
- Compute products efficiently
- Handle modular arithmetic carefully
- Time complexity: O(k²) naive, O(k log k) with FFT optimization
- Requires modular inverse computation

## Related Topics

lagrange-interpolation, modular-arithmetic, polynomial

---

## Solution Template

### Java


### Python


### C++


### JavaScript

