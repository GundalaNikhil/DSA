---
problem_id: MTH_BERLEKAMP_MASSEY__5628
display_id: MTH-010
slug: berlekamp-massey
title: "Berlekamp-Massey Sequence Reconstruction"
difficulty: Hard
difficulty_score: 80
topics:
  - MathAdvanced
  - Berlekamp-Massey
tags:
  - math-advanced
  - berlekamp-massey
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-010: Berlekamp-Massey Sequence Reconstruction

## Problem Statement

Given the first 2k terms of a linearly recurrent sequence, use the Berlekamp-Massey algorithm to find the minimal recurrence relation and compute the nth term.

![Problem Illustration](../images/MTH-010/problem-illustration.png)

## Input Format

- Line 1: Two integers `m` (number of terms given) and `n` (target term)
- Line 2: m space-separated integers representing the sequence
- Line 3: An integer `MOD` (prime modulus)

## Output Format

A single integer representing the nth term of the sequence modulo MOD.

## Constraints

- `1 <= m <= 4000`
- `0 <= n <= 10^18`
- `0 <= sequence[i] < MOD`
- MOD is prime

## Example

**Input:**
```
6 10
1 1 2 3 5 8
1000000007
```

**Output:**
```
89
```

**Explanation:**

Sequence: 1, 1, 2, 3, 5, 8 (Fibonacci)

Berlekamp-Massey finds: a_n = a_{n-1} + a_{n-2}

Continuing: 13, 21, 34, 55, 89
a_10 = 89

![Example Visualization](../images/MTH-010/example-1.png)

## Notes

- Berlekamp-Massey finds minimal linear recurrence
- Works with partial sequence information
- Use matrix exponentiation for large n
- Time complexity: O(m²) for algorithm, O(k³ log n) for term
- Applications in cryptography and coding theory

## Related Topics

berlekamp-massey, linear-recurrence, sequence-reconstruction

---

## Solution Template

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

    // Polynomial Multiplication (Naive O(N^2))
    private long[] polyMul(long[] A, long[] B) {
        int n = A.length;
        int m = B.length;
        long[] res = new long[n + m - 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                res[i + j] = (res[i + j] + A[i] * B[j]) % MOD;
            }
        }
        return res;
    }

    // Polynomial Modulo (Naive O(N*M))
    private long[] polyMod(long[] A, long[] Mod) {
        int n = A.length;
        int m = Mod.length; // Degree of Mod is m-1
        if (n < m) return A;
        
        // We want remainder of A / Mod.
        // Mod is monic? Not necessarily x^L - ...
        // In Kitamasa, Mod is x^L - \sum c_i x^i. So Mod[L] = 1.
        // We reduce from highest degree.
        
        long[] res = Arrays.copyOf(A, n);
        for (int i = n - 1; i >= m - 1; i--) {
            long factor = res[i]; // Since Mod[last] is 1
            if (factor == 0) continue;
            for (int j = 0; j < m; j++) {
                // Mod corresponds to x^L - \sum c_i x^i
                // If recurrence is S[n] = \sum c_i S[n-i], char poly is x^L - \sum c_i x^{L-i}.
                // Let's implement simpler logic:
                // We have relation x^L = \sum_{i=1}^L c_i x^{L-i}.
                // Whenever we see x^k (k >= L), we replace x^L with the sum.
                // Let Mod be the array representing x^L - \sum ...
                // Mod[m-1] is coeff of x^L (which is 1).
                int degDiff = i - (m - 1);
                res[i - j] = (res[i - j] - factor * Mod[m - 1 - j] % MOD + MOD) % MOD;
            }
        }
        return Arrays.copyOf(res, m - 1);
    }
    
    // Better Kitamasa:
    // We want x^n mod (x^L - \sum_{i=1}^L C_i x^{L-i})
    // Let Rec = [C_1, C_2, ..., C_L]
    // Multiplication: A * B. Then reduce using Rec.
    private long[] combine(long[] A, long[] B, long[] Rec) {
        long[] prod = polyMul(A, B);
        int L = Rec.length;
        // Reduce terms with degree >= L
        for (int i = prod.length - 1; i >= L; i--) {
            long factor = prod[i];
            if (factor == 0) continue;
            for (int j = 0; j < L; j++) {
                // x^i = x^{i-L} * x^L = x^{i-L} * \sum C_k x^{L-k}
                // coeff of x^{i-1-j} gets added C_{j+1} * factor
                // Rec[j] is C_{j+1}
                int targetDeg = i - 1 - j;
                prod[targetDeg] = (prod[targetDeg] + factor * Rec[j]) % MOD;
            }
        }
        return Arrays.copyOf(prod, L);
    }

    public long berlekamp_massey(int m, long n, long mod, long[] S) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int m = sc.nextInt();
        long n = sc.nextLong();
        long[] S = new long[m];
        for (int i = 0; i < m; i++) S[i] = sc.nextLong();
        long MOD = sc.nextLong();
        
        Solution solution = new Solution();
        System.out.println(solution.berlekamp_massey(m, n, MOD, S));
        
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def berlekamp_massey(self, m: int, n: int, MOD: int, S: list[int]) -> int:
        return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        m = int(next(iterator))
        n = int(next(iterator))
        S = [int(next(iterator)) for _ in range(m)]
        MOD = int(next(iterator))
        
        sol = Solution()
        print(sol.berlekamp_massey(m, n, MOD, S))
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

    vector<long long> combine(const vector<long long>& A, const vector<long long>& B, const vector<long long>& Rec) {
        int K = Rec.size();
        vector<long long> prod(2 * K, 0);
        for (int i = 0; i < A.size(); i++) {
            for (int j = 0; j < B.size(); j++) {
                prod[i + j] = (prod[i + j] + A[i] * B[j]) % MOD;
            }
        }

        for (int i = prod.size() - 1; i >= K; i--) {
            long long factor = prod[i];
            if (factor == 0) continue;
            for (int j = 0; j < K; j++) {
                int target = i - 1 - j;
                prod[target] = (prod[target] + factor * Rec[j]) % MOD;
            }
        }
        prod.resize(K);
        return prod;
    }

public:
    long long berlekamp_massey(int m, long long n, long long mod, vector<long long>& S) {
        MOD = mod;
        vector<long long> C = {1};
        vector<long long> B = {1};
        int L = 0;
        int b = 1;
        long long b_delta = 1;

        for (int i = 0; i < m; i++) {
            long long delta = S[i];
            for (int j = 1; j < C.size(); j++) {
                delta = (delta + C[j] * S[i - j]) % MOD;
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

        int K = C.size() - 1;
        if (K == 0) return 0;

        vector<long long> Rec(K);
        for (int i = 0; i < K; i++) {
            Rec[i] = (MOD - C[i + 1]) % MOD;
        }

        if (n < m) return S[n];

        vector<long long> res(K, 0);
        res[0] = 1;
        vector<long long> base(K, 0);
        if (K > 1) base[1] = 1;
        else base[0] = Rec[0];

        long long exp = n;
        while (exp > 0) {
            if (exp & 1) res = combine(res, base, Rec);
            base = combine(base, base, Rec);
            exp >>= 1;
        }

        long long ans = 0;
        for (int i = 0; i < K; i++) {
            ans = (ans + res[i] * S[i]) % MOD;
        }

        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    long long n, MOD;
    if (!(cin >> m >> n)) return 0;
    vector<long long> S(m);
    for (int i = 0; i < m; i++) cin >> S[i];
    cin >> MOD;

    Solution solution;
    cout << solution.berlekamp_massey(m, n, MOD, S) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  berlekamp_massey(m, n, MOD, S) {
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
  
  const m = parseInt(data[ptr++]);
  const n = BigInt(data[ptr++]);
  
  const S = [];
  for(let i=0; i<m; i++) S.push(parseInt(data[ptr++]));
  
  const MOD = parseInt(data[ptr++]);
  
  const solution = new Solution();
  console.log(solution.berlekamp_massey(m, n, MOD, S));
});
```

