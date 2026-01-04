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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539110/dsa/gametheory_simple/bpm2a57mbbhujslczrkn.jpg)

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
import java.io.*;

class Solution {
    public long determineFinalScore(int n, int m, long[][] matrix) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nmLine = br.readLine();
        if (nmLine == null) return;
        String[] nmParts = nmLine.trim().split("\\s+");
        int n = Integer.parseInt(nmParts[0]);
        int m = Integer.parseInt(nmParts[1]);

        long[][] matrix = new long[n][m];
        for (int i = 0; i < n; i++) {
            String[] rowParts = br.readLine().trim().split("\\s+");
            for (int j = 0; j < m; j++) {
                matrix[i][j] = Long.parseLong(rowParts[j]);
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.determineFinalScore(n, m, matrix));
    }
}
```

### Python

```python
import sys

# Increase recursion depth for minimax
sys.setrecursionlimit(10000)

class Solution:
    def determine_final_score(self, n, m, matrix):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    matrix = []
    idx = 2
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(input_data[idx]))
            idx += 1
        matrix.append(row)

    sol = Solution()
    print(sol.determine_final_score(n, m, matrix))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long determineFinalScore(int n, int m, const vector<vector<long long>>& matrix) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> matrix(n, vector<long long>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    Solution sol;
    cout << sol.determineFinalScore(n, m, matrix) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  determineFinalScore(n, m, matrix) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);

  const matrix = [];
  for (let i = 0; i < n; i++) {
    const row = [];
    for (let j = 0; j < m; j++) {
      row.push(BigInt(input[idx++]));
    }
    matrix.push(row);
  }

  const sol = new Solution();
  const res = sol.determineFinalScore(n, m, matrix);
  console.log(res === null || res === undefined ? 0 : res.toString());
}

solve();
```
