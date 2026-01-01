---
problem_id: DP_GRID_TURN_LIMIT__4930
display_id: DP-008
slug: grid-paths-turn-limit
title: "Grid Paths With Turn Limit"
difficulty: Medium
difficulty_score: 58
topics:
  - Dynamic Programming
  - Grid DP
  - Counting
tags:
  - dp
  - grid
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2500
memory_limit: 256
---

# DP-008: Grid Paths With Turn Limit

## Problem Statement

You are in an `m x n` grid, starting at the top-left cell `(0,0)` and wanting to reach the bottom-right cell `(m-1, n-1)`.

You may move only:

- **Right** (increase column by 1), or
- **Down** (increase row by 1)

A **turn** occurs when your move direction changes between consecutive moves (Right→Down or Down→Right). The first move does **not** count as a turn because there is no previous direction.

Given an integer `T`, count the number of valid paths that use **at most `T` turns**.

Because the count can be huge, output the answer modulo `1_000_000_007`.

![Problem Illustration](../images/DP-008/problem-illustration.png)

## Input Format

- First line: three integers `m`, `n`, `T`

## Output Format

Print one integer: number of paths from `(0,0)` to `(m-1,n-1)` using at most `T` turns, modulo `1_000_000_007`.

## Constraints

- `1 <= m, n <= 100`
- `0 <= T <= 50`

## Example

**Input:**
```
2 3 1
```

**Output:**
```
2
```

**Explanation:**

Grid is 2 rows and 3 columns. We need 2 Rights and 1 Down in some order.

All possible paths:

- `R R D` (1 turn: R→D)
- `R D R` (2 turns: R→D→R)
- `D R R` (1 turn: D→R)

With at most `T=1` turns, valid paths are `RRD` and `DRR` ⇒ answer is `2`.

![Example Visualization](../images/DP-008/example-1.png)

## Notes

- If `m=1` or `n=1`, there is only one path and it uses 0 turns.
- The first move does not count as a turn.
- Use modulo arithmetic throughout.

## Related Topics

Dynamic Programming, Grid DP, Counting

---

## Solution Template

### Java


### Python


### C++


### JavaScript


