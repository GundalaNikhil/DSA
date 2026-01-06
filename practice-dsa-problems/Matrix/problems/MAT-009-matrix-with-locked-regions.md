---
problem_id: MAT_MATRIX_WITH_LOCKED_REGIONS__1116
display_id: NTB-MAT-1116
slug: matrix-with-locked-regions
title: "Matrix with Locked Regions"
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
  - matrix-with-locked-regions
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix with Locked Regions

## Problem Statement

You are given a matrix and a list of locked rectangles. An update adds a value `delta` to every cell in a rectangle, but locked cells are never modified.

For each update, report how many locked cells were skipped. After all updates, output the final matrix.

## Input Format

- First line: integers `n`, `m`, `L`, `q`
- Next `n` lines: `m` integers (initial matrix)
- Next `L` lines: `r1 c1 r2 c2` (1-based locked rectangles, inclusive)
- Next `q` lines: `r1 c1 r2 c2 delta` (updates)

## Output Format

- For each update: one line with the number of locked cells skipped
- After all updates: `n` lines with `m` integers (final matrix)

## Constraints

- `1 <= n, m <= 200`
- `0 <= L, q <= 200000`
- `-10^9 <= values, delta <= 10^9`

## Clarifying Notes

- Locked rectangles may overlap; any cell covered by at least one lock is immutable.

## Example Input

```
2 2 1 1
1 2
3 4
1 1 1 1
1 1 2 2 5
```

## Example Output

```
1
1 7
8 9
```
