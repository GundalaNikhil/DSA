---
problem_id: DP_STOCK_WEEK_REST_FEE__6420
display_id: DP-015
slug: stock-trading-weekly-rest-fee
title: "Stock Trading With Weekly Rest and Fee"
difficulty: Medium
difficulty_score: 55
topics:
  - Dynamic Programming
  - Greedy
  - Finance
tags:
  - dp
  - stocks
  - cooldown
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-015: Stock Trading With Weekly Rest and Fee

## Problem Statement

You are given stock prices for `n` days and a transaction fee `f`. Day 0 is Monday, day 1 is Tuesday, day 6 is Sunday, day 7 is the next Monday, and so on.

Rules:

- You may buy and sell multiple times.
- After **every sale on day `i`**, you must **rest until the next Monday** (day index `i - (i % 7) + 7`). During rest you cannot buy, but you may finish the sale that triggered the rest.
- Each sale pays `price[i] - fee` (the fee is subtracted once per sale).

Find the maximum achievable profit.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513334/dsa/dp/tegcspu3uyw2gpcnlcu6.jpg)

## Input Format

- First line: two integers `n` and `f`
- Second line: `n` integers `price[0..n-1]`

## Output Format

- Single integer: maximum profit.

## Constraints

- `1 <= n <= 100000`
- `0 <= price[i], f <= 10^9`
- Use 64-bit integers to store profits.

## Example

**Input:**
```
7 1
1 5 3 6 4 2 7
```

**Output:**
```
5
```

**Explanation:**

- Buy day 0 (Mon) at 1, sell day 1 (Tue) at 5 → profit 4, rest until next Monday (day 7, beyond the list).
- Profit = 4; no further trades possible.
- Best profit is 5 by instead holding longer: buy day 0 at 1, sell day 3 at 6 → profit 5, rest to day 7.

![Example Visualization](../images/DP-015/example-1.png)

## Notes

- You cannot buy during a rest window triggered by your last sale.
- Buying and selling on the same day is not allowed by this model (sell uses stock you already held).
- If you never sell, profit is 0.

## Related Topics

Dynamic Programming, Cooldown Scheduling, Greedy

---

## Solution Template

### Java


### Python


### C++


### JavaScript

