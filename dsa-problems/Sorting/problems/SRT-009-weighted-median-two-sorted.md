---
problem_id: SRT_WEIGHTED_MEDIAN_TWO_SORTED__3086
display_id: SRT-009
slug: weighted-median-two-sorted
title: "Weighted Median of Two Sorted Arrays"
difficulty: Medium
difficulty_score: 60
topics:
  - Sorting
  - Binary Search
  - Median
tags:
  - median
  - binary-search
  - sorted-arrays
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-009: Weighted Median of Two Sorted Arrays

## Problem Statement

You are given two sorted arrays `A` and `B` along with positive weights `wA` and `wB`. Treat each element of `A` as appearing `wA` times and each element of `B` as appearing `wB` times.

Return the median of the combined multiset without expanding it.

If the total count is even, return the average of the two middle values as a decimal (e.g., `2.5`).

![Problem Illustration](../images/SRT-009/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Second line: `n` space-separated integers (array `A`)
- Third line: `m` space-separated integers (array `B`)
- Fourth line: integers `wA` and `wB`

## Output Format

- Single number: the weighted median

## Constraints

- `1 <= n, m <= 100000`
- `1 <= wA, wB <= 10^6`
- Arrays are sorted in nondecreasing order

## Example

**Input:**

```
2 2
1 3
2 7
1 2
```

**Output:**

```
2.5
```

**Explanation:**

Expanded multiset is `[1, 3, 2, 2, 7, 7]` -> sorted `[1,2,2,3,7,7]`. Median is average of 3rd and 4th: `(2+3)/2`.

![Example Visualization](../images/SRT-009/example-1.png)

## Notes

- Use binary search on value space or k-th order logic
- Total count is `n*wA + m*wB`
- Keep all arithmetic in 64-bit integers
- Output with `.5` when needed

## Related Topics

Median, Binary Search, Sorted Arrays

---

## Solution Template
### Java


### Python


### C++


### JavaScript

