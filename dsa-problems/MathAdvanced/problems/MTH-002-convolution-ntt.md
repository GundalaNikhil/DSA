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
time_limit: 2000
memory_limit: 256
---

# MTH-002: Convolution Mod Prime Using NTT

## Problem Statement

Given two sequences A and B, compute their convolution using the Number Theoretic Transform (NTT) modulo a prime number 998244353. The convolution C of two sequences is defined as:

C[k] = Σ(i=0 to k) A[i] × B[k-i]

You must pad the sequences to the next power of 2 for efficient NTT computation.

![Problem Illustration](../images/MTH-002/problem-illustration.png)

## Input Format

- Line 1: An integer `n` representing the length of sequence A
- Line 2: `n` space-separated integers representing elements of A
- Line 3: An integer `m` representing the length of sequence B
- Line 4: `m` space-separated integers representing elements of B

## Output Format

A single line containing space-separated integers representing the convolution result modulo 998244353.

## Constraints

- `1 <= n, m <= 100000`
- `0 <= A[i], B[i] <= 998244352`
- The output length will be `n + m - 1`
- All operations must be performed modulo 998244353 (a prime suitable for NTT)

## Example

**Input:**

```
3
1 1 1
2
1 2
```

**Output:**

```
1 3 3 2
```

**Explanation:**

A = [1, 1, 1]
B = [1, 2]

Convolution C:

- C[0] = A[0] × B[0] = 1 × 1 = 1
- C[1] = A[0] × B[1] + A[1] × B[0] = 1 × 2 + 1 × 1 = 3
- C[2] = A[1] × B[1] + A[2] × B[0] = 1 × 2 + 1 × 1 = 3
- C[3] = A[2] × B[1] = 1 × 2 = 2

Result: [1, 3, 3, 2]

![Example Visualization](../images/MTH-002/example-1.png)

## Notes

- NTT (Number Theoretic Transform) is the modular arithmetic version of FFT
- The modulus 998244353 = 119 × 2^23 + 1 is chosen because it's a prime with a primitive root
- NTT allows exact integer arithmetic without floating-point errors
- Padding to power of 2 is essential for divide-and-conquer approach
- Time complexity: O((n+m) log(n+m))

## Related Topics

Number Theoretic Transform, FFT, Modular Arithmetic, Primitive Roots, Convolution

---

## Solution Template

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
            for (; (j & bit) != 0; bit >>= 1) j ^= bit;
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
        return null;
    }
}

class Main {
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

