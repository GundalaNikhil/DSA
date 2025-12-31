# ARR-031: Online Array with Rollbacks

## Problem Statement

You are given an array `a1..an` and must process `q` operations online:

- `SET i x`: set `a_i = x`
- `SUM l r`: output the sum of `a_l..a_r`
- `UNDO`: undo the most recent `SET` operation that has not already been undone

Process operations in order and output answers for `SUM` queries.

## Input Format

- First line: integers `n` and `q`
- Second line: `n` integers `a1 a2 ... an`
- Next `q` lines: one operation per line

## Output Format

- For each `SUM` operation, output the sum on its own line

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a_i, x <= 10^9`
- `1 <= i <= n`
- `1 <= l <= r <= n`

## Clarifying Notes

- `UNDO` always refers to a previous `SET` that has not been undone.
- `SUM` queries should reflect all applied and not-yet-undone updates.

## Example Input

```
3 5
1 2 3
SUM 1 3
SET 2 5
SUM 2 3
UNDO
SUM 2 3
```

## Example Output

```
6
8
5
```
