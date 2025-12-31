# ARR-017: Longest Non-Decreasing with One Drop

## Problem Statement

Given an array `a1..an`, find the length of the longest contiguous subarray where the sequence is non-decreasing **except** that you may allow at most one drop. A drop is an index `i` such that `a_i > a_{i+1}`.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum length of a valid subarray

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- A valid subarray may contain zero or one drop.
- Equal consecutive values do not count as drops.

## Example Input

```
6
1 2 5 3 4 6
```

## Example Output

```
6
```
