---
problem_id: GMT_COIN_SPLIT__4721
display_id: GMT-014
slug: greedy-coin-split-game
title: "Greedy Coin Split Game"
difficulty: Medium
difficulty_score: 65
topics:
  - Game Theory
  - Dynamic Programming
tags:
  - minimax
  - memoization
  - interval-dp
premium: true
subscription_tier: basic
---

# GMT-014: Greedy Coin Split Game

## 📋 Problem Summary

A Splitter divides the current contiguous segment into two non-empty parts.
The Chooser keeps one part (adds its sum to their score), and the remaining part
continues with roles swapped. The last single coin is discarded. Compute the
optimal final score difference (Player 1 minus Player 2).

## 🌍 Real-World Scenario

**Scenario Title:** The Estate Division.

Two heirs are dividing a linear estate (coastline properties).
- One heir draws a line to split the estate.
- The other heir chooses which side to take immediately.
- The remaining side is then split by the second heir, and the first chooses.
- This continues until the land is too small to split.

![Real-World Application](../images/GMT-014/real-world-scenario.png)

## Detailed Explanation

### State Representation

`dp[i][j]` represents the maximum score difference `(Splitter - Chooser)` obtainable from the subarray `A[i...j]`.

### Transitions

For a subarray `A[i...j]`, the Splitter can split at any index `k` (`i <= k < j`).
This creates `Left = A[i...k]` and `Right = A[k+1...j]`.

The Chooser has two options:
1.  **Take Left:**
    - Chooser gets `Sum(Left)`.
    - Game continues on `Right` with Chooser becoming Splitter.
    - Future outcome from `Right` is `dp[k+1][j]` (which is `NewSplitter - NewChooser`).
    - Since current Chooser becomes New Splitter, `dp[k+1][j]` represents `Chooser - Splitter` relative to current roles.
    - So Chooser's total advantage = `Sum(Left) + dp[k+1][j]`.
    - Splitter's advantage = `- (Sum(Left) + dp[k+1][j])`.

2.  **Take Right:**
    - Chooser gets `Sum(Right)`.
    - Game continues on `Left`.
    - Chooser's total advantage = `Sum(Right) + dp[i][k]`.
    - Splitter's advantage = `- (Sum(Right) + dp[i][k])`.

The Chooser will choose the option that maximizes their advantage (minimizes Splitter's advantage).
So for a fixed split `k`, the outcome is:
`Outcome(k) = min( -Sum(Left) - dp[k+1][j], -Sum(Right) - dp[i][k] )`.

The Splitter will choose `k` to maximize this outcome:
`dp[i][j] = max_{k} ( Outcome(k) )`.

### Base Case

- If `i == j` (single element), no split is possible.
- The coin is discarded.
- `dp[i][i] = 0`.

### Complexity

- **States:** `N^2`.
- **Transitions:** `O(N)`.
- **Total:** `O(N^3)`.
- With `N=100`, `10^6` operations. Fast.

![Algorithm Visualization](../images/GMT-014/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `[10, 20, 30]`

Let `f(i, j)` be the optimal Splitter − Chooser score on subarray `A[i..j]`.

- `f(10) = f(20) = f(30) = 0` (single coin is discarded).
- `f(10, 20) = min(-10, -20) = -20`.
- `f(20, 30) = min(-20, -30) = -30`.

Now for `[10, 20, 30]`:
- Split `10 | 20, 30`:
  - Chooser takes `10`: value `-10 - f(20,30) = -10 - (-30) = 20`.
  - Chooser takes `20,30`: value `-50 - f(10) = -50`.
  - Chooser minimizes => `-50`.
- Split `10, 20 | 30`:
  - Chooser takes `10,20`: value `-30 - f(30) = -30`.
  - Chooser takes `30`: value `-30 - f(10,20) = -10`.
  - Chooser minimizes => `-30`.

Splitter maximizes: `max(-50, -30) = -30`.

**Result:** `-30`.

## ✅ Proof of Correctness

- **DP State:** Captures full game state (subarray).
- **Minimax:** Correctly models adversarial play.
- **Base Case:** Correctly handles termination.

## 💡 Interview Extensions

- **Extension 1:** What if we can split into K parts?
  - *Answer:* Loop over K-1 split points.
- **Extension 2:** What if we want to maximize Sum?
  - *Answer:* Change recurrence to return `(MyScore, OppScore)`.

### Common Mistakes

1.  **Sign Error:**
    - ❌ Wrong: `sumLeft + solve(...)`.
    - ✅ Correct: `-sumLeft - solve(...)` because roles swap.
2.  **Base Case:**
    - ❌ Wrong: `return A[i]`.
    - ✅ Correct: `return 0` (discarded).

## Related Concepts

- **Interval DP**
- **Game Theory**
