---
problem_id: MTH_MULTIPOINT_EVALUATION__8129
display_id: MTH-004
slug: multipoint-evaluation
title: "Multipoint Evaluation"
difficulty: Hard
difficulty_score: 75
topics:
  - MathAdvanced
  - Multipoint
tags:
  - math-advanced
  - polynomial-evaluation
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-004: Multipoint Evaluation

## Problem Statement

Given a polynomial P(x) and a set of points x_i, compute P(x_i) for all points using divide-and-conquer with product tree and remainder tree.

![Problem Illustration](../images/MTH-004/problem-illustration.png)

## Input Format

- Line 1: Two integers `d` (degree of P) and `n` (number of points)
- Line 2: `d+1` space-separated integers representing coefficients of P(x)
- Line 3: `n` space-separated integers representing evaluation points x_i

## Output Format

A single line containing `n` space-separated integers representing P(x_i) for each point, modulo 10^9+7.

## Constraints

- `0 <= d <= 100000`
- `1 <= n <= 100000`
- `-10^9 <= coefficients, x_i <= 10^9`
- All outputs modulo 10^9 + 7

## Example

**Input:**

```
2 3
1 0 1
0 1 2
```

**Output:**

```
1 2 5
```

**Explanation:**

P(x) = 1 + 0x + x² = 1 + x²

Evaluations:

- P(0) = 1 + 0² = 1
- P(1) = 1 + 1² = 2
- P(2) = 1 + 2² = 5

![Example Visualization](../images/MTH-004/example-1.png)

## Notes

- Use divide-and-conquer approach with product tree and remainder tree
- Product tree: Build tree of products of (x - x_i)
- Remainder tree: Compute remainders top-down
- Time complexity: O(n log² n) using FFT/NTT
- Faster than evaluating each point independently

## Related Topics

polynomial-evaluation, divide-and-conquer, product-tree

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[] evaluate(int d, int n, long[] p, long[] x) {
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
        int d = Integer.parseInt(firstLine[0]);
        int n = Integer.parseInt(firstLine[1]);

        long[] p = new long[d + 1];
        String[] pLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i <= d; i++) p[i] = Long.parseLong(pLine[i]);

        long[] xPoints = new long[n];
        String[] xLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) xPoints[i] = Long.parseLong(xLine[i]);

        Solution sol = new Solution();
        long[] result = sol.evaluate(d, n, p, xPoints);

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
    def evaluate(self, d, n, p, x):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    d = int(input_data[0])
    n = int(input_data[1])
    p = [int(val) for val in input_data[2:2+d+1]]
    x = [int(val) for val in input_data[2+d+1:2+d+1+n]]

    sol = Solution()
    result = sol.evaluate(d, n, p, x)
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
    vector<long long> evaluate(int d, int n, vector<long long>& p, vector<long long>& x) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int d, n;
    if (!(cin >> d >> n)) return 0;

    vector<long long> p(d + 1);
    for (int i = 0; i <= d; i++) cin >> p[i];

    vector<long long> x(n);
    for (int i = 0; i < n; i++) cin >> x[i];

    Solution sol;
    vector<long long> result = sol.evaluate(d, n, p, x);

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
  evaluate(d, n, p, x) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  const d = parseInt(input[0]);
  const n = parseInt(input[1]);
  const p = [];
  for (let i = 0; i <= d; i++) p.push(BigInt(input[2 + i]));
  const x = [];
  for (let i = 0; i < n; i++) x.push(BigInt(input[2 + d + 1 + i]));

  const sol = new Solution();
  const result = sol.evaluate(d, n, p, x);
  process.stdout.write(result.join(" ") + "\n");
}

solve();
```
