---
problem_id: SEG_KTH_ORDER_STAT_PREFIX__7093
display_id: SEG-005
slug: kth-order-stat-prefix
title: "K-th Order Statistic in Prefix"
difficulty: Medium
difficulty_score: 57
topics:
  - Segment Tree
  - Persistent Data Structures
  - Order Statistics
tags:
  - segment-tree
  - persistent
  - kth-statistic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-005: K-th Order Statistic in Prefix

## Problem Statement

Given an array `a`, answer queries of the form `PREFIX r k`: find the k-th smallest value in the prefix `a[0..r]`.

All indices are 0-based. It is guaranteed that `1 <= k <= r+1`.

![Problem Illustration](../images/SEG-005/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `PREFIX r k`

## Output Format

- For each query, output the k-th smallest value

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
4 1
5 1 3 2
PREFIX 3 2
```

**Output:**

```
2
```

**Explanation:**

The prefix is `[5,1,3,2]`, sorted as `[1,2,3,5]`, so the 2nd smallest is 2.

![Example Visualization](../images/SEG-005/example-1.png)

## Notes

- Coordinate-compress values for the segment tree domain
- Build a persistent segment tree for each prefix
- Query the tree to find the k-th smallest
- Time per query: O(log n)

## Related Topics

Persistent Segment Tree, Order Statistics, Prefix Queries

---

## Solution Template
### Java


### Python


### C++


### JavaScript

