---
problem_id: GEO_MST_MANHATTAN__7082
display_id: GEO-016
slug: mst-complete-geometry
title: "Minimum Spanning Tree on Complete Graph by Geometry"
difficulty: Hard
difficulty_score: 80
topics:
  - Computational Geometry
  - Minimum Spanning Tree
  - Manhattan Distance
tags:
  - geometry
  - manhattan
  - mst
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-016: Minimum Spanning Tree on Complete Graph by Geometry

## Problem Statement

You are given `n` points in 2D. The complete graph has an edge between every pair of points with weight equal to their **Manhattan distance** (`|x1 - x2| + |y1 - y2|`).

Compute the total weight of a Minimum Spanning Tree (MST) of this graph.

Return the MST weight as an integer.

## ASCII Visual

```
Points:
● (0,0)   ● (3,0)
     ● (2,2)

Edge weights (Manhattan):
 (0,0)-(3,0): 3
 (0,0)-(2,2): 4
 (3,0)-(2,2): 3
MST weight = 6
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`

## Output Format

- Single integer: total weight of the MST

## Constraints

- `2 <= n <= 200000`
- `-10^9 <= xi, yi <= 10^9`

## Example

**Input:**
```
3
0 0
2 2
3 0
```

**Output:**
```
6
```

**Explanation:**

Edges: 4,3,3; MST chooses 3+3 = 6.

## Notes

- Use the Manhattan MST trick: consider 4 directional transforms and connect near neighbors via sweep with Fenwick/Hash map.
- Then run Kruskal on candidate edges (`O(n log n)`).

## Related Topics

MST, Manhattan Geometry, Kruskal, Sweep

---

## Solution Template

### Java


### Python


### C++


### JavaScript

