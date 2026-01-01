---
problem_id: HEP_SLIDING_WINDOW_KTH_SMALLEST__2665
display_id: HEP-007
slug: sliding-window-kth-smallest
title: "Sliding Window Kth Smallest"
difficulty: Medium
difficulty_score: 58
topics:
  - Heaps
  - Sliding Window
  - Order Statistics
tags:
  - heaps
  - sliding-window
  - order-statistics
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-007: Sliding Window Kth Smallest

## Problem Statement

Given an array `arr` of length `n`, a window size `w`, and an integer `k`, output the `k`-th smallest element in every contiguous window of size `w`.

![Problem Illustration](../images/HEP-007/problem-illustration.png)

## Input Format

- First line: integers `n`, `w`, and `k`
- Second line: `n` space-separated integers

## Output Format

- `n - w + 1` integers: the `k`-th smallest value for each window

## Constraints

- `1 <= n <= 200000`
- `1 <= w <= n`
- `1 <= k <= w`
- `-10^9 <= arr[i] <= 10^9`

## Example

**Input:**

```
5 3 2
1 3 2 6 4
```

**Output:**

```
2 3 4
```

**Explanation:**

Windows:

- [1, 3, 2] -> sorted [1, 2, 3], 2nd smallest = 2
- [3, 2, 6] -> sorted [2, 3, 6], 2nd smallest = 3
- [2, 6, 4] -> sorted [2, 4, 6], 2nd smallest = 4

![Example Visualization](../images/HEP-007/example-1.png)

## Notes

- Use two heaps to maintain lower and upper partitions
- Apply lazy deletion when elements leave the window
- Each window update runs in O(log w)
- Space complexity: O(w)

## Related Topics

Heaps, Sliding Window, Order Statistics, Median Maintenance

---

## Solution Template

### Java


### Python


### C++


### JavaScript

