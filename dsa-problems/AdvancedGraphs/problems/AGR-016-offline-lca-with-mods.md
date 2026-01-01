---
problem_id: AGR_OFFLINE_LCA_WITH_MODS__9025
display_id: AGR-016
slug: offline-lca-with-mods
title: "Offline Lowest Common Ancestor with Modifications"
difficulty: Hard
difficulty_score: 72
topics:
  - Graphs
  - Trees
  - LCA
tags:
  - advanced-graphs
  - lca
  - offline
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-016: Offline Lowest Common Ancestor with Modifications
## Problem Statement
You are given an initial tree on `n` nodes rooted at node `0`. Then you must process a sequence of operations:
- `cut u v`: remove the edge between `u` and `v`
- `link u v`: add an edge between `u` and `v`
- `query u v`: output the LCA of `u` and `v` in the current tree
If `u` and `v` are not connected, output `-1`.
All operations are valid, and the active edge set always forms a forest.
![Problem Illustration](../images/AGR-016/problem-illustration.png)
## Input Format
- First line: integer `n`
- Next `n-1` lines: `u v` edges of the initial tree
- Next line: integer `q`
- Next `q` lines: one of the operations above
## Output Format
- For each `query`, print the LCA value on its own line
## Constraints
- `1 <= n <= 200000`
- `1 <= q <= 200000`
- `0 <= u, v < n`
- Operations are valid and keep the active edges acyclic
## Example
**Input:**
```
4
0 1
1 2
1 3
4
query 2 3
cut 1 3
query 2 3
link 1 3
```
**Output:**
```
1
-1
```
**Explanation:**
Initially, LCA(2,3)=1. After removing edge (1,3), nodes 2 and 3 are disconnected.
![Example Visualization](../images/AGR-016/example-1.png)
## Notes
- Solve offline using a segment tree over time for edge activation intervals.
- Use DSU rollback for dynamic connectivity, and binary lifting for LCA in the base tree.
- Treat LCA as undefined if nodes are disconnected.
## Related Topics
LCA, DSU Rollback, Offline Queries
---
## Solution Template
### Java
### Python
### C++
### JavaScript
