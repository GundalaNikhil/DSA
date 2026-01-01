---
title: Knight Tour With Blocked Cells
slug: knight-tour-blocked
difficulty: Medium
difficulty_score: 60
tags:
- Recursion
- Backtracking
- Knight Tour
problem_id: REC_KNIGHT_TOUR_BLOCKED__7742
display_id: REC-012
topics:
- Recursion
- Backtracking
- Chess
---
# Knight Tour With Blocked Cells - Editorial

## Problem Summary

You are given an `N x N` chessboard with some blocked cells. A knight starts at `(0,0)`. The goal is to find a path that visits every **unblocked** cell exactly once. If no such path exists, output `NONE`.


## Constraints

- `1 <= n <= 5`
- `0 <= b < n * n`
- `(0,0)` is guaranteed to be unblocked
## Real-World Scenario

Imagine a **Security Guard** patrolling a building. The building is a grid of rooms. Some rooms are under construction (blocked). The guard needs to visit every accessible room exactly once to check for intruders, starting from the entrance. The guard moves in an "L" shape (like a knight) due to the corridor layout.

## Problem Exploration

### 1. Hamiltonian Path
This is a variation of the **Hamiltonian Path** problem on a graph.
-   Nodes: Unblocked cells.
-   Edges: Knight moves between unblocked cells.
-   Hamiltonian Path is NP-Complete. However, for small `N` (`N <= 5`), backtracking is feasible.

### 2. Constraints
-   `N <= 5`: Total cells `<= 25`.
-   Backtracking depth is at most 25.
-   Branching factor is at most 8.
-   `8^25` is huge, but the board is small and constrained, so many branches die quickly. Warnsdorff's Rule (heuristic) can speed it up, but for `N=5`, simple backtracking usually passes within 2 seconds.

### 3. Base Case
-   If `path.size() == total_unblocked_cells`: Success!

## Approaches

### Approach 1: Backtracking (DFS)
`dfs(r, c, count)`
-   Mark `(r, c)` visited.
-   If `count == total_unblocked`: Return true.
-   Iterate 8 knight moves.
    -   If valid (in bounds, not blocked, not visited):
        -   Recurse `dfs(nr, nc, count + 1)`.
        -   If true, return true.
-   Backtrack: Unmark `(r, c)`. Return false.

### Approach 2: Warnsdorff's Rule (Heuristic)
To optimize, always move to the neighbor that has the **fewest** available onward moves. This heuristic keeps the knight from getting stuck in a corner early. For `N=5`, it's not strictly necessary but good to know.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `2`, Blocked: `(0,1), (1,0), (1,1)`
Unblocked: `(0,0)`. Total = 1.
1.  Start `(0,0)`. Count = 1.
2.  `count == total`. Return True.
**Path:** `0,0`.

**Input:** `3`, Blocked: None. Total = 9.
1.  Start `(0,0)`.
2.  Moves: `(1,2), (2,1)`.
3.  ... (Standard Knight Tour logic) ...
4.  Eventually finds a path covering all 9 cells.

## Proof of Correctness

The algorithm explores all valid knight paths from the start.
-   **Validity**: Checks bounds, blocked status, and visited status.
-   **Completeness**: DFS explores all branches.
-   **Termination**: Path length increases by 1 each step. Max length `N^2`.

## Interview Extensions

1.  **Closed Tour?**
    -   Check if the last cell can reach the start cell `(0,0)`.
2.  **Larger N?**
    -   Use Warnsdorff's Rule.
    -   Divide and Conquer (split board into smaller tours and merge).

### Common Mistakes

-   **Start Cell**: Ensure `(0,0)` is counted and visited initially.
-   **Blocked Check**: Don't move to blocked cells.
-   **Total Count**: Count unblocked cells correctly (`N^2 - B`).
