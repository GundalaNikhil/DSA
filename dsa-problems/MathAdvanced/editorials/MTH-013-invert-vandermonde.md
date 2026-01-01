---
problem_id: MTH_INVERT_VANDERMONDE__8453
display_id: MTH-013
slug: invert-vandermonde
title: "Fast Inversion of Vandermonde Matrix"
difficulty: Hard
difficulty_score: 76
topics:
  - MathAdvanced
  - Fast
tags:
  - math-advanced
  - vandermonde-matrix
  - hard
premium: true
subscription_tier: basic
---

# MTH-013: Fast Inversion of Vandermonde Matrix

## 📋 Problem Summary

Given `n` distinct points `x_0, dots, x_n-1`, compute the inverse of the Vandermonde matrix `V` where `V_ij = x_i^j`.
- Standard matrix inversion is `O(n^3)`.
- We need a faster approach, ideally `O(n^2)`.

## 🌍 Real-World Scenario

**Scenario Title:** The Polynomial Interpolator

In scientific computing, we often need to fit a polynomial to a set of data points.
- Given points `(x_i, y_i)`, we want to find coefficients `c_j` such that `sum c_j x_i^j = y_i`.
- This is the linear system `V c = y`.
- Solving this requires `V^-1`.
- If we need to interpolate many different sets of `y` values for the *same* `x` locations (e.g., sensors at fixed locations reading different data over time), precomputing `V^-1` allows us to solve for coefficients in `O(n^2)` instead of re-solving the system every time.

**Why This Problem Matters:**

- **Coding Theory:** Reed-Solomon decoding involves solving systems with Vandermonde matrices.
- **Signal Processing:** Reconstruction of signals from non-uniform samples.
- **Numerical Analysis:** Stable methods for interpolation.

![Real-World Application](../images/MTH-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Matrix Structure


`V = \beginbmatrix
1 & x_0 & x_0^2 & \dots \\
1 & x_1 & x_1^2 & \dots \\
\vdots & \vdots & \vdots & \ddots
\endbmatrix`


The inverse `U = V^-1` has entries `U_ji` related to the coefficients of the Lagrange basis polynomials.
Specifically, the `i`-th column of `U` contains the coefficients of the polynomial `L_i(x)` such that `L_i(x_k) = delta_ik`.


`L_i(x) = \prod_j !=q i \fracx - x_jx_i - x_j`


### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `n` distinct values `x_i`.
- **Output:** The `n x n` inverse matrix.
- **Modulo:** `10^9+7`.
- **Constraints:** `n <= 2000`. `O(n^2)` is required.

### Core Concept: Lagrange Basis Coefficients

The polynomial `L_i(x)` can be written as:

`L_i(x) = \frac1\prod_j !=q i (x_i - x_j) \prod_j !=q i (x - x_j)`

Let `w_i = frac1prod_j !=q i (x_i - x_j)`.
Let `P(x) = prod_k=0^n-1 (x - x_k)`.
Then `prod_j !=q i (x - x_j) = fracP(x)x - x_i`.

So the `i`-th column of `V^-1` contains the coefficients of `w_i fracP(x)x - x_i`.

## Naive Approach

### Intuition

Gaussian Elimination.

### Algorithm

Standard row reduction.

### Time Complexity

- **O(n^3)**. Too slow for `n=2000` (`8 x 10^9` ops).

### Space Complexity

- **O(n^2)**.

## Optimal Approach

### Key Insight

Use the explicit formula for Lagrange coefficients.
1. Compute the master polynomial `P(x) = prod (x - x_k)`.
2. For each `i`, compute `P_i(x) = P(x) / (x - x_i)`. This division is simple synthetic division.
3. Scale coefficients by `w_i`.

### Algorithm

1. **Compute Coefficients of P(x):**
   - Start with `poly = [1]`.
   - For each `x_k`, multiply `poly` by `(x - x_k)`.
   - This takes `O(n^2)`.
2. **Compute Weights `w_i`:**
   - For each `i`, `w_i = prod_j !=q i (x_i - x_j)^-1`.
   - This takes `O(n^2)`.
3. **Compute Columns of Inverse:**
   - For each `i`:
     - Compute `Q(x) = P(x) / (x - x_i)`.
     - Since we know `P(x)`, we can do this division in `O(n)`.
     - Multiply each coeff of `Q(x)` by `w_i`.
     - Store in column `i`.

### Time Complexity

- **O(n^2)**.

### Space Complexity

- **O(n^2)** for the output matrix.

![Algorithm Visualization](../images/MTH-013/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-013/algorithm-steps.png)

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

    public long[][] invert_vandermonde(int n, long mod, long[] x) {
        this.MOD = mod;
        
        // 1. Compute P(x) = product(x - x_k)
        // P has degree n, so n+1 coefficients.
        long[] P = new long[n + 1];
        P[0] = 1; // Highest degree term coeff (monic)
        // Let's stick to P[0] is x^0, P[n] is x^n.
        // Initially P(x) = 1 (degree 0). P[0]=1.
        
        // (c0 + c1 x + ...) * ( -xk + x )
        // New c_i = c_{i-1} - xk * c_i
        
        Arrays.fill(P, 0);
        P[0] = 1;
        
        for (int k = 0; k < n; k++) {
            // Multiply by (x - x_k)
            // Shift right (multiply by x) and subtract x_k * P
            for (int i = k + 1; i >= 1; i--) {
                P[i] = (P[i - 1] - x[k] * P[i] % MOD + MOD) % MOD;
            }
            P[0] = (MOD - x[k] * P[0] % MOD) % MOD;
        }
        
        long[][] inv = new long[n][n];
        
        for (int i = 0; i < n; i++) {
            // 2. Compute w_i
            long prod = 1;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                prod = (prod * (x[i] - x[j] + MOD)) % MOD;
            }
            long w = modInverse(prod);
            
            // 3. Compute Q(x) = P(x) / (x - x_i)
            // Synthetic division of P by (x - x_i)
            // P(x) = Q(x) * (x - x_i)
            // Let Q(x) = q_0 + ... + q_{n-1} x^{n-1}
            // Coeff of x^n in P is 1. Coeff of x^n in Q*(x-xi) is q_{n-1}. So q_{n-1} = 1.
            // Generally, P[k] = q_{k-1} - x_i * q_k
            // So q_{k-1} = P[k] + x_i * q_k
            
            long q_k = 0; // Represents q_n (which is 0)
            // We iterate from highest degree n down to 1
            for (int k = n; k >= 1; k--) {
                // q_{k-1} corresponds to coeff of x^{k-1}
                long val = (P[k] + x[i] * q_k) % MOD;
                q_k = val;
                
                // Store in column i, row k-1
                // inv[row][col]
                inv[k - 1][i] = (val * w) % MOD;
            }
        }
        
        return inv;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        long MOD = sc.nextLong();
        
        long[] x = new long[n];
        for (int i = 0; i < n; i++) x[i] = sc.nextLong();
        
        Solution solution = new Solution();
        long[][] res = solution.invert_vandermonde(n, MOD, x);
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(res[i][j] + (j < n - 1 ? " " : ""));
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python
```python
import sys

class Solution:
    def invert_vandermonde(self, n: int, MOD: int, x: list[int]) -> list[list[int]]:
        
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

        # Compute P(x) = product(x - x_k)
        P = [0] * (n + 1)
        P[0] = 1
        
        for k in range(n):
            # Multiply by (x - x_k)
            # P_new[i] = P_old[i-1] - x_k * P_old[i]
            prev = P[0]
            P[0] = (MOD - x[k] * P[0] % MOD) % MOD
            for i in range(1, k + 2):
                temp = P[i]
                P[i] = (prev - x[k] * P[i] % MOD + MOD) % MOD
                prev = temp
                
        inv = [[0] * n for _ in range(n)]
        
        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j: continue
                prod = (prod * (x[i] - x[j] + MOD)) % MOD
            w = modInverse(prod)
            
            # Synthetic division P(x) / (x - x_i)
            q_k = 0
            for k in range(n, 0, -1):
                val = (P[k] + x[i] * q_k) % MOD
                q_k = val
                inv[k - 1][i] = (val * w) % MOD
                
        return inv

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        MOD = int(next(iterator))
        x = [int(next(iterator)) for _ in range(n)]
        
        sol = Solution()
        res = sol.invert_vandermonde(n, MOD, x)
        
        for row in res:
            print(*(row))
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
    vector<vector<long long>> invert_vandermonde(int n, long long mod, vector<long long>& x) {
        MOD = mod;

        vector<long long> P(n + 1, 0);
        P[0] = 1;

        for (int k = 0; k < n; k++) {
            for (int i = k + 1; i >= 1; i--) {
                P[i] = (P[i - 1] - x[k] * P[i] % MOD + MOD) % MOD;
            }
            P[0] = (MOD - x[k] * P[0] % MOD) % MOD;
        }

        vector<vector<long long>> inv(n, vector<long long>(n));

        for (int i = 0; i < n; i++) {
            long long prod = 1;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                prod = (prod * (x[i] - x[j] + MOD)) % MOD;
            }
            long long w = modInverse(prod);

            long long q_k = 0;
            for (int k = n; k >= 1; k--) {
                long long val = (P[k] + x[i] * q_k) % MOD;
                q_k = val;
                inv[k - 1][i] = (val * w) % MOD;
            }
        }

        return inv;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long MOD;
    if (!(cin >> n >> MOD)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; i++) cin >> x[i];

    Solution solution;
    vector<vector<long long>> res = solution.invert_vandermonde(n, MOD, x);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << res[i][j] << (j < n - 1 ? " " : "");
        }
        cout << "\n";
    }

    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  invert_vandermonde(n, MOD, x) {
    const P_MOD = BigInt(MOD);
    const X = x.map(BigInt);

    function power(base, exp) {
      let res = 1n;
      base %= P_MOD;
      while (exp > 0n) {
        if (exp % 2n === 1n) res = (res * base) % P_MOD;
        base = (base * base) % P_MOD;
        exp /= 2n;
      }
      return res;
    }

    function modInverse(n) {
      return power(n, P_MOD - 2n);
    }

    const P = new Array(n + 1).fill(0n);
    P[0] = 1n;

    for (let k = 0; k < n; k++) {
      for (let i = k + 1; i >= 1; i--) {
        P[i] = (P[i - 1] - X[k] * P[i] % P_MOD + P_MOD) % P_MOD;
      }
      P[0] = (P_MOD - X[k] * P[0] % P_MOD) % P_MOD;
    }

    const inv = Array.from({ length: n }, () => new Array(n).fill(0n));

    for (let i = 0; i < n; i++) {
      let prod = 1n;
      for (let j = 0; j < n; j++) {
        if (i === j) continue;
        prod = (prod * (X[i] - X[j] + P_MOD)) % P_MOD;
      }
      const w = modInverse(prod);

      let q_k = 0n;
      for (let k = n; k >= 1; k--) {
        const val = (P[k] + X[i] * q_k) % P_MOD;
        q_k = val;
        inv[k - 1][i] = (val * w) % P_MOD;
      }
    }

    return inv.map(row => row.map(val => Number(val)));
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
  
  const x = [];
  for(let i=0; i<n; i++) x.push(parseInt(data[ptr++]));
  
  const solution = new Solution();
  const res = solution.invert_vandermonde(n, MOD, x);
  
  for (let i = 0; i < n; i++) {
    console.log(res[i].join(" "));
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `x = [1, 2]`.
1. **Compute P(x):**
   - Init `P = [1, 0, 0]`.
   - `k=0, x[0]=1`: `P = [-1, 1, 0]`. (`(x-1) = -1 + x`)
   - `k=1, x[1]=2`: `P = [2, -3, 1]`. (`(x-1)(x-2) = x^2 - 3x + 2`)
2. **Column 0 (`x_0=1`):**
   - `w_0 = (1-2)^-1 = -1`.
   - `Q(x) = (x^2 - 3x + 2) / (x-1) = x - 2`.
   - Coeffs: `-2, 1`.
   - Scaled by `w_0`: `2, -1`.
   - Col 0: `[2, -1]^T`.
3. **Column 1 (`x_1=2`):**
   - `w_1 = (2-1)^-1 = 1`.
   - `Q(x) = (x^2 - 3x + 2) / (x-2) = x - 1`.
   - Coeffs: `-1, 1`.
   - Scaled by `w_1`: `-1, 1`.
   - Col 1: `[-1, 1]^T`.
4. **Result Matrix:**
   - Row 0: `[2, -1]`
   - Row 1: `[-1, 1]`
   - Matches example.

![Example Visualization](../images/MTH-013/example-1.png)

## ✅ Proof of Correctness

### Invariant
The columns of `V^-1` are the coefficients of the Lagrange basis polynomials.
The synthetic division correctly computes `P(x)/(x-x_i)`.

### Why the approach is correct
- By definition, `V x V^-1 = I`.
- The dot product of row `i` of `V` (powers of `x_i`) and column `j` of `V^-1` (coeffs of `L_j`) is `L_j(x_i)`, which is `delta_ij`.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Solve `V c = y` without explicit inverse.
  - *Hint:* This is just polynomial interpolation. `O(n^2)`.
- **Extension 2:** Transpose Inverse `V^-T y`.
  - *Hint:* Related to multipoint evaluation.
- **Extension 3:** Dynamic updates (add point).
  - *Hint:* Update Lagrange weights in `O(n)`.

### Common Mistakes to Avoid

1. **Polynomial Indexing**
   - ❌ Wrong: `P[i]` is coeff of `x^n-i`.
   - ✅ Correct: `P[i]` is coeff of `x^i`. Be consistent.

2. **Synthetic Division Loop**
   - ❌ Wrong: Iterate 0 to n.
   - ✅ Correct: Iterate n down to 1. `q_k-1` depends on `q_k`.

## Related Concepts

- **Lagrange Interpolation:** The theoretical basis.
- **Synthetic Division:** For polynomial division.
