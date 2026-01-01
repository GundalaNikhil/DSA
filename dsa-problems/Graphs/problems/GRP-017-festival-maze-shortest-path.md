---
problem_id: GRP_FESTIVAL_MAZE_SHORTEST__7418
display_id: GRP-017
slug: festival-maze-shortest-path
title: "Festival Maze Shortest Path"
difficulty: Medium
difficulty_score: 55
topics:
  - Grid Graph
  - BFS
  - State Space Search
  - Shortest Path
tags:
  - graph
  - grid
  - bfs
  - state-space
  - shortest-path
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-017: Festival Maze Shortest Path

## Problem Statement

You are given a 2D grid representing a festival maze with the following cells:
- `S`: Start position (exactly one)
- `E`: Exit position (exactly one)
- `F`: Food stall (at least one)
- `#`: Wall (impassable)
- `.`: Open cell (passable)

You can move 4-directionally (up, down, left, right) through non-wall cells.

**Rule**: You must visit at least one food stall (`F`) before reaching the exit (`E`).

Find the minimum number of steps from `S` to `E` while satisfying the food stall visit rule, or return `-1` if impossible.

![Problem Illustration](../images/GRP-017/problem-illustration.png)

## Input Format

- First line: two integers `r c` (number of rows and columns)
- Next `r` lines: strings of length `c` representing the grid

## Output Format

- Single integer: minimum steps from S to E visiting at least one F, or `-1` if impossible

## Constraints

- `1 <= r, c <= 400`
- Total cells `<= 160,000`
- Grid contains exactly one `S`, exactly one `E`, and at least one `F`

## Example

**Input:**
```
3 3
SF.
###E
.F.
```

**Output:**
```
4
```

**Explanation:**

Grid layout:
```
S F .
# # # E
. F .
```

The optimal path demonstrates the constraint requirement:
```
S . F
# . .
. . E
```

Path: S(0,0) → (0,1) → F(0,2) → (1,2) → (2,2)=E: 4 steps ✓

![Example Visualization](../images/GRP-017/example-1.png)

## Notes

- Use BFS with state tracking: (row, col, visited_food_stall)
- State space: (r, c, {0, 1}) where 0 = haven't visited F yet, 1 = have visited F
- Start from S with state (row_S, col_S, 0)
- When you reach a food stall F, flip the visited flag to 1
- Can only reach E when visited_food_stall = 1
- Time complexity: O(r × c × 2) = O(r × c)
- Use a queue with (row, col, has_visited_food, steps)

## Related Topics

Grid Graph, BFS, State Space Search, Shortest Path with Constraints, Multi-State BFS

---

## Solution Template

### Java


### Python


### C++


### JavaScript
