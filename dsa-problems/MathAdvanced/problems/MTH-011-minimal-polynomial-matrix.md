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
[1  1]
[0  1]

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

class Solution {
    private long MOD;

    private long power(long base, long exp) {
        return 0;
    }

    private long modInverse(long n) {
        return 0;
    }

    private ArrayList<Long> berlekampMassey(List<Long> s) {
        return null;
    }

    public long[] minimal_polynomial_matrix(int n, long mod, long[][] matrix) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        long MOD = sc.nextLong();
        
        long[][] matrix = new long[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextLong();
            }
        }
        
        Solution solution = new Solution();
        long[] result = solution.minimal_polynomial_matrix(n, MOD, matrix);
        
        System.out.println(result[0]);
        for (int i = 1; i < result.length; i++) {
            System.out.print(result[i] + (i < result.length - 1 ? " " : ""));
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
import sys
import random

class Solution:
    def minimal_polynomial_matrix(self, n: int, MOD: int, matrix: list[list[int]]) -> list[int]:
        return []
def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        MOD = int(next(iterator))
        
        matrix = []
        for _ in range(n):
            row = [int(next(iterator)) for _ in range(n)]
            matrix.append(row)
            
        sol = Solution()
        res = sol.minimal_polynomial_matrix(n, MOD, matrix)
        
        print(res[0])
        print(*(res[1:]))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <random>
using namespace std;

class Solution {
    long long MOD;

    long long power(long long base, long long exp) {
        return 0;
    }

    long long modInverse(long long n) {
        return 0;
    }

    vector<long long> berlekampMassey(const vector<long long>& s) {
        return {};
    }

public:
    vector<long long> minimal_polynomial_matrix(int n, long long mod, vector<vector<long long>>& matrix) {
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long MOD;
    if (!(cin >> n >> MOD)) return 0;

    vector<vector<long long>> matrix(n, vector<long long>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }

    Solution solution;
    vector<long long> result = solution.minimal_polynomial_matrix(n, MOD, matrix);

    cout << result[0] << "\n";
    for (int i = 1; i < result.size(); i++) {
        cout << result[i] << (i < result.size() - 1 ? " " : "");
    }
    cout << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minimal_polynomial_matrix(n, MOD, matrix) {
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
  const MOD = parseInt(data[ptr++]);
  
  const matrix = [];
  for(let i=0; i<n; i++) {
      const row = [];
      for(let j=0; j<n; j++) row.push(parseInt(data[ptr++]));
      matrix.push(row);
  }
  
  const solution = new Solution();
  const result = solution.minimal_polynomial_matrix(n, MOD, matrix);
  
  console.log(result[0]);
  console.log(result.slice(1).join(" "));
});
```

