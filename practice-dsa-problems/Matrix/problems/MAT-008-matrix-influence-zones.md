# MAT-008: Matrix Influence Zones

## Problem Statement

You are given an `n x m` matrix of non-negative integers. Each cell with value `v > 0` radiates influence within Manhattan distance `D`. The influence contributed by a source to a target cell at distance `d` is:

```
contribution = v * (D - d + 1)  if d <= D
```

Compute the total influence at every cell.

## Input Format

- First line: integers `n`, `m`, `D`
- Next `n` lines: `m` integers (source values)

## Output Format

- `n` lines with `m` integers: the influence field

## Constraints

- `1 <= n, m <= 200`
- `0 <= D <= 200`
- `0 <= value <= 10^6`

## Clarifying Notes

- Distance is Manhattan: `|r1 - r2| + |c1 - c2|`.
- Cells with value 0 contribute nothing.

## Example Input

```
2 3 1
5 0 0
0 0 0
```

## Example Output

```
5 5 0
5 0 0
```
