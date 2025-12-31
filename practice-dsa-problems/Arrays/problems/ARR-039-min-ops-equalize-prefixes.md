# ARR-039: Minimum Operations to Equalize Prefixes

## Problem Statement

You are given an array `a1..an` and a target value `T`. You may apply the following operations:

1. `INC i`: increment all elements in prefix `[1..i]` by 1.
2. `ROT i`: rotate the prefix `[1..i]` left by 1 (cyclic shift).

Your goal is to make every prefix sum equal to `i * T` for all `i = 1..n`. This is equivalent to making every element equal to `T`.

Find the minimum number of operations required. If it is impossible, output `-1`.

## Input Format

- First line: integers `n` and `T`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: minimum number of operations, or `-1` if impossible

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i, T <= 10^9`

## Clarifying Notes

- Only increments are allowed; values can never decrease.
- If any `a_i > T`, the answer is `-1`.

## Example Input

```
4 3
3 3 3 3
```

## Example Output

```
0
```
