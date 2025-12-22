---
problem_id: PDS_COUNTING_BLOOM_FILTER__5830
display_id: PDS-002
slug: counting-bloom-filter
title: "Counting Bloom Filter"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - Bloom Filter
  - Poisson Approximation
tags:
  - probabilistic-ds
  - bloom-filter
  - poisson
  - medium
premium: true
subscription_tier: basic
---

# PDS-002: Counting Bloom Filter

## 📋 Problem Summary

We need to calculate the probability that any counter in a Counting Bloom Filter overflows.
- A Counting Bloom Filter replaces bits with $c$-bit counters.
- We have $m$ counters, $k$ hash functions, and $n$ items inserted.
- We model the number of items hashing to a specific counter using a Poisson distribution with parameter $\lambda = \frac{kn}{m}$.
- Overflow happens if a counter value exceeds $MAX = 2^c - 1$.

## 🌍 Real-World Scenario

**Scenario Title:** Streaming Data Deletion

Standard Bloom Filters are great, but they don't support deletion. If you delete an item, you can't just flip bits to 0 because other items might map to the same bits.
- **Solution:** Use counters!
- When inserting: Increment counters.
- When deleting: Decrement counters.
- **Problem:** Counters have a fixed size (e.g., 4 bits).
- If a counter reaches 15 (binary 1111) and you try to increment it, it overflows.
- Usually, implementations "saturate" at max value. If it saturates, you can no longer safely decrement it (because you don't know if it was 15 or 16 or 100).
- **Goal:** Choose a counter size $c$ large enough so that overflow is extremely rare.

**Why This Problem Matters:**

- **Network Routers:** Tracking flow counts with limited memory.
- **Database Indexing:** Supporting updates and deletions in LSM trees.
- **DDoS Protection:** Counting requests per IP.

![Real-World Application](../images/PDS-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Counting Bloom Filter

```
Counters (m=5, c=3 bits, MAX=7):
Idx:  0   1   2   3   4
Val: [2] [0] [5] [1] [7]

Insert "X" (hashes to 0, 4):
[2]->[3]
[7]->[7] (Overflow/Saturation!)

Delete "X":
[3]->[2]
[7]->[6] (ERROR! We decremented a saturated counter. It might have been 8 or 9 logically.)
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Inputs:**
  - $m$: Number of counters.
  - $k$: Hash functions.
  - $c$: Bits per counter.
  - $n$: Items inserted.
- **Output:** Probability of overflow for a *single* counter.
- **Model:** Poisson approximation.
  - The probability that a specific counter is incremented $i$ times is $P(X=i) = \frac{e^{-\lambda} \lambda^i}{i!}$.
  - Overflow occurs if $i > MAX$.
  - $P(\text{overflow}) = 1 - P(X \le MAX) = 1 - \sum_{i=0}^{MAX} \frac{e^{-\lambda} \lambda^i}{i!}$.

## Naive Approach

### Intuition

Just implement the formula directly.

### Algorithm

1. Calculate $\lambda = (k \times n) / m$.
2. Calculate $MAX = 2^c - 1$.
3. Sum Poisson probabilities from $i=0$ to $MAX$.
4. Subtract sum from 1.

### Limitations

- Factorials grow very fast. `15!` is huge. `100!` overflows 64-bit integers.
- We need to handle floating point precision carefully.

## Optimal Approach

### Key Insight

Since $c$ is small (up to 10), $MAX = 2^{10}-1 = 1023$.
We can compute terms iteratively to avoid large factorials.
Term $T_i = \frac{e^{-\lambda} \lambda^i}{i!}$.
$T_0 = e^{-\lambda}$.
$T_{i} = T_{i-1} \times \frac{\lambda}{i}$.

### Algorithm

1. Read inputs.
2. $\lambda = (double)k * n / m$.
3. $MAX = (1 \ll c) - 1$.
4. `term` = $\exp(-\lambda)$.
5. `sum` = `term`.
6. Loop $i$ from 1 to $MAX$:
   - `term` *= $\lambda / i$.
   - `sum` += `term`.
7. Result = $1.0 - sum$.
8. Print result.

### Time Complexity

- **O(2^c)**. Since $c \le 10$, this is very fast (max 1024 iterations).

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PDS-002/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-002/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public double overflowProbability(int m, int k, int c, int n) {
        double lambda = (double) k * n / m;
        long maxVal = (1L << c) - 1;
        
        double term = Math.exp(-lambda);
        double sum = term;
        
        for (int i = 1; i <= maxVal; i++) {
            term *= (lambda / i);
            sum += term;
        }
        
        return 1.0 - sum;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int k = sc.nextInt();
            int c = sc.nextInt();
            int n = sc.nextInt();

            Solution solution = new Solution();
            System.out.println(solution.overflowProbability(m, k, c, n));
        }
        sc.close();
    }
}
```

### Python

```python
import math
import sys

def overflow_probability(m: int, k: int, c: int, n: int) -> float:
    lambda_val = (k * n) / m
    max_val = (1 << c) - 1
    
    term = math.exp(-lambda_val)
    total_prob = term
    
    for i in range(1, max_val + 1):
        term *= (lambda_val / i)
        total_prob += term
        
    return 1.0 - total_prob

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = int(data[0])
    k = int(data[1])
    c = int(data[2])
    n = int(data[3])
    print(f"{overflow_probability(m, k, c, n):.15f}")

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
    double overflowProbability(int m, int k, int c, int n) {
        double lambda = (double)k * n / m;
        long long maxVal = (1LL << c) - 1;
        
        double term = exp(-lambda);
        double sum = term;
        
        for (int i = 1; i <= maxVal; i++) {
            term *= (lambda / i);
            sum += term;
        }
        
        return 1.0 - sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, k, c, n;
    if (cin >> m >> k >> c >> n) {
        Solution solution;
        cout << fixed << setprecision(15) << solution.overflowProbability(m, k, c, n) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function overflowProbability(m, k, c, n) {
  const lambda = (k * n) / m;
  const maxVal = (1 << c) - 1;
  
  let term = Math.exp(-lambda);
  let sum = term;
  
  for (let i = 1; i <= maxVal; i++) {
    term *= (lambda / i);
    sum += term;
  }
  
  return 1.0 - sum;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const m = parseInt(data[0], 10);
  const k = parseInt(data[1], 10);
  const c = parseInt(data[2], 10);
  const n = parseInt(data[3], 10);
  console.log(overflowProbability(m, k, c, n).toFixed(15));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `m=1000, k=3, c=4, n=500`

1. $\lambda = 3 \times 500 / 1000 = 1.5$.
2. $MAX = 2^4 - 1 = 15$.
3. We need $P(X > 15)$ for Poisson(1.5).
4. Since $\lambda=1.5$ is small and $MAX=15$ is far in the tail (10 standard deviations away), the probability will be tiny.
5. Loop sums $P(X=0) \dots P(X=15)$.
6. Result is $1 - \text{sum}$.

Output: `7.679...e-12`. Matches example.

![Example Visualization](../images/PDS-002/example-1.png)

## ✅ Proof of Correctness

### Invariant
We correctly compute the CDF of the Poisson distribution and subtract from 1 to get the complementary CDF (tail probability).

### Why the approach is correct
The Poisson approximation is standard for "balls in bins" problems when $m$ is large. The iterative computation avoids numerical overflow of factorials.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** What is the optimal $c$?
  - *Hint:* Usually 4 bits is enough for most applications (overflow prob $\approx 10^{-9}$ if space is optimized).
- **Extension 2:** d-left hashing?
  - *Hint:* Using multiple choices for counters reduces the max load significantly (power of two choices), allowing smaller $c$.
- **Extension 3:** Spectral Bloom Filter?
  - *Hint:* Uses counters to estimate frequencies, not just existence.

### C++ommon Mistakes to Avoid

1. **Precision Loss**
   - ❌ Wrong: `1 - sum` when `sum` is very close to 1.
   - ✅ Correct: For extremely small probabilities, we might want to sum the tail directly, but here $MAX$ is small enough that `1-sum` works fine with double precision.
2. **Integer Division**
   - ❌ Wrong: `k * n / m` in integer.
   - ✅ Correct: `(double) k * n / m`.

## Related Concepts

- **Poisson Distribution:** Modeling rare events.
- **Balls in Bins:** Load balancing.
- **Saturation Arithmetic:** Counters that stick at max value.
