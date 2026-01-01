---
problem_id: GRP_ROBOTICS_BRIDGES__4172
display_id: GRP-013
slug: robotics-bridges
title: "Robotics Bridges"
difficulty: Medium
difficulty_score: 60
topics:
  - Graph Theory
  - Bridges
  - Tarjan's Algorithm
  - DFS
tags:
  - graph
  - bridges
  - tarjan
  - dfs
  - critical-edges
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-013: Robotics Bridges

## Problem Statement

Given an undirected graph with `n` nodes (numbered 0 to n-1), find all bridges in the graph.

A **bridge** (or cut edge) is an edge whose removal increases the number of connected components. In other words, removing a bridge disconnects the graph (or a component).

Return a list of all bridges as pairs of nodes.

![Problem Illustration](../images/GRP-013/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- First line: integer `k` (number of bridges)
- Next `k` lines: two integers `u v` representing a bridge edge (output each bridge in sorted order: smaller node first)
- Sort bridges lexicographically

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- There are no self-loops or multiple edges

## Example

**Input:**
```
5
5
0 1
1 2
2 0
1 3
3 4
```

**Output:**
```
2
1 3
3 4
```

**Explanation:**

Graph structure:
- Nodes {0, 1, 2} form a cycle (triangle)
- Node 3 is connected to node 1
- Node 4 is connected to node 3

Bridges:
- Edge (1, 3): Removing it disconnects the triangle {0,1,2} from nodes {3,4}
- Edge (3, 4): Removing it disconnects node 4 from the rest

Edges (0,1), (1,2), (2,0) are NOT bridges because they're part of a cycle.

![Example Visualization](../images/GRP-013/example-1.png)

## Notes

- Use Tarjan's algorithm for finding bridges
- Maintain discovery time and low-link values for each node during DFS
- An edge (u, v) is a bridge if: `low[v] > discovery[u]` (where v is a child of u in DFS tree)
- Low-link value: minimum discovery time reachable from the subtree rooted at that node
- Time complexity: O(n + m)
- Space complexity: O(n)

## Related Topics

Bridges, Tarjan's Algorithm, DFS, Cut Edges, Graph Connectivity

---

## Solution Template

### Java


### Python


### C++


### JavaScript
