---
problem_id: MTH_INVERSE_POLYNOMIAL__7264
display_id: MTH-003
slug: inverse-polynomial
title: "Inverse Polynomial Mod x^n"
difficulty: Hard
difficulty_score: 72
topics:
  - MathAdvanced
  - Polynomial
  - Newton Iteration
tags:
  - math-advanced
  - polynomial-inverse
  - newton-method
  - hard
premium: true
subscription_tier: basic
---

# MTH-003: Inverse Polynomial Mod x^n

## 📋 Problem Summary

Given a polynomial $P(x)$, find another polynomial $Q(x)$ such that $P(x) \cdot Q(x) \equiv 1 \pmod{x^n}$.
- The coefficients are in a finite field modulo a prime $MOD$.
- $P[0]$ is non-zero (guaranteeing an inverse exists).
- Output the first $n$ coefficients of $Q(x)$.

## 🌍 Real-World Scenario

**Scenario Title:** The Corrupted Data Stream

In advanced communication systems (like satellite links), data is encoded as polynomials to survive noise. This is the basis of **Reed-Solomon Error Correction**.
- To decode a message, we often need to divide polynomials.
- In modular arithmetic, "division" by $P(x)$ is actually "multiplication by the inverse of $P(x)$".
- Finding this inverse efficiently is crucial for decoding gigabytes of data in real-time.

Just like finding $1/7$ in decimal gives an infinite series $0.142857...$, finding $1/P(x)$ gives an infinite polynomial series. We only need the first $n$ terms (modulo $x^n$) to reconstruct the message accurately.

**Why This Problem Matters:**

- **Cryptography:** Polynomial operations are central to post-quantum cryptography schemes (like NTRU).
- **Generating Functions:** In combinatorics, $1/P(x)$ is the generating function for linear recurrences.
- **Computer Algebra Systems:** Tools like Mathematica use this for fast symbolic computation.

![Real-World Application](../images/MTH-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Newton Iteration

We want to solve $F(Q) = \frac{1}{Q} - P = 0$.
Newton's Method finds roots by iterating: $x_{new} = x_{old} - \frac{f(x_{old})}{f'(x_{old})}$.

For polynomials:
1. **Base Case:** $n=1$. $Q(x) \equiv P[0]^{-1} \pmod x$.
2. **Step:** If we know $Q_k(x)$ such that $P \cdot Q_k \equiv 1 \pmod{x^{\lceil n/2 \rceil}}$, we can find $Q_{2k}(x)$ modulo $x^n$.
3. **Formula:** $Q_{new}(x) = Q_{old}(x) \cdot (2 - P(x) \cdot Q_{old}(x)) \pmod{x^n}$.

```
Iteration 0: [1]          (Mod x^1)
      |
      v Double Precision
Iteration 1: [1, -1]      (Mod x^2)
      |
      v Double Precision
Iteration 2: [1, -1, 1, 0] (Mod x^4)
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Modulus:** The problem typically uses $998244353$, which supports NTT.
- **Degree:** If input $P$ has degree $K$, and we need inverse mod $x^N$, we only care about the first $N$ terms of $P$.
- **Output:** Exactly $N$ coefficients.

### Core Concept: Newton-Raphson for Polynomials

The standard Newton iteration for finding root of $f(x)=0$ is $x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$.
We want to find $Q$ such that $Q = 1/P$, or $1/Q - P = 0$.
Let $f(Q) = Q^{-1} - P$.
Then $f'(Q) = -Q^{-2}$.
$Q_{new} = Q - \frac{Q^{-1} - P}{-Q^{-2}} = Q + Q^2(Q^{-1} - P) = Q + Q - P Q^2 = 2Q - P Q^2 = Q(2 - PQ)$.

## Naive Approach

### Intuition

Polynomial long division. Compute $1 / P(x)$ term by term.

### Algorithm

1. $Q[0] = P[0]^{-1}$.
2. For $i$ from 1 to $n-1$:
   - Compute coefficient of $x^i$ in $P \cdot Q$.
   - Adjust $Q[i]$ to make the term zero.

### Time Complexity

- **O(N^2)**.

### Space Complexity

- **O(N)**.

## Optimal Approach

### Key Insight

Use **Divide and Conquer** with **NTT**.
To compute inverse mod $x^n$, first compute inverse mod $x^{\lceil n/2 \rceil}$, then use the Newton formula to double the precision.

### Algorithm

1. **Base Case:** If $n=1$, return $[power(P[0], MOD-2)]$.
2. **Recursive Step:**
   - Recursively compute $Q_{half} = Inverse(P, \lceil n/2 \rceil)$.
   - We want $Q_{full} = Q_{half} (2 - P \cdot Q_{half}) \pmod{x^n}$.
   - Use NTT for multiplication:
     - Pad $Q_{half}$ and $P$ (first $n$ terms) to suitable power of 2.
     - $NTT(Q_{half})$, $NTT(P)$.
     - Pointwise: $Res[i] = Q_{half}[i] \cdot (2 - P[i] \cdot Q_{half}[i])$.
     - Inverse NTT.
   - Truncate to $n$ terms.

### Time Complexity

- $T(n) = T(n/2) + O(n \log n)$.
- By Master Theorem, **O(n \log n)**.

### Space Complexity

- **O(n)**.

![Algorithm Visualization](../images/MTH-003/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-003/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private long MOD;
    private long G = 3;

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
            for (int i = 0; i < n; i++) a[i] = (a[i] * nInv) % MOD;
        }
    }

    public long[] inversePolynomial(long[] P, int n, long MOD) {
        this.MOD = MOD;
        int size = 1;
        while (size < n) size <<= 1;
        
        long[] a = new long[size];
        System.arraycopy(P, 0, a, 0, Math.min(P.length, size));
        
        long[] b = new long[1];
        b[0] = modInverse(a[0]);
        
        int len = 1;
        while (len < n) {
            len <<= 1;
            int limit = len << 1;
            
            long[] copyA = new long[limit];
            long[] copyB = new long[limit];
            
            System.arraycopy(a, 0, copyA, 0, Math.min(a.length, len));
            System.arraycopy(b, 0, copyB, 0, b.length);
            
            ntt(copyA, false);
            ntt(copyB, false);
            
            for (int i = 0; i < limit; i++) {
                // b_new = b * (2 - a * b)
                long term = (copyA[i] * copyB[i]) % MOD;
                copyB[i] = (copyB[i] * (2 - term + MOD)) % MOD;
            }
            
            ntt(copyB, true);
            
            b = new long[len];
            System.arraycopy(copyB, 0, b, 0, len);
        }
        
        long[] res = new long[n];
        System.arraycopy(b, 0, res, 0, n);
        return res;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int k = sc.nextInt();
        int n = sc.nextInt();
        long[] P = new long[k];
        for (int i = 0; i < k; i++) P[i] = sc.nextLong();
        long MOD = sc.nextLong();

        Solution solution = new Solution();
        long[] result = solution.inversePolynomial(P, n, MOD);

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
    def inverse_polynomial(self, P: list[int], n: int, MOD: int) -> list[int]:
        G = 3
        
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

        def ntt(a, invert):
            N = len(a)
            j = 0
            for i in range(1, N):
                bit = N >> 1
                while j & bit:
                    j ^= bit
                    bit >>= 1
                j ^= bit
                if i < j: a[i], a[j] = a[j], a[i]
            
            length = 2
            while length <= N:
                wlen = power(G, (MOD - 1) // length)
                if invert: wlen = modInverse(wlen)
                for i in range(0, N, length):
                    w = 1
                    for j in range(length // 2):
                        u = a[i + j]
                        v = (a[i + j + length // 2] * w) % MOD
                        a[i + j] = (u + v) % MOD
                        a[i + j + length // 2] = (u - v + MOD) % MOD
                        w = (w * wlen) % MOD
                length <<= 1
            
            if invert:
                nInv = modInverse(N)
                for i in range(N): a[i] = (a[i] * nInv) % MOD

        # Iterative Approach
        b = [modInverse(P[0])]
        length = 1
        while length < n:
            length <<= 1
            limit = length << 1
            
            copyA = P[:length] + [0] * (limit - min(len(P), length))
            copyB = b + [0] * (limit - len(b))
            
            ntt(copyA, False)
            ntt(copyB, False)
            
            for i in range(limit):
                term = (copyA[i] * copyB[i]) % MOD
                copyB[i] = (copyB[i] * (2 - term + MOD)) % MOD
            
            ntt(copyB, True)
            b = copyB[:length]
            
        return b[:n]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        n = int(next(iterator))
        P = [int(next(iterator)) for _ in range(k)]
        MOD = int(next(iterator))
        
        sol = Solution()
        res = sol.inverse_polynomial(P, n, MOD)
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

class Solution {
    long long MOD;
    long long G = 3;

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

public:
    vector<long long> inversePolynomial(vector<long long>& P, int n, long long mod) {
        MOD = mod;
        vector<long long> b = {modInverse(P[0])};
        int len = 1;
        while (len < n) {
            len <<= 1;
            int limit = len << 1;
            
            vector<long long> copyA(limit, 0);
            vector<long long> copyB(limit, 0);
            
            for (int i = 0; i < min((int)P.size(), len); i++) copyA[i] = P[i];
            for (int i = 0; i < b.size(); i++) copyB[i] = b[i];
            
            ntt(copyA, false);
            ntt(copyB, false);
            
            for (int i = 0; i < limit; i++) {
                long long term = (copyA[i] * copyB[i]) % MOD;
                copyB[i] = (copyB[i] * (2 - term + MOD)) % MOD;
            }
            
            ntt(copyB, true);
            b.resize(len);
            for (int i = 0; i < len; i++) b[i] = copyB[i];
        }
        b.resize(n);
        return b;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, n;
    if (!(cin >> k >> n)) return 0;
    vector<long long> P(k);
    for (int i = 0; i < k; i++) cin >> P[i];
    long long MOD;
    cin >> MOD;

    Solution solution;
    vector<long long> result = solution.inversePolynomial(P, n, MOD);

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
  inversePolynomial(P, n, MOD) {
    const G = 3n;
    const P_MOD = BigInt(MOD);

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

    function modInverse(x) {
      return power(x, P_MOD - 2n);
    }

    function ntt(a, invert) {
      const N = a.length;
      for (let i = 1, j = 0; i < N; i++) {
        let bit = N >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) [a[i], a[j]] = [a[j], a[i]];
      }
      for (let len = 2; len <= N; len <<= 1) {
        let wlen = power(G, (P_MOD - 1n) / BigInt(len));
        if (invert) wlen = modInverse(wlen);
        for (let i = 0; i < N; i += len) {
          let w = 1n;
          for (let j = 0; j < len / 2; j++) {
            const u = a[i + j];
            const v = (a[i + j + len / 2] * w) % P_MOD;
            a[i + j] = (u + v) % P_MOD;
            a[i + j + len / 2] = (u - v + P_MOD) % P_MOD;
            w = (w * wlen) % P_MOD;
          }
        }
      }
      if (invert) {
        const nInv = modInverse(BigInt(N));
        for (let i = 0; i < N; i++) a[i] = (a[i] * nInv) % P_MOD;
      }
    }

    let b = [modInverse(BigInt(P[0]))];
    let len = 1;
    while (len < n) {
      len <<= 1;
      const limit = len << 1;
      
      const copyA = new Array(limit).fill(0n);
      const copyB = new Array(limit).fill(0n);
      
      for(let i=0; i<Math.min(P.length, len); i++) copyA[i] = BigInt(P[i]);
      for(let i=0; i<b.length; i++) copyB[i] = b[i];
      
      ntt(copyA, false);
      ntt(copyB, false);
      
      for(let i=0; i<limit; i++) {
        const term = (copyA[i] * copyB[i]) % P_MOD;
        copyB[i] = (copyB[i] * (2n - term + P_MOD)) % P_MOD;
      }
      
      ntt(copyB, true);
      b = copyB.slice(0, len);
    }
    
    return b.slice(0, n).map(x => Number(x));
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
  const n = parseInt(data[ptr++]);
  const P = [];
  for(let i=0; i<k; i++) P.push(parseInt(data[ptr++]));
  const MOD = parseInt(data[ptr++]);

  const solution = new Solution();
  const result = solution.inversePolynomial(P, n, MOD);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `P = [1, 1]`, `n = 3`, `MOD = 998244353`
$P(x) = 1 + x$.

1. **Base Case:** $n=1$. $Q_0 = [1^{-1}] = [1]$.
2. **Iteration 1:** Target $n=2$.
   - $Q_{old} = [1]$.
   - $P$ (mod $x^2$) = $[1, 1]$.
   - $Q_{new} = Q(2 - PQ) \pmod{x^2}$.
   - $PQ = 1+x$.
   - $2 - PQ = 1-x$.
   - $Q(2-PQ) = 1(1-x) = 1-x$.
   - $Q_1 = [1, -1] \equiv [1, 998244352]$.
3. **Iteration 2:** Target $n=4$ (covers 3).
   - $Q_{old} = [1, -1]$.
   - $P = [1, 1]$.
   - $PQ = (1+x)(1-x) = 1-x^2$.
   - $2 - PQ = 1+x^2$.
   - $Q(2-PQ) = (1-x)(1+x^2) = 1-x+x^2-x^3$.
   - $Q_2 = [1, -1, 1, -1]$.
4. **Truncate:** First 3 terms: $[1, -1, 1]$.
   - Modulo: `[1, 998244352, 1]`.

![Example Visualization](../images/MTH-003/example-1.png)

## ✅ Proof of Correctness

### Invariant
If $P \cdot Q_k \equiv 1 \pmod{x^{2^k}}$, then $Q_{k+1} = Q_k(2 - P Q_k)$ satisfies $P \cdot Q_{k+1} \equiv 1 \pmod{x^{2^{k+1}}}$.

### Why the approach is correct
- Let $A = P^{-1}$. Then $A - Q_k \equiv 0 \pmod{x^{2^k}}$.
- Squaring both sides: $(A - Q_k)^2 \equiv 0 \pmod{x^{2^{k+1}}}$.
- $A^2 - 2AQ_k + Q_k^2 \equiv 0$.
- Multiply by $P$ (where $PA=1$): $A - 2Q_k + P Q_k^2 \equiv 0$.
- $A \equiv 2Q_k - P Q_k^2 = Q_k(2 - P Q_k)$.
- This confirms the quadratic convergence of Newton iteration.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Polynomial Division.
  - *Hint:* $A(x) / B(x)$ can be computed by reversing coefficients and multiplying by $Inverse(B_{rev})$.
- **Extension 2:** Polynomial Logarithm.
  - *Hint:* $\ln P(x) = \int \frac{P'(x)}{P(x)} dx$. Requires inverse.
- **Extension 3:** Polynomial Exponentiation.
  - *Hint:* $P(x)^k = \exp(k \ln P(x))$.

## Common Mistakes to Avoid

1. **Array Sizing**
   - ❌ Wrong: Using size $n$ for NTT.
   - ✅ Correct: Must use $2n$ (next power of 2) because intermediate product $P \cdot Q$ has degree $2n-2$.

2. **Modular Arithmetic**
   - ❌ Wrong: Negative results in subtraction.
   - ✅ Correct: Add MOD before modulo.

## Related Concepts

- **Newton's Method:** General root finding.
- **Formal Power Series:** The theoretical framework.
- **NTT:** The engine for fast multiplication.
