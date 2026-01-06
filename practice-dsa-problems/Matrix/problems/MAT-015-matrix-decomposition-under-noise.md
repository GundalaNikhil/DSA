---
problem_id: MAT_MATRIX_DECOMPOSITION_UNDER_NOISE__4177
display_id: NTB-MAT-4177
slug: matrix-decomposition-under-noise
title: "Matrix Decomposition Under Noise"
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
  - matrix-decomposition-under-noise
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix Decomposition Under Noise

## Problem Statement

Given an `n x n` integer matrix `A`, find a symmetric matrix `B` that minimizes:

```
error = sum |A[i][j] - B[i][j]| over all i, j
```

If multiple `B` achieve the same minimum error, choose the one where for each pair `(i, j)` with `i < j`:

```
B[i][j] = B[j][i] = min(A[i][j], A[j][i])
```

Output the matrix `B` and the minimum error.

## Input Format

- First line: integer `n`
- Next `n` lines: `n` integers (matrix `A`)

## Output Format

- First line: integer `error`
- Next `n` lines: `n` integers (matrix `B`)

## Constraints

- `1 <= n <= 500`
- `-10^9 <= A[i][j] <= 10^9`

## Clarifying Notes

- For diagonal entries, `B[i][i] = A[i][i]`.

## Example Input

```
2
1 5
2 4
```

## Example Output

```
3
1 2
2 4
```
