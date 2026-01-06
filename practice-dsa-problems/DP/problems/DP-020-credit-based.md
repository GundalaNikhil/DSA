---
problem_id: DP_CREDIT_BASED__7513
display_id: NTB-DP-7513
slug: credit-based
title: "Credit-Based DP"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - credit-based
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

# Credit-Based DP

## Problem Statement

You have `n` steps and a credit balance. Each step you choose one action. Action `i` yields reward `r_i` and consumes `c_i` credits. Credits regenerate by `g` per step, capped at `C`.

Maximize total reward.

## Input Format

- First line: integers `n`, `a`, `C`, `g`
- Next `a` lines: `r_i c_i`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `1 <= a <= 10`
- `0 <= C <= 50`
- `0 <= g <= 50`
- `0 <= c_i <= C`
- `-10^9 <= r_i <= 10^9`

## Clarifying Notes

- Credits regenerate at the start of each step.

## Example Input

```
3 2 5 2
4 3
1 1
```

## Example Output

```
9
```
