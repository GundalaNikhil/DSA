---
problem_id: STK_WORKSHOP_NEXT_TALLER_WIDTH__8156
display_id: STK-005
slug: workshop-next-taller-width
title: "Workshop Next Taller with Width"
difficulty: Medium
difficulty_score: 45
topics:
  - Stack
  - Monotonic Stack
  - Arrays
tags:
  - stack
  - monotonic
  - next-greater
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-005: Workshop Next Taller with Width

## Problem Statement

For each height `h[i]`, find the next taller height to its right within distance at most `w`. If no taller height exists within `w`, output `-1` for that position.

![Problem Illustration](../images/STK-005/problem-illustration.png)

## Input Format

- First line: integers `n` and `w`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers, the next taller heights or `-1`

## Constraints

- `1 <= n <= 200000`
- `0 <= h[i] <= 10^9`
- `1 <= w <= n`

## Example

**Input:**

```
5 2
1 7 3 4 2
```

**Output:**

```
7 -1 4 -1 -1
```

**Explanation:**

For index 0, the next taller within distance 2 is 7. For index 2, 4 is taller and within width.

![Example Visualization](../images/STK-005/example-1.png)

## Notes

- Use a monotonic decreasing stack of indices
- Remove indices that are more than `w` away
- Pop while current height is taller to resolve answers
- Time complexity: O(n)

## Related Topics

Monotonic Stack, Next Greater Element, Sliding Window

---

## Solution Template
### Java


### Python


### C++


### JavaScript

