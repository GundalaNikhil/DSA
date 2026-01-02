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
- Line 2: n space-separated integers representing distinct values x_0, x_1, ..., x_{n-1}

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
V = [1  1]
    [1  2]

V^(-1) = [ 2  -1]
         [-1   1]

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

class Solution {
    public long[][] invert_vandermonde(int n, long mod, long[] x) {
        // Implementation here
        return new long[0][0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        long MOD = sc.nextLong();
        
        long[] x = new long[n];
        for (int i = 0; i < n; i++) x[i] = sc.nextLong();
        
        Solution solution = new Solution();
        long[][] res = solution.invert_vandermonde(n, MOD, x);
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(res[i][j] + (j < n - 1 ? " " : ""));
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def invert_vandermonde(self, n: int, MOD: int, x: list[int]) -> list[list[int]]:
        # Implementation here
        return []

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        MOD = int(next(iterator))
        x = [int(next(iterator)) for _ in range(n)]
        
        sol = Solution()
        res = sol.invert_vandermonde(n, MOD, x)
        
        for row in res:
            print(*(row))
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
public:
    long long power(long long base, long long exp) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long MOD;
    if (!(cin >> n >> MOD)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; i++) cin >> x[i];

    Solution solution;
    vector<vector<long long>> res = solution.invert_vandermonde(n, MOD, x);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << res[i][j] << (j < n - 1 ? " " : "");
        }
        cout << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  invert_vandermonde(n, MOD, x) {
    // Implementation here
    return null;
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
  
  const x = [];
  for(let i=0; i<n; i++) x.push(parseInt(data[ptr++]));
  
  const solution = new Solution();
  const res = solution.invert_vandermonde(n, MOD, x);
  
  for (let i = 0; i < n; i++) {
    console.log(res[i].join(" "));
  }
});
```
