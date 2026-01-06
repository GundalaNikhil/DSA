---
problem_id: DP_OSCILLATING_COSTS__2069
display_id: NTB-DP-2069
slug: oscillating-costs
title: "DP with Oscillating Costs"
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
  - optimization
  - oscillating-costs
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Oscillating Costs

## Problem Statement

You have `n` steps and `a` actions. Each action `i` has a base cost `c_i`. Each action also has a usage level `u_i` (initially 0). At each step:

- If you choose action `i`, you pay `c_i + inc_i * u_i`, then `u_i` increases by 1 up to `U`.
- For every other action `j != i`, `u_j` decreases by `dec_j` down to 0.

Find the minimum total cost over `n` steps.

## Input Format

- First line: integers `n`, `a`, `U`
- Next `a` lines: `c_i inc_i dec_i`

## Output Format

- Single integer: minimum total cost

## Constraints

- `1 <= n <= 60`
- `1 <= a <= 3`
- `0 <= U <= 6`
- `0 <= c_i, inc_i, dec_i <= 10`

## Clarifying Notes

- Usage levels are capped in `[0, U]`.

## Example Input

```
4 2 3
1 2 1
2 1 1
```

## Example Output

```
6
```
