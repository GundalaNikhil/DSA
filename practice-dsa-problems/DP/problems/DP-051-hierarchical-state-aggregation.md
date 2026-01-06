---
problem_id: DP_HIERARCHICAL_STATE_AGGREGATION__6904
display_id: NTB-DP-6904
slug: hierarchical-state-aggregation
title: "DP with Hierarchical State Aggregation"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - hierarchical-state-aggregation
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Hierarchical State Aggregation

## Problem Statement

There are `g` groups, each containing several states. At each step you choose a state; reward depends on the state and the number of times its group has been chosen so far.

For group `u`, the reward multiplier for the `k`-th pick in that group is `M[u][k]`.

Maximize total reward after `n` steps.

## Input Format

- First line: integers `n` and `g`
- Next `g` lines: integer `s_u` followed by `s_u` state rewards
- Next `g` lines: `n` integers: multipliers `M[u][1..n]`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 60`
- `1 <= g <= 6`
- Total states <= 20
- `-10^9 <= rewards <= 10^9`

## Clarifying Notes

- Group pick counts start at 0.

## Example Input

```
3 2
2 5 2
1 4
1 1 1
2 1 1
```

## Example Output

```
15
```
