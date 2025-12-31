# ARR-024: Array Game with Penalties

## Problem Statement

You are given an array `a1..an` and an integer `K`. You start at index 1 with score `a1` and must reach index `n`. From index `i`, you may jump to any `j` such that `1 <= j - i <= K`.

Your score is the sum of values at all visited indices. Negative values reduce the score. Find the maximum possible score to reach index `n`.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum achievable score at index `n`

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- You must start at index 1 and end at index `n`.
- Jumps must always move forward.

## Example Input

```
5 2
1 -5 4 -2 3
```

## Example Output

```
8
```
