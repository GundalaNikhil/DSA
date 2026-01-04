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
- P_approx = e^-2 \* 2^3 / 3! = 0.180447044
- P_binomial = C(200,3) _ 0.01^3 _ 0.99^197 = 0.181355340
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
    public void compareDistributions(int n, double p, int k) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        double p = sc.nextDouble();
        int k = sc.nextInt();
        Solution sol = new Solution();
        sol.compareDistributions(n, p, k);
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def compare_distributions(self, n, p, k):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    p = float(input_data[1])
    k = int(input_data[2])
    sol = Solution()
    sol.compare_distributions(n, p, k)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

class Solution {
public:
    void compareDistributions(int n, double p, int k) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    double p;
    if (!(cin >> n >> p >> k)) return 0;
    Solution sol;
    sol.compareDistributions(n, p, k);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  compareDistributions(n, p, k) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;
  const n = parseInt(input[0]);
  const p = parseFloat(input[1]);
  const k = parseInt(input[2]);
  const sol = new Solution();
  sol.compareDistributions(n, p, k);
}

solve();
```
