---
problem_id: GMT_CIRCULAR_NIM_VARIANT__4829
display_id: GMT-004
slug: circular-nim-variant
title: "Circular Nim Variant"
difficulty: Medium
difficulty_score: 55
topics:
  - Game Theory
  - Dynamic Programming
tags:
  - impartial-game
  - memoization
  - cycle-detection
premium: true
subscription_tier: basic
---

# GMT-004: Circular Nim Variant

## 📋 Problem Summary

There are `n` piles arranged in a circle. On each move, pick a pile `i` with at
least one stone, remove `k` stones (`1 <= k <= piles[i]`), then add 1 stone to
each adjacent pile. A player who cannot move loses; if play can loop forever,
the result is a draw. Determine "First", "Second", or "Draw".

## 🌍 Real-World Scenario

**Scenario Title:** The Ripple Effect

Imagine a resource distribution network where taking resources from one node causes a slight overflow into neighboring nodes. You want to drain the network (or force the other operator to be unable to act), but every action has a side effect that can prolong the game.

**Why This Problem Matters:**

- **Side Effects:** Standard Nim moves are independent. Here, moves affect other parts of the state.
- **Cycles:** The "add" rule introduces the possibility of infinite games, requiring cycle detection.

![Real-World Application](../images/GMT-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Move Dynamics

```
State: [1, 0, 1] (Triangle)

Move on Index 0 (Size 1):
  - Remove 1 -> Size 0.
  - Add 1 to Index 2 (Left) -> 1+1=2.
  - Add 1 to Index 1 (Right) -> 0+1=1.
  - New State: [0, 1, 2].

Effect:
  - Total stones changed from 2 to 3.
  - Game state complexity increases.
```

## ✅ Input/Output Clarifications

- **Adjacent:** `(i-1+n)%n` and `(i+1)%n`.
- **Draw:** If the game enters a loop of states.

## Optimal Approach

### Key Insight

Since `n` and `piles[i]` are small, we can use **Memoization with State Tracking**.
We map each state (tuple of pile sizes) to a result: WIN, LOSS, DRAW.
- **WIN:** There exists a move to a LOSS state.
- **LOSS:** All moves lead to WIN states (or no moves).
- **DRAW:** No move to LOSS, but some move to DRAW (and others to WIN).

### Algorithm

1.  Use a Map `memo` to store results for states.
2.  Use a Set `visiting` to detect cycles in the current recursion stack.
3.  `solve(state)`:
    - If `state` in `memo`, return result.
    - If `state` in `visiting`, return DRAW (cycle detected).
    - Add `state` to `visiting`.
    - `canReachLoss = False`
    - `canReachDraw = False`
    - For each pile `i` > 0:
        - For `k` from 1 to `piles[i]`:
            - Create `next_state`.
            - `res = solve(next_state)`
            - If `res == LOSS`: `canReachLoss = True`.
            - If `res == DRAW`: `canReachDraw = True`.
    - Remove `state` from `visiting`.
    - If `canReachLoss`: Result = WIN.
    - Else if `canReachDraw`: Result = DRAW.
    - Else: Result = LOSS.
    - Store in `memo` and return.

### Time Complexity

- **Exponential**: The state space can be large. However, for small inputs, it's feasible. The "add 1" rule can limit the depth effectively or lead to quick cycles.

### Space Complexity

- **O(States)**: To store memoization table.

![Algorithm Visualization](../images/GMT-004/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `[1, 0, 1]`

1.  Start `[1, 0, 1]`.
2.  Move 1: Remove 1 from index 0. Add to 2, 1. -> `[0, 1, 2]`.
3.  From `[0, 1, 2]`:
    - Move 1: Remove 1 from index 1. Add to 0, 2. -> `[1, 0, 3]`.
    - Move 2: Remove 1 from index 2. Add to 1, 0. -> `[1, 2, 1]`.
    - Move 3: Remove 2 from index 2. Add to 1, 0. -> `[1, 2, 0]`.
4.  Recursion continues. Eventually, we find that `[1, 0, 1]` can reach a state that forces the opponent to lose.

## ✅ Proof of Correctness

- **Memoization:** Ensures we don't recompute states.
- **Cycle Detection:** `visiting` set correctly identifies loops, returning "Draw".
- **Minimax Logic:** Correctly propagates Win/Loss/Draw up the recursion tree.

## 💡 Interview Extensions

- **Extension 1:** What if `n` is large?
  - *Answer:* The state space explodes. We'd need a mathematical pattern or simpler rule.
- **Extension 2:** What if we add to *all* other piles?
  - *Answer:* Different game, different strategy.

### Common Mistakes

1.  **Infinite Recursion:**
    - ❌ Wrong: Not handling cycles.
2.  **Incorrect Adjacency:**
    - ❌ Wrong: `(i-1)%n` in Python/Java can be negative. Use `(i-1+n)%n`.

## Related Concepts

- **Memoization**
- **Graph Cycles**
- **Minimax**
