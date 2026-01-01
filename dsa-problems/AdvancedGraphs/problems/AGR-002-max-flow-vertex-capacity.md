---
problem_id: AGR_MAX_FLOW_VERTEX_CAPACITY__5913
display_id: AGR-002
slug: max-flow-vertex-capacity
title: "Max Flow With Vertex Capacities"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - Max Flow
  - Vertex Capacities
tags:
  - advanced-graphs
  - max-flow
  - vertex-capacity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-002: Max Flow With Vertex Capacities

## Problem Statement

You are given a directed graph with edge capacities and **vertex capacities**. Compute the maximum flow from source `s` to sink `t` while respecting both edge and vertex limits.

A vertex with capacity `C` can carry at most `C` units of flow through it. The source and sink have unlimited capacity.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186940/dsa-problems/AGR-002/problem/cunfjp4k77gbrhhghgms.jpg)

## Input Format

- First line: integers `n`, `m`, `s`, `t`
- Second line: `n` integers `cap[i]` (`-1` means infinite capacity)
- Next `m` lines: `u v c` describing a directed edge `u -> v` with capacity `c`

## Output Format

- Single integer: maximum flow from `s` to `t`

## Constraints

- `2 <= n <= 2000`
- `0 <= m <= 5000`
- `0 <= c <= 10^9`
- `cap[i] = -1` or `0 <= cap[i] <= 10^9`
- `0 <= s, t < n`, `s != t`

## Example

**Input:**

```
4 3 0 3
-1 3 2 -1
0 1 3
1 2 2
2 3 3
```

**Output:**

```
2
```

**Explanation:**

Vertex 2 limits the flow to 2, so the max flow is 2.

![Example Visualization](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186943/dsa-problems/AGR-002/problem/zssufeqz99vcroa175c6.jpg)

## Notes

- Split each vertex into `in` and `out` with an edge of its capacity.
- Use a max flow algorithm like Dinic on the transformed graph.
- Treat `cap[s]` and `cap[t]` as infinite.

## Related Topics

Max Flow, Vertex Capacities, Dinic

---

## Solution Template

### Java


### Python


### C++


### JavaScript

