---
problem_id: GMT_MATRIX_REMOVE__1928
display_id: GMT-013
slug: matrix-removal-game
title: "Matrix Removal Game"
difficulty: Medium
difficulty_score: 60
topics:
  - Game Theory
  - Dynamic Programming
tags:
  - minimax
  - memoization
  - zero-sum
premium: true
subscription_tier: basic
---

# GMT-013: Matrix Removal Game

## 📋 Problem Summary

Players alternately remove the first/last row or first/last column of a matrix
until a single cell remains. Player 1 (Maximizer) wants that final value as
large as possible; Player 2 (Minimizer) wants it as small as possible. Output
the final value under optimal play.

## 🌍 Real-World Scenario

**Scenario Title:** The Land Auction.

Imagine a plot of land divided into a grid of values (oil reserves, gold, etc.).
- Two developers are negotiating boundaries.
- One wants to shrink the plot to a high-value center.
- The other wants to shrink it to a low-value swamp.
- They take turns ceding territory from the edges.

![Real-World Application](../images/GMT-013/real-world-scenario.png)

## Detailed Explanation

### State Representation

The state is defined by the current submatrix, represented by `(r1, r2, c1, c2)`.
- `r1`: Start row index.
- `r2`: End row index.
- `c1`: Start col index.
- `c2`: End col index.

### Transitions

From `(r1, r2, c1, c2)`:
1.  Remove Top: `(r1+1, r2, c1, c2)`
2.  Remove Bottom: `(r1, r2-1, c1, c2)`
3.  Remove Left: `(r1, r2, c1+1, c2)`
4.  Remove Right: `(r1, r2, c1, c2-1)`

### Turn Management

- Total moves made so far = `(N - (r2 - r1 + 1)) + (M - (c2 - c1 + 1))`.
- If `Total Moves` is Even -> Maximizer's turn.
- If `Total Moves` is Odd -> Minimizer's turn.

### Minimax Logic

- **Base Case:** If `r1 == r2` and `c1 == c2`, return `Matrix[r1][c1]`.
- **Maximizer:** `max(Rec(Top), Rec(Bottom), Rec(Left), Rec(Right))`.
- **Minimizer:** `min(Rec(Top), Rec(Bottom), Rec(Left), Rec(Right))`.

### Complexity

- **States:** `N * N * M * M`.
- **Transitions:** 4.
- **Time:** `O(N^2 * M^2)`.
- With `N, M <= 20`, `20^4 = 160,000`. Very fast.

![Algorithm Visualization](../images/GMT-013/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `[[10, 0], [5, 5]]`
- Max removes Top -> `[5, 5]`. Min removes Left -> `5`.
- Max removes Bottom -> `[10, 0]`. Min removes Left -> `0`.
- Max removes Left -> `[0, 5]^T`. Min removes Top -> `0`.
- Max removes Right -> `[10, 5]^T`. Min removes Bottom -> `5`.
- Max chooses 5.

## ✅ Proof of Correctness

- **Minimax:** Standard algorithm for zero-sum perfect information games.
- **DAG:** Game state always shrinks, no cycles.
- **Optimality:** Assumes best play from both sides.

## 💡 Interview Extensions

- **Extension 1:** What if we can remove K rows?
  - *Answer:* Just more transitions.
- **Extension 2:** What if we want to maximize sum of removed elements?
  - *Answer:* Change payoff function.

### Common Mistakes

1.  **Wrong Turn:**
    - ❌ Wrong: Alternating based on recursion depth without checking total moves.
    - ✅ Correct: Check parity of total moves.
2.  **Base Case:**
    - ❌ Wrong: Stopping at empty matrix.
    - ✅ Correct: Stopping at 1x1.

## Related Concepts

- **Minimax**
- **Dynamic Programming**
