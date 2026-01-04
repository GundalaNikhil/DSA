---
problem_id: MTH_SUBSET_CONVOLUTION_AND_OR__9174
display_id: MTH-009
slug: subset-convolution-and-or
title: "Subset Convolution (AND/OR)"
difficulty: Hard
difficulty_score: 78
topics:
  - MathAdvanced
  - Subset
tags:
  - math-advanced
  - subset-convolution
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-009: Subset Convolution (AND/OR)

## Problem Statement

Perform subset convolution under bitwise AND or OR operations using zeta and Möbius transforms on the subset lattice.

![Problem Illustration](../images/MTH-009/problem-illustration.png)

## Input Format

- Line 1: Two integers `n` (bit size) and `op` (0 for AND, 1 for OR)
- Line 2: 2^n space-separated integers representing array A
- Line 3: 2^n space-separated integers representing array B

## Output Format

A single line containing 2^n space-separated integers representing the subset convolution modulo 10^9+7.

## Constraints

- `1 <= n <= 20`
- `0 <= A[i], B[i] <= 10^9`
- op = 0 (AND) or 1 (OR)
- Output modulo 10^9 + 7

## Example

**Input:**

```
2 1
1 1 0 0
0 1 1 0
```

**Output:**

```
0 1 1 2
```

**Explanation:**

n=2, so we have 4 subsets: {}, {0}, {1}, {0,1}
A = [1, 1, 0, 0]
B = [0, 1, 1, 0]

OR convolution computes sum over subsets.

![Example Visualization](../images/MTH-009/example-1.png)

## Notes

- Use ranked zeta/Möbius transforms
- Subset convolution: C[S] = Σ(T⊆S) A[T] × B[S\T]
- Time complexity: O(2^n × n²)
- Applications in DP on subsets
- More complex than FWHT

## Related Topics

subset-convolution, zeta-transform, mobius-transform

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[] subsetConvolution(int n, int op, long[] a, long[] b) {
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
        int op = Integer.parseInt(firstLine[1]);
        int size = 1 << n;

        long[] a = new long[size];
        String[] aLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < size; i++) a[i] = Long.parseLong(aLine[i]);

        long[] b = new long[size];
        String[] bLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < size; i++) b[i] = Long.parseLong(bLine[i]);

        Solution sol = new Solution();
        long[] result = sol.subsetConvolution(n, op, a, b);

        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0; i < size; i++) {
            out.print(result[i] + (i == size - 1 ? "" : " "));
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
    def subset_convolution(self, n, op, a, b):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    op = int(input_data[1])
    size = 1 << n
    a = [int(val) for val in input_data[2:2+size]]
    b = [int(val) for val in input_data[2+size:2+2*size]]

    sol = Solution()
    result = sol.subset_convolution(n, op, a, b)
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
    vector<long long> subsetConvolution(int n, int op, vector<long long>& a, vector<long long>& b) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, op;
    if (!(cin >> n >> op)) return 0;
    int size = 1 << n;

    vector<long long> a(size), b(size);
    for (int i = 0; i < size; i++) cin >> a[i];
    for (int i = 0; i < size; i++) cin >> b[i];

    Solution sol;
    vector<long long> result = sol.subsetConvolution(n, op, a, b);

    for (int i = 0; i < size; i++) {
        cout << result[i] << (i == size - 1 ? "" : " ");
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
  subsetConvolution(n, op, a, b) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  const n = parseInt(input[0]);
  const op = parseInt(input[1]);
  const size = 1 << n;
  const a = [];
  const b = [];
  let idx = 2;
  for (let i = 0; i < size; i++) a.push(BigInt(input[idx++]));
  for (let i = 0; i < size; i++) b.push(BigInt(input[idx++]));

  const sol = new Solution();
  const result = sol.subsetConvolution(n, op, a, b);
  process.stdout.write(result.join(" ") + "\n");
}

solve();
```
