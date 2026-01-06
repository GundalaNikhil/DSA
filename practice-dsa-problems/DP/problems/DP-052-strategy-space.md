---
problem_id: DP_STRATEGY_SPACE__2867
display_id: NTB-DP-2867
slug: strategy-space
title: "DP on Strategy Space"
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
  - strategy-space
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP on Strategy Space

## Problem Statement

You are given `s` strategies. Each strategy is a fixed sequence of actions of length `K` and yields a total reward `R_s` when executed. You must execute exactly `n` actions (`n` is divisible by `K`) by selecting a sequence of strategies. Switching strategies has a cost `C` applied each time the chosen strategy differs from the previous block.

Maximize total reward minus switch costs.

## Input Format

- First line: integers `n`, `K`, `s`, `C`
- Next `s` lines: integer `R_s`

## Output Format

- Single integer: maximum total score

## Constraints

- `1 <= n <= 200`
- `1 <= K <= n`, `n % K == 0`
- `1 <= s <= 50`
- `0 <= C <= 10^9`

## Clarifying Notes

- The first strategy does not incur a switch cost.

## Example Input

```
4 2 2 3
10
7
```

## Example Output

```
20
```
