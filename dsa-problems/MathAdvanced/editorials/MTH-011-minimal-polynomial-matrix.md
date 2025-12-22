---
problem_id: MTH_MINIMAL_POLYNOMIAL_MATRIX__3891
display_id: MTH-011
slug: minimal-polynomial-matrix
title: "Minimal Polynomial of Matrix (Krylov)"
difficulty: Hard
difficulty_score: 82
topics:
  - MathAdvanced
  - Minimal
tags:
  - math-advanced
  - minimal-polynomial
  - hard
premium: true
subscription_tier: basic
---

# MTH-011: Minimal Polynomial of Matrix (Krylov)

## 📋 Problem Summary

Given an $n \times n$ matrix $A$, find its **minimal polynomial** $\mu_A(x)$.
- $\mu_A(x)$ is the monic polynomial of lowest degree such that $\mu_A(A) = 0$ (the zero matrix).
- It divides the characteristic polynomial $\chi_A(x) = \det(xI - A)$.

## 🌍 Real-World Scenario

**Scenario Title:** The Control System Stabilizer

In control theory, a dynamic system is often modeled by a state-space equation $\dot{x} = Ax + Bu$.
- The stability and controllability of the system depend on the eigenvalues of $A$.
- The **minimal polynomial** tells us the size of the largest Jordan block for each eigenvalue.
- If the minimal polynomial has distinct roots, the matrix is diagonalizable, meaning the system can be decoupled into independent modes.
- Calculating this efficiently allows engineers to design controllers for complex systems (like stabilizing a fighter jet).

**Why This Problem Matters:**

- **Linear Algebra:** Fundamental property of a matrix.
- **Krylov Subspace Methods:** Used in solving massive sparse linear systems (GMRES, Conjugate Gradient).
- **Coding Theory:** Finding the error locator polynomial.

![Real-World Application](../images/MTH-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Krylov Sequence

We pick a random vector $v$ and compute the sequence:
$v, Av, A^2v, A^3v, \dots$

Since the space is $n$-dimensional, these vectors must eventually become linearly dependent.
The relation $\sum c_i A^i v = 0$ gives us a polynomial $P(x) = \sum c_i x^i$ such that $P(A)v = 0$.
With high probability (if $v$ is random), this $P(x)$ is the minimal polynomial.

```
v  = [1, 0]
Av = [1, 1] * [1, 0] = [1, 0]
A^2v = [1, 0]
...
Here v is an eigenvector. Minimal poly for v is x-1.
But true minimal poly for A is (x-1)^2.
We might need multiple random vectors or a better v.
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Random Vector:** A single random vector usually works if the field is large enough.
- **Output:** Coefficients of the polynomial.
- **Degree:** Can be up to $n$.
- **Constraint:** $n \le 200$. $O(n^3)$ is acceptable ($8 \times 10^6$).

### Core Concept: Wiedemann's Algorithm (Simplified)

1. Pick random vector $u$ and $v$.
2. Compute scalar sequence $S_k = u^T A^k v$.
3. Use **Berlekamp-Massey** on $S_k$ to find the minimal recurrence.
4. The characteristic polynomial of this recurrence is likely the minimal polynomial of $A$.

## Naive Approach

### Intuition

Compute characteristic polynomial using interpolation or Faddeev-LeVerrier. Then check factors.

### Algorithm

Hard to implement and slow.

## Optimal Approach

### Key Insight

Combine **Krylov Sequence** generation with **Berlekamp-Massey**.

### Algorithm

1. **Generate Sequence:**
   - Pick random vector $v$ (or random $u, v$).
   - Compute $S_k = u^T (A^k v)$ for $k=0 \dots 2n$.
   - This takes $O(n^3)$ if we compute $A^k$ or $O(n^3)$ if we do matrix-vector mults $2n$ times.
   - Actually:
     - $v_0 = v$.
     - $v_{k+1} = A v_k$. (Matrix-Vector mul: $O(n^2)$).
     - Total for $2n$ terms: $O(n^3)$.
     - Then $S_k = u \cdot v_k$ ($O(n)$).
2. **Find Recurrence:**
   - Run Berlekamp-Massey on $S_0, \dots, S_{2n-1}$.
   - This gives a polynomial $P(x)$.
3. **Verification (Optional):**
   - Ideally, verify $P(A) = 0$. If not, repeat with different random vectors and take LCM of polynomials.
   - For competitive programming with random constraints, one pass is usually sufficient.

### Time Complexity

- **O(n^3)**.

### Space Complexity

- **O(n^2)**.

![Algorithm Visualization](../images/MTH-011/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-011/algorithm-steps.png)

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

    private ArrayList<Long> berlekampMassey(List<Long> s) {
        ArrayList<Long> C = new ArrayList<>();
        ArrayList<Long> B = new ArrayList<>();
        C.add(1L);
        B.add(1L);
        
        int L = 0;
        int b = 1;
        long b_delta = 1;
        
        for (int i = 0; i < s.size(); i++) {
            long delta = s.get(i);
            for (int j = 1; j < C.size(); j++) {
                delta = (delta + C.get(j) * s.get(i - j)) % MOD;
            }
            
            if (delta == 0) {
                b++;
                continue;
            }
            
            ArrayList<Long> T = new ArrayList<>(C);
            long factor = (delta * modInverse(b_delta)) % MOD;
            
            while (C.size() < B.size() + b) C.add(0L);
            for (int j = 0; j < B.size(); j++) {
                long val = (B.get(j) * factor) % MOD;
                int idx = j + b;
                C.set(idx, (C.get(idx) - val + MOD) % MOD);
            }
            
            if (2 * L <= i) {
                L = i + 1 - L;
                B = T;
                b_delta = delta;
                b = 1;
            } else {
                b++;
            }
        }
        return C;
    }

    public long[] minimal_polynomial_matrix(int n, long mod, long[][] matrix) {
        this.MOD = mod;
        
        // Random vectors u and v
        long[] u = new long[n];
        long[] v = new long[n];
        Random rand = new Random(12345); // Fixed seed for reproducibility
        for(int i=0; i<n; i++) {
            u[i] = rand.nextInt((int)MOD);
            v[i] = rand.nextInt((int)MOD);
        }
        
        List<Long> seq = new ArrayList<>();
        long[] currV = Arrays.copyOf(v, n);
        
        for(int k=0; k < 2*n + 2; k++) {
            long val = 0;
            for(int i=0; i<n; i++) val = (val + u[i] * currV[i]) % MOD;
            seq.add(val);
            
            // Multiply A * currV
            long[] nextV = new long[n];
            for(int r=0; r<n; r++) {
                for(int c=0; c<n; c++) {
                    nextV[r] = (nextV[r] + matrix[r][c] * currV[c]) % MOD;
                }
            }
            currV = nextV;
        }
        
        ArrayList<Long> C = berlekampMassey(seq);
        
        // C is [1, -c1, -c2, ...] corresponding to 1 - c1 x - c2 x^2 ...
        // We want monic polynomial x^d - c1 x^{d-1} ...
        // Minimal poly is x^L C(1/x). i.e., reverse C.
        // And normalize leading coeff to 1.
        
        int d = C.size() - 1;
        long[] res = new long[d + 1];
        
        // Reverse C to get P(x)
        // C[0] is constant term of connection poly -> coeff of x^d in minimal poly
        // C[d] is coeff of x^d in connection poly -> constant term in minimal poly
        // Then recurrence is S_n + c1 S_{n-1} + ... = 0
        // Char poly is x^L + c1 x^{L-1} + ... + cL
        
        // So coeff of x^{L-i} is C[i].
        // Coeff of x^L is C[0] = 1.
        // Coeff of x^0 is C[L].
        
        // We need to output coefficients from constant to highest degree.
        // So output C[L], C[L-1], ..., C[0].
        // But we need to ensure C[0] is 1 (it is by BM construction).
        // And we need to negate coefficients?
        // BM finds \sum C_j S_{n-j} = 0.
        // Char poly is \sum C_j x^{L-j}.
        // Yes, directly C is the coefficients in reverse order.
        
        for(int i=0; i<=d; i++) {
            res[i] = C.get(d - i);
        }
        
        // Output format: degree, then coeffs
        long[] output = new long[d + 2];
        output[0] = d;
        System.arraycopy(res, 0, output, 1, d + 1);
        
        return output;
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
        long[] result = solution.minimal_polynomial_matrix(n, MOD, matrix);
        
        System.out.println(result[0]);
        for (int i = 1; i < result.length; i++) {
            System.out.print(result[i] + (i < result.length - 1 ? " " : ""));
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
import sys
import random

class Solution:
    def minimal_polynomial_matrix(self, n: int, MOD: int, matrix: list[list[int]]) -> list[int]:
        
        def power(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1: res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        def modInverse(x):
            return power(x, MOD - 2)

        def berlekamp_massey(s):
            C = [1]
            B = [1]
            L = 0
            b = 1
            b_delta = 1
            
            for i in range(len(s)):
                delta = s[i]
                for j in range(1, len(C)):
                    delta = (delta + C[j] * s[i - j]) % MOD
                
                if delta == 0:
                    b += 1
                    continue
                
                T = C[:]
                factor = (delta * modInverse(b_delta)) % MOD
                
                if len(C) < len(B) + b:
                    C.extend([0] * (len(B) + b - len(C)))
                
                for j in range(len(B)):
                    val = (B[j] * factor) % MOD
                    idx = j + b
                    C[idx] = (C[idx] - val + MOD) % MOD
                
                if 2 * L <= i:
                    L = i + 1 - L
                    B = T
                    b_delta = delta
                    b = 1
                else:
                    b += 1
            return C

        # Random vectors
        random.seed(12345)
        u = [random.randint(0, MOD-1) for _ in range(n)]
        v = [random.randint(0, MOD-1) for _ in range(n)]
        
        seq = []
        currV = list(v)
        
        for _ in range(2 * n + 2):
            val = sum((u[i] * currV[i]) % MOD for i in range(n)) % MOD
            seq.append(val)
            
            nextV = [0] * n
            for r in range(n):
                for c in range(n):
                    nextV[r] = (nextV[r] + matrix[r][c] * currV[c]) % MOD
            currV = nextV
            
        C = berlekamp_massey(seq)
        
        d = len(C) - 1
        # Reverse C to get coefficients from constant to x^d
        res = C[::-1]
        
        return [d] + res

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
        res = sol.minimal_polynomial_matrix(n, MOD, matrix)
        
        print(res[0])
        print(*(res[1:]))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <random>
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

    vector<long long> berlekampMassey(const vector<long long>& s) {
        vector<long long> C = {1};
        vector<long long> B = {1};
        int L = 0;
        int b = 1;
        long long b_delta = 1;

        for (int i = 0; i < s.size(); i++) {
            long long delta = s[i];
            for (int j = 1; j < C.size(); j++) {
                delta = (delta + C[j] * s[i - j]) % MOD;
            }

            if (delta == 0) {
                b++;
                continue;
            }

            vector<long long> T = C;
            long long factor = (delta * modInverse(b_delta)) % MOD;

            if (C.size() < B.size() + b) C.resize(B.size() + b, 0);
            for (int j = 0; j < B.size(); j++) {
                long long val = (B[j] * factor) % MOD;
                int idx = j + b;
                C[idx] = (C[idx] - val + MOD) % MOD;
            }

            if (2 * L <= i) {
                L = i + 1 - L;
                B = T;
                b_delta = delta;
                b = 1;
            } else {
                b++;
            }
        }
        return C;
    }

public:
    vector<long long> minimal_polynomial_matrix(int n, long long mod, vector<vector<long long>>& matrix) {
        MOD = mod;

        vector<long long> u(n), v(n);
        mt19937 rng(12345);
        for (int i = 0; i < n; i++) {
            u[i] = rng() % MOD;
            v[i] = rng() % MOD;
        }

        vector<long long> seq;
        vector<long long> currV = v;

        for (int k = 0; k < 2 * n + 2; k++) {
            long long val = 0;
            for (int i = 0; i < n; i++) val = (val + u[i] * currV[i]) % MOD;
            seq.push_back(val);

            vector<long long> nextV(n, 0);
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    nextV[r] = (nextV[r] + matrix[r][c] * currV[c]) % MOD;
                }
            }
            currV = nextV;
        }

        vector<long long> C = berlekampMassey(seq);
        int d = C.size() - 1;
        vector<long long> res;
        res.push_back(d);
        for (int i = d; i >= 0; i--) {
            res.push_back(C[i]);
        }
        return res;
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
    vector<long long> result = solution.minimal_polynomial_matrix(n, MOD, matrix);

    cout << result[0] << "\n";
    for (int i = 1; i < result.size(); i++) {
        cout << result[i] << (i < result.size() - 1 ? " " : "");
    }
    cout << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minimal_polynomial_matrix(n, MOD, matrix) {
    const P = BigInt(MOD);
    const N = n;
    
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

    function modInverse(x) {
      return power(x, P - 2n);
    }

    function berlekampMassey(s) {
      let C = [1n];
      let B = [1n];
      let L = 0;
      let b = 1;
      let b_delta = 1n;

      for (let i = 0; i < s.length; i++) {
        let delta = s[i];
        for (let j = 1; j < C.length; j++) {
          delta = (delta + C[j] * s[i - j]) % P;
        }

        if (delta === 0n) {
          b++;
          continue;
        }

        const T = [...C];
        const factor = (delta * modInverse(b_delta)) % P;

        while (C.length < B.length + b) C.push(0n);
        for (let j = 0; j < B.length; j++) {
          const val = (B[j] * factor) % P;
          const idx = j + b;
          C[idx] = (C[idx] - val + P) % P;
        }

        if (2 * L <= i) {
          L = i + 1 - L;
          B = T;
          b_delta = delta;
          b = 1;
        } else {
          b++;
        }
      }
      return C;
    }

    // Random vectors u and v
    const u = new Array(N).fill(0n).map(() => BigInt(Math.floor(Math.random() * MOD)));
    const v = new Array(N).fill(0n).map(() => BigInt(Math.floor(Math.random() * MOD)));
    
    const seq = [];
    let currV = [...v];
    
    for(let k=0; k < 2*N + 2; k++) {
        let val = 0n;
        for(let i=0; i<N; i++) val = (val + u[i] * currV[i]) % P;
        seq.push(val);
        
        const nextV = new Array(N).fill(0n);
        for(let r=0; r<N; r++) {
            for(let c=0; c<N; c++) {
                nextV[r] = (nextV[r] + mat[r][c] * currV[c]) % P;
            }
        }
        currV = nextV;
    }
    
    const C = berlekampMassey(seq);
    const d = C.length - 1;
    const res = [];
    res.push(d);
    for(let i=d; i>=0; i--) res.push(Number(C[i]));
    
    return res;
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
  const result = solution.minimal_polynomial_matrix(n, MOD, matrix);
  
  console.log(result[0]);
  console.log(result.slice(1).join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `2x2` Jordan Block `[[1, 1], [0, 1]]`.
1. **Krylov Sequence:**
   - $v = [1, 0]^T$.
   - $Av = [1, 0]^T$.
   - $A^2v = [1, 0]^T$.
   - Sequence is constant. BM gives $x-1$.
   - This is minimal poly for $v$, but not for $A$.
   - $v = [0, 1]^T$.
   - $Av = [1, 1]^T$.
   - $A^2v = [2, 1]^T$.
   - $A^3v = [3, 1]^T$.
   - Sequence: $0, 1, 2, 3 \dots$
   - BM finds recurrence $S_n = 2S_{n-1} - S_{n-2}$.
   - Char poly: $x^2 - 2x + 1 = (x-1)^2$.
2. **Random Vectors:**
   - With random $u, v$, we likely capture the largest block structure.
   - Result: $x^2 - 2x + 1$.
   - Coeffs: `1, -2, 1` (from constant to $x^2$).
   - Output: `1 1000000005 1`.

![Example Visualization](../images/MTH-011/example-1.png)

## ✅ Proof of Correctness

### Invariant
The sequence $u^T A^k v$ is linearly recurrent with characteristic polynomial equal to the minimal polynomial of $A$ (with high probability).

### Why the approach is correct
- The minimal polynomial of the sequence divides the minimal polynomial of $A$.
- For random $u, v$, the probability that they fall into a proper subspace is low (inverse of field size).

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Characteristic Polynomial.
  - *Hint:* Same degree as $n$. Minimal poly divides it.
- **Extension 2:** Eigenvalues.
  - *Hint:* Roots of minimal polynomial.
- **Extension 3:** Sparse Matrix.
  - *Hint:* This algorithm works in $O(E \cdot n)$ for sparse matrices!

### Common Mistakes to Avoid

1. **Sequence Length**
   - ❌ Wrong: $n$ terms.
   - ✅ Correct: $2n$ terms are needed to recover degree $n$ polynomial.

2. **Coefficient Order**
   - ❌ Wrong: Highest degree first.
   - ✅ Correct: Problem asks for constant to highest (or check example carefully). Example: `1 -2 1` for $x^2-2x+1$. $1$ is constant term? No, example says `1 1000000005 1`. $1$ is $x^2$, $-2$ is $x$, $1$ is constant.
   - $x^2 - 2x + 1$.
   - If order is constant to highest: `1, -2, 1`.
   - If order is highest to constant: `1, -2, 1`. Symmetric.
   - Let's check another example. $x-2$. Coeffs: $-2, 1$ (const, high) or $1, -2$ (high, const).
   - Problem statement says: "coefficients from constant to highest degree".
   - So for $x^2 - 2x + 1$, it is `1, -2, 1`.
   - My code reverses C (which is $1, -c1, -c2$) to get $1, -c1, -c2$.
   - $C$ corresponds to $1 - c_1 x - c_2 x^2$.
   - Minimal poly is $x^d - c_1 x^{d-1} - c_2 x^{d-2}$.
   - So coeffs are $C[d], C[d-1], \dots, C[0]$.
   - My code does `res[i] = C.get(d-i)`.
   - `res[0] = C[d]`. `res[d] = C[0] = 1`.
   - This matches "constant to highest".

## Related Concepts

- **Wiedemann Algorithm:** The sparse version.
- **Block Wiedemann:** Parallel version.
