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

class Solution {
    public long[] inversePolynomial(long[] P, int n, long MOD) {
        // Implementation here
        return new long[0];
    }
}

class Main {
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
        # Implementation here
        return []

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
public:
    vector<long long> inversePolynomial(vector<long long>& P, int n, long long mod) {
        // Implementation here
        return {};
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
    // Implementation here
    return null;
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
