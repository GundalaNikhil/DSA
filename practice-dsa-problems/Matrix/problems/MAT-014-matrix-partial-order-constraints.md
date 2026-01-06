---
problem_id: MAT_MATRIX_PARTIAL_ORDER_CONSTRAINTS__1846
display_id: NTB-MAT-1846
slug: matrix-partial-order-constraints
title: "Matrix with Partial Order Constraints"
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
  - matrix-partial-order-constraints
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix with Partial Order Constraints

## Problem Statement

You are given an `n x m` matrix of integer ranges. For each cell `(r, c)`, you know a lower bound `L` and upper bound `U` (inclusive). You are also given `k` constraints of the form:

```
cell A <= cell B
```

Your task is to determine whether a valid assignment exists. If it does, output any assignment that satisfies all bounds and constraints.

## Input Format

- First line: integers `n`, `m`, `k`
- Next `n * m` lines: `L U` for each cell in row-major order
- Next `k` lines: `r1 c1 r2 c2` meaning `M[r1][c1] <= M[r2][c2]`

## Output Format

- If impossible: `IMPOSSIBLE`
- Otherwise:
  - `POSSIBLE`
  - `n` lines with `m` integers forming a valid matrix

## Constraints

- `1 <= n, m <= 200`
- `0 <= k <= 200000`
- `-10^9 <= L <= U <= 10^9`

## Clarifying Notes

- Indices are 1-based.
- Constraints may form cycles; cycles imply equality across the cycle.

## Example Input

```
1 2 1
0 5
0 5
1 1 1 2
```

## Example Output

```
POSSIBLE
0 0
```
