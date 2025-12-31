# DP-054: DP with Nested Subproblems

## Problem Statement

You must split an array into `k` segments. The score of a segment is the maximum subarray sum within that segment. Maximize the total score across all segments.

## Input Format

- First line: integers `n` and `k`
- Second line: `n` integers: array values

## Output Format

- Single integer: maximum total score

## Constraints

- `1 <= n <= 200`
- `1 <= k <= n`
- `-10^9 <= values <= 10^9`

## Clarifying Notes

- Each segment's inner maximum subarray sum is a DP subproblem.

## Example Input

```
5 2
1 -2 3 -1 2
```

## Example Output

```
5
```
