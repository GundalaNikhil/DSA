# ARR-043: Offline Queries with Mo's and Modifications

## Problem Statement

You are given an array `a1..an` and `q` operations of two types:

- `U i x`: update `a[i] = x`
- `Q l r`: query the range `[l, r]`

For a query, define the score of a range as:

```
score = sum( value * (frequency)^2 ) over all distinct values in the range
```

You must output the score for each query in the order they appear. All operations are known in advance, and the intended solution uses Mo's algorithm with modifications.

## Input Format

- First line: integers `n` and `q`
- Second line: `n` integers `a1 a2 ... an`
- Next `q` lines: operations `U` or `Q` as described

## Output Format

- For each `Q` operation, output the score on its own line

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a_i, x <= 10^9`
- `1 <= l <= r <= n`

## Clarifying Notes

- The score uses the current array state after applying all prior updates.
- Distinct values may be large; coordinate compression is allowed.

## Example Input

```
5 5
1 2 1 3 2
Q 1 5
U 2 1
Q 1 3
U 5 1
Q 3 5
```

## Example Output

```
15
9
9
```
