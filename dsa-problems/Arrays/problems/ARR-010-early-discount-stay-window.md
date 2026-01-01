---
problem_id: ARR_EARLY_DISCOUNT_WINDOW__9051
display_id: ARR-010
slug: early-discount-stay-window
title: "Early Discount With Stay Window and Ceiling"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
  - Sliding Window
  - Greedy
tags:
  - arrays
  - sliding-window
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-010: Early Discount With Stay Window and Ceiling

## Problem Statement

You may buy once and sell once. You must hold the item for at least dMin days and at most dMax days. The selling price is capped at C. Return the maximum profit, or 0 if no profitable trade exists.

![Problem Illustration](../images/ARR-010/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers prices[i]
- Third line: integers dMin, dMax, and C

## Output Format

Print the maximum achievable profit (0 if none).

## Constraints

- `1 <= n <= 200000`
- `0 <= prices[i] <= 1000000000`
- `1 <= dMin <= dMax <= n`
- `0 <= C <= 1000000000`

## Example

**Input:**
```
5
7 2 5 1 9
1 3 6
```

**Output:**
```
5
```

**Explanation:**

Buy at price 1 and sell at min(9, 6) = 6 for a profit of 5.

![Example Visualization](../images/ARR-010/example-1.png)

## Notes

- You must buy before you sell.
- The holding period is in days between buy and sell indices.

## Related Topics

Sliding Window, Greedy, Arrays

---

## Solution Template

### Java



### Python



### C++



### JavaScript


