---
problem_id: QUE_CORRIDOR_WINDOW_SECOND_MINIMUM__2748
display_id: QUE-008
slug: corridor-window-second-minimum
title: "Corridor Window Second Minimum"
difficulty: Medium
difficulty_score: 48
topics:
  - Sliding Window
  - Ordered Map
  - Queue
tags:
  - sliding-window
  - multiset
  - queue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-008: Corridor Window Second Minimum

## Problem Statement

Security sensors report values along a corridor. For each sliding window of size `k`, you must output the second smallest value in that window.

If the window size is `1`, the second smallest value is defined as the only element. If the smallest value appears at least twice, the second smallest equals the smallest.

![Problem Illustration](../images/QUE-008/problem-illustration.png)

## Input Format

- First line: two integers `n` and `k`
- Second line: `n` space-separated integers (sensor values)

## Output Format

- Single line: `n - k + 1` integers, each the second smallest for a window

## Constraints

- `1 <= n <= 200000`
- `1 <= k <= n`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
5 3
6 2 5 1 7
```

**Output:**

```
5 2 5
```

**Explanation:**

Windows and second minima:

- [6, 2, 5] -> sorted [2, 5, 6], second smallest = 5
- [2, 5, 1] -> sorted [1, 2, 5], second smallest = 2
- [5, 1, 7] -> sorted [1, 5, 7], second smallest = 5

![Example Visualization](../images/QUE-008/example-1.png)

## Notes

- Maintain a balanced structure with counts to track the smallest two values
- Removing outgoing elements must update counts correctly
- Time complexity: O(n log k)
- Space complexity: O(k)

## Related Topics

Sliding Window, Multiset, Ordered Map

---

## Solution Template

### Java


### Python


### C++


### JavaScript

