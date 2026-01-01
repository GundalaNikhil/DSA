---
problem_id: REC_RESTORE_MATRIX_UPPER_BOUNDS__2607
display_id: REC-010
slug: restore-matrix-upper-bounds
title: "Restore Matrix With Upper Bounds"
difficulty: Medium
difficulty_score: 56
topics:
  - Recursion
  - Backtracking
  - Matrices
tags:
  - recursion
  - backtracking
  - matrix
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-010: Restore Matrix With Upper Bounds
## Problem Statement
You are given row sums, column sums, and per-cell upper bounds `u[i][j]` for an `r x c` matrix of non-negative integers.
Construct any matrix that satisfies all row sums, column sums, and bounds. If no matrix exists, output `NONE`.
![Problem Illustration](../images/REC-010/problem-illustration.png)
## Input Format
- First line: integers `r` and `c`
- Second line: `r` space-separated row sums
- Third line: `c` space-separated column sums
- Next `r` lines: `c` space-separated upper bounds `u[i][j]`

## Output Format

- If possible, output `r` lines each with `c` integers of a valid matrix
- Otherwise output `NONE`

## Constraints

- `1 <= r, c <= 6`
- `0 <= rowSum[i], colSum[j] <= 20`
- `0 <= u[i][j] <= 20`

## Example

**Input:**

```
2 2
3 4
4 3
2 3
3 4
```

**Output:**

```
2 1
2 2
```

**Explanation:**

Row sums: 2+1=3, 2+2=4. Column sums: 2+2=4, 1+2=3. All values respect bounds.

![Example Visualization](../images/REC-010/example-1.png)

## Notes

- Fill cells row by row with recursion
- Prune when any row or column sum becomes negative
- Bounds reduce the branching factor
- Any valid matrix is acceptable

## Related Topics

Backtracking, Constraint Satisfaction, Recursion

---

## Solution Template
### Java


### Python


### C++


### JavaScript

