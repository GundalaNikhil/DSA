---
problem_id: PRB_MEDIAN_UNIFORMS_CLT__3524
display_id: PRB-015
slug: median-uniforms-clt
title: "Median of Uniforms CLT"
difficulty: Medium
difficulty_score: 50
topics:
  - Probability
  - Statistics
  - CLT
tags:
  - probability
  - clt
  - median
  - medium
premium: true
subscription_tier: basic
---

# PRB-015: Median of Uniforms CLT

## 📋 Problem Summary

Given n independent random variables uniformly distributed on $[0,1]$, we want to find the approximate mean and variance of their sample median using the Central Limit Theorem (CLT) for quantiles.

## 🌍 Real-World Scenario

**Scenario Title:** Salary Estimation

Imagine you want to estimate the typical salary in a large city.
- You survey n people at random.
- Salaries often have massive outliers (billionaires), so the **mean** (average) is skewed.
- The **median** (middle value) is a much better representation of the "typical" person.
- If you repeat this survey many times, your calculated median will vary slightly.
- This problem asks: "How much will my median estimate fluctuate?" knowing the variance helps you understand the reliability of your survey.

**Why This Problem Matters:**

- **Robust Statistics:** Median is robust to outliers, unlike the mean.
- **Polling:** Understanding margin of error for median-based statistics.
- **Performance Testing:** Measuring "p50" latency of a server.

![Real-World Application](../images/PRB-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Distribution of the Median

For a Uniform distribution on $[0,1]$:
- The individual values are flat across 0 to 1.
- But the **median** of n samples tends to cluster around 0.5.
- As n grows, this cluster becomes a tight Bell Curve (Normal Distribution).

```
      Frequency
         ^
         |      _--_
         |    /      \    <-- Distribution of the Median
         |   |        |
         |  /          \
    -----|-+------------+-----
         0    0.5     1.0
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Integer n (sample size).
- **Output:** Two floats: Mean and Variance.
- **Approximation:** We are using the asymptotic approximation, which becomes very accurate as n increases.
- **Formula:**
  - Mean $\mu \approx 0.5$
  - Variance $\sigma^2 \approx \frac{1}{4n}$

## Naive Approach

### Intuition

Run a Monte Carlo simulation. Generate n random numbers, find the median, repeat 1,000,000 times, and compute statistics.

### Algorithm

1. Loop K times:
   - Generate array of n randoms.
   - Sort and find median.
   - Store in list.
2. Compute average of list.
3. Compute variance of list.

### Time Complexity

- **O(K \cdot n \log n)**. Very slow for high precision.

### Space Complexity

- **O(n)**.

### Limitations

- Probabilistic, not exact.
- Computationally expensive.

## Optimal Approach

### Key Insight

The Central Limit Theorem for Sample Quantiles states that for a distribution with PDF $f(x)$, the sample median $\hat{m}$ of n observations is approximately normally distributed:

.  \hat{m} \sim N\left(m, \frac{1}{4n [f(m)]^2}\right) . 

Where:
- m is the true population median.
- $f(m)$ is the probability density function evaluated at the median.

For Uniform $[0,1]$:
- True median m = 0.5$.
- PDF $f(x) = 1$ for $0 \le x \le 1$.
- So $f(m) = f(0.5) = 1$.

Plugging these in:
- Mean ≈ 0.5$.
- Variance ≈ \frac{1}{4n(1)^2} = \frac{1}{4n}$.

### Algorithm

1. Read n.
2. Mean = 0.5.
3. Variance = $1.0 / (4 * n)$.
4. Print results.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

### Why This Is Optimal

It's a direct formula application derived from statistical theory.

![Algorithm Visualization](../images/PRB-015/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-015/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public double[] medianClt(int n) {
        double mean = 0.5;
        double variance = 1.0 / (4.0 * n);
        return new double[]{mean, variance};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();

            Solution solution = new Solution();
            double[] res = solution.medianClt(n);
            System.out.printf("%.6f %.6f\n", res[0], res[1]);
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def median_clt(n: int):
    mean = 0.5
    variance = 1.0 / (4 * n)
    return mean, variance

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    print(f"{0.5:.6f} {1.0/(4*n):.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

class Solution {
public:
    pair<double, double> medianClt(int n) {
        double mean = 0.5;
        double variance = 1.0 / (4.0 * n);
        return {mean, variance};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        Solution solution;
        auto res = solution.medianClt(n);
        cout << fixed << setprecision(6) << res.first << " " << res.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function medianClt(n) {
  const mean = 0.5;
  const variance = 1.0 / (4 * n);
  return [mean, variance];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const res = medianClt(n);
  console.log(res[0].toFixed(6) + " " + res[1].toFixed(6));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `n = 5`

1. Mean is always 0.5.
2. Variance formula: $1 / (4 \times 5)$.
3. $1 / 20 = 0.05$.
4. Output: `0.500000 0.050000`.

Matches example output.

![Example Visualization](../images/PRB-015/example-1.png)

## ✅ Proof of Correctness

### Invariant
The asymptotic distribution of the sample median is Normal.

### Why the approach is correct
The formula $\text{Var} = \frac{1}{4n f(m)^2}$ is a standard result in non-parametric statistics. For uniform distribution $f(x)=1$, it simplifies to $1/4n$.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** What if distribution is Exponential($\lambda$)?
  - *Hint:* Median m = \ln(2)/\lambda$. PDF $f(m) = \lambda e^{-\lambda m} = \lambda e^{-\ln 2} = \lambda/2$.
  - Variance ≈ \frac{1}{4n (\lambda/2)^2} = \frac{1}{n \lambda^2}$.
- **Extension 2:** What if we want the 75th percentile?
  - *Hint:* General formula involves $p(1-p)$ where p = 0.75$.
- **Extension 3:** Exact distribution?
  - *Hint:* Beta distribution. The k-th order statistic of n uniforms follows Beta($k, n-k+1$). For median, k \approx n/2$, so Beta($n/2, n/2$). Variance of Beta is $\frac{\alpha \beta}{(\alpha+\beta)^2 (\alpha+\beta+1)} \approx \frac{1}{4n}$.

## Common Mistakes to Avoid

1. **Variance of Mean vs Median**
   - ❌ Wrong: Thinking variance is $1/12n$ (which is variance of the sample *mean*).
   - ✅ Correct: Variance of median is $1/4n$ (3 times larger! Median is less efficient than mean for Uniform).
2. **Integer Division**
   - ❌ Wrong: `1 / (4 * n)` in integer arithmetic.
   - ✅ Correct: `1.0 / (4 * n)`.

## Related Concepts

- **Order Statistics:** Study of sorted random variables.
- **Efficiency:** Mean is a more efficient estimator for Uniform/Normal, but Median is more robust.
- **Beta Distribution:** Exact distribution of order statistics.
