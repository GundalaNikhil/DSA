---
problem_id: SRT_COUNT_WITHIN_THRESHOLD_AFTER_SELF__7028
display_id: SRT-012
slug: count-within-threshold-after-self
title: "Count Within Threshold After Self"
difficulty: Medium
difficulty_score: 56
topics:
  - Sorting
  - Divide and Conquer
  - Counting
tags:
  - merge-sort
  - counting
  - arrays
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-012: Count Within Threshold After Self

## Problem Statement

For each element `a[i]`, count how many elements to its right satisfy `a[i] - a[j] <= T`.

Return the counts in order.

![Problem Illustration](../images/SRT-012/problem-illustration.png)

## Input Format

- First line: integers `n` and `T`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers, the counts for each index

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`
- `0 <= T <= 10^9`

## Example

**Input:**

```
3 1
4 1 3
```

**Output:**

```
1 1 0
```

**Explanation:**

For 4, elements to the right within threshold are {3}. For 1, elements to the right are {3} because 1 - 3 = -2 <= 1.

![Example Visualization](../images/SRT-012/example-1.png)

## Notes

- Condition `a[i] - a[j] <= T` is equivalent to `a[j] >= a[i] - T`
- Use a modified merge sort to count efficiently
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Merge Sort, Counting, Divide and Conquer

---

## Solution Template
### Java


### Python


### C++


### JavaScript

