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

class Solution {
    public boolean findMatrix(int[][] A, int[][] B) {
        //Implement here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] A = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    A[i][j] = sc.nextInt();
                }
            }
            
            int p = sc.nextInt();
            int q = sc.nextInt();
            int[][] B = new int[p][q];
            for (int i = 0; i < p; i++) {
                for (int j = 0; j < q; j++) {
                    B[i][j] = sc.nextInt();
                }
            }
            
            Solution solution = new Solution();
            System.out.println(solution.findMatrix(A, B));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def find_matrix(A: list, B: list) -> bool:
    # //Implement here
    return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        A = []
        for _ in range(n):
            row = []
            for _ in range(m):
                row.append(int(next(iterator)))
            A.append(row)
            
        p = int(next(iterator))
        q = int(next(iterator))
        B = []
        for _ in range(p):
            row = []
            for _ in range(q):
                row.append(int(next(iterator)))
            B.append(row)
            
        result = find_matrix(A, B)
        print("true" if result else "false")
    except StopIteration:
        pass

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
    bool findMatrix(vector<vector<int>>& A, vector<vector<int>>& B) {
        //Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    vector<vector<int>> A(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> A[i][j];
        }
    }
    
    int p, q;
    if (!(cin >> p >> q)) return 0;
    
    vector<vector<int>> B(p, vector<int>(q));
    for (int i = 0; i < p; i++) {
        for (int j = 0; j < q; j++) {
            cin >> B[i][j];
        }
    }
    
    Solution solution;
    cout << (solution.findMatrix(A, B) ? "true" : "false") << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findMatrix(A, B) {
    //Implement here
    return 0;
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
  let ptr = 0;
  const [n, m] = data[ptr++].split(" ").map(Number);
  
  const A = [];
  for (let i = 0; i < n; i++) {
    A.push(data[ptr++].split(" ").map(Number));
  }
  
  const [p, q] = data[ptr++].split(" ").map(Number);
  
  const B = [];
  for (let i = 0; i < p; i++) {
    B.push(data[ptr++].split(" ").map(Number));
  }
  
  const solution = new Solution();
  console.log(solution.findMatrix(A, B) ? "true" : "false");
});
```

