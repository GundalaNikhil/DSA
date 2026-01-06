---
problem_id: MAT_COLUMN_DRIFT_DETECTION__4167
display_id: NTB-MAT-4167
slug: column-drift-detection
title: "Column Drift Detection"
difficulty: Medium
difficulty_score: 50
topics:
  - Matrix
tags:
  - 2d-arrays
  - algorithms
  - coding-interviews
  - column-drift-detection
  - data-structures
  - grids
  - matrix
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Column Drift Detection

## Problem Statement

Rows represent time steps `0..n-1`. The adjusted value of each cell is:

```
adjusted[r][c] = a[r][c] + r
```

A column is considered **monotone** if its adjusted values are non-decreasing from row 0 to row `n-1`.

Find the smallest column index (1-based) that violates monotonicity. If all columns are monotone, output `0`.

## Input Format

- First line: integers `n` and `m`
- Next `n` lines: `m` integers `a[r][c]`

## Output Format

- Single integer: the smallest violating column index, or `0`

## Constraints

- `1 <= n, m <= 200000` with `n * m <= 200000`
- `-10^9 <= a[r][c] <= 10^9`

## Clarifying Notes

- The adjusted values use row index starting from 0.

## Example Input

```
3 3
5 3 8
6 1 9
8 0 11
```

## Example Output

```
2
```
