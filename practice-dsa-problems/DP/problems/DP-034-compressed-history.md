---
problem_id: DP_COMPRESSED_HISTORY__2785
display_id: NTB-DP-2785
slug: compressed-history
title: "DP on Compressed History"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - compressed-history
  - data-structures
  - dp
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP on Compressed History

## Problem Statement

You choose one of `a` actions each step for `n` steps. Only two summary statistics are kept: total sum of chosen action values and the maximum single action value used so far.

Each action `i` adds value `v_i` and reward `r_i`. A sequence is valid only if at every step:

```
max_value_so_far <= total_sum_so_far
```

Maximize total reward.

## Input Format

- First line: integers `n` and `a`
- Next `a` lines: `v_i r_i`

## Output Format

- Single integer: maximum total reward, or `-1` if impossible

## Constraints

- `1 <= n <= 100`
- `1 <= a <= 10`
- `0 <= v_i <= 20`
- `-10^9 <= r_i <= 10^9`

## Clarifying Notes

- State includes step, total sum, and max value so far.

## Example Input

```
3 2
1 5
3 4
```

## Example Output

```
14
```
