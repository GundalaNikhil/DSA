---
problem_id: PRB_COIN_FLIP_STREAK_PROBABILITY__1842
display_id: PRB-001
slug: coin-flip-streak-probability
title: "Coin Flip Streak Probability"
difficulty: Medium
difficulty_score: 40
topics:
  - Probability
  - Dynamic Programming
  - Markov Chains
tags:
  - probability
  - dp
  - streaks
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-001: Coin Flip Streak Probability

## Problem Statement

A fair coin is flipped `n` times. Compute the probability of getting at least one streak of `k` consecutive heads.

![Problem Illustration](../images/PRB-001/problem-illustration.png)

## Input Format

- Single line: two integers `n` and `k`

## Output Format

- Single floating-point number: the probability

## Constraints

- `1 <= n <= 60`
- `1 <= k <= n`

## Example

**Input:**

```
3 2
```

**Output:**

```
0.375
```

**Explanation:**

The sequences with at least one streak of two consecutive heads are HHT, HHH, and THH. Each has probability 1/8, total 3/8 = 0.375.

![Example Visualization](../images/PRB-001/example-1.png)

## Notes

- Use DP with state (position, current run of heads)
- Probability = 1 - probability of no length-k streak
- Accept answers with absolute error <= 1e-6
- Time complexity: O(n \* k)

## Related Topics

Probability, DP, Streaks

---

## Solution Template

### Java


### Python


### C++


### JavaScript

