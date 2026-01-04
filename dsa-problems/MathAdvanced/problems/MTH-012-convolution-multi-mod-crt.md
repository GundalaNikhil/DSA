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
import java.io.*;

class Solution {
    public long[] convolutionCRT(int n, int m, long[] a, long[] b, long mod) {
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
        int n = Integer.parseInt(firstLine[0]);
        int m = Integer.parseInt(firstLine[1]);

        long[] a = new long[n];
        String[] aLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) a[i] = Long.parseLong(aLine[i]);

        long[] b = new long[m];
        String[] bLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < m; i++) b[i] = Long.parseLong(bLine[i]);

        long mod = Long.parseLong(br.readLine().trim());

        Solution sol = new Solution();
        long[] result = sol.convolutionCRT(n, m, a, b, mod);

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
    def convolution_crt(self, n, m, a, b, mod):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    a = [int(val) for val in input_data[2:2+n]]
    b = [int(val) for val in input_data[2+n:2+n+m]]
    mod = int(input_data[2+n+m])

    sol = Solution()
    result = sol.convolution_crt(n, m, a, b, mod)
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
    vector<long long> convolutionCRT(int n, int m, vector<long long>& a, vector<long long>& b, long long mod) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < m; i++) cin >> b[i];

    long long mod;
    cin >> mod;

    Solution sol;
    vector<long long> result = sol.convolutionCRT(n, m, a, b, mod);

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
  convolutionCRT(n, m, a, b, mod) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  const n = parseInt(input[0]);
  const m = parseInt(input[1]);
  const a = [];
  const b = [];
  for (let i = 0; i < n; i++) a.push(BigInt(input[2 + i]));
  for (let i = 0; i < m; i++) b.push(BigInt(input[2 + n + i]));
  const mod = BigInt(input[2 + n + m]);

  const sol = new Solution();
  const result = sol.convolutionCRT(n, m, a, b, mod);
  process.stdout.write(result.join(" ") + "\n");
}

solve();
```
