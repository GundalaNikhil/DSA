---
problem_id: PDS_CUCKOO_HASHING_SUCCESS__7392
display_id: PDS-003
slug: cuckoo-hashing-success
title: "Cuckoo Hashing Success Probability"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - Hashing
  - Random Graphs
tags:
  - probabilistic-ds
  - cuckoo-hashing
  - probability
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-003: Cuckoo Hashing Success Probability

## Problem Statement

Use the following approximation for the failure probability of cuckoo hashing with two hash functions:

```
P_fail = exp(-((1 - alpha)^2 * m) / 2)
```

where `alpha` is the load factor and `m` is the table size. Compute the success probability:

```
P_success = 1 - P_fail
```

![Problem Illustration](../images/PDS-003/problem-illustration.png)

## Input Format

- Single line: integer `m` and real `alpha`

## Output Format

- Single floating-point number: `P_success`

## Constraints

- `1 <= m <= 10^6`
- `0 < alpha < 1`

## Example

**Input:**

```
50 0.8
```

**Output:**

```
0.632121
```

**Explanation:**

P_fail = exp(-1) = 0.367879, so P_success = 0.632121.

![Example Visualization](../images/PDS-003/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Cuckoo Hashing, Randomized Analysis

---

## Solution Template

### Java


### Python


### C++


### JavaScript

