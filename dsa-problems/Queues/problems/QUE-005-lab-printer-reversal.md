---
problem_id: QUE_LAB_PRINTER_REVERSAL__6429
display_id: QUE-005
slug: lab-printer-reversal
title: "Lab Printer Reversal"
difficulty: Easy
difficulty_score: 26
topics:
  - Queue
  - Stack
  - Simulation
tags:
  - queue
  - stack
  - reversal
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-005: Lab Printer Reversal

## Problem Statement

A lab printer processes jobs in a queue. The technician wants to reverse the first `k` jobs while preserving the order of the remaining jobs.

Given the queue and `k`, output the new queue order.

![Problem Illustration](../images/QUE-005/problem-illustration.png)

## Input Format

- First line: integer `n` (number of jobs)
- Second line: `n` space-separated integers (queue order, front to back)
- Third line: integer `k` (number of jobs to reverse from the front)

## Output Format

- Single line: updated queue values, space-separated

## Constraints

- `1 <= n <= 100000`
- `1 <= k <= n`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
5
2 4 6 8 10
4
```

**Output:**

```
8 6 4 2 10
```

**Explanation:**

Reverse the first 4 jobs:

- Original: `[2, 4, 6, 8, 10]`
- After reversal of first 4: `[8, 6, 4, 2, 10]`

![Example Visualization](../images/QUE-005/example-1.png)

## Notes

- Use a stack to reverse the first `k` elements
- Append the remaining `n - k` elements in their original order
- Time complexity: O(n)
- Space complexity: O(k)

## Related Topics

Queue, Stack, Reversal

---

## Solution Template

### Java


### Python


### C++


### JavaScript

