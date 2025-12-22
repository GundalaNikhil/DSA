---
problem_id: PRB_MIN_CUT_RANDOM_CONTRACTION__8305
display_id: PRB-006
slug: min-cut-random-contraction
title: "Min-Cut with Randomized Contraction"
difficulty: Medium
difficulty_score: 52
topics:
  - Probability
  - Graphs
  - Randomized Algorithms
tags:
  - probability
  - karger
  - min-cut
  - medium
premium: true
subscription_tier: basic
---

# PRB-006: Min-Cut with Randomized Contraction

## 📋 Problem Summary

Karger's algorithm finds the global min-cut of a graph with n vertices with probability $p_{success} \ge \frac{2}{n(n-1)}$.
Given n and a desired confidence level P (e.g., 0.99), calculate the minimum number of independent trials t required to ensure the probability of finding the min-cut is at least P.

| | |
|---|---|
| **Input** | n, P |
| **Output** | Integer t |

## 🌍 Real-World Scenario

**Scenario Title:** The Network Vulnerability Scan

You are a security analyst testing a communication network for bottlenecks.
- The "Global Min-Cut" represents the smallest set of links whose removal would disconnect the network into two pieces.
- Finding this exactly is computationally expensive for massive networks.
- You run a fast randomized algorithm (Karger's) that might miss the true min-cut.
- To be 99.9% sure you've found the actual weakest point, you need to run the simulation multiple times.
- You need to calculate exactly how many times to run it to meet your safety certification standards.

**Why This Problem Matters:**

- **Network Reliability:** Assessing robustness against link failures.
- **Image Segmentation:** Graph cuts are used to separate objects from backgrounds.
- **Clustering:** Identifying tightly connected communities.

![Real-World Application](../images/PRB-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Probability Amplification

Single Trial:
Success (S) prob p. Failure (F) prob 1-p.

t Trials:
All Fail: $(1-p)^t$.
At least one Success: $1 - (1-p)^t$.

We want $1 - (1-p)^t \ge P$.
$(1-p)^t \le 1 - P$. t \ln(1-p) \le \ln(1-P)$.
Since $\ln(1-p)$ is negative, dividing flips the inequality: t \ge \frac{\ln(1-P)}{\ln(1-p)}$.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Formula:** $p_{success} = \frac{2}{n(n-1)}$.
- **Logarithms:** Use natural log (`Math.log` in Java/JS, `math.log` in Python, `log` in C++).
- **Rounding:** Since t must be an integer, take the ceiling.
- **Constraints:** n up to 10⁹. $p_{success}$ can be very small.
  - If p is very small, $\ln(1-p) \approx -p$.
  - t \approx \frac{\ln(1-P)}{-p} = \frac{-\ln(1-P)}{p}$.
  - This approximation is useful for mental checks but use exact log for code.

### Core Concept: Bernoulli Trials

We are repeating a Bernoulli trial until "at least one success".
This is related to the Geometric distribution (waiting time), but here we fix the number of trials to guarantee a cumulative probability.

## Naive Approach

### Intuition

Loop t = 1, 2, \dots$ until $1 - (1-p)^t \ge P$.

### Algorithm

While loop.

### Time Complexity

- **O(t)**. If p is small (10⁻¹⁸), t can be huge ($10^{18}$). Loop is too slow.

## Optimal Approach

### Key Insight

Use the closed-form logarithmic formula derived above.

### Algorithm

1. Calculate $p_{success} = 2.0 / (n * (n - 1))$.
2. Calculate numerator = $\ln(1 - P)$.
3. Calculate denominator = $\ln(1 - p_{success})$.
4. Calculate t = \text{ceil}(\text{numerator} / \text{denominator})$.
5. Print t.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PRB-006/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-006/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long minTrials(long n, double P) {
        if (n < 2) return 0; // Should not happen based on constraints
        
        double pSuccess = 2.0 / (n * (n - 1.0));
        
        // We want 1 - (1 - pSuccess)^t >= P
        // (1 - pSuccess)^t <= 1 - P
        // t * ln(1 - pSuccess) <= ln(1 - P)
        // t >= ln(1 - P) / ln(1 - pSuccess)
        
        double numerator = Math.log(1.0 - P);
        double denominator = Math.log(1.0 - pSuccess);
        
        return (long) Math.ceil(numerator / denominator);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            double P = sc.nextDouble();

            Solution solution = new Solution();
            System.out.println(solution.minTrials(n, P));
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import math

def min_trials(n: int, P: float) -> int:
    if n < 2:
        return 0
        
    p_success = 2.0 / (n * (n - 1))
    
    # Avoid log(0) if P=1 (though constraints say P < 1)
    if P >= 1.0:
        return float('inf') # Or handle appropriately
        
    numerator = math.log(1.0 - P)
    denominator = math.log(1.0 - p_success)
    
    return math.ceil(numerator / denominator)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    P = float(data[1])
    print(min_trials(n, P))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    long long minTrials(long long n, double P) {
        if (n < 2) return 0;
        
        double pSuccess = 2.0 / (n * (n - 1.0));
        
        double numerator = log(1.0 - P);
        double denominator = log(1.0 - pSuccess);
        
        return (long long)ceil(numerator / denominator);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    double P;
    if (cin >> n >> P) {
        Solution solution;
        cout << solution.minTrials(n, P) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function minTrials(n, P) {
  if (n < 2) return 0;
  
  const pSuccess = 2.0 / (n * (n - 1));
  
  const numerator = Math.log(1.0 - P);
  const denominator = Math.log(1.0 - pSuccess);
  
  return Math.ceil(numerator / denominator);
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
  const P = parseFloat(data[1]);
  console.log(minTrials(n, P));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `4 0.9`.
1. $p_{success} = 2 / (4 \times 3) = 2/12 = 1/6 \approx 0.1667$.
2. $\ln(1 - 0.9) = \ln(0.1) \approx -2.3026$.
3. $\ln(1 - 0.1667) = \ln(0.8333) \approx -0.1823$.
4. Ratio: $-2.3026 / -0.1823 \approx 12.63$.
5. Ceil: 13.
Matches example.

## ✅ Proof of Correctness

### Invariant
The formula directly solves the inequality for cumulative probability.

### Why the approach is correct
Standard probability theory.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Karger-Stein Algorithm.
  - *Hint:* Recursive contraction improves success probability to $1/\log n$.
- **Extension 2:** Parallel trials.
  - *Hint:* Run trials on multiple cores to reduce wall-clock time.
- **Extension 3:** Weighted Graphs.
  - *Hint:* Karger's works for weighted graphs too (probabilities proportional to weights).

### C++ommon Mistakes to Avoid

1. **Precision Loss**
   - ❌ Wrong: `1.0 - P` when P is very close to 1.
   - ✅ Correct: Use `log1p(-P)` if available for better precision, though standard `log` is usually fine for P < 1 - 10^{-15}$.
2. **Integer Division**
   - ❌ Wrong: `2 / (n * (n-1))` in integer arithmetic.
   - ✅ Correct: `2.0 / ...`.

## Related Concepts

- **Monte Carlo Algorithms:** Always fast, sometimes wrong (but error bounded).
- **Las Vegas Algorithms:** Always correct, sometimes slow. Karger's is Monte Carlo.
