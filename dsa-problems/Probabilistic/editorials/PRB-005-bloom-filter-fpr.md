---
problem_id: PRB_BLOOM_FILTER_FPR__4972
display_id: PRB-005
slug: bloom-filter-fpr
title: "Bloom Filter False Positive Rate"
difficulty: Medium
difficulty_score: 48
topics:
  - Probability
  - Data Structures
  - Hashing
tags:
  - probability
  - bloom-filter
  - hashing
  - medium
premium: true
subscription_tier: basic
---

# PRB-005: Bloom Filter False Positive Rate

## 📋 Problem Summary

Calculate the theoretical false positive probability of a Bloom Filter.

| | |
|---|---|
| **Parameters** | m bits, k hash functions, n inserted elements |
| **Formula** | P = (1 - e^(-kn/m))^k |
| **Input** | m, k, n |
| **Output** | Probability (float) |

## 🌍 Real-World Scenario

**Scenario Title:** The Malicious URL Blocker

You are building a web browser feature to warn users about malicious websites.

- The list of malicious URLs is huge (millions) and constantly updating.
- Storing the full list on every user's device is too expensive (memory/storage).
- Instead, you use a **Bloom Filter**: a compact probabilistic data structure.
- When a user visits a URL, you check the filter.
  - If it says "Safe", it is definitely safe (No False Negatives).
  - If it says "Malicious", it might be a False Positive. In this case, you make a slower API call to the server to verify.
- You need to tune the filter parameters (m, k) to minimize the False Positive Rate (FPR) so you don't overload the server with unnecessary checks.

**Why This Problem Matters:**

- **Database Systems:** Reducing disk lookups (e.g., Cassandra, HBase).
- **Networking:** Router IP lookups.
- **Blockchain:** Bitcoin SPV wallets use Bloom filters to request relevant transactions.

![Real-World Application](../images/PRB-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Bloom Filter Operation

m = 10bits, k = 2 hashes. Insert "A".
$h_1(A) = 3, h_2(A) = 7$.

```
Step 1: Insert "A"
Index: 0 1 2 3 4 5 6 7 8 9
Bits: [0 0 0 1 0 0 0 1 0 0]
             ↑       ↑
          h₁(A)    h₂(A)
```

Query "B" - Definitely NOT in set:

```
h₁(B) = 3, h₂(B) = 5
Index: 0 1 2 3 4 5 6 7 8 9
Bits: [0 0 0 1 0 0 0 1 0 0]
             ✓   ✗
        Bit 3=1  Bit 5=0  → "Definitely Not Present"
```

Query "C" - False Positive:

```
h₁(C) = 3, h₂(C) = 7
Index: 0 1 2 3 4 5 6 7 8 9
Bits: [0 0 0 1 0 0 0 1 0 0]
             ✓       ✓
        Both bits are 1 → "Possibly Present"
        (But "C" was never inserted! FALSE POSITIVE)
```

### Bit Array Evolution

How the filter fills up as elements are added:

```
┌─────────────────────────────────────────────────────────┐
│ m=10, k=2 (2 hash functions)                           │
├─────────────────────────────────────────────────────────┤
│ n=0  [0 0 0 0 0 0 0 0 0 0]  Empty      (0% filled)    │
│                                                         │
│ n=1  [0 0 0 1 0 0 0 1 0 0]  1 element  (20% filled)   │
│                                                         │
│ n=3  [1 0 1 1 0 1 0 1 0 0]  3 elements (50% filled)   │
│                                                         │
│ n=5  [1 1 1 1 1 1 0 1 0 1]  5 elements (80% filled)   │
│                                                         │
│ n=10 [1 1 1 1 1 1 1 1 1 1]  10 elements(100% filled)  │
│                             ↑ FPR approaches 1.0!      │
└─────────────────────────────────────────────────────────┘

Observation: As more elements added, FPR increases dramatically!
```

### False Positive Rate Graph

```
FPR (%)
100 │                                    ╱
    │                                  ╱
 80 │                                ╱
    │                              ╱
 60 │                            ╱
    │                         ╱─┘
 40 │                      ╱─┘
    │                   ╱─┘
 20 │              ╱──┘
    │         ╱───┘
  0 │────────┘─────────────────────────────> n (elements)
    0       m/4      m/2        m

    Optimal n ≈ (m/k)×ln(2) minimizes FPR for given m
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Formula Derivation:**
  - Prob a specific bit is 0 after 1 hash: $1 - 1/m$.
  - Prob a specific bit is 0 after $kn$ hashes: $(1 - 1/m)^{kn} \approx e^{-kn/m}$.
  - Prob a specific bit is 1: $1 - e^{-kn/m}$.
  - False Positive: All k hashes for a new element hit 1s.
  - P \approx (1 - e^{-kn/m})^k$.
- **Precision:** Use `double`.
- **Constraints:** m, n ≤ 10⁶. Calculation is O(1).

### Core Concept: Probability of Collision

**Step-by-Step Derivation:**

1. **Probability a specific bit remains 0 after one hash:**
   . P(\text{bit is 0}) = 1 - \frac{1}{m} = \frac{m-1}{m}. 

2. **After k hash functions on one element:**
   . P(\text{bit is 0}) = \left(1 - \frac{1}{m}\right)^k. 

3. **After inserting n elements (total $kn$ hash operations):**
   . P(\text{bit is 0}) = \left(1 - \frac{1}{m}\right)^{kn}. 

4. **Approximate using $\lim_{m \to \infty} (1 - 1/m)^m = e^{-1}$:**
   . P(\text{bit is 0}) \approx e^{-kn/m}. 

5. **Therefore, probability bit is 1:**
   . P(\text{bit is 1}) = 1 - e^{-kn/m}. 

6. **False Positive = All k bits for new element are 1:**
   . P_{\text{FP}} = \left(1 - e^{-kn/m}\right)^k. 

**Optimal Number of Hash Functions:**

To minimize FPR for given m and n:
. k_{\text{optimal}} = \frac{m}{n} \ln 2 \approx 0.693 \times \frac{m}{n}. 

This balances:

- **Too few hashes** → bits fill up quickly → high collision rate
- **Too many hashes** → more opportunities for false matches

**Example Comparison:**

```
┌────────┬─────┬─────┬─────────┬──────────┐
│ m      │  n  │  k  │ FPR     │ Notes    │
├────────┼─────┼─────┼─────────┼──────────┤
│ 1,000  │ 100 │  7  │ 0.0082  │ Optimal  │
│ 1,000  │ 100 │  3  │ 0.0468  │ Too few  │
│ 1,000  │ 100 │ 15  │ 0.0172  │ Too many │
│ 10,000 │ 100 │ 69  │ 0.0001  │ Low FPR  │
└────────┴─────┴─────┴─────────┴──────────┘
```

## Naive Approach

### Intuition

Simulate a Bloom Filter.

### Algorithm

Create bit array, hash n items, check random items.

### Time Complexity

- **O(k \cdot n)**. Too slow and approximate.

## Optimal Approach

### Key Insight

Direct implementation of the mathematical formula.

### Algorithm

1. Calculate exponent: `exponent = -k * n / m`.
2. Calculate base: `base = 1.0 - exp(exponent)`.
3. Calculate result: `p = pow(base, k)`.
4. Print `p`.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PRB-005/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-005/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public double bloomFpr(double m, double k, double n) {
        // P = (1 - exp(-k * n / m))^k
        double exponent = -k * n / m;
        double term = 1.0 - Math.exp(exponent);
        return Math.pow(term, k);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextDouble()) {
            double m = sc.nextDouble();
            double k = sc.nextDouble();
            double n = sc.nextDouble();

            Solution solution = new Solution();
            System.out.printf("%.6f\n", solution.bloomFpr(m, k, n));
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import math

def bloom_fpr(m: float, k: float, n: float) -> float:
    exponent = -k * n / m
    term = 1.0 - math.exp(exponent)
    return math.pow(term, k)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = float(data[0])
    k = float(data[1])
    n = float(data[2])
    print(f"{bloom_fpr(m, k, n):.6f}")

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
    double bloomFpr(double m, double k, double n) {
        double exponent = -k * n / m;
        double term = 1.0 - exp(exponent);
        return pow(term, k);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double m, k, n;
    if (cin >> m >> k >> n) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.bloomFpr(m, k, n) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function bloomFpr(m, k, n) {
  const exponent = (-k * n) / m;
  const term = 1.0 - Math.exp(exponent);
  return Math.pow(term, k);
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const m = parseFloat(data[0]);
  const k = parseFloat(data[1]);
  const n = parseFloat(data[2]);
  console.log(bloomFpr(m, k, n).toFixed(6));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `1000 3 100`.

1. `exponent = -3 * 100 / 1000 = -0.3`.
2. `exp(-0.3) ≈ 0.740818`.
3. `term = 1 - 0.740818 = 0.259182`.
4. `pow(0.259182, 3) ≈ 0.017411`.
   Matches example.

## ✅ Proof of Correctness

### Invariant

The formula is the standard asymptotic approximation for Bloom Filter FPR.

### Why the approach is correct

Direct application of the formula.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Optimal k for given $m, n$.
  - _Hint:_ k = \frac{m}{n} \ln 2$.
- **Extension 2:** Counting Bloom Filter.
  - _Hint:_ Use counters instead of bits to allow deletion.
- **Extension 3:** Union/Intersection of Bloom Filters.
  - _Hint:_ Bitwise OR/AND (if sizes match).

## Common Mistakes to Avoid

1. **Integer Division**
   - ❌ Wrong: `k * n / m` with integers.
   - ✅ Correct: Use doubles.
2. **Log Base**
   - ❌ Wrong: `log` usually means `ln` in math libs, but check documentation.
   - ✅ Correct: `exp` is $e^x$.

## Related Concepts

- **False Positive vs False Negative:** Bloom filters have no false negatives.
- **Space Efficiency:** Bloom filters are much smaller than HashSets.
