---
problem_id: REC_ROBOT_ROUTE_TURNS__7405
display_id: REC-005
slug: robot-route-turns
title: "Robot Route With Turns"
difficulty: Medium
difficulty_score: 52
topics:
  - Recursion
  - Backtracking
  - Grid
tags:
  - recursion
  - backtracking
  - grid
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-005: Robot Route With Turns

## Problem Statement

A robot must move from the top-left cell `(0,0)` to the bottom-right cell `(r-1,c-1)` on a grid. You may move up, down, left, or right, but cannot enter blocked cells (`1`).

Find any valid path that uses at most `T` turns, where a turn is a change in movement direction between consecutive steps. If no path exists, output `NONE`.

![Problem Illustration](../images/REC-005/problem-illustration.png)

## Input Format

- First line: integers `r`, `c`, and `T`
- Next `r` lines: `c` space-separated integers (0 = open, 1 = blocked)

## Output Format

- One line with the path as coordinates `row,col` separated by spaces
- If no valid path exists, output `NONE`

## Constraints

- `1 <= r, c <= 8`
- `0 <= T <= 6`
- Grid values are `0` or `1`

## Example

**Input:**

```
3 3 2
0 0 0
1 1 0
0 0 0
```

**Output:**

```
0,0 0,1 0,2 1,2 2,2
```

**Explanation:**

The path goes right, right, down, down. It has one turn (right to down).

![Example Visualization](../images/REC-005/example-1.png)

## Notes

- Track the previous direction to count turns
- Use a visited grid to avoid cycles
- Stop early when turns exceed `T`
- Any valid path is acceptable

## Related Topics

Backtracking, Grid Search, Pruning

---

## Solution Template
### Java


### Python


### C++


### JavaScript

