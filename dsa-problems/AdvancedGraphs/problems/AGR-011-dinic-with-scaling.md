---
problem_id: AGR_DINIC_WITH_SCALING__5083
display_id: AGR-011
slug: dinic-with-scaling
title: "Dinic With Scaling"
difficulty: Medium
difficulty_score: 56
topics:
  - Graphs
  - Max Flow
  - Scaling
tags:
  - advanced-graphs
  - max-flow
  - dinic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-011: Dinic With Scaling

## Problem Statement

Compute the maximum flow in a directed graph using Dinic's algorithm with capacity scaling.

![Problem Illustration](../images/AGR-011/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, `s`, `t`
- Next `m` lines: `u v c` describing a directed edge `u -> v` with capacity `c`

## Output Format

- Single integer: maximum flow from `s` to `t`

## Constraints

- `2 <= n <= 5000`
- `0 <= m <= 20000`
- `0 <= c <= 10^9`
- `0 <= s, t < n`, `s != t`

## Example

**Input:**

```
4 4 0 3
0 1 10
0 2 5
1 3 7
2 3 8
```

**Output:**

```
12
```

**Explanation:**

The maximum flow sends 7 through node 1 and 5 through node 2.

![Example Visualization](../images/AGR-011/example-1.png)

## Notes

- Capacity scaling improves performance on large capacities.
- Use 64-bit integers for flow values.
- Dinic still works without scaling; scaling is an optimization.

## Related Topics

Max Flow, Dinic, Capacity Scaling

---

## Solution Template

### Java


### Python


### C++


### JavaScript

