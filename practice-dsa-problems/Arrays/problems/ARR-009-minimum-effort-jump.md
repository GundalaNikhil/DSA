# ARR-009: Minimum Effort Jump

## Problem Statement

You are given an array `e1..en` of non-negative effort costs and an integer `K`. You start at index 1 and want to reach index `n`. From position `i`, you may jump to any `j` such that `1 <= j - i <= K`.

The total effort is the sum of `e` values at all visited indices, including the start and the end. Find the minimum possible total effort to reach index `n`.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `e1 e2 ... en`

## Output Format

- Single integer: minimum total effort to reach index `n`

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- `0 <= e_i <= 10^9`

## Clarifying Notes

- You must start at index 1 and finish at index `n`.
- Jumps must always move forward.

## Example Input

```
5 2
1 3 2 5 1
```

## Example Output

```
4
```
