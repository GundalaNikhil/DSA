---
problem_id: MTH_INVERT_VANDERMONDE__8453
display_id: MTH-013
slug: invert-vandermonde
title: "Fast Inversion of Vandermonde Matrix"
difficulty: Hard
difficulty_score: 76
topics:
  - MathAdvanced
  - Fast
tags:
  - math-advanced
  - vandermonde-matrix
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-013: Fast Inversion of Vandermonde Matrix

## Problem Statement

Given n distinct values x_i, efficiently compute the inverse of the n × n Vandermonde matrix V where V[i][j] = x_i^j. Use this to solve polynomial interpolation problems.

![Problem Illustration](../images/MTH-013/problem-illustration.png)

## Input Format

- Line 1: Two integers `n` (matrix size) and `MOD` (prime modulus)
- Line 2: n space-separated integers representing distinct values x*0, x_1, ..., x*{n-1}

## Output Format

n lines, each containing n space-separated integers representing the inverse Vandermonde matrix modulo MOD.

## Constraints

- `1 <= n <= 2000`
- `0 <= x_i < MOD`
- All x_i are distinct
- MOD is prime

## Example

**Input:**

```
2 1000000007
1 2
```

**Output:**

```
2 1000000006
1000000006 1
```

**Explanation:**

Vandermonde matrix for [1, 2]:
V = [1 1]
[1 2]

V^(-1) = [ 2 -1]
[-1 1]

mod 10^9+7:
-1 ≡ 1000000006

![Example Visualization](../images/MTH-013/example-1.png)

## Notes

- Vandermonde determinant: ∏(i>j) (x_i - x_j)
- Use Lagrange basis for fast inversion
- Applications in polynomial interpolation
- Time complexity: O(n²) with FFT optimization
- More efficient than general matrix inversion

## Related Topics

vandermonde-matrix, matrix-inversion, interpolation

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[][] invertVandermonde(int n, long mod, long[] x) {
        // Implement here
        return new long[0][0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] firstLine = line.trim().split("\\s+");
        int n = Integer.parseInt(firstLine[0]);
        long mod = Long.parseLong(firstLine[1]);

        long[] x = new long[n];
        String[] xLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) x[i] = Long.parseLong(xLine[i]);

        Solution sol = new Solution();
        long[][] result = sol.invertVandermonde(n, mod, x);

        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                out.print(result[i][j] + (j == n - 1 ? "" : " "));
            }
            out.println();
        }
        out.flush();
    }
}
```

### Python

```python
import sys

class Solution:
    def invert_vandermonde(self, n, mod, x):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    mod = int(input_data[1])
    x = [int(val) for val in input_data[2:2+n]]

    sol = Solution()
    result = sol.invert_vandermonde(n, mod, x)
    for row in result:
        print(*(row))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<long long>> invertVandermonde(int n, long long mod, const vector<long long>& x) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long mod;
    if (!(cin >> n >> mod)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; i++) cin >> x[i];

    Solution sol;
    vector<vector<long long>> result = sol.invertVandermonde(n, mod, x);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << result[i][j] << (j == n - 1 ? "" : " ");
        }
        cout << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  invertVandermonde(n, mod, x) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  const n = parseInt(input[0]);
  const mod = BigInt(input[1]);
  const x = [];
  for (let i = 0; i < n; i++) x.push(BigInt(input[2 + i]));

  const sol = new Solution();
  const result = sol.invertVandermonde(n, mod, x);
  for (const row of result) {
    process.stdout.write(row.join(" ") + "\n");
  }
}

solve();
```
