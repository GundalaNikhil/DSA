---
problem_id: PRB_POISSON_APPROX_BINOMIAL__6602
display_id: PRB-012
slug: poisson-approx-binomial
title: "Poisson Approximation of Binomial"
difficulty: Medium
difficulty_score: 52
topics:
  - Probability
  - Poisson Approximation
  - Error Bounds
tags:
  - probability
  - poisson
  - approximation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-012: Poisson Approximation of Binomial

## Problem Statement

Compute the Poisson approximation to a binomial probability. For `X ~ Binomial(n, p)` and a specific value `k`, compute:

1. **Exact Binomial Probability**: `P_binomial = C(n,k) * p^k * (1-p)^(n-k)`
2. **Poisson Approximation**: `P_approx = e^{-lambda} * lambda^k / k!`, where `lambda = n * p`
3. **Error**: The absolute difference between the two probabilities

![Problem Illustration](../images/PRB-012/problem-illustration.png)

## Input Format

- Single line: integer `n`, real `p`, integer `k`

## Output Format

- Three floating-point numbers: `P_approx`, `P_binomial`, `error`
- Where `error = |P_binomial - P_approx|`

## Constraints

- `1 <= n <= 10^6`
- `0 < p <= 0.01`
- `0 <= k <= n`

## Example

**Input:**

```
200 0.01 3
```

**Output:**

```
0.180447 0.181355 0.000908
```

**Explanation:**

- lambda = 2
- P_approx = e^-2 * 2^3 / 3! = 0.180447044
- P_binomial = C(200,3) * 0.01^3 * 0.99^197 = 0.181355340
- error = |0.181355340 - 0.180447044| = 0.000908296

![Example Visualization](../images/PRB-012/example-1.png)

## Notes

- Use double precision for factorials (or log-factorials)
- Accept answers with absolute error <= 1e-6
- Time complexity: O(k)

## Related Topics

Poisson Approximation, Binomial Distribution

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class Result {
        double binomial;
        double approx;
        double error;
        Result(double b, double a, double e) { binomial = b; approx = a; error = e; }
    }

    private double logFactorial(int n) {
        return 0;
    }

    public Result solve(int n, double p, int k) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            int n = (int) sc.nextLong();
            double p = sc.nextDouble();
            int k = (int) sc.nextLong();

            Solution solution = new Solution();
            Solution.Result res = solution.solve(n, p, k);
            
            // Output order: Approx Exact Error
            System.out.printf("%.9f %.9f %.9f\n", res.approx, res.binomial, res.error);
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import math

def poisson_approx(n: int, p: float, k: int):
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    p = float(data[1])
    k = int(data[2])
    binomial, approx, error = poisson_approx(n, p, k)
    print(f"{approx:.9f} {binomial:.9f} {error:.9f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    struct Result {
        double binomial;
        double approx;
        double error;
    };

    Result solve(int n, double p, int k) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    double p;
    if (cin >> n >> p >> k) {
        Solution solution;
        auto res = solution.solve(n, p, k);
        // Output order: Approx Exact Error (matching Python print f"{approx} {binomial} {error}")
        cout << fixed << setprecision(9) 
             << res.approx << " " 
             << res.binomial << " " 
             << res.error << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function logFactorial(n) {
    return 0;
  }

function solve(n, p, k) {
    return 0;
  }

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part !== "") data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const p = parseFloat(data[1]);
  const k = parseInt(data[2], 10);
  const res = solve(n, p, k);
  // Output order: Approx Exact Error
  console.log(res.approx.toFixed(9) + " " + res.binomial.toFixed(9) + " " + res.error.toFixed(9));
});
```

