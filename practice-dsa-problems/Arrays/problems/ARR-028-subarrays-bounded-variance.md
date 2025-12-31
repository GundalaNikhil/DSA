# ARR-028: Subarrays with Bounded Variance

## Problem Statement

Given an array `a1..an` and an integer `K`, count how many subarrays satisfy:

```
max(subarray) - min(subarray) <= K
```

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: number of qualifying subarrays

## Constraints

- `1 <= n <= 200000`
- `0 <= K <= 10^9`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Subarrays are contiguous and non-empty.

## Example Input

```
3 1
1 3 2
```

## Example Output

```
4
```
