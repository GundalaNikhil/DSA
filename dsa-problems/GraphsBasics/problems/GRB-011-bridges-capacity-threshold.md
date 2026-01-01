---
problem_id: GRB_BRIDGES_CAPACITY_THRESHOLD__4509
display_id: GRB-011
slug: bridges-capacity-threshold
title: "Bridges With Capacity Threshold"
difficulty: Medium
difficulty_score: 55
topics:
  - Graphs
  - Bridges
  - DFS
tags:
  - graphs-basics
  - bridges
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-011: Bridges With Capacity Threshold

## Problem Statement

You are given an undirected graph where each edge has a capacity `c`. An edge is **critical** if:

1. It is a bridge (removing it increases the number of connected components), and
2. Its capacity is strictly less than a threshold `T`.

Find all such edges.

![Problem Illustration](../images/GRB-011/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, and `T`
- Next `m` lines: `u v c` describing an undirected edge with capacity `c`

## Output Format

- Line 1: integer `k`, number of critical edges
- Next `k` lines: `u v` for each critical edge in the order they appear in input

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= c <= 10^9`
- `0 <= T <= 10^9`
- `0 <= u, v < n`

## Example

**Input:**

```
4 4 3
0 1 1
1 2 5
2 0 1
1 3 2
```

**Output:**

```
1
1 3
```

**Explanation:**

Edge (1,3) is a bridge and has capacity 2 < 3.

![Example Visualization](../images/GRB-011/example-1.png)

## Notes

- Use DFS low-link to detect bridges.
- The order of output edges must match their input order.
- If no edges qualify, print `0` and nothing else.

## Related Topics

Bridges, DFS, Graph Connectivity

---

## Solution Template

### Java


### Python


### C++


### JavaScript

