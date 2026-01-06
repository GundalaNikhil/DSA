---
problem_id: DP_CHUNKED_DP_BOUNDARY__6929
display_id: NTB-DP-6929
slug: chunked-dp-boundary
title: "Chunked DP with Boundary Conditions"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - chunked-dp-boundary
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

# Chunked DP with Boundary Conditions

## Problem Statement

You must assign integers `x_1..x_n` in range `[0, M]`. The sequence is divided into chunks of size `K` (last chunk may be smaller). Each chunk must satisfy:

- Sum of values in the chunk is between `L` and `R`.
- The absolute difference between the first and last value of the chunk is at most `D`.

The cost of the sequence is `sum cost_i[x_i]`. Find the minimum total cost.

## Input Format

- First line: integers `n`, `K`, `M`, `L`, `R`, `D`
- Next `n` lines: `M+1` integers: cost table for position `i`

## Output Format

- Single integer: minimum total cost, or `-1` if impossible

## Constraints

- `1 <= n <= 60`
- `1 <= K <= n`
- `0 <= M <= 15`
- `0 <= L <= R <= K * M`
- `0 <= D <= M`

## Clarifying Notes

- Costs are 32-bit signed integers.

## Example Input

```
4 2 2 1 3 1
1 2 3
1 1 1
2 2 2
3 1 0
```

## Example Output

```
4
```
