---
problem_id: STK_TRADING_DESK_THRESHOLD_JUMP__2549
display_id: STK-007
slug: trading-desk-threshold-jump
title: "Trading Desk Threshold Jump"
difficulty: Medium
difficulty_score: 48
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
# STK-007: Trading Desk Threshold Jump

## Problem Statement

Given prices `p[i]` and a threshold `t`, for each index find how many steps forward until you see a price at least `t` higher than `p[i]`. If no such future price exists, output `0`.

![Problem Illustration](../images/STK-007/problem-illustration.png)

## Input Format

- First line: integers `n` and `t`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers of wait steps (0 if none)

## Constraints

- `1 <= n <= 200000`
- `0 <= p[i], t <= 10^9`

## Example

**Input:**

```
5 2
3 1 4 6 5
```

**Output:**

```
2 1 1 0 0
```

**Explanation:**

For 3, the first price at least 2 higher is 4 at distance 2. For 6, no future price is >= 8.

![Example Visualization](../images/STK-007/example-1.png)

## Notes

- Use a monotonic stack of indices
- Compare `p[j] - p[i] >= t`
- Pop indices that are satisfied by the current price
- Time complexity: O(n)

## Related Topics

Next Greater Element, Monotonic Stack, Arrays

---

## Solution Template
### Java


### Python


### C++


### JavaScript

