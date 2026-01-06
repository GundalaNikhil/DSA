---
problem_id: REC_RECURSION_WITH_DELAYED_INFORMATION__3358
display_id: NTB-REC-3358
slug: recursion-with-delayed-information
title: "Recursion with Delayed Information"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - recursion
  - recursion-with-delayed-information
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursion with Delayed Information

## Problem Statement

You are given a rooted tree. Each node has a base value `b_u` and a type `t_u` (0 or 1). The recursive value is defined as:

- If `u` is a leaf, `val(u) = b_u`.
- Otherwise compute `sum_children`.
  - If `t_u = 0`, then `val(u) = b_u + sum_children`.
  - If `t_u = 1`, then `val(u) = b_u - sum_children`.

Compute `val(root)`.

## Input Format

- First line: integer `n`
- Next `n` lines: `b_u t_u parent` (parent is 0 for root)

## Output Format

- Single integer: value of the root

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= b_u <= 10^9`
- `t_u` is 0 or 1

## Clarifying Notes

- The choice of `+` or `-` depends on child results, so it is resolved only after recursion returns.

## Example Input

```
3
5 1 0
2 0 1
1 0 1
```

## Example Output

```
2
```
