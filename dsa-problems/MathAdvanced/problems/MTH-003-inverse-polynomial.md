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
time_limit: 2000
memory_limit: 256
---

# MTH-003: Inverse Polynomial Mod x^n

## Problem Statement

Given a polynomial P(x) with P[0] ≠ 0 modulo a prime number, compute the inverse polynomial Q(x) such that P(x) × Q(x) ≡ 1 (mod x^n) under the given modulus.

The inverse polynomial Q(x) satisfies the property that when multiplied with P(x) and taken modulo x^n, the result is 1.

Use Newton iteration method with NTT for efficient computation.

![Problem Illustration](../images/MTH-003/problem-illustration.png)

## Input Format

- Line 1: Two integers `k` (number of coefficients of P) and `n` (the modulus degree)
- Line 2: `k` space-separated integers representing coefficients of P(x) from lowest to highest degree
- Line 3: An integer `MOD` (the prime modulus, typically 998244353)

## Output Format

A single line containing `n` space-separated integers representing the first `n` coefficients of Q(x) modulo MOD.

## Constraints

- `1 <= k <= 100000`
- `1 <= n <= 100000`
- `P[0] ≠ 0 (mod MOD)`
- `MOD` is a prime number (typically 998244353)
- `0 <= P[i] < MOD`

## Example

**Input:**

```
2 3
1 1
998244353
```

**Output:**

```
1 998244352 1
```

**Explanation:**

P(x) = 1 + x (coefficients [1, 1])
We need Q(x) such that P(x) × Q(x) ≡ 1 (mod x^3)

Q(x) = 1 - x + x² (coefficients [1, -1, 1])

Verification:
(1 + x)(1 - x + x²) = 1 - x + x² + x - x² + x³
= 1 + x³
≡ 1 (mod x^3)

Since -1 ≡ 998244352 (mod 998244353), the output is [1, 998244352, 1].

![Example Visualization](../images/MTH-003/example-1.png)

## Notes

- Newton iteration formula: Q\_{i+1}(x) = Q_i(x) × (2 - P(x) × Q_i(x)) mod x^{2^i}
- Start with Q_0(x) = P[0]^{-1} (modular inverse of first coefficient)
- Double the precision at each iteration
- Time complexity: O(n log n) using NTT
- Requires modular inverse computation and polynomial multiplication

## Related Topics

Newton Iteration, Polynomial Inverse, NTT, Modular Arithmetic, Divide and Conquer

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[] inversePolynomial(int k, int n, long[] p, long mod) {
        // Implement here
        return new long[0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] firstLine = line.trim().split("\\s+");
        int k = Integer.parseInt(firstLine[0]);
        int n = Integer.parseInt(firstLine[1]);

        long[] p = new long[k];
        String[] pLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < k; i++) p[i] = Long.parseLong(pLine[i]);

        long mod = Long.parseLong(br.readLine().trim());

        Solution sol = new Solution();
        long[] result = sol.inversePolynomial(k, n, p, mod);

        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0; i < result.length; i++) {
            out.print(result[i] + (i == result.length - 1 ? "" : " "));
        }
        out.println();
        out.flush();
    }
}
```

### Python

```python
import sys

class Solution:
    def inverse_polynomial(self, k, n, p, mod):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    n = int(input_data[1])
    p = [int(x) for x in input_data[2:2+k]]
    mod = int(input_data[2+k])

    sol = Solution()
    result = sol.inverse_polynomial(k, n, p, mod)
    sys.stdout.write(" ".join(map(str, result)) + "\n")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<long long> inversePolynomial(int k, int n, vector<long long>& p, long long mod) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, n;
    if (!(cin >> k >> n)) return 0;

    vector<long long> p(k);
    for (int i = 0; i < k; i++) cin >> p[i];

    long long mod;
    cin >> mod;

    Solution sol;
    vector<long long> result = sol.inversePolynomial(k, n, p, mod);

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
  inversePolynomial(k, n, p, mod) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  const k = parseInt(input[0]);
  const n = parseInt(input[1]);
  const p = [];
  for (let i = 0; i < k; i++) p.push(BigInt(input[2 + i]));
  const mod = BigInt(input[2 + k]);

  const sol = new Solution();
  const result = sol.inversePolynomial(k, n, p, mod);
  process.stdout.write(result.join(" ") + "\n");
}

solve();
```
