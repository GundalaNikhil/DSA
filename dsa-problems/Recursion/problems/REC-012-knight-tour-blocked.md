---
problem_id: REC_KNIGHT_TOUR_BLOCKED__7742
display_id: REC-012
slug: knight-tour-blocked
title: "Knight Tour With Blocked Cells"
difficulty: Medium
difficulty_score: 60
topics:
  - Recursion
  - Backtracking
  - Chess
tags:
  - recursion
  - backtracking
  - knight-tour
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-012: Knight Tour With Blocked Cells

## Problem Statement

On an `n x n` board, a knight starts at `(0,0)` and must visit every unblocked cell exactly once using standard knight moves.

Some cells are blocked and cannot be visited. Output any valid path that visits all unblocked cells, or `NONE` if impossible.

![Problem Illustration](../images/REC-012/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: integer `b` (number of blocked cells)
- Next `b` lines: two integers `r` and `c` for each blocked cell

## Output Format

- One line with the path as `row,col` coordinates separated by spaces
- Output `NONE` if no tour exists

## Constraints

- `1 <= n <= 5`
- `0 <= b < n * n`
- `(0,0)` is guaranteed to be unblocked

## Example

**Input:**

```
2
3
0 1
1 0
1 1
```

**Output:**

```
0,0
```

**Explanation:**

Only the start cell is unblocked, so the tour is just `(0,0)`.

![Example Visualization](../images/REC-012/example-1.png)

## Notes

- Track visited cells and remaining unblocked count
- Knight moves are (±2, ±1) and (±1, ±2)
- Backtracking is required due to branching
- Any valid tour is acceptable

## Related Topics

Backtracking, Graph Traversal, Recursion

---

## Solution Template
### Java


### Python


### C++


### JavaScript

