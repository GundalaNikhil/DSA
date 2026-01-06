---
problem_id: MAT_MATRIX_DIFF_ENGINE__2592
display_id: NTB-MAT-2592
slug: matrix-diff-engine
title: "Matrix Diff Engine"
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
  - matrix-diff-engine
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix Diff Engine

## Problem Statement

Transform matrix `A` into matrix `B` with minimum cost. Allowed operations:

- Swap any two rows (cost `cr`)
- Swap any two columns (cost `cc`)
- Set a single cell to any value (cost `cs`)

You may apply operations in any order. Compute the minimum total cost.

## Input Format

- First line: integers `n`, `m`
- Second line: integers `cr`, `cc`, `cs`
- Next `n` lines: `m` integers (matrix `A`)
- Next `n` lines: `m` integers (matrix `B`)

## Output Format

- Single integer: minimum cost

## Constraints

- `1 <= n, m <= 6`
- `0 <= cr, cc, cs <= 10^9`
- `-10^9 <= values <= 10^9`

## Clarifying Notes

- A row swap exchanges entire rows; a column swap exchanges entire columns.
- Setting a cell overrides its value regardless of previous swaps.

## Example Input

```
2 2
2 2 1
1 2
3 4
3 4
1 2
```

## Example Output

```
2
```
