---
problem_id: MTH_FWHT_XOR_CONVOLUTION__7451
display_id: MTH-008
slug: fwht-xor-convolution
title: "Fast Walsh-Hadamard Transform (XOR Convolution)"
difficulty: Medium
difficulty_score: 62
topics:
  - MathAdvanced
  - Fast
tags:
  - math-advanced
  - fwht
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-008: Fast Walsh-Hadamard Transform (XOR Convolution)

## Problem Statement

Given two arrays A and B of length 2^k, compute their XOR convolution using the Fast Walsh-Hadamard Transform (FWHT). The XOR convolution C is defined as: C[i⊕j] += A[i] × B[j].

![Problem Illustration](../images/MTH-008/problem-illustration.png)

## Input Format

- Line 1: An integer `k` (arrays have length 2^k)
- Line 2: 2^k space-separated integers representing array A
- Line 3: 2^k space-separated integers representing array B

## Output Format

A single line containing 2^k space-separated integers representing the XOR convolution modulo 10^9+7.

## Constraints

- `0 <= k <= 17`
- `0 <= A[i], B[i] <= 10^9`
- Array length is power of 2
- Output modulo 10^9 + 7

## Example

**Input:**
```
1
1 2
3 4
```

**Output:**
```
11 10
```

**Explanation:**

A = [1, 2], B = [3, 4]

XOR convolution:
- C[0⊕0] = A[0]*B[0] + A[1]*B[1] = 1*3 + 2*4 = 11
- C[0⊕1] = A[0]*B[1] + A[1]*B[0] = 1*4 + 2*3 = 10

Result: [11, 10]

![Example Visualization](../images/MTH-008/example-1.png)

## Notes

- FWHT is similar to FFT but for XOR operation
- Transform, pointwise multiply, inverse transform
- Time complexity: O(n log n) where n = 2^k
- Applications in subset sum problems
- Different from standard convolution

## Related Topics

fwht, xor-convolution, walsh-hadamard

---

## Solution Template

### Java


### Python


### C++


### JavaScript

