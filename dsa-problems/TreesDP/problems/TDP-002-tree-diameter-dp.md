---
problem_id: TDP_TREE_DIAMETER_DP__4829
display_id: TDP-002
slug: tree-diameter-dp
title: "Tree Diameter DP"
difficulty: Medium
difficulty_score: 40
topics:
  - Tree DP
  - DFS
  - Tree Diameter
tags:
  - tree-properties
  - dfs
  - longest-path
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TDP-002: Tree Diameter DP

## Problem Statement

You are given a tree with `n` nodes numbered from 1 to n. The tree is represented by `n-1` edges, where each edge connects two nodes.

Find the **diameter** of the tree, which is defined as the length of the longest path between any two nodes in the tree. The length of a path is the number of edges in the path.

![Problem Illustration](../images/TDP-002/problem-illustration.png)

## Input Format

- First line: Single integer `n` (number of nodes)
- Next `n-1` lines: Two integers `u` and `v` representing an edge between nodes u and v

## Output Format

A single integer representing the diameter of the tree (length of the longest path).

## Constraints

- `2 ≤ n ≤ 2 × 10^5`
- `1 ≤ u, v ≤ n`
- The given edges form a valid tree (connected, acyclic)
- All edge lengths are 1

## Example

**Input:**

```
4
1 2
2 3
3 4
```

**Output:**

```
3
```

**Explanation:**

The tree is a straight line: 1 - 2 - 3 - 4

The longest path is from node 1 to node 4 (or 4 to 1), which has length 3 (passing through edges 1-2, 2-3, 3-4).

Alternatively, we can visualize all paths:

- 1 to 2: length 1
- 1 to 3: length 2
- 1 to 4: length 3 ✓ (maximum)
- 2 to 3: length 1
- 2 to 4: length 2
- 3 to 4: length 1

The diameter is 3.

![Example Visualization](../images/TDP-002/example-1.png)

## Notes

- Use DFS-based dynamic programming to solve in O(n) time
- For each node, track the two deepest paths in its subtree
- The diameter is the maximum sum of two deepest paths across all nodes
- Alternative approach: Run BFS twice (from any node to farthest, then from that node to farthest)

## Related Topics

Tree DP, DFS, Graph Theory, Longest Path

---

## Solution Template

### Java


### Python


### C++


### JavaScript

