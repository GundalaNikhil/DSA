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
---

# PRB-012: Poisson Approximation of Binomial

## 📋 Problem Summary

Approximate the probability of observing exactly k successes in n trials, where each trial succeeds with small probability p, using the Poisson distribution.

| | |
|---|---|
| **Binomial parameters** | n, p |
| **Poisson parameter** | `lambda = np` |
| **Approximation** | `P(X=k) ~= frace^-lambda lambda^kk!` |
| **Error Bound (Le Cam's Theorem)** | Total Variation Distance `<= 2np^2` |
| **Input** | n, p, k |
| **Output** | Approx probability, Error bound |

## 🌍 Real-World Scenario

**Scenario Title:** The Call Center Overload

You manage a call center that receives 10,000 calls per hour (n = 10000$).
- The probability of any specific call being a "Critical Emergency" is very low, say 0.05% (p = 0.0005$).
- You want to staff enough specialists to handle these critical calls.
- Calculating the exact Binomial probability for every possible number of critical calls involves huge factorials (10000!).
- Instead, you use the **Poisson Approximation** to quickly estimate the probability of getting exactly k emergencies (e.g., 5, 10, or 20) to set staffing levels.
- You also need to know the **error bound** to be sure your approximation is safe enough for critical planning.

**Why This Problem Matters:**

- **Insurance:** Modeling rare catastrophic events (earthquakes, floods).
- **Manufacturing:** Defect rates in high-volume production.
- **Web Operations:** Server error rates (500s) in massive traffic streams.

![Real-World Application](../images/PRB-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Binomial vs Poisson

n = 10, p=0.1 \implies \lambda=1$.

```
k   Binomial(10, 0.1)    Poisson(1)
0   0.3487               0.3679
1   0.3874               0.3679
2   0.1937               0.1839
3   0.0574               0.0613
...
```

- As n \to \infty$ and p → 0 with np = λ, Binomial converges to Poisson.
- The approximation is computationally much cheaper (no large factorials of n).
- Le Cam's theorem gives a tight bound on the error.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Formulas:**
  - `lambda = n * p`.
  - `P_approx = e^-lambda * fraclambda^kk!`.
  - `Error = min(1.0, 2 * n * p^2)`. (Or just `2np^2` if small).
- **Precision:**
  - `k!` can overflow 64-bit integers for k > 20$.
  - Use `double` for intermediate calculations or compute terms iteratively:
    `term = 1; for i in 1..k: term *= lambda / i`.
  - Alternatively, use log-prob: `ln P = -lambda + k ln lambda - ln(k!)`. Then `exp`.
- **Constraints:** n \le 10^6`, p <= 0.01`. k can be up to n, but probability is negligible for large k.
  - If k is large (e.g., 1000), direct power/factorial overflows.
  - Use Log-Gamma function or iterative multiplication.
  - However, given p \le 0.01`and n <= 10^6`, `lambda` can be `10^4`.
  - If `lambda` is large, `P(X=k)` is tiny unless k \approx \lambda$.
  - For the purpose of this problem, standard double precision with iterative multiplication or log-math is sufficient.

### Core Concept: Law of Rare Events

When events are independent and rare, their count follows a Poisson distribution.
The "memoryless" property of the underlying exponential inter-arrival times leads to this distribution.

## Naive Approach

### Intuition

Compute `lambda^k` and `k!` directly.

### Algorithm

`pow(lambda, k) / factorial(k) * exp(-lambda)`.

### Time Complexity

- **O(k)**.
- **Risk:** Overflow for k > 20$.

## Optimal Approach

### Key Insight

Use Logarithms to avoid overflow/underflow during intermediate steps.
`ln P = -lambda + k ln lambda - sum_i=1^k ln i`.
Then P = e^{\ln P}$.

### Algorithm

1. Calculate `lambda = n * p`.
2. Calculate `log_P = -lambda + k * log(lambda)`.
3. Subtract `lgamma(k+1)` or sum of logs for factorial.
4. `P_approx = exp(log_P)`.
5. `err = min(1.0, 2.0 * n * p * p)`.
6. Print results.

### Time Complexity

- **O(k)** or **O(1)** with `lgamma`.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PRB-012/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-012/algorithm-steps.png)

## Implementations

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
        double res = 0.0;
        for (int i = 1; i <= n; i++) res += Math.log(i);
        return res;
    }

    public Result solve(int n, double p, int k) {
        double lambda = n * p;

        // 1. Exact Binomial
        double binomialProb = 0.0;
        if (k <= n) {
            double logBinom = logFactorial(n) - logFactorial(k) - logFactorial(n - k);
            
            if (p > 0) logBinom += k * Math.log(p);
            else if (k > 0) logBinom = Double.NEGATIVE_INFINITY;

            if (p < 1) logBinom += (n - k) * Math.log(1.0 - p);
            else if (n - k > 0) logBinom = Double.NEGATIVE_INFINITY;

            if (logBinom > -1e14) binomialProb = Math.exp(logBinom);
        }

        // 2. Poisson Approx
        double approxProb = 0.0;
        if (lambda == 0) {
            approxProb = (k == 0) ? 1.0 : 0.0;
        } else {
            double logP = -lambda + k * Math.log(lambda) - logFactorial(k);
            if (logP > -1e14) approxProb = Math.exp(logP);
        }

        double error = Math.abs(binomialProb - approxProb);
        return new Result(binomialProb, approxProb, error);
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
    lam = n * p

    # Compute exact binomial probability: C(n,k) * p^k * (1-p)^(n-k)
    # Use log space for stability
    if k > n:
        binomial_prob = 0.0
    else:
        try:
            log_binom = math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            log_binom += k * math.log(p) if p > 0 else (0 if k == 0 else float('-inf'))
            log_binom += (n - k) * math.log(1 - p) if p < 1 else (0 if k == n else float('-inf'))
            binomial_prob = math.exp(log_binom) if log_binom != float('-inf') else 0.0
        except (ValueError, OverflowError):
            binomial_prob = 0.0

    # Compute Poisson approximation: e^{-lambda} * lambda^k / k!
    if lam == 0:
        p_approx = 1.0 if k == 0 else 0.0
    else:
        try:
            log_p = -lam + k * math.log(lam) - math.lgamma(k + 1)
            p_approx = math.exp(log_p)
        except ValueError:
            p_approx = 0.0

    error = abs(binomial_prob - p_approx)

    return binomial_prob, p_approx, error

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
        double lambda = n * p;

        // 1. Exact Binomial: C(n, k) * p^k * (1-p)^(n-k)
        double binomialProb = 0.0;
        if (k <= n) {
            double logBinom = lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1);
            if (p > 0) logBinom += k * log(p);
            else if (k > 0) logBinom = -1e18; // -inf effectively

            if (p < 1) logBinom += (n - k) * log(1.0 - p);
            else if (n - k > 0) logBinom = -1e18;

            if (logBinom > -1e14) binomialProb = exp(logBinom);
            else binomialProb = 0.0;
        }

        // 2. Poisson Approx: e^-lambda * lambda^k / k!
        double approxProb = 0.0;
        if (lambda == 0) {
            approxProb = (k == 0) ? 1.0 : 0.0;
        } else {
            double logP = -lambda + k * log(lambda) - lgamma(k + 1);
            if (logP > -1e14) approxProb = exp(logP);
            else approxProb = 0.0;
        }

        double error = abs(binomialProb - approxProb);
        return {binomialProb, approxProb, error};
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
  let res = 0.0;
  for (let i = 1; i <= n; i++) res += Math.log(i);
  return res;
}

function solve(n, p, k) {
  const lambda = n * p;

  // 1. Exact Binomial
  let binomialProb = 0.0;
  if (k <= n) {
    let logBinom = logFactorial(n) - logFactorial(k) - logFactorial(n - k);
    
    if (p > 0) logBinom += k * Math.log(p);
    else if (k > 0) logBinom = -Infinity;

    if (p < 1) logBinom += (n - k) * Math.log(1.0 - p);
    else if (n - k > 0) logBinom = -Infinity;

    if (logBinom > -1e14) binomialProb = Math.exp(logBinom);
  }

  // 2. Poisson Approx
  let approxProb = 0.0;
  if (lambda === 0) {
    approxProb = (k === 0) ? 1.0 : 0.0;
  } else {
    let logP = -lambda + k * Math.log(lambda) - logFactorial(k);
    if (logP > -1e14) approxProb = Math.exp(logP);
  }

  const error = Math.abs(binomialProb - approxProb);
  return { binomial: binomialProb, approx: approxProb, error };
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

## 🧪 Test Case Walkthrough (Dry Run)

Input: `200 0.01 3`.
1. `lambda = 200 x 0.01 = 2`.
2. `ln P = -2 + 3 ln 2 - ln 6`.
   - `-2 + 3(0.6931) - 1.7917`.
   - `-2 + 2.0794 - 1.7917 = -1.7123`.
3. P = e^{-1.7123} \approx 0.180447$.
4. `Error = 2 x 200 x (0.01)^2 = 400 x 0.0001 = 0.04`.
Matches example.

## ✅ Proof of Correctness

### Invariant
The formula is the standard definition of the Poisson PMF.

### Why the approach is correct
Log-space arithmetic prevents overflow for intermediate terms like `k!` or `lambda^k`.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Normal Approximation.
  - *Hint:* Use Gaussian when `lambda` is large (`lambda > 20`).
- **Extension 2:** Chen-Stein Method.
  - *Hint:* Generalizes Poisson approximation to dependent events.
- **Extension 3:** Confidence Intervals.
  - *Hint:* Exact Poisson intervals vs Normal approximation.

### Common Mistakes to Avoid

1. **Overflow**
   - ❌ Wrong: `pow(lambda, k)` for large k.
   - ✅ Correct: Use `log` and `exp`.
2. **Precision**
   - ❌ Wrong: `float` (32-bit).
   - ✅ Correct: `double` (64-bit).

## Related Concepts

- **Exponential Distribution:** Time between Poisson events.
- **Binomial Distribution:** Exact distribution for independent trials.
