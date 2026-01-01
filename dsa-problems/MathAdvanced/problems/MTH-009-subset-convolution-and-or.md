---
problem_id: MTH_SUBSET_CONVOLUTION_AND_OR__9174
display_id: MTH-009
slug: subset-convolution-and-or
title: "Subset Convolution (AND/OR)"
difficulty: Hard
difficulty_score: 78
topics:
  - MathAdvanced
  - Subset
tags:
  - math-advanced
  - subset-convolution
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-009: Subset Convolution (AND/OR)

## Problem Statement

Perform subset convolution under bitwise AND or OR operations using zeta and Möbius transforms on the subset lattice.

![Problem Illustration](../images/MTH-009/problem-illustration.png)

## Input Format

- Line 1: Two integers `n` (bit size) and `op` (0 for AND, 1 for OR)
- Line 2: 2^n space-separated integers representing array A
- Line 3: 2^n space-separated integers representing array B

## Output Format

A single line containing 2^n space-separated integers representing the subset convolution modulo 10^9+7.

## Constraints

- `1 <= n <= 20`
- `0 <= A[i], B[i] <= 10^9`
- op = 0 (AND) or 1 (OR)
- Output modulo 10^9 + 7

## Example

**Input:**
```
2 1
1 1 0 0
0 1 1 0
```

**Output:**
```
0 1 1 2
```

**Explanation:**

n=2, so we have 4 subsets: {}, {0}, {1}, {0,1}
A = [1, 1, 0, 0]
B = [0, 1, 1, 0]

OR convolution computes sum over subsets.

![Example Visualization](../images/MTH-009/example-1.png)

## Notes

- Use ranked zeta/Möbius transforms
- Subset convolution: C[S] = Σ(T⊆S) A[T] × B[S\T]
- Time complexity: O(2^n × n²)
- Applications in DP on subsets
- More complex than FWHT

## Related Topics

subset-convolution, zeta-transform, mobius-transform

---

## Solution Template

### Java


### Python


### C++


### JavaScript

