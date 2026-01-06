---
problem_id: DP_DIMINISHING_RETURNS_PER_PATH__5314
display_id: NTB-DP-5314
slug: diminishing-returns-per-path
title: "DP with Diminishing Returns per Path"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - diminishing-returns-per-path
  - dp
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Diminishing Returns per Path

## Problem Statement

You have `p` paths. Choosing path `i` for the `k`-th time yields reward `R[i][k]` (non-increasing in `k`). You must make exactly `n` choices.

Maximize total reward.

## Input Format

- First line: integers `n` and `p`
- Next `p` lines: `n` integers: reward table for each path (rewards for the 1st..n-th use)

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `1 <= p <= 10`
- `-10^9 <= R[i][k] <= 10^9`

## Clarifying Notes

- Each path can be chosen at most `n` times.

## Example Input

```
3 2
5 3 1
4 2 2
```

## Example Output

```
11
```
