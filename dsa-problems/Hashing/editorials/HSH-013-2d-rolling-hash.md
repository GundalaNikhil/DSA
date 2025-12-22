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
---

# HSH-013: 2D Rolling Hash for Matrix Match

## 📋 Problem Summary

You are given a large matrix `A` ($N \times M$) and a smaller pattern matrix `B` ($P \times Q$).
Determine if `B` exists as a submatrix within `A`.

## 🌍 Real-World Scenario

**Scenario Title:** Image Recognition

Think of finding a specific icon (like a "Save" button) on a screenshot of a desktop.
- The screenshot is a large grid of pixels (Matrix A).
- The icon is a small grid of pixels (Matrix B).
- You want to find the coordinates where the icon appears.
- 2D Hashing allows scanning the image efficiently without comparing every pixel repeatedly.

![Real-World Application](../images/HSH-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: 2D Hashing

Matrix B (2x2):
```
1 2
3 4
```

**Step 1: Row Hashing**
Hash each row of B individually (using Base $B_1$).
- Row 0: Hash([1, 2]) = $H_{R0}$
- Row 1: Hash([3, 4]) = $H_{R1}$

**Step 2: Column Hashing**
Hash the column of row hashes (using Base $B_2$).
- Col Hash: Hash([$H_{R0}, H_{R1}$]) = $H_{Final}$

**Scanning Matrix A:**
1. Compute rolling hashes for all rows of A (window size $Q$).
   - This creates a temporary matrix of row hashes.
2. Compute rolling hashes for columns of this temporary matrix (window size $P$).
3. Compare result with $H_{Final}$.

### Key Concept: Separable Hashing

A 2D hash can be computed by hashing rows first, then hashing the resulting columns.
$H(A) = \sum_{i=0}^{P-1} \sum_{j=0}^{Q-1} A[i][j] \cdot B_1^{P-1-i} \cdot B_2^{Q-1-j}$.
This allows us to use the rolling hash technique in two dimensions sequentially.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Matrix A ($N \times M$), Matrix B ($P \times Q$).
- **Output:** Boolean.
- **Constraints:** $N, M \le 1000$. Values up to $10^9$.
- **Time Limit:** 2000ms. $O(NM)$ is required. Naive $O(NMPQ)$ is too slow ($10^{12}$ ops).

## Naive Approach

### Intuition

For every top-left position $(i, j)$ in A, check if the submatrix matches B.

### Time Complexity

- **O(N * M * P * Q)**: In worst case.

## Optimal Approach

### Key Insight

Use **Rabin-Karp** extended to 2D.
1. **Precompute Row Hashes:** For each row in A, compute rolling hashes of length $Q$. Store in `rowHashes[N][M-Q+1]`.
2. **Compute Column Hashes:** For each column in `rowHashes`, compute rolling hashes of length $P$.
3. **Compare:** The result corresponds to the hash of a $P \times Q$ submatrix. Compare with B's hash.

### Algorithm

1. Calculate hash of B ($H_B$).
   - Hash rows of B -> `tempB`.
   - Hash `tempB` column -> $H_B$.
2. Hash rows of A.
   - For each row $i$, compute rolling hashes of window size $Q$.
   - Store in `H[i][j]` (hash of $A[i][j \dots j+Q-1]$).
3. Hash columns of `H`.
   - For each column $j$, compute rolling hashes of window size $P$.
   - Result `Final[i][j]` is hash of submatrix at $(i, j)$.
4. If any `Final[i][j] == H_B`, return true.

### Time Complexity

- **O(NM)**: Each cell visited constant times.

### Space Complexity

- **O(NM)**: To store intermediate hashes. Can be optimized to $O(M)$ if processing row-by-row carefully.

![Algorithm Visualization](../images/HSH-013/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE1 = 313L; // For rows
    private static final long BASE2 = 317L; // For cols
    
    public boolean findMatrix(int[][] A, int[][] B) {
        int n = A.length, m = A[0].length;
        int p = B.length, q = B[0].length;
        
        if (p > n || q > m) return false;
        
        // 1. Compute Hash of B
        long targetHash = computeMatrixHash(B, p, q);
        
        // 2. Precompute Row Hashes of A
        // rowHashes[i][j] stores hash of A[i][j...j+q-1]
        long[][] rowHashes = new long[n][m - q + 1];
        long power1 = 1; // BASE1^(q-1)
        for (int k = 0; k < q - 1; k++) power1 = (power1 * BASE1) % MOD;
        
        for (int i = 0; i < n; i++) {
            long h = 0;
            // Initial window
            for (int k = 0; k < q; k++) {
                h = (h * BASE1 + A[i][k]) % MOD;
            }
            rowHashes[i][0] = h;
            
            // Slide
            for (int j = 1; j <= m - q; j++) {
                long remove = (A[i][j - 1] * power1) % MOD;
                h = (h - remove + MOD) % MOD;
                h = (h * BASE1 + A[i][j + q - 1]) % MOD;
                rowHashes[i][j] = h;
            }
        }
        
        // 3. Compute Column Hashes on rowHashes
        // We need to find hash of P rows in rowHashes column j
        long power2 = 1; // BASE2^(p-1)
        for (int k = 0; k < p - 1; k++) power2 = (power2 * BASE2) % MOD;
        
        for (int j = 0; j <= m - q; j++) {
            long h = 0;
            // Initial window of P rows
            for (int k = 0; k < p; k++) {
                h = (h * BASE2 + rowHashes[k][j]) % MOD;
            }
            if (h == targetHash) return true;
            
            // Slide down
            for (int i = 1; i <= n - p; i++) {
                long remove = (rowHashes[i - 1][j] * power2) % MOD;
                h = (h - remove + MOD) % MOD;
                h = (h * BASE2 + rowHashes[i + p - 1][j]) % MOD;
                
                if (h == targetHash) return true;
            }
        }
        
        return false;
    }
    
    private long computeMatrixHash(int[][] M, int p, int q) {
        long[] rowH = new long[p];
        for (int i = 0; i < p; i++) {
            long h = 0;
            for (int j = 0; j < q; j++) {
                h = (h * BASE1 + M[i][j]) % MOD;
            }
            rowH[i] = h;
        }
        
        long finalH = 0;
        for (int i = 0; i < p; i++) {
            finalH = (finalH * BASE2 + rowH[i]) % MOD;
        }
        return finalH;
    }
}

public class Main {
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

class Solution:
    def find_matrix(self, A: list, B: list) -> bool:
        n, m = len(A), len(A[0])
        p, q = len(B), len(B[0])
        
        if p > n or q > m:
            return False
            
        MOD = 10**9 + 7
        BASE1 = 313
        BASE2 = 317
        
        # Helper to compute hash of B
        def compute_target_hash():
            row_hashes = []
            for i in range(p):
                h = 0
                for j in range(q):
                    h = (h * BASE1 + B[i][j]) % MOD
                row_hashes.append(h)
            
            final_h = 0
            for h in row_hashes:
                final_h = (final_h * BASE2 + h) % MOD
            return final_h
            
        target_hash = compute_target_hash()
        
        # Precompute row hashes of A
        # row_hashes[i][j] is hash of A[i][j...j+q-1]
        row_hashes = [[0] * (m - q + 1) for _ in range(n)]
        power1 = pow(BASE1, q - 1, MOD)
        
        for i in range(n):
            h = 0
            for k in range(q):
                h = (h * BASE1 + A[i][k]) % MOD
            row_hashes[i][0] = h
            
            for j in range(1, m - q + 1):
                remove = (A[i][j - 1] * power1) % MOD
                h = (h - remove + MOD) % MOD
                h = (h * BASE1 + A[i][j + q - 1]) % MOD
                row_hashes[i][j] = h
                
        # Compute column hashes on row_hashes
        power2 = pow(BASE2, p - 1, MOD)
        
        for j in range(m - q + 1):
            h = 0
            for k in range(p):
                h = (h * BASE2 + row_hashes[k][j]) % MOD
            
            if h == target_hash:
                return True
                
            for i in range(1, n - p + 1):
                remove = (row_hashes[i - 1][j] * power2) % MOD
                h = (h - remove + MOD) % MOD
                h = (h * BASE2 + row_hashes[i + p - 1][j]) % MOD
                
                if h == target_hash:
                    return True
                    
        return False

def find_matrix(A: list, B: list) -> bool:
    solver = Solution()
    return solver.find_matrix(A, B)

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
    const long long MOD = 1e9 + 7;
    const long long BASE1 = 313;
    const long long BASE2 = 317;

public:
    bool findMatrix(vector<vector<int>>& A, vector<vector<int>>& B) {
        int n = A.size(), m = A[0].size();
        int p = B.size(), q = B[0].size();
        
        if (p > n || q > m) return false;
        
        long long targetHash = computeMatrixHash(B, p, q);
        
        vector<vector<long long>> rowHashes(n, vector<long long>(m - q + 1));
        long long power1 = 1;
        for (int k = 0; k < q - 1; k++) power1 = (power1 * BASE1) % MOD;
        
        for (int i = 0; i < n; i++) {
            long long h = 0;
            for (int k = 0; k < q; k++) {
                h = (h * BASE1 + A[i][k]) % MOD;
            }
            rowHashes[i][0] = h;
            
            for (int j = 1; j <= m - q; j++) {
                long long remove = (A[i][j - 1] * power1) % MOD;
                h = (h - remove + MOD) % MOD;
                h = (h * BASE1 + A[i][j + q - 1]) % MOD;
                rowHashes[i][j] = h;
            }
        }
        
        long long power2 = 1;
        for (int k = 0; k < p - 1; k++) power2 = (power2 * BASE2) % MOD;
        
        for (int j = 0; j <= m - q; j++) {
            long long h = 0;
            for (int k = 0; k < p; k++) {
                h = (h * BASE2 + rowHashes[k][j]) % MOD;
            }
            if (h == targetHash) return true;
            
            for (int i = 1; i <= n - p; i++) {
                long long remove = (rowHashes[i - 1][j] * power2) % MOD;
                h = (h - remove + MOD) % MOD;
                h = (h * BASE2 + rowHashes[i + p - 1][j]) % MOD;
                
                if (h == targetHash) return true;
            }
        }
        
        return false;
    }
    
    long long computeMatrixHash(const vector<vector<int>>& M, int p, int q) {
        vector<long long> rowH(p);
        for (int i = 0; i < p; i++) {
            long long h = 0;
            for (int j = 0; j < q; j++) {
                h = (h * BASE1 + M[i][j]) % MOD;
            }
            rowH[i] = h;
        }
        
        long long finalH = 0;
        for (int i = 0; i < p; i++) {
            finalH = (finalH * BASE2 + rowH[i]) % MOD;
        }
        return finalH;
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
    const n = A.length, m = A[0].length;
    const p = B.length, q = B[0].length;
    
    if (p > n || q > m) return false;
    
    const MOD = 1000000007n;
    const BASE1 = 313n;
    const BASE2 = 317n;
    
    const computeMatrixHash = (M, rows, cols) => {
      const rowH = new BigInt64Array(rows);
      for (let i = 0; i < rows; i++) {
        let h = 0n;
        for (let j = 0; j < cols; j++) {
          h = (h * BASE1 + BigInt(M[i][j])) % MOD;
        }
        rowH[i] = h;
      }
      let finalH = 0n;
      for (let i = 0; i < rows; i++) {
        finalH = (finalH * BASE2 + rowH[i]) % MOD;
      }
      return finalH;
    };
    
    const targetHash = computeMatrixHash(B, p, q);
    
    // rowHashes[i][j]
    const rowHashes = Array.from({ length: n }, () => new BigInt64Array(m - q + 1));
    
    let power1 = 1n;
    for (let k = 0; k < q - 1; k++) power1 = (power1 * BASE1) % MOD;
    
    for (let i = 0; i < n; i++) {
      let h = 0n;
      for (let k = 0; k < q; k++) {
        h = (h * BASE1 + BigInt(A[i][k])) % MOD;
      }
      rowHashes[i][0] = h;
      
      for (let j = 1; j <= m - q; j++) {
        let remove = (BigInt(A[i][j - 1]) * power1) % MOD;
        h = (h - remove + MOD) % MOD;
        h = (h * BASE1 + BigInt(A[i][j + q - 1])) % MOD;
        rowHashes[i][j] = h;
      }
    }
    
    let power2 = 1n;
    for (let k = 0; k < p - 1; k++) power2 = (power2 * BASE2) % MOD;
    
    for (let j = 0; j <= m - q; j++) {
      let h = 0n;
      for (let k = 0; k < p; k++) {
        h = (h * BASE2 + rowHashes[k][j]) % MOD;
      }
      if (h === targetHash) return true;
      
      for (let i = 1; i <= n - p; i++) {
        let remove = (rowHashes[i - 1][j] * power2) % MOD;
        h = (h - remove + MOD) % MOD;
        h = (h * BASE2 + rowHashes[i + p - 1][j]) % MOD;
        
        if (h === targetHash) return true;
      }
    }
    
    return false;
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

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
A (3x3), B (2x2).
A: `[[1,2,3], [4,5,6], [7,8,9]]`
B: `[[5,6], [8,9]]`

**B Hash:**
- Row 0 (5,6): $5B_1 + 6$.
- Row 1 (8,9): $8B_1 + 9$.
- Final: $(5B_1+6)B_2 + (8B_1+9)$.

**A Row Hashes (Window 2):**
- Row 0: `[1,2]`, `[2,3]`
- Row 1: `[4,5]`, `[5,6]`
- Row 2: `[7,8]`, `[8,9]`

**A Col Hashes (Window 2):**
- Col 0: `[Row0[0], Row1[0]]` -> `[1,2]` then `[4,5]`. No match.
- Col 1: `[Row0[1], Row1[1]]` -> `[2,3]` then `[5,6]`.
  - Next window: `[Row1[1], Row2[1]]` -> `[5,6]` then `[8,9]`.
  - This matches B! Return true.

## ✅ Proof of Correctness

### Invariant
The 2D hash uniquely (with high probability) represents the submatrix content.
The rolling hash correctly updates row hashes horizontally and column hashes vertically.

## 💡 Interview Extensions

- **Extension 1:** Count occurrences of B in A.
  - *Answer:* Increment counter instead of returning true.
- **Extension 2:** Find largest square submatrix appearing twice.
  - *Answer:* Binary search on size + 2D hashing.

### Common Mistakes to Avoid

1. **Order of Hashing**
   - ❌ Wrong: Hashing all cells in one giant polynomial.
   - ✅ Correct: Row-then-Column or Column-then-Row structure preserves 2D spatial relationships.
2. **Base Choice**
   - ❌ Wrong: Same base for rows and columns.
   - ✅ Correct: Different bases minimize collisions (e.g., `[1, 2], [3, 4]` vs `[1, 3], [2, 4]`).

## Related Concepts

- **Aho-Corasick 2D:** For multiple patterns.
- **Quadtrees:** For sparse matrices.
