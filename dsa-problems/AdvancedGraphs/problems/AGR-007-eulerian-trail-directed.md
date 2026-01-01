---
problem_id: AGR_EULERIAN_TRAIL_DIRECTED__4836
display_id: AGR-007
slug: eulerian-trail-directed
title: "Eulerian Trail With Directed Edges"
difficulty: Medium
difficulty_score: 48
topics:
  - Graphs
  - Eulerian Path
  - DFS
tags:
  - advanced-graphs
  - eulerian
  - hierholzer
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-007: Eulerian Trail With Directed Edges

## Problem Statement

Determine whether a directed graph has an Eulerian trail (a path that uses every edge exactly once). If it exists, output one such trail.

![Problem Illustration](../images/AGR-007/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` describing a directed edge `u -> v`

## Output Format

- If no Eulerian trail exists: print `NO`
- Otherwise: print `YES` and then one line with the trail as a sequence of `m+1` nodes

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
3 3
0 1
1 2
2 0
```

**Output:**

```
YES
0 1 2 0
```

**Explanation:**

The cycle uses each directed edge exactly once.

![Example Visualization](../images/AGR-007/example-1.png)

## Notes

- A directed Euler trail exists if at most one node has out-in = 1 and at most one node has in-out = 1, and all edges are in one weakly connected component.
- Use Hierholzer's algorithm to construct the trail.
- If `m=0`, output `YES` and any single node (e.g., 0).

## Related Topics

Eulerian Path, Hierholzer, Graph Traversal

---

## Solution Template

### Java


### Python


### C++


### JavaScript

