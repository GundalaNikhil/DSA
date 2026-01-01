---
problem_id: DP_REQ_WEIGHT_KNAP__6427
display_id: DP-003
slug: required-weight-knapsack
title: "Required Weight Knapsack"
difficulty: Medium
difficulty_score: 54
topics:
  - Dynamic Programming
  - Knapsack
  - Optimization
tags:
  - dp
  - knapsack
  - 0-1-knapsack
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-003: Required Weight Knapsack

## Problem Statement

You are given `n` items. Item `i` has weight `w[i]` and value `v[i]`. You also have a knapsack with maximum capacity `W`.

Unlike classic knapsack, you must select items such that the **total weight is at least `R`** (required minimum weight) and **at most `W`**.

Your task is to maximize the total value under these constraints.

If it is impossible to reach total weight ≥ `R` without exceeding `W`, print `-1`.

![Problem Illustration](../images/DP-003/problem-illustration.png)

## Input Format

- First line: three integers `n`, `W`, `R`
- Next `n` lines: two integers `w[i]` and `v[i]`

## Output Format

Print a single integer:

- maximum achievable value with `R <= totalWeight <= W`, or
- `-1` if no valid selection exists

## Constraints

- `1 <= n <= 200`
- `1 <= W <= 5000`
- `0 <= R <= W`
- `1 <= w[i] <= W`
- `0 <= v[i] <= 10^9`

## Example

**Input:**
```
3 6 5
2 4
3 5
4 6
```

**Output:**
```
10
```

**Explanation:**

Valid selections must have total weight between 5 and 6:

- Pick items with weights `2 + 3 = 5` ⇒ value `4 + 5 = 9`
- Pick items with weights `2 + 4 = 6` ⇒ value `4 + 6 = 10` ✅ best

So the answer is `10`.

![Example Visualization](../images/DP-003/example-1.png)

## Notes

- This is a **0/1 knapsack**: each item can be taken at most once.
- The “required minimum weight” constraint is handled by taking the best value among weights `R..W`.
- Use 64-bit integers for value sums.

## Related Topics

Dynamic Programming, 0/1 Knapsack, Optimization

---

## Solution Template

### Java


### Python


### C++


### JavaScript


