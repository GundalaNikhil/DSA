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
    public int[][] restoreMatrix(int[] rowSums, int[] colSums) {
        return null;
    }

    private boolean backtrack(int i, int j, int[] rowSums, int[] colSums, int[][] matrix) {
        int R = rowSums.length;
        int C = colSums.length;

        if (i == R) {
            // Check if all colSums are 0 (should be guaranteed if logic is correct)
            for (int val : colSums) if (val != 0) return false;
            return true;
        }

        int nextI = (j == C - 1) ? i + 1 : i;
        int nextJ = (j == C - 1) ? 0 : j + 1;

        // Optimization: If last column, value is fixed
        if (j == C - 1) {
            int val = rowSums[i]; // Must use all remaining row sum
            if (val < 0 || val > colSums[j]) return false;
            
            matrix[i][j] = val;
            rowSums[i] -= val;
            colSums[j] -= val;
            
            if (backtrack(nextI, nextJ, rowSums, colSums, matrix)) return true;
            
            rowSums[i] += val;
            colSums[j] += val;
            return false;
        }

        int maxVal = Math.min(rowSums[i], colSums[j]);

        // Try values from maxVal down to 0
        for (int val = maxVal; val >= 0; val--) {
            matrix[i][j] = val;
            rowSums[i] -= val;
            colSums[j] -= val;

            if (backtrack(nextI, nextJ, rowSums, colSums, matrix)) return true;

            rowSums[i] += val;
            colSums[j] += val;
        }

        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int R = sc.nextInt();
        int C = sc.nextInt();
        int[] rowSums = new int[R];
        int[] colSums = new int[C];
        for (int i = 0; i < R; i++) rowSums[i] = sc.nextInt();
        for (int i = 0; i < C; i++) colSums[i] = sc.nextInt();
        Solution sol = new Solution();
        int[][] res = sol.restoreMatrix(rowSums, colSums);
        if (res.length == 0) {
            System.out.println("IMPOSSIBLE");
        } else {
            for (int i = 0; i < res.length; i++) {
                for (int j = 0; j < res[i].length; j++) {
                    System.out.print(res[i][j]);
                    if (j + 1 < res[i].length) System.out.print(" ");
                }
                System.out.println();
            }
        }
        sc.close();
    }
}
```

### Python

```python
def restore_matrix(row_sums: list[int], col_sums: list[int]) -> list[list[int]]:
    return []
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 3:
        return
    r, c = map(int, lines[0].split())
    row_sums = list(map(int, lines[1].split()))
    col_sums = list(map(int, lines[2].split()))
    result = restore_matrix(row_sums, col_sums)
    if result:
        for row in result:
            print(' '.join(map(str, row)))
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int> rowSums, vector<int> colSums) {
        return {};
    }

private:
    bool backtrack(int r, int c, vector<int>& rowSums, vector<int>& colSums, vector<vector<int>>& matrix) {
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int R, C;
    if (!(cin >> R >> C)) return 0;
    vector<int> rowSums(R), colSums(C);
    for(int i=0; i<R; i++) cin >> rowSums[i];
    for(int i=0; i<C; i++) cin >> colSums[i];
    Solution sol;
    vector<vector<int>> res = sol.restoreMatrix(rowSums, colSums);
    if (res.empty()) {
        cout << "IMPOSSIBLE\n";
        return 0;
    }
    for(const auto& row : res) {
        for(size_t i=0; i<row.size(); i++) cout << row[i] << (i==row.size()-1?"":" ");
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  restoreMatrix(rowSums, colSums) {
    return 0;
  }
}

const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const R = parseInt(tokens[ptr++], 10);
    const C = parseInt(tokens[ptr++], 10);
    const rowSums = [];
    const colSums = [];
    for(let i=0; i<R; i++) rowSums.push(parseInt(tokens[ptr++], 10));
    for(let i=0; i<C; i++) colSums.push(parseInt(tokens[ptr++], 10));
    const sol = new Solution();
    const res = sol.restoreMatrix(rowSums, colSums);
    if (res.length === 0) {
        console.log("IMPOSSIBLE");
    } else {
        res.forEach(row => console.log(row.join(' ')));
    }
});
```

