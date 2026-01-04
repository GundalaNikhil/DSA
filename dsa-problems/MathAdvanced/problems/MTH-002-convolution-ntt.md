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
import java.io.*;

class Solution {
    public long[] convolution(int n, long[] a, int m, long[] b) {
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
        String[] aLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) a[i] = Long.parseLong(aLine[i]);

        line = br.readLine();
        if (line == null) return;
        int m = Integer.parseInt(line.trim());
        long[] b = new long[m];
        String[] bLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < m; i++) b[i] = Long.parseLong(bLine[i]);

        Solution sol = new Solution();
        long[] result = sol.convolution(n, a, m, b);

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
    def convolution(self, n, a, m, b):
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
    result = sol.convolution(n, a, m, b)
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
    vector<long long> convolution(int n, vector<long long>& a, int m, vector<long long>& b) {
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
    vector<long long> result = sol.convolution(n, a, m, b);

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
  convolution(n, a, m, b) {
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
  const result = sol.convolution(n, a, m, b);
  process.stdout.write(result.join(" ") + "\n");
}

solve();
```
