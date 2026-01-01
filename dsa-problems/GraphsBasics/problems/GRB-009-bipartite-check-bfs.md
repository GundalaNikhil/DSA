---
problem_id: GRB_BIPARTITE_CHECK_BFS__5073
display_id: GRB-009
slug: bipartite-check-bfs
title: "Bipartite Check BFS"
difficulty: Easy
difficulty_score: 36
topics:
  - Graphs
  - BFS
  - Bipartite
tags:
  - graphs-basics
  - bipartite
  - bfs
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-009: Bipartite Check BFS

## Problem Statement

Given an undirected graph, determine whether it is bipartite. If it is bipartite, output a valid 2-coloring. Otherwise, output `false`.

![Problem Illustration](../images/GRB-009/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` describing an undirected edge

## Output Format

- If bipartite: print `true` on line 1 and a line of `n` integers (`0` or `1`) for node colors
- If not bipartite: print `false`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
3 3
0 1
1 2
2 0
```

**Output:**

```
false
```

**Explanation:**

A triangle has an odd cycle, so it is not bipartite.

![Example Visualization](../images/GRB-009/example-1.png)

## Notes

- The graph may be disconnected; check each component.
- Use BFS coloring with two colors.
- Any valid coloring is accepted.

## Related Topics

Bipartite Graph, BFS, Coloring

---

## Solution Template

### Java


### Python


### C++


### JavaScript

