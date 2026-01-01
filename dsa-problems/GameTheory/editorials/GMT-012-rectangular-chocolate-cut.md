---
problem_id: GMT_CHOCOLATE_CUT__8392
display_id: GMT-012
slug: rectangular-chocolate-cut
title: "Rectangular Chocolate Cut"
difficulty: Easy
difficulty_score: 30
topics:
  - Game Theory
  - Math
tags:
  - impartial-game
  - sprague-grundy
  - parity
premium: true
subscription_tier: basic
---

# GMT-012: Rectangular Chocolate Cut

## 📋 Problem Summary

You are given a `R x C` chocolate bar. Each move chooses one existing piece and
cuts it along a grid line into two rectangles. The game ends when all pieces are
`1 x 1`; the player who cannot cut loses. Determine the winner.

## 🌍 Real-World Scenario

**Scenario Title:** The Glass Cutter.

You are cutting a large sheet of glass into unit squares for a mosaic.
- Every cut takes energy.
- You and your rival are competing to see who does the last cut (for example, getting paid for finishing the job).
- The total work is fixed!

![Real-World Application](../images/GMT-012/real-world-scenario.png)

## Detailed Explanation

### Key Insight: Fixed Number of Moves

This is a "Shear Game" or "Breaking Game".
Notice that every cut increases the number of pieces by exactly 1.
- Start: 1 piece.
- End: `R * C` pieces (all `1x1`).
- Total cuts needed = `(R * C) - 1`.

Since the total number of moves is fixed and independent of the strategy (order of cuts), the winner is determined solely by the parity of the total moves.
- If `Total Moves` is Odd -> First Player makes moves 1, 3, 5... -> Last move. First Wins.
- If `Total Moves` is Even -> Second Player makes moves 2, 4, 6... -> Last move. Second Wins.

### Formula

- `Moves = R * C - 1`.
- If `(R * C - 1)` is Odd => `R * C` is Even.
- If `(R * C - 1)` is Even => `R * C` is Odd.

So:
- If `R * C` is Even -> First Wins.
- If `R * C` is Odd -> Second Wins.

### Why does this work?

This is a rare impartial game where the game length is invariant.
Usually, games can end quickly or slowly.
Here, you CANNOT reach the end state (`1x1`s) without making exactly `R*C - 1` cuts.
Every cut splits one piece into two. To get `N` pieces from 1, you need `N-1` splits.

### Complexity

- **Time:** `O(1)`.
- **Space:** `O(1)`.

![Algorithm Visualization](../images/GMT-012/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `2 2`
Area = 4 (Even).
Result: First.

**Input:** `3 3`
Area = 9 (Odd).
Result: Second.

## ✅ Proof of Correctness

- **Invariant:** Number of cuts = `Area - 1`.
- **Parity:** Winner depends only on `(Area - 1) % 2`.

## 💡 Interview Extensions

- **Extension 1:** What if we can cut multiple pieces at once (stacking)?
  - *Answer:* Then it becomes Nim with pile sizes `log2(R)` and `log2(C)`? No, much harder.
- **Extension 2:** What if we discard one piece?
  - *Answer:* Then it's Nim with `R-1` and `C-1`.

### Common Mistakes

1.  **Overthinking:**
    - ❌ Wrong: Trying to use Sprague-Grundy or DP.
    - ✅ Correct: Realizing total moves is fixed.
2.  **Off-by-one:**
    - ❌ Wrong: Thinking Even Area means Even Moves.
    - ✅ Correct: Even Area means Odd Moves (First wins).

## Related Concepts

- **Game Invariants**
- **Parity**
