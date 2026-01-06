---
problem_id: MAT_MATRIX_CONSISTENCY_CONCURRENT_UPDATES__2568
display_id: NTB-MAT-2568
slug: matrix-consistency-concurrent-updates
title: "Matrix Consistency Under Concurrent Updates"
difficulty: Medium
difficulty_score: 50
topics:
  - Matrix
tags:
  - 2d-arrays
  - algorithms
  - coding-interviews
  - data-structures
  - grids
  - matrix
  - matrix-consistency-concurrent-updates
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix Consistency Under Concurrent Updates

## Problem Statement

You are given a schedule of read and write operations on matrix cells, performed by multiple threads. Determine whether the schedule is conflict-serializable.

Two operations conflict if they access the same cell and at least one is a write. A schedule is conflict-serializable if its precedence graph is acyclic.

## Input Format

- First line: integers `n`, `m`, `q`
- Next `q` lines: `thread_id op r c` where `op` is `R` or `W`

## Output Format

- `SERIALIZABLE` if the schedule is conflict-serializable, otherwise `NOT_SERIALIZABLE`

## Constraints

- `1 <= n, m <= 200`
- `1 <= q <= 200000`
- `1 <= thread_id <= 200000`

## Clarifying Notes

- The matrix values themselves are irrelevant; only access patterns matter.
- Operations are given in execution order.

## Example Input

```
2 2 4
1 R 1 1
2 W 1 1
1 W 1 2
2 R 1 2
```

## Example Output

```
NOT_SERIALIZABLE
```
