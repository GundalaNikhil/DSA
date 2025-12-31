# ARR-006: Rain Buffer Days

## Problem Statement

Given an array `a1..an`, a day `i` is called a **rain buffer day** if:

- `a_i < 0` (rainfall day), and
- `a_{i+1} > 0` and `a_{i+2} > 0` (two positive recovery days)

Count how many rain buffer days exist.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: count of rain buffer days

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Indices `i` with `i+2 > n` cannot be rain buffer days.

## Example Input

```
7
-1 2 3 -4 5 6 7
```

## Example Output

```
2
```
