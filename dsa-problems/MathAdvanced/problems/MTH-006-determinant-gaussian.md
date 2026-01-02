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
[1  2]
[3  4]

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

class Solution {
    private long MOD;

    private long power(long base, long exp) {
        return 0;
    }

    private long modInverse(long n) {
        return 0;
    }

    public long determinant_gaussian(int n, long mod, long[][] matrix) {
        return 0;
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
        System.out.println(solution.determinant_gaussian(n, MOD, matrix));
        
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def determinant_gaussian(self, n: int, MOD: int, matrix: list[list[int]]) -> int:
        return 0
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
        print(sol.determinant_gaussian(n, MOD, matrix))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
    long long MOD;

    long long power(long long base, long long exp) {
        return 0;
    }

    long long modInverse(long long n) {
        return 0;
    }

public:
    long long determinant_gaussian(int n, long long mod, vector<vector<long long>>& matrix) {
        return 0;
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
    cout << solution.determinant_gaussian(n, MOD, matrix) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  determinant_gaussian(n, MOD, matrix) {
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
  console.log(solution.determinant_gaussian(n, MOD, matrix));
});
```

