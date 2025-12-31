# ARR-014: Subarray Score = min x length

## Problem Statement

Given an array `a1..an`, define the score of a subarray as:

```
score = (minimum value in the subarray) * (subarray length)
```

Find the maximum possible score across all subarrays.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum subarray score

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Subarrays are contiguous and non-empty.
- The minimum value can be negative, which may produce a negative score.

## Example Input

```
4
2 2 1 3
```

## Example Output

```
4
```
