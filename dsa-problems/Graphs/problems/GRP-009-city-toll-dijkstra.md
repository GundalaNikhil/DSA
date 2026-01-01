---
problem_id: GRP_CITY_TOLL_DIJKSTRA__7561
display_id: GRP-009
slug: city-toll-dijkstra
title: "City Toll Dijkstra"
difficulty: Medium
difficulty_score: 55
topics:
  - Shortest Path
  - Dijkstra
  - Priority Queue
tags:
  - graph
  - dijkstra
  - shortest-path
  - weighted-graph
  - priority-queue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-009: City Toll Dijkstra

## Problem Statement

Given a weighted directed graph with `n` nodes (numbered 0 to n-1), find the shortest path from a source node `s` to all other nodes using Dijkstra's algorithm.

Each edge has a non-negative weight representing the toll/cost. Output the minimum cost to reach each node from the source. If a node is unreachable, output `-1`.

![Problem Illustration](../images/GRP-009/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of directed edges)
- Next `m` lines: three integers `u v w` representing a directed edge from node `u` to node `v` with weight `w`
- Last line: integer `s` (source node)

## Output Format

- Single line with `n` space-separated integers representing the shortest distance from source `s` to nodes 0, 1, 2, ..., n-1

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- `0 <= w <= 10^6`
- `0 <= s < n`
- There are no self-loops or negative weights

## Example

**Input:**
```
4
5
0 1 4
0 2 1
2 1 2
1 3 1
2 3 5
0
```

**Output:**
```
0 3 1 4
```

**Explanation:**

From source node 0:
- To node 0: 0 (source itself)
- To node 1: 3 (path 0→2→1 with cost 1+2=3, better than direct 0→1 with cost 4)
- To node 2: 1 (direct path 0→2)
- To node 3: 4 (path 0→2→1→3 with cost 1+2+1=4)

![Example Visualization](../images/GRP-009/example-1.png)

## Notes

- Use Dijkstra's algorithm with a priority queue (min-heap)
- Initialize all distances to infinity (or a large value), except source which is 0
- Always extract the node with minimum distance from the priority queue
- Relax edges: if distance[u] + weight(u,v) < distance[v], update distance[v]
- Works only with non-negative edge weights
- Time complexity: O((n + m) log n) with binary heap
- Space complexity: O(n + m)

## Related Topics

Dijkstra's Algorithm, Shortest Path, Weighted Graph, Priority Queue, Greedy Algorithm

---

## Solution Template

### Java


### Python


### C++


### JavaScript

