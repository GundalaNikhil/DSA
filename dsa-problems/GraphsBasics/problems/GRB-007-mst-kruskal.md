---
problem_id: GRB_MST_KRUSKAL__2657
display_id: GRB-007
slug: mst-kruskal
title: "MST Kruskal"
difficulty: Medium
difficulty_score: 42
topics:
  - Graphs
  - MST
  - DSU
tags:
  - graphs-basics
  - mst
  - dsu
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-007: MST Kruskal

## Problem Statement

Given a connected, undirected weighted graph, compute the total weight of its minimum spanning tree (MST) using Kruskal's algorithm.

![Problem Illustration](../images/GRB-007/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w` describing an undirected edge with weight `w`

## Output Format

- Single integer: the total weight of the MST

## Constraints

- `1 <= n <= 100000`
- `n-1 <= m <= 200000`
- `0 <= w <= 10^9`
- The graph is connected

## Example

**Input:**

```
3 3
0 1 1
1 2 2
0 2 3
```

**Output:**

```
3
```

**Explanation:**

The MST uses edges (0-1) and (1-2) with total weight 3.

![Example Visualization](../images/GRB-007/example-1.png)

## Notes

- Sort edges by weight and add if they connect different components.
- Use DSU (disjoint set union) with path compression and union by rank.
- The total fits in 64-bit integers.

## Related Topics

Minimum Spanning Tree, Kruskal, DSU

---

## Solution Template

### Java


### Python


### C++


### JavaScript

