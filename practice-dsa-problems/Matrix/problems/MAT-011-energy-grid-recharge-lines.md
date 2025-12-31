# MAT-011: Energy Grid with Recharge Lines

## Problem Statement

You are given an `n x m` grid of base energy values, a recharge value for each row, and a drain value for each column. The net energy of cell `(r, c)` is:

```
net = base[r][c] + row_recharge[r] + col_drain[c]
```

A cell remains active if `net >= 0`.

Compute the number of active cells and output the active grid as `1` (active) or `0` (inactive).

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers: row recharge values
- Third line: `m` integers: column drain values
- Next `n` lines: `m` integers (base energy grid)

## Output Format

- First line: integer `active_count`
- Next `n` lines: `m` integers (0 or 1)

## Constraints

- `1 <= n, m <= 2000` with `n * m <= 200000`
- `-10^9 <= values <= 10^9`

## Clarifying Notes

- Column drain values can be negative (meaning extra recharge).

## Example Input

```
2 3
10 20
-5 -15 -25
0 0 0
0 0 0
```

## Example Output

```
4
1 1 0
1 1 0
```
