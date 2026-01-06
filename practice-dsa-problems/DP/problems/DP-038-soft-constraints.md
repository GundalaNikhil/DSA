---
problem_id: DP_SOFT_CONSTRAINTS__9598
display_id: NTB-DP-9598
slug: soft-constraints
title: "DP with Soft Constraints"
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
  - soft-constraints
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Soft Constraints

## Problem Statement

You must choose one action per step for `n` steps. Each action `i` yields reward `r_i`. There are `c` constraints of the form "action i must be used at most L times". Violating a constraint is allowed but incurs penalty `P` per extra use.

Maximize total reward minus penalties.

## Input Format

- First line: integers `n`, `a`, `c`, `P`
- Second line: `a` integers: rewards
- Next `c` lines: `action_id L`

## Output Format

- Single integer: maximum total score

## Constraints

- `1 <= n <= 60`
- `1 <= a <= 6`
- `0 <= P <= 10^6`

## Clarifying Notes

- If an action appears in multiple constraints, all penalties apply.

## Example Input

```
3 2 1 2
5 3
1 1
```

## Example Output

```
11
```
