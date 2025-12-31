# ARR-041: Persistent Prefix Maximum Queries

## Problem Statement

You are given an initial array `a1..an` and must support versioned updates and queries.

- Version `0` is the initial array.
- Each update creates a new version with exactly one element changed.

Operations:

- `U v i x`: create a new version based on version `v` where `a[i] = x`.
- `Q v r`: return the maximum value in prefix `a[1..r]` of version `v`.

Output the answer for every query.

## Input Format

- First line: integers `n` and `q`
- Second line: `n` integers `a1 a2 ... an`
- Next `q` lines: operations `U` or `Q` as described

## Output Format

- For each `Q` operation, output a single integer on its own line

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a_i, x <= 10^9`
- `1 <= i <= n`
- `1 <= r <= n`

## Clarifying Notes

- Updates do not modify earlier versions.
- Version IDs are 0-based and update operations create the next version ID in order.
- The intended data structure is a persistent segment tree.

## Example Input

```
5 4
1 3 -2 4 0
Q 0 3
U 0 2 10
Q 1 4
Q 0 5
```

## Example Output

```
3
10
4
```
