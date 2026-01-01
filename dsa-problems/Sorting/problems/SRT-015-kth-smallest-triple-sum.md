---
problem_id: SRT_KTH_SMALLEST_TRIPLE_SUM__7904
display_id: SRT-015
slug: kth-smallest-triple-sum
title: "Kth Smallest Triple Sum"
difficulty: Medium
difficulty_score: 59
topics:
  - Sorting
  - Binary Search
  - Two Pointers
tags:
  - sorting
  - binary-search
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-015: Kth Smallest Triple Sum

## Problem Statement

Given an array `a`, consider all sums `a[i] + a[j] + a[k]` with `i < j < k`. Find the k-th smallest such sum.

![Problem Illustration](../images/SRT-015/problem-illustration.png)

## Input Format

- First line: integers `n` and `k`
- Second line: `n` space-separated integers

## Output Format

- Single integer: the k-th smallest triple sum

## Constraints

- `3 <= n <= 100000`
- `1 <= k <= n*(n-1)*(n-2)/6`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
4 2
1 2 4 7
```

**Output:**

```
10
```

**Explanation:**

Triple sums are 7, 10, 12, 13 in sorted order; the 2nd is 10.

![Example Visualization](../images/SRT-015/example-1.png)

## Notes

- Sort the array first
- Use binary search on the possible sum range
- Count triples with sum <= mid using two pointers
- Time complexity: O(n^2 log R)

## Related Topics

Binary Search, Two Pointers, Sorting

---

## Solution Template
### Java


### Python


### C++


### JavaScript

