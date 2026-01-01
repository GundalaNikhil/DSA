---
problem_id: MTH_POLYNOMIAL_MULTIPLICATION_FFT__2847
display_id: MTH-001
slug: polynomial-multiplication-fft
title: "Polynomial Multiplication via FFT"
difficulty: Medium
difficulty_score: 55
topics:
  - MathAdvanced
  - FFT
  - Polynomial
tags:
  - math-advanced
  - fft
  - polynomial-multiplication
  - medium
premium: true
subscription_tier: basic
---

# MTH-001: Polynomial Multiplication via FFT

## 📋 Problem Summary

You are given two polynomials, `A(x)` and `B(x)`, represented by their coefficients. You need to compute their product `C(x) = A(x) x B(x)` and return the coefficients of `C(x)` modulo `1,000,000,007`.
- Input: Two arrays of coefficients.
- Output: One array of coefficients representing the product polynomial.

## 🌍 Real-World Scenario

**Scenario Title:** The Audio Equalizer

Imagine you are an audio engineer working on a music production software. You have a raw audio signal (represented as a sequence of samples over time) and you want to apply a specific filter (like a bass boost or reverb).
- In signal processing, the audio signal can be viewed as a polynomial `A(x)`.
- The filter's impulse response is another polynomial `B(x)`.
- Applying the filter to the audio is mathematically equivalent to the **convolution** of these two sequences, which is exactly what polynomial multiplication computes.

If the audio track is long (e.g., 3 minutes at 44.1kHz = 8 million samples), a naive multiplication would take trillions of operations (`O(N^2)`). Using Fast Fourier Transform (FFT), we can do this in seconds (`O(N log N)`), making real-time audio effects possible.

**Why This Problem Matters:**

- **Signal Processing:** Convolution is the core operation for filtering, blurring images, and reverb.
- **Big Integer Multiplication:** Multiplying two massive numbers (millions of digits) uses FFT-based polynomial multiplication.
- **Competitive Programming:** A fundamental building block for advanced combinatorial counting problems.

![Real-World Application](../images/MTH-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: FFT Butterfly

The core of FFT is the "butterfly" operation, which combines results from smaller sub-problems.

```
      u --------+--------> u + v * w
                 \     /
                  \   /
                   \ /
                    X
                   / \
                  /   \
                 /     \
      v --------+--------> u - v * w
```
- `u` and `v` are values from the previous stage.
- `w` is a "root of unity" (a complex number that rotates the value).
- This structure allows us to reuse calculations, reducing complexity from `N^2` to `N log N`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Coefficients:** Input is given from lowest degree (`x^0`) to highest (`x^n-1`).
- **Modulo:** The problem asks for the result modulo `10^9 + 7`. Since standard FFT uses complex numbers which have precision issues, we typically use **Number Theoretic Transform (NTT)** for modular arithmetic.
- **Degree:** If `A` has degree `n-1` and `B` has degree `m-1`, the product has degree `n+m-2`. The output array size will be `n+m-1`.

### Core Concept: Point-Value Representation

1. **Coefficient Form:** `A(x) = a_0 + a_1x + dots` (Hard to multiply: `O(N^2)`).
2. **Point-Value Form:** `A(x)` evaluated at `N` distinct points: `(x_0, y_0), (x_1, y_1), dots`.
3. **Multiplication:** In point-value form, `C(x_i) = A(x_i) x B(x_i)`. This is just `O(N)` scalar multiplications!

**The Strategy:**
1. **Evaluation (FFT):** Convert `A` and `B` from coefficient form to point-value form.
2. **Pointwise Multiply:** Compute `C(x_i) = A(x_i) * B(x_i)`.
3. **Interpolation (Inverse FFT):** Convert `C` back to coefficient form.

## Naive Approach

### Intuition

Multiply every term in `A` by every term in `B` and sum up the coefficients for each power of `x`.

### Algorithm

1. Initialize `result` array of size `n+m-1` with zeros.
2. Loop `i` from 0 to `n-1`.
3. Loop `j` from 0 to `m-1`.
4. `result[i+j] += A[i] * B[j]`.
5. Take modulo at each step.

### Time Complexity

- **O(N * M)**. Too slow for `N, M = 100,000`.

### Space Complexity

- **O(N + M)**.

## Optimal Approach

### Key Insight

Use **Number Theoretic Transform (NTT)**. It's exactly like FFT but works in a finite field (integers modulo `P`) instead of complex numbers. This avoids floating-point errors and naturally handles the modulo requirement.

**Prerequisites for NTT:**
- Modulus `P` must be a prime of the form `c * 2^k + 1`.
- `10^9 + 7` is not an NTT-friendly prime.
- Standard approaches for arbitrary modulo (like `10^9+7`):
  1. Perform NTT with 3 different NTT-friendly primes (e.g., 998244353) and use Chinese Remainder Theorem (CRT) to combine results.
  2. Use the "Split FFT" method:
     - Split each coefficient `x` into `x = x_1 * M + x_0` where `M ≈ sqrt(P)`.
     - Then `A(x) = A_1(x)M + A_0(x)`.
     - Compute: `A * B = (A_1 M + A_0)(B_1 M + B_0) = A_1 B_1 M^2 + (A_1 B_0 + A_0 B_1) M + A_0 B_0`.
     - Use standard Complex FFT as the split values fit in `double` precision without error.

### Algorithm (Split FFT / Arbitrary Modulo FFT)

1. Choose `S = sqrtMOD ~= 31622`.
2. Split `A(x) -> A_1(x) * S + A_0(x)` where coefficients of `A_0, A_1 < S`.
3. Split `B(x) -> B_1(x) * S + B_0(x)`.
4. We need to compute `P_1 = A_1 B_1`, `P_2 = A_1 B_0`, `P_3 = A_0 B_1`, `P_4 = A_0 B_0`.
6. Use Complex FFT. Since inputs are small (`~= 3 * 10^4`), max output is `~= 10^5 * (3 * 10^4)^2 ~= 10^14`, which fits in `double`'s mantissa (53 bits `~= 9 * 10^15`).
7. Perform FFTs, multiply pointwise, Inverse FFT.
8. Reconstruct result: `Result = P_1 S^2 + (P_2 + P_3) S + P_4 +/-odMOD`.

### Time Complexity

- **O(N \log N)**.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/MTH-001/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-001/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private static final long MOD = 1000000007;
    private static final double PI = Math.acos(-1);

    static class Complex {
        double r, i;
        Complex(double r, double i) { this.r = r; this.i = i; }
        Complex add(Complex o) { return new Complex(r + o.r, i + o.i); }
        Complex sub(Complex o) { return new Complex(r - o.r, i - o.i); }
        Complex mul(Complex o) { return new Complex(r * o.r - i * o.i, r * o.i + i * o.r); }
    }

    private void fft(Complex[] a, boolean invert) {
        int n = a.length;
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; j >= bit; bit >>= 1) j -= bit;
            j += bit;
            if (i < j) { Complex temp = a[i]; a[i] = a[j]; a[j] = temp; }
        }
        for (int len = 2; len <= n; len <<= 1) {
            double ang = 2 * PI / len * (invert ? -1 : 1);
            Complex wlen = new Complex(Math.cos(ang), Math.sin(ang));
            for (int i = 0; i < n; i += len) {
                Complex w = new Complex(1, 0);
                for (int j = 0; j < len / 2; j++) {
                    Complex u = a[i + j], v = a[i + j + len / 2].mul(w);
                    a[i + j] = u.add(v);
                    a[i + j + len / 2] = u.sub(v);
                    w = w.mul(wlen);
                }
            }
        }
        if (invert) {
            for (int i = 0; i < n; i++) { a[i].r /= n; a[i].i /= n; }
        }
    }

    public long[] multiplyPolynomials(long[] A, long[] B) {
        int n = 1;
        while (n < A.length + B.length) n <<= 1;
        
        Complex[] fa = new Complex[n];
        Complex[] fb = new Complex[n];
        
        // Split coefficients to handle large modulo
        // Using simplified approach: Assuming standard FFT precision is enough for this problem's constraints
        // If strict 10^9+7 with full range, need 2-3 FFTs or splitting.
        // Here implementing standard FFT for simplicity, noting precision limits.
        // For robust solution, one would split A[i] = A1[i]*S + A0[i].
        
        // Let's implement the splitting method (MTT) for correctness.
        int S = 32000;
        Complex[] a0 = new Complex[n], a1 = new Complex[n];
        Complex[] b0 = new Complex[n], b1 = new Complex[n];
        
        for(int i=0; i<n; i++) {
            long valA = (i < A.length) ? A[i] : 0;
            long valB = (i < B.length) ? B[i] : 0;
            a0[i] = new Complex(valA % S, 0);
            a1[i] = new Complex(valA / S, 0);
            b0[i] = new Complex(valB % S, 0);
            b1[i] = new Complex(valB / S, 0);
        }
        
        fft(a0, false); fft(a1, false);
        fft(b0, false); fft(b1, false);
        
        Complex[] c0 = new Complex[n], c1 = new Complex[n], c2 = new Complex[n];
        for(int i=0; i<n; i++) {
            // (a1*S + a0) * (b1*S + b0) = a1*b1*S^2 + (a1*b0 + a0*b1)*S + a0*b0
            c0[i] = a0[i].mul(b0[i]); // a0*b0
            c2[i] = a1[i].mul(b1[i]); // a1*b1
            // Middle term: (a0+a1)*(b0+b1) - a0*b0 - a1*b1
            Complex sumA = a0[i].add(a1[i]);
            Complex sumB = b0[i].add(b1[i]);
            c1[i] = sumA.mul(sumB).sub(c0[i]).sub(c2[i]);
        }
        
        fft(c0, true); fft(c1, true); fft(c2, true);
        
        long[] res = new long[A.length + B.length - 1];
        for(int i=0; i<res.length; i++) {
            long v0 = (long)(c0[i].r + 0.5) % MOD;
            long v1 = (long)(c1[i].r + 0.5) % MOD;
            long v2 = (long)(c2[i].r + 0.5) % MOD;
            
            long term1 = v2 * S % MOD * S % MOD;
            long term2 = v1 * S % MOD;
            long term3 = v0;
            
            res[i] = (term1 + term2 + term3) % MOD;
        }
        return res;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] A = new long[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextLong();
        
        int m = sc.nextInt();
        long[] B = new long[m];
        for (int i = 0; i < m; i++) B[i] = sc.nextLong();
        
        Solution solution = new Solution();
        long[] result = solution.multiplyPolynomials(A, B);
        
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
import math

class Solution:
    def multiply_polynomials(self, A: list[int], B: list[int]) -> list[int]:
        MOD = 1000000007
        n = 1
        while n < len(A) + len(B):
            n <<= 1
            
        # Standard FFT implementation
        def fft(a, invert):
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
                ang = 2 * math.pi / length * (-1 if invert else 1)
                wlen = complex(math.cos(ang), math.sin(ang))
                for i in range(0, n, length):
                    w = complex(1, 0)
                    for j in range(length // 2):
                        u = a[i + j]
                        v = a[i + j + length // 2] * w
                        a[i + j] = u + v
                        a[i + j + length // 2] = u - v
                        w *= wlen
                length <<= 1
                
            if invert:
                for i in range(n):
                    a[i] /= n

        # Splitting for precision
        S = 32000
        a0 = [complex(x % S, 0) for x in A] + [0] * (n - len(A))
        a1 = [complex(x // S, 0) for x in A] + [0] * (n - len(A))
        b0 = [complex(x % S, 0) for x in B] + [0] * (n - len(B))
        b1 = [complex(x // S, 0) for x in B] + [0] * (n - len(B))
        
        fft(a0, False); fft(a1, False)
        fft(b0, False); fft(b1, False)
        
        c0 = [a0[i] * b0[i] for i in range(n)]
        c2 = [a1[i] * b1[i] for i in range(n)]
        c1 = [(a0[i] + a1[i]) * (b0[i] + b1[i]) - c0[i] - c2[i] for i in range(n)]
        
        fft(c0, True); fft(c1, True); fft(c2, True)
        
        res = []
        for i in range(len(A) + len(B) - 1):
            v0 = int(c0[i].real + 0.5) % MOD
            v1 = int(c1[i].real + 0.5) % MOD
            v2 = int(c2[i].real + 0.5) % MOD
            val = (v2 * S * S + v1 * S + v0) % MOD
            res.append(val)
            
        return res

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
        res = sol.multiply_polynomials(A, B)
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
#include <complex>
#include <cmath>
#include <algorithm>

using namespace std;

const double PI = acos(-1);
const int MOD = 1000000007;

using cd = complex<double>;

void fft(vector<cd> & a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        double ang = 2 * PI / len * (invert ? -1 : 1);
        cd wlen(cos(ang), sin(ang));
        for (int i = 0; i < n; i += len) {
            cd w(1);
            for (int j = 0; j < len / 2; j++) {
                cd u = a[i+j], v = a[i+j+len/2] * w;
                a[i+j] = u + v;
                a[i+j+len/2] = u - v;
                w *= wlen;
            }
        }
    }
    if (invert) {
        for (cd & x : a) x /= n;
    }
}

class Solution {
public:
    vector<long long> multiplyPolynomials(vector<long long>& A, vector<long long>& B) {
        int n = 1;
        while (n < A.size() + B.size()) n <<= 1;
        
        int S = 32000;
        vector<cd> a0(n), a1(n), b0(n), b1(n);
        
        for(int i=0; i<A.size(); i++) {
            a0[i] = cd(A[i] % S, 0);
            a1[i] = cd(A[i] / S, 0);
        }
        for(int i=0; i<B.size(); i++) {
            b0[i] = cd(B[i] % S, 0);
            b1[i] = cd(B[i] / S, 0);
        }
        
        fft(a0, false); fft(a1, false);
        fft(b0, false); fft(b1, false);
        
        vector<cd> c0(n), c1(n), c2(n);
        for(int i=0; i<n; i++) {
            c0[i] = a0[i] * b0[i];
            c2[i] = a1[i] * b1[i];
            c1[i] = (a0[i] + a1[i]) * (b0[i] + b1[i]) - c0[i] - c2[i];
        }
        
        fft(c0, true); fft(c1, true); fft(c2, true);
        
        vector<long long> res(A.size() + B.size() - 1);
        for(int i=0; i<res.size(); i++) {
            long long v0 = (long long)(c0[i].real() + 0.5) % MOD;
            long long v1 = (long long)(c1[i].real() + 0.5) % MOD;
            long long v2 = (long long)(c2[i].real() + 0.5) % MOD;
            
            res[i] = (v2 * S % MOD * S % MOD + v1 * S % MOD + v0) % MOD;
        }
        return res;
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
    vector<long long> result = solution.multiplyPolynomials(A, B);

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

class Complex {
  constructor(r, i) { this.r = r; this.i = i; }
  add(o) { return new Complex(this.r + o.r, this.i + o.i); }
  sub(o) { return new Complex(this.r - o.r, this.i - o.i); }
  mul(o) { return new Complex(this.r * o.r - this.i * o.i, this.r * o.i + this.i * o.r); }
}

function fft(a, invert) {
  const n = a.length;
  for (let i = 1, j = 0; i < n; i++) {
    let bit = n >> 1;
    for (; j & bit; bit >>= 1) j ^= bit;
    j ^= bit;
    if (i < j) [a[i], a[j]] = [a[j], a[i]];
  }
  for (let len = 2; len <= n; len <<= 1) {
    const ang = 2 * Math.PI / len * (invert ? -1 : 1);
    const wlen = new Complex(Math.cos(ang), Math.sin(ang));
    for (let i = 0; i < n; i += len) {
      let w = new Complex(1, 0);
      for (let j = 0; j < len / 2; j++) {
        const u = a[i + j];
        const v = a[i + j + len / 2].mul(w);
        a[i + j] = u.add(v);
        a[i + j + len / 2] = u.sub(v);
        w = w.mul(wlen);
      }
    }
  }
  if (invert) {
    for (let i = 0; i < n; i++) { a[i].r /= n; a[i].i /= n; }
  }
}

class Solution {
  multiplyPolynomials(A, B) {
    const MOD = 1000000007n;
    let n = 1;
    while (n < A.length + B.length) n <<= 1;
    
    const S = 32000;
    const a0 = new Array(n).fill(null).map(() => new Complex(0, 0));
    const a1 = new Array(n).fill(null).map(() => new Complex(0, 0));
    const b0 = new Array(n).fill(null).map(() => new Complex(0, 0));
    const b1 = new Array(n).fill(null).map(() => new Complex(0, 0));
    
    for(let i=0; i<n; i++) {
        if (i < A.length) {
            a0[i].r = A[i] % S;
            a1[i].r = Math.floor(A[i] / S);
        }
        if (i < B.length) {
            b0[i].r = B[i] % S;
            b1[i].r = Math.floor(B[i] / S);
        }
    }
    
    fft(a0, false); fft(a1, false);
    fft(b0, false); fft(b1, false);
    
    const c0 = new Array(n), c1 = new Array(n), c2 = new Array(n);
    for(let i=0; i<n; i++) {
        c0[i] = a0[i].mul(b0[i]);
        c2[i] = a1[i].mul(b1[i]);
        const sumA = a0[i].add(a1[i]);
        const sumB = b0[i].add(b1[i]);
        c1[i] = sumA.mul(sumB).sub(c0[i]).sub(c2[i]);
    }
    
    fft(c0, true); fft(c1, true); fft(c2, true);
    
    const res = [];
    const Sn = BigInt(S);
    for(let i=0; i < A.length + B.length - 1; i++) {
        const v0 = BigInt(Math.round(c0[i].r)) % MOD;
        const v1 = BigInt(Math.round(c1[i].r)) % MOD;
        const v2 = BigInt(Math.round(c2[i].r)) % MOD;
        
        let val = (v2 * Sn * Sn + v1 * Sn + v0) % MOD;
        res.push(Number(val));
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
  const A = [];
  for(let i=0; i<n; i++) A.push(parseInt(data[ptr++]));
  
  const m = parseInt(data[ptr++]);
  const B = [];
  for(let i=0; i<m; i++) B.push(parseInt(data[ptr++]));

  const solution = new Solution();
  const result = solution.multiplyPolynomials(A, B);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `A = [1, 2]`, `B = [3, 4]`
- `A(x) = 1 + 2x`
- `B(x) = 3 + 4x`

1. **Pad to power of 2:** `N=4`.
   - `A = [1, 2, 0, 0]`
   - `B = [3, 4, 0, 0]`
2. **FFT (Evaluation):**
   - Evaluate at roots of unity `omega^0, omega^1, omega^2, omega^3`.
   - `A_eval = [3, 1+2i, -1, 1-2i]`
   - `B_eval = [7, 3+4i, -1, 3-4i]`
3. **Pointwise Multiply:**
   - `C_eval[0] = 3 x 7 = 21`
   - `C_eval[1] = (1+2i)(3+4i) = 3 + 4i + 6i - 8 = -5 + 10i`
   - `C_eval[2] = (-1)(-1) = 1`
   - `C_eval[3] = (1-2i)(3-4i) = -5 - 10i`
4. **Inverse FFT (Interpolation):**
   - Transform back to coefficients: `[3, 10, 8, 0]`.
5. **Result:** `3 10 8`.

![Example Visualization](../images/MTH-001/example-1.png)

## ✅ Proof of Correctness

### Invariant
The convolution theorem states that `mathcalF(A * B) = mathcalF(A) x mathcalF(B)`, where `mathcalF` is the Fourier Transform and `x` is pointwise multiplication.

### Why the approach is correct
- **Evaluation:** FFT correctly evaluates the polynomial at `N` points in `O(N log N)`.
- **Uniqueness:** A polynomial of degree `N-1` is uniquely determined by `N` points.
- **Interpolation:** Inverse FFT correctly reconstructs the coefficients from the point values.
- **Splitting:** The "Split FFT" technique avoids floating point precision errors for large coefficients by breaking them into smaller chunks that fit within `double` precision.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Multiply polynomials with arbitrary modulo (e.g., `10^9+9`).
  - *Hint:* Use the splitting method (MTT) shown above or 3-modulus NTT + CRT.
- **Extension 2:** Multiply large integers.
  - *Hint:* Treat integers as polynomials where `x=10`. Handle carries after multiplication.
- **Extension 3:** Count subsets with sum `K`.
  - *Hint:* Generating functions. If item `v` exists, term is `x^v`. Square the polynomial.

### Common Mistakes to Avoid

1. **Precision Errors**
   - ❌ Wrong: Using standard `complex<double>` FFT directly on coefficients `> 10^4` without splitting.
   - ✅ Correct: Use Split FFT (MTT) or NTT if the modulus allows.

2. **Array Sizing**
   - ❌ Wrong: Using size `N+M`.
   - ✅ Correct: Must be a **power of 2** greater than `N+M-2`.

## Related Concepts

- **NTT:** FFT for modular arithmetic.
- **Karatsuba Algorithm:** `O(N^1.58)` multiplication (simpler but slower than FFT for very large `N`).
- **Generating Functions:** Combinatorial counting using polynomials.
