---
problem_id: AGR_BIPARTITE_MIN_COST_VERTEX_COVER__3406
display_id: AGR-010
slug: bipartite-min-cost-vertex-cover
title: "Minimum Cost Vertex Cover in Bipartite Graph"
difficulty: Medium
difficulty_score: 56
topics:
  - Graphs
  - Vertex Cover
  - Min Cut
tags:
  - advanced-graphs
  - vertex-cover
  - min-cut
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-010: Minimum Cost Vertex Cover in Bipartite Graph

## Problem Statement

You are given a bipartite graph with left part `U` and right part `V`. Each vertex has a non-negative weight. Find the minimum total weight vertex cover.

A vertex cover is a set of vertices such that every edge has at least one endpoint in the set.

![Problem Illustration](../images/AGR-010/problem-illustration.png)

## Input Format

- First line: integers `nU`, `nV`, and `m`
- Second line: `nU` integers, weights for `U`
- Third line: `nV` integers, weights for `V`
- Next `m` lines: `u v` describing an edge between `u` in `U` and `v` in `V`

## Output Format

- Single integer: minimum total weight of a vertex cover

## Constraints

- `1 <= nU + nV <= 100000`
- `0 <= m <= 200000`
- `0 <= weight <= 10^9`
- `0 <= u < nU`, `0 <= v < nV`

## Example

**Input:**

```
2 2 3
3 1
2 2
0 0
1 0
1 1
```

**Output:**

```
3
```

**Explanation:**

Choosing `U1` (weight 1) and `V0` (weight 2) covers all edges with total weight 3.

![Example Visualization](../images/AGR-010/example-1.png)

## Notes

- Reduce to a min-cut: source->U edges with capacity weight, V->sink edges with capacity weight, U->V edges with capacity INF.
- The minimum cut value equals the minimum vertex cover weight (Kőnig's theorem).
- Use 64-bit integers for capacities.

## Related Topics

Vertex Cover, Min Cut, Bipartite Graphs

---

## Solution Template

### Java


### Python


### C++


### JavaScript

