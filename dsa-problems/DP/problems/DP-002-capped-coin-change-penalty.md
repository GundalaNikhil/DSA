---
problem_id: DP_COIN_CAP_PENALTY__1842
display_id: DP-002
slug: capped-coin-change-penalty
title: "Capped Coin Change With Penalty"
difficulty: Medium
difficulty_score: 58
topics:
  - Dynamic Programming
  - Knapsack
  - Optimization
tags:
  - dp
  - knapsack
  - bounded-knapsack
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-002: Capped Coin Change With Penalty

## Problem Statement

You are given `k` coin types. Coin type `i` has:

- denomination `d[i]`
- maximum usable count `c[i]`
- penalty `p[i]`

You want to form an exact sum `target`.

Cost rules:

- Each coin you use contributes `+1` to total cost.
- For each coin type `i`, if you use **more than** `floor(c[i]/2)` coins of that type, you pay an additional one-time penalty `+p[i]` (for that type).

Compute the minimum total cost to form `target`. If it is impossible, print `-1`.

![Problem Illustration](../images/DP-002/problem-illustration.png)

## Input Format

- First line: two integers `k` and `target`
- Next `k` lines: three integers `d[i] c[i] p[i]`

## Output Format

Print a single integer: the minimum cost, or `-1` if unreachable.

## Constraints

- `1 <= k <= 50`
- `1 <= target <= 5000`
- `1 <= d[i] <= 5000`
- `0 <= c[i] <= 10^9` (effective usage is capped by `target / d[i]`)
- `0 <= p[i] <= 10^9`

## Example

**Input:**
```
2 7
1 4 2
5 2 1
```

**Output:**
```
3
```

**Explanation:**

- One optimal way is `5 + 1 + 1 = 7`. It uses:
  - coin `5`: 1 time (≤ floor(2/2)=1, no penalty)
  - coin `1`: 2 times (≤ floor(4/2)=2, no penalty)
- Total coins used = 3, and no penalties are triggered ⇒ minimum cost is `3`.

![Example Visualization](../images/DP-002/example-1.png)

## Notes

- The penalty for type `i` is charged **at most once**, and only if `used_i > floor(c[i]/2)`.
- You must respect the maximum count `c[i]` for each type.
- This is a bounded knapsack variant with a “threshold + activation cost”.

## Related Topics

Dynamic Programming, Knapsack, Optimization

---

## Solution Template

### Java


### Python


### C++


### JavaScript

