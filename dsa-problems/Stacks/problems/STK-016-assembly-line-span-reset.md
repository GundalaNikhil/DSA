---
problem_id: STK_ASSEMBLY_LINE_SPAN_RESET__3846
display_id: STK-016
slug: assembly-line-span-reset
title: "Assembly Line Span Reset"
difficulty: Medium
difficulty_score: 45
topics:
  - Stack
  - Spans
  - Arrays
tags:
  - stack
  - spans
  - arrays
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-016: Assembly Line Span Reset

## Problem Statement

Given daily production counts, compute for each day the span of consecutive prior days with counts strictly less than today's count. The span includes today as 1.

Return the span counts.

![Problem Illustration](../images/STK-016/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers of spans

## Constraints

- `1 <= n <= 100000`
- `0 <= count[i] <= 10^9`

## Example

**Input:**

```
5
2 1 3 2 5
```

**Output:**

```
1 1 3 1 5
```

**Explanation:**

Day 3 (value 3) covers days 1..3, and day 5 covers all prior days.

![Example Visualization](../images/STK-016/example-1.png)

## Notes

- Use a monotonic decreasing stack of (value, span)
- Pop while top value is strictly less than current
- Add spans as you pop
- Time complexity: O(n)

## Related Topics

Stock Span, Monotonic Stack, Arrays

---

## Solution Template
### Java


### Python


### C++


### JavaScript

