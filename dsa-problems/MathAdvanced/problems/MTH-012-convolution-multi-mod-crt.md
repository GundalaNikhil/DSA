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
        return 0;
    }

    private long modInverse(long n, long mod) {
        return 0;
    }

    private void ntt(long[] a, boolean invert, long mod, long g) {
    }

    private long[] convolve(long[] A, long[] B, long mod, long g) {
        return null;
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
        return 0;
    }

    long long modInverse(long long n, long long mod) {
        return 0;
    }

    void ntt(vector<long long>& a, bool invert, long long mod, long long g) {
    }

    vector<long long> convolve(const vector<long long>& A, const vector<long long>& B, long long mod, long long g) {
        return {};
    }

public:
    vector<long long> convolution_multi_mod_crt(int n, int m, vector<long long>& A, vector<long long>& B, long long targetMod) {
        return {};
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

