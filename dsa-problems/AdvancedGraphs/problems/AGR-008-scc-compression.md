---
problem_id: AGR_SCC_COMPRESSION__2659
display_id: AGR-008
slug: scc-compression
title: "Strongly Connected Components Compression"
difficulty: Easy
difficulty_score: 40
topics:
  - Graphs
  - SCC
  - Condensation Graph
tags:
  - advanced-graphs
  - scc
  - condensation
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-008: Strongly Connected Components Compression

## Problem Statement

Find the strongly connected components (SCCs) of a directed graph and build the condensation DAG where each SCC is contracted into a single node.

![Problem Illustration](../images/AGR-008/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` describing a directed edge `u -> v`

## Output Format

- Line 1: integer `k`, number of SCCs
- Line 2: `n` integers `comp[i]` in `[0, k-1]`
- Line 3: integer `e`, number of edges in the condensation DAG
- Next `e` lines: `a b` for each edge `a -> b` between SCCs

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
3 3
0 1
1 0
1 2
```

**Output:**

```
2
0 0 1
1
0 1
```

**Explanation:**

Nodes {0,1} are one SCC, node {2} is another. The condensation graph has one edge.

![Example Visualization](../images/AGR-008/example-1.png)

## Notes

- Use Kosaraju or Tarjan to compute SCCs.
- Avoid duplicate edges in the condensation DAG.
- Any valid component labeling is accepted.

## Related Topics

SCC, Tarjan, Condensation Graph

---

## Solution Template

### Java


### Python


### C++


### JavaScript

