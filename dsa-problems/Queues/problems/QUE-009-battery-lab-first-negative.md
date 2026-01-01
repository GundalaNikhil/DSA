---
problem_id: QUE_BATTERY_LAB_FIRST_NEGATIVE__8630
display_id: QUE-009
slug: battery-lab-first-negative
title: "Battery Lab First Negative"
difficulty: Easy
difficulty_score: 32
topics:
  - Sliding Window
  - Queue
  - Array
tags:
  - sliding-window
  - queue
  - negatives
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-009: Battery Lab First Negative

## Problem Statement

A battery lab records voltage deltas over time. For each window of size `k`, report the first negative value in that window. If a window contains no negative values, output `0`.

![Problem Illustration](../images/QUE-009/problem-illustration.png)

## Input Format

- First line: two integers `n` and `k`
- Second line: `n` space-separated integers (voltage deltas)

## Output Format

- Single line: `n - k + 1` integers, each the first negative in the window or `0`

## Constraints

- `1 <= n <= 100000`
- `1 <= k <= n`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
5 2
5 -2 -7 3 4
```

**Output:**

```
-2 -2 -7 0
```

**Explanation:**

Windows:

- [5, -2] -> first negative is -2
- [-2, -7] -> first negative is -2
- [-7, 3] -> first negative is -7
- [3, 4] -> no negatives -> 0

![Example Visualization](../images/QUE-009/example-1.png)

## Notes

- Store indices of negative values in a queue
- Remove indices that fall out of the window
- The front of the queue is always the first negative
- Time complexity: O(n)

## Related Topics

Sliding Window, Queue, Two Pointers

---

## Solution Template

### Java


### Python


### C++


### JavaScript

