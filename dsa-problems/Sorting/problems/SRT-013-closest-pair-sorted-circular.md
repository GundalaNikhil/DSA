---
problem_id: SRT_CLOSEST_PAIR_SORTED_CIRCULAR__3817
display_id: SRT-013
slug: closest-pair-sorted-circular
title: "Closest Pair in Sorted Circular Array"
difficulty: Medium
difficulty_score: 49
topics:
  - Sorting
  - Two Pointers
  - Circular Arrays
tags:
  - two-pointers
  - circular
  - search
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-013: Closest Pair in Sorted Circular Array

## Problem Statement

You are given a sorted circular array (a sorted array rotated at an unknown pivot) and a target. Find a pair of values whose sum is closest to the target.

If multiple pairs tie, return any one. Output the pair values.

![Problem Illustration](../images/SRT-013/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (rotated sorted array)
- Third line: integer `target`

## Output Format

- Two integers: the chosen pair values

## Constraints

- `2 <= n <= 200000`
- `-10^9 <= a[i], target <= 10^9`

## Example

**Input:**

```
5
4 5 1 2 3
7
```

**Output:**

```
4 3
```

**Explanation:**

The pair (4,3) sums to 7 exactly.

![Example Visualization](../images/SRT-013/example-1.png)

## Notes

- Find the pivot (smallest element) to set two pointers
- Use a circular two-pointer technique
- Stop after one full cycle
- Time complexity: O(n)

## Related Topics

Two Pointers, Circular Arrays, Searching

---

## Solution Template
### Java


### Python


### C++


### JavaScript

