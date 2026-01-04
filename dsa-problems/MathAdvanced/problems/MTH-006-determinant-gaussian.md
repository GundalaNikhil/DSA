---
problem_id: MTH_DETERMINANT_GAUSSIAN__4917
display_id: MTH-006
slug: determinant-gaussian
title: "Determinant via Gaussian Elimination"
difficulty: Medium
difficulty_score: 55
topics:
  - MathAdvanced
  - Determinant
tags:
  - math-advanced
  - determinant
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-006: Determinant via Gaussian Elimination

## Problem Statement

Compute the determinant of an n × n matrix modulo a prime using Gaussian elimination with partial pivoting. Track row swaps to maintain correct sign.

![Problem Illustration](../images/MTH-006/problem-illustration.png)

## Input Format

- Line 1: Two integers `n` (matrix size) and `MOD` (prime modulus)
- Next n lines: n space-separated integers representing each row of the matrix

## Output Format

A single integer representing the determinant modulo MOD.

## Constraints

- `1 <= n <= 1000`
- `0 <= matrix[i][j] < MOD`
- MOD is prime (typically 10^9 + 7)

## Example

**Input:**

```
2 1000000007
1 2
3 4
```

**Output:**

```
1000000005
```

**Explanation:**

Matrix:
[1 2]
[3 4]

Determinant = 1*4 - 2*3 = 4 - 6 = -2

-2 mod 10^9+7 = 10^9+7-2 = 1000000005

![Example Visualization](../images/MTH-006/example-1.png)

## Notes

- Use Gaussian elimination to convert to upper triangular form
- Track number of row swaps (affects sign)
- Use modular inverse for division
- Det = (-1)^swaps × product of diagonal elements
- Time complexity: O(n³)

## Related Topics

determinant, gaussian-elimination, linear-algebra

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long computeDeterminant(int n, long mod, long[][] matrix) {
        // Implement here
        return 0;
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
        System.out.println(sol.computeDeterminant(n, mod, matrix));
    }
}
```

### Python

```python
import sys

class Solution:
    def compute_determinant(self, n, mod, matrix):
        # Implement here
        return 0

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
    print(sol.compute_determinant(n, mod, matrix))

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
    long long computeDeterminant(int n, long long mod, vector<vector<long long>>& matrix) {
        // Implement here
        return 0;
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
    cout << sol.computeDeterminant(n, mod, matrix) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  computeDeterminant(n, mod, matrix) {
    // Implement here
    return 0;
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
  console.log(sol.computeDeterminant(n, mod, matrix).toString());
}

solve();
```
