---
problem_id: DP_ADVERSARIAL_COST_FUNCTION__7812
display_id: NTB-DP-7812
slug: adversarial-cost-function
title: "DP with Adversarial Cost Function"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - adversarial-cost-function
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Adversarial Cost Function

## Problem Statement

You have `n` steps and choose one action per step. For each action `i`, the adversary chooses a cost from a given set `C_i` to maximize your total cost. You choose actions to minimize the worst-case total cost.

Compute the minimum possible worst-case total cost.

## Input Format

- First line: integers `n` and `a`
- Next `a` lines: integer `k_i` followed by `k_i` costs for action `i`

## Output Format

- Single integer: minimum worst-case total cost

## Constraints

- `1 <= n <= 200`
- `1 <= a <= 10`
- `1 <= k_i <= 10`
- `0 <= cost <= 10^6`

## Clarifying Notes

- This is a minimax DP: you minimize while the adversary maximizes.

## Example Input

```
2 2
2 3 5
1 4
```

## Example Output

```
8
```
