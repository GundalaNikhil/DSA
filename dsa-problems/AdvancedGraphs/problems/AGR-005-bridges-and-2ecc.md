---
problem_id: AGR_BRIDGES_AND_2ECC__3471
display_id: AGR-005
slug: bridges-and-2ecc
title: "Bridges and 2-Edge-Connected Components"
difficulty: Medium
difficulty_score: 54
topics:
  - Graphs
  - Bridges
  - Components
tags:
  - advanced-graphs
  - bridges
  - components
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-005: Bridges and 2-Edge-Connected Components
## Problem Statement
Given an undirected graph, find all bridges and compute the 2-edge-connected components (2ECCs). A 2ECC is a maximal set of nodes that stays connected after removing any single edge.
![Problem Illustration](../images/AGR-005/problem-illustration.png)
## Input Format
- First line: integers `n` and `m`
- Next `m` lines: `u v` describing an undirected edge
## Output Format
- Line 1: integer `b`, number of bridges
- Next `b` lines: each bridge edge `u v` in input order
- Last line: `n` integers `comp[i]` (1-based component id)
## Constraints
- `1 <= n <= 200000`
- `0 <= m <= 200000`
- `0 <= u, v < n`
## Example
**Input:**
```
4 4
0 1
1 2
2 0
2 3
```
**Output:**
```
1
2 3
1 1 1 2
```
**Explanation:**
Edge (2,3) is a bridge. Nodes {0,1,2} form one 2ECC, node {3} is another.
![Example Visualization](../images/AGR-005/example-1.png)
## Notes
- Use DFS low-link to detect bridges.
- Build components by unioning all non-bridge edges.
- Output bridge edges in their input order.
## Related Topics
Bridges, 2-Edge-Connected Components, DFS
---
## Solution Template
### Java
### Python
### C++
### JavaScript
