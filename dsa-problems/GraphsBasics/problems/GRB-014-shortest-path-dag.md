---
problem_id: GRB_SHORTEST_PATH_DAG__7291
display_id: GRB-014
slug: shortest-path-dag
title: "Shortest Path in DAG"
difficulty: Easy
difficulty_score: 38
topics:
  - Graphs
  - DAG
  - Shortest Path
tags:
  - graphs-basics
  - dag
  - shortest-path
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-014: Shortest Path in DAG

## Problem Statement

Given a weighted directed acyclic graph (DAG), compute shortest distances from a source node `s`.

If a node is unreachable, its distance should be `-1`.

![Problem Illustration](../images/GRB-014/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, and `s`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- Single line: `n` integers, the distances from `s` to nodes `0..n-1`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `-10^9 <= w <= 10^9`
- The graph is a DAG

## Example

**Input:**

```
3 2 0
0 1 1
1 2 2
```

**Output:**

```
0 1 3
```

**Explanation:**

The DAG order is `0,1,2`. Distances relax along this order.

![Example Visualization](../images/GRB-014/example-1.png)

## Notes

- Use topological order and relax edges once.
- Negative weights are allowed in a DAG.
- Use 64-bit integers for distances.

## Related Topics

DAG, Topological Sort, Shortest Path

---

## Solution Template

### Java


### Python


### C++


### JavaScript

