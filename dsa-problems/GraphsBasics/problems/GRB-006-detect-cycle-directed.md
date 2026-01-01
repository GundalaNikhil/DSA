---
problem_id: GRB_DETECT_CYCLE_DIRECTED__8425
display_id: GRB-006
slug: detect-cycle-directed
title: "Detect Cycle in Directed Graph"
difficulty: Easy
difficulty_score: 34
topics:
  - Graphs
  - DFS
  - Cycle Detection
tags:
  - graphs-basics
  - cycle-detection
  - dfs
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-006: Detect Cycle in Directed Graph

## Problem Statement

Given a directed graph, determine whether it contains a cycle.

![Problem Illustration](../images/GRB-006/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` representing a directed edge `u -> v`

## Output Format

- Print `true` if a directed cycle exists, otherwise `false`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
3 3
0 1
1 2
2 0
```

**Output:**

```
true
```

**Explanation:**

The edges form a cycle `0 -> 1 -> 2 -> 0`.

![Example Visualization](../images/GRB-006/example-1.png)

## Notes

- Use DFS with colors (0=unvisited, 1=visiting, 2=done) or Kahn's algorithm.
- Self-loops also count as cycles.
- The graph may be disconnected.

## Related Topics

Cycle Detection, DFS, Directed Graphs

---

## Solution Template

### Java


### Python


### C++


### JavaScript

