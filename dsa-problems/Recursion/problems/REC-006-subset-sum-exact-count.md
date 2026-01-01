---
problem_id: REC_SUBSET_SUM_EXACT_COUNT__1854
display_id: REC-006
slug: subset-sum-exact-count
title: "Subset Sum Exact Count"
difficulty: Medium
difficulty_score: 43
topics:
  - Recursion
  - Backtracking
  - Subset Sum
tags:
  - recursion
  - subset-sum
  - backtracking
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-006: Subset Sum Exact Count

## Problem Statement

Given an array `arr`, determine whether there exists a subset of exactly `k` elements that sums to `target`. Return one such subset if it exists, otherwise output `NONE`.

![Problem Illustration](../images/REC-006/problem-illustration.png)

## Input Format

- First line: integers `n`, `k`, and `target`
- Second line: `n` space-separated integers `arr[i]`

## Output Format

- One line with a valid subset (space-separated), or `NONE` if no solution exists

## Constraints

- `1 <= n <= 20`
- `0 <= k <= n`
- `|arr[i]| <= 10000`
- `|target| <= 10^9`

## Example

**Input:**

```
4 2 7
4 1 6 2
```

**Output:**

```
1 6
```

**Explanation:**

The subset `{1, 6}` uses exactly two elements and sums to 7.

![Example Visualization](../images/REC-006/example-1.png)

## Notes

- Use recursion to choose or skip each element
- Track how many elements have been chosen
- Prune when remaining elements are insufficient to reach `k`
- Any valid subset is acceptable

## Related Topics

Backtracking, Subset Sum, Pruning

---

## Solution Template
### Java


### Python


### C++


### JavaScript

