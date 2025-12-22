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

You are given an $N \times N$ chessboard with some blocked cells. A knight starts at `(0,0)`. The goal is to find a path that visits every **unblocked** cell exactly once. If no such path exists, output `NONE`.

## Real-World Scenario

Imagine a **Security Guard** patrolling a building. The building is a grid of rooms. Some rooms are under construction (blocked). The guard needs to visit every accessible room exactly once to check for intruders, starting from the entrance. The guard moves in an "L" shape (like a knight) because... well, maybe the corridors are weirdly shaped!

## Problem Exploration

### 1. Hamiltonian Path
This is a variation of the **Hamiltonian Path** problem on a graph.
-   Nodes: Unblocked cells.
-   Edges: Knight moves between unblocked cells.
-   Hamiltonian Path is NP-Complete. However, for small $N$ ($N \le 5$), backtracking is feasible.

### 2. Constraints
-   $N \le 5$: Total cells $\le 25$.
-   Backtracking depth is at most 25.
-   Branching factor is at most 8.
-   $8^{25}$ is huge, but the board is small and constrained, so many branches die quickly. Warnsdorff's Rule (heuristic) can speed it up, but for $N=5$, simple backtracking usually passes within 2 seconds.

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
To optimize, always move to the neighbor that has the **fewest** available onward moves. This heuristic keeps the knight from getting stuck in a corner early. For $N=5$, it's not strictly necessary but good to know.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private int rows, cols;
    private int[][] moves = {
        {-2, -1}, {-2, 1}, {-1, -2}, {-1, 2},
        {1, -2}, {1, 2}, {2, -1}, {2, 1}
    };

    public List<int[]> knightTour(int n, boolean[][] blocked) {
        rows = n;
        cols = n;
        int totalUnblocked = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!blocked[i][j]) totalUnblocked++;
            }
        }

        boolean[][] visited = new boolean[n][n];
        List<int[]> path = new ArrayList<>();
        
        // Start at 0,0
        visited[0][0] = true;
        path.add(new int[]{0, 0});
        
        if (dfs(0, 0, 1, totalUnblocked, blocked, visited, path)) {
            return path;
        }
        
        return new ArrayList<>();
    }

    private boolean dfs(int r, int c, int count, int target, boolean[][] blocked, 
                       boolean[][] visited, List<int[]> path) {
        if (count == target) {
            return true;
        }

        for (int[] m : moves) {
            int nr = r + m[0];
            int nc = c + m[1];

            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !blocked[nr][nc] && !visited[nr][nc]) {
                visited[nr][nc] = true;
                path.add(new int[]{nr, nc});
                if (dfs(nr, nc, count + 1, target, blocked, visited, path)) {
                    return true;
                }
                path.remove(path.size() - 1);
                visited[nr][nc] = false;
            }
        }
        return false;
    }
}
```

### Python

```python
def knight_tour(n: int, blocked: list[list[bool]]) -> list[tuple[int, int]]:
    total_unblocked = sum(not cell for row in blocked for cell in row)
    visited = [[False] * n for _ in range(n)]
    path = [(0, 0)]
    visited[0][0] = True
    
    moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]

    def dfs(r, c, count):
        if count == total_unblocked:
            return True
        
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not blocked[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = True
                path.append((nr, nc))
                if dfs(nr, nc, count + 1):
                    return True
                path.pop()
                visited[nr][nc] = False
        return False

    if dfs(0, 0, 1):
        return path
    return []
```

### C++

```cpp
#include <vector>
#include <utility>

using namespace std;

class Solution {
    int N;
    int moves[8][2] = {
        {-2, -1}, {-2, 1}, {-1, -2}, {-1, 2},
        {1, -2}, {1, 2}, {2, -1}, {2, 1}
    };

public:
    vector<pair<int, int>> knightTour(int n, const vector<vector<bool>>& blocked) {
        N = n;
        int totalUnblocked = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!blocked[i][j]) totalUnblocked++;
            }
        }

        vector<vector<bool>> visited(n, vector<bool>(n, false));
        vector<pair<int, int>> path;
        
        visited[0][0] = true;
        path.push_back({0, 0});
        
        if (dfs(0, 0, 1, totalUnblocked, blocked, visited, path)) {
            return path;
        }
        return {};
    }

    bool dfs(int r, int c, int count, int target, const vector<vector<bool>>& blocked, 
             vector<vector<bool>>& visited, vector<pair<int, int>>& path) {
        if (count == target) return true;

        for (auto& m : moves) {
            int nr = r + m[0];
            int nc = c + m[1];

            if (nr >= 0 && nr < N && nc >= 0 && nc < N && !blocked[nr][nc] && !visited[nr][nc]) {
                visited[nr][nc] = true;
                path.push_back({nr, nc});
                if (dfs(nr, nc, count + 1, target, blocked, visited, path)) return true;
                path.pop_back();
                visited[nr][nc] = false;
            }
        }
        return false;
    }
};
```

### JavaScript

```javascript
class Solution {
  knightTour(n, blocked) {
    let totalUnblocked = 0;
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (!blocked[i][j]) totalUnblocked++;
      }
    }

    const visited = Array.from({ length: n }, () => Array(n).fill(false));
    const path = [[0, 0]];
    visited[0][0] = true;

    const moves = [
      [-2, -1], [-2, 1], [-1, -2], [-1, 2],
      [1, -2], [1, 2], [2, -1], [2, 1]
    ];

    const dfs = (r, c, count) => {
      if (count === totalUnblocked) return true;

      for (const [dr, dc] of moves) {
        const nr = r + dr;
        const nc = c + dc;

        if (nr >= 0 && nr < n && nc >= 0 && nc < n && !blocked[nr][nc] && !visited[nr][nc]) {
          visited[nr][nc] = true;
          path.push([nr, nc]);
          if (dfs(nr, nc, count + 1)) return true;
          path.pop();
          visited[nr][nc] = false;
        }
      }
      return false;
    };

    if (dfs(0, 0, 1)) return path;
    return [];
  }
}
```

## Test Case Walkthrough

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
-   **Termination**: Path length increases by 1 each step. Max length $N^2$.

## Interview Extensions

1.  **Closed Tour?**
    -   Check if the last cell can reach the start cell `(0,0)`.
2.  **Larger N?**
    -   Use Warnsdorff's Rule.
    -   Divide and Conquer (split board into smaller tours and merge).

### C++ommon Mistakes

-   **Start Cell**: Ensure `(0,0)` is counted and visited initially.
-   **Blocked Check**: Don't move to blocked cells.
-   **Total Count**: Count unblocked cells correctly ($N^2 - B$).
