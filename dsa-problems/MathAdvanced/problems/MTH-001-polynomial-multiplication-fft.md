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
time_limit: 2000
memory_limit: 256
---

# MTH-001: Polynomial Multiplication via FFT

## Problem Statement

Given two polynomials A(x) and B(x) represented as arrays of their coefficients, compute their product polynomial C(x) = A(x) × B(x) using the Fast Fourier Transform (FFT) algorithm. Return the coefficients of the resulting polynomial modulo 1,000,000,007.

A polynomial is represented as an array where the index represents the power of x. For example, [1, 2, 3] represents the polynomial 1 + 2x + 3x².

![Problem Illustration](../images/MTH-001/problem-illustration.png)

## Input Format

- Line 1: An integer `n` representing the degree of polynomial A(x) plus one (number of coefficients)
- Line 2: `n` space-separated integers representing coefficients of A(x) from lowest to highest degree
- Line 3: An integer `m` representing the degree of polynomial B(x) plus one (number of coefficients)
- Line 4: `m` space-separated integers representing coefficients of B(x) from lowest to highest degree

## Output Format

A single line containing space-separated integers representing the coefficients of the product polynomial C(x) modulo 1,000,000,007, from lowest to highest degree.

## Constraints

- `1 <= n, m <= 100000`
- `0 <= A[i], B[i] <= 1000000006`
- The degree of the resulting polynomial will be at most `n + m - 2`
- All coefficients must be output modulo `10^9 + 7`

## Example

**Input:**

```
2
1 2
2
3 4
```

**Output:**

```
3 10 8
```

**Explanation:**

A(x) = 1 + 2x
B(x) = 3 + 4x

C(x) = A(x) × B(x) = (1 + 2x)(3 + 4x)
= 1×3 + 1×4x + 2x×3 + 2x×4x
= 3 + 4x + 6x + 8x²
= 3 + 10x + 8x²

Therefore, the coefficients are [3, 10, 8].

![Example Visualization](../images/MTH-001/example-1.png)

## Notes

- FFT allows polynomial multiplication in O((n+m) log(n+m)) time instead of O(nm) with naive approach
- You may need to pad the input polynomials to the next power of 2 for FFT implementation
- Handle modular arithmetic carefully to avoid overflow
- The result polynomial has degree (n-1) + (m-1) = n + m - 2
- Consider using Complex numbers for FFT or Number Theoretic Transform (NTT) for modular arithmetic

## Related Topics

Fast Fourier Transform, Number Theoretic Transform, Polynomial Algorithms, Divide and Conquer

---

## Solution Template

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
        return null;
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
        return []
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
    return 0;
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

