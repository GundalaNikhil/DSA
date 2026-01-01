---
problem_id: GRB_BELLMAN_FORD__3812
display_id: GRB-004
slug: bellman-ford
title: "Bellman-Ford with Negative Edges"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
  - Shortest Path
  - Bellman-Ford
tags:
  - graphs-basics
  - bellman-ford
  - shortest-path
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-004: Bellman-Ford with Negative Edges

## Problem Statement

You are given a directed graph that may contain negative edge weights. Compute shortest distances from a source node `s`.

If a negative cycle is reachable from `s`, output `NEGATIVE CYCLE`.

![Problem Illustration](../images/GRB-004/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, and `s`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- If a reachable negative cycle exists: print `NEGATIVE CYCLE`
- Otherwise: print `n` integers, the distances from `s` to nodes `0..n-1` (`-1` if unreachable)

## Constraints

- `1 <= n <= 10000`
- `0 <= m <= 50000`
- `-10^9 <= w <= 10^9`
- `0 <= s < n`

## Example

**Input:**

```
2 2 0
0 1 -1
1 0 -1
```

**Output:**

```
NEGATIVE CYCLE
```

**Explanation:**

The cycle `0 -> 1 -> 0` has total weight `-2` and is reachable from the source.

![Example Visualization](../images/GRB-004/example-1.png)

## Notes

- Run `n-1` relaxations, then one extra pass to detect negative cycles.
- Distances should use 64-bit integers.
- Unreachable nodes keep distance `-1`.

## Related Topics

Bellman-Ford, Shortest Path, Negative Cycles

---

## Solution Template

### Java


### Python


### C++


### JavaScript

