---
problem_id: REC_RECURSIVE_STATE_COMPRESSION__9481
display_id: NTB-REC-9481
slug: recursive-state-compression
title: "Recursive State Compression"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - recursion
  - recursive-state-compression
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive State Compression

## Problem Statement

You are given an array `a[1..n]`. A recursive reduction replaces any contiguous segment by its sum modulo `M`. The recursion continues until a single value remains.

You are only allowed to pass down the **segment sum modulo `M`** and the segment length to deeper calls. Determine whether it is possible to reduce the array to value `0`.

## Input Format

- First line: integers `n` and `M`
- Second line: `n` integers: array values

## Output Format

- `YES` if reduction to 0 is possible, otherwise `NO`

## Constraints

- `1 <= n <= 30`
- `1 <= M <= 10`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- You may choose any split point at each recursive step.

## Example Input

```
3 5
1 2 2
```

## Example Output

```
YES
```
