---
problem_id: MTH_MATRIX_EXP_LINEAR_RECURRENCE__6283
display_id: MTH-007
slug: matrix-exp-linear-recurrence
title: "Matrix Exponentiation for Linear Recurrence"
difficulty: Medium
difficulty_score: 58
topics:
  - MathAdvanced
  - Matrix
tags:
  - math-advanced
  - matrix-exponentiation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-007: Matrix Exponentiation for Linear Recurrence

## Problem Statement

Given a linear recurrence relation of order k with coefficients and initial terms, compute the nth term modulo a prime using matrix exponentiation.

![Problem Illustration](../images/MTH-007/problem-illustration.png)

## Input Format

- Line 1: Three integers `k` (recurrence order), `n` (target term), and `MOD` (modulus)
- Line 2: k space-separated integers representing recurrence coefficients c_0 to c_{k-1}
- Line 3: k space-separated integers representing initial terms a_0 to a_{k-1}

## Output Format

A single integer representing the nth term of the sequence modulo MOD.

## Constraints

- `1 <= k <= 50`
- `0 <= n <= 10^18`
- `0 <= c_i, a_i < MOD`
- MOD is prime (typically 10^9 + 7)

## Example

**Input:**
```
2 5 1000000007
1 1
0 1
```

**Output:**
```
5
```

**Explanation:**

Fibonacci sequence: a_n = a_{n-1} + a_{n-2}
Coefficients: [1, 1]
Initial: [0, 1]

Sequence: 0, 1, 1, 2, 3, 5, ...
a_5 = 5

![Example Visualization](../images/MTH-007/example-1.png)

## Notes

- Build k×k transition matrix
- Use fast matrix exponentiation: O(k³ log n)
- Handles very large n efficiently
- Common for Fibonacci-like sequences
- Can solve any linear recurrence

## Related Topics

matrix-exponentiation, linear-recurrence, fast-exponentiation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long matrix_exp_linear_recurrence(int k, long n, long mod, long[] coeffs, long[] initial) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int k = sc.nextInt();
        long n = sc.nextLong();
        long MOD = sc.nextLong();
        
        long[] coeffs = new long[k];
        for (int i = 0; i < k; i++) coeffs[i] = sc.nextLong();
        
        long[] initial = new long[k];
        for (int i = 0; i < k; i++) initial[i] = sc.nextLong();
        
        Solution solution = new Solution();
        System.out.println(solution.matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial));
        
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def matrix_exp_linear_recurrence(self, k: int, n: int, MOD: int, coeffs: list[int], initial: list[int]) -> int:
        # Implementation here
        return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        n = int(next(iterator))
        MOD = int(next(iterator))
        
        coeffs = [int(next(iterator)) for _ in range(k)]
        initial = [int(next(iterator)) for _ in range(k)]
        
        sol = Solution()
        print(sol.matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial))
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
    long matrix_exp_linear_recurrence(int k, long long n, long long mod, vector<long long>& coeffs, vector<long long>& initial) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    long long n, MOD;
    if (!(cin >> k >> n >> MOD)) return 0;

    vector<long long> coeffs(k);
    for (int i = 0; i < k; i++) cin >> coeffs[i];

    vector<long long> initial(k);
    for (int i = 0; i < k; i++) cin >> initial[i];

    Solution solution;
    cout << solution.matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial) {
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
  
  const k = parseInt(data[ptr++]);
  const n = BigInt(data[ptr++]); // Keep as BigInt or string
  const MOD = parseInt(data[ptr++]);
  
  const coeffs = [];
  for(let i=0; i<k; i++) coeffs.push(parseInt(data[ptr++]));
  
  const initial = [];
  for(let i=0; i<k; i++) initial.push(parseInt(data[ptr++]));
  
  const solution = new Solution();
  console.log(solution.matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial));
});
```
