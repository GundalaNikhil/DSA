---
problem_id: DP_ERROR_PROPAGATION__5688
display_id: NTB-DP-5688
slug: error-propagation
title: "DP with Error Propagation"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - error-propagation
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Error Propagation

## Problem Statement

You have `n` steps and actions with reward `r_i` and error `e_i`. The total error accumulates and is multiplied by a factor `k` each step:

```
error = k * error + e_i
```

You must keep error <= `E_max` at all times. Maximize total reward.

## Input Format

- First line: integers `n`, `a`, `k`, `E_max`
- Next `a` lines: `r_i e_i`

## Output Format

- Single integer: maximum total reward, or `-1` if impossible

## Constraints

- `1 <= n <= 50`
- `1 <= a <= 6`
- `0 <= k <= 5`
- `0 <= E_max <= 200`

## Clarifying Notes

- Error values are integers; use exact arithmetic.

## Example Input

```
3 2 2 10
5 1
3 2
```

## Example Output

```
13
```
