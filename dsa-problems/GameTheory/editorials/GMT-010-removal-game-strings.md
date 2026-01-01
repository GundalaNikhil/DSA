---
problem_id: GMT_STRING_REMOVE__2847
display_id: GMT-010
slug: removal-game-strings
title: "Removal Game on Strings"
difficulty: Medium
difficulty_score: 45
topics:
  - Game Theory
  - Strings
tags:
  - impartial-game
  - sprague-grundy
  - ad-hoc
premium: true
subscription_tier: basic
---

# GMT-010: Removal Game on Strings

## 📋 Problem Summary

You are given `n` binary strings (`a`/`b`). Players take turns choosing a string,
removing a contiguous block of identical characters, and merging neighbors if
they become equal. The player who cannot move loses. Determine the winner.

## 🌍 Real-World Scenario

**Scenario Title:** The collapsing tunnel.

Imagine a tunnel supported by segments of different materials (Concrete, Steel, Concrete, Wood).
- Removing a segment causes the tunnel to collapse/compress.
- If two Concrete segments touch after a removal, they fuse into one stronger segment.
- You want to be the one to make the last safe removal.

![Real-World Application](../images/GMT-010/real-world-scenario.png)

## Detailed Explanation

### Key Observations

1. Compress each string into consecutive groups (blocks) of identical characters.
   Example: `aaabbbaabbb` -> `a, b, a, b` (4 groups).
2. The input alphabet is only `{a, b}`, so in the compressed form the groups
   **always alternate**.
3. If you remove a group in the middle, the two neighbors are the same
   character and merge, so the number of groups decreases by **2**.
4. If you remove an end group, the number of groups decreases by **1**.

So for a string with `k` groups, the moves are exactly:
- `k -> k - 1`
- `k -> k - 2`

This is a single-pile impartial game. The Grundy values are:
- `G(0)=0`, `G(1)=1`, `G(2)=0`
- For `k >= 3`, the pattern repeats with period 3:
  - `k % 3 == 1 -> 1`
  - `k % 3 == 2 -> 0`
  - `k % 3 == 0 -> 2`

Each string is a pile with size = number of groups. The overall game is the XOR
of the Grundy values across all strings.

### Algorithm


1.  For each string:
    - Compress to find number of groups `k`.
    - Compute `g = grundy(k)`.
    - `xor_sum ^= g`.
2.  Return "First" if `xor_sum > 0`.

### Time Complexity

- **O(N * |S|)** to parse strings.

### Space Complexity

- **O(1)** if processing on the fly.

![Algorithm Visualization](../images/GMT-010/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
Groups: 4.
`G(4) = 1`.
Result: First.

**Input:** `[aabb]`
Groups: 2.
`G(2) = 0`.
Result: Second.

## ✅ Proof of Correctness

- **Reduction:** Binary string -> Alternating groups -> Game on length `L`.
- **Moves:** `L -> L-1` or `L -> L-2`.
- **Pattern:** Verified manually.

## 💡 Interview Extensions

- **Extension 1:** What if alphabet size > 2?
  - *Answer:* Merging is not guaranteed. Much harder.
- **Extension 2:** What if we can remove non-contiguous characters?
  - *Answer:* Different game.

### Common Mistakes

1.  **Counting Characters:**
    - ❌ Wrong: Using string length.
    - ✅ Correct: Using group count.
2.  **Wrong Pattern:**
    - ❌ Wrong: `L % 3`.
    - ✅ Correct: `0, 1, 0, 2, 1, 0...`

## Related Concepts

- **Nim**
- **Sprague-Grundy**
- **String Compression**
