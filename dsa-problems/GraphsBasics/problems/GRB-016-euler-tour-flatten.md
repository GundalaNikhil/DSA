---
problem_id: GRB_EULER_TOUR_FLATTEN__5068
display_id: GRB-016
slug: euler-tour-flatten
title: "Euler Tour of Tree (Array Flatten)"
difficulty: Medium
difficulty_score: 44
topics:
  - Graphs
  - Trees
  - DFS
  - Euler Tour
tags:
  - graphs-basics
  - euler-tour
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-016: Euler Tour of Tree (Array Flatten)

## Problem Statement

You are given a rooted tree with `n` nodes. Produce the entry time `tin[u]` and exit time `tout[u]` for each node using a DFS Euler tour. The subtree of `u` corresponds to the contiguous range `[tin[u], tout[u]]` in the Euler order.

![Problem Illustration](../images/GRB-016/problem-illustration.png)

## Input Format

- First line: integer `n`
- Next `n-1` lines: `u v` describing an undirected edge
- Last line: integer `r`, the root node

## Output Format

- Line 1: `n` integers `tin[0..n-1]`
- Line 2: `n` integers `tout[0..n-1]`

## Constraints

- `1 <= n <= 200000`
- `0 <= u, v, r < n`

## Example

**Input:**

```
3
0 1
0 2
0
```

**Output:**

```
0 1 2
2 1 2
```

**Explanation:**

A DFS from root 0 visits nodes in order 0,1,2. The subtree of 0 covers indices 0..2.

![Example Visualization](../images/GRB-016/example-1.png)

## Notes

- Use a global timer that increments on entry.
- `tout[u]` is the last time index inside `u`'s subtree.
- The exact times depend on DFS order; any valid Euler tour is accepted.

## Related Topics

Euler Tour, Tree Flattening, DFS

---

## Solution Template

### Java


### Python


### C++


### JavaScript

