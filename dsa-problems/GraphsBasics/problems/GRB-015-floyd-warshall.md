---
problem_id: GRB_FLOYD_WARSHALL__9386
display_id: GRB-015
slug: floyd-warshall
title: "Floyd-Warshall All-Pairs"
difficulty: Medium
difficulty_score: 48
topics:
  - Graphs
  - Floyd-Warshall
  - Shortest Path
tags:
  - graphs-basics
  - floyd-warshall
  - shortest-path
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-015: Floyd-Warshall All-Pairs

## Problem Statement

Given a directed weighted graph with up to 500 nodes, compute the shortest path distance between every pair of nodes using the Floyd-Warshall algorithm.

If a negative cycle exists, output `NEGATIVE CYCLE`.

![Problem Illustration](../images/GRB-015/problem-illustration.png)

## Input Format

- First line: integer `n`
- Next `n` lines: `n` integers each, the adjacency matrix

For `i != j`, a value of `-1` means no direct edge. The diagonal entries are `0`.

## Output Format

- If a negative cycle exists: print `NEGATIVE CYCLE`
- Otherwise: print the `n x n` distance matrix, with `-1` for unreachable pairs

## Constraints

- `1 <= n <= 500`
- Edge weights are in `[-10^9, 10^9]`

## Example

**Input:**

```
3
0 1 4
-1 0 2
-1 -1 0
```

**Output:**

```
0 1 3
-1 0 2
-1 -1 0
```

**Explanation:**

The shortest path from 0 to 2 goes through 1 with total cost 3.

![Example Visualization](../images/GRB-015/example-1.png)

## Notes

- Use 64-bit integers to avoid overflow.
- After running, if any `dist[i][i] < 0`, a negative cycle exists.
- Keep `-1` for unreachable pairs.

## Related Topics

Floyd-Warshall, APSP, Dynamic Programming

---

## Solution Template

### Java


### Python


### C++


### JavaScript

