# MAT-001: Row Authority Matrix

## Problem Statement

You manage an access-control matrix with `n` rows and `m` columns. Each row has a base authority value. Each column applies one of three dominance rules to every cell in that column:

- Type `0`: no override (cell keeps the row authority value).
- Type `1`: cap with value `c` (cell becomes `min(row_value, c)`).
- Type `2`: force with value `f` (cell becomes exactly `f`).

Compute the final matrix after all rules are applied.

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers: row authorities
- Next `m` lines: `type value` for each column (value is ignored when type = 0)

## Output Format

- `n` lines, each with `m` integers: the final matrix

## Constraints

- `1 <= n, m <= 500`
- `-10^9 <= row_value, value <= 10^9`

## Clarifying Notes

- Column rules apply to all rows independently.
- Type 2 (force) overrides any row value.

## Example Input

```
3 3
10 20 30
0 0
1 15
0 0
```

## Example Output

```
10 10 10
20 15 20
30 15 30
```
