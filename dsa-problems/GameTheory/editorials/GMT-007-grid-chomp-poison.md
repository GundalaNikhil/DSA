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
---

# GMT-007: Grid Chomp with Poisoned Cells

## 📋 Problem Summary

You play Chomp on an `R x C` grid with poisoned cells. A move chooses a
non-poisoned cell `(r, c)` and eats the rectangle `[r..R-1] x [c..C-1]`, but the
chosen rectangle cannot include any poisoned cell. The player with no legal move
loses. Determine the winner.

## 🌍 Real-World Scenario

**Scenario Title:** The Minefield Cleanup

Imagine clearing a field of mines (poisoned cells). You can clear rectangular areas starting from a point to the boundary. However, you must not trigger any mines. The person who cannot make a safe clearance move is stuck and loses.

**Why This Problem Matters:**

- **Constrained Moves:** Shows how constraints (poison) reshape the game tree.
- **State Representation:** Teaches how to represent complex grid states (Young Diagrams) efficiently.

![Real-World Application](../images/GMT-007/real-world-scenario.png)

## Detailed Explanation

### Young Diagram State

```
Grid 3x3
State represented by column heights: [3, 2, 1]
X X X
X X .
X . .

Move at (1, 1):
- Remove (x>=1, y>=1).
- (1, 1) is removed.
- New heights: [3, 1, 1]
X X X
X . .
X . .
```

## ✅ Input/Output Clarifications

- **Poisoned Cell:** If `(pr, pc)` is poison, you cannot pick `(r, c)` if `pr >= r` and `pc >= c`.
- **Loss:** No valid moves available.

## Optimal Approach

### Key Insight

The state of the game is always defined by the heights of the columns `h[0], h[1], ..., h[C-1]`, where `R >= h[0] >= h[1] >= ... >= h[C-1] >= 0`.
This is because removing a rectangle `(r, c)` cuts the heights of columns `c` through `C-1` to be at most `r`.
We can memoize this state.
Since `R, C <= 8`, we can encode the state tuple into a Map or Integer (if small enough).
For `R, C <= 8`, the number of states is `(R+C) choose R` = `16 choose 8` = `12870`. Very small!
We can simply use a Map.

### Algorithm

1.  Identify all poisoned cells.
2.  Initial state: `[R, R, ..., R]` (C times).
3.  `solve(state)`:
    - If `state` in `memo`, return.
    - Iterate all possible moves `(r, c)`:
        - `c` from `0` to `C-1`.
        - `r` from `0` to `state[c]-1`.
        - Check if move `(r, c)` is valid (doesn't eat poison).
            - A move `(r, c)` eats poison `(pr, pc)` if `pr >= r` and `pc >= c`.
            - So `(r, c)` is valid if for ALL poisons `(pr, pc)`, NOT (`pr >= r` and `pc >= c`).
        - If valid, compute `next_state`:
            - `new_h[i] = min(state[i], r)` for `i` from `c` to `C-1`.
            - `new_h[i] = state[i]` for `i < c`.
        - If `!solve(next_state)`, then `state` is Winning.
    - If no move leads to Losing, `state` is Losing.

### Time Complexity

- **O(States * R * C)**: Number of states is small (~13k). Transitions `R*C`. Total operations ~10^6.

### Space Complexity

- **O(States)**: To store memoization.

![Algorithm Visualization](../images/GMT-007/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `2x2` Grid, Poison at `(0, 0)`.

**Step-by-Step Execution:**

1.  **Initial State:** `[2, 2]` (Col 0 height 2, Col 1 height 2).
2.  **Possible Moves from `[2, 2]`:**
    - Pick `(1, 1)`: Reduces Col 1 to height 1. New State: `[2, 1]`.
    - Pick `(0, 1)`: Reduces Col 1 to height 0. New State: `[2, 0]`.
    - Pick `(1, 0)`: Reduces Col 0 to height 1, Col 1 to height 0. New State: `[1, 0]`? No.
      - `(1, 0)` sets `h[0] = min(2, 1) = 1`. `h[1] = min(2, 1) = 1`. New State: `[1, 1]`.
    - Pick `(0, 0)`: Invalid (Poison).

3.  **Analyze Next States:**
    - **Analyze `[2, 1]`:**
        - Moves:
            - `(0, 1)` -> `[2, 0]`.
            - `(1, 0)` -> `[1, 1]`.
        - If `[2, 0]` and `[1, 1]` are Winning, then `[2, 1]` is **Losing**.
    - **Analyze `[2, 0]`:**
        - Moves:
            - `(1, 0)` -> `[1, 0]`.
        - If `[1, 0]` is Losing, then `[2, 0]` is **Winning**.
    - **Analyze `[1, 1]`:**
        - Moves:
            - `(0, 1)` -> `[1, 0]`.
        - If `[1, 0]` is Losing, then `[1, 1]` is **Winning**.
    - **Analyze `[1, 0]`:**
        - Moves:
            - `(0, 0)` is Poison. No valid moves.
        - **Losing State**.

4.  **Backpropagate Results:**
    - `[1, 0]` is **Losing**.
    - `[2, 0]` -> `[1, 0]` (Losing). So `[2, 0]` is **Winning**.
    - `[1, 1]` -> `[1, 0]` (Losing). So `[1, 1]` is **Winning**.
    - `[2, 1]` -> `[2, 0]` (Winning) and `[1, 1]` (Winning). All moves lead to Winning. So `[2, 1]` is **Losing**.
    - `[2, 2]` -> `[2, 1]` (Losing). So `[2, 2]` is **Winning**.

**Conclusion:** First player wins by picking `(1, 1)`.

## ✅ Proof of Correctness

- **State Representation:** Young Diagrams cover all reachable states.
- **Memoization:** Handles overlapping subproblems.
- **Small Constraints:** `R, C <= 8` ensures feasible state space.

## 💡 Interview Extensions

- **Extension 1:** What if `R, C` are large?
  - *Answer:* Unsolved problem.
- **Extension 2:** What if we can eat non-rectangular shapes?
  - *Answer:* State representation becomes complex (bitmask of all cells).

### Common Mistakes

1.  **Invalid Moves:**
    - ❌ Wrong: Thinking `(1, 0)` eats `(0, 0)`. It doesn't. `(1, 0)` eats `(r>=1, c>=0)`.
    - ✅ Correct: Check `pr >= r` AND `pc >= c`.
2.  **Poison Logic:**
    - ❌ Wrong: Checking if `(r, c)` IS poison.
    - ✅ Correct: Must check if `(r, c)` **EATS** any poison.
3.  **State Updates:**
    - ❌ Wrong: Only updating column `c`.
    - ✅ Correct: Must update all columns `i >= c` because the rectangle extends to the right boundary. `h[i] = min(h[i], r)`.
4.  **Base Case:**
    - ❌ Wrong: Assuming empty grid is Winning.
    - ✅ Correct: Empty grid (or grid with only poisons) has no moves, so it is Losing.

## Related Concepts

- **Young Tableaux**
- **Partitions**
