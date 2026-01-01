---
problem_id: GMT_DIVISOR_TURN__6832
display_id: GMT-006
slug: divisor-turn-game
title: "Divisor Turn Game"
difficulty: Medium
difficulty_score: 45
topics:
  - Game Theory
  - Number Theory
  - Dynamic Programming
tags:
  - impartial-game
  - divisors
  - memoization
premium: true
subscription_tier: basic
---

# GMT-006: Divisor Turn Game

## 📋 Problem Summary

Starting from a number `n`, each move replaces `n` with a proper divisor
`d` where `1 < d < n`. If no such divisor exists (i.e., `n` is prime), you lose.
Determine if the first player wins.

## 🌍 Real-World Scenario

**Scenario Title:** The Molecular Breakdown

Imagine a molecule that can be broken down into smaller stable components (factors). You and a rival scientist are taking turns breaking it down. The one who is left with an "atomic" component (prime number) that cannot be broken down further loses the grant (or wins, depending on perspective - here, stuck means lose).

**Why This Problem Matters:**

- **Number Theory in Games:** It combines factorization with game states.
- **DAG Structure:** The divisor lattice forms a DAG, allowing DP.

![Real-World Application](../images/GMT-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Divisor Lattice

```
n = 12
Divisors > 1: 2, 3, 4, 6

Moves:
- 12 -> 6
- 12 -> 4
- 12 -> 3
- 12 -> 2

Analysis:
- 2 (Prime) -> Losing (L)
- 3 (Prime) -> Losing (L)
- 4 -> 2 (L) -> Winning (W)
- 6 -> 2 (L) or 3 (L) -> Winning (W)
- 12 -> 4 (W), 6 (W), 3 (L), 2 (L).
  - Since 12 can move to 2 (L) or 3 (L), 12 is Winning (W).
```

## ✅ Input/Output Clarifications

- **Proper Divisor:** `d < n`.
- **Constraint:** `d > 1`.
- **Primes:** Have no valid moves.

## Optimal Approach

### Key Insight

We can use **Memoization** or **DP**.
Since `n` goes up to `10^6`, we can precompute the status for all numbers or use recursion with memoization.
Given multiple test cases are not the issue here (single input), recursion is fine.
However, if we want to be safe, a simple recursive function `solve(n)`:
- Find all proper divisors `d > 1`.
- If any `solve(d)` returns "Second" (Losing), then `solve(n)` returns "First" (Winning).
- If all `solve(d)` return "First", then `solve(n)` returns "Second".

Optimization:
- Iterate `i` from 2 to `sqrt(n)`.
- If `i` divides `n`:
  - `d1 = i`. Check `solve(d1)`.
  - `d2 = n/i`. Check `solve(d2)`.
- If no divisors found, `n` is prime -> "Second".

### Algorithm

1.  `memo` map or array.
2.  `solve(n)`:
    - If `n` in `memo`, return.
    - Iterate `i` from 2 to `sqrt(n)`.
    - If `n % i == 0`:
        - `d1 = i`. If `!solve(d1)` -> return True.
        - `d2 = n/i`. If `d2 < n` (always true for i >= 2) and `!solve(d2)` -> return True.
    - Return False.

### Time Complexity

- **O(N * sqrt(N))** worst case without memoization, but with memoization, we visit each state once.
- Finding divisors takes `O(sqrt(N))`.
- Total complexity roughly `O(N * sqrt(N))`? No, sum of divisors is `O(N log N)`.
- For `N=10^6`, it's fast enough.

### Space Complexity

- **O(N)**: Memoization array.

![Algorithm Visualization](../images/GMT-006/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `6`

1.  `solve(2)`: Prime -> Loss.
2.  `solve(3)`: Prime -> Loss.
3.  `solve(6)`:
    - Divisor 2: `solve(2)` is Loss. Found move to Loss -> Win.
    - Divisor 3: `solve(3)` is Loss. Found move to Loss -> Win.
    - Result: Win.

## ✅ Proof of Correctness

- **Finite Game:** Numbers strictly decrease.
- **Impartial:** Moves depend only on `n`.
- **Memoization:** Correctly computes W/L based on successors.

## 💡 Interview Extensions

- **Extension 1:** What if we can subtract a divisor?
  - *Answer:* That's the standard "Divisor Subtraction Game" (usually depends on parity).
- **Extension 2:** What if `n` is up to `10^12`?
  - *Answer:* Too large for DP. Need to find a pattern or properties of prime factors.

### Common Mistakes

1.  **Considering 1 as a move:**
    - ❌ Wrong: `d > 1`.
2.  **Considering n as a move:**
    - ❌ Wrong: Proper divisor `d < n`.

## Related Concepts

- **Number Theory**
- **DAG Games**
