---
problem_id: AGR_MIN_CUT_SMALL_GRAPH__4182
display_id: AGR-001
slug: min-cut-small-graph
title: "Minimum Cut on Small Graph"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
  - Min Cut
  - Stoer-Wagner
tags:
  - advanced-graphs
  - min-cut
  - stoer-wagner
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-001: Minimum Cut on Small Graph

## Problem Statement

Given an undirected weighted graph with `n` nodes, compute the value of the **global minimum cut**. The cut value is the total weight of edges crossing between the two partitions.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767185652/dsa-problems/AGR-001/problem/ngj17ehpuwgruaqgacaw.jpg)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w` describing an undirected edge with weight `w`

## Output Format

- Single integer: the minimum cut value

## Constraints

- `1 <= n <= 200`
- `0 <= m <= 2000`
- `0 <= w <= 10^9`
- `0 <= u, v < n`

## Example

**Input:**

```
4 4
0 1 1
1 2 2
2 3 1
0 3 2
```

**Output:**

```
2
```

**Explanation:**

One minimum cut separates `{0, 3}` from `{1, 2}`.
Edges crossing: `(0, 1)` (weight 1) and `(3, 2)` (weight 1).
Total cost: `1 + 1 = 2`.

![Example Visualization](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767185654/dsa-problems/AGR-001/problem/lhavu7kthroej0xvm6av.jpg)

## Notes

- The graph may be disconnected; then the minimum cut is 0.
- Use Stoer-Wagner for the global min-cut in `O(n^3)`.
- Use 64-bit integers for the cut value.

## Related Topics

Global Min-Cut, Stoer-Wagner, Graph Algorithms

---

## Solution Template

### Java


### Python


### C++


### JavaScript

