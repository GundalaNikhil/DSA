---
problem_id: AGR_BIPARTITE_MATCHING_NODE_CAPACITY__8194
display_id: AGR-009
slug: bipartite-matching-node-capacity
title: "Maximum Matching with Node Capacities"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - Bipartite Matching
  - Max Flow
tags:
  - advanced-graphs
  - bipartite-matching
  - max-flow
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-009: Maximum Matching with Node Capacities

## Problem Statement

You are given a bipartite graph with left part `U` and right part `V`. Each node `u` in `U` has capacity `capU[u]` (maximum number of matches it can take), and each node `v` in `V` has capacity `capV[v]`.

Find the maximum matching size respecting these capacities.

![Problem Illustration](../images/AGR-009/problem-illustration.png)

## Input Format

- First line: integers `nU`, `nV`, and `m`
- Second line: `nU` integers `capU`
- Third line: `nV` integers `capV`
- Next `m` lines: `u v` describing an edge from `u` in `U` to `v` in `V`

## Output Format

- Single integer: maximum feasible matching size

## Constraints

- `1 <= nU + nV <= 100000`
- `0 <= m <= 200000`
- `0 <= capU[i], capV[j] <= 10^9`
- `0 <= u < nU`, `0 <= v < nV`

## Example

**Input:**

```
2 2 3
1 2
1 1
0 0
1 0
1 1
```

**Output:**

```
2
```

**Explanation:**

The capacities limit the matching to size 2.

![Example Visualization](../images/AGR-009/example-1.png)

## Notes

- Convert to a flow network with source->U capacities, V->sink capacities, and edges U->V with capacity 1.
- Use Dinic for efficiency.
- Use 64-bit integers for flow values.

## Related Topics

Bipartite Matching, Max Flow, Capacity Constraints

---

## Solution Template

### Java


### Python


### C++


### JavaScript

