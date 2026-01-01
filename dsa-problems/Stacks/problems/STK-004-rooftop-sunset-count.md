---
problem_id: STK_ROOFTOP_SUNSET_COUNT__2974
display_id: STK-004
slug: rooftop-sunset-count
title: "Rooftop Sunset Count"
difficulty: Easy
difficulty_score: 32
topics:
  - Stack
  - Monotonic Stack
  - Arrays
tags:
  - stack
  - monotonic
  - arrays
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-004: Rooftop Sunset Count

## Problem Statement

Given building heights from west to east, a building can see the sunset if there is no taller building to its left. Count how many buildings can see the sunset.

![Problem Illustration](../images/STK-004/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (heights)

## Output Format

- Single integer: number of buildings with sunset view

## Constraints

- `1 <= n <= 200000`
- `0 <= h[i] <= 10^9`

## Example

**Input:**

```
5
2 5 2 6 1
```

**Output:**

```
3
```

**Explanation:**

Buildings with sunset view are heights 2, 5, and 6.

![Example Visualization](../images/STK-004/example-1.png)

## Notes

- Use a monotonic decreasing stack
- Pop while current height is greater than or equal to stack top
- Count remaining stack size at the end
- Time complexity: O(n)

## Related Topics

Monotonic Stack, Visibility, Arrays

---

## Solution Template
### Java


### Python


### C++


### JavaScript

