---
problem_id: GRP_LAB_NETWORK_DFS__5729
display_id: GRP-002
slug: lab-network-dfs
title: "Lab Network DFS"
difficulty: Easy
difficulty_score: 25
topics:
  - Graph Traversal
  - Depth-First Search
  - Recursion
tags:
  - graph
  - dfs
  - traversal
  - recursion
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-002: Lab Network DFS

## Problem Statement

Given an undirected graph represented by `n` nodes (numbered from 0 to n-1) and an adjacency list, perform a Depth-First Search (DFS) in preorder starting from node 0 and return the visited nodes in the order they were first encountered.

DFS explores as far as possible along each branch before backtracking. The preorder means we record a node when we first visit it, not when we backtrack from it.

![Problem Illustration](../images/GRP-002/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: integer `m` (number of edges)
- Next `m` lines: two integers `u v` representing an undirected edge between nodes `u` and `v`

## Output Format

- Single line with space-separated integers representing the preorder DFS traversal starting from node 0

## Constraints

- `1 <= n <= 10^5`
- `0 <= m <= 2*10^5`
- `0 <= u, v < n`
- The graph may be disconnected
- There are no self-loops or multiple edges

## Example

**Input:**
```
5
3
0 1
0 2
1 4
```

**Output:**
```
0 1 4 2
```

**Explanation:**

Starting from node 0:
- Visit node 0 (record it)
- Go to neighbor 1 (first neighbor in adjacency list)
- Visit node 1 (record it)
- Go to neighbor 4 (only unvisited neighbor of 1)
- Visit node 4 (record it)
- Backtrack to 1, then to 0
- Go to neighbor 2 (next unvisited neighbor of 0)
- Visit node 2 (record it)

The DFS preorder traversal is: 0 → 1 → 4 → 2

![Example Visualization](../images/GRP-002/example-1.png)

## Notes

- Can be implemented recursively (using call stack) or iteratively (using explicit stack)
- Use a visited array/set to track which nodes have been explored
- If the graph is disconnected, only nodes reachable from node 0 will be visited
- The order of neighbors in the adjacency list determines which branch to explore first
- Preorder means recording the node when first visited, not during backtracking

## Related Topics

Graph Traversal, DFS, Recursion, Stack, Backtracking

---

## Solution Template

### Java


### Python


### C++


### JavaScript

