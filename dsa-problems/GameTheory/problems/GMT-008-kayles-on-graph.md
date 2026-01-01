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
time_limit: 2000
memory_limit: 256
---

# GMT-008: Kayles on Graph

## Problem Statement

You are given an undirected graph with `n` nodes and `m` edges.
Two players take turns making a move.
In each turn, a player must choose a node `u` that is currently available (not removed).
The player removes `u` and **all its neighbors** from the graph.
The player who cannot make a valid move loses.
(This happens when the graph is empty).

Determine if the first player has a winning strategy.

![Problem Illustration](../images/GMT-008/problem-illustration.png)

## Input Format

- The first line contains two integers `n` and `m`.
- The next `m` lines each contain two integers `u` and `v`, representing an edge between `u` and `v`.
- Nodes are 0-indexed.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= n <= 15`
- `0 <= m <= n * (n - 1) / 2`

## Example

**Input:**
```
3 2
0 1
1 2
```

**Output:**
```
First
```

**Explanation:**
- Graph: 0-1-2 (Path).
- Available moves:
  - Pick 0: Removes 0 and neighbor 1. Remaining: {2}.
    - From {2}, P2 picks 2 (removes 2). Graph empty. P2 wins.
    - So picking 0 leads to P2 winning. Bad for P1.
  - Pick 1: Removes 1 and neighbors 0, 2. Remaining: {}.
    - Graph empty. P2 has no moves. P2 loses.
    - So picking 1 leads to P1 winning.
  - Pick 2: Removes 2 and neighbor 1. Remaining: {0}.
    - From {0}, P2 picks 0. P2 wins. Bad for P1.
- Since P1 can pick 1 and win, P1 has a winning strategy.

![Example Visualization](../images/GMT-008/example-1.png)

## Notes

- This is a variation of the game Kayles played on a general graph.
- Since `n` is small, use bitmask DP with Sprague-Grundy theorem (or just Win/Loss since it's a single graph).

## Related Topics

Game Theory, Bitmask DP, Graph Theory

---

## Solution Template

### Java


### Python


### C++


### JavaScript

