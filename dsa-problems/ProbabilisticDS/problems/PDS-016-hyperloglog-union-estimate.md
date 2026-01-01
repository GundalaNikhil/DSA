---
problem_id: PDS_PROBLEM_16__7318
display_id: PDS-016
slug: hyperloglog-union-estimate
title: "HyperLogLog Union Estimate"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - HyperLogLog
  - Cardinality Estimation
tags:
  - probabilistic-ds
  - hyperloglog
  - union
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-016: HyperLogLog Union Estimate

## Problem Statement

Given two HyperLogLog sketches with the same number of registers `m`, compute the union estimate by taking register-wise maximums and then applying the HLL estimate:

```
E = alpha_m * m^2 / sum(2^{-register[i]})
```

Use `alpha_m` as:

- 0.673 if m = 16
- 0.697 if m = 32
- 0.709 if m = 64
- otherwise: 0.7213 / (1 + 1.079 / m)

Ignore small-range corrections.

![Problem Illustration](../images/PDS-016/problem-illustration.png)

## Input Format

- First line: integer `m`
- Second line: `m` integers (registers for sketch A)
- Third line: `m` integers (registers for sketch B)

## Output Format

- Single floating-point number: union cardinality estimate

## Constraints

- `m` is a power of two, `16 <= m <= 65536`
- `0 <= register[i] <= 64`

## Example

**Input:**

```
16
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
```

**Output:**

```
43.072000
```

**Explanation:**

Union registers are all 2. The estimate is 43.072.

![Example Visualization](../images/PDS-016/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(m)

## Related Topics

HyperLogLog, Sketch Union

---

## Solution Template

### Java


### Python


### C++


### JavaScript

