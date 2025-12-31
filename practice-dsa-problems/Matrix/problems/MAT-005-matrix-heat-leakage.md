# MAT-005: Matrix Heat Leakage

## Problem Statement

You are given a heat matrix `A` of size `n x m`. At each step, every cell leaks a fixed percentage `P` of its current heat to its 4-directional neighbors. The leakage rule is:

- `leak_total = floor(A[r][c] * P / 100)`
- Each neighbor receives `floor(leak_total / deg)` where `deg` is the number of in-bounds neighbors
- Any remainder stays in the cell

All updates occur simultaneously. After `T` steps, output the final matrix and the total remaining heat.

## Input Format

- First line: integers `n`, `m`, `T`, `P`
- Next `n` lines: `m` integers (initial heat)

## Output Format

- First line: integer `total` (sum of all cells after `T` steps)
- Next `n` lines: `m` integers (final heat matrix)

## Constraints

- `1 <= n, m <= 100`
- `0 <= T <= 1000`
- `0 <= P <= 100`
- `0 <= A[r][c] <= 10^9`

## Clarifying Notes

- Heat values are integers at all times.
- If `deg = 0` (only possible for `n = m = 1`), no leakage occurs.

## Example Input

```
2 2 1 50
4 0
0 0
```

## Example Output

```
4
2 1
1 0
```
