---
problem_id: GRP_CAMPUS_MAP_BFS__4821
display_id: GRP-001
slug: campus-map-bfs
title: "Campus Map BFS"
difficulty: Easy
difficulty_score: 25
topics:
  - Graph Traversal
  - Breadth-First Search
  - Queue
tags:
  - graph
  - bfs
  - traversal
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-001: Campus Map BFS

## Problem Statement

Given an undirected unweighted graph represented by `n` nodes (numbered from 0 to n-1) and an adjacency list, perform a Breadth-First Search (BFS) starting from node 0 and return the order in which nodes are visited.

The graph is represented as an adjacency list where each node may have zero or more neighbors. You must traverse the graph level by level, visiting all nodes at distance `k` before visiting any nodes at distance `k+1`.

![Problem Illustration](../images/GRP-001/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- Single line with space-separated integers representing the order of nodes visited during BFS starting from node 0

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- The graph may be disconnected
- There are no self-loops or multiple edges

## Example

**Input:**
```
4
3
0 1
0 2
1 3
```

**Output:**
```
0 1 2 3
```

**Explanation:**

Starting from node 0:
- Level 0: Visit node 0
- Level 1: Visit nodes 1 and 2 (neighbors of 0, in the order they appear in adjacency list)
- Level 2: Visit node 3 (neighbor of 1)

The BFS traversal visits nodes in order: 0 → 1 → 2 → 3

![Example Visualization](../images/GRP-001/example-1.png)

## Notes

- Use a queue data structure to maintain the FIFO order of traversal
- Use a visited array/set to track which nodes have been explored to avoid revisiting
- If the graph is disconnected, only nodes reachable from node 0 will be visited
- The order of neighbors in the adjacency list determines the order of visitation when multiple nodes are at the same level
- Nodes that are not reachable from node 0 will not appear in the output

## Related Topics

Graph Traversal, BFS, Queue, Visited Set, Level Order Traversal

---

## Solution Template

### Java


### Python


### C++


### JavaScript

