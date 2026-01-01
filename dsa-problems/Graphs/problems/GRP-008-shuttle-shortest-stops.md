---
problem_id: GRP_SHUTTLE_SHORTEST_STOPS__9247
display_id: GRP-008
slug: shuttle-shortest-stops
title: "Shuttle Shortest Stops"
difficulty: Easy-Medium
difficulty_score: 35
topics:
  - Graph Traversal
  - BFS
  - Shortest Path
tags:
  - graph
  - bfs
  - shortest-path
  - unweighted
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-008: Shuttle Shortest Stops

## Problem Statement

Given an unweighted undirected graph with `n` nodes (numbered 0 to n-1) and a source node `s`, find the shortest distance (in number of edges) from the source to all other nodes.

For each node, output its shortest distance from the source. If a node is unreachable from the source, output `-1` for that node.

![Problem Illustration](../images/GRP-008/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`
- Last line: integer `s` (source node)

## Output Format

- Single line with `n` space-separated integers representing the shortest distance from source `s` to nodes 0, 1, 2, ..., n-1

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- `0 <= s < n`
- There are no self-loops or multiple edges

## Example

**Input:**
```
5
4
0 1
1 2
0 3
3 4
0
```

**Output:**
```
0 1 2 1 2
```

**Explanation:**

Starting from node 0 (source):
- Distance to node 0: 0 (source itself)
- Distance to node 1: 1 (direct edge 0→1)
- Distance to node 2: 2 (path 0→1→2)
- Distance to node 3: 1 (direct edge 0→3)
- Distance to node 4: 2 (path 0→3→4)

![Example Visualization](../images/GRP-008/example-1.png)

## Notes

- Use BFS (Breadth-First Search) to find shortest paths in unweighted graphs
- Initialize all distances to -1, then set source distance to 0
- BFS guarantees that nodes are visited in increasing order of distance from source
- Time complexity: O(n + m)
- Space complexity: O(n) for queue and distance array

## Related Topics

BFS, Shortest Path, Unweighted Graph, Level Order Traversal

---

## Solution Template

### Java


### Python


### C++


### JavaScript

