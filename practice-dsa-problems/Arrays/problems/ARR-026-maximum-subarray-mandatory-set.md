# ARR-026: Maximum Subarray with Mandatory Inclusion Set

## Problem Statement

You are given an array `a1..an` and a set `S` of `m` distinct values. A subarray is **valid** if it contains at least one occurrence of every value in `S`.

Find the maximum sum among all valid subarrays. If no valid subarray exists, output `IMPOSSIBLE`.

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers `a1 a2 ... an`
- Third line: `m` distinct integers: the set `S`

## Output Format

- Single line: maximum valid subarray sum, or `IMPOSSIBLE`

## Constraints

- `1 <= n <= 200000`
- `1 <= m <= n`
- `-10^9 <= a_i <= 10^9`
- `-10^9 <= S_i <= 10^9`

## Clarifying Notes

- Subarrays are contiguous and non-empty.
- `S` values are distinct but may appear multiple times in the array.

## Example Input

```
7 2
2 -1 3 2 -4 3 1
2 3
```

## Example Output

```
6
```
