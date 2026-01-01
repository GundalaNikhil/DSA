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
---

# PRB-004: Monte Carlo Estimation of Pi

## 📋 Problem Summary

Given the results of a Monte Carlo simulation (N total points, C points inside a quarter circle), calculate:

1. The estimated value of `pi` (`hatpi`).
2. The 95% confidence interval half-width (margin of error) for this estimate.

| | |
|---|---|
| **Input** | N, C |
| **Output** | π̂, error |

## 🌍 Real-World Scenario

**Scenario Title:** The Nuclear Reactor Shielding

You are designing a radiation shield for a nuclear reactor.

- The physics of neutron scattering is too complex to solve analytically.
- Instead, you run a **Monte Carlo simulation**: you simulate millions of individual neutrons, tracking their random paths through the shield material.
- You count how many neutrons penetrate the shield (C) out of the total simulated (N).
- To certify the shield's safety, you need not just the estimated penetration rate, but also the **statistical confidence** (error bars) to ensure the result isn't just due to random chance.

**Why This Problem Matters:**

- **Finance:** Pricing complex derivatives (options) where closed-form formulas don't exist.
- **Physics:** Simulating particle interactions.
- **AI/ML:** Reinforcement learning (estimating value functions via sampling).

![Real-World Application](../images/PRB-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Quarter Circle with Points

Unit Square `[0,1] x [0,1]`. Area = 1.
Quarter Circle radius 1. Area = `pi r^2 / 4 = pi / 4`.

```
(0,1) +─────────────────+ (1,1)
      │ ╱               │
      │╱  Outside       │  ● Points outside circle
      │   Region        │  (x² + y² > 1)
      ├─────╲           │
      │Inside ╲         │  ● Points inside circle
      │ Quarter╲        │  (x² + y² ≤ 1)
      │  Circle ╲       │
      │          ╲      │
(0,0) +───────────╲─────+ (1,0)
                   Arc
```

**Key Relationship:**

```
Probability of landing inside = Area of Quarter Circle / Area of Square
                              = (π/4) / 1
                              = π/4

Therefore: π = 4 × (Count Inside / Total Count)
```

### Convergence Visualization

How the estimate improves with more samples:

```
┌──────────────────────────────────────────────────────────────┐
│ Sample Size │  Estimate  │ Error from π │ Confidence Width │
├─────────────┼────────────┼──────────────┼──────────────────┤
│ N = 100     │  π̂ = 3.20  │   ±0.34      │    ±0.18        │
│ N = 1,000   │  π̂ = 3.15  │   ±0.09      │    ±0.06        │
│ N = 10,000  │  π̂ = 3.142 │   ±0.001     │    ±0.02        │
│ N = 100,000 │  π̂ = 3.1416│   ±0.0001    │    ±0.006       │
└─────────────┴────────────┴──────────────┴──────────────────┘
        Accuracy improves as √N (law of large numbers)
```

**Visual Distribution of Points:**

```
Small Sample (N=20):         Large Sample (N=200):
Lots of variance             Smooth approximation
(0,1) +─────────+ (1,1)     (0,1) +─────────+ (1,1)
      │ ╱ ●   ● │                 │╱●●●●   ●●│
      │╱ ●      │                 │●●●●    ●●│
      │   ●   ● │                 │●●●●●  ●●●│
      │ ●  ●    │                 │●●●●●● ●●●│
      │●    ●   │                 │●●●●●●●●●●│
(0,0) +─────────+ (1,0)     (0,0) +─────────+ (1,0)
   π̂ ≈ 3.0 (rough)              π̂ ≈ 3.14 (better)
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Formula:**
  - `hatpi = 4 x fracCN`.
  - Standard Error of `hatp` is `sqrtfracp(1-p)N`.
  - Since `hatpi = 4hatp`, the error scales by 4.
  - 95% Confidence Interval uses Z-score ≈ 1.96$.
  - Error Half-Width = `1.96 x 4 x sqrtfrachatp(1-hatp)N`.
- **Precision:** Use `double` for all calculations.
- **Constraints:** N \le 10^6$. Calculation is O(1).

### Core Concept: Central Limit Theorem

The count C follows a Binomial distribution `B(N, p)` where p = \pi/4$.
For large N, this approximates a Normal distribution by the Central Limit Theorem.

**Standard Error Calculation:**

The standard deviation of the proportion `hatp` is:
. SE(\hat{p}) = \sqrt{\frac{p(1-p)}{N}}. 

Since `hatpi = 4hatp`, the error scales by 4:
. SE(\hat{\pi}) = 4 \times SE(\hat{p}) = 4\sqrt{\frac{\hat{p}(1-\hat{p})}{N}}. 

**95% Confidence Interval:**

For a 95% confidence level, we use the Z-score of 1.96:
. \text{Margin of Error} = 1.96 \times SE(\hat{\pi}) = 1.96 \times 4\sqrt{\frac{\hat{p}(1-\hat{p})}{N}}. 

**Why This Works:**

- We use the sample proportion `hatp` to estimate the true p (since we don't know π beforehand)
- The error decreases as `1/sqrtN`, so 4× more samples halves the error
- 95% CI means: if we repeat this experiment many times, 95% of our intervals will contain the true value of π

## Naive Approach

### Intuition

Just print `4C/N`.

### Algorithm

Ignore error calculation.

### Time Complexity

- **O(1)**. But incomplete.

## Optimal Approach

### Key Insight

Direct implementation of the statistical formulas provided in the problem statement.

### Algorithm

1. `p_hat = C / N`.
2. `pi_hat = 4 * p_hat`.
3. `std_err_p = sqrt(p_hat * (1 - p_hat) / N)`.
4. `margin_error = 1.96 * std_err_p * 4`.
5. Print `pi_hat` and `margin_error`.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PRB-004/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-004/algorithm-steps.png)

## Implementations

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
        LCG rng = new LCG(seed);
        long countInside = 0;
        
        for (long i = 0; i < N; i++) {
            double x = rng.nextFloat();
            double y = rng.nextFloat();
            if (x * x + y * y <= 1.0) {
                countInside++;
            }
        }
        
        double pHat = (double) countInside / N;
        double piHat = 4.0 * pHat;
        
        double error = 0.0;
        if (N > 0) {
            double stdErrP = Math.sqrt(pHat * (1.0 - pHat) / N);
            error = 1.96 * stdErrP * 4.0;
        }
        
        return new double[]{piHat, error};
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
        self.state = seed & 0xFFFFFFFF

    def next_float(self):
        self.state = (self.state * 1664525 + 1013904223) & 0xFFFFFFFF
        return self.state / 4294967296.0

def monte_carlo_pi(N: int, seed: int):
    rng = LCG(seed)

    count_inside = 0

    for _ in range(N):
        # Generate two random numbers in [0, 1)
        x = rng.next_float()
        y = rng.next_float()

        # Check if point is inside quarter circle
        if x * x + y * y <= 1.0:
            count_inside += 1

    # Calculate pi estimate
    p_hat = count_inside / N
    pi_hat = 4.0 * p_hat

    # Calculate 95% confidence interval half-width
    # Avoid division by zero if p_hat is 0 or 1 (edge case)
    if N > 0:
        std_err_p = math.sqrt(p_hat * (1.0 - p_hat) / N)
        error = 1.96 * std_err_p * 4.0
    else:
        error = 0.0

    return pi_hat, error

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
            state = (state * 1664525 + 1013904223);
            return state / 4294967296.0;
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
  const rng = new LCG(seed);
  let countInside = 0;
  
  for (let i = 0; i < N; i++) {
    const x = rng.nextFloat();
    const y = rng.nextFloat();
    if (x * x + y * y <= 1.0) {
      countInside++;
    }
  }

  const pHat = countInside / N;
  const piHat = 4.0 * pHat;

  let error = 0.0;
  if (N > 0) {
    const stdErrP = Math.sqrt((pHat * (1.0 - pHat)) / N);
    error = 1.96 * stdErrP * 4.0;
  }

  return [piHat, error];
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

## 🧪 Test Case Walkthrough (Dry Run)

Input: `10000 7854`.

1. `p_hat = 0.7854`.
2. `pi_hat = 4 * 0.7854 = 3.1416`.
3. `p(1-p) = 0.7854 * 0.2146 = 0.16854684`.
4. `p(1-p)/N = 0.000016854684`.
5. `sqrt(...) = 0.004105445`.
6. `error = 1.96 * 4 * 0.004105445 = 7.84 * 0.004105445 = 0.0321866`.
   Matches example output.

## ✅ Proof of Correctness

### Invariant

The formulas are standard statistical definitions for binomial proportion confidence intervals (Wald interval).

### Why the approach is correct

Direct application of math.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** How many samples needed for error < 0.001?
  - _Hint:_ Solve for N. N \approx (1.96 \cdot 4 / 0.001)^2 \cdot p(1-p)$.
- **Extension 2:** Variance Reduction.
  - _Hint:_ Stratified sampling or Antithetic variates.
- **Extension 3:** Higher dimensions (Volume of hypersphere).
  - _Hint:_ Rejection sampling efficiency drops exponentially with dimension.

### Common Mistakes to Avoid

1. **Integer Division**
   - ❌ Wrong: `C / N` in Java/C++ (returns 0).
   - ✅ Correct: `(double) C / N`.
2. **Scaling Error**
   - ❌ Wrong: Forgetting to multiply error by 4.
   - ✅ Correct: `Var(4X) = 16Var(X)`, so `StdDev(4X) = 4StdDev(X)`.

## Related Concepts

- **Law of Large Numbers:** Convergence to true mean.
- **Central Limit Theorem:** Distribution of sample mean.
