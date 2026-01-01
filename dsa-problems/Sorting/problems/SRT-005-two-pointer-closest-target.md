---
problem_id: SRT_TWO_POINTER_CLOSEST_TARGET__2651
display_id: SRT-005
slug: two-pointer-closest-target
title: "Two-Pointer Sum Closest to Target"
difficulty: Easy
difficulty_score: 28
topics:
  - Sorting
  - Two Pointers
  - Searching
tags:
  - two-pointers
  - sorted-array
  - search
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-005: Two-Pointer Sum Closest to Target

## Problem Statement

You are given a sorted array and a target value. Find the pair of values whose sum is closest to the target.

If there are multiple valid pairs with the same distance to the target, return the pair with the smaller first value.

![Problem Illustration](../images/SRT-005/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (sorted ascending)
- Third line: integer `target`

## Output Format

- Two integers: the pair values in increasing order

## Constraints

- `2 <= n <= 200000`
- `-10^9 <= a[i], target <= 10^9`

## Example

**Input:**

```
4
1 4 6 8
10
```

**Output:**

```
4 6
```

**Explanation:**

The sum 4 + 6 = 10 exactly matches the target.

![Example Visualization](../images/SRT-005/example-1.png)

## Notes

- Use a two-pointer scan from both ends
- Track the closest difference seen so far
- If equal differences occur, pick the smaller first value
- Time complexity: O(n)

## Related Topics

Two Pointers, Sorted Array, Searching

---

## Solution Template
### Java


### Python


### C++


### JavaScript

