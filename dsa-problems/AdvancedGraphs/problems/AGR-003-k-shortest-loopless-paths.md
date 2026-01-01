---
problem_id: AGR_K_SHORTEST_LOOPLESS_PATHS__2749
display_id: AGR-003
slug: k-shortest-loopless-paths
title: "K Shortest Paths (Loopless)"
difficulty: Medium
difficulty_score: 62
topics:
  - Graphs
  - Shortest Path
  - Yen Algorithm
tags:
  - advanced-graphs
  - k-shortest
  - yen
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-003: K Shortest Paths (Loopless)

## Problem Statement

Given a directed weighted graph, find the `k` shortest **simple** paths from source `s` to target `t` (no repeated vertices). Output the path lengths in ascending order.

If fewer than `k` simple paths exist, output all of them.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187126/dsa-problems/AGR-003/problem/ycidx4enufuhzccowmgb.jpg)

## Input Format

- First line: integers `n`, `m`, `s`, `t`, and `k`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- Line 1: integer `r`, the number of paths found
- Line 2: `r` integers, the path lengths in ascending order

## Constraints

- `1 <= n <= 500`
- `0 <= m <= 5000`
- `1 <= k <= 50`
- `0 <= w <= 10^9`
- `0 <= s, t < n`

## Example

**Input:**

```
3 3 0 2 2
0 1 1
1 2 1
0 2 3
```

**Output:**

```
2
2 3
```

**Explanation:**

The two shortest simple paths are `0-1-2` (length 2) and `0-2` (length 3).

![Example Visualization](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187128/dsa-problems/AGR-003/problem/wvacrhnvixycwwqlk1md.jpg)

## Notes

- Use Yen's algorithm with Dijkstra for spur paths.
- Distances can exceed 32-bit; use 64-bit integers.
- If no path exists, output `0` and an empty second line.

## Related Topics

K Shortest Paths, Dijkstra, Yen's Algorithm

---

## Solution Template

### Java


### Python


### C++


### JavaScript

