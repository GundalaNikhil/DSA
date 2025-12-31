# ARR-018: Circular Peak Detection

## Problem Statement

Given a circular array `a1..an`, an index `i` is a **peak** if `a_i` is strictly greater than both its circular neighbors. Neighbors wrap around, so `a_1` is adjacent to `a_n` and `a_2`.

Count the number of peaks.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: number of peaks

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- For `n = 1`, the single element is a peak.
- For `n = 2`, `a_1` is a peak if `a_1 > a_2`, and `a_2` is a peak if `a_2 > a_1`.

## Example Input

```
4
1 3 2 4
```

## Example Output

```
2
```
