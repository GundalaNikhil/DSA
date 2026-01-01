---
problem_id: GMT_KAYLES_GRAPH__8203
display_id: GMT-008
slug: kayles-on-graph
title: "Kayles on Graph"
difficulty: Hard
difficulty_score: 65
topics:
  - Game Theory
  - Graph Theory
  - Dynamic Programming
  - Bitmask
tags:
  - impartial-game
  - sprague-grundy
  - state-compression
premium: true
subscription_tier: basic
---

# GMT-008: Kayles on Graph

## 📋 Problem Summary

On each move, choose a node `u` in the graph and remove `u` and all its
neighbors. The player who cannot move loses. Determine whether the first player
wins.

## 🌍 Real-World Scenario

**Scenario Title:** The Network Disruption

Imagine a network of servers. You launch a virus at a server `u`. The virus destroys `u` and spreads to all directly connected servers, destroying them too. You and an opponent take turns launching viruses. The one who clears the last server wins (or the one who cannot find a target loses).

**Why This Problem Matters:**

- **Dominating Set:** The game is related to finding independent sets and dominating sets.
- **Bitmask DP:** Essential technique for small constraint problems involving subsets.

![Real-World Application](../images/GMT-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Move Effect

```
Graph: 0 -- 1 -- 2
       |
       3

Move: Pick 1.
- Removes 1.
- Removes neighbors of 1: 0, 2.
- Remaining: 3 (since 3 is connected to 0, not 1. 0 is removed, so 3 is not removed.)
  - Rule: "Removes u and all its neighbors".
  - Neighbors of 1 are 0, 2.
  - So 1, 0, 2 are removed.
  - 3 is NOT a neighbor of 1.
  - So 3 remains.
```

## ✅ Input/Output Clarifications

- **Available Node:** A node not yet removed.
- **Neighbors:** Neighbors in the original graph (or current? Neighbors are defined by edges. If `v` is removed, edge `u-v` is gone. But "neighbors" usually refers to the set of nodes adjacent to `u` in the current graph. Since we remove `u` and neighbors simultaneously, it's the same).

## Optimal Approach

### Key Insight

Since `n <= 15`, we can use a **Bitmask** to represent the set of available nodes.
`mask` has bit `i` set if node `i` is available.
We can compute `Win/Loss` (or Grundy numbers) for each mask.
Since it's a single game (not sum of games), boolean Win/Loss is sufficient.
`dp[mask] = True` if there exists a move `u` (where `mask & (1<<u)`) such that `dp[next_mask]` is False.
`next_mask = mask & ~((1<<u) | neighbors_mask[u])`.

### Algorithm

1.  Precompute `adj[u]` as a bitmask for each node `u`.
2.  Initialize `memo` array of size `2^n` with -1.
3.  `solve(mask)`:
    - If `mask == 0`, return False (Losing).
    - If `memo[mask]` != -1, return it.
    - Iterate `u` from 0 to `n-1`.
    - If `(mask >> u) & 1`:
        - `remove_mask = (1 << u) | adj[u]`.
        - `next_mask = mask & ~remove_mask`.
        - If `!solve(next_mask)`:
            - `memo[mask] = True`.
            - Return True.
    - `memo[mask] = False`.
    - Return False.

### Time Complexity

- **O(2^N * N)**: There are `2^N` states. For each state, we try `N` moves.
- `2^15 * 15 ≈ 32768 * 15 ≈ 5 * 10^5`. Very fast.

### Space Complexity

- **O(2^N)**: For memoization array.

![Algorithm Visualization](../images/GMT-008/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `3 nodes, 0-1, 1-2`

1.  Start `mask = 111` (binary 7).
2.  Moves:
    - Pick 0: Remove 0, 1. `next = 100` (4). `solve(4)` (Node 2 left).
      - From 4: Pick 2. `next = 0`. `solve(0)` is False.
      - So `solve(4)` is True.
    - Pick 1: Remove 1, 0, 2. `next = 0`.
      - `solve(0)` is False.
      - So `solve(7)` sees move to False. Returns True.
3.  Result: First.

## ✅ Proof of Correctness

- **Small N:** Allows full state exploration.
- **Bitmask:** Correctly tracks available nodes.
- **Impartial:** Standard W/L logic applies.

## 💡 Interview Extensions

- **Extension 1:** What if `N` is larger but graph is a tree?
  - *Answer:* Use Tree DP. `dp[u][state]` where state indicates if `u` or parent is removed.
- **Extension 2:** What if we calculate Grundy numbers?
  - *Answer:* Needed if graph is disconnected and we treat components as subgames.

### Common Mistakes

1.  **Removing wrong nodes:**
    - ❌ Wrong: Removing only `u`.
    - ✅ Correct: Remove `u` AND neighbors.
2.  **Bitwise precedence:**
    - ❌ Wrong: `mask & 1 << u` (can be interpreted as `(mask & 1) << u`).
    - ✅ Correct: `mask & (1 << u)`.

## Related Concepts

- **Bitmask DP**
- **Independent Set**
