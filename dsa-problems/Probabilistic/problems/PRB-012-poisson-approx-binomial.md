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

Approximate `P(X = k)` for `X ~ Binomial(n, p)` using the Poisson approximation with `lambda = n * p`:

```
P_approx = e^{-lambda} * lambda^k / k!
```

Also output the Le Cam error bound on total variation:

```
err = min(1, 2 * n * p^2)
```

![Problem Illustration](../images/PRB-012/problem-illustration.png)

## Input Format

- Single line: integer `n`, real `p`, integer `k`

## Output Format

- Two floating-point numbers: `P_approx` and `err`

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
0.180447 0.040000
```

**Explanation:**

lambda = 2. P_approx = e^-2 * 2^3 / 3! = 0.180447.

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
    public double[] poissonApprox(int n, double p, int k) {
        // Your implementation here
        return new double[]{0.0, 0.0};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double p = sc.nextDouble();
        int k = sc.nextInt();

        Solution solution = new Solution();
        double[] res = solution.poissonApprox(n, p, k);
        System.out.printf("%.6f %.6f\n", res[0], res[1]);
        sc.close();
    }
}
```

### Python

```python
import math

def poisson_approx(n: int, p: float, k: int):
    # Your implementation here
    return 0.0, 0.0

def main():
    n, p, k = input().split()
    approx, err = poisson_approx(int(n), float(p), int(k))
    print(f"{approx:.6f} {err:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

class Solution {
public:
    pair<double, double> poissonApprox(int n, double p, int k) {
        // Your implementation here
        return {0.0, 0.0};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    double p;
    cin >> n >> p >> k;
    Solution solution;
    auto res = solution.poissonApprox(n, p, k);
    cout << fixed << setprecision(6) << res.first << " " << res.second << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function poissonApprox(n, p, k) {
  // Your implementation here
  return [0.0, 0.0];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const p = parseFloat(data[1]);
  const k = parseInt(data[2], 10);
  const res = poissonApprox(n, p, k);
  console.log(res[0].toFixed(6) + " " + res[1].toFixed(6));
});
```
