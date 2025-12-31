# ARR-011: Maximum Subarray with Cooldown

## Problem Statement

You are given an array `a1..an` and an integer `X`. You may select one or more non-overlapping subarrays. If you select a subarray that ends at index `r`, the next selected subarray must start at index `r + X + 1` or later (cooldown of `X` elements).

Find the maximum total sum of selected subarrays. You must select at least one subarray.

## Input Format

- First line: integers `n` and `X`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum total sum under the cooldown rule

## Constraints

- `1 <= n <= 200000`
- `0 <= X <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Subarrays must be contiguous and non-overlapping.
- The cooldown applies between any two consecutive chosen subarrays.

## Example Input

```
6 1
4 -1 3 -2 5 -1
```

## Example Output

```
11
```
