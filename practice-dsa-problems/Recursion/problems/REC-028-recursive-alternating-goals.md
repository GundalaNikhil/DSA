# REC-028: Recursive Alternating Goals

## Problem Statement

You are given a rooted tree where each node has a value. Define a recursive evaluation with alternating goals:

- At even depth (root depth 0), a node returns the maximum of its children's results.
- At odd depth, a node returns the minimum of its children's results.
- A leaf node returns its own value.

Compute the value returned by the root.

## Input Format

- First line: integer `n`
- Next `n` lines: `value parent` (parent is 0 for root)

## Output Format

- Single integer: root value

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= value <= 10^9`

## Clarifying Notes

- If an internal node has only one child, the max/min is that child's value.
- Depth is measured from the root.

## Example Input

```
5
3 0
1 1
4 1
2 2
6 2
```

## Example Output

```
2
```
