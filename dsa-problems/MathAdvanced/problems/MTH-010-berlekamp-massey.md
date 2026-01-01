---
problem_id: MTH_BERLEKAMP_MASSEY__5628
display_id: MTH-010
slug: berlekamp-massey
title: "Berlekamp-Massey Sequence Reconstruction"
difficulty: Hard
difficulty_score: 80
topics:
  - MathAdvanced
  - Berlekamp-Massey
tags:
  - math-advanced
  - berlekamp-massey
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-010: Berlekamp-Massey Sequence Reconstruction

## Problem Statement

Given the first 2k terms of a linearly recurrent sequence, use the Berlekamp-Massey algorithm to find the minimal recurrence relation and compute the nth term.

![Problem Illustration](../images/MTH-010/problem-illustration.png)

## Input Format

- Line 1: Two integers `m` (number of terms given) and `n` (target term)
- Line 2: m space-separated integers representing the sequence
- Line 3: An integer `MOD` (prime modulus)

## Output Format

A single integer representing the nth term of the sequence modulo MOD.

## Constraints

- `1 <= m <= 4000`
- `0 <= n <= 10^18`
- `0 <= sequence[i] < MOD`
- MOD is prime

## Example

**Input:**
```
6 10
1 1 2 3 5 8
1000000007
```

**Output:**
```
89
```

**Explanation:**

Sequence: 1, 1, 2, 3, 5, 8 (Fibonacci)

Berlekamp-Massey finds: a_n = a_{n-1} + a_{n-2}

Continuing: 13, 21, 34, 55, 89
a_10 = 89

![Example Visualization](../images/MTH-010/example-1.png)

## Notes

- Berlekamp-Massey finds minimal linear recurrence
- Works with partial sequence information
- Use matrix exponentiation for large n
- Time complexity: O(m²) for algorithm, O(k³ log n) for term
- Applications in cryptography and coding theory

## Related Topics

berlekamp-massey, linear-recurrence, sequence-reconstruction

---

## Solution Template

### Java


### Python


### C++


### JavaScript

