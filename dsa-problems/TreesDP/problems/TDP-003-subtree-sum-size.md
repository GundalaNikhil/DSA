---
problem_id: TDP_SUBTREE_SUM_SIZE__3184
display_id: TDP-003
slug: subtree-sum-size
title: "Subtree Sum and Size"
difficulty: Easy
difficulty_score: 25
topics:
  - Tree DP
  - DFS
  - Subtree Queries
tags:
  - tree-traversal
  - aggregation
  - subtree-properties
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TDP-003: Subtree Sum and Size

## Problem Statement

You are given a rooted tree with `n` nodes numbered from 1 to n, where node 1 is the root. Each node has an integer value associated with it.

For each node, compute the **subtree sum**, which is the sum of values of all nodes in the subtree rooted at that node (including the node itself).

Output the subtree sum for each node from 1 to n.

![Problem Illustration](../images/TDP-003/problem-illustration.png)

## Input Format

- First line: Single integer `n` (number of nodes)
- Second line: `n` space-separated integers representing node values (value[1], value[2], ..., value[n])
- Next `n-1` lines: Two integers `u` and `v` representing an edge between nodes u and v

## Output Format

`n` lines, where the i-th line contains the subtree sum for node i.

## Constraints

- `1 ≤ n ≤ 2 × 10^5`
- `-10^9 ≤ value[i] ≤ 10^9`
- `1 ≤ u, v ≤ n`
- The given edges form a valid tree

## Example

**Input:**

```
3
1 2 3
1 2
1 3
```

**Output:**

```
6
2
3
```

**Explanation:**

Tree structure:

```
    1 (value=1)
   / \
  2   3
(v=2) (v=3)
```

- Node 1's subtree: {1, 2, 3}, sum = 1 + 2 + 3 = 6
- Node 2's subtree: {2}, sum = 2
- Node 3's subtree: {3}, sum = 3

![Example Visualization](../images/TDP-003/example-1.png)

## Notes

- Use DFS to traverse the tree and compute subtree sums bottom-up
- Be careful with integer overflow - use long/long long for sums
- The subtree of a leaf node contains only itself
- Root node's subtree sum equals the sum of all node values

## Related Topics

Tree DP, DFS, Aggregation, Bottom-Up DP

---

## Solution Template

### Java


### Python


### C++


### JavaScript

