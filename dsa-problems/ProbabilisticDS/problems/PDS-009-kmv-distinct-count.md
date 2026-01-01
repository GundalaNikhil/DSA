---
problem_id: PDS_KMV_DISTINCT_COUNT__9186
display_id: PDS-009
slug: kmv-distinct-count
title: "k-Minimum Values (KMV) Distinct Count"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - KMV
  - Distinct Count
tags:
  - probabilistic-ds
  - kmv
  - distinct-count
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-009: k-Minimum Values (KMV) Distinct Count

## Problem Statement

You are given the `k` smallest hash values in (0,1) for a set. Estimate the number of distinct elements using:

```
Estimate = (k - 1) / h_k
```

where `h_k` is the k-th smallest hash value.

![Problem Illustration](../images/PDS-009/problem-illustration.png)

## Input Format

- First line: integer `k`
- Second line: `k` floating-point numbers in ascending order

## Output Format

- Single floating-point number: estimated distinct count

## Constraints

- `2 <= k <= 100000`
- `0 < h_k < 1`

## Example

**Input:**

```
3
0.1 0.2 0.4
```

**Output:**

```
5.0
```

**Explanation:**

Estimate = (3-1) / 0.4 = 5.

![Example Visualization](../images/PDS-009/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

KMV, Sketches, Distinct Counting

---

## Solution Template

### Java


### Python


### C++


### JavaScript

