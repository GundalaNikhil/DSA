---
problem_id: MAT_MATRIX_FLOW_CONSERVATION__5034
display_id: NTB-MAT-5034
slug: matrix-flow-conservation
title: "Matrix with Flow Conservation"
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
  - matrix-flow-conservation
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix with Flow Conservation

## Problem Statement

You are given an `n x m` matrix of non-negative values. Each operation moves an amount between adjacent cells.

Operation format:

```
MOVE r1 c1 r2 c2 x
```

The move is valid only if `(r1, c1)` and `(r2, c2)` are 4-directional neighbors and `A[r1][c1] >= x`.

Find the first invalid operation. If all operations are valid, output `0` and the final matrix.

## Input Format

- First line: integers `n`, `m`, `q`
- Next `n` lines: `m` integers (initial matrix)
- Next `q` lines: operations

## Output Format

- If an operation is invalid: output its 1-based index
- Otherwise: output `0` and the final matrix

## Constraints

- `1 <= n, m <= 200`
- `0 <= A[r][c] <= 10^9`
- `1 <= q <= 200000`
- `0 <= x <= 10^9`

## Clarifying Notes

- Total sum must remain constant if all operations are valid.

## Example Input

```
2 2 2
5 0
0 0
MOVE 1 1 1 2 3
MOVE 1 1 2 1 3
```

## Example Output

```
2
```
