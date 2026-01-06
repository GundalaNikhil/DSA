---
problem_id: DP_MAINTENANCE_WINDOWS__2365
display_id: NTB-DP-2365
slug: maintenance-windows
title: "DP with Maintenance Windows"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - maintenance-windows
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Maintenance Windows

## Problem Statement

You have `n` time slots. In each slot you may perform a task earning reward `v_i`, or do maintenance earning 0. You must schedule maintenance so that there is **at least one maintenance slot in every window of length `W`**.

Maximize total reward.

## Input Format

- First line: integers `n` and `W`
- Second line: `n` integers: rewards `v_1..v_n`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200000`
- `1 <= W <= n`
- `-10^9 <= v_i <= 10^9`

## Clarifying Notes

- This is equivalent to choosing maintenance positions to satisfy sliding-window constraints.

## Example Input

```
5 3
5 4 3 2 1
```

## Example Output

```
9
```
