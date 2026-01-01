---
problem_id: AGR_DIRECTED_CYCLE_BASIS__8240
display_id: AGR-015
slug: directed-cycle-basis
title: "Directed Cycle Basis"
difficulty: Hard
difficulty_score: 72
topics:
  - Graphs
  - Cycle Basis
  - Spanning Forest
tags:
  - advanced-graphs
  - cycle-basis
  - directed
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-015: Directed Cycle Basis

## Problem Statement

Given a directed graph, output a cycle basis of size `m - n + c`, where `c` is the number of connected components in the underlying undirected graph.

Each cycle should be a simple directed cycle. Any valid basis is accepted.

![Problem Illustration](../images/AGR-015/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` describing a directed edge `u -> v`

## Output Format

- Line 1: integer `b`, number of cycles output
- Next `b` lines: each cycle as `k v1 v2 ... vk` where `v1 == vk` (cycle closed)

## Constraints

- `1 <= n <= 500`
- `0 <= m <= 2000`
- `0 <= u, v < n`

## Example

**Input:**

```
4 5
0 1
1 2
2 0
1 3
3 1
```

**Output:**

```
2
4 0 1 2 0
3 1 3 1
```

**Explanation:**

Two independent directed cycles are shown. This is a valid basis.

![Example Visualization](../images/AGR-015/example-1.png)

## Notes

- Build a spanning forest on the underlying undirected graph.
- Each non-tree edge creates a fundamental cycle via parent pointers.
- Any valid basis size is accepted.

## Related Topics

Cycle Basis, Spanning Forest, Graph Theory

---

## Solution Template

### Java


### Python


### C++


### JavaScript

