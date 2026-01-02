---
problem_id: PRB_MONTE_CARLO_PI__2365
display_id: PRB-004
slug: monte-carlo-pi
title: "Monte Carlo Estimation of Pi"
difficulty: Easy
difficulty_score: 30
topics:
  - Probability
  - Statistics
  - Monte Carlo
tags:
  - probability
  - monte-carlo
  - statistics
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-004: Monte Carlo Estimation of Pi

## Problem Statement

You sampled `N` random points in the unit square and counted how many fell inside the quarter circle of radius 1. Given `N` and `C` (count inside), compute:

- The estimate of π: `pi_hat = 4 * C / N`
- A 95% confidence half-width: `err = 1.96 * sqrt(p*(1-p)/N) * 4` where `p = C/N`

![Problem Illustration](../images/PRB-004/problem-illustration.png)

## Input Format

- Single line: integers `N` and `C`

## Output Format

- Two floating-point numbers: `pi_hat` and `err`

## Constraints

- `1 <= N <= 10^6`
- `0 <= C <= N`

## Example

**Input:**

```
10000 7854
```

**Output:**

```
3.141600 0.032187
```

**Explanation:**

p = 0.7854, pi_hat = 3.1416. The error half-width is about 0.032187.

![Example Visualization](../images/PRB-004/example-1.png)

## Notes

- Print values with at least 6 decimal digits
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Monte Carlo, Confidence Intervals, Estimation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class LCG {
        long state;
        LCG(long seed) {
            this.state = seed & 0xFFFFFFFFL;
        }
        double nextFloat() {
            state = (state * 1664525 + 1013904223) & 0xFFFFFFFFL;
            return state / 4294967296.0;
        }
    }

    public double[] estimatePi(long N, long seed) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long N = sc.nextLong();
            long C = sc.nextLong();

            Solution solution = new Solution();
            double[] res = solution.estimatePi(N, C);
            System.out.printf("%.6f %.6f\n", res[0], res[1]);
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class LCG:
    def __init__(self, seed):
        return 0
    def next_float(self):
        return 0
def monte_carlo_pi(N: int, seed: int):
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    N = int(data[0])
    seed = int(data[1])
    pi_hat, err = monte_carlo_pi(N, seed)
    print(f"{pi_hat:.6f} {err:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    class LCG {
        unsigned int state;
    public:
        LCG(unsigned int seed) : state(seed) {}
        double nextFloat() {
        return 0;
    }
    };

    pair<double, double> estimatePi(long long N, long long seed) {
        LCG rng(seed);
        long long count_inside = 0;
        
        for (long long i = 0; i < N; i++) {
            double x = rng.nextFloat();
            double y = rng.nextFloat();
            if (x * x + y * y <= 1.0) {
                count_inside++;
            }
        }
        
        double pHat = (double)count_inside / N;
        double piHat = 4.0 * pHat;
        
        double error = 0.0;
        if (N > 0) {
            double stdErrP = sqrt(pHat * (1.0 - pHat) / N);
            error = 1.96 * stdErrP * 4.0;
        }
        return {piHat, error};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, C;
    if (cin >> N >> C) {
        Solution solution;
        auto res = solution.estimatePi(N, C);
        cout << fixed << setprecision(6) << res.first << " " << res.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class LCG {
  constructor(seed) {
    this.state = BigInt(seed) & 0xFFFFFFFFn;
  }
  nextFloat() {
    this.state = (this.state * 1664525n + 1013904223n) & 0xFFFFFFFFn;
    return Number(this.state) / 4294967296.0;
  }
}

function estimatePi(N, seed) {
    return 0;
  }

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const N = parseInt(data[0], 10);
  const C = parseInt(data[1], 10);
  const res = estimatePi(N, C);
  console.log(res[0].toFixed(6) + " " + res[1].toFixed(6));
});
```

