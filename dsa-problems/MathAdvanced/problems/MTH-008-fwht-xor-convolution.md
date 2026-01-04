---
problem_id: MTH_FWHT_XOR_CONVOLUTION__7451
display_id: MTH-008
slug: fwht-xor-convolution
title: "Fast Walsh-Hadamard Transform (XOR Convolution)"
difficulty: Medium
difficulty_score: 62
topics:
  - MathAdvanced
  - Fast
tags:
  - math-advanced
  - fwht
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-008: Fast Walsh-Hadamard Transform (XOR Convolution)

## Problem Statement

Given two arrays A and B of length 2^k, compute their XOR convolution using the Fast Walsh-Hadamard Transform (FWHT). The XOR convolution C is defined as: C[i⊕j] += A[i] × B[j].

![Problem Illustration](../images/MTH-008/problem-illustration.png)

## Input Format

- Line 1: An integer `k` (arrays have length 2^k)
- Line 2: 2^k space-separated integers representing array A
- Line 3: 2^k space-separated integers representing array B

## Output Format

A single line containing 2^k space-separated integers representing the XOR convolution modulo 10^9+7.

## Constraints

- `0 <= k <= 17`
- `0 <= A[i], B[i] <= 10^9`
- Array length is power of 2
- Output modulo 10^9 + 7

## Example

**Input:**

```
1
1 2
3 4
```

**Output:**

```
11 10
```

**Explanation:**

A = [1, 2], B = [3, 4]

XOR convolution:

- C[0⊕0] = A[0]*B[0] + A[1]*B[1] = 1*3 + 2*4 = 11
- C[0⊕1] = A[0]*B[1] + A[1]*B[0] = 1*4 + 2*3 = 10

Result: [11, 10]

![Example Visualization](../images/MTH-008/example-1.png)

## Notes

- FWHT is similar to FFT but for XOR operation
- Transform, pointwise multiply, inverse transform
- Time complexity: O(n log n) where n = 2^k
- Applications in subset sum problems
- Different from standard convolution

## Related Topics

fwht, xor-convolution, walsh-hadamard

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[] xorConvolution(int k, long[] a, long[] b) {
        // Implement here
        return new long[0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        int k = Integer.parseInt(line.trim());
        int n = 1 << k;

        long[] a = new long[n];
        String[] aLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) a[i] = Long.parseLong(aLine[i]);

        long[] b = new long[n];
        String[] bLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) b[i] = Long.parseLong(bLine[i]);

        Solution sol = new Solution();
        long[] result = sol.xorConvolution(k, a, b);

        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0; i < n; i++) {
            out.print(result[i] + (i == n - 1 ? "" : " "));
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
    def xor_convolution(self, k, a, b):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    n = 1 << k
    a = [int(val) for val in input_data[1:1+n]]
    b = [int(val) for val in input_data[1+n:1+2*n]]

    sol = Solution()
    result = sol.xor_convolution(k, a, b)
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
    vector<long long> xorConvolution(int k, vector<long long>& a, vector<long long>& b) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;
    int n = 1 << k;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];

    Solution sol;
    vector<long long> result = sol.xorConvolution(k, a, b);

    for (int i = 0; i < n; i++) {
        cout << result[i] << (i == n - 1 ? "" : " ");
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
  xorConvolution(k, a, b) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  const k = parseInt(input[0]);
  const n = 1 << k;
  const a = [];
  const b = [];
  let idx = 1;
  for (let i = 0; i < n; i++) a.push(BigInt(input[idx++]));
  for (let i = 0; i < n; i++) b.push(BigInt(input[idx++]));

  const sol = new Solution();
  const result = sol.xorConvolution(k, a, b);
  process.stdout.write(result.join(" ") + "\n");
}

solve();
```
