# REC-020: Recursive Undo-Forbidden System

## Problem Statement

You are given a rooted tree where each node has a boolean flag `ok`. A recursive procedure must choose one child to continue at each non-leaf node. If the chosen child eventually fails, you cannot backtrack to siblings.

A node succeeds if all nodes on the chosen root-to-leaf path have `ok = 1`.

Determine if the root succeeds when always choosing the **leftmost** child first.

## Input Format

- First line: integer `n`
- Next `n` lines: `ok parent` (parent is 0 for root)

## Output Format

- `YES` if the root succeeds, otherwise `NO`

## Constraints

- `1 <= n <= 200000`
- `ok` is 0 or 1

## Clarifying Notes

- Children are ordered by node id.
- No backtracking is allowed once a child is chosen.

## Example Input

```
3
1 0
0 1
1 1
```

## Example Output

```
NO
```
