---
problem_id: GRB_DFS_CONNECTED_COMPONENTS__5190
display_id: GRB-002
slug: dfs-connected-components
title: "DFS Connected Components"
difficulty: Easy
difficulty_score: 28
topics:
  - Graphs
  - DFS
  - Components
tags:
  - graphs-basics
  - dfs
  - components
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-002: DFS Connected Components

## Problem Statement

You are given an undirected graph with `n` nodes (0 to `n-1`) and `m` edges. Count the number of connected components and label each node with its component id.

Use depth-first search (DFS) to explore the graph.

![Problem Illustration](../images/GRB-002/problem-illustration.png)

## Input Format

- First line: two integers `n` and `m`
- Next `m` lines: two integers `u` and `v` describing an undirected edge

## Output Format

- Line 1: integer `c`, the number of connected components
- Line 2: `n` integers, `comp[i]` is the component id (1-based) for node `i`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
4 2
0 1
2 3
```

**Output:**

```
2
1 1 2 2
```

**Explanation:**

Nodes `{0,1}` form component 1 and nodes `{2,3}` form component 2.

![Example Visualization](../images/GRB-002/example-1.png)

## Notes

- Components are numbered in the order they are discovered by DFS.
- If `m=0`, each node is its own component.
- An isolated node forms a component of size 1.

## Related Topics

Graph Traversal, DFS, Connected Components

---

## Solution Template

### Java


### Python


### C++


### JavaScript

