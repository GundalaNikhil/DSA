---
problem_id: MTH_FWHT_XOR_CONVOLUTION__7451
display_id: MTH-008
slug: fwht-xor-convolution
title: "Fast Walsh-Hadamard Transform (XOR Convolution)"
difficulty: Medium
difficulty_score: 62
topics:
  - MathAdvanced
  - Fast
tags:
  - math-advanced
  - fwht
  - medium
premium: true
subscription_tier: basic
---

# MTH-008: Fast Walsh-Hadamard Transform (XOR Convolution)

## 📋 Problem Summary

Given two arrays `A` and `B` of size `2^k`, compute their **XOR convolution** `C`.
- `C[k] = sum_i oplus j = k A[i] x B[j]`.
- Output the result modulo `10^9+7`.

## 🌍 Real-World Scenario

**Scenario Title:** The Quantum Logic Gate Simulation

In quantum computing, the **Hadamard Gate** is a fundamental operation that creates superposition.
- A quantum state of `k` qubits is a vector of size `2^k`.
- Applying Hadamard gates to all qubits corresponds to performing a Walsh-Hadamard Transform on the state vector.
- XOR convolution appears when analyzing the interference patterns of quantum states or in coding theory (Walsh codes used in CDMA cellular networks).

Just like FFT speeds up standard multiplication, FWHT speeds up "XOR multiplication" from `O(N^2)` to `O(N log N)`.

**Why This Problem Matters:**

- **Signal Processing:** Analyzing boolean functions (spectral analysis).
- **Coding Theory:** Reed-Muller codes.
- **Competitive Programming:** Problems involving "number of pairs with XOR sum K".

![Real-World Application](../images/MTH-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: FWHT Butterfly

The structure is very similar to FFT, but the "twiddle factors" are just `+1` and `-1`.

For a block of size `2L`:
- Let `u` be an element from the first half (indices having bit 0).
- Let `v` be the corresponding element from the second half (indices having bit 1).
- **Forward Transform:**
  - `u_new = u + v`
  - `v_new = u - v`
- **Inverse Transform:**
  - Same operations, but divide by 2 at the end.

```
      u --------+--------> u + v
                 \     /
                  \   /
                   \ /
                    X
                   / \
                  /   \
                 /     \
      v --------+--------> u - v
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input Size:** `N = 2^k`.
- **Modulo:** `10^9+7`. Note that in the inverse transform, we divide by `N`. Division means multiplication by modular inverse.
- **Negative Numbers:** `u-v` can be negative. Always add `MOD` before taking modulo.

### Core Concept: The Transform Property

Just like `mathcalF(A * B) = mathcalF(A) * mathcalF(B)` for FFT:
`FWHT(A oplus B) = FWHT(A) * FWHT(B)` (pointwise multiplication).

**Algorithm:**
1. Transform `A -> hatA`.
2. Transform `B -> hatB`.
3. `hatC[i] = hatA[i] x hatB[i]`.
4. Inverse Transform `hatC -> C`.

## Naive Approach

### Intuition

Double loop over all pairs.

### Algorithm

1. Initialize `C` with zeros.
2. Loop `i` from `0` to `N-1`.
3. Loop `j` from `0` to `N-1`.
4. `C[i oplus j] += A[i] x B[j]`.

### Time Complexity

- **O(N^2)**. With `k=17`, `N ~= 1.3 x 10^5`, `N^2 ~= 1.7 x 10^10`. Too slow.

### Space Complexity

- **O(N)**.

## Optimal Approach

### Key Insight

Use Fast Walsh-Hadamard Transform (FWHT).

### Algorithm

1. **FWHT Function:**
   - Iterate length `len` from 1 to `N/2` (doubling each time).
   - Iterate `i` from 0 to `N-1` with step `2*len`.
   - Iterate `j` from 0 to `len-1`.
     - `u = A[i+j]`, `v = A[i+j+len]`.
     - `A[i+j] = u + v`.
     - `A[i+j+len] = u - v`.
2. **Convolution:**
   - `FWHT(A, false)`.
   - `FWHT(B, false)`.
   - `For i in 0..N-1: A[i] = A[i] * B[i]`.
   - `FWHT(A, true)` (Inverse).
     - Inverse is same as forward, but divide each element by `N` at the end.

### Time Complexity

- **O(N \log N)**. `17 x 2^17 ~= 2.2 x 10^6` operations.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/MTH-008/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-008/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private long MOD = 1000000007;

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

    private void fwht(long[] a, boolean invert) {
        int n = a.length;
        for (int len = 1; len < n; len <<= 1) {
            for (int i = 0; i < n; i += 2 * len) {
                for (int j = 0; j < len; j++) {
                    long u = a[i + j];
                    long v = a[i + j + len];
                    a[i + j] = (u + v) % MOD;
                    a[i + j + len] = (u - v + MOD) % MOD;
                }
            }
        }
        
        if (invert) {
            long invN = modInverse(n);
            for (int i = 0; i < n; i++) {
                a[i] = (a[i] * invN) % MOD;
            }
        }
    }

    public long[] fwht_xor_convolution(int k, long[] A, long[] B) {
        int n = 1 << k;
        
        fwht(A, false);
        fwht(B, false);
        
        long[] C = new long[n];
        for (int i = 0; i < n; i++) {
            C[i] = (A[i] * B[i]) % MOD;
        }
        
        fwht(C, true);
        return C;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int k = sc.nextInt();
        int n = 1 << k;
        
        long[] A = new long[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextLong();
        
        long[] B = new long[n];
        for (int i = 0; i < n; i++) B[i] = sc.nextLong();
        
        Solution solution = new Solution();
        long[] res = solution.fwht_xor_convolution(k, A, B);
        
        for (int i = 0; i < n; i++) {
            System.out.print(res[i] + (i < n - 1 ? " " : ""));
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
    def fwht_xor_convolution(self, k: int, A: list[int], B: list[int]) -> list[int]:
        MOD = 1000000007
        n = 1 << k
        
        def fwht(a, invert):
            length = 1
            while length < n:
                for i in range(0, n, 2 * length):
                    for j in range(length):
                        u = a[i + j]
                        v = a[i + j + length]
                        a[i + j] = (u + v) % MOD
                        a[i + j + length] = (u - v + MOD) % MOD
                length <<= 1
            
            if invert:
                invN = pow(n, MOD - 2, MOD)
                for i in range(n):
                    a[i] = (a[i] * invN) % MOD

        fwht(A, False)
        fwht(B, False)
        
        C = [(A[i] * B[i]) % MOD for i in range(n)]
        
        fwht(C, True)
        return C

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        n = 1 << k
        A = [int(next(iterator)) for _ in range(n)]
        B = [int(next(iterator)) for _ in range(n)]
        
        sol = Solution()
        res = sol.fwht_xor_convolution(k, A, B)
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
using namespace std;

class Solution {
    long long MOD = 1000000007;

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

    void fwht(vector<long long>& a, bool invert) {
        int n = a.size();
        for (int len = 1; len < n; len <<= 1) {
            for (int i = 0; i < n; i += 2 * len) {
                for (int j = 0; j < len; j++) {
                    long long u = a[i + j];
                    long long v = a[i + j + len];
                    a[i + j] = (u + v) % MOD;
                    a[i + j + len] = (u - v + MOD) % MOD;
                }
            }
        }

        if (invert) {
            long long invN = modInverse(n);
            for (int i = 0; i < n; i++) {
                a[i] = (a[i] * invN) % MOD;
            }
        }
    }

public:
    vector<long long> fwht_xor_convolution(int k, vector<long long>& A, vector<long long>& B) {
        fwht(A, false);
        fwht(B, false);

        int n = A.size();
        vector<long long> C(n);
        for (int i = 0; i < n; i++) {
            C[i] = (A[i] * B[i]) % MOD;
        }

        fwht(C, true);
        return C;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;
    int n = 1 << k;

    vector<long long> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    vector<long long> B(n);
    for (int i = 0; i < n; i++) cin >> B[i];

    Solution solution;
    vector<long long> result = solution.fwht_xor_convolution(k, A, B);

    for (int i = 0; i < n; i++) {
        cout << result[i] << (i < n - 1 ? " " : "");
    }
    cout << "\n";

    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  fwht_xor_convolution(k, A, B) {
    const MOD = 1000000007n;
    const n = 1 << k;
    
    // Convert to BigInt
    const bigA = A.map(BigInt);
    const bigB = B.map(BigInt);

    function power(base, exp) {
      let res = 1n;
      base %= MOD;
      while (exp > 0n) {
        if (exp % 2n === 1n) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2n;
      }
      return res;
    }

    function modInverse(n) {
      return power(n, MOD - 2n);
    }

    function fwht(a, invert) {
      for (let len = 1; len < n; len <<= 1) {
        for (let i = 0; i < n; i += 2 * len) {
          for (let j = 0; j < len; j++) {
            const u = a[i + j];
            const v = a[i + j + len];
            a[i + j] = (u + v) % MOD;
            a[i + j + len] = (u - v + MOD) % MOD;
          }
        }
      }
      if (invert) {
        const invN = modInverse(BigInt(n));
        for (let i = 0; i < n; i++) {
          a[i] = (a[i] * invN) % MOD;
        }
      }
    }

    fwht(bigA, false);
    fwht(bigB, false);

    const bigC = new Array(n);
    for (let i = 0; i < n; i++) {
      bigC[i] = (bigA[i] * bigB[i]) % MOD;
    }

    fwht(bigC, true);

    return bigC.map(x => Number(x));
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
  const n = 1 << k;
  
  const A = [];
  for(let i=0; i<n; i++) A.push(parseInt(data[ptr++]));
  
  const B = [];
  for(let i=0; i<n; i++) B.push(parseInt(data[ptr++]));
  
  const solution = new Solution();
  const result = solution.fwht_xor_convolution(k, A, B);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `k=1`, `A=[1, 2]`, `B=[3, 4]`.
`N=2`.

1. **FWHT(A):**
   - `u=1, v=2`.
   - `A[0] = 1+2 = 3`.
   - `A[1] = 1-2 = -1 equiv MOD-1`.
   - `hatA = [3, -1]`.
2. **FWHT(B):**
   - `u=3, v=4`.
   - `B[0] = 3+4 = 7`.
   - `B[1] = 3-4 = -1`.
   - `hatB = [7, -1]`.
3. **Pointwise Multiply:**
   - `hatC[0] = 3 x 7 = 21`.
   - `hatC[1] = (-1) x (-1) = 1`.
   - `hatC = [21, 1]`.
4. **Inverse FWHT(C):**
   - `u=21, v=1`.
   - `C'[0] = 21+1 = 22`.
   - `C'[1] = 21-1 = 20`.
   - Divide by `N=2`:
     - `C[0] = 11`.
     - `C[1] = 10`.
5. **Result:** `[11, 10]`.

![Example Visualization](../images/MTH-008/example-1.png)

## ✅ Proof of Correctness

### Invariant
The Walsh-Hadamard Transform diagonalizes the XOR convolution operation.
`H_k = beginpmatrix 1 & 1  1 & -1 endpmatrix^otimes k`.

### Why the approach is correct
- The transform maps the convolution in the time domain to pointwise multiplication in the frequency (Walsh) domain.
- The inverse transform recovers the coefficients.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** AND/OR Convolution.
  - *Hint:* Use SOS DP (Sum Over Subsets) or Mobius Transform.
- **Extension 2:** K-dimensional FFT.
  - *Hint:* FWHT is essentially a K-dimensional FFT where each dimension has size 2.
- **Extension 3:** Subset Sum.
  - *Hint:* Use FWHT to count ways to get XOR sum `S`.

### Common Mistakes to Avoid

1. **Modulo Arithmetic**
   - ❌ Wrong: `(u - v) % MOD`.
   - ✅ Correct: `(u - v + MOD) % MOD`.

2. **Inverse Scaling**
   - ❌ Wrong: Forgetting to divide by `N` in inverse.
   - ✅ Correct: Multiply by `modInverse(N)`.

## Related Concepts

- **FFT:** For sum convolution (`i+j`).
- **SOS DP:** For subset convolution (`i & j`, `i | j`).
