---
problem_id: MTH_INVERSE_POLYNOMIAL__7264
display_id: MTH-003
slug: inverse-polynomial
title: "Inverse Polynomial Mod x^n"
difficulty: Hard
difficulty_score: 72
topics:
  - MathAdvanced
  - Polynomial
  - Newton Iteration
tags:
  - math-advanced
  - polynomial-inverse
  - newton-method
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-003: Inverse Polynomial Mod x^n

## Problem Statement

Given a polynomial P(x) with P[0] ≠ 0 modulo a prime number, compute the inverse polynomial Q(x) such that P(x) × Q(x) ≡ 1 (mod x^n) under the given modulus.

The inverse polynomial Q(x) satisfies the property that when multiplied with P(x) and taken modulo x^n, the result is 1.

Use Newton iteration method with NTT for efficient computation.

![Problem Illustration](../images/MTH-003/problem-illustration.png)

## Input Format

- Line 1: Two integers `k` (number of coefficients of P) and `n` (the modulus degree)
- Line 2: `k` space-separated integers representing coefficients of P(x) from lowest to highest degree
- Line 3: An integer `MOD` (the prime modulus, typically 998244353)

## Output Format

A single line containing `n` space-separated integers representing the first `n` coefficients of Q(x) modulo MOD.

## Constraints

- `1 <= k <= 100000`
- `1 <= n <= 100000`
- `P[0] ≠ 0 (mod MOD)`
- `MOD` is a prime number (typically 998244353)
- `0 <= P[i] < MOD`

## Example

**Input:**

```
2 3
1 1
998244353
```

**Output:**

```
1 998244352 1
```

**Explanation:**

P(x) = 1 + x (coefficients [1, 1])
We need Q(x) such that P(x) × Q(x) ≡ 1 (mod x^3)

Q(x) = 1 - x + x² (coefficients [1, -1, 1])

Verification:
(1 + x)(1 - x + x²) = 1 - x + x² + x - x² + x³
= 1 + x³
≡ 1 (mod x^3)

Since -1 ≡ 998244352 (mod 998244353), the output is [1, 998244352, 1].

![Example Visualization](../images/MTH-003/example-1.png)

## Notes

- Newton iteration formula: Q\_{i+1}(x) = Q_i(x) × (2 - P(x) × Q_i(x)) mod x^{2^i}
- Start with Q_0(x) = P[0]^{-1} (modular inverse of first coefficient)
- Double the precision at each iteration
- Time complexity: O(n log n) using NTT
- Requires modular inverse computation and polynomial multiplication

## Related Topics

Newton Iteration, Polynomial Inverse, NTT, Modular Arithmetic, Divide and Conquer

---

## Solution Template

### Java


### Python


### C++


### JavaScript

