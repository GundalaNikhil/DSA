---
problem_id: DP_RESOURCE_BORROWING__4551
display_id: NTB-DP-4551
slug: resource-borrowing
title: "DP on Resource Allocation with Borrowing"
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
  - resource-borrowing
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP on Resource Allocation with Borrowing

## Problem Statement

You have `n` steps and a resource balance. You may borrow resources, making the balance negative. Each step, borrowed amount incurs interest: `balance = balance - interest` if balance is negative.

Each action yields reward `r_i` and changes balance by `d_i`. The balance must never drop below `-B`.

Maximize total reward.

## Input Format

- First line: integers `n`, `a`, `B`, `interest`
- Next `a` lines: `r_i d_i`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 100`
- `1 <= a <= 10`
- `0 <= B <= 50`
- `0 <= interest <= 10`
- `-10 <= d_i <= 10`

## Clarifying Notes

- Interest applies after action effect each step.

## Example Input

```
2 2 5 1
5 -3
2 2
```

## Example Output

```
7
```
