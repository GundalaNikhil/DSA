---
title: Restore Matrix With Upper Bounds
slug: restore-matrix-upper-bounds
difficulty: Medium
difficulty_score: 56
tags:
- Recursion
- Backtracking
- Matrix
problem_id: REC_RESTORE_MATRIX_UPPER_BOUNDS__2607
display_id: REC-010
topics:
- Recursion
- Backtracking
- Matrices
---
# Restore Matrix With Upper Bounds - Editorial

## Problem Summary

You need to construct an `R x C` matrix of non-negative integers such that:
1.  The sum of the `i`-th row equals `rowSums[i]`.
2.  The sum of the `j`-th column equals `colSums[j]`.
3.  Each cell `matrix[i][j]` is between `0` and `bounds[i][j]` inclusive.

If multiple solutions exist, any one is acceptable. If none exist, output `NONE`.


## Constraints

- `1 <= r, c <= 6`
- `0 <= rowSum[i], colSum[j] <= 20`
- `0 <= u[i][j] <= 20`
## Real-World Scenario

Imagine **Supply Chain Management**. You have `R` factories and `C` warehouses.
-   Factory `i` produces exactly `rowSums[i]` units.
-   Warehouse `j` demands exactly `colSums[j]` units.
-   The shipping route from Factory `i` to Warehouse `j` has a capacity limit of `bounds[i][j]`.
You need to determine how much to ship on each route to satisfy all supply and demand within capacity limits.

## Problem Exploration

### 1. Constraints
-   `R, C <= 6`: Very small dimensions. Total cells `<= 36`.
-   Sums and bounds `<= 20`: Small values.
-   This suggests backtracking is feasible, but we need to be smart about pruning.

### 2. Recursive Structure
We can fill the matrix cell by cell, say from `(0,0)` to `(R-1, C-1)`.
At cell `(r, c)`, we need to decide a value `v`.
-   **Lower Bound**: `0`.
-   **Upper Bound**: `bounds[r][c]`.
-   **Row Constraint**: `v` cannot exceed the remaining sum needed for row `r`.
-   **Column Constraint**: `v` cannot exceed the remaining sum needed for column `c`.

So, `v` can range from `0` to `min(bounds[r][c], remaining_row_sum[r], remaining_col_sum[c])`.

### 3. Pruning
-   **Lookahead**: After picking `v` for `(r, c)`, is it possible to satisfy the rest?
    -   If we are at the end of a row (column `C-1`), the value is fixed: it *must* be exactly `remaining_row_sum[r]`. If this value is invalid (negative or > bound or > remaining_col_sum), backtrack.
    -   Similarly, if at the end of a column (row `R-1`), value is fixed by column sum.
-   **Feasibility Check**: At any point, if `remaining_row_sum[i]` > sum of bounds of remaining cells in row `i`, it's impossible. (This might be too expensive to check every step, but simple checks help).

## Approaches

### Approach 1: Backtracking with Pruning
We iterate through cells `(0,0) -> (0,1) -> ... -> (0, C-1) -> (1,0) -> ...`.
At each cell `(r, c)`:
1.  Determine valid range for `val`: `[0, min(bounds[r][c], rowSums[r], colSums[c])]`.
2.  Iterate `val` in this range (try largest first? or smallest? Greedy approach works for simple "Restore Matrix" without bounds, but with bounds, we might need specific values. Trying largest first often satisfies sums quicker but might violate future bounds. Let's try descending).
3.  Update `rowSums[r]` and `colSums[c]`.
4.  Recurse to next cell.
5.  Backtrack (restore sums).

**Optimization**:
-   If `c == C-1`: We *must* pick `val = rowSums[r]`. Check if valid. If so, recurse.
-   If `r == R-1`: We *must* pick `val = colSums[c]`. Check if valid. If so, recurse.

### Approach 2: Max Flow (Network Flow)
This problem can be modeled as a Max Flow problem with demands and capacity constraints.
-   Source -> Rows (capacity `rowSum`).
-   Rows -> Cols (capacity `bound`).
-   Cols -> Sink (capacity `colSum`).
-   Check if max flow equals total row sum (and total col sum).
Given the constraints (`N <= 6`), backtracking is easier to implement during an interview than a full Max Flow algorithm (Dinic/Edmonds-Karp).

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
RowSums: `[3, 4]`
ColSums: `[4, 3]`
Bounds:
`2 3`
`3 4`

1.  `backtrack(0, 0)`:
    -   `maxVal = min(2, 3, 4) = 2`.
    -   Try `val = 2`.
    -   `matrix[0][0] = 2`. `rSums[0]=1`, `cSums[0]=2`.
    -   Recurse `backtrack(0, 1)`.
2.  `backtrack(0, 1)` (Last col):
    -   `val = rSums[0] = 1`.
    -   Check: `1 <= bounds[0][1]=3` (OK), `1 <= cSums[1]=3` (OK).
    -   `matrix[0][1] = 1`. `rSums[0]=0`, `cSums[1]=2`.
    -   Recurse `backtrack(1, 0)`.
3.  `backtrack(1, 0)`:
    -   `maxVal = min(3, 4, 2) = 2`. (Note: `cSums[0]` is now 2).
    -   Try `val = 2`.
    -   `matrix[1][0] = 2`. `rSums[1]=2`, `cSums[0]=0`.
    -   Recurse `backtrack(1, 1)`.
4.  `backtrack(1, 1)` (Last col):
    -   `val = rSums[1] = 2`.
    -   Check: `2 <= bounds[1][1]=4` (OK), `2 <= cSums[1]=2` (OK).
    -   `matrix[1][1] = 2`. `rSums[1]=0`, `cSums[1]=0`.
    -   Recurse `backtrack(2, 0)`.
5.  `backtrack(2, 0)`:
    -   `r == R`. Check `cSums`: `[0, 0]`. All zero.
    -   Return `true`.

**Result:**
`2 1`
`2 2`

## Proof of Correctness

The backtracking algorithm fills the matrix cell by cell.
-   **Validity**: At each step, we ensure the chosen value respects the cell's upper bound and does not exceed the remaining required sum for the current row or column.
-   **Completeness**: By iterating from `maxVal` down to `0`, we explore possible assignments. The optimization for the last column ensures we exactly meet the row sum requirement, pruning invalid branches early.
-   **Termination**: The recursion depth is `R x C`, which is small.

## Interview Extensions

1.  **Minimize the maximum value in the matrix?**
    -   Binary search on the answer `K`. For a fixed `K`, check if a valid matrix exists where `bounds[i][j]` is effectively `min(bounds[i][j], K)`.

2.  **Large R, C?**
    -   Use Max Flow. Create a source connected to rows, columns connected to sink. Edges between row `i` and col `j` have capacity `bounds[i][j]`. Check if max flow saturates source edges.

### Common Mistakes

-   **Greedy Failure**: Simply picking `min(rowSum, colSum)` works for unbounded matrices but fails here because it might consume too much capacity needed for other cells.
-   **Bound Checking**: Forgetting to check `val <= bounds[i][j]`.
