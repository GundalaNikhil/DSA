---
problem_id: GRB_DIJKSTRA_BINARY_HEAP__6041
display_id: GRB-003
slug: dijkstra-binary-heap
title: "Dijkstra with Binary Heap"
difficulty: Medium
difficulty_score: 45
topics:
  - Graphs
  - Dijkstra
  - Shortest Path
tags:
  - graphs-basics
  - dijkstra
  - shortest-path
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-003: Dijkstra with Binary Heap

## Problem Statement

You are given a directed graph with non-negative edge weights. Compute the shortest distance from a source node `s` to every node.

If a node is unreachable, its distance should be `-1`.

![Problem Illustration](../images/GRB-003/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, and `s`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- Single line: `n` integers, the distances from `s` to nodes `0..n-1`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= w <= 10^9`
- `0 <= s < n`

## Example

**Input:**

```
3 3 0
0 1 1
1 2 2
0 2 5
```

**Output:**

```
0 1 3
```

**Explanation:**

The shortest path to node 2 is `0 -> 1 -> 2` with total cost 3.

![Example Visualization](../images/GRB-003/example-1.png)

## Notes

- Use Dijkstra with a min-heap (priority queue).
- Skip outdated heap entries using a distance check.
- Distances can exceed 32-bit; use 64-bit integers.

## Related Topics

Dijkstra, Priority Queue, Shortest Path

---

## Solution Template

### Java


### Python


### C++


### JavaScript

