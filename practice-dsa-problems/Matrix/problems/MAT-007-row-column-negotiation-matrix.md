# MAT-007: Row-Column Negotiation Matrix

## Problem Statement

Each row proposes a value for all its cells. Each column has a minimum acceptable value and a cap. For each cell `(r, c)`:

- If `row_value < col_min`, the negotiation fails for that cell.
- Otherwise the final value is `min(row_value, col_cap)`.

Compute the final matrix and the number of failed cells.

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers: row proposals
- Next `m` lines: `col_min col_cap` for each column

## Output Format

- First line: integer `failures`
- Next `n` lines: `m` integers, using `-1` for failed cells

## Constraints

- `1 <= n, m <= 500`
- `-10^9 <= values <= 10^9`

## Clarifying Notes

- A cell fails only if `row_value < col_min`.
- A column cap can be less than the row value.

## Example Input

```
3 3
10 20 30
5 15
15 25
0 35
```

## Example Output

```
1
10 10 10
15 20 20
15 25 30
```
