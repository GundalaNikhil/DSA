---
problem_id: REC_RECURSIVE_BATCHING__7216
display_id: NTB-REC-7216
slug: recursive-batching
title: "Recursive Batching"
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
  - recursive-batching
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Batching

## Problem Statement

You are given an array of length `n` and a batch size `B`. Define a recursive function `Batch(l, r)`:

- If `r - l + 1 <= B`, return `max(A[l..r]) - min(A[l..r])`.
- Otherwise, partition `[l, r]` into consecutive batches of size `B` (the last batch may be smaller), compute `Batch` on each batch, and return the maximum of those results.

Compute `Batch(1, n)`.

## Input Format

- First line: integers `n` and `B`
- Second line: `n` integers `A[i]`

## Output Format

- Single integer: value of `Batch(1, n)`

## Constraints

- `1 <= n <= 200000`
- `1 <= B <= n`
- `-10^9 <= A[i] <= 10^9`

## Clarifying Notes

- Batches must be contiguous and processed in order.
- You cannot rebalance or merge batches across boundaries.

## Example Input

```
7 3
5 1 9 2 6 3 4
```

## Example Output

```
8
```
