---
problem_id: QUE_FESTIVAL_LANTERN_SPREAD__8461
display_id: QUE-015
slug: festival-lantern-spread
title: "Festival Lantern Spread"
difficulty: Medium
difficulty_score: 52
topics:
  - BFS
  - Queue
  - Grid
tags:
  - bfs
  - grid
  - queue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-015: Festival Lantern Spread

## Problem Statement

A festival grid uses `0` for unlit cells and `1` for lit lanterns. Every minute, each lit lantern lights its four neighboring cells (up, down, left, right).

Compute the minimum number of minutes required to light the entire grid. If it is impossible, output `-1`.

![Problem Illustration](../images/QUE-015/problem-illustration.png)

## Input Format

- First line: two integers `r` and `c`
- Next `r` lines: `c` space-separated integers (`0` or `1`)

## Output Format

- Single integer: minutes to light all cells, or `-1`

## Constraints

- `1 <= r, c <= 200`
- `r * c <= 40000`
- Grid values are `0` or `1`

## Example

**Input:**

```
4 4
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 1
```

**Output:**

```
3
```

**Explanation:**

The farthest cell from a lit lantern is at Manhattan distance 3, so it takes 3 minutes to light the entire grid.

![Example Visualization](../images/QUE-015/example-1.png)

## Notes

- Use multi-source BFS starting from all `1` cells
- Track the number of unlit cells to detect impossible cases
- Each BFS layer corresponds to one minute
- Time complexity: O(r * c)

## Related Topics

BFS, Grid, Queue

---

## Solution Template

### Java


### Python


### C++


### JavaScript

