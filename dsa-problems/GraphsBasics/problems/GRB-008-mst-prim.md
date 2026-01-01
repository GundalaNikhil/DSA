---
problem_id: GRB_MST_PRIM__9142
display_id: GRB-008
slug: mst-prim
title: "MST Prim"
difficulty: Medium
difficulty_score: 42
topics:
  - Graphs
  - MST
  - Priority Queue
tags:
  - graphs-basics
  - mst
  - prim
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-008: MST Prim

## Problem Statement

Given a connected, undirected weighted graph, compute the total weight of its minimum spanning tree (MST) using Prim's algorithm.

![Problem Illustration](../images/GRB-008/problem-illustration.png)

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

Prim's algorithm selects edges with weights 1 and 2 for total 3.

![Example Visualization](../images/GRB-008/example-1.png)

## Notes

- Use a min-heap keyed by edge weight.
- Track visited nodes to avoid cycles.
- Total MST weight fits in 64-bit integers.

## Related Topics

Minimum Spanning Tree, Prim, Priority Queue

---

## Solution Template

### Java


### Python


### C++


### JavaScript

