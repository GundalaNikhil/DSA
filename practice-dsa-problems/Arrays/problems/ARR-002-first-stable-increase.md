# ARR-002: First Stable Increase

## Problem Statement

Given an array `a1..an`, find the smallest index `i` (1-based) such that:

```
a_i < a_{i+1} < a_{i+2} < a_{i+3}
```

This represents three consecutive day-to-day increases. If no such index exists, output `-1`.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: the smallest valid index `i`, or `-1`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- A valid sequence requires four consecutive values with three strict increases.
- Indices are 1-based in the output.

## Example Input

```
7
5 6 7 4 5 6 7
```

## Example Output

```
4
```
