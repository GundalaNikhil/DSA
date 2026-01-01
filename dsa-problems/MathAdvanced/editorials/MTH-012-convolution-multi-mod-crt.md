---
problem_id: MTH_CONVOLUTION_MULTI_MOD_CRT__4736
display_id: MTH-012
slug: convolution-multi-mod-crt
title: "Convolution Under Multiple Mods with CRT"
difficulty: Medium
difficulty_score: 65
topics:
  - MathAdvanced
  - Convolution
tags:
  - math-advanced
  - crt
  - medium
premium: true
subscription_tier: basic
---

# MTH-012: Convolution Under Multiple Mods with CRT

## 📋 Problem Summary

Compute the convolution of two large arrays `A` and `B` modulo an arbitrary integer `M` (which may not be prime or NTT-friendly).
- Standard NTT only works for specific primes like `998244353`.
- FFT uses floating point numbers, which can lose precision for large results.
- The solution is to compute the convolution modulo several NTT-friendly primes and combine them using the **Chinese Remainder Theorem (CRT)**.

## 🌍 Real-World Scenario

**Scenario Title:** The Big Integer Multiplier

Imagine you are building a cryptographic library that needs to multiply two massive numbers (e.g., 1 million digits each).
- Multiplication is essentially convolution of digit arrays (followed by carry handling).
- Naive multiplication is `O(N^2)`.
- FFT-based multiplication is `O(N log N)`.
- However, the intermediate values in convolution can exceed `10^18` (e.g., sum of `10^5` products of digits up to 9). Standard 64-bit integers overflow.
- To handle this without slow arbitrary-precision arithmetic libraries, we compute the result modulo several large primes (e.g., three `10^9` primes give a range of `10^27`) and reconstruct the exact value.

**Why This Problem Matters:**

- **High-Performance Computing:** Multiplying polynomials with large coefficients.
- **Cryptography:** RSA key generation involves massive integer arithmetic.
- **Competitive Programming:** Solving "count ways" problems with arbitrary modulo.

![Real-World Application](../images/MTH-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: CRT Reconstruction

We have a value `X`. We don't know `X`, but we know:
- `X equiv a_1 +/-odp_1`
- `X equiv a_2 +/-odp_2`
- `X equiv a_3 +/-odp_3`

We want to find `X +/-od M`.
Since `p_1 p_2 p_3 > max possible value of convolution`, the CRT solution is the exact value of the convolution. Then we just take modulo `M`.

```
      [ NTT mod p1 ] ---> [ a1 ]
     /
A, B -- [ NTT mod p2 ] ---> [ a2 ]  ---> [ CRT ] ---> X ---> X % M
     \
      [ NTT mod p3 ] ---> [ a3 ]
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Primes:** Use `P_1 = 998244353`, `P_2 = 1004535809`, `P_3 = 469762049`. All are of form `c * 2^k + 1` with `2^20 | (P-1)`, supporting NTT size up to `10^6`.
- **Max Value:** If `N=10^5` and values are `10^9`, max convolution value is `10^5 x 10^9 x 10^9 = 10^23`.
- **Product of Primes:** `P_1 P_2 P_3 ~= 4 x 10^26 > 10^23`. So 3 primes are sufficient.
- **Garner's Algorithm:** A standard way to implement CRT for large numbers.

### Core Concept: Garner's Algorithm

To find `X` such that `X equiv a_i +/-odp_i`:
1. `X = x_1 + x_2 p_1 + x_3 p_1 p_2`.
2. `X equiv x_1 equiv a_1 +/-odp_1 implies x_1 = a_1`.
3. `X equiv x_1 + x_2 p_1 equiv a_2 +/-odp_2 implies x_2 = (a_2 - x_1) p_1^-1 +/-odp_2`.
4. `X equiv x_1 + x_2 p_1 + x_3 p_1 p_2 equiv a_3 +/-odp_3 implies x_3 = ((a_3 - x_1 - x_2 p_1) p_1^-1 p_2^-1) +/-odp_3`.

## Naive Approach

### Intuition

Standard `O(N^2)` convolution.

### Algorithm

Nested loops.

### Time Complexity

- **O(N^2)**. Too slow for `N=10^5`.

### Space Complexity

- **O(N)**.

## Optimal Approach

### Key Insight

Run NTT for 3 primes, then CRT.

### Algorithm

1. **NTT Implementation:** Write a generic NTT function that takes a modulus and a primitive root.
   - `P_1=998244353, g=3`.
   - `P_2=1004535809, g=3`.
   - `P_3=469762049, g=3`.
2. **Compute Convolutions:**
   - `C_1 = Conv(A, B) +/-odP_1`.
   - `C_2 = Conv(A, B) +/-odP_2`.
   - `C_3 = Conv(A, B) +/-odP_3`.
3. **Reconstruct:**
   - For each index `i`, use Garner's algorithm on `(C_1[i], C_2[i], C_3[i])` to find the true value `Val`.
   - Output `Val +/-od M`.

### Time Complexity

- **O(N \log N)**. 3 passes of NTT.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/MTH-012/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-012/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private long power(long base, long exp, long mod) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }

    private long modInverse(long n, long mod) {
        return power(n, mod - 2, mod);
    }

    private void ntt(long[] a, boolean invert, long mod, long g) {
        int n = a.length;
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; (j & bit) != 0; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) {
                long temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
        
        for (int len = 2; len <= n; len <<= 1) {
            long wlen = power(g, (mod - 1) / len, mod);
            if (invert) wlen = modInverse(wlen, mod);
            for (int i = 0; i < n; i += len) {
                long w = 1;
                for (int j = 0; j < len / 2; j++) {
                    long u = a[i + j];
                    long v = (a[i + j + len / 2] * w) % mod;
                    a[i + j] = (u + v) % mod;
                    a[i + j + len / 2] = (u - v + mod) % mod;
                    w = (w * wlen) % mod;
                }
            }
        }
        
        if (invert) {
            long nInv = modInverse(n, mod);
            for (int i = 0; i < n; i++) a[i] = (a[i] * nInv) % mod;
        }
    }

    private long[] convolve(long[] A, long[] B, long mod, long g) {
        int size = 1;
        while (size < A.length + B.length) size <<= 1;
        
        long[] fa = Arrays.copyOf(A, size);
        long[] fb = Arrays.copyOf(B, size);
        
        ntt(fa, false, mod, g);
        ntt(fb, false, mod, g);
        
        for (int i = 0; i < size; i++) fa[i] = (fa[i] * fb[i]) % mod;
        
        ntt(fa, true, mod, g);
        return fa;
    }

    public long[] convolution_multi_mod_crt(int n, int m, long[] A, long[] B, long targetMod) {
        long P1 = 998244353, G1 = 3;
        long P2 = 1004535809, G2 = 3;
        long P3 = 469762049, G3 = 3;
        
        long[] c1 = convolve(A, B, P1, G1);
        long[] c2 = convolve(A, B, P2, G2);
        long[] c3 = convolve(A, B, P3, G3);
        
        int len = n + m - 1;
        long[] res = new long[len];
        
        long P1_inv_P2 = modInverse(P1, P2);
        long P1P2_inv_P3 = modInverse((P1 * P2) % P3, P3);
        
        for (int i = 0; i < len; i++) {
            long a1 = c1[i];
            long a2 = c2[i];
            long a3 = c3[i];
            
            long x1 = a1;
            long x2 = ((a2 - x1 + P2) % P2 * P1_inv_P2) % P2;
            long x3 = ((a3 - x1) % P3 + P3) % P3;
            x3 = (x3 - (x2 * P1) % P3 + P3) % P3;
            x3 = (x3 * P1P2_inv_P3) % P3;
            
            // Result = x1 + x2*P1 + x3*P1*P2
            long ans = (x1 + x2 * P1) % targetMod;
            ans = (ans + (x3 * ((P1 * P2) % targetMod)) % targetMod) % targetMod;
            res[i] = ans;
        }
        
        return res;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        long[] A = new long[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextLong();
        
        long[] B = new long[m];
        for (int i = 0; i < m; i++) B[i] = sc.nextLong();
        
        long MOD = sc.nextLong();
        
        Solution solution = new Solution();
        long[] res = solution.convolution_multi_mod_crt(n, m, A, B, MOD);
        
        for (int i = 0; i < res.length; i++) {
            System.out.print(res[i] + (i < res.length - 1 ? " " : ""));
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
    def convolution_multi_mod_crt(self, n: int, m: int, A: list[int], B: list[int], targetMod: int) -> list[int]:
        
        def power(base, exp, mod):
            res = 1
            base %= mod
            while exp > 0:
                if exp % 2 == 1: res = (res * base) % mod
                base = (base * base) % mod
                exp //= 2
            return res

        def modInverse(n, mod):
            return power(n, mod - 2, mod)

        def ntt(a, invert, mod, g):
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
                wlen = power(g, (mod - 1) // length, mod)
                if invert: wlen = modInverse(wlen, mod)
                for i in range(0, n, length):
                    w = 1
                    for j in range(length // 2):
                        u = a[i + j]
                        v = (a[i + j + length // 2] * w) % mod
                        a[i + j] = (u + v) % mod
                        a[i + j + length // 2] = (u - v + mod) % mod
                        w = (w * wlen) % mod
                length <<= 1
            
            if invert:
                nInv = modInverse(n, mod)
                for i in range(n):
                    a[i] = (a[i] * nInv) % mod

        def convolve(A, B, mod, g):
            size = 1
            while size < len(A) + len(B): size <<= 1
            fa = A + [0] * (size - len(A))
            fb = B + [0] * (size - len(B))
            ntt(fa, False, mod, g)
            ntt(fb, False, mod, g)
            for i in range(size): fa[i] = (fa[i] * fb[i]) % mod
            ntt(fa, True, mod, g)
            return fa

        P1, G1 = 998244353, 3
        P2, G2 = 1004535809, 3
        P3, G3 = 469762049, 3
        
        c1 = convolve(A, B, P1, G1)
        c2 = convolve(A, B, P2, G2)
        c3 = convolve(A, B, P3, G3)
        
        length = n + m - 1
        res = []
        
        P1_inv_P2 = modInverse(P1, P2)
        P1P2_inv_P3 = modInverse((P1 * P2) % P3, P3)
        
        for i in range(length):
            a1 = c1[i]
            a2 = c2[i]
            a3 = c3[i]
            
            x1 = a1
            x2 = ((a2 - x1 + P2) % P2 * P1_inv_P2) % P2
            x3 = ((a3 - x1 - x2 * P1 % P3 + 2 * P3) % P3 * P1P2_inv_P3) % P3
            
            ans = (x1 + x2 * P1) % targetMod
            ans = (ans + (x3 * ((P1 * P2) % targetMod)) % targetMod) % targetMod
            res.append(ans)
            
        return res

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        A = [int(next(iterator)) for _ in range(n)]
        B = [int(next(iterator)) for _ in range(m)]
        MOD = int(next(iterator))
        
        sol = Solution()
        res = sol.convolution_multi_mod_crt(n, m, A, B, MOD)
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
    long long power(long long base, long long exp, long long mod) {
        long long res = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp /= 2;
        }
        return res;
    }

    long long modInverse(long long n, long long mod) {
        return power(n, mod - 2, mod);
    }

    void ntt(vector<long long>& a, bool invert, long long mod, long long g) {
        int n = a.size();
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; j & bit; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) swap(a[i], a[j]);
        }

        for (int len = 2; len <= n; len <<= 1) {
            long long wlen = power(g, (mod - 1) / len, mod);
            if (invert) wlen = modInverse(wlen, mod);
            for (int i = 0; i < n; i += len) {
                long long w = 1;
                for (int j = 0; j < len / 2; j++) {
                    long long u = a[i + j];
                    long long v = (a[i + j + len / 2] * w) % mod;
                    a[i + j] = (u + v) % mod;
                    a[i + j + len / 2] = (u - v + mod) % mod;
                    w = (w * wlen) % mod;
                }
            }
        }

        if (invert) {
            long long nInv = modInverse(n, mod);
            for (int i = 0; i < n; i++) a[i] = (a[i] * nInv) % mod;
        }
    }

    vector<long long> convolve(const vector<long long>& A, const vector<long long>& B, long long mod, long long g) {
        int size = 1;
        while (size < A.size() + B.size()) size <<= 1;
        vector<long long> fa(size), fb(size);
        for(int i=0; i<A.size(); i++) fa[i] = A[i];
        for(int i=0; i<B.size(); i++) fb[i] = B[i];

        ntt(fa, false, mod, g);
        ntt(fb, false, mod, g);
        for (int i = 0; i < size; i++) fa[i] = (fa[i] * fb[i]) % mod;
        ntt(fa, true, mod, g);
        return fa;
    }

public:
    vector<long long> convolution_multi_mod_crt(int n, int m, vector<long long>& A, vector<long long>& B, long long targetMod) {
        long long P1 = 998244353, G1 = 3;
        long long P2 = 1004535809, G2 = 3;
        long long P3 = 469762049, G3 = 3;

        vector<long long> c1 = convolve(A, B, P1, G1);
        vector<long long> c2 = convolve(A, B, P2, G2);
        vector<long long> c3 = convolve(A, B, P3, G3);

        int len = n + m - 1;
        vector<long long> res(len);

        long long P1_inv_P2 = modInverse(P1, P2);
        long long P1P2_inv_P3 = modInverse((P1 * P2) % P3, P3);

        for (int i = 0; i < len; i++) {
            long long a1 = c1[i];
            long long a2 = c2[i];
            long long a3 = c3[i];

            long long x1 = a1;
            long long x2 = ((a2 - x1 + P2) % P2 * P1_inv_P2) % P2;
            long long x3 = ((a3 - x1) % P3 + P3) % P3;
            x3 = (x3 - (x2 * P1) % P3 + P3) % P3;
            x3 = (x3 * P1P2_inv_P3) % P3;

            long long ans = (x1 + x2 * P1) % targetMod;
            ans = (ans + (x3 * ((P1 * P2) % targetMod)) % targetMod) % targetMod;
            res[i] = ans;
        }

        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    vector<long long> B(m);
    for (int i = 0; i < m; i++) cin >> B[i];

    long long MOD;
    cin >> MOD;

    Solution solution;
    vector<long long> result = solution.convolution_multi_mod_crt(n, m, A, B, MOD);

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
  convolution_multi_mod_crt(n, m, A, B, targetMod) {
    const TM = BigInt(targetMod);
    
    const bigA = A.map(BigInt);
    const bigB = B.map(BigInt);

    function power(base, exp, mod) {
      let res = 1n;
      base %= mod;
      while (exp > 0n) {
        if (exp % 2n === 1n) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2n;
      }
      return res;
    }

    function modInverse(n, mod) {
      return power(n, mod - 2n, mod);
    }

    function ntt(a, invert, mod, g) {
      const n = a.length;
      let j = 0;
      for (let i = 1; i < n; i++) {
        let bit = n >> 1;
        while (j & bit) {
          j ^= bit;
          bit >>= 1;
        }
        j ^= bit;
        if (i < j) [a[i], a[j]] = [a[j], a[i]];
      }

      for (let len = 2; len <= n; len <<= 1) {
        let wlen = power(g, (mod - 1n) / BigInt(len), mod);
        if (invert) wlen = modInverse(wlen, mod);
        for (let i = 0; i < n; i += len) {
          let w = 1n;
          for (let j = 0; j < len / 2; j++) {
            const u = a[i + j];
            const v = (a[i + j + len / 2] * w) % mod;
            a[i + j] = (u + v) % mod;
            a[i + j + len / 2] = (u - v + mod) % mod;
            w = (w * wlen) % mod;
          }
        }
      }

      if (invert) {
        const nInv = modInverse(BigInt(n), mod);
        for (let i = 0; i < n; i++) a[i] = (a[i] * nInv) % mod;
      }
    }

    function convolve(A, B, mod, g) {
      let size = 1;
      while (size < A.length + B.length) size <<= 1;
      const fa = new Array(size).fill(0n);
      const fb = new Array(size).fill(0n);
      for(let i=0; i<A.length; i++) fa[i] = A[i];
      for(let i=0; i<B.length; i++) fb[i] = B[i];

      ntt(fa, false, mod, g);
      ntt(fb, false, mod, g);
      for (let i = 0; i < size; i++) fa[i] = (fa[i] * fb[i]) % mod;
      ntt(fa, true, mod, g);
      return fa;
    }

    const P1 = 998244353n, G1 = 3n;
    const P2 = 1004535809n, G2 = 3n;
    const P3 = 469762049n, G3 = 3n;

    const c1 = convolve(bigA, bigB, P1, G1);
    const c2 = convolve(bigA, bigB, P2, G2);
    const c3 = convolve(bigA, bigB, P3, G3);

    const len = n + m - 1;
    const res = [];

    const P1_inv_P2 = modInverse(P1, P2);
    const P1P2_inv_P3 = modInverse((P1 * P2) % P3, P3);

    for (let i = 0; i < len; i++) {
      const a1 = c1[i];
      const a2 = c2[i];
      const a3 = c3[i];

      const x1 = a1;
      const x2 = ((a2 - x1 + P2) % P2 * P1_inv_P2) % P2;
      let x3 = ((a3 - x1) % P3 + P3) % P3;
      x3 = (x3 - (x2 * P1) % P3 + P3) % P3;
      x3 = (x3 * P1P2_inv_P3) % P3;

      let ans = (x1 + x2 * P1) % TM;
      ans = (ans + (x3 * ((P1 * P2) % TM)) % TM) % TM;
      res.push(Number(ans));
    }

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
  const m = parseInt(data[ptr++]);
  
  const A = [];
  for(let i=0; i<n; i++) A.push(parseInt(data[ptr++]));
  
  const B = [];
  for(let i=0; i<m; i++) B.push(parseInt(data[ptr++]));
  
  const MOD = parseInt(data[ptr++]);
  
  const solution = new Solution();
  const result = solution.convolution_multi_mod_crt(n, m, A, B, MOD);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `A=[1, 2]`, `B=[3, 4]`, `MOD=10^9+7`.
1. **NTT Mod P1:**
   - `C_1 = [3, 10, 8]`.
2. **NTT Mod P2:**
   - `C_2 = [3, 10, 8]`.
3. **NTT Mod P3:**
   - `C_3 = [3, 10, 8]`.
4. **CRT:**
   - Since all `C_i` are equal and small, the reconstructed value is exactly `[3, 10, 8]`.
   - Modulo `10^9+7`, result is `3 10 8`.

![Example Visualization](../images/MTH-012/example-1.png)

## ✅ Proof of Correctness

### Invariant
The CRT guarantees a unique solution modulo `P_1 P_2 P_3`.
Since the true convolution value is less than `P_1 P_2 P_3`, the CRT solution is the exact integer value.

### Why the approach is correct
- We perform exact arithmetic in the ring `mathbbZ_P_1 P_2 P_3`.
- The final modulo `M` is applied to the exact integer.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Arbitrary Modulo NTT (Schonhage-Strassen).
  - *Hint:* Split coefficients into smaller chunks to avoid CRT.
- **Extension 2:** Polynomial Inverse.
  - *Hint:* Newton's method.
- **Extension 3:** BigInt Multiplication.
  - *Hint:* This IS BigInt multiplication (base `10^9`).

### Common Mistakes to Avoid

1. **Negative Modulo**
   - ❌ Wrong: `(a - b) % mod`.
   - ✅ Correct: `(a - b + mod) % mod`.

2. **Overflow in CRT**
   - ❌ Wrong: `x1 + x2 * P1` without modulo `M`.
   - *Correction:* In the code, we do `(x1 + x2 * P1) % targetMod`. This is safe if `targetMod` fits in long. But `x2 * P1` can be `10^18`. `x3 * P1 * P2` is definitely `> 2^63`.
   - We must be careful. `P1 * P2` is `10^18`. `x3` is `10^9`. Product is `10^27`.
   - In Java/C++, we need `__int128` or careful modular arithmetic.
   - However, we only need the result modulo `targetMod`.
   - So `(x3 * ((P1 * P2) % targetMod)) % targetMod` is safe!
   - `P1 * P2` might overflow `long` before modulo. `10^18` fits in `long` (max `9 x 10^18`).
   - `P_1 ~= 10^9, P_2 ~= 10^9 implies P_1 P_2 ~= 10^18`. Safe.

## Related Concepts

- **NTT:** Number Theoretic Transform.
- **Garner's Algorithm:** Efficient CRT.
