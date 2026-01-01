---
problem_id: GRB_BFS_SHORTEST_PATH_UNWEIGHTED__4821
display_id: GRB-001
slug: bfs-shortest-path-unweighted
title: "BFS Shortest Path in Unweighted Graph"
difficulty: Easy
difficulty_score: 25
topics:
  - Graphs
  - BFS
  - Shortest Path
tags:
  - graphs-basics
  - bfs
  - shortest-path
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRB-001: BFS Shortest Path in Unweighted Graph

## Problem Statement

You are given an undirected, unweighted graph with `n` nodes (numbered from `0` to `n-1`) and `m` edges. You need to find the shortest path distance from a source node `s` to all other nodes in the graph.

In an unweighted graph, each edge has the same weight (you can think of it as weight 1). The shortest path between two nodes is the path with the minimum number of edges.

If a node is not reachable from the source, its distance should be `-1`.

![Problem Illustration](../images/GRB-001/problem-illustration.png)

## Input Format

- First line: Three integers `n`, `m`, and `s` — the number of nodes, number of edges, and source node.
- Next `m` lines: Two integers `u` and `v` representing an undirected edge between nodes `u` and `v`.

## Output Format

Print `n` space-separated integers representing the shortest distance from node `s` to nodes `0, 1, 2, ..., n-1`.

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= s < n`
- `0 <= u, v < n`
- No self-loops or multiple edges between the same pair of nodes

## Example

**Input:**

```
4 3 0
0 1
1 2
0 3
```

**Output:**

```
0 1 2 1
```

**Explanation:**

Starting from node 0:

- Distance to node 0 = 0 (itself)
- Distance to node 1 = 1 (direct edge: 0 → 1)
- Distance to node 2 = 2 (path: 0 → 1 → 2)
- Distance to node 3 = 1 (direct edge: 0 → 3)

![Example Visualization](../images/GRB-001/example-1.png)

## Notes

- The graph is undirected, so edge (u, v) means you can travel from u to v and from v to u.
- BFS (Breadth-First Search) naturally finds shortest paths in unweighted graphs.
- Make sure to handle disconnected components (nodes unreachable from source should have distance -1).

## Related Topics

Graphs, BFS, Queue, Shortest Path

---

## Solution Template

### Java


### Python


### C++


### JavaScript

