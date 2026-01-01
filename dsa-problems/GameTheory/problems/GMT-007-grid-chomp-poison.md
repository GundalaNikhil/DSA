---
problem_id: GMT_GRID_CHOMP_POISON__7391
display_id: GMT-007
slug: grid-chomp-poisoned
title: "Grid Chomp with Poisoned Cells"
difficulty: Hard
difficulty_score: 60
topics:
  - Game Theory
  - Dynamic Programming
  - Bitmask
tags:
  - impartial-game
  - memoization
  - state-compression
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GMT-007: Grid Chomp with Poisoned Cells

## Problem Statement

You are given an `R x C` grid of chocolate bars.
The cell at `(0, 0)` is poisoned. There may be other poisoned cells as well.
Two players take turns making a move.
In each turn, a player must choose a non-poisoned cell `(r, c)` and eat it, along with all cells `(x, y)` such that `x >= r` and `y >= c` (i.e., the rectangle to the bottom-right of the chosen cell).
However, a player **cannot** choose a cell `(r, c)` if eating it would also consume any poisoned cell.
In other words, the chosen rectangle `[r, R-1] x [c, C-1]` must not contain any poisoned cells.
The player who cannot make a valid move loses.
(This happens when all remaining edible cells would force eating a poisoned cell, or no edible cells are left).

Determine if the first player has a winning strategy.

![Problem Illustration](../images/GMT-007/problem-illustration.png)

## Input Format

- The first line contains two integers `R` and `C`.
- The second line contains an integer `K`, the number of poisoned cells.
- The next `K` lines each contain two integers `r` and `c`, representing a poisoned cell.
- `(0, 0)` is always included in the poisoned cells.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= R, C <= 8`
- `1 <= K <= R * C`
- `(0, 0)` is always poisoned.

## Example

**Input:**
```
2 2
1
0 0
```

**Output:**
```
First
```

**Explanation:**
- Grid 2x2. Poison at (0,0).
- Valid moves:
  - (0, 1): Removes (0,1), (1,1).
  - (1, 0): Removes (1,0), (1,1).
  - (1, 1): Removes (1,1).
- If P1 picks (1, 1): Grid becomes L-shape (missing (1,1)).
  - P2 can pick (0, 1) or (1, 0).
  - If P2 picks (0, 1), only (1, 0) remains. P1 picks (1, 0). P2 has no moves. P1 wins.
- Thus P1 has a winning strategy.

![Example Visualization](../images/GMT-007/example-1.png)

## Notes

- The state of the game can be represented by the heights of the columns.
- Since we always remove a bottom-right rectangle, the remaining cells always form a "staircase" shape (Young Diagram).
- `h[0] >= h[1] >= ... >= h[C-1]`.

## Related Topics

Game Theory, Memoization, Young Tableaux

---

## Solution Template

### Java


### Python


### C++


### JavaScript

