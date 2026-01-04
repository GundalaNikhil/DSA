---
problem_id: HSH_2D_ROLLING_HASH__5849
display_id: HSH-013
slug: 2d-rolling-hash
title: "2D Rolling Hash for Matrix Match"
difficulty: Medium
difficulty_score: 60
topics:
  - Hashing
  - 2D Arrays
  - Pattern Matching
tags:
  - hashing
  - 2d-array
  - matrix
  - pattern-matching
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-013: 2D Rolling Hash for Matrix Match

## Problem Statement

Given a matrix `A` (size `n × m`) and a smaller matrix `B` (size `p × q`), determine if `B` appears as a submatrix in `A` using 2D rolling hash.

![Problem Illustration](../images/HSH-013/problem-illustration.png)

## Input Format

- First line: two integers `n m` (dimensions of matrix A)
- Next `n` lines: `m` space-separated integers (matrix A)
- Next line: two integers `p q` (dimensions of matrix B)
- Next `p` lines: `q` space-separated integers (matrix B)

## Output Format

- Single word: `true` if B is found in A, `false` otherwise

## Constraints

- `1 <= p <= n <= 1000`
- `1 <= q <= m <= 1000`
- `0 <= A[i][j], B[i][j] <= 10^9`

## Example

**Input:**

```
3 3
1 2 3
4 5 6
7 8 9
2 2
5 6
8 9
```

**Output:**

```
true
```

**Explanation:**

Matrix A (3×3):

```
1 2 3
4 5 6
7 8 9
```

Matrix B (2×2):

```
5 6
8 9
```

B appears in A starting at position (1, 1).

![Example Visualization](../images/HSH-013/example-1.png)

## Notes

- Compute 2D hash for matrix B
- Use 2D rolling hash to check all possible positions in A
- Hash function: combine row hashes with polynomial hash
- Time complexity: O(n × m)
- Space complexity: O(n × m)

## Related Topics

2D Hashing, Matrix Pattern Matching, Rolling Hash, Rabin-Karp 2D

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean findMatrixPattern(int n, int m, int[][] a, int p, int q, int[][] b) {
        // Implement here
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line1 = br.readLine();
        if (line1 == null) return;
        String[] dims1 = line1.trim().split("\\s+");
        int n = Integer.parseInt(dims1[0]);
        int m = Integer.parseInt(dims1[1]);

        int[][] a = new int[n][m];
        for (int i = 0; i < n; i++) {
            String[] row = br.readLine().trim().split("\\s+");
            for (int j = 0; j < m; j++) a[i][j] = Integer.parseInt(row[j]);
        }

        String line2 = br.readLine();
        if (line2 == null) return;
        String[] dims2 = line2.trim().split("\\s+");
        int p = Integer.parseInt(dims2[0]);
        int q_m = Integer.parseInt(dims2[1]);

        int[][] b = new int[p][q_m];
        for (int i = 0; i < p; i++) {
            String[] row = br.readLine().trim().split("\\s+");
            for (int j = 0; j < q_m; j++) b[i][j] = Integer.parseInt(row[j]);
        }

        Solution sol = new Solution();
        System.out.println(sol.findMatrixPattern(n, m, a, p, q_m, b));
    }
}
```

### Python

```python
import sys

class Solution:
    def find_matrix_pattern(self, n, m, a, p, q, b):
        # Implement here
        return False

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n = int(input_data[idx++])
    m = int(input_data[idx++])
    a = []
    for _ in range(n):
        a.append(list(map(int, input_data[idx:idx+m])))
        idx += m

    p = int(input_data[idx++])
    q = int(input_data[idx++])
    b = []
    for _ in range(p):
        b.append(list(map(int, input_data[idx:idx+q])))
        idx += q

    sol = Solution()
    print("true" if sol.find_matrix_pattern(n, m, a, p, q, b) else "false")

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
    bool findMatrixPattern(int n, int m, const vector<vector<int>>& a, int p, int q, const vector<vector<int>>& b) {
        // Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> a(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cin >> a[i][j];
    }

    int p, q;
    if (!(cin >> p >> q)) return 0;

    vector<vector<int>> b(p, vector<int>(q));
    for (int i = 0; i < p; i++) {
        for (int j = 0; j < q; j++) cin >> b[i][j];
    }

    Solution sol;
    cout << (sol.findMatrixPattern(n, m, a, p, q, b) ? "true" : "false") << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findMatrixPattern(n, m, a, p, q, b) {
    // Implement here
    return false;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) {
    const row = [];
    for (let j = 0; j < m; j++) row.push(parseInt(input[idx++]));
    a.push(row);
  }

  const p = parseInt(input[idx++]);
  const q = parseInt(input[idx++]);
  const b = [];
  for (let i = 0; i < p; i++) {
    const row = [];
    for (let j = 0; j < q; j++) row.push(parseInt(input[idx++]));
    b.push(row);
  }

  const sol = new Solution();
  console.log(sol.findMatrixPattern(n, m, a, p, q, b));
}

solve();
```
