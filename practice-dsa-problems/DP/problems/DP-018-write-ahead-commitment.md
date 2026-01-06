---
problem_id: DP_WRITE_AHEAD_COMMITMENT__8617
display_id: NTB-DP-8617
slug: write-ahead-commitment
title: "DP with Write-Ahead Commitment"
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
  - technical-interview-prep
  - write-ahead-commitment
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Write-Ahead Commitment

## Problem Statement

You must plan actions in blocks of size `K`. Before executing a block, you must commit to its sequence. You cannot change the sequence mid-block.

Each action `i` has cost `c_i`. You must perform exactly `n` actions (n is divisible by `K`). Minimize total cost.

## Input Format

- First line: integers `n`, `K`, `a`
- Second line: `a` integers: costs `c_1..c_a`
- Third line: integer `b` (number of allowed blocks)
- Next `b` lines: sequences of length `K` (action ids)

## Output Format

- Single integer: minimum total cost, or `-1` if impossible

## Constraints

- `1 <= n <= 200`
- `1 <= K <= n`
- `n % K == 0`
- `1 <= a <= 20`
- `1 <= b <= 200`

## Clarifying Notes

- Each block must be chosen from the allowed block list.

## Example Input

```
4 2 3
3 1 2
2
1 2
2 3
```

## Example Output

```
6
```
