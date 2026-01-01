---
problem_id: QUE_LAB_WINDOW_INSTABILITY__3951
display_id: QUE-007
slug: lab-window-instability
title: "Lab Window Instability"
difficulty: Medium
difficulty_score: 50
topics:
  - Sliding Window
  - Queue
  - Heaps
tags:
  - sliding-window
  - deque
  - median
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-007: Lab Window Instability

## Problem Statement

A lab monitors sensor readings in a sliding window. For each window of size `k`, compute:

```
instability = floor((max - min) / median)
```

The median is the lower median when `k` is even. If the median is `0`, output `0` for that window.

![Problem Illustration](../images/QUE-007/problem-illustration.png)

## Input Format

- First line: two integers `n` and `k`
- Second line: `n` space-separated integers (readings)

## Output Format

- Single line: `n - k + 1` integers, each the instability of a window

## Constraints

- `1 <= n <= 200000`
- `1 <= k <= n`
- Readings fit in 32-bit signed integer

## Example

**Input:**

```
5 3
5 1 4 6 2
```

**Output:**

```
1 1 1
```

**Explanation:**

Windows:

- [5, 1, 4] -> min=1, max=5, median=4, (5-1)/4=1
- [1, 4, 6] -> min=1, max=6, median=4, (6-1)/4=1
- [4, 6, 2] -> min=2, max=6, median=4, (6-2)/4=1

![Example Visualization](../images/QUE-007/example-1.png)

## Notes

- Use deques for max and min in O(1) amortized time
- Use two heaps with lazy deletion for the median
- Keep the lower heap size equal to or one more than the upper heap
- Total time complexity should be O(n log k)

## Related Topics

Sliding Window, Deque, Median Maintenance

---

## Solution Template

### Java


### Python


### C++


### JavaScript

