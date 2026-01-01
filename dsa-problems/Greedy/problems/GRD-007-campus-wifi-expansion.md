---
problem_id: GRD_CAMPUS_WIFI_EXPANSION__4892
display_id: GRD-007
slug: campus-wifi-expansion
title: "Campus Wi-Fi Expansion"
difficulty: Medium
difficulty_score: 55
topics:
  - Greedy Algorithms
  - Minimum Spanning Tree
  - Kruskal's Algorithm
tags:
  - greedy
  - mst
  - kruskal
  - graph
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-007: Campus Wi-Fi Expansion

## Problem Statement

You need to connect `n` buildings on campus with network cables. Some buildings may already have cable connections between them (at no additional cost).

For buildings that aren't connected, laying a new cable between buildings `i` and `j` costs `|h[i] - h[j]|`, where `h[i]` is the height of building `i`.

Your goal is to find the minimum total cost to ensure all buildings are connected (directly or indirectly) to the same network.

![Problem Illustration](../images/GRD-007/problem-illustration.png)

## Input Format

- First line: integer `n` (number of buildings)
- Second line: `n` space-separated integers representing building heights `h[0], h[1], ..., h[n-1]`
- Third line: integer `m` (number of existing free cables)
- Next `m` lines: two integers `u v` representing an existing cable between buildings `u` and `v`

## Output Format

- Single integer: minimum total cost to connect all buildings

## Constraints

- `1 <= n <= 10^5`
- `1 <= h[i] <= 10^9`
- `0 <= m < n`
- `0 <= u, v < n`

## Example

**Input:**
```
3
5 1 9
0
```

**Output:**
```
8
```

**Explanation:**

Buildings with heights: [5, 1, 9]
No existing cables (m = 0)

Need to connect all 3 buildings. Possible edges:
- Building 0 to Building 1: cost = |5 - 1| = 4
- Building 0 to Building 2: cost = |5 - 9| = 4
- Building 1 to Building 2: cost = |1 - 9| = 8

Using Minimum Spanning Tree (MST):
- Connect buildings 0 and 1: cost = 4
- Connect buildings 0 and 2: cost = 4
- Total cost = 8

![Example Visualization](../images/GRD-007/example-1.png)

## Notes

- This is a Minimum Spanning Tree (MST) problem
- Existing cables are free (cost = 0) and should be used first
- For new cables, generate all possible edges with costs |h[i] - h[j]|
- Use Kruskal's algorithm with Union-Find
- Optimization: Sort buildings by height and only consider edges between adjacent buildings in sorted order
- Time complexity: O(n² log n) for generating all edges, or O(n log n) with optimization

## Related Topics

Minimum Spanning Tree, Kruskal's Algorithm, Greedy Algorithms, Union-Find, Graph Theory

---

## Solution Template

### Java


### Python


### C++


### JavaScript
