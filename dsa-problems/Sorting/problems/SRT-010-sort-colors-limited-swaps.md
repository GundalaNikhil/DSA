---
problem_id: SRT_SORT_COLORS_LIMITED_SWAPS__4762
display_id: SRT-010
slug: sort-colors-limited-swaps
title: "Sort Colors With Limited Swaps"
difficulty: Medium
difficulty_score: 57
topics:
  - Sorting
  - Greedy
  - Adjacent Swaps
tags:
  - greedy
  - adjacent-swaps
  - sorting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-010: Sort Colors With Limited Swaps

## Problem Statement

You are given an array of 0s, 1s, and 2s. You may swap only adjacent elements and perform at most `S` swaps. Determine whether the array can be fully sorted with at most `S` adjacent swaps.

![Problem Illustration](../images/SRT-010/problem-illustration.png)

## Input Format

- First line: integers `n` and `S`
- Second line: `n` space-separated integers (each is 0, 1, or 2)

## Output Format

- Single line: YES if the array can be fully sorted with at most `S` adjacent swaps, NO otherwise

## Constraints

- `1 <= n <= 200000`
- `0 <= S <= 10^9`
- Values are only 0, 1, or 2

## Example

**Input:**

```
8 2
2 1 0 0 0 2 0 2
```

**Output:**

```
YES
```

**Explanation:**

The array `[2,1,0,0,0,2,0,2]` can be fully sorted with at most 2 adjacent swaps.

![Example Visualization](../images/SRT-010/example-1.png)

## Notes

- Greedily move smaller values left while swaps remain
- Adjacent swaps act like limited bubble steps
- Track remaining swaps to avoid exceeding `S`
- Time complexity should be near O(n)

## Related Topics

Greedy, Adjacent Swaps, Sorting

---

## Solution Template
### Java


### Python


### C++


### JavaScript

