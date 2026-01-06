---
problem_id: DP_REGISTER_ALLOCATION__3510
display_id: NTB-DP-3510
slug: register-allocation
title: "Compiler Register Allocation DP"
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
  - register-allocation
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Compiler Register Allocation DP

## Problem Statement

You are given `n` variables with live intervals `[l_i, r_i]` and spill cost `c_i`. You have `R` registers. At any time, at most `R` variables can be kept in registers; the rest must be spilled, incurring their cost.

Minimize total spill cost.

## Input Format

- First line: integers `n` and `R`
- Next `n` lines: `l_i r_i c_i`

## Output Format

- Single integer: minimum total spill cost

## Constraints

- `1 <= n <= 20`
- `1 <= R <= 5`
- `0 <= l_i <= r_i <= 100`
- `0 <= c_i <= 10^9`

## Clarifying Notes

- A variable spilled incurs its cost once.

## Example Input

```
3 1
0 2 5
1 3 4
2 4 3
```

## Example Output

```
7
```
