---
problem_id: REC_RESTORE_MATRIX_UPPER_BOUNDS__2607
display_id: REC-010
slug: restore-matrix-upper-bounds
title: "Restore Matrix With Upper Bounds"
difficulty: Medium
difficulty_score: 56
topics:
  - Recursion
  - Backtracking
  - Matrices
tags:
  - recursion
  - backtracking
  - matrix
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# REC-010: Restore Matrix With Upper Bounds

## Problem Statement

You are given row sums, column sums, and per-cell upper bounds `u[i][j]` for an `r x c` matrix of non-negative integers.
Construct any matrix that satisfies all row sums, column sums, and bounds. If no matrix exists, output `NONE`.
![Problem Illustration](../images/REC-010/problem-illustration.png)

## Input Format

- First line: integers `r` and `c`
- Second line: `r` space-separated row sums
- Third line: `c` space-separated column sums
- Next `r` lines: `c` space-separated upper bounds `u[i][j]`

## Output Format

- If possible, output `r` lines each with `c` integers of a valid matrix
- Otherwise output `NONE`

## Constraints

- `1 <= r, c <= 6`
- `0 <= rowSum[i], colSum[j] <= 20`
- `0 <= u[i][j] <= 20`

## Example

**Input:**

```
2 2
3 4
4 3
2 3
3 4
```

**Output:**

```
2 1
2 2
```

**Explanation:**

Row sums: 2+1=3, 2+2=4. Column sums: 2+2=4, 1+2=3. All values respect bounds.

![Example Visualization](../images/REC-010/example-1.png)

## Notes

- Fill cells row by row with recursion
- Prune when any row or column sum becomes negative
- Bounds reduce the branching factor
- Any valid matrix is acceptable

## Related Topics

Backtracking, Constraint Satisfaction, Recursion

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void restoreMatrix(int r, int c, int[] rowSums, int[] colSums, int[][] bounds) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int r = sc.nextInt();
        int c = sc.nextInt();
        int[] rowSums = new int[r];
        for (int i = 0; i < r; i++) rowSums[i] = sc.nextInt();
        int[] colSums = new int[c];
        for (int i = 0; i < c; i++) colSums[i] = sc.nextInt();
        int[][] bounds = new int[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                bounds[i][j] = sc.nextInt();
            }
        }
        Solution sol = new Solution();
        sol.restoreMatrix(r, c, rowSums, colSums, bounds);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def restore_matrix(self, r, c, row_sums, col_sums, bounds):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    r = int(input_data[0])
    c = int(input_data[1])
    row_sums = [int(x) for x in input_data[2:2+r]]
    col_sums = [int(x) for x in input_data[2+r:2+r+c]]
    bounds = []
    idx = 2 + r + c
    for i in range(r):
        bounds.append([int(x) for x in input_data[idx:idx+c]])
        idx += c
    sol = Solution()
    sol.restore_matrix(r, c, row_sums, col_sums, bounds)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void restoreMatrix(int r, int c, vector<int>& rowSums, vector<int>& colSums, vector<vector<int>>& bounds) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int r, c;
    if (!(cin >> r >> c)) return 0;
    vector<int> rowSums(r), colSums(c);
    for (int i = 0; i < r; i++) cin >> rowSums[i];
    for (int i = 0; i < c; i++) cin >> colSums[i];
    vector<vector<int>> bounds(r, vector<int>(c));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) cin >> bounds[i][j];
    }
    Solution sol;
    sol.restoreMatrix(r, c, rowSums, colSums, bounds);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  restoreMatrix(r, c, rowSums, colSums, bounds) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  let idx = 0;
  const r = parseInt(input[idx++]);
  const c = parseInt(input[idx++]);
  const rowSums = [];
  for (let i = 0; i < r; i++) rowSums.push(parseInt(input[idx++]));
  const colSums = [];
  for (let i = 0; i < c; i++) colSums.push(parseInt(input[idx++]));
  const bounds = [];
  for (let i = 0; i < r; i++) {
    const row = [];
    for (let j = 0; j < c; j++) row.push(parseInt(input[idx++]));
    bounds.push(row);
  }
  const sol = new Solution();
  sol.restoreMatrix(r, c, rowSums, colSums, bounds);
}

solve();
```
