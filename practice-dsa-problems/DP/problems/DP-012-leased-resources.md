---
problem_id: DP_LEASED_RESOURCES__7345
display_id: NTB-DP-7345
slug: leased-resources
title: "DP with Leased Resources"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - leased-resources
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Leased Resources

## Problem Statement

You have `n` days and `r` resource types. Each resource lease has a duration `L` days. Each day you can choose one task or skip. Task `i` yields reward `v_i` and requires a subset of resources. If you use a resource on a day, its lease timer resets to `L`. If a resource is not used for `L` consecutive days, it expires and cannot be used until you pay a renewal cost `c_j` to reactivate it.

Find the maximum total reward.

## Input Format

- First line: integers `n`, `r`, `L`
- Second line: `r` integers: renewal costs `c_1..c_r`
- Third line: integer `t` (number of task types)
- Next `t` lines: `v_i` and a bitmask of required resources (0..(1<<r)-1)

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 30`
- `1 <= r <= 6`
- `1 <= L <= 6`
- `1 <= t <= 10`
- `0 <= v_i, c_j <= 1000`

## Clarifying Notes

- If a required resource is expired, you may renew it by paying `c_j` before performing the task.
- State includes remaining lease timers for each resource.

## Example Input

```
3 2 2
3 4
2
5 1
4 2
```

## Example Output

```
9
```
