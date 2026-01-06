---
problem_id: DP_MULTI_OBJECTIVE_OPTIMIZATION__7521
display_id: NTB-DP-7521
slug: multi-objective-optimization
title: "DP with Multi-Objective Optimization"
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
  - multi-objective-optimization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Multi-Objective Optimization

## Problem Statement

You must choose one action per step for `n` steps. Action `i` yields reward `r_i` and fatigue `f_i`.

Maximize total reward. If multiple sequences achieve the same maximum reward, choose the one with minimum total fatigue.

Output both values.

## Input Format

- First line: integers `n` and `a`
- Next `a` lines: `r_i f_i`

## Output Format

- Two integers: maximum reward and corresponding minimum fatigue

## Constraints

- `1 <= n <= 200`
- `1 <= a <= 20`
- `-10^9 <= r_i, f_i <= 10^9`

## Clarifying Notes

- Tie-breaking is applied only after maximizing reward.

## Example Input

```
2 2
5 3
5 1
```

## Example Output

```
10 2
```
