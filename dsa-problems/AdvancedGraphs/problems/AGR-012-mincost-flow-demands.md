---
problem_id: AGR_MINCOST_FLOW_DEMANDS__7702
display_id: AGR-012
slug: mincost-flow-demands
title: "Minimum-Cost Flow With Demands"
difficulty: Hard
difficulty_score: 70
topics:
  - Graphs
  - Min-Cost Flow
  - Circulation
tags:
  - advanced-graphs
  - min-cost-flow
  - demands
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-012: Minimum-Cost Flow With Demands

## Problem Statement

You are given a directed graph with lower and upper bounds on edges and a supply/demand value at each node. Find a feasible circulation that satisfies all demands and minimizes total cost.

If no feasible flow exists, output `INFEASIBLE`.

![Problem Illustration](../images/AGR-012/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers `b[i]` (positive = supply, negative = demand)
- Next `m` lines: `u v low high cost` for edge `u -> v`

## Output Format

- If infeasible: print `INFEASIBLE`
- Otherwise: print `FEASIBLE` and a line with the minimum total cost

## Constraints

- `1 <= n <= 500`
- `0 <= m <= 2000`
- `-10^9 <= b[i] <= 10^9`
- `0 <= low <= high <= 10^9`
- `-10^6 <= cost <= 10^6`

## Example

**Input:**

```
2 1
5 -5
0 1 2 5 1
```

**Output:**

```
FEASIBLE
5
```

**Explanation:**

Send 5 units from 0 to 1. Total cost is 5.

![Example Visualization](../images/AGR-012/example-1.png)

## Notes

- Convert to circulation with a super source and super sink.
- Use potentials and Dijkstra/SPFA for min-cost max-flow.
- Use 64-bit integers for costs and flows.

## Related Topics

Min-Cost Flow, Circulation, Potentials

---

## Solution Template

### Java


### Python


### C++


### JavaScript

