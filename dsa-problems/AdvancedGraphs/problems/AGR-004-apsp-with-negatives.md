---
problem_id: AGR_APSP_WITH_NEGATIVES__6027
display_id: AGR-004
slug: apsp-with-negatives
title: "All-Pairs Shortest Path With Negative Edges"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - APSP
  - Johnson
tags:
  - advanced-graphs
  - apsp
  - johnson
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-004: All-Pairs Shortest Path With Negative Edges

## Problem Statement

Given a directed weighted graph with no negative cycles, compute the shortest path distance between every pair of nodes.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187669/dsa-problems/AGR-004/problem/nii8p5fuu2xwkypthout.jpg)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- Print `n` lines, each with `n` entries
- Use `INF` for unreachable pairs

## Constraints

- `1 <= n <= 2000`
- `0 <= m <= 5000`
- `-10^9 <= w <= 10^9`
- The graph has no negative cycles

## Example

**Input:**

```
3 3
0 1 2
1 2 -1
0 2 4
```

**Output:**

```
0 2 1
INF 0 -1
INF INF 0
```

**Explanation:**

The shortest path from 0 to 2 goes through 1 with total cost 1.

![Example Visualization](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187671/dsa-problems/AGR-004/problem/mpmwtfgxrk0cjmjldfs0.jpg)

## Notes

- Johnson's algorithm runs Bellman-Ford once, then Dijkstra from each node.
- Use 64-bit integers to avoid overflow.
- `INF` is only for unreachable; negative distances can occur.

## Related Topics

APSP, Johnson, Dijkstra

---

## Solution Template

### Java


### Python


### C++


### JavaScript

