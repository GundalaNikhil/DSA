---
problem_id: GRP_SEMINAR_BIPARTITE_LOCKED__6927
display_id: GRP-004
slug: seminar-bipartite-check-locked
title: "Seminar Bipartite Check with Locked Nodes"
difficulty: Medium
difficulty_score: 50
topics:
  - Graph Coloring
  - Bipartite Graphs
  - BFS
  - DFS
tags:
  - graph
  - bipartite
  - coloring
  - bfs
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-004: Seminar Bipartite Check with Locked Nodes

## Problem Statement

Given an undirected graph with `n` nodes, determine if the graph can be colored to satisfy bipartite constraints while respecting pre-colored (locked) nodes.

Some nodes are pre-colored either group A (locked value 1) or group B (locked value 2) and cannot change their color. Unlocked nodes (value 0) can be colored either A or B. The graph must satisfy the bipartite property: no two adjacent nodes can have the same color.

Return `true` if a valid coloring exists, `false` otherwise.

![Problem Illustration](../images/GRP-004/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`
- Last line: `n` space-separated integers representing the locked array (0 = unlocked, 1 = force group A, 2 = force group B)

## Output Format

- Single word: `true` if valid bipartite coloring exists, `false` otherwise

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- locked[i] ∈ {0, 1, 2}
- There are no self-loops or multiple edges

## Example

**Input:**

```
4
4
0 1
1 2
2 3
3 0
0 1 0 2
```

**Output:**

```
true
```

**Explanation:**

The graph forms a cycle: 0 - 1 - 2 - 3 - 0

- Node 0: locked to group A (1)
- Node 1: unlocked (0)
- Node 2: unlocked (0)
- Node 3: locked to group B (2)

Valid coloring:

- Node 0: A (locked)
- Node 1: B (to satisfy edge 0-1)
- Node 2: A (to satisfy edge 1-2)
- Node 3: B (locked, and satisfies edges 2-3 and 3-0)

This is a valid bipartite coloring.

![Example Visualization](../images/GRP-004/example-1.png)

## Notes

- Use BFS or DFS for graph coloring
- When visiting a locked node, check if its forced color conflicts with the color it should have based on its parent
- If a locked node's color conflicts with its required color, return false immediately
- For unlocked nodes, assign them the opposite color of their parent
- Handle disconnected components by checking all nodes
- A cycle of odd length cannot be bipartite

## Related Topics

Bipartite Graphs, Graph Coloring, BFS, DFS, Two-Coloring

---

## Solution Template

### Java


### Python


### C++


### JavaScript

