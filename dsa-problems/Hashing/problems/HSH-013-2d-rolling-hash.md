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
import java.io.*;
import java.util.*;

class Solution {
    public boolean findMatrix(long[][] A, long[][] B) {
        //Implemention here
        return false;
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append(' ');
        }
        String input = sb.toString().trim();
        if (input.isEmpty()) return;
        String[] data = input.split("\\s+");
        int idx = 0;
        int n = Integer.parseInt(data[idx++]);
        int m = Integer.parseInt(data[idx++]);
        long[][] A = new long[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                A[i][j] = Long.parseLong(data[idx++]);
            }
        }
        int p = Integer.parseInt(data[idx++]);
        int q = Integer.parseInt(data[idx++]);
        long[][] B = new long[p][q];
        for (int i = 0; i < p; i++) {
            for (int j = 0; j < q; j++) {
                B[i][j] = Long.parseLong(data[idx++]);
            }
        }

        Solution solution = new Solution();
        boolean result = solution.findMatrix(A, B);
        System.out.print(result ? "true" : "false");
    }
}
```

### Python

```python
import sys

def find_matrix(A, B):
    # //Implemention here
    return False

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]);
    m = int(data[idx + 1]);
    idx += 2
    A = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(int(data[idx]));
            idx += 1
        A.append(row)
    p = int(data[idx]);
    q = int(data[idx + 1]);
    idx += 2
    B = []
    for _ in range(p):
        row = []
        for _ in range(q):
            row.append(int(data[idx]));
            idx += 1
        B.append(row)
    result = find_matrix(A, B)
    sys.stdout.write('true' if result else 'false')

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool find_matrix(const vector<vector<long long>>& A, const vector<vector<long long>>& B) {
    //Implemention here
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<long long>> A(n, vector<long long>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> A[i][j];
        }
    }
    int p, q;
    cin >> p >> q;
    vector<vector<long long>> B(p, vector<long long>(q));
    for (int i = 0; i < p; i++) {
        for (int j = 0; j < q; j++) {
            cin >> B[i][j];
        }
    }

    bool result = find_matrix(A, B);
    cout << (result ? "true" : "false");
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function findMatrix(A, B) {
  //Implemention here
  return false;
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const m = parseInt(data[idx++], 10);
const A = [];
for (let i = 0; i < n; i++) {
  const row = [];
  for (let j = 0; j < m; j++) {
    row.push(parseInt(data[idx++], 10));
  }
  A.push(row);
}
const p = parseInt(data[idx++], 10);
const q = parseInt(data[idx++], 10);
const B = [];
for (let i = 0; i < p; i++) {
  const row = [];
  for (let j = 0; j < q; j++) {
    row.push(parseInt(data[idx++], 10));
  }
  B.push(row);
}
const result = findMatrix(A, B);
process.stdout.write(result ? "true" : "false");
```

