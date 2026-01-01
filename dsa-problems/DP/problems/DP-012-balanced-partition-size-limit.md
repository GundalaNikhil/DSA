---
problem_id: DP_BAL_PART_SIZE__5120
display_id: DP-012
slug: balanced-partition-size-limit
title: "Balanced Partition With Size Limit"
difficulty: Medium
difficulty_score: 56
topics:
  - Dynamic Programming
  - Subset Sum
  - Optimization
tags:
  - dp
  - subset-sum
  - partition
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-012: Balanced Partition With Size Limit

## Problem Statement

You are given an array `a` of length `n` and an integer `D`. Partition the array into two groups (each element goes to exactly one group) such that:

- The absolute difference of the two group sums is at most `D`.
- Among all such valid partitions, minimize the size of the **larger** group.

Return the minimum possible larger-group size. If no valid partition exists, return `-1`.

![Problem Illustration](../images/DP-012/problem-illustration.png)

## Input Format

- First line: integers `n` and `D`
- Second line: `n` integers `a[i]`

## Output Format

Print one integer: the minimum larger-group size, or `-1` if impossible.

## Constraints

- `1 <= n <= 50`
- `-500 <= a[i] <= 500`
- `0 <= D <= 5000`

## Example

**Input:**
```
4 1
3 1 4 2
```

**Output:**
```
2
```

**Explanation:**

Partition into `{3,2}` and `{1,4}`:

- sums: 5 and 5, difference = 0 ≤ 1
- group sizes: 2 and 2, larger size = 2 (minimum possible)

![Example Visualization](../images/DP-012/example-1.png)

## Notes

- Groups can be empty, but that may be suboptimal. Check constraints carefully.
- Negative values are allowed; sums can be negative.
- We minimize the larger group size, **not** the difference (difference is constrained).

## Related Topics

Dynamic Programming, Subset Sum, Partitioning

---

## Solution Template

### Java


### Python


### C++


### JavaScript


