---
problem_id: STK_AUDITORIUM_HISTOGRAM_ONE_BOOSTER__9153
display_id: STK-013
slug: auditorium-histogram-one-booster
title: "Auditorium Histogram With One Booster"
difficulty: Medium
difficulty_score: 60
topics:
  - Stack
  - Histogram
  - Optimization
tags:
  - stack
  - histogram
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-013: Auditorium Histogram With One Booster

## Problem Statement

You are given histogram heights. You may increase exactly one bar by at most `b` units (you may choose to add less than `b`). Compute the maximum possible rectangle area after the boost.

![Problem Illustration](../images/STK-013/problem-illustration.png)

## Input Format

- First line: integers `n` and `b`
- Second line: `n` space-separated integers (heights)

## Output Format

- Single integer: maximum possible rectangle area

## Constraints

- `1 <= n <= 200000`
- `0 <= h[i], b <= 10^9`

## Example

**Input:**

```
3 3
2 4 2
```

**Output:**

```
7
```

**Explanation:**

Boost the middle bar to 7; the best rectangle has area 7.

![Example Visualization](../images/STK-013/example-1.png)

## Notes

- The classic largest-rectangle-in-histogram uses a monotonic stack
- You must account for a single boosted bar
- Consider how far each bar can extend as the minimum height
- Time complexity should be near O(n)

## Related Topics

Histogram, Monotonic Stack, Optimization

---

## Solution Template
### Java


### Python


### C++


### JavaScript

