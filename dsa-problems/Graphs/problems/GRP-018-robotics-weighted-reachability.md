---
problem_id: GRP_ROBOTICS_WEIGHTED_REACH__9571
display_id: GRP-018
slug: robotics-weighted-reachability
title: "Robotics Weighted Reachability"
difficulty: Medium
difficulty_score: 50
topics:
  - Weighted Graph
  - BFS
  - DFS
  - Union-Find
tags:
  - graph
  - weighted-graph
  - reachability
  - bfs
  - dfs
  - union-find
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-018: Robotics Weighted Reachability

## Problem Statement

Given a weighted undirected graph with `n` nodes (numbered 0 to n-1), edges with positive weights, and a threshold `T`, count how many nodes are reachable from node 0 using only edges with weight `<= T`.

An edge (u, v, w) can be traversed if and only if `w <= T`. Count all nodes that can be reached from node 0 through such valid edges.

![Problem Illustration](../images/GRP-018/problem-illustration.png)

## Input Format

- First line: two integers `n T` (number of nodes and threshold)
- Second line: integer `m` (number of edges)
- Next `m` lines: three integers `u v w` representing an undirected edge between nodes `u` and `v` with weight `w`

## Output Format

- Single integer: number of nodes reachable from node 0 using only edges with weight `<= T` (including node 0 itself)

## Constraints

- `1 <= n <= 10^5`
- `1 <= m <= 2*10^5`
- `0 <= u, v < n`
- `1 <= w <= 10^9`
- `0 <= T <= 10^9`

## Example

**Input:**
```
5 4
4
0 1 3
1 2 7
0 3 2
3 4 5
```

**Output:**
```
3
```

**Explanation:**

Graph edges:
- (0, 1) with weight 3 ≤ 4 ✓ (valid)
- (1, 2) with weight 7 > 4 ✗ (invalid)
- (0, 3) with weight 2 ≤ 4 ✓ (valid)
- (3, 4) with weight 5 > 4 ✗ (invalid)

Reachable nodes from node 0 using edges with weight ≤ 4:
- Node 0 (starting point)
- Node 1 (via edge 0-1 with weight 3)
- Node 3 (via edge 0-3 with weight 2)

Nodes 2 and 4 are not reachable because:
- Node 2 requires edge (1,2) with weight 7 > 4
- Node 4 requires edge (3,4) with weight 5 > 4

Total reachable: 3 nodes

![Example Visualization](../images/GRP-018/example-1.png)

## Notes

- Filter edges to include only those with weight ≤ T
- Run BFS or DFS from node 0 on the filtered graph
- Count all visited nodes
- Alternative approach: Use Union-Find
  - Sort edges by weight
  - Union nodes connected by edges with weight ≤ T
  - Return size of component containing node 0
- Time complexity: O(m log m) for sorting + O(m × α(n)) for Union-Find, or O(n + m) for BFS/DFS

## Related Topics

Weighted Graph, Reachability, BFS, DFS, Union-Find, Edge Filtering

---

## Solution Template

### Java


### Python


### C++


### JavaScript
