# ARR-008: Distinct Until Repeat

## Problem Statement

Given an array `a1..an`, find the length of the longest prefix that contains no repeated values. The prefix ends right before the first duplicate appears.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: length of the prefix before the first duplicate

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- If the entire array has all distinct values, output `n`.

## Example Input

```
5
5 1 3 5 2
```

## Example Output

```
3
```
