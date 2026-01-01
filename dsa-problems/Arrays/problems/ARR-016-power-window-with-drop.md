---
problem_id: ARR_POWER_WINDOW_DROP__2879
display_id: ARR-016
slug: power-window-with-drop
title: "Power Window With Drop"
difficulty: Medium
difficulty_score: 49
topics:
  - Arrays
  - Sliding Window
  - Greedy
tags:
  - arrays
  - sliding-window
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-016: Power Window With Drop

## Problem Statement

Given positive integers and a window size k, find the maximum sum of any window after optionally removing one element from that window (you may also remove none).

![Problem Illustration](../images/ARR-016/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]
- Third line: integer k

## Output Format

Print the maximum adjusted window sum.

## Constraints

- `1 <= n <= 200000`
- `1 <= k <= n`
- `1 <= arr[i] <= 1000000000`

## Example

**Input:**
```
5
2 1 5 3 2
3
```

**Output:**
```
10
```

**Explanation:**

Window [5, 3, 2] sums to 10 with no drop, which is the maximum.

![Example Visualization](../images/ARR-016/example-1.png)

## Notes

- You may drop at most one element per window.
- All elements are positive.

## Related Topics

Sliding Window, Greedy, Arrays

---

## Solution Template

### Java



### Python



### C++



### JavaScript


