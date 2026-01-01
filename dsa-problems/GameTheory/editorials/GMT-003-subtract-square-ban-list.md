---
problem_id: GMT_SUBTRACT_SQUARE_BAN__3912
display_id: GMT-003
slug: subtract-square-ban-list
title: "Subtract-a-Square with Ban List"
difficulty: Medium
difficulty_score: 45
topics:
  - Game Theory
  - Dynamic Programming
tags:
  - impartial-game
  - subtraction-game
  - grundy-numbers
premium: true
subscription_tier: basic
---

# GMT-003: Subtract-a-Square with Ban List

## 📋 Problem Summary

You have a pile of `n` stones. In each turn, you must remove `s` stones where `s` is a perfect square and `s` is NOT in a banned set `B`. The player who cannot move loses.

## 🌍 Real-World Scenario

**Scenario Title:** The Restricted Budget

Imagine you are reducing a budget deficit. You can only make cuts in specific "square" amounts (like `1k,`4k, `9k packages). However, certain packages (e.g., the`1k package) are "banned" by management and cannot be used. You want to be the one to make the final cut that clears the deficit (reaches 0).

**Why This Problem Matters:**

- **Constrained Games:** It shows how removing specific moves from a standard game changes the strategy.
- **DP on Games:** It reinforces the concept that a state's value is determined by the values of the states it can reach.

![Real-World Application](../images/GMT-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: State Transitions

```
n = 7, B = {1}
Allowed moves: 4, 9, 16...

State 7:
  - Can move to 7 - 4 = 3.

State 3:
  - Allowed moves: 4, 9...
  - 3 - 4 < 0 (Invalid).
  - No moves from 3.
  - 3 is LOSING.

Back to 7:
  - Can move to 3 (Losing).
  - Since we can force opponent to Lose, 7 is WINNING.
```

## ✅ Input/Output Clarifications

- **Perfect Squares:** 1, 4, 9, 16, 25, ...
- **Banned Set:** If 4 is in B, you cannot subtract 4.
- **Winning:** You can make a move to a Losing state.

## Optimal Approach

### Key Insight

This is a standard subtraction game. Since it is impartial and normal play, we can determine if a state `i` is Winning or Losing using a boolean array `dp`.
- `dp[i] = True` (Winning) if there exists a valid square `s` such that `dp[i-s] == False` (Losing).
- `dp[i] = False` (Losing) if for all valid squares `s`, `dp[i-s] == True` (Winning).

### Algorithm

1.  Create a boolean set for `B` for O(1) lookups.
2.  Initialize `dp` array of size `n+1`. `dp[0] = False`.
3.  Iterate `i` from 1 to `n`.
4.  For each `j` starting from 1 such that `s = j*j <= i`:
    - If `s` is not in `B`:
        - Check `dp[i-s]`.
        - If `dp[i-s]` is `False`, then `dp[i]` becomes `True`. Break loop.
5.  Return "First" if `dp[n]` is `True`, else "Second".

### Time Complexity

- **O(N * sqrt(N))**: For each `i`, we iterate squares up to `i`. The number of squares is `sqrt(i)`. Total operations roughly `N * sqrt(N)`.
- With `N=10^5`, `sqrt(N) ≈ 316`. Total ops ≈ `3 * 10^7`, well within 2 seconds.

### Space Complexity

- **O(N)**: For the `dp` array.

![Algorithm Visualization](../images/GMT-003/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `n=7, B={1}`

- `dp[0] = F`
- `i=1`: s=1 (Banned). No moves. `dp[1] = F`.
- `i=2`: s=1 (Banned). No moves. `dp[2] = F`.
- `i=3`: s=1 (Banned). No moves. `dp[3] = F`.
- `i=4`:
  - s=1 (Banned).
  - s=4. `dp[4-4] = dp[0] = F`. Found move to L. `dp[4] = T`.
- `i=5`:
  - s=4. `dp[5-4] = dp[1] = F`. Found move to L. `dp[5] = T`.
- `i=6`:
  - s=4. `dp[6-4] = dp[2] = F`. Found move to L. `dp[6] = T`.
- `i=7`:
  - s=4. `dp[7-4] = dp[3] = F`. Found move to L. `dp[7] = T`.

Result: `dp[7] = T`. Output: "First".

## ✅ Proof of Correctness

The game is finite, impartial, and normal play.
The recurrence `dp[i] = OR(NOT dp[i-s])` correctly computes the Winning/Losing status.
If `dp[i]` is True, there is a move to a Losing state.
If `dp[i]` is False, all moves lead to Winning states (or no moves exist).

## 💡 Interview Extensions

- **Extension 1:** What if we want the number of winning moves?
  - *Answer:* Count how many `s` satisfy `dp[i-s] == False`.
- **Extension 2:** What if `n` is very large (10^18)?
  - *Answer:* We'd need to look for a period in the sequence of W/L values.

### Common Mistakes

1.  **Ignoring Banned Set:**
    - ❌ Wrong: Always allowing 1, 4, 9.
2.  **Off-by-one:**
    - ❌ Wrong: Not checking `s=i` (moving to 0).

## Related Concepts

- **Sprague-Grundy (though boolean is enough here)**
- **Dynamic Programming**
