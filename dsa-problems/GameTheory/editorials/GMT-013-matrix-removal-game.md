---
problem_id: GMT_MATRIX_REMOVE__1928
display_id: GMT-013
slug: matrix-removal-game
title: "Matrix Removal Game"
difficulty: Medium
difficulty_score: 60
topics:
  - Game Theory
  - Dynamic Programming
tags:
  - minimax
  - memoization
  - zero-sum
premium: true
subscription_tier: basic
---

# GMT-013: Matrix Removal Game

## 📋 Problem Summary

Players alternately remove the first/last row or first/last column of a matrix
until a single cell remains. Player 1 (Maximizer) wants that final value as
large as possible; Player 2 (Minimizer) wants it as small as possible. Output
the final value under optimal play.

## 🌍 Real-World Scenario

**Scenario Title:** The Land Auction.

Imagine a plot of land divided into a grid of values (oil reserves, gold, etc.).
- Two developers are negotiating boundaries.
- One wants to shrink the plot to a high-value center.
- The other wants to shrink it to a low-value swamp.
- They take turns ceding territory from the edges.

![Real-World Application](../images/GMT-013/real-world-scenario.png)

## Detailed Explanation

### State Representation

The state is defined by the current submatrix, represented by `(r1, r2, c1, c2)`.
- `r1`: Start row index.
- `r2`: End row index.
- `c1`: Start col index.
- `c2`: End col index.

### Transitions

From `(r1, r2, c1, c2)`:
1.  Remove Top: `(r1+1, r2, c1, c2)`
2.  Remove Bottom: `(r1, r2-1, c1, c2)`
3.  Remove Left: `(r1, r2, c1+1, c2)`
4.  Remove Right: `(r1, r2, c1, c2-1)`

### Turn Management

- Total moves made so far = `(N - (r2 - r1 + 1)) + (M - (c2 - c1 + 1))`.
- If `Total Moves` is Even -> Maximizer's turn.
- If `Total Moves` is Odd -> Minimizer's turn.

### Minimax Logic

- **Base Case:** If `r1 == r2` and `c1 == c2`, return `Matrix[r1][c1]`.
- **Maximizer:** `max(Rec(Top), Rec(Bottom), Rec(Left), Rec(Right))`.
- **Minimizer:** `min(Rec(Top), Rec(Bottom), Rec(Left), Rec(Right))`.

### Complexity

- **States:** `N * N * M * M`.
- **Transitions:** 4.
- **Time:** `O(N^2 * M^2)`.
- With `N, M <= 20`, `20^4 = 160,000`. Very fast.

![Algorithm Visualization](../images/GMT-013/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private int[][][][] memo;
    private int[][] mat;
    private int N, M;

    private int solve(int r1, int r2, int c1, int c2) {
        if (r1 == r2 && c1 == c2) return mat[r1][c1];
        if (memo[r1][r2][c1][c2] != Integer.MIN_VALUE) return memo[r1][r2][c1][c2];

        int movesMade = (N - (r2 - r1 + 1)) + (M - (c2 - c1 + 1));
        boolean isMax = (movesMade % 2 == 0);

        int res;
        if (isMax) {
            res = Integer.MIN_VALUE;
            if (r1 < r2) {
                res = Math.max(res, solve(r1 + 1, r2, c1, c2)); // Remove Top
                res = Math.max(res, solve(r1, r2 - 1, c1, c2)); // Remove Bottom
            }
            if (c1 < c2) {
                res = Math.max(res, solve(r1, r2, c1 + 1, c2)); // Remove Left
                res = Math.max(res, solve(r1, r2, c1, c2 - 1)); // Remove Right
            }
        } else {
            res = Integer.MAX_VALUE;
            if (r1 < r2) {
                res = Math.min(res, solve(r1 + 1, r2, c1, c2));
                res = Math.min(res, solve(r1, r2 - 1, c1, c2));
            }
            if (c1 < c2) {
                res = Math.min(res, solve(r1, r2, c1 + 1, c2));
                res = Math.min(res, solve(r1, r2, c1, c2 - 1));
            }
        }

        return memo[r1][r2][c1][c2] = res;
    }

    public int matrixGame(int n, int m, int[][] matrix) {
        this.N = n;
        this.M = m;
        this.mat = matrix;
        memo = new int[n][n][m][m];
        for (int[][][] row : memo) {
            for (int[][] col : row) {
                for (int[] arr : col) {
                    Arrays.fill(arr, Integer.MIN_VALUE);
                }
            }
        }
        return solve(0, n - 1, 0, m - 1);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] matrix = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    matrix[i][j] = sc.nextInt();
                }
            }

            Solution solution = new Solution();
            System.out.println(solution.matrixGame(n, m, matrix));
        }
        sc.close();
    }
}
```

### Python
```python
from typing import List
import sys

# Increase recursion depth
sys.setrecursionlimit(20000)

def matrix_game(n: int, m: int, matrix: List[List[int]]) -> int:
    memo = {}

    def solve(r1, r2, c1, c2):
        state = (r1, r2, c1, c2)
        if state in memo:
            return memo[state]
        
        if r1 == r2 and c1 == c2:
            return matrix[r1][c1]
        
        moves_made = (n - (r2 - r1 + 1)) + (m - (c2 - c1 + 1))
        is_max = (moves_made % 2 == 0)
        
        if is_max:
            res = -float('inf')
            if r1 < r2:
                res = max(res, solve(r1 + 1, r2, c1, c2))
                res = max(res, solve(r1, r2 - 1, c1, c2))
            if c1 < c2:
                res = max(res, solve(r1, r2, c1 + 1, c2))
                res = max(res, solve(r1, r2, c1, c2 - 1))
        else:
            res = float('inf')
            if r1 < r2:
                res = min(res, solve(r1 + 1, r2, c1, c2))
                res = min(res, solve(r1, r2 - 1, c1, c2))
            if c1 < c2:
                res = min(res, solve(r1, r2, c1 + 1, c2))
                res = min(res, solve(r1, r2, c1, c2 - 1))
        
        memo[state] = res
        return res

    return solve(0, n - 1, 0, m - 1)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        matrix = []
        for _ in range(n):
            row = []
            for _ in range(m):
                row.append(int(next(iterator)))
            matrix.append(row)
            
        print(matrix_game(n, m, matrix))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
    int memo[20][20][20][20];
    vector<vector<int>> mat;
    int N, M;
    bool visited[20][20][20][20];

    int solve(int r1, int r2, int c1, int c2) {
        if (r1 == r2 && c1 == c2) return mat[r1][c1];
        if (visited[r1][r2][c1][c2]) return memo[r1][r2][c1][c2];

        int movesMade = (N - (r2 - r1 + 1)) + (M - (c2 - c1 + 1));
        bool isMax = (movesMade % 2 == 0);

        int res;
        if (isMax) {
            res = INT_MIN;
            if (r1 < r2) {
                res = max(res, solve(r1 + 1, r2, c1, c2));
                res = max(res, solve(r1, r2 - 1, c1, c2));
            }
            if (c1 < c2) {
                res = max(res, solve(r1, r2, c1 + 1, c2));
                res = max(res, solve(r1, r2, c1, c2 - 1));
            }
        } else {
            res = INT_MAX;
            if (r1 < r2) {
                res = min(res, solve(r1 + 1, r2, c1, c2));
                res = min(res, solve(r1, r2 - 1, c1, c2));
            }
            if (c1 < c2) {
                res = min(res, solve(r1, r2, c1 + 1, c2));
                res = min(res, solve(r1, r2, c1, c2 - 1));
            }
        }

        visited[r1][r2][c1][c2] = true;
        return memo[r1][r2][c1][c2] = res;
    }

public:
    int matrixGame(int n, int m, vector<vector<int>>& matrix) {
        N = n;
        M = m;
        mat = matrix;
        // Initialize visited
        for(int i=0; i<n; ++i)
            for(int j=0; j<n; ++j)
                for(int k=0; k<m; ++k)
                    for(int l=0; l<m; ++l)
                        visited[i][j][k][l] = false;
                        
        return solve(0, n - 1, 0, m - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (cin >> n >> m) {
        vector<vector<int>> matrix(n, vector<int>(m));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> matrix[i][j];
            }
        }
        
        Solution solution;
        cout << solution.matrixGame(n, m, matrix) << "\n";
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  matrixGame(n, m, matrix) {
    const memo = new Map();

    const solve = (r1, r2, c1, c2) => {
      const key = `${r1},${r2},${c1},${c2}`;
      if (memo.has(key)) return memo.get(key);

      if (r1 === r2 && c1 === c2) return matrix[r1][c1];

      const movesMade = (n - (r2 - r1 + 1)) + (m - (c2 - c1 + 1));
      const isMax = (movesMade % 2 === 0);

      let res;
      if (isMax) {
        res = -Infinity;
        if (r1 < r2) {
          res = Math.max(res, solve(r1 + 1, r2, c1, c2));
          res = Math.max(res, solve(r1, r2 - 1, c1, c2));
        }
        if (c1 < c2) {
          res = Math.max(res, solve(r1, r2, c1 + 1, c2));
          res = Math.max(res, solve(r1, r2, c1, c2 - 1));
        }
      } else {
        res = Infinity;
        if (r1 < r2) {
          res = Math.min(res, solve(r1 + 1, r2, c1, c2));
          res = Math.min(res, solve(r1, r2 - 1, c1, c2));
        }
        if (c1 < c2) {
          res = Math.min(res, solve(r1, r2, c1 + 1, c2));
          res = Math.min(res, solve(r1, r2, c1, c2 - 1));
        }
      }

      memo.set(key, res);
      return res;
    };

    return solve(0, n - 1, 0, m - 1);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const n = parseInt(flatData[idx++]);
  const m = parseInt(flatData[idx++]);
  
  const matrix = [];
  for (let i = 0; i < n; i++) {
      const row = [];
      for (let j = 0; j < m; j++) {
          row.push(parseInt(flatData[idx++]));
      }
      matrix.push(row);
  }

  const solution = new Solution();
  console.log(solution.matrixGame(n, m, matrix));
});
```

## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `[[10, 0], [5, 5]]`
- Max removes Top -> `[5, 5]`. Min removes Left -> `5`.
- Max removes Bottom -> `[10, 0]`. Min removes Left -> `0`.
- Max removes Left -> `[0, 5]^T`. Min removes Top -> `0`.
- Max removes Right -> `[10, 5]^T`. Min removes Bottom -> `5`.
- Max chooses 5.

## ✅ Proof of Correctness

- **Minimax:** Standard algorithm for zero-sum perfect information games.
- **DAG:** Game state always shrinks, no cycles.
- **Optimality:** Assumes best play from both sides.

## 💡 Interview Extensions

- **Extension 1:** What if we can remove K rows?
  - *Answer:* Just more transitions.
- **Extension 2:** What if we want to maximize sum of removed elements?
  - *Answer:* Change payoff function.

### Common Mistakes

1.  **Wrong Turn:**
    - ❌ Wrong: Alternating based on recursion depth without checking total moves.
    - ✅ Correct: Check parity of total moves.
2.  **Base Case:**
    - ❌ Wrong: Stopping at empty matrix.
    - ✅ Correct: Stopping at 1x1.

## Related Concepts

- **Minimax**
- **Dynamic Programming**
