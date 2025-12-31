# ARR-023: Longest Zigzag Subarray

## Problem Statement

Given an array `a1..an`, find the length of the longest contiguous subarray where consecutive differences strictly alternate in sign.

Formally, for a subarray `a_l..a_r`, the differences `(a_{i+1} - a_i)` for `i = l..r-1` must be non-zero and must alternate between positive and negative.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: length of the longest zigzag subarray

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- A subarray of length 1 is always zigzag.
- Zero difference breaks the zigzag condition.

## Example Input

```
7
1 3 2 4 3 5 6
```

## Example Output

```
6
```
