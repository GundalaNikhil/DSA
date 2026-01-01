---
problem_id: STK_CANTEEN_TOKEN_CLIMB_SPAN__6180
display_id: STK-008
slug: canteen-token-climb-span
title: "Canteen Token Climb Span"
difficulty: Medium
difficulty_score: 50
topics:
  - Stack
  - Monotonic Stack
  - Spans
tags:
  - stack
  - spans
  - monotonic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-008: Canteen Token Climb Span

## Problem Statement

For each day, compute how many consecutive prior days had demand strictly lower than today's demand. If any prior day equals today's demand, the span resets to 0 at that day.

Return the span counts (not including today).

![Problem Illustration](../images/STK-008/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (demands)

## Output Format

- Single line: `n` integers of spans

## Constraints

- `1 <= n <= 100000`
- `0 <= demand[i] <= 10^9`

## Example

**Input:**

```
5
3 1 2 2 5
```

**Output:**

```
0 0 1 0 4
```

**Explanation:**

Day 4 (value 5) has four prior days with smaller demand; day 3 equals 2 so its span is 0.

![Example Visualization](../images/STK-008/example-1.png)

## Notes

- Use a strictly increasing stack of (value, index)
- Pop while values are strictly lower
- If the top equals current, span is 0
- Time complexity: O(n)

## Related Topics

Stock Span, Monotonic Stack, Arrays

---

## Solution Template
### Java


### Python


### C++


### JavaScript

