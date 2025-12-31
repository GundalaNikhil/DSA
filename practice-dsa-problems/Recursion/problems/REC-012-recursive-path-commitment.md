# REC-012: Recursive Path Commitment

## Problem Statement

You are given a rooted tree with node values. A committed recursion chooses exactly one child at each non-leaf node and continues recursively. Once a child is chosen, all siblings are ignored forever (no backtracking).

Find the maximum sum of values along a root-to-leaf path of **exact length** `L` (number of nodes). If no such path exists, output `-1`.

## Input Format

- First line: integers `n` and `L`
- Next `n` lines: `value parent` (parent is 0 for root)

## Output Format

- Single integer: maximum path sum of length `L`, or `-1`

## Constraints

- `1 <= n <= 200000`
- `1 <= L <= n`
- Values are 32-bit signed integers

## Clarifying Notes

- Path length counts nodes, not edges.

## Example Input

```
4 3
5 0
3 1
2 1
4 2
```

## Example Output

```
12
```
