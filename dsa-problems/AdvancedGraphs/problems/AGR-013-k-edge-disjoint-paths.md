---
problem_id: AGR_K_EDGE_DISJOINT_PATHS__2167
display_id: AGR-013
slug: k-edge-disjoint-paths
title: "K-Edge-Disjoint Paths"
difficulty: Hard
difficulty_score: 68
topics:
  - Graphs
  - Max Flow
  - Disjoint Paths
tags:
  - advanced-graphs
  - disjoint-paths
  - max-flow
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-013: K-Edge-Disjoint Paths

## Problem Statement

Given a directed graph, determine whether there exist at least `k` edge-disjoint paths from `s` to `t`.

![Problem Illustration](../images/AGR-013/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, `s`, `t`, `k`
- Next `m` lines: `u v` describing a directed edge `u -> v`

## Output Format

- Print `YES` if at least `k` edge-disjoint paths exist, otherwise `NO`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `1 <= k <= 10000`
- `0 <= s, t < n`, `s != t`

## Example

**Input:**

```
4 4 0 3 2
0 1
1 3
0 2
2 3
```

**Output:**

```
YES
```

**Explanation:**

Two edge-disjoint paths exist: 0-1-3 and 0-2-3.

![Example Visualization](../images/AGR-013/example-1.png)

## Notes

- Transform to max flow with unit capacities on edges.
- Answer is YES if max flow >= k.
- Use Dinic for performance on large graphs.

## Related Topics

Edge-Disjoint Paths, Max Flow, Dinic

---

## Solution Template

### Java


### Python


### C++


### JavaScript

