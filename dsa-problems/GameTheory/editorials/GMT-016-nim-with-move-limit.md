---
problem_id: GMT_NIM_LIMIT__7392
display_id: GMT-016
slug: nim-with-move-limit
title: "Nim with Move Limit"
difficulty: Easy
difficulty_score: 35
topics:
  - Game Theory
  - Math
tags:
  - impartial-game
  - sprague-grundy
  - xor-sum
premium: true
subscription_tier: basic
---

# GMT-016: Nim with Move Limit

## 📋 Problem Summary

You are given heaps `A[i]`, each with a per-heap removal limit `L[i]`. A move
chooses a heap and removes `k` stones where `1 <= k <= min(A[i], L[i])`. The
player with no moves loses. Determine the winner.

## 🌍 Real-World Scenario

**Scenario Title:** The Budgeted Project.

You have several project tasks (heaps) with remaining work hours.
- You can work on any task, but you have a daily limit (e.g., max 8 hours) for each specific task type.
- You want to be the one to complete the last task.

![Real-World Application](../images/GMT-016/real-world-scenario.png)

## Detailed Explanation

### Grundy Value Analysis

Consider a single heap of size `S` with limit `L`.
- `G(0) = 0`.
- `G(1) = mex(G(0)) = 1`.
- ...
- `G(L) = mex(0, 1, ..., L-1) = L`.
- `G(L+1) = mex(G(1), ..., G(L)) = mex(1, ..., L) = 0`.
  - Why? We can remove `1` to `L` stones.
  - Reachable states: `L, L-1, ..., 1`.
  - `0` is NOT reachable (requires removing `L+1` > `L`).
  - So `mex` is 0.
- `G(L+2) = mex(G(2), ..., G(L+1)) = mex(2, ..., L, 0) = 1`.
- The pattern repeats every `L+1`.
- `G(S) = S % (L + 1)`.

### Optimal Strategy

1.  Calculate `G(A[i]) = A[i] % (L[i] + 1)` for each heap.
2.  Compute XOR Sum of all `G` values.
3.  If XOR Sum > 0, First wins. Else, Second wins.

### Complexity

- **Time:** `O(N)`.
- **Space:** `O(1)`.

![Algorithm Visualization](../images/GMT-016/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `A=[10, 15], L=[3, 5]`
- `G(10) = 10 % 4 = 2`.
- `G(15) = 15 % 6 = 3`.
- `XOR = 2 ^ 3 = 1`.
- Result: First.

## ✅ Proof of Correctness

- **Periodicity:** The game on a single heap is periodic with period `L+1`.
- **Independence:** Heaps are independent, so XOR sum applies.

## 💡 Interview Extensions

- **Extension 1:** What if `L[i]` changes over time?
  - *Answer:* Much harder, not impartial.
- **Extension 2:** What if we must remove `k` such that `k >= L[i]`?
  - *Answer:* Different game, different pattern.

### Common Mistakes

1.  **Modulo:**
    - ❌ Wrong: `A[i] % L[i]`.
    - ✅ Correct: `A[i] % (L[i] + 1)`.
2.  **Limit:**
    - ❌ Wrong: Ignoring limit if `A[i] < L[i]`.
    - ✅ Correct: Formula works regardless, as `A % (L+1) == A` when `A <= L`.

## Related Concepts

- **Nim**
- **Sprague-Grundy**
