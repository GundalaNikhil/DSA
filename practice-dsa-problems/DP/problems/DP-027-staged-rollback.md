---
problem_id: DP_STAGED_ROLLBACK__4334
display_id: NTB-DP-4334
slug: staged-rollback
title: "DP with Staged Rollback"
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
  - staged-rollback
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Staged Rollback

## Problem Statement

You have `n` steps and may create checkpoints at chosen steps. Each rollback returns you to the most recent checkpoint and costs `C`. You may rollback at most `R` times.

Each step `i` has reward `v_i`. If you rollback, all rewards gained after the checkpoint are discarded.

Maximize total reward.

## Input Format

- First line: integers `n`, `R`, `C`
- Second line: `n` integers: rewards `v_1..v_n`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `0 <= R <= 10`
- `0 <= C <= 10^9`
- `-10^9 <= v_i <= 10^9`

## Clarifying Notes

- A rollback can only return to an existing checkpoint. You may choose to never set a checkpoint.

## Example Input

```
4 1 3
5 -10 5 5
```

## Example Output

```
10
```
