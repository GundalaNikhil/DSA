---
problem_id: MTH_MATRIX_EXP_LINEAR_RECURRENCE__6283
display_id: MTH-007
slug: matrix-exp-linear-recurrence
title: "Matrix Exponentiation for Linear Recurrence"
difficulty: Medium
difficulty_score: 58
topics:
  - MathAdvanced
  - Matrix
tags:
  - math-advanced
  - matrix-exponentiation
  - medium
premium: true
subscription_tier: basic
---

# MTH-007: Matrix Exponentiation for Linear Recurrence

## 📋 Problem Summary

Given a linear recurrence relation `a_n = c_0 a_n-1 + c_1 a_n-2 + dots + c_k-1 a_n-k` and initial terms `a_0, dots, a_k-1`, find the `n`-th term modulo `MOD`.
- `n` can be up to `10^18`.
- `k` is small (`<= 50`).

## 🌍 Real-World Scenario

**Scenario Title:** The Rabbit Population Explosion

Fibonacci's original problem was about rabbits: pairs breed, and after a month, the offspring also breed.
- `F_n = F_n-1 + F_n-2`.
- In ecology, population models often depend on the previous few years (e.g., salmon returning to spawn after 4 years).
- If we want to predict the population 1 billion years from now (or steps in a simulation), iterating one by one is too slow (`10^9` steps).
- Matrix Exponentiation allows us to "jump" through time, calculating the state at `t=10^18` in logarithmic time.

**Why This Problem Matters:**

- **Computer Graphics:** Transformations (rotation, scaling) are matrix multiplications. Repeated application is exponentiation.
- **Dynamic Programming:** Many DP problems on graphs or sequences with small states can be optimized from `O(N)` to `O(log N)` using matrices.
- **Cryptography:** Some stream ciphers use linear feedback shift registers (LFSRs), which are linear recurrences.

![Real-World Application](../images/MTH-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: State Transition

We represent the "state" at step `i` as a vector:

`V_i = [a_i, a_i-1, \dots, a_i-k+1]^T`


We want a matrix `T` such that `V_i+1 = T x V_i`.

For Fibonacci (`a_n = a_n-1 + a_n-2`):

`\beginbmatrix a_i+1 \\ a_i \endbmatrix = 
\beginbmatrix 1 & 1 \\ 1 & 0 \endbmatrix 
\beginbmatrix a_i \\ a_i-1 \endbmatrix`


To get to step `n`, we compute `V_n = T^n-k+1 x V_k-1`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Coefficients:** The problem gives `c_0, dots, c_k-1` corresponding to `a_n-1, dots, a_n-k`.
- **Base Cases:** If `n < k`, just return `a_n` directly.
- **Matrix Size:** `k x k`.
- **Complexity:** Matrix multiplication is `O(k^3)`. Exponentiation is `O(log n)`. Total `O(k^3 log n)`. With `k=50`, `k^3 = 125,000`, `log n ~= 60`. Total ops `~= 7.5 x 10^6`, well within time limit.

### Core Concept: Transition Matrix Construction

The first row of `T` represents the recurrence equation:
`a_n = c_0 a_n-1 + c_1 a_n-2 + dots + c_k-1 a_n-k`.
Row 0: `[c_0, c_1, dots, c_k-1]`.

The subsequent rows simply shift the values:
`a_n-1 = 1 * a_n-1`.
Row 1: `[1, 0, dots, 0]`.
Row 2: `[0, 1, dots, 0]`.
...
Row `k-1`: `[0, 0, dots, 1, 0]`.

## Naive Approach

### Intuition

Iterate from `k` to `n`.

### Algorithm

Loop `i` from `k` to `n`, computing `a[i]` using the formula.

### Time Complexity

- **O(n \cdot k)**. For `n=10^18`, this will take forever.

### Space Complexity

- **O(k)** (if we only store last k terms).

## Optimal Approach

### Key Insight

Use **Binary Exponentiation** (Square and Multiply) on the transition matrix.

### Algorithm

1. **Handle Base Case:** If `n < k`, return `a_n`.
2. **Construct Matrix T:**
   - Top row: coefficients `c_0, dots, c_k-1`.
   - Sub-diagonal: `1`s at `T[i][i-1]` for `i > 0`.
3. **Construct Initial Vector V:**
   - `[a_k-1, a_k-2, dots, a_0]^T`.
   - Note the order! `a_k-1` is at the top because it's the "most recent" term needed to compute `a_k`.
4. **Compute Power:** `M = T^n - (k-1)`.
5. **Multiply:** `ResultVector = M x V`.
6. **Result:** The first element of `ResultVector` is `a_n`.

### Time Complexity

- **O(k^3 \log n)**.

### Space Complexity

- **O(k^2)**.

![Algorithm Visualization](../images/MTH-007/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-007/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private long MOD;
    private int K;

    private long[][] multiply(long[][] A, long[][] B) {
        long[][] C = new long[K][K];
        for (int i = 0; i < K; i++) {
            for (int k = 0; k < K; k++) {
                if (A[i][k] == 0) continue;
                for (int j = 0; j < K; j++) {
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
                }
            }
        }
        return C;
    }

    private long[][] power(long[][] A, long exp) {
        long[][] res = new long[K][K];
        for (int i = 0; i < K; i++) res[i][i] = 1;
        
        while (exp > 0) {
            if ((exp & 1) == 1) res = multiply(res, A);
            A = multiply(A, A);
            exp >>= 1;
        }
        return res;
    }

    public long matrix_exp_linear_recurrence(int k, long n, long mod, long[] coeffs, long[] initial) {
        this.MOD = mod;
        this.K = k;
        
        if (n < k) return initial[(int)n];
        
        long[][] T = new long[k][k];
        // Fill first row with coeffs
        for (int j = 0; j < k; j++) {
            T[0][j] = coeffs[j];
        }
        // Fill sub-diagonal with 1s
        for (int i = 1; i < k; i++) {
            T[i][i - 1] = 1;
        }
        
        T = power(T, n - k + 1);
        
        // Result is T * InitialVector
        // InitialVector is [a_{k-1}, a_{k-2}, ..., a_0]^T
        // We only need the first element of the result vector
        long ans = 0;
        for (int j = 0; j < k; j++) {
            // initial[k - 1 - j] corresponds to a_{k-1}, a_{k-2}...
            ans = (ans + T[0][j] * initial[k - 1 - j]) % MOD;
        }
        
        return ans;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int k = sc.nextInt();
        long n = sc.nextLong();
        long MOD = sc.nextLong();
        
        long[] coeffs = new long[k];
        for (int i = 0; i < k; i++) coeffs[i] = sc.nextLong();
        
        long[] initial = new long[k];
        for (int i = 0; i < k; i++) initial[i] = sc.nextLong();
        
        Solution solution = new Solution();
        System.out.println(solution.matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial));
        
        sc.close();
    }
}
```

### Python
```python
import sys

class Solution:
    def matrix_exp_linear_recurrence(self, k: int, n: int, MOD: int, coeffs: list[int], initial: list[int]) -> int:
        if n < k:
            return initial[n]
            
        def multiply(A, B):
            C = [[0] * k for _ in range(k)]
            for i in range(k):
                for l in range(k):
                    if A[i][l] == 0: continue
                    for j in range(k):
                        C[i][j] = (C[i][j] + A[i][l] * B[l][j]) % MOD
            return C

        def power(A, exp):
            res = [[0] * k for _ in range(k)]
            for i in range(k): res[i][i] = 1
            while exp > 0:
                if exp % 2 == 1: res = multiply(res, A)
                A = multiply(A, A)
                exp //= 2
            return res

        T = [[0] * k for _ in range(k)]
        for j in range(k):
            T[0][j] = coeffs[j]
        for i in range(1, k):
            T[i][i - 1] = 1
            
        T_pow = power(T, n - k + 1)
        
        ans = 0
        # Initial vector is [a_{k-1}, a_{k-2}, ..., a_0]
        # We multiply T_pow[0] (first row) with this vector
        for j in range(k):
            ans = (ans + T_pow[0][j] * initial[k - 1 - j]) % MOD
            
        return ans

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        n = int(next(iterator))
        MOD = int(next(iterator))
        
        coeffs = [int(next(iterator)) for _ in range(k)]
        initial = [int(next(iterator)) for _ in range(k)]
        
        sol = Solution()
        print(sol.matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial))
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
    int K;

    vector<vector<long long>> multiply(const vector<vector<long long>>& A, const vector<vector<long long>>& B) {
        vector<vector<long long>> C(K, vector<long long>(K, 0));
        for (int i = 0; i < K; i++) {
            for (int k = 0; k < K; k++) {
                if (A[i][k] == 0) continue;
                for (int j = 0; j < K; j++) {
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
                }
            }
        }
        return C;
    }

    vector<vector<long long>> power(vector<vector<long long>> A, long long exp) {
        vector<vector<long long>> res(K, vector<long long>(K, 0));
        for (int i = 0; i < K; i++) res[i][i] = 1;
        while (exp > 0) {
            if (exp & 1) res = multiply(res, A);
            A = multiply(A, A);
            exp >>= 1;
        }
        return res;
    }

public:
    long long matrix_exp_linear_recurrence(int k, long long n, long long mod, vector<long long>& coeffs, vector<long long>& initial) {
        MOD = mod;
        K = k;

        if (n < k) return initial[n];

        vector<vector<long long>> T(k, vector<long long>(k, 0));
        for (int j = 0; j < k; j++) {
            T[0][j] = coeffs[j];
        }
        for (int i = 1; i < k; i++) {
            T[i][i - 1] = 1;
        }

        T = power(T, n - k + 1);

        long long ans = 0;
        for (int j = 0; j < k; j++) {
            ans = (ans + T[0][j] * initial[k - 1 - j]) % MOD;
        }

        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    long long n, MOD;
    if (!(cin >> k >> n >> MOD)) return 0;

    vector<long long> coeffs(k);
    for (int i = 0; i < k; i++) cin >> coeffs[i];

    vector<long long> initial(k);
    for (int i = 0; i < k; i++) cin >> initial[i];

    Solution solution;
    cout << solution.matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial) << "\n";

    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial) {
    const P = BigInt(MOD);
    const N = BigInt(n);
    
    if (N < BigInt(k)) return Number(initial[Number(N)]);
    
    const K = k;

    function multiply(A, B) {
      const C = Array.from({ length: K }, () => Array(K).fill(0n));
      for (let i = 0; i < K; i++) {
        for (let l = 0; l < K; l++) {
          if (A[i][l] === 0n) continue;
          for (let j = 0; j < K; j++) {
            C[i][j] = (C[i][j] + A[i][l] * B[l][j]) % P;
          }
        }
      }
      return C;
    }

    function power(A, exp) {
      let res = Array.from({ length: K }, () => Array(K).fill(0n));
      for (let i = 0; i < K; i++) res[i][i] = 1n;
      while (exp > 0n) {
        if (exp % 2n === 1n) res = multiply(res, A);
        A = multiply(A, A);
        exp /= 2n;
      }
      return res;
    }

    let T = Array.from({ length: K }, () => Array(K).fill(0n));
    for (let j = 0; j < K; j++) T[0][j] = BigInt(coeffs[j]);
    for (let i = 1; i < K; i++) T[i][i - 1] = 1n;

    T = power(T, N - BigInt(K) + 1n);

    let ans = 0n;
    for (let j = 0; j < K; j++) {
      ans = (ans + T[0][j] * BigInt(initial[K - 1 - j])) % P;
    }

    return Number(ans);
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
  
  const k = parseInt(data[ptr++]);
  const n = BigInt(data[ptr++]); // Keep as BigInt or string
  const MOD = parseInt(data[ptr++]);
  
  const coeffs = [];
  for(let i=0; i<k; i++) coeffs.push(parseInt(data[ptr++]));
  
  const initial = [];
  for(let i=0; i<k; i++) initial.push(parseInt(data[ptr++]));
  
  const solution = new Solution();
  console.log(solution.matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `k=2, n=5, MOD=10^9+7`.
Coeffs: `[1, 1]` (`a_n = a_n-1 + a_n-2`).
Initial: `[0, 1]` (`a_0=0, a_1=1`).

1. **Matrix T:**
   - Row 0: `[1, 1]`
   - Row 1: `[1, 0]`
2. **Initial Vector V:**
   - `[a_1, a_0]^T = [1, 0]^T`.
3. **Exponent:**
   - `n - k + 1 = 5 - 2 + 1 = 4`.
   - Compute `T^4`.
   - `T^1 = [[1, 1], [1, 0]]`
   - `T^2 = [[2, 1], [1, 1]]`
   - `T^4 = [[5, 3], [3, 2]]`
4. **Result Vector:**
   - `T^4 x V = [[5, 3], [3, 2]] x [1, 0]^T = [5 * 1 + 3 * 0, 3 * 1 + 2 * 0]^T = [5, 3]^T`.
5. **Ans:**
   - First element is 5. Correct (`F_5 = 5`).

![Example Visualization](../images/MTH-007/example-1.png)

## ✅ Proof of Correctness

### Invariant
The matrix multiplication `T x V_i` correctly produces `V_i+1`.
- Top row: `c_0 a_i + c_1 a_i-1 + dots = a_i+1`.
- Other rows: `1 * a_i-j = a_i-j`.
By induction, `T^p x V_i = V_i+p`.

### Why the approach is correct
- Matrix multiplication is associative, allowing binary exponentiation.
- Modular arithmetic applies at each step.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Sum of terms `S_n = sum_i=0^n a_i`.
  - *Hint:* Augment the matrix to size `(k+1) x (k+1)` to track the sum.
- **Extension 2:** Non-homogeneous recurrence (`a_n = dots + C`).
  - *Hint:* Add a constant 1 to the state vector and matrix.
- **Extension 3:** Find `k` given sequence (Berlekamp-Massey).
  - *Hint:* Inverse problem.

### Common Mistakes to Avoid

1. **Vector Order**
   - ❌ Wrong: `[a_0, a_1, ...]`.
   - ✅ Correct: `[a_{k-1}, a_{k-2}, ..., a_0]`. The transition matrix expects the most recent terms first.

2. **Exponent Calculation**
   - ❌ Wrong: `T^n`.
   - ✅ Correct: `T^n-k+1` because we start from state `k-1`.

## Related Concepts

- **Cayley-Hamilton Theorem:** Characteristic polynomial of the matrix.
- **Berlekamp-Massey:** Finding the recurrence relation.
