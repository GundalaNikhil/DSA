---
problem_id: DP_POLICY_SELECTION__4090
display_id: NTB-DP-4090
slug: policy-selection
title: "DP on Policy Selection"
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
  - policy-selection
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP on Policy Selection

## Problem Statement

You must traverse positions `1..m` in exactly `n` moves, starting at position 1 and ending at position `m`. You have `p` policies. Policy `k` defines move costs `cost_k[i][j]` for moving from `i` to `j` (only `j = i+1` or `j = i-1`). You may switch policies at any time; each switch costs `S`.

Minimize total cost.

## Input Format

- First line: integers `n`, `m`, `p`, `S`
- Next `p` blocks:
  - Two lines with `m-1` integers each: forward costs and backward costs for the policy

## Output Format

- Single integer: minimum total cost, or `-1` if impossible

## Constraints

- `1 <= n <= 200`
- `2 <= m <= 50`
- `1 <= p <= 5`
- `0 <= S <= 10^6`

## Clarifying Notes

- Switching policies changes future move costs but does not move position.
- State includes position, step, and current policy.

## Example Input

```
3 3 2 5
1 2
2 1
2 2
1 3
```

## Example Output

```
3
```
