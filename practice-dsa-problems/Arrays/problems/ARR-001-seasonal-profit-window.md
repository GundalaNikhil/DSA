# ARR-001: Seasonal Profit Window

## Problem Statement

You are given an array `a1..an` of daily profit values (positive or negative). For any subarray, define the **adjusted sum** as:

- If `x >= 0`, contribution is `x`.
- If `x < 0`, contribution is `-ceil(|x| / 2)`.

Your task is to find the maximum adjusted sum over all subarrays of length **at least** `K`.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum adjusted sum among all subarrays of length >= `K`

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- `ceil(|x| / 2)` is computed as `(abs(x) + 1) // 2`.
- The subarray must be contiguous.

## Example Input

```
5 2
3 -4 2 -1 5
```

## Example Output

```
7
```
