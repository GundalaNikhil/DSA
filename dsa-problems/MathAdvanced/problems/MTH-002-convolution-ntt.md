---
problem_id: MTH_CONVOLUTION_NTT__5931
display_id: MTH-002
slug: convolution-ntt
title: "Convolution Mod Prime Using NTT"
difficulty: Medium
difficulty_score: 58
topics:
  - MathAdvanced
  - NTT
  - Convolution
tags:
  - math-advanced
  - ntt
  - number-theoretic-transform
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-002: Convolution Mod Prime Using NTT

## Problem Statement

Given two sequences A and B, compute their convolution using the Number Theoretic Transform (NTT) modulo a prime number 998244353. The convolution C of two sequences is defined as:

C[k] = Σ(i=0 to k) A[i] × B[k-i]

You must pad the sequences to the next power of 2 for efficient NTT computation.

![Problem Illustration](../images/MTH-002/problem-illustration.png)

## Input Format

- Line 1: An integer `n` representing the length of sequence A
- Line 2: `n` space-separated integers representing elements of A
- Line 3: An integer `m` representing the length of sequence B
- Line 4: `m` space-separated integers representing elements of B

## Output Format

A single line containing space-separated integers representing the convolution result modulo 998244353.

## Constraints

- `1 <= n, m <= 100000`
- `0 <= A[i], B[i] <= 998244352`
- The output length will be `n + m - 1`
- All operations must be performed modulo 998244353 (a prime suitable for NTT)

## Example

**Input:**

```
3
1 1 1
2
1 2
```

**Output:**

```
1 3 3 2
```

**Explanation:**

A = [1, 1, 1]
B = [1, 2]

Convolution C:

- C[0] = A[0] × B[0] = 1 × 1 = 1
- C[1] = A[0] × B[1] + A[1] × B[0] = 1 × 2 + 1 × 1 = 3
- C[2] = A[1] × B[1] + A[2] × B[0] = 1 × 2 + 1 × 1 = 3
- C[3] = A[2] × B[1] = 1 × 2 = 2

Result: [1, 3, 3, 2]

![Example Visualization](../images/MTH-002/example-1.png)

## Notes

- NTT (Number Theoretic Transform) is the modular arithmetic version of FFT
- The modulus 998244353 = 119 × 2^23 + 1 is chosen because it's a prime with a primitive root
- NTT allows exact integer arithmetic without floating-point errors
- Padding to power of 2 is essential for divide-and-conquer approach
- Time complexity: O((n+m) log(n+m))

## Related Topics

Number Theoretic Transform, FFT, Modular Arithmetic, Primitive Roots, Convolution

---

## Solution Template

### Java


### Python


### C++


### JavaScript

