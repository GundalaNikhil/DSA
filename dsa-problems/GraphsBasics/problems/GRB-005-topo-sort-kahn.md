---
problem_id: GRB_TOPO_SORT_KAHN__7394
display_id: GRB-005
slug: topo-sort-kahn
title: "Topological Sort (Kahn)"
difficulty: Easy
difficulty_score: 34
topics:
  - Graphs
  - Topological Sort
  - BFS
tags:
  - graphs-basics
  - topo-sort
  - bfs
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-005: Topological Sort (Kahn)

## Problem Statement

Given a directed acyclic graph (DAG), output any valid topological ordering of its nodes.

![Problem Illustration](../images/GRB-005/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` representing a directed edge `u -> v`

## Output Format

- Single line: `n` integers representing a topological ordering

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`
- The input graph is guaranteed to be a DAG

## Example

**Input:**

```
3 2
0 1
1 2
```

**Output:**

```
0 1 2
```

**Explanation:**

The ordering `0 -> 1 -> 2` respects all edges.

![Example Visualization](../images/GRB-005/example-1.png)

## Notes

- Use Kahn's algorithm with an indegree queue.
- Multiple valid orders may exist; any is accepted.
- Since the graph is a DAG, a full ordering always exists.

## Related Topics

Topological Sort, DAGs, BFS

---

## Solution Template

### Java


### Python


### C++


### JavaScript

