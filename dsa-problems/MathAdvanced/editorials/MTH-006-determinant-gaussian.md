---
problem_id: MTH_DETERMINANT_GAUSSIAN__4917
display_id: MTH-006
slug: determinant-gaussian
title: "Determinant via Gaussian Elimination"
difficulty: Medium
difficulty_score: 55
topics:
  - MathAdvanced
  - Determinant
tags:
  - math-advanced
  - determinant
  - medium
premium: true
subscription_tier: basic
---

# MTH-006: Determinant via Gaussian Elimination

## 📋 Problem Summary

Given an `n x n` matrix, compute its determinant modulo a prime `MOD`.
- The determinant is a scalar value that describes properties of the matrix (e.g., invertibility).
- Naive calculation using cofactor expansion is `O(n!)`.
- We need an efficient `O(n^3)` approach.

## 🌍 Real-World Scenario

**Scenario Title:** The Volume of the Hyper-Parallelepiped

In data science and geometry, a matrix often represents a set of vectors.
- The determinant of a `2 x 2` matrix is the area of the parallelogram formed by its row vectors.
- The determinant of a `3 x 3` matrix is the volume of the parallelepiped.
- In `n` dimensions, it's the hyper-volume.

Calculating this volume is crucial for:
- **Change of Variables:** The Jacobian determinant in calculus scales volumes when transforming coordinates.
- **Machine Learning:** Determinants appear in multivariate Gaussian distributions (normalizing constant).
- **Cryptography:** Checking if a key matrix is invertible (non-zero determinant).

![Real-World Application](../images/MTH-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Gaussian Elimination

We want to transform the matrix into **Upper Triangular Form** (all zeros below diagonal).
The determinant of a triangular matrix is just the product of its diagonal elements.

```
Original:       Step 1 (Eliminate col 0):    Step 2 (Eliminate col 1):
[ 2  4  6 ]     [ 2  4  6 ]                  [ 2  4  6 ]
[ 1  5  9 ] --> [ 0  3  6 ]                  [ 0  3  6 ]
[ 3  1 -2 ]     [ 0 -5 -11]              --> [ 0  0 -1 ]

Det = 2 * 3 * (-1) = -6
```

**Row Operations & Determinant:**
1. **Swap Rows:** Determinant multiplies by `-1`.
2. **Multiply Row by `k`:** Determinant multiplies by `k`.
3. **Add multiple of row to another:** Determinant **does not change**.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Modulo:** All arithmetic is modulo `MOD`.
- **Division:** "Dividing" row `i` by `A[i][i]` means multiplying by modular inverse.
- **Zero Pivot:** If `A[i][i]` is 0, swap with a lower row `k` where `A[k][i] !=q 0`. If no such row exists, determinant is 0.
- **Sign:** Keep track of row swaps. If odd swaps, multiply result by `-1` (or `MOD-1`).

### Core Concept: Gaussian Elimination

Iterate through columns `j` from 0 to `n-1`:
1. **Pivot:** Find a row `i >= j` with non-zero entry in column `j`. Swap row `i` with row `j`.
2. **Eliminate:** For all rows `k > j`, subtract a multiple of row `j` from row `k` to make `A[k][j] = 0`.
   - Factor `f = A[k][j] * A[j][j]^-1`.
   - Row `k = Row  k - f * Row  j`.

## Naive Approach

### Intuition

Recursive Cofactor Expansion (Laplace Expansion).

### Algorithm

`Det(A) = sum (-1)^j A[0][j] * Det(Minor_0,j)`.

### Time Complexity

- **O(n!)**. Impossible for `n > 12`.

### Space Complexity

- **O(n^2)** stack depth.

## Optimal Approach

### Key Insight

Gaussian Elimination reduces the matrix to row echelon form in cubic time.

### Algorithm

1. Initialize `det = 1`.
2. Loop `i` from 0 to `n-1`:
   - Find pivot row `k` (`k >= i`) such that `matrix[k][i] != 0`.
   - If no pivot, return 0.
   - If `k != i`:
     - Swap rows `i` and `k`.
     - `det = -det`.
   - `det = det * matrix[i][i]`.
   - For elimination, use the pivot value directly without scaling row `i` (scaling would change the determinant).
     - `det = det * matrix[i][i]`.
     - `inv = modInverse(matrix[i][i])`.
     - For `j` from `i+1` to `n-1`:
       - `factor = matrix[j][i] * inv`.
       - `Row[j] = Row[j] - factor * Row[i]`.
3. Return `det`.

### Time Complexity

- **O(n^3)**.

### Space Complexity

- **O(n^2)** to store matrix.

![Algorithm Visualization](../images/MTH-006/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-006/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private long MOD;

    private long power(long base, long exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return res;
    }

    private long modInverse(long n) {
        return power(n, MOD - 2);
    }

    public long determinant_gaussian(int n, long mod, long[][] matrix) {
        this.MOD = mod;
        long det = 1;
        
        for (int i = 0; i < n; i++) {
            int pivot = i;
            while (pivot < n && matrix[pivot][i] == 0) pivot++;
            
            if (pivot == n) return 0; // Singular matrix
            
            if (pivot != i) {
                // Swap rows
                long[] temp = matrix[i];
                matrix[i] = matrix[pivot];
                matrix[pivot] = temp;
                det = (MOD - det) % MOD; // Flip sign
            }
            
            det = (det * matrix[i][i]) % MOD;
            long inv = modInverse(matrix[i][i]);
            
            for (int j = i + 1; j < n; j++) {
                if (matrix[j][i] != 0) {
                    long factor = (matrix[j][i] * inv) % MOD;
                    for (int k = i; k < n; k++) {
                        long sub = (factor * matrix[i][k]) % MOD;
                        matrix[j][k] = (matrix[j][k] - sub + MOD) % MOD;
                    }
                }
            }
        }
        
        return det;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        long MOD = sc.nextLong();
        
        long[][] matrix = new long[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextLong();
            }
        }
        
        Solution solution = new Solution();
        System.out.println(solution.determinant_gaussian(n, MOD, matrix));
        
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def determinant_gaussian(self, n: int, MOD: int, matrix: list[list[int]]) -> int:
        
        def power(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1: res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        def modInverse(n):
            return power(n, MOD - 2)

        det = 1
        
        for i in range(n):
            pivot = i
            while pivot < n and matrix[pivot][i] == 0:
                pivot += 1
            
            if pivot == n:
                return 0
            
            if pivot != i:
                matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
                det = (MOD - det) % MOD
            
            det = (det * matrix[i][i]) % MOD
            inv = modInverse(matrix[i][i])
            
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    factor = (matrix[j][i] * inv) % MOD
                    # Optimize: only update from column i onwards
                    # Python slicing is convenient but creates copies. Loop is better for O(1) space.
                    for k in range(i, n):
                        sub = (factor * matrix[i][k]) % MOD
                        matrix[j][k] = (matrix[j][k] - sub + MOD) % MOD
                        
        return det

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        MOD = int(next(iterator))
        
        matrix = []
        for _ in range(n):
            row = [int(next(iterator)) for _ in range(n)]
            matrix.append(row)
            
        sol = Solution()
        print(sol.determinant_gaussian(n, MOD, matrix))
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
    long long MOD;

    long long power(long long base, long long exp) {
        long long res = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    }

    long long modInverse(long long n) {
        return power(n, MOD - 2);
    }

public:
    long long determinant_gaussian(int n, long long mod, vector<vector<long long>>& matrix) {
        MOD = mod;
        long long det = 1;

        for (int i = 0; i < n; i++) {
            int pivot = i;
            while (pivot < n && matrix[pivot][i] == 0) pivot++;

            if (pivot == n) return 0;

            if (pivot != i) {
                swap(matrix[i], matrix[pivot]);
                det = (MOD - det) % MOD;
            }

            det = (det * matrix[i][i]) % MOD;
            long long inv = modInverse(matrix[i][i]);

            for (int j = i + 1; j < n; j++) {
                if (matrix[j][i] != 0) {
                    long long factor = (matrix[j][i] * inv) % MOD;
                    for (int k = i; k < n; k++) {
                        long long sub = (factor * matrix[i][k]) % MOD;
                        matrix[j][k] = (matrix[j][k] - sub + MOD) % MOD;
                    }
                }
            }
        }

        return det;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long MOD;
    if (!(cin >> n >> MOD)) return 0;

    vector<vector<long long>> matrix(n, vector<long long>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }

    Solution solution;
    cout << solution.determinant_gaussian(n, MOD, matrix) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  determinant_gaussian(n, MOD, matrix) {
    const P = BigInt(MOD);
    let det = 1n;
    
    // Convert matrix to BigInt
    const mat = matrix.map(row => row.map(BigInt));

    function power(base, exp) {
      let res = 1n;
      base %= P;
      while (exp > 0n) {
        if (exp % 2n === 1n) res = (res * base) % P;
        base = (base * base) % P;
        exp /= 2n;
      }
      return res;
    }

    function modInverse(n) {
      return power(n, P - 2n);
    }

    for (let i = 0; i < n; i++) {
      let pivot = i;
      while (pivot < n && mat[pivot][i] === 0n) pivot++;

      if (pivot === n) return 0;

      if (pivot !== i) {
        [mat[i], mat[pivot]] = [mat[pivot], mat[i]];
        det = (P - det) % P;
      }

      det = (det * mat[i][i]) % P;
      const inv = modInverse(mat[i][i]);

      for (let j = i + 1; j < n; j++) {
        if (mat[j][i] !== 0n) {
          const factor = (mat[j][i] * inv) % P;
          for (let k = i; k < n; k++) {
            const sub = (factor * mat[i][k]) % P;
            mat[j][k] = (mat[j][k] - sub + P) % P;
          }
        }
      }
    }

    return Number(det);
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
  let ptr = 0;
  
  const n = parseInt(data[ptr++]);
  const MOD = parseInt(data[ptr++]);
  
  const matrix = [];
  for(let i=0; i<n; i++) {
      const row = [];
      for(let j=0; j<n; j++) row.push(parseInt(data[ptr++]));
      matrix.push(row);
  }
  
  const solution = new Solution();
  console.log(solution.determinant_gaussian(n, MOD, matrix));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `2x2`, `MOD=10^9+7`, `[[1, 2], [3, 4]]`.

1. **i = 0:**
   - Pivot at `(0,0)` is 1 (non-zero).
   - `det = 1 * 1 = 1`.
   - `inv = 1`.
   - Eliminate row 1:
     - `factor = mat[1][0] * inv = 3 * 1 = 3`.
     - `mat[1][0] -= 3 * 1 = 0`.
     - `mat[1][1] -= 3 * 2 = 4 - 6 = -2`.
   - Matrix: `[[1, 2], [0, -2]]`.
2. **i = 1:**
   - Pivot at `(1,1)` is -2.
   - `det = 1 * (-2) = -2`.
   - No rows below to eliminate.
3. **Result:**
   - -2 modulo `10^9+7` is `1000000005`.

![Example Visualization](../images/MTH-006/example-1.png)

## ✅ Proof of Correctness

### Invariant
Gaussian elimination operations (adding a multiple of one row to another) preserve the determinant. Swapping rows negates it. The determinant of an upper triangular matrix is the product of its diagonal entries.

### Why the approach is correct
- By reducing to upper triangular form, we simplify the calculation from `O(n!)` to `O(n)` (product of diagonal), plus the `O(n^3)` cost of reduction.
- Modular arithmetic properties hold for all field operations (division is multiplication by inverse).

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Matrix Rank.
  - *Hint:* The number of non-zero rows after Gaussian elimination is the rank.
- **Extension 2:** System of Linear Equations.
  - *Hint:* Augment the matrix with the solution vector and solve.
- **Extension 3:** Matrix Inverse.
  - *Hint:* Augment with Identity matrix. If `A -> I`, then `I -> A^-1`.

### Common Mistakes to Avoid

1. **Integer Division**
   - ❌ Wrong: `matrix[j][i] / matrix[i][i]`.
   - ✅ Correct: Multiply by modular inverse.

2. **Modulus Handling**
   - ❌ Wrong: Forgetting `+ MOD` after subtraction.
   - ✅ Correct: `(a - b + MOD) % MOD`.

## Related Concepts

- **LU Decomposition:** A related factorization method.
- **Cramer's Rule:** Theoretical formula for inverse/solutions using determinants.
