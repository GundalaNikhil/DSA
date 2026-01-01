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
time_limit: 1000
memory_limit: 256
---

# GMT-011: Blocking Tokens on DAG

## Problem Statement

You are given a Directed Acyclic Graph (DAG) with `n` nodes and `m` edges.
There are two tokens placed on distinct nodes `u` and `v`.
Two players take turns making a move.
In each turn, a player must choose **one** of the two tokens and move it along a directed edge to an adjacent node.
**Constraint:** A token cannot be moved to a node that is currently occupied by the other token.

The player who cannot make a valid move loses.
(This happens when both tokens are stuck, or the only available moves are blocked).

Determine if the first player has a winning strategy.

![Problem Illustration](../images/GMT-011/problem-illustration.png)

## Input Format

- The first line contains two integers `n` and `m`.
- The next `m` lines each contain two integers `a` and `b`, representing a directed edge from `a` to `b`.
- The last line contains two integers `u` and `v`, the starting positions of the two tokens.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `2 <= n <= 100`
- `0 <= m <= 2000`
- `1 <= u, v <= n`
- `u != v`
- The graph is a DAG (no cycles).

## Example

**Input:**
```
4 3
1 2
2 3
1 3
1 2
```

**Output:**
```
First
```

**Explanation:**
- Nodes: 1, 2, 3, 4.
- Edges: 1->2, 2->3, 1->3.
- Tokens at 1 and 2.
- Player 1 moves:
  - Move Token 1 (at 1):
    - To 2? Blocked (Token 2 is at 2).
    - To 3? Valid. State becomes {3, 2}.
  - Move Token 2 (at 2):
    - To 3? Valid. State becomes {1, 3}.
- If P1 moves 1->3 (State {2, 3}):
  - P2 moves:
    - Token at 2 can go to 3? Blocked.
    - Token at 3 has no moves.
  - P2 has no moves. P2 loses.
- So P1 wins by moving 1->3.

![Example Visualization](../images/GMT-011/example-1.png)

## Notes

- The game state is defined by the pair of positions `{pos1, pos2}`.
- Since it's a DAG, the game is guaranteed to end.
- `N` is small enough for `O(N^2)` solutions.

## Related Topics

Game Theory, Graph Traversal, Memoization

---

## Solution Template

### Java


### Python


### C++


### JavaScript

