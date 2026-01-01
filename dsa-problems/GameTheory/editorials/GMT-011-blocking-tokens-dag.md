---
problem_id: GMT_BLOCKING_TOKENS__5821
display_id: GMT-011
slug: blocking-tokens-dag
title: "Blocking Tokens on DAG"
difficulty: Medium
difficulty_score: 55
topics:
  - Game Theory
  - Graph Theory
  - Dynamic Programming
tags:
  - impartial-game
  - memoization
  - dag
premium: true
subscription_tier: basic
---

# GMT-011: Blocking Tokens on DAG

## 📋 Problem Summary

Two tokens start on distinct nodes of a DAG. On each turn, choose one token and
move it along a directed edge to an unoccupied node. If no legal move exists,
the current player loses. Determine the winner.

## 🌍 Real-World Scenario

**Scenario Title:** The Narrow Corridors.

Imagine two robots navigating a facility with one-way corridors.
- They cannot occupy the same room (collision).
- They must keep moving to stay powered.
- If a robot cannot move (dead end or blocked by the other), the system fails.
- You want to force the system into a state where the opponent has no valid moves.

![Real-World Application](../images/GMT-011/real-world-scenario.png)

## Detailed Explanation

### State Representation

The state is defined by the positions of the two tokens: `(u, v)`.
Since the tokens are identical (or players can pick either), the state `(u, v)` is equivalent to `(v, u)`.
However, it's easier to implement as `(u, v)` where order doesn't matter for logic but matters for storage (e.g., store `min(u,v), max(u,v)`).

### Transitions

From state `(u, v)`:
1.  **Move u:** To any neighbor `u'` of `u`.
    - Valid only if `u' != v`.
    - New state: `(u', v)`.
2.  **Move v:** To any neighbor `v'` of `v`.
    - Valid only if `v' != u`.
    - New state: `(u, v')`.

### Winning/Losing Positions

- **Losing:** No valid moves exist.
- **Winning:** There exists at least one move to a **Losing** state.
- **Losing:** All reachable states are **Winning**.

Since it's a DAG, there are no cycles, so we can use Memoization or simple recursion.

### Complexity

- **States:** `N * N`.
- **Transitions per state:** `deg(u) + deg(v)`.
- **Total Complexity:** `O(N * (N + M))`.
- With `N=100`, this is roughly `100 * 2100 = 2.1 * 10^5` operations. Very fast.

![Algorithm Visualization](../images/GMT-011/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** 4 nodes, edges 1->2, 2->3, 1->3. Tokens at 1, 2.
1.  State (1, 2).
2.  P1 moves 1->3. New state (3, 2).
3.  P2 at (3, 2).
    - Token at 3: No moves.
    - Token at 2: Move to 3? Blocked.
4.  P2 has no moves. P2 loses.
5.  P1 wins.

## ✅ Proof of Correctness

- **Impartial Game:** Moves depend only on state.
- **Finite:** DAG ensures no infinite play.
- **Memoization:** Correctly computes Win/Loss values.

## 💡 Interview Extensions

- **Extension 1:** What if graph has cycles?
  - *Answer:* Can have draws. Use iterative updates or graph coloring.
- **Extension 2:** What if we have K tokens?
  - *Answer:* State space `N^K`. Exponential.

### Common Mistakes

1.  **Ignoring Blocking:**
    - ❌ Wrong: Treating tokens as independent games.
    - ✅ Correct: Checking `next != other_pos`.
2.  **Order Matters:**
    - ❌ Wrong: Assuming `(u, v)` is different from `(v, u)` in logic (it's symmetric, but implementation usually handles ordered pair).
    - ✅ Correct: Since players can pick *either* token, `(u, v)` is effectively the same set as `(v, u)`.

## Related Concepts

- **Graph Games**
- **Memoization**
