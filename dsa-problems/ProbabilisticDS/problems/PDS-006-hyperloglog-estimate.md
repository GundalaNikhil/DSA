---
problem_id: PDS_HYPERLOGLOG_ESTIMATE__1507
display_id: PDS-006
slug: hyperloglog-estimate
title: "HyperLogLog Cardinality Estimate"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - HyperLogLog
  - Cardinality Estimation
tags:
  - probabilistic-ds
  - hyperloglog
  - cardinality
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-006: HyperLogLog Cardinality Estimate

## Problem Statement

Given `m` HyperLogLog registers (m is a power of two) and their maximum values, compute the cardinality estimate:

```
E = alpha_m * m^2 / sum(2^{-register[i]})
```

Use `alpha_m` as:

- 0.673 if m = 16
- 0.697 if m = 32
- 0.709 if m = 64
- otherwise: 0.7213 / (1 + 1.079 / m)

If `E <= 2.5 * m` and there are `V` zero registers, apply linear counting:

```
E = m * ln(m / V)
```

Output `E`.

![Problem Illustration](../images/PDS-006/problem-illustration.png)

## Input Format

- First line: integer `m`
- Second line: `m` integers (register values)

## Output Format

- Single floating-point number: estimated cardinality

## Constraints

- `m` is a power of two, `16 <= m <= 65536`
- `0 <= register[i] <= 64`

## Example

**Input:**

```
16
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
```

**Output:**

```
21.536000
```

**Explanation:**

With all registers equal to 1, the raw estimate is 21.536.

![Example Visualization](../images/PDS-006/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(m)

## Related Topics

HyperLogLog, Cardinality Estimation

---

## Solution Template

### Java


### Python


### C++


### JavaScript

