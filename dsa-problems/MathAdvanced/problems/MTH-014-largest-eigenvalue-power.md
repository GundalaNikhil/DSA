---
problem_id: MTH_LARGEST_EIGENVALUE_POWER__2197
display_id: MTH-014
slug: largest-eigenvalue-power
title: "Largest Eigenvalue Power Method"
difficulty: Medium
difficulty_score: 58
topics:
  - MathAdvanced
  - Largest
tags:
  - math-advanced
  - eigenvalue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-014: Largest Eigenvalue Power Method

## Problem Statement

Approximate the largest eigenvalue (by absolute value) of a real matrix using the power iteration method. Continue until convergence within a specified tolerance.

![Problem Illustration](../images/MTH-014/problem-illustration.png)

## Input Format

- Line 1: Two integers `n` (matrix size) and `maxIter` (maximum iterations)
- Next n lines: n space-separated real numbers representing each row of the matrix
- Last line: A real number `epsilon` (convergence tolerance)

## Output Format

A single real number representing the approximate largest eigenvalue (6 decimal places).

## Constraints

- `1 <= n <= 500`
- `1 <= maxIter <= 10000`
- `10^-10 <= epsilon <= 10^-3`
- Matrix entries in range [-1000, 1000]

## Example

**Input:**

```
2 1000
2.0 0.0
0.0 1.0
0.000001
```

**Output:**

```
2.000000
```

**Explanation:**

Matrix:
[2 0]
[0 1]

Eigenvalues: 2 and 1
Largest eigenvalue: 2

Power method converges to 2.000000

![Example Visualization](../images/MTH-014/example-1.png)

## Notes

- Power method: v_{k+1} = A × v_k / ||A × v_k||
- Eigenvalue λ ≈ v^T × A × v
- Converges to largest eigenvalue by magnitude
- Convergence rate depends on eigenvalue gap
- May not converge if multiple eigenvalues have same magnitude

## Related Topics

eigenvalue, power-method, iterative-algorithm

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public double findLargestEigenvalue(int n, int maxIter, double epsilon, double[][] matrix) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        int maxIter = sc.nextInt();

        double[][] matrix = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextDouble();
            }
        }
        double epsilon = sc.nextDouble();

        Solution sol = new Solution();
        System.out.printf("%.6f\n", sol.findLargestEigenvalue(n, maxIter, epsilon, matrix));
    }
}
```

### Python

```python
import sys

class Solution:
    def find_largest_eigenvalue(self, n, max_iter, epsilon, matrix):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    max_iter = int(input_data[1])

    matrix = []
    idx = 2
    for i in range(n):
        row = [float(val) for val in input_data[idx:idx+n]]
        matrix.append(row)
        idx += n

    epsilon = float(input_data[idx])

    sol = Solution()
    print("{:.6f}".format(sol.find_largest_eigenvalue(n, max_iter, epsilon, matrix)))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

class Solution {
public:
    double findLargestEigenvalue(int n, int maxIter, double epsilon, const vector<vector<double>>& matrix) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, maxIter;
    if (!(cin >> n >> maxIter)) return 0;

    vector<vector<double>> matrix(n, vector<double>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }
    double epsilon;
    cin >> epsilon;

    Solution sol;
    cout << fixed << setprecision(6) << sol.findLargestEigenvalue(n, maxIter, epsilon, matrix) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findLargestEigenvalue(n, maxIter, epsilon, matrix) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  const n = parseInt(input[0]);
  const maxIter = parseInt(input[1]);

  const matrix = [];
  let idx = 2;
  for (let i = 0; i < n; i++) {
    const row = [];
    for (let j = 0; j < n; j++) {
      row.push(parseFloat(input[idx++]));
    }
    matrix.push(row);
  }
  const epsilon = parseFloat(input[idx++]);

  const sol = new Solution();
  process.stdout.write(
    sol.findLargestEigenvalue(n, maxIter, epsilon, matrix).toFixed(6) + "\n"
  );
}

solve();
```
