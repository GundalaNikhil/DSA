# REC-032: Recursive Quorum Decisions

## Problem Statement

You are given a rooted tree. Each node has a quorum requirement `q`.

Define the recursive decision `Decide(node)`:

- If the node is a leaf, return its fixed vote `v` (0 or 1).
- Otherwise, evaluate all children and count how many return 1.
- The node returns 1 if the count is at least `q`, otherwise 0.

Compute the root decision.

## Input Format

- First line: integer `n`
- Next `n` lines: `q v parent` (parent is 0 for root)
  - For internal nodes, `v` is ignored.

## Output Format

- Single integer: `0` or `1`

## Constraints

- `1 <= n <= 200000`
- `0 <= q <= 200000`
- `v` is `0` or `1`

## Clarifying Notes

- If a node has fewer children than its quorum `q`, it returns `0`.
- Quorum is evaluated independently at each node.

## Example Input

```
4
2 0 0
0 1 1
0 0 1
0 1 1
```

## Example Output

```
1
```
