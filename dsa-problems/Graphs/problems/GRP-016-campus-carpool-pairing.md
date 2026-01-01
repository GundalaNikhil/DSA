---
problem_id: GRP_CAMPUS_CARPOOL_PAIRING__2914
display_id: GRP-016
slug: campus-carpool-pairing
title: "Campus Carpool Pairing"
difficulty: Medium
difficulty_score: 45
topics:
  - Graph Theory
  - Cycle Detection
  - Union-Find
  - Forest
tags:
  - graph
  - cycle-detection
  - union-find
  - forest
  - tree
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-016: Campus Carpool Pairing

## Problem Statement

Given an undirected graph with `n` nodes (numbered 0 to n-1) and `m` edges, determine if the graph is a **forest**.

A **forest** is a graph with no cycles. Equivalently, it's a collection of trees where each tree is a connected acyclic graph. An isolated node (with no edges) is considered a tree of size 1.

Return `true` if the graph is a forest (has no cycles), `false` otherwise.

![Problem Illustration](../images/GRP-016/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- Single word: `true` if the graph is a forest (no cycles), `false` otherwise

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- There are no self-loops or multiple edges

## Example

**Input:**
```
3
2
0 1
1 2
```

**Output:**
```
true
```

**Explanation:**

Graph structure:
```
0 --- 1 --- 2
```

This is a simple path (a tree) with no cycles, so it's a forest.

Output: `true`

![Example Visualization](../images/GRP-016/example-1.png)

## Notes

- A forest has no cycles
- For a graph to be a forest, it must satisfy: `m < n` (number of edges < number of nodes)
- If `m >= n`, at least one cycle must exist (pigeonhole principle)
- Use Union-Find (DSU) to detect cycles:
  - Process each edge (u, v)
  - If u and v are already in the same component, adding this edge creates a cycle
  - If they're in different components, union them
- Alternatively, use DFS with parent tracking (same as undirected cycle detection)
- Time complexity: O(m × α(n)) for Union-Find, O(n + m) for DFS

## Related Topics

Forest, Trees, Cycle Detection, Union-Find, DFS, Acyclic Graph

---

## Solution Template

### Java


### Python


### C++


### JavaScript
