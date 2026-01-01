---
problem_id: TDP_LCA_BINARY_LIFTING__7291
display_id: TDP-001
slug: lca-binary-lifting
title: "Lowest Common Ancestor (Binary Lifting)"
difficulty: Medium
difficulty_score: 45
topics:
  - Tree DP
  - Binary Lifting
  - LCA
tags:
  - preprocessing
  - tree-traversal
  - ancestors
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TDP-001: Lowest Common Ancestor (Binary Lifting)

## Problem Statement

You are given a rooted tree with `n` nodes numbered from 1 to n. Node 1 is the root. The tree is represented by `n-1` edges, where each edge connects two nodes.

You need to preprocess the tree and then answer `q` queries. Each query asks for the Lowest Common Ancestor (LCA) of two nodes `u` and `v`.

The Lowest Common Ancestor of two nodes is the deepest (farthest from root) node that is an ancestor of both nodes.

![Problem Illustration](../images/TDP-001/problem-illustration.png)

## Input Format

- First line: Two integers `n` and `q` (number of nodes and number of queries)
- Next `n-1` lines: Two integers `u` and `v` representing an edge between nodes u and v
- Next `q` lines: Two integers `u` and `v` representing a query for LCA(u, v)

## Output Format

For each query, output a single integer representing the LCA of the two given nodes.

## Constraints

- `1 ≤ n ≤ 2 × 10^5`
- `1 ≤ q ≤ 2 × 10^5`
- `1 ≤ u, v ≤ n`
- The given edges form a valid tree
- All queries are independent

## Example

**Input:**

```
7 3
1 2
1 3
2 4
2 5
3 6
3 7
4 5
2 3
6 7
```

**Output:**

```
2
1
3
```

**Explanation:**

The tree structure:

```
       1
      / \
     2   3
    / \ / \
   4  5 6  7
```

Query 1: LCA(4, 5) = 2 (node 2 is the parent of both 4 and 5)
Query 2: LCA(2, 3) = 1 (node 1 is the parent of both 2 and 3)
Query 3: LCA(6, 7) = 3 (node 3 is the parent of both 6 and 7)

![Example Visualization](../images/TDP-001/example-1.png)

## Notes

- Use binary lifting to achieve O(log n) time complexity per query
- Preprocess the tree in O(n log n) time
- The root node (node 1) is its own ancestor
- If one node is an ancestor of another, the LCA is the ancestor node itself

## Related Topics

Tree DP, Binary Search, Preprocessing, Graph Traversal

---

## Solution Template

### Java


### Python


### C++


### JavaScript

