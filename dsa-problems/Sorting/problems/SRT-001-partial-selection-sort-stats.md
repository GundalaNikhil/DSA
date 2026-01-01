---
problem_id: SRT_PARTIAL_SELECTION_SORT_STATS__6835
display_id: SRT-001
slug: partial-selection-sort-stats
title: "Partial Selection Sort Stats"
difficulty: Easy
difficulty_score: 24
topics:
  - Sorting
  - Simulation
  - Arrays
tags:
  - sorting
  - selection-sort
  - simulation
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-001: Partial Selection Sort Stats

## Problem Statement

Given an array, simulate only the first `k` iterations of selection sort. In iteration `i`, find the minimum element in the subarray `a[i..n-1]` and swap it with `a[i]`.

Return the array state after exactly `k` iterations.

![Problem Illustration](../images/SRT-001/problem-illustration.png)

## Input Format

- First line: integers `n` and `k`
- Second line: `n` space-separated integers

## Output Format

- Single line: array after `k` iterations, space-separated

## Constraints

- `1 <= n <= 100000`
- `0 <= k <= n-1`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
4 2
4 3 1 2
```

**Output:**

```
1 2 4 3
```

**Explanation:**

Iteration 0 swaps 1 to the front, iteration 1 swaps 2 into position 1.

![Example Visualization](../images/SRT-001/example-1.png)

## Notes

- If `k = 0`, the array is unchanged
- Use an index of the minimum in the remaining suffix
- Time complexity: O(k * n)
- Space complexity: O(1)

## Related Topics

Selection Sort, Simulation, Arrays

---

## Solution Template
### Java


### Python


### C++


### JavaScript

