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
import java.io.*;

class Solution {
    public long[] multiply(int n, long[] a, int m, long[] b) {
        // Implement here
        return new long[0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        int n = Integer.parseInt(line.trim());
        long[] a = new long[n];
        String[] aCoeffs = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) a[i] = Long.parseLong(aCoeffs[i]);

        line = br.readLine();
        if (line == null) return;
        int m = Integer.parseInt(line.trim());
        long[] b = new long[m];
        String[] bCoeffs = br.readLine().trim().split("\\s+");
        for (int i = 0; i < m; i++) b[i] = Long.parseLong(bCoeffs[i]);

        Solution sol = new Solution();
        long[] result = sol.multiply(n, a, m, b);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            sb.append(result[i]).append(i == result.length - 1 ? "" : " ");
        }
        System.out.println(sb.toString());
    }
}
```

### Python

```python
import sys

class Solution:
    def multiply(self, n, a, m, b):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n = int(input_data[idx])
    idx += 1
    a = [int(x) for x in input_data[idx:idx+n]]
    idx += n

    m = int(input_data[idx])
    idx += 1
    b = [int(x) for x in input_data[idx:idx+m]]

    sol = Solution()
    result = sol.multiply(n, a, m, b)
    print(*(result))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <complex>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<long long> multiply(int n, vector<long long>& a, int m, vector<long long>& b) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    if (!(cin >> m)) return 0;
    vector<long long> b(m);
    for (int i = 0; i < m; i++) cin >> b[i];

    Solution sol;
    vector<long long> result = sol.multiply(n, a, m, b);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  multiply(n, a, m, b) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) a.push(BigInt(input[idx++]));

  const m = parseInt(input[idx++]);
  const b = [];
  for (let i = 0; i < m; i++) b.push(BigInt(input[idx++]));

  const sol = new Solution();
  const result = sol.multiply(n, a, m, b);
  console.log(result.join(" "));
}

solve();
```
