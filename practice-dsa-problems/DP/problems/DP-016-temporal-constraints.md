---
problem_id: DP_TEMPORAL_CONSTRAINTS__9592
display_id: NTB-DP-9592
slug: temporal-constraints
title: "DP on Temporal Constraints"
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
  - technical-interview-prep
  - temporal-constraints
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP on Temporal Constraints

## Problem Statement

You have `n` time slots and `t` tasks. Task `i` must be scheduled within time window `[l_i, r_i]` and yields reward `v_i`. You may schedule at most one task per time slot. A task can be scheduled at most once.

Maximize total reward.

## Input Format

- First line: integers `n` and `t`
- Next `t` lines: `l_i r_i v_i`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 2000`
- `1 <= t <= 2000`
- `1 <= l_i <= r_i <= n`
- `0 <= v_i <= 10^9`

## Clarifying Notes

- This is a weighted scheduling DP with time windows.

## Example Input

```
3 2
1 2 5
2 3 6
```

## Example Output

```
11
```
