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
time_limit: 1000
memory_limit: 256
---

# GMT-005: Interval Removal Game

## Problem Statement

You are given a set of disjoint intervals on a line.
Two players take turns making a move.
In each turn, a player must choose one interval `[L, R]` and remove a sub-interval of **positive length** from it.
Removing a sub-interval might split the original interval into two smaller intervals, or reduce it to one smaller interval, or remove it completely.
The player who cannot make a valid move loses.

Determine if the first player has a winning strategy.

![Problem Illustration](../images/GMT-005/problem-illustration.png)

## Input Format

- The first line contains an integer `n`, the number of intervals.
- The next `n` lines each contain two integers `L` and `R`, representing the interval `[L, R]`.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= n <= 10^5`
- `0 <= L < R <= 10^9`
- Intervals are guaranteed to be disjoint.

## Example

**Input:**
```
2
0 2
5 6
```

**Output:**
```
First
```

**Explanation:**
- Interval 1: `[0, 2]`, length 2.
- Interval 2: `[5, 6]`, length 1.
- This is equivalent to a Nim game with piles of size 2 and 1.
- XOR sum = `2 ^ 1 = 3`.
- Since 3 > 0, First player wins.

![Example Visualization](../images/GMT-005/example-1.png)

## Notes

- The length of an interval `[L, R]` is `R - L`.
- The game is impartial and equivalent to Nim.

## Related Topics

Game Theory, Nim Game, XOR

---

## Solution Template

### Java


### Python


### C++


### JavaScript

