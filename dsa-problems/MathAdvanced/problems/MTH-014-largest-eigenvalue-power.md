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
[2  0]
[0  1]

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

class Solution {
    public double largest_eigenvalue_power(int n, int maxIter, double[][] matrix, double epsilon) {
        //Implement here
        return 0.0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int maxIter = sc.nextInt();
        
        double[][] matrix = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextDouble();
            }
        }
        
        double epsilon = sc.nextDouble();
        
        Solution solution = new Solution();
        double res = solution.largest_eigenvalue_power(n, maxIter, matrix, epsilon);
        
        System.out.printf("%.6f\n", res);
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def largest_eigenvalue_power(self, n: int, maxIter: int, matrix: list[list[float]], epsilon: float) -> float:
        # //Implement here
        return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        maxIter = int(next(iterator))
        
        matrix = []
        for _ in range(n):
            row = [float(next(iterator)) for _ in range(n)]
            matrix.append(row)
            
        epsilon = float(next(iterator))
        
        sol = Solution()
        res = sol.largest_eigenvalue_power(n, maxIter, matrix, epsilon)
        print(f"{res:.6f}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

class Solution {
public:
    double largest_eigenvalue_power(int n, int maxIter, vector<vector<double>>& matrix, double epsilon) {
        //Implement here
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

    Solution solution;
    double res = solution.largest_eigenvalue_power(n, maxIter, matrix, epsilon);

    cout << fixed << setprecision(6) << res << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  largest_eigenvalue_power(n, maxIter, matrix, epsilon) {
    //Implement here
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
  const maxIter = parseInt(data[ptr++]);
  
  const matrix = [];
  for(let i=0; i<n; i++) {
      const row = [];
      for(let j=0; j<n; j++) row.push(parseFloat(data[ptr++]));
      matrix.push(row);
  }
  
  const epsilon = parseFloat(data[ptr++]);
  
  const solution = new Solution();
  const res = solution.largest_eigenvalue_power(n, maxIter, matrix, epsilon);
  
  console.log(res.toFixed(6));
});
```

