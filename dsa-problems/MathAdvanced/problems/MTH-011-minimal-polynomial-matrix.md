---
problem_id: MTH_MINIMAL_POLYNOMIAL_MATRIX__3891
display_id: MTH-011
slug: minimal-polynomial-matrix
title: "Minimal Polynomial of Matrix (Krylov)"
difficulty: Hard
difficulty_score: 82
topics:
  - MathAdvanced
  - Minimal
tags:
  - math-advanced
  - minimal-polynomial
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-011: Minimal Polynomial of Matrix (Krylov)

## Problem Statement

Compute the minimal polynomial of an n × n matrix using the Krylov sequence method combined with Berlekamp-Massey algorithm on the generated vector sequence.

![Problem Illustration](../images/MTH-011/problem-illustration.png)

## Input Format

- Line 1: Two integers `n` (matrix size) and `MOD` (prime modulus)
- Next n lines: n space-separated integers representing each row of the matrix

## Output Format

First line: degree d of minimal polynomial
Second line: d+1 space-separated integers representing coefficients from constant to highest degree.

## Constraints

- `1 <= n <= 200`
- `0 <= matrix[i][j] < MOD`
- MOD is prime (typically 10^9 + 7)

## Example

**Input:**

```
2 1000000007
1 1
0 1
```

**Output:**

```
2
1 1000000005 1
```

**Explanation:**

Matrix:
[1 1]
[0 1]

This is a Jordan block. Minimal polynomial: (x-1)²
= x² - 2x + 1

Coefficients: [1, -2, 1]
-2 mod 10^9+7 = 1000000005

![Example Visualization](../images/MTH-011/example-1.png)

## Notes

- Generate Krylov sequence: v, Av, A²v, ...
- Apply Berlekamp-Massey to find recurrence
- Minimal polynomial divides characteristic polynomial
- Time complexity: O(n³) for Krylov, O(n²) for BM
- Important in matrix theory

## Related Topics

minimal-polynomial, krylov-sequence, matrix-theory

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[] minimalPolynomial(int n, long mod, long[][] matrix) {
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
        long mod = Long.parseLong(firstLine[1]);

        long[][] matrix = new long[n][n];
        for (int i = 0; i < n; i++) {
            String[] rowLine = br.readLine().trim().split("\\s+");
            for (int j = 0; j < n; j++) {
                matrix[i][j] = Long.parseLong(rowLine[j]);
            }
        }

        Solution sol = new Solution();
        long[] result = sol.minimalPolynomial(n, mod, matrix);

        System.out.println(result.length - 1);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            sb.append(result[i]).append(i == result.length - 1 ? "" : " ");
        }
        System.out.println(sb.toString());
    }
}
```

### Python

```python
import sys

class Solution:
    def minimal_polynomial(self, n, mod, matrix):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    mod = int(input_data[1])

    matrix = []
    idx = 2
    for i in range(n):
        row = [int(val) for val in input_data[idx:idx+n]]
        matrix.append(row)
        idx += n

    sol = Solution()
    result = sol.minimal_polynomial(n, mod, matrix)
    print(len(result) - 1)
    print(*(result))

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
    vector<long long> minimalPolynomial(int n, long long mod, vector<vector<long long>>& matrix) {
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

    vector<vector<long long>> matrix(n, vector<long long>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }

    Solution sol;
    vector<long long> result = sol.minimalPolynomial(n, mod, matrix);

    cout << result.size() - 1 << endl;
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
  minimalPolynomial(n, mod, matrix) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  const n = parseInt(input[0]);
  const mod = BigInt(input[1]);

  const matrix = [];
  let idx = 2;
  for (let i = 0; i < n; i++) {
    const row = [];
    for (let j = 0; j < n; j++) {
      row.push(BigInt(input[idx++]));
    }
    matrix.push(row);
  }

  const sol = new Solution();
  const result = sol.minimalPolynomial(n, mod, matrix);
  console.log(result.length - 1);
  console.log(result.join(" "));
}

solve();
```
