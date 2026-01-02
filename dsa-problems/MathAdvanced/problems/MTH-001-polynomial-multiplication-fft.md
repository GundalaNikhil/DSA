---
problem_id: MTH_POLYNOMIAL_MULTIPLICATION_FFT__2847
display_id: MTH-001
slug: polynomial-multiplication-fft
title: "Polynomial Multiplication via FFT"
difficulty: Medium
difficulty_score: 55
topics:
  - MathAdvanced
  - FFT
  - Polynomial
tags:
  - math-advanced
  - fft
  - polynomial-multiplication
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# MTH-001: Polynomial Multiplication via FFT

## Problem Statement

Given two polynomials A(x) and B(x) represented as arrays of their coefficients, compute their product polynomial C(x) = A(x) × B(x) using the Fast Fourier Transform (FFT) algorithm. Return the coefficients of the resulting polynomial modulo 1,000,000,007.

A polynomial is represented as an array where the index represents the power of x. For example, [1, 2, 3] represents the polynomial 1 + 2x + 3x².

![Problem Illustration](../images/MTH-001/problem-illustration.png)

## Input Format

- Line 1: An integer `n` representing the degree of polynomial A(x) plus one (number of coefficients)
- Line 2: `n` space-separated integers representing coefficients of A(x) from lowest to highest degree
- Line 3: An integer `m` representing the degree of polynomial B(x) plus one (number of coefficients)
- Line 4: `m` space-separated integers representing coefficients of B(x) from lowest to highest degree

## Output Format

A single line containing space-separated integers representing the coefficients of the product polynomial C(x) modulo 1,000,000,007, from lowest to highest degree.

## Constraints

- `1 <= n, m <= 100000`
- `0 <= A[i], B[i] <= 1000000006`
- The degree of the resulting polynomial will be at most `n + m - 2`
- All coefficients must be output modulo `10^9 + 7`

## Example

**Input:**

```
2
1 2
2
3 4
```

**Output:**

```
3 10 8
```

**Explanation:**

A(x) = 1 + 2x
B(x) = 3 + 4x

C(x) = A(x) × B(x) = (1 + 2x)(3 + 4x)
= 1×3 + 1×4x + 2x×3 + 2x×4x
= 3 + 4x + 6x + 8x²
= 3 + 10x + 8x²

Therefore, the coefficients are [3, 10, 8].

![Example Visualization](../images/MTH-001/example-1.png)

## Notes

- FFT allows polynomial multiplication in O((n+m) log(n+m)) time instead of O(nm) with naive approach
- You may need to pad the input polynomials to the next power of 2 for FFT implementation
- Handle modular arithmetic carefully to avoid overflow
- The result polynomial has degree (n-1) + (m-1) = n + m - 2
- Consider using Complex numbers for FFT or Number Theoretic Transform (NTT) for modular arithmetic

## Related Topics

Fast Fourier Transform, Number Theoretic Transform, Polynomial Algorithms, Divide and Conquer

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] multiplyPolynomials(long[] A, long[] B) {
        // Implementation here
        return new long[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] A = new long[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextLong();
        
        int m = sc.nextInt();
        long[] B = new long[m];
        for (int i = 0; i < m; i++) B[i] = sc.nextLong();
        
        Solution solution = new Solution();
        long[] result = solution.multiplyPolynomials(A, B);
        
        for (int i = 0; i < result.length; i++) {
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
import math

class Solution:
    def multiply_polynomials(self, A: list[int], B: list[int]) -> list[int]:
        # Implementation here
        return []

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        A = [int(next(iterator)) for _ in range(n)]
        m = int(next(iterator))
        B = [int(next(iterator)) for _ in range(m)]
        
        sol = Solution()
        res = sol.multiply_polynomials(A, B)
        print(*(res))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<long long> multiplyPolynomials(vector<long long>& A, vector<long long>& B) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    int m;
    cin >> m;
    vector<long long> B(m);
    for (int i = 0; i < m; i++) cin >> B[i];

    Solution solution;
    vector<long long> result = solution.multiplyPolynomials(A, B);

    for (int i = 0; i < result.size(); i++) {
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
  multiplyPolynomials(A, B) {
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
  const A = [];
  for(let i=0; i<n; i++) A.push(parseInt(data[ptr++]));
  
  const m = parseInt(data[ptr++]);
  const B = [];
  for(let i=0; i<m; i++) B.push(parseInt(data[ptr++]));

  const solution = new Solution();
  const result = solution.multiplyPolynomials(A, B);
  console.log(result.join(" "));
});
```
