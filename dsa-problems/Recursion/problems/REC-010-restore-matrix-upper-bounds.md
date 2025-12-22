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
    public int[][] restoreMatrix(int[] rowSums, int[] colSums, int[][] bounds) {
        // Your implementation here
        return new int[0][0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int c = sc.nextInt();
        int[] rowSums = new int[r];
        int[] colSums = new int[c];
        for (int i = 0; i < r; i++) rowSums[i] = sc.nextInt();
        for (int j = 0; j < c; j++) colSums[j] = sc.nextInt();
        int[][] bounds = new int[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) bounds[i][j] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[][] result = solution.restoreMatrix(rowSums, colSums, bounds);
        if (result.length == 0) {
            System.out.println("NONE");
        } else {
            for (int i = 0; i < r; i++) {
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < c; j++) {
                    if (j > 0) sb.append(' ');
                    sb.append(result[i][j]);
                }
                System.out.println(sb.toString());
            }
        }
        sc.close();
    }
}
```

### Python

```python
def restore_matrix(row_sums: list[int], col_sums: list[int], bounds: list[list[int]]) -> list[list[int]]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    r = int(next(it))
    c = int(next(it))
    row_sums = [int(next(it)) for _ in range(r)]
    col_sums = [int(next(it)) for _ in range(c)]
    bounds = [[int(next(it)) for _ in range(c)] for _ in range(r)]

    result = restore_matrix(row_sums, col_sums, bounds)
    if not result:
        print("NONE")
    else:
        for row in result:
            print(" ".join(str(x) for x in row))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> restoreMatrix(const vector<int>& rowSums, const vector<int>& colSums, const vector<vector<int>>& bounds) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r, c;
    if (!(cin >> r >> c)) return 0;
    vector<int> rowSums(r), colSums(c);
    for (int i = 0; i < r; i++) cin >> rowSums[i];
    for (int j = 0; j < c; j++) cin >> colSums[j];
    vector<vector<int>> bounds(r, vector<int>(c));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) cin >> bounds[i][j];
    }

    Solution solution;
    vector<vector<int>> result = solution.restoreMatrix(rowSums, colSums, bounds);
    if (result.empty()) {
        cout << "NONE\n";
    } else {
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (j) cout << ' ';
                cout << result[i][j];
            }
            cout << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  restoreMatrix(rowSums, colSums, bounds) {
    // Your implementation here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const r = parseInt(data[idx++], 10);
  const c = parseInt(data[idx++], 10);
  const rowSums = [];
  const colSums = [];
  for (let i = 0; i < r; i++) rowSums.push(parseInt(data[idx++], 10));
  for (let j = 0; j < c; j++) colSums.push(parseInt(data[idx++], 10));
  const bounds = [];
  for (let i = 0; i < r; i++) {
    const row = [];
    for (let j = 0; j < c; j++) row.push(parseInt(data[idx++], 10));
    bounds.push(row);
  }

  const solution = new Solution();
  const result = solution.restoreMatrix(rowSums, colSums, bounds);
  if (result.length === 0) {
    console.log("NONE");
  } else {
    console.log(result.map((row) => row.join(" ")).join("\n"));
  }
});
```
