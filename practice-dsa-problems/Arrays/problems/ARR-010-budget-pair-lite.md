---
problem_id: ARR_BUDGET_PAIR_LITE__4682
display_id: NTB-ARR-4682
slug: budget-pair-lite
title: "Budget Pair Lite"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - budget-pair-lite
  - coding-interviews
  - data-structures
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Budget Pair Lite

## Problem Statement

Given an array `a1..an`, a target sum `T`, and a maximum allowed difference `D`, find a pair of indices `(i, j)` such that:

- `i < j`
- `a_i + a_j = T`
- `|a_i - a_j| <= D`

Among all valid pairs, choose the one with the smallest `i`, and if tied, the smallest `j`. If no valid pair exists, output `-1`.

## Input Format

- First line: integers `n`, `T`, and `D`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- If a pair exists: output two integers `i j`
- Otherwise: output `-1`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i, T <= 10^9`
- `0 <= D <= 10^9`

## Clarifying Notes

- Indices are 1-based in the output.
- Each index can be used at most once.

## Example Input

```
5 5 3
1 4 7 3 2
```

## Example Output

```
4 5
```
