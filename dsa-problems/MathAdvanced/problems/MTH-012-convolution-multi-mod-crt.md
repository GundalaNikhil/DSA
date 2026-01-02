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
time_limit: 2000
memory_limit: 256
---

# MTH-012: Convolution Under Multiple Mods with CRT

## Problem Statement

Compute convolution of two arrays when the final modulus is not NTT-friendly. Use Chinese Remainder Theorem (CRT) to combine results from multiple NTT-friendly primes.

![Problem Illustration](../images/MTH-012/problem-illustration.png)

## Input Format

- Line 1: Two integers `n` and `m` (array sizes)
- Line 2: n space-separated integers representing array A
- Line 3: m space-separated integers representing array B
- Line 4: An integer `MOD` (target modulus, may not be NTT-friendly)

## Output Format

A single line containing n+m-1 space-separated integers representing the convolution modulo MOD.

## Constraints

- `1 <= n, m <= 100000`
- `0 <= A[i], B[i] <= 10^9`
- `1 <= MOD <= 10^9 + 9`
- MOD may not support NTT

## Example

**Input:**
```
2 2
1 2
3 4
1000000007
```

**Output:**
```
3 10 8
```

**Explanation:**

A = [1, 2], B = [3, 4]

Convolution:
[1*3, 1*4+2*3, 2*4] = [3, 10, 8]

All values already < 10^9+7

![Example Visualization](../images/MTH-012/example-1.png)

## Notes

- Use 2-3 NTT-friendly primes (998244353, 1004535809, 469762049)
- Compute convolution mod each prime
- Apply CRT to reconstruct result mod target
- Handles arbitrary moduli
- Time complexity: O(n log n) per prime

## Related Topics

crt, chinese-remainder-theorem, multi-modular

---

## Solution Template

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
        return null;
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
        return []
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

