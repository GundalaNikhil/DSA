---
problem_id: DP_IRREVERSIBLE_DECISIONS__9474
display_id: NTB-DP-9474
slug: irreversible-decisions
title: "DP with Irreversible Decisions"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - irreversible-decisions
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Irreversible Decisions

## Problem Statement

You have `n` steps and `m` modes. At step 1 you start in mode 1. At any step you may stay in the current mode or move to a higher mode. Moving to a higher mode is **irreversible**; you can never return to a lower mode.

Each step `i` in mode `k` yields reward `R[i][k]`. Maximize total reward over `n` steps.

## Input Format

- First line: integers `n` and `m`
- Next `n` lines: `m` integers `R[i][1..m]`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200000`
- `1 <= m <= 50`
- `-10^9 <= R[i][k] <= 10^9`

## Clarifying Notes

- You may move to a higher mode at most `m-1` times.

## Example Input

```
3 3
3 1 0
2 4 2
1 5 3
```

## Example Output

```
12
```
