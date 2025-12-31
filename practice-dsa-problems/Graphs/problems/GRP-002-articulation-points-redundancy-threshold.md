# GRP-002: Articulation Points with Redundancy Threshold

## Problem Statement

You are given a connected, undirected graph with `n` nodes and `m` edges, and an integer percentage `X` (0 to 100). For a node `v`, remove `v` and all incident edges. Let the remaining graph split into components with sizes `s1, s2, ...` and let `s_max` be the largest component size.

Node `v` is **critical** if more than `X` percent of the remaining nodes are **not** in the largest component:

```
(n - 1 - s_max) * 100 > X * (n - 1)
```

Your task is to output all critical nodes in ascending order.

## Input Format

- First line: integers `n`, `m`, and `X`
- Next `m` lines: edges `u v`

## Output Format

- If there are no critical nodes, output a single line `0`.
- Otherwise, output:
  - First line: the number of critical nodes
  - Second line: their indices in ascending order, separated by spaces

## Constraints

- `1 <= n, m <= 200000`
- `0 <= X <= 100`
- `1 <= u, v <= n`

## Clarifying Notes

- The graph is connected before any removals.
- The intended solution uses articulation points (Tarjan) plus component size tracking.

## Example Input

```
5 4 40
1 2
2 3
3 4
3 5
```

## Example Output

```
1
3
```
