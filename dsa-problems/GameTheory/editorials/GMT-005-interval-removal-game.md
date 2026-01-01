---
problem_id: GMT_INTERVAL_REMOVAL__5921
display_id: GMT-005
slug: interval-removal-game
title: "Interval Removal Game"
difficulty: Medium
difficulty_score: 40
topics:
  - Game Theory
  - Bitwise Operations
tags:
  - nim-game
  - sprague-grundy
  - xor-sum
premium: true
subscription_tier: basic
---

# GMT-005: Interval Removal Game

## 📋 Problem Summary

You are given disjoint intervals on a line. A move selects one interval and
removes any sub-interval of positive length, which can shrink the interval or
split it into two. The player who cannot move loses. Determine the winner.

## 🌍 Real-World Scenario

**Scenario Title:** The Land Developer

Imagine you own several strips of land. You and a competitor are zoning the land. In each turn, you must zone (remove) a piece of land from one strip. You can zone the middle, leaving two smaller strips, or an end. The person who zones the last piece wins the contract.

**Why This Problem Matters:**

- **Equivalence to Nim:** It demonstrates how a seemingly complex splitting game reduces to a simple Nim sum.
- **Grundy Values:** It reinforces the idea that `G(L) = L` for games where you can reach any state `x < L` (and combinations that XOR to any `x < L`).

![Real-World Application](../images/GMT-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Splitting an Interval

```
Interval: [0, 10] (Length 10)

Move: Remove [4, 6] (Length 2)
Result: [0, 4] (Length 4) AND [6, 10] (Length 4)

Grundy Analysis:
- G(10) = 10
- New State: G(4) ^ G(4) = 4 ^ 4 = 0.
- Since we can reach 0 from 10, G(10) must be > 0.
- In fact, for this game, G(L) = L.
```

## ✅ Input/Output Clarifications

- **Length:** `R - L`.
- **Positive Length:** You must remove at least 1 unit.

## Optimal Approach

### Key Insight

The Grundy value (or nim-value) of an interval of length `L` is simply `L`.
Why?
From a pile of size `L`, we can transition to any state `a ^ b` where `a + b < L`.
It can be proven by induction that `mex({ a ^ b | a + b < L }) = L`.
Thus, the game is equivalent to Nim with pile sizes equal to interval lengths.
The winning condition is `XOR_sum(lengths) > 0`.

### Algorithm

1.  Initialize `xor_sum = 0`.
2.  For each interval `[L, R]`:
    - `length = R - L`.
    - `xor_sum ^= length`.
3.  If `xor_sum > 0`, return "First".
4.  Else, return "Second".

### Time Complexity

- **O(N)**: We iterate through the intervals once.

### Space Complexity

- **O(1)**: Only a few variables used.

![Algorithm Visualization](../images/GMT-005/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `[0, 2], [5, 6]`

1.  Interval 1: `2 - 0 = 2`.
2.  Interval 2: `6 - 5 = 1`.
3.  XOR Sum: `2 ^ 1 = 3`.
4.  `3 > 0`, so "First".

## ✅ Proof of Correctness

The game is impartial.
The Grundy value of a sum of independent games is the XOR sum of their Grundy values.
For this specific game, `G(L) = L`.
Thus, the winning strategy is determined by the XOR sum of lengths.

## 💡 Interview Extensions

- **Extension 1:** What if we can only remove from the ends?
  - *Answer:* Then `G(L)` can be different (like standard Nim or subtraction game).
- **Extension 2:** What if intervals can merge?
  - *Answer:* Not possible given the rules (removing sub-interval keeps pieces separate).

### Common Mistakes

1.  **Using Integer:**
    - ❌ Wrong: `R` can be `10^9`, so lengths fit in integer, but XOR sum fits in integer. However, in some languages, be careful with overflow if summing (though XOR doesn't overflow).
2.  **Confusing Coordinates with Length:**
    - ❌ Wrong: XORing `R` or `L`. Must use `R - L`.

## Related Concepts

- **Nim Game**
- **XOR Sum**
