---
title: Tree DP for Vertex Cover
problem_id: TDP_TREE_VERTEX_COVER__7514
display_id: TDP-006
difficulty: Medium
time_limit: 2000
memory_limit: 256
tags:
  - Tree DP
  - Graph Theory
  - Optimization
categories:
  - Algorithms
  - Data Structures
slug: tree-vertex-cover
---

# Tree DP for Vertex Cover

## Problem Description

Given a tree with `n` nodes, find the size of the **minimum vertex cover**.

A vertex cover is a set of vertices such that every edge in the tree has at least one of its endpoints in the set.

## Input Format

- First line: integer `n` (number of nodes)
- Next `n-1` lines: each contains two integers `u v` representing an edge

## Output Format

- Single integer: the size of the minimum vertex cover

## Constraints

- `1 <= n <= 2 x 10^5`
- `1 <= u, v <= n`
- The graph forms a valid tree

## Example 1

**Input:**

```
3
1 2
1 3
```

**Output:**

```
1
```

**Explanation:**
Tree structure:

```
  1
 / \
2   3
```

Vertex cover = {1} covers both edges (1-2) and (1-3).
Size = 1 (minimum possible).

## Example 2

**Input:**

```
4
1 2
2 3
3 4
```

**Output:**

```
2
```

**Explanation:**
Tree structure: 1 -- 2 -- 3 -- 4

Possible minimum vertex covers:

- {2, 3} covers edges (1-2), (2-3), and (3-4)
- Size = 2

Alternatively: {1, 3} or {2, 4} also work.

## Solution Template

### Java


### Python


### C++


### JavaScript


## Notes

- dp[u][0] = minimum cover size for subtree of u when u is NOT included
- dp[u][1] = minimum cover size for subtree of u when u IS included
- When u is not included, all children must be included
- When u is included, children can be included or not (take minimum)
