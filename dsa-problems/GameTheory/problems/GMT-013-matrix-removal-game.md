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
time_limit: 1000
memory_limit: 256
---

# GMT-013: Matrix Removal Game

## Problem Statement

You are given an `N x M` matrix of integers.
Two players, Maximizer (P1) and Minimizer (P2), take turns making a move.
In each turn, a player must choose to remove one of the following:
1.  The **first row** (topmost).
2.  The **last row** (bottommost).
3.  The **first column** (leftmost).
4.  The **last column** (rightmost).

The game ends when only a single cell `(1 x 1)` remains.
The value of this remaining cell is the score of the game.
Maximizer wants to maximize this score, while Minimizer wants to minimize it.

Determine the final score of the game assuming both players play optimally.
Maximizer goes first.

![Problem Illustration](../images/GMT-013/problem-illustration.png)

## Input Format

- The first line contains two integers `N` and `M`.
- The next `N` lines each contain `M` integers, representing the matrix.

## Output Format

- Return the final score.

## Constraints

- `1 <= N, M <= 20`
- `-10^9 <= Matrix[i][j] <= 10^9`

## Example

**Input:**
```
2 2
10 0
5 5
```

**Output:**
```
5
```

**Explanation:**
- Matrix:
  ```
  10 0
  5  5
  ```
- Maximizer (P1) moves first.
  - Option A: Remove Top Row (`10 0`). Remaining: `[5 5]`.
    - Minimizer (P2) moves.
      - Remove Left (`5`): Remaining `5`.
      - Remove Right (`5`): Remaining `5`.
    - Result: 5.
  - Option B: Remove Bottom Row (`5 5`). Remaining: `[10 0]`.
    - Minimizer (P2) moves.
      - Remove Left (`10`): Remaining `0`.
      - Remove Right (`0`): Remaining `10`.
    - Minimizer chooses `0`. Result: 0.
  - Option C: Remove Left Col (`10 5`). Remaining: `[0 5]^T`.
    - Minimizer chooses `0`. Result: 0.
  - Option D: Remove Right Col (`0 5`). Remaining: `[10 5]^T`.
    - Minimizer chooses `5`. Result: 5.
- Maximizer chooses Option A or D to get score 5.

![Example Visualization](../images/GMT-013/example-1.png)

## Notes

- The game always lasts exactly `(N - 1) + (M - 1)` turns.
- Use Minimax algorithm with Memoization.

## Related Topics

Game Theory, Minimax, Dynamic Programming

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int matrixGame(int n, int m, int[][] matrix) {
        // Implementation here
        return 0;
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

def matrix_game(n: int, m: int, matrix: List[List[int]]) -> int:
    # Implementation here
    return 0

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
public:
    int matrixGame(int n, int m, vector<vector<int>>& matrix) {
        // Implementation here
        return {};
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
    // Implementation here
    return null;
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
