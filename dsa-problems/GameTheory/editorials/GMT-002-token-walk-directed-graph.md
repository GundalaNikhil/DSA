---
problem_id: GMT_TOKEN_WALK_DAG__2847
display_id: GMT-002
slug: token-walk-directed-graph
title: "Token Walk on Directed Graph"
difficulty: Medium
difficulty_score: 50
topics:
  - Game Theory
  - Graph Theory
  - Dynamic Programming
tags:
  - dag
  - topological-sort
  - memoization
premium: true
subscription_tier: basic
---

# GMT-002: Token Walk on Directed Graph

## 📋 Problem Summary

Given a Directed Acyclic Graph (DAG), determine for every node whether the first player wins or loses if the game starts at that node. Players take turns moving a token along directed edges. A player who cannot move loses. Because the graph is acyclic, the game always ends (no draws).

## 🌍 Real-World Scenario

**Scenario Title:** The Project Dependency Game

Imagine a project management tool where tasks are nodes and dependencies are edges. You and a colleague are assigning tasks. The rule is: you pick a task, then your colleague must pick a task that depends on yours, and so on. The person who picks the final task (completing the chain) wins the "efficiency bonus" (or in this game, the person who *cannot* pick loses, so the last person to pick wins).

**Why This Problem Matters:**

- **State Space Search:** It models decision-making in environments with irreversible actions (DAGs).
- **Backward Induction:** The core logic is working backwards from terminal states to determine the value of earlier states.

![Real-World Application](../images/GMT-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Winning/Losing Propagation

```
Graph: 0 -> 1 -> 2 <- 3
       |
       v
       4

Analysis:
- Node 2: No outgoing edges. Terminal. -> LOSING (L)
- Node 4: No outgoing edges. Terminal. -> LOSING (L)
- Node 1: Edge to 2 (L). Can move to L. -> WINNING (W)
- Node 3: Edge to 2 (L). Can move to L. -> WINNING (W)
- Node 0: Edges to 1 (W) and 4 (L).
  - Move to 1 gives opponent W (Bad).
  - Move to 4 gives opponent L (Good).
  - Since there is a move to L, 0 is -> WINNING (W)
```

## ✅ Input/Output Clarifications

- **Losing State:** A node with `out_degree = 0`.
- **Winning State:** A node with at least one neighbor that is a Losing State.
- **Losing State (Recursive):** A node where ALL neighbors are Winning States.

## Optimal Approach

### Key Insight

Since the graph is a DAG, there are no cycles. We can use **Memoization** (DFS) or **Topological Sort** (reverse order) to compute the state of each node.
Memoization is often easier to implement.

State Logic:
- `solve(u)`:
  - If `u` has no neighbors, return `False` (Losing).
  - Iterate through all neighbors `v` of `u`.
  - If `!solve(v)` (i.e., moving to `v` forces opponent to lose), then return `True` (Winning).
  - If all neighbors return `True` (all moves lead to opponent winning), return `False`.

### Algorithm

1.  Build adjacency list `adj`.
2.  Initialize a `memo` array with -1 (unknown).
3.  For each node `i` from 0 to `n-1`, call `dfs(i)`.
4.  `dfs(u)`:
    - If `memo[u]` != -1, return it.
    - `is_winning = False`
    - For `v` in `adj[u]`:
        - If `!dfs(v)`:
            - `is_winning = True`
            - Break
    - `memo[u] = is_winning`
    - Return `is_winning`

### Time Complexity

- **O(N + M)**: Each node and edge is visited once.

### Space Complexity

- **O(N + M)**: For adjacency list and recursion stack/memoization.

![Algorithm Visualization](../images/GMT-002/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `3 nodes, 0->1, 1->2`

1. `dfs(2)`: No neighbors. Returns `False` (Losing).
2. `dfs(1)`: Neighbor 2 is Losing, so `dfs(1)` returns `True` (Winning).
3. `dfs(0)`: Neighbor 1 is Winning, so all moves lead to Winning. `dfs(0)` returns `False` (Losing).

Result: `Losing Winning Losing`

## ✅ Proof of Correctness

- **Base Case:** Terminal nodes are Losing (no moves).
- **Inductive Step:**
  - If a node has a move to a Losing node, the current player takes that move, forcing the opponent into a Losing state. Thus, current is Winning.
  - If all moves lead to Winning nodes, the opponent will always receive a Winning state. Thus, current is Losing.
This covers all cases for a finite DAG.

## 💡 Interview Extensions

- **Extension 1:** What if the graph has cycles?
  - *Answer:* The game can be non-terminating (draw). Handle cycles (states that are neither W nor L).
- **Extension 2:** What if we want to calculate the Grundy number (Mex)?
  - *Answer:* `G(u) = mex({G(v) for v in adj[u]})`. Useful if playing sums of games.

### Common Mistakes

1.  **Confusing W/L:**
    - ❌ Wrong: "If I can move to a Winning node, I win."
    - ✅ Correct: "If I can move to a *Losing* node (for the opponent), I win."

2.  **Not handling disconnected components:**
    - The problem asks for the status of *each* node as a starting point, so we iterate all nodes.

## Related Concepts

- **Minimax**
- **Topological Sort**
- **Memoization**
