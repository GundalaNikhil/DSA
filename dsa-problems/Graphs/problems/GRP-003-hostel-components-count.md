---
problem_id: GRP_HOSTEL_COMPONENTS_COUNT__3184
display_id: GRP-003
slug: hostel-components-count
title: "Hostel Components Count"
difficulty: Easy-Medium
difficulty_score: 35
topics:
  - Graph Traversal
  - Connected Components
  - Union-Find
tags:
  - graph
  - connected-components
  - bfs
  - dfs
  - union-find
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-003: Hostel Components Count

## Problem Statement

Given an undirected graph with `n` nodes (numbered from 0 to n-1) and an adjacency list, count the number of connected components in the graph.

A connected component is a maximal set of nodes where every pair of nodes is connected by a path. Two nodes are in the same component if and only if there exists a path between them.

![Problem Illustration](../images/GRP-003/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- Single integer representing the number of connected components

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- There are no self-loops or multiple edges

## Example

**Input:**

```
5
2
0 1
2 3
```

**Output:**

```
3
```

**Explanation:**

The graph has 5 nodes and 2 edges:

- Component 1: {0, 1} - connected by edge (0,1)
- Component 2: {2, 3} - connected by edge (2,3)
- Component 3: {4} - isolated node

Total: 3 connected components

![Example Visualization](../images/GRP-003/example-1.png)

## Notes

- A single isolated node (with no edges) forms its own connected component
- Can be solved using BFS, DFS, or Union-Find (Disjoint Set Union)
- Iterate through all nodes; for each unvisited node, start a BFS/DFS to mark all reachable nodes
- Each time you start a new BFS/DFS, increment the component count
- Time complexity: O(n + m) for BFS/DFS approach

## Related Topics

Connected Components, Graph Traversal, BFS, DFS, Union-Find, Disjoint Set Union

---

## Solution Template

### Java


### Python


### C++


### JavaScript

