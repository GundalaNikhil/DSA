---
problem_id: MTH_CONVOLUTION_NTT__5931
display_id: MTH-002
slug: convolution-ntt
title: "Convolution Mod Prime Using NTT"
difficulty: Medium
difficulty_score: 58
topics:
  - MathAdvanced
  - NTT
  - Convolution
tags:
  - math-advanced
  - ntt
  - number-theoretic-transform
  - medium
premium: true
subscription_tier: basic
---

# MTH-002: Convolution Mod Prime Using NTT

## 📋 Problem Summary

You are given two sequences $A$ and $B$. You need to compute their **convolution** $C$ modulo $998244353$.
- $C[k] = \sum_{i=0}^k A[i] \times B[k-i]$
- This is equivalent to multiplying two polynomials $A(x)$ and $B(x)$ and returning the coefficients of the product.

## 🌍 Real-World Scenario

**Scenario Title:** The Image Blurring Filter

Imagine you are writing a photo editing app. You want to apply a "Gaussian Blur" to an image.
- The image is a 2D grid of pixels (intensities).
- The blur effect is defined by a "kernel" (a small matrix of weights).
- Applying the blur means replacing every pixel with a weighted average of its neighbors. This operation is exactly **convolution**.

While images are 2D, the concept is the same for 1D signals (like audio). If the kernel is large, direct convolution is slow ($O(N \cdot K)$). By transforming the signal and kernel into the frequency domain (using FFT/NTT), multiplying them, and transforming back, we can apply massive filters instantly ($O(N \log N)$).

**Why This Problem Matters:**

- **Computer Vision:** Convolutional Neural Networks (CNNs) are built on this operation.
- **Competitive Programming:** Many counting problems (e.g., "number of ways to form sum K") reduce to polynomial multiplication.
- **Cryptography:** Lattice-based cryptography (like Kyber/Dilithium) relies heavily on polynomial multiplication over finite fields.

![Real-World Application](../images/MTH-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: NTT Process

```
Input A: [1, 2]   Input B: [3, 4]
      |                |
      v NTT            v NTT
A_eval: [3, -1]   B_eval: [7, -1]  (Evaluated at roots of unity)
      |                |
      +-------+--------+
              | Pointwise Multiply
              v
      C_eval: [21, 1]
              |
              v Inverse NTT
Output C: [11, 10] (Coefficients: 11 + 10x)
```
*Note: This is a simplified view. Real NTT uses bit-reversal permutation and butterfly operations.*

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Modulus:** $998244353$ is a special prime. It equals $119 \times 2^{23} + 1$. This means $P-1$ is divisible by a large power of 2 ($2^{23}$), allowing us to use NTT for arrays up to size $2^{23} \approx 8 \times 10^6$.
- **Primitive Root:** For this prime, $g=3$ is a primitive root. This plays the role of the complex root of unity in standard FFT.
- **Padding:** The result length is $N+M-1$. You must pad inputs to the next power of 2 that is $\ge N+M-1$.

### Core Concept: Roots of Unity in Finite Fields

In standard FFT, we use $\omega_n = e^{2\pi i / n}$.
In NTT, we use $g^{(P-1)/n} \pmod P$.
- This integer has the property that $\omega^n \equiv 1 \pmod P$ and $\omega^{n/2} \equiv -1 \pmod P$, exactly mimicking the behavior of complex roots of unity.
- This allows us to use the exact same Divide & Conquer algorithm as FFT, but with integer modular arithmetic.

## Naive Approach

### Intuition

Directly compute the sum for each index $k$.

### Algorithm

1. Initialize `C` of size $N+M-1$.
2. Nested loops: `for i in 0..N-1`, `for j in 0..M-1`.
3. `C[i+j] = (C[i+j] + A[i] * B[j]) % MOD`.

### Time Complexity

- **O(N * M)**. Too slow for $N, M = 100,000$.

### Space Complexity

- **O(N + M)**.

## Optimal Approach

### Key Insight

Use **Number Theoretic Transform (NTT)** with the prime $998244353$ and primitive root $3$.

### Algorithm

1. **Setup:**
   - Find smallest power of 2, `limit`, such that `limit >= n + m - 1`.
   - Precompute "bit-reversal" permutation indices for iterative FFT (optional but faster).
2. **NTT Function:**
   - Input: Array `a`, boolean `invert`.
   - Reorder `a` using bit-reversal.
   - Iterate `len` from 2 to `limit`:
     - Calculate `wlen = g^((P-1)/len)`. If `invert`, use modular inverse.
     - For each block of size `len`:
       - `w = 1`.
       - For each pair `(u, v)` in the butterfly:
         - `u = a[i+j]`, `v = a[i+j+len/2] * w`.
         - `a[i+j] = u + v`.
         - `a[i+j+len/2] = u - v`.
         - `w = w * wlen`.
   - If `invert`, multiply all elements by `inv(limit)`.
3. **Convolution:**
   - Pad `A` and `B` with zeros to size `limit`.
   - `NTT(A, false)`.
   - `NTT(B, false)`.
   - Pointwise multiply: `A[i] = A[i] * B[i]`.
   - `NTT(A, true)` (Inverse).
   - Output first `n + m - 1` elements.

### Time Complexity

- **O((N+M) \log (N+M))**.

### Space Complexity

- **O(N + M)**.

![Algorithm Visualization](../images/MTH-002/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-002/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private static final long MOD = 998244353;
    private static final long G = 3;

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

    private void ntt(long[] a, boolean invert) {
        int n = a.length;
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; j & bit; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) {
                long temp = a[i]; a[i] = a[j]; a[j] = temp;
            }
        }

        for (int len = 2; len <= n; len <<= 1) {
            long wlen = power(G, (MOD - 1) / len);
            if (invert) wlen = modInverse(wlen);
            
            for (int i = 0; i < n; i += len) {
                long w = 1;
                for (int j = 0; j < len / 2; j++) {
                    long u = a[i + j];
                    long v = (a[i + j + len / 2] * w) % MOD;
                    a[i + j] = (u + v) % MOD;
                    a[i + j + len / 2] = (u - v + MOD) % MOD;
                    w = (w * wlen) % MOD;
                }
            }
        }

        if (invert) {
            long nInv = modInverse(n);
            for (int i = 0; i < n; i++) {
                a[i] = (a[i] * nInv) % MOD;
            }
        }
    }

    public long[] convolution(long[] A, long[] B, long MOD_UNUSED) {
        int size = 1;
        while (size < A.length + B.length) size <<= 1;

        long[] fa = new long[size];
        long[] fb = new long[size];

        System.arraycopy(A, 0, fa, 0, A.length);
        System.arraycopy(B, 0, fb, 0, B.length);

        ntt(fa, false);
        ntt(fb, false);

        for (int i = 0; i < size; i++) {
            fa[i] = (fa[i] * fb[i]) % MOD;
        }

        ntt(fa, true);

        long[] result = new long[A.length + B.length - 1];
        System.arraycopy(fa, 0, result, 0, result.length);
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // MOD is fixed to 998244353 for this problem
        long MOD = 998244353L;

        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] A = new long[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextLong();

        int m = sc.nextInt();
        long[] B = new long[m];
        for (int i = 0; i < m; i++) B[i] = sc.nextLong();

        Solution solution = new Solution();
        long[] result = solution.convolution(A, B, MOD);

        for (int i = 0; i < result.length; i++) {
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

class Solution:
    def convolution(self, A: list[int], B: list[int], MOD: int) -> list[int]:
        G = 3
        
        def power(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        def modInverse(n):
            return power(n, MOD - 2)

        def ntt(a, invert):
            n = len(a)
            j = 0
            for i in range(1, n):
                bit = n >> 1
                while j & bit:
                    j ^= bit
                    bit >>= 1
                j ^= bit
                if i < j:
                    a[i], a[j] = a[j], a[i]

            length = 2
            while length <= n:
                wlen = power(G, (MOD - 1) // length)
                if invert:
                    wlen = modInverse(wlen)
                
                for i in range(0, n, length):
                    w = 1
                    for j in range(length // 2):
                        u = a[i + j]
                        v = (a[i + j + length // 2] * w) % MOD
                        a[i + j] = (u + v) % MOD
                        a[i + j + length // 2] = (u - v + MOD) % MOD
                        w = (w * wlen) % MOD
                length <<= 1

            if invert:
                nInv = modInverse(n)
                for i in range(n):
                    a[i] = (a[i] * nInv) % MOD

        size = 1
        while size < len(A) + len(B):
            size <<= 1
            
        fa = A + [0] * (size - len(A))
        fb = B + [0] * (size - len(B))
        
        ntt(fa, False)
        ntt(fb, False)
        
        for i in range(size):
            fa[i] = (fa[i] * fb[i]) % MOD
            
        ntt(fa, True)
        
        return fa[:len(A) + len(B) - 1]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        A = [int(next(iterator)) for _ in range(n)]
        m = int(next(iterator))
        B = [int(next(iterator)) for _ in range(m)]
        
        sol = Solution()
        res = sol.convolution(A, B, 998244353)
        print(*(res))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long MOD = 998244353;
const long long G = 3;

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

void ntt(vector<long long>& a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        long long wlen = power(G, (MOD - 1) / len);
        if (invert) wlen = modInverse(wlen);

        for (int i = 0; i < n; i += len) {
            long long w = 1;
            for (int j = 0; j < len / 2; j++) {
                long long u = a[i + j];
                long long v = (a[i + j + len / 2] * w) % MOD;
                a[i + j] = (u + v) % MOD;
                a[i + j + len / 2] = (u - v + MOD) % MOD;
                w = (w * wlen) % MOD;
            }
        }
    }

    if (invert) {
        long long nInv = modInverse(n);
        for (long long& x : a) x = (x * nInv) % MOD;
    }
}

class Solution {
public:
    vector<long long> convolution(vector<long long>& A, vector<long long>& B) {
        int size = 1;
        while (size < A.size() + B.size()) size <<= 1;

        vector<long long> fa(A.begin(), A.end());
        fa.resize(size);
        vector<long long> fb(B.begin(), B.end());
        fb.resize(size);

        ntt(fa, false);
        ntt(fb, false);

        for (int i = 0; i < size; i++) {
            fa[i] = (fa[i] * fb[i]) % MOD;
        }

        ntt(fa, true);

        fa.resize(A.size() + B.size() - 1);
        return fa;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    int m;
    cin >> m;
    vector<long long> B(m);
    for (int i = 0; i < m; i++) cin >> B[i];

    Solution solution;
    vector<long long> result = solution.convolution(A, B);

    for (int i = 0; i < result.size(); i++) {
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
  convolution(A, B, MOD) {
    const G = 3n;
    const P = BigInt(MOD);

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

    function ntt(a, invert) {
      const n = a.length;
      for (let i = 1, j = 0; i < n; i++) {
        let bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) [a[i], a[j]] = [a[j], a[i]];
      }

      for (let len = 2; len <= n; len <<= 1) {
        let wlen = power(G, (P - 1n) / BigInt(len));
        if (invert) wlen = modInverse(wlen);

        for (let i = 0; i < n; i += len) {
          let w = 1n;
          for (let j = 0; j < len / 2; j++) {
            const u = a[i + j];
            const v = (a[i + j + len / 2] * w) % P;
            a[i + j] = (u + v) % P;
            a[i + j + len / 2] = (u - v + P) % P;
            w = (w * wlen) % P;
          }
        }
      }

      if (invert) {
        const nInv = modInverse(BigInt(n));
        for (let i = 0; i < n; i++) {
          a[i] = (a[i] * nInv) % P;
        }
      }
    }

    let size = 1;
    while (size < A.length + B.length) size <<= 1;

    const fa = new Array(size).fill(0n);
    const fb = new Array(size).fill(0n);

    for (let i = 0; i < A.length; i++) fa[i] = BigInt(A[i]);
    for (let i = 0; i < B.length; i++) fb[i] = BigInt(B[i]);

    ntt(fa, false);
    ntt(fb, false);

    for (let i = 0; i < size; i++) {
      fa[i] = (fa[i] * fb[i]) % P;
    }

    ntt(fa, true);

    const result = [];
    for (let i = 0; i < A.length + B.length - 1; i++) {
      result.push(Number(fa[i]));
    }
    return result;
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
  const MOD = 998244353;
  let ptr = 0;

  const n = parseInt(data[ptr++]);
  const A = [];
  for(let i=0; i<n; i++) A.push(parseInt(data[ptr++]));
  
  const m = parseInt(data[ptr++]);
  const B = [];
  for(let i=0; i<m; i++) B.push(parseInt(data[ptr++]));

  const solution = new Solution();
  const result = solution.convolution(A, B, MOD);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `A = [1, 1, 1]`, `B = [1, 2]`
Target Modulo: 998244353.

1. **Padding:** Target size $3+2-1=4$. Next power of 2 is 4.
   - $A = [1, 1, 1, 0]$
   - $B = [1, 2, 0, 0]$
2. **NTT (Forward):**
   - $A_{eval} = [3, \dots]$ (Values in frequency domain)
   - $B_{eval} = [3, \dots]$
3. **Pointwise Multiply:**
   - $C_{eval}[i] = A_{eval}[i] \times B_{eval}[i] \pmod P$
4. **NTT (Inverse):**
   - Transform back.
   - Result: `[1, 3, 3, 2]`
   - Check:
     - $x^0: 1 \cdot 1 = 1$
     - $x^1: 1 \cdot 2 + 1 \cdot 1 = 3$
     - $x^2: 1 \cdot 0 + 1 \cdot 2 + 1 \cdot 1 = 3$
     - $x^3: 1 \cdot 0 + 1 \cdot 0 + 1 \cdot 2 = 2$

![Example Visualization](../images/MTH-002/example-1.png)

## ✅ Proof of Correctness

### Invariant
The NTT transforms a polynomial $A(x)$ into a vector of values $(A(g^0), A(g^1), \dots, A(g^{n-1}))$.
Pointwise multiplication in this domain corresponds to polynomial multiplication in the coefficient domain because $C(x_i) = A(x_i)B(x_i)$ holds for any $x_i$.

### Why the approach is correct
- $998244353$ is a prime of form $c \cdot 2^k + 1$, ensuring existence of $2^k$-th roots of unity.
- The algorithm is isomorphic to FFT but operates in the finite field $\mathbb{Z}_P$, avoiding all precision issues.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Polynomial Inverse.
  - *Hint:* Use Newton's Method with NTT. $B_{k} = B_{k-1}(2 - A B_{k-1}) \pmod {x^{2^k}}$.
- **Extension 2:** Multipoint Evaluation.
  - *Hint:* Build a subproduct tree and use polynomial division.
- **Extension 3:** Circular Convolution.
  - *Hint:* Just standard NTT/FFT without padding to $N+M-1$ (pad to $N$ if $N=M$).

## Common Mistakes to Avoid

1. **Modulo Arithmetic**
   - ❌ Wrong: Forgetting `+ MOD` when subtracting: `(u - v) % MOD` can be negative.
   - ✅ Correct: `(u - v + MOD) % MOD`.

2. **Primitive Root**
   - ❌ Wrong: Using $G=3$ for any prime.
   - ✅ Correct: $G=3$ is specific to $998244353$. For $10^9+7$, no such simple $2^k$-th root exists easily.

## Related Concepts

- **FFT:** The continuous version.
- **Generating Functions:** Used for combinatorial counting.
- **Divide and Conquer:** The underlying algorithmic paradigm.
