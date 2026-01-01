---
problem_id: AGR_ARTICULATION_AND_BCC__7358
display_id: AGR-006
slug: articulation-and-bcc
title: "Articulation Points and Biconnected Components"
difficulty: Medium
difficulty_score: 60
topics:
  - Graphs
  - Articulation Points
  - Biconnected Components
tags:
  - advanced-graphs
  - articulation-points
  - bcc
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-006: Articulation Points and Biconnected Components
## Problem Statement
Given an undirected graph, find all articulation points and all vertex-biconnected components (BCCs).
A BCC is a maximal set of vertices that remains connected after removing any single vertex from the set.
![Problem Illustration](../images/AGR-006/problem-illustration.png)
## Input Format
- First line: integers `n` and `m`
- Next `m` lines: `u v` describing an undirected edge
## Output Format
- Line 1: integer `a`, number of articulation points
- Line 2: `a` integers of articulation points in increasing order (or empty line)
- Line 3: integer `b`, number of biconnected components
- Next `b` lines: each BCC as `k v1 v2 ... vk` (vertices in any order)
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
1 3
```
**Output:**
```
1
1
2
3 0 1 2
2 1 3
```
**Explanation:**
Node 1 is an articulation point. The BCCs are {0,1,2} and {1,3}.
![Example Visualization](../images/AGR-006/example-1.png)
## Notes
- Use Tarjan's algorithm with an edge stack to extract BCCs.
- The order of BCCs and vertex order inside each component does not matter.
- The graph may be disconnected.
## Related Topics
Articulation Points, Biconnected Components, DFS
---
## Solution Template
### Java
### Python
### C++
### JavaScript
