---
problem_id: GRB_ARTICULATION_POINTS_COLORED__1685
display_id: GRB-010
slug: articulation-points-colored
title: "Articulation Points Under Edge Colors"
difficulty: Medium
difficulty_score: 60
topics:
  - Graphs
  - DFS
  - Articulation Points
tags:
  - graphs-basics
  - articulation-points
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-010: Articulation Points Under Edge Colors

## Problem Statement

You are given an undirected graph where each edge is colored `R` (red) or `B` (blue). A node is **critical** if removing it disconnects the graph into components such that at least one component contains a red edge and at least one (different) component contains a blue edge.

Return all critical nodes in increasing order.

![Problem Illustration](../images/GRB-010/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v c` describing an undirected edge with color `c` (`R` or `B`)

## Output Format

- Line 1: integer `k`, number of critical nodes
- Line 2: `k` integers, the critical node indices in increasing order (or empty line if `k=0`)

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`
- `c` is `R` or `B`

## Example

**Input:**

```
5 4
0 2 R
3 4 B
1 0 R
1 3 B
```

**Output:**

```
1
1
```

**Explanation:**

Removing node `1` splits the graph into a red-edge component `{0,2}` and a blue-edge component `{3,4}`.

![Example Visualization](../images/GRB-010/example-1.png)

## Notes

- Use DFS low-link to identify articulation points.
- Track whether each subtree contains red/blue edges to detect color separation.
- A node can be an articulation point without being critical under color rules.

## Related Topics

Articulation Points, DFS, Graph Coloring

---

## Solution Template

### Java


### Python


### C++


### JavaScript

