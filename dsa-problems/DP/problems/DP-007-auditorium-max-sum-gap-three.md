---
problem_id: DP_MAXSUM_GAP3__7706
display_id: DP-007
slug: auditorium-max-sum-gap-three
title: "Auditorium Max Sum With Gap Three"
difficulty: Medium
difficulty_score: 45
topics:
  - Dynamic Programming
  - Array
  - Optimization
tags:
  - dp
  - arrays
  - maximum-sum
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-007: Auditorium Max Sum With Gap Three

## Problem Statement

You are given an integer array `a` of length `n`. You want to select a subset of indices to maximize the sum of selected values, with the constraint:

For any two selected indices `i` and `j` (`i != j`), `|i - j| >= 3`.

In other words, if you pick index `i`, you cannot pick `i-1`, `i-2`, `i+1`, or `i+2`.

Return the maximum possible sum.

![Problem Illustration](../images/DP-007/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `a[i]`

## Output Format

Print one integer: the maximum sum achievable under the gap constraint.

## Constraints

- `1 <= n <= 100000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**
```
5
4 1 2 9 3
```

**Output:**
```
13
```

**Explanation:**

One optimal selection is indices `0` and `3`:

- `a[0] + a[3] = 4 + 9 = 13`
- Distance between indices: `3` (allowed)

So the answer is `13`.

![Example Visualization](../images/DP-007/example-1.png)

## Notes

- You are allowed to pick **no elements**; in that case the sum is `0`. This matters when all numbers are negative.
- This is a “House Robber”-style DP with a skip of 2 indices between picks.
- Use 64-bit integer arithmetic for sums.

## Related Topics

Dynamic Programming, Array DP, Maximum Sum

---

## Solution Template

### Java


### Python


### C++


### JavaScript


