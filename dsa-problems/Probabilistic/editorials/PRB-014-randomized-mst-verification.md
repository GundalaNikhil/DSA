---
problem_id: PRB_RANDOMIZED_MST_VERIFICATION__6089
display_id: PRB-014
slug: randomized-mst-verification
title: "Randomized MST Verification"
difficulty: Medium
difficulty_score: 56
topics:
  - Probability
  - Graphs
  - Verification
tags:
  - probability
  - mst
  - verification
  - medium
premium: true
subscription_tier: basic
---

# PRB-014: Randomized MST Verification

## 📋 Problem Summary

We have a randomized algorithm that detects if a Minimum Spanning Tree (MST) is incorrect with probability p = 1/n^2$ in a single trial. We need to find the minimum number of trials t such that the probability of detecting an error (if one exists) is at least C.

| | |
|---|---|
| **Input** | n, C |
| **Output** | Integer t |

## 🌍 Real-World Scenario

**Scenario Title:** Factory Defect Detection

Imagine a factory producing high-end computer chips. Occasionally, a machine malfunctions and produces a batch of chips with a subtle defect.
- You have a quick, randomized test that can spot this defect.
- However, the test is not perfect. It only catches the defect with a small probability p (say, 1 in 100) each time you run it.
- If the batch is actually defective, you want to be 99.9% sure you catch it before shipping.
- How many times must you run this quick test to achieve that confidence level?

**Why This Problem Matters:**

- **Software Testing:** Fuzz testing often relies on hitting rare edge cases.
- **Security:** Intrusion detection systems might only catch a sophisticated attacker with low probability per packet.
- **Monte Carlo Simulations:** Determining how many samples are needed to bound error.

![Real-World Application](../images/PRB-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Probability Accumulation

Let p be the probability of success (detection) in one trial.
Let q = 1-p$ be the probability of failure (miss) in one trial.

After t trials:
- Prob(All Miss) = q \times q \times \dots \times q = q^t$
- Prob(At least one Hit) = `1 - q^t`

We want this to be `>= C`.

```
Trial 1: [Miss (99%)] ----> Trial 2: [Miss (99%)] ...
      |                      |
      v                      v
   [Hit (1%)]             [Hit (1%)]
   (Success!)             (Success!)

Target: Total Probability of hitting "Success" >= C
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Probability p:** The problem states p = 1/n^2$.
- **Confidence C:** A value between 0 and 1 (exclusive). E.g., 0.99.
- **Constraints:** n can be up to 10⁹, so p can be very small (10⁻¹⁸).
- **Precision:** Standard floating point `double` is usually sufficient, but be careful with `log(1-C)` if C is extremely close to 1.
- **Output:** An integer representing the count.

## Naive Approach

### Intuition

Simulate the probability accumulation by multiplying `(1-p)` repeatedly until the result is small enough.

### Algorithm

1. Calculate p = 1.0 / (n \times n)$.
2. Initialize `miss_prob = 1.0`.
3. Initialize `trials = 0`.
4. While `1.0 - miss_prob < C`:
   - `miss_prob *= (1.0 - p)`
   - `trials++`
5. Return `trials`.

### Time Complexity

- **O(t)**. If t is large (which it is when p is small), this is too slow.
- For n = 10^5, p = 10^{-10}`. To get C = 0.5, we need t ~= 1/p = 10^10` iterations. This will TLE.

### Space Complexity

- **O(1)**.

### Limitations

- Way too slow for large n.

## Optimal Approach

### Key Insight

We can solve the inequality mathematically using logarithms.

.  1 - (1-p)^t \ge C . 
.  (1-p)^t \le 1 - C . 

Take natural log (`ln`) on both sides. Since `ln` is monotonic increasing, the inequality direction is preserved.
.  \ln((1-p)^t) \le \ln(1 - C) . 
.  t \cdot \ln(1-p) \le \ln(1 - C) . 

Now divide by `ln(1-p)`.
**Crucial Step:** Since p > 0`,`(1-p) < 1`, so`\ln(1-p)$ is **negative**.
Dividing by a negative number **flips the inequality**.

.  t \ge \frac{\ln(1 - C)}{\ln(1 - p)} . 

So, t = \lceil \frac{\ln(1 - C)}{\ln(1 - p)} \rceil$.

### Algorithm

1. Compute p = 1.0 / (n \times n)$.
2. Compute numerator `num = ln(1 - C)`.
3. Compute denominator `den = ln(1 - p)`.
4. Result t = \lceil num / den \rceil$.
5. Return t cast to integer.

### Time Complexity

- **O(1)** assuming log operations are constant time.

### Space Complexity

- **O(1)**.

### Why This Is Optimal

Direct formula computation is instant.

![Algorithm Visualization](../images/PRB-014/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-014/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long minTrials(long n, double C) {
        // p is probability of detection per trial
        double p = 1.0 / (n * n);
        
        // We want 1 - (1-p)^t >= C
        // (1-p)^t <= 1 - C
        // t * ln(1-p) <= ln(1-C)
        // t >= ln(1-C) / ln(1-p)  (since ln(1-p) is negative)
        
        double num = Math.log(1.0 - C);
        double den = Math.log(1.0 - p);
        
        return (long) Math.ceil(num / den);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            double C = sc.nextDouble();

            Solution solution = new Solution();
            System.out.println(solution.minTrials(n, C));
        }
        sc.close();
    }
}
```

### Python

```python
import math
import sys

def min_trials(n: int, C: float) -> int:
    # p is probability of detection per trial
    # Use float for division
    p = 1.0 / (n * n)
    
    # Avoid log(0) if C is exactly 1 (though constraints say C < 1)
    if C >= 1.0:
        return float('inf') # Theoretically impossible
        
    num = math.log(1.0 - C)
    den = math.log(1.0 - p)
    
    return math.ceil(num / den)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    C = float(data[1])
    print(min_trials(n, C))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    long long minTrials(long long n, double C) {
        double p = 1.0 / ((double)n * n);
        
        double num = log(1.0 - C);
        double den = log(1.0 - p);
        
        return (long long) ceil(num / den);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    double C;
    if (cin >> n >> C) {
        Solution solution;
        cout << solution.minTrials(n, C) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function minTrials(n, C) {
  const p = 1.0 / (n * n);
  
  const num = Math.log(1.0 - C);
  const den = Math.log(1.0 - p);
  
  return Math.ceil(num / den);
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
  const C = parseFloat(data[1]);
  console.log(minTrials(n, C));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `n = 10, C = 0.99`

1. Calculate p:
   p = 1 / (10 \times 10) = 0.01$.
2. Calculate terms:
   `1 - C = 0.01`.
   `1 - p = 0.99`.
3. Logarithms:
   `ln(0.01) ~= -4.60517`
   `ln(0.99) ~= -0.01005`
4. Division:
   t = -4.60517 / -0.01005 \approx 458.2$
5. Ceiling:
   `lceil 458.2 rceil = 459`.

Answer: 459.

Let's check:
`(0.99)^458 ~= 0.01004 > 0.01` (Fail probability still too high)
`(0.99)^459 ~= 0.00994 < 0.01` (Fail probability low enough)
Success prob `= 1 - 0.00994 = 0.99006 > 0.99`. Correct.

![Example Visualization](../images/PRB-014/example-1.png)

## ✅ Proof of Correctness

### Invariant
The probability of failing all t trials is `(1-p)^t`.

### Why the approach is correct
We directly solved the inequality `1 - (1-p)^t >= C` for t. The logarithmic transformation is valid and preserves the solution set, provided we handle the sign change when dividing by the negative log.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** What if p is not constant but changes?
  - *Hint:* Product of `(1-p_i)`.
- **Extension 2:** Approximation for small p.
  - *Hint:* `ln(1-p) ~= -p`. So t \approx \frac{-\ln(1-C)}{p}$.
  - For n = 10, p = 0.01`. t ~= 4.605 / 0.01 = 460.5`. Close to 459.
- **Extension 3:** Two-sided error (false positives and negatives).
  - *Hint:* Chernoff bounds.

### Common Mistakes to Avoid

1. **Integer Division**
   - ❌ Wrong: `p = 1 / (n * n)` in integer arithmetic results in 0.
   - ✅ Correct: `p = 1.0 / (n * n)`.
2. **Log Base**
   - ❌ Wrong: Using `log10` for one and `ln` for other.
   - ✅ Correct: Use same base (usually `Math.log` is natural log).
3. **Inequality Direction**
   - ❌ Wrong: Forgetting to flip inequality when dividing by negative `ln(1-p)`.

## Related Concepts

- **Geometric Distribution:** Number of trials to get first success.
- **Bernoulli Trials:** Independent experiments.
- **Monte Carlo Methods:** Error reduction by repetition.
