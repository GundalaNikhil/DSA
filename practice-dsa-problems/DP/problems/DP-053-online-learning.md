---
problem_id: DP_ONLINE_LEARNING__6195
display_id: NTB-DP-6195
slug: online-learning
title: "DP with Online Learning"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - online-learning
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Online Learning

## Problem Statement

You have `n` steps and `a` actions. Each action `i` has base cost `c_i` and a learning penalty that increases with usage: the `k`-th time you choose action `i`, you pay an extra `p_i * k`.

Minimize total cost.

## Input Format

- First line: integers `n` and `a`
- Next `a` lines: `c_i p_i`

## Output Format

- Single integer: minimum total cost

## Constraints

- `1 <= n <= 100`
- `1 <= a <= 10`
- `0 <= c_i, p_i <= 10^6`

## Clarifying Notes

- This is a DP over action usage counts.

## Example Input

```
3 2
1 1
2 0
```

## Example Output

```
5
```
