# ARR-044: Max Sum Rectangle Reduced to 1D Arrays

## Problem Statement

You are given a matrix with `n` rows and `m` columns. Find the maximum possible sum of any non-empty axis-aligned rectangular submatrix.

The intended solution reduces the 2D problem into multiple 1D maximum subarray computations by fixing row pairs.

## Input Format

- First line: integers `n` and `m`
- Next `n` lines: `m` integers each, the matrix values

## Output Format

- Single integer: maximum submatrix sum

## Constraints

- `1 <= n, m <= 400`
- `-10^9 <= value <= 10^9`

## Clarifying Notes

- The rectangle must contain at least one cell.
- The answer can be negative if all values are negative.

## Example Input

```
3 3
1 -2 3
-1 4 -2
2 -1 2
```

## Example Output

```
6
```
