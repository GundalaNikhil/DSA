# ARR-019: Split Array into Balanced Energy Segments

## Problem Statement

Given an array `a1..an` and an integer `K`, split the array into exactly `K` non-empty contiguous segments. The **energy** of a segment is the sum of its elements. Your goal is to minimize the maximum segment energy.

Output the minimum possible value of the maximum segment energy.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: minimal possible maximum segment sum

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- All segments must be non-empty and contiguous.
- The optimal split is based on sums, not lengths.

## Example Input

```
5 2
7 2 5 10 8
```

## Example Output

```
18
```
