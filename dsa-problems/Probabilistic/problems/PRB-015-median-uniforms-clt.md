---
problem_id: PRB_MEDIAN_UNIFORMS_CLT__3524
display_id: PRB-015
slug: median-uniforms-clt
title: "Median of Uniforms CLT"
difficulty: Medium
difficulty_score: 50
topics:
  - Probability
  - Statistics
  - CLT
tags:
  - probability
  - clt
  - median
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-015: Median of Uniforms CLT

## Problem Statement

Let `n` i.i.d. random variables be uniformly distributed on [0,1]. Using the CLT approximation for the sample median, output the approximate mean and variance of the median.

For uniform distribution, the asymptotic variance is:

```
Var(median) ≈ 1 / (4n)
```

and the mean is 0.5.

![Problem Illustration](../images/PRB-015/problem-illustration.png)

## Input Format

- Single line: integer `n`

## Output Format

- Two floating-point numbers: mean and variance

## Constraints

- `1 <= n <= 1000`

## Example

**Input:**

```
5
```

**Output:**

```
0.500000 0.050000
```

**Explanation:**

Var ≈ 1/(4*5) = 0.05.

![Example Visualization](../images/PRB-015/example-1.png)

## Notes

- This is an approximation for large n
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

CLT, Order Statistics, Probability

---

## Solution Template

### Java


### Python


### C++


### JavaScript

