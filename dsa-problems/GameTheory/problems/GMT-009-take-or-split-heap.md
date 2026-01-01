---
problem_id: GMT_TAKE_OR_SPLIT__9382
display_id: GMT-009
slug: take-or-split-heap
title: "Take-or-Split Heap"
difficulty: Medium
difficulty_score: 50
topics:
  - Game Theory
  - Bitwise Operations
tags:
  - impartial-game
  - sprague-grundy
  - xor-sum
premium: true
subscription_tier: basic
time_limit: 1000
memory_limit: 256
---

# GMT-009: Take-or-Split Heap

## Problem Statement

You are given `n` heaps of stones.
Two players take turns making a move.
In each turn, a player must choose one heap with `x` stones (`x > 1`) and perform one of the following actions:
1.  **Remove** `k` stones from the heap, where `1 <= k < x`. The heap size becomes `x - k`.
2.  **Split** the heap into two non-empty heaps of sizes `a` and `b` such that `a + b = x`. The original heap is replaced by these two new heaps.

The player who cannot make a valid move loses.
(This happens when all heaps have size 1).

Determine if the first player has a winning strategy.

![Problem Illustration](../images/GMT-009/problem-illustration.png)

## Input Format

- The first line contains an integer `n`, the number of heaps.
- The second line contains `n` space-separated integers, the sizes of the heaps.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= n <= 10^5`
- `1 <= heap_size <= 10^9`

## Example

**Input:**
```
2
2 2
```

**Output:**
```
Second
```

**Explanation:**
- Heaps: `[2, 2]`.
- Moves from a heap of size 2:
  - Remove 1 -> Size 1.
  - Split 1+1 -> Sizes 1, 1.
- If P1 picks the first heap (size 2):
  - Option A: Remove 1. Heaps become `[1, 2]`.
  - Option B: Split 1+1. Heaps become `[1, 1, 2]`.
- From `[1, 2]`, P2 can pick the heap of size 2 and remove 1 -> `[1, 1]`.
  - Now heaps are `[1, 1]`. No valid moves (size 1 cannot be reduced or split). P1 loses.
- From `[1, 1, 2]`, P2 can pick size 2 and split -> `[1, 1, 1, 1]`.
  - No moves. P1 loses.
- Since P1 loses in all branches, P2 wins.

![Example Visualization](../images/GMT-009/example-1.png)

## Notes

- A heap of size 1 is a terminal state (Grundy value 0).
- The game is equivalent to Nim with modified pile sizes.

## Related Topics

Game Theory, Sprague-Grundy Theorem

---

## Solution Template

### Java


### Python


### C++


### JavaScript

