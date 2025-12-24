---
problem_id: PDS_BLOOM_FILTER_DESIGN__4217
display_id: PDS-001
slug: bloom-filter-design
title: "Bloom Filter Design"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - Bloom Filter
  - Optimization
tags:
  - probabilistic-ds
  - bloom-filter
  - optimization
  - medium
premium: true
subscription_tier: basic
---

# PDS-001: Bloom Filter Design

## 📋 Problem Summary

We need to design a Bloom Filter by calculating the optimal bit array size (`m`) and number of hash functions (`k`) to store `n` items with a target false positive rate `f`. We then need to verify the design by computing the actual expected false positive rate.

## 🌍 Real-World Scenario

**Scenario Title:** Username Availability Checker

Imagine you are building a massive social network like "TwitFace".
- You have 1 billion users.
- When a new user signs up and types a username, you need to instantly check if it's taken.
- Querying the main database for every keystroke is too slow and expensive.
- **Solution:** Keep a Bloom Filter in memory containing all taken usernames.
- If the filter says "No", the username is definitely available (0% false negative).
- If the filter says "Yes", it *might* be taken (false positive). In this case, you do a slow DB check to confirm.
- You want to minimize memory usage (`m`) while keeping the false alarm rate (`f`) low (e.g., 1%).

**Why This Problem Matters:**

- **Cache Filtering:** Akamai/Cloudflare use Bloom filters to avoid caching "one-hit-wonder" URLs.
- **Database:** Cassandra/HBase use them to avoid reading disk files that don't contain the requested key.
- **Blockchain:** Bitcoin SPV nodes use them to filter transactions.

![Real-World Application](../images/PDS-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Bloom Filter Operations

```
Bit Array (m=10): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Insert "Alice" (k=3 hashes):
H1("Alice") % 10 = 1
H2("Alice") % 10 = 4
H3("Alice") % 10 = 9
Set bits:         [0, 1, 0, 0, 1, 0, 0, 0, 0, 1]

Check "Bob":
H1("Bob") % 10 = 1 (Match)
H2("Bob") % 10 = 3 (Zero! -> Definitely Not Present)
H3("Bob") % 10 = 8 (Zero!)

Check "Alice":
All bits 1, 4, 9 are 1 -> Probably Present.
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Inputs:**
  - `n`: Number of items expected to be inserted.
  - `f`: Desired False Positive Rate (e.g., 0.01 for 1%).
- **Outputs:**
  - `m`: Size of bit array (integer).
  - `k`: Number of hash functions (integer).
  - `FPR`: The calculated error rate using these integer `m` and `k`.
- **Formulas:**
  - `m = lceil frac-n ln f(ln 2)^2 rceil`
  - `k = round(fracmn ln 2)`
  - `FPR = (1 - e^-k n / m)^k`

## Naive Approach

### Intuition

Guess values for `m` and `k` until the FPR looks good.

### Algorithm

1. Try `m = n`. Calculate FPR. Too high?
2. Try `m = 2n`. Better?
3. Keep increasing.

### Limitations

- Inefficient and inexact.
- We have closed-form optimal formulas, so guessing is unnecessary.

## Optimal Approach

### Key Insight

The formulas provided in the problem statement are derived from minimizing the FPR with respect to `k` for a fixed `m`, and then solving for `m` given a target FPR.

1. **Optimal `k`:** For a fixed ratio `m/n`, the optimal `k` is `fracmn ln 2`.
2. **Optimal `m`:** To achieve probability `f`, `m ~= -fracn ln f(ln 2)^2`.

### Algorithm

1. Read `n` and `f`.
2. Compute `m` using `ceil(-n * log(f) / (log(2)^2))`.
3. Compute `k` using `round((m / n) * log(2))`.
4. Compute actual `FPR` using `pow(1 - exp(-k * n / m), k)`.
5. Print `m`, `k`, and formatted `FPR`.

### Time Complexity

- **O(1)**. Just math operations.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PDS-001/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-001/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public Object[] designBloom(long n, double f) {
        double ln2 = Math.log(2);
        
        // Calculate m
        double mDouble = -(n * Math.log(f)) / (ln2 * ln2);
        long m = (long) Math.ceil(mDouble);
        
        // Calculate k
        double kDouble = (m / (double)n) * ln2;
        long k = Math.round(kDouble);
        
        // Calculate actual FPR
        double exponent = -((double)k * n) / m;
        double fpr = Math.pow(1 - Math.exp(exponent), k);
        
        return new Object[]{m, k, fpr};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            double f = sc.nextDouble();

            Solution solution = new Solution();
            Object[] res = solution.designBloom(n, f);
            System.out.println(res[0] + " " + res[1] + " " + String.format("%.6f", (double)res[2]));
        }
        sc.close();
    }
}
```

### Python

```python
import math
import sys

def design_bloom(n: int, f: float):
    ln2 = math.log(2)
    
    # Calculate m
    m_float = -(n * math.log(f)) / (ln2 ** 2)
    m = math.ceil(m_float)
    
    # Calculate k
    k_float = (m / n) * ln2
    k = round(k_float)
    
    # Calculate actual FPR
    exponent = -(k * n) / m
    fpr = (1 - math.exp(exponent)) ** k
    
    return m, k, fpr

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    f = float(data[1])
    m, k, fpr = design_bloom(n, f)
    print(f"{m} {k} {fpr:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
#include <tuple>

using namespace std;

class Solution {
public:
    tuple<long long, long long, double> designBloom(long long n, double f) {
        double ln2 = log(2);
        
        double mDouble = -(n * log(f)) / (ln2 * ln2);
        long long m = (long long) ceil(mDouble);
        
        double kDouble = (m / (double)n) * ln2;
        long long k = (long long) round(kDouble);
        
        double exponent = -((double)k * n) / m;
        double fpr = pow(1.0 - exp(exponent), k);
        
        return make_tuple(m, k, fpr);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    double f;
    if (cin >> n >> f) {
        Solution solution;
        auto res = solution.designBloom(n, f);
        cout << get<0>(res) << " " << get<1>(res) << " " << fixed << setprecision(6) << get<2>(res) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function designBloom(n, f) {
  const ln2 = Math.log(2);
  
  const mDouble = -(n * Math.log(f)) / (ln2 * ln2);
  const m = Math.ceil(mDouble);
  
  const kDouble = (m / n) * ln2;
  const k = Math.round(kDouble);
  
  const exponent = -(k * n) / m;
  const fpr = Math.pow(1 - Math.exp(exponent), k);
  
  return [m, k, fpr];
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
  const f = parseFloat(data[1]);
  const res = designBloom(n, f);
  console.log(res[0] + " " + res[1] + " " + res[2].toFixed(6));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `n = 1000, f = 0.01`

1. **Calculate `m`:**
   - `ln(0.01) ~= -4.605`
   - `(ln 2)^2 ~= 0.480`
   - `m ~= -(1000 x -4.605) / 0.480 ~= 9585.05`
   - `lceil 9585.05 rceil = 9586`.

2. **Calculate `k`:**
   - `m/n = 9.586`
   - `k ~= 9.586 x 0.693 ~= 6.64`
   - `round(6.64) = 7`.

3. **Calculate FPR:**
   - exponent `= -(7 x 1000) / 9586 ~= -0.730`
   - `e^-0.730 ~= 0.481`
   - `1 - 0.481 = 0.519`
   - `0.519^7 ~= 0.010035`

Output: `9586 7 0.010035`. Matches example.

![Example Visualization](../images/PDS-001/example-1.png)

## ✅ Proof of Correctness

### Invariant
The formulas are mathematically derived approximations for optimal Bloom filter parameters assuming ideal hash functions.

### Why the approach is correct
We simply implement the standard formulas. The slight deviation in FPR (0.010035 vs 0.01) is expected because `m` and `k` must be integers.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** What if we can't resize `m`?
  - *Hint:* Then we just optimize `k`. `k = fracmn ln 2`.
- **Extension 2:** Deleting items?
  - *Hint:* Standard Bloom filters don't support deletion. Use Counting Bloom Filter (PDS-002).
- **Extension 3:** Union/Intersection?
  - *Hint:* Bitwise OR/AND works if `m` and `k` are same.

### Common Mistakes to Avoid

1. **Log Base**
   - ❌ Wrong: Using `log10`.
   - ✅ Correct: Use natural log `ln` (`Math.log`).
2. **Integer Division**
   - ❌ Wrong: `m / n` in integer arithmetic before multiplying by `ln 2`.
   - ✅ Correct: Cast to double.
3. **Rounding**
   - ❌ Wrong: Truncating `k` instead of rounding to nearest.

## Related Concepts

- **Hash Functions:** MurmurHash, FNV.
- **False Positive vs False Negative:** Bloom filters have NO false negatives.
- **Space Efficiency:** Bloom filters use `~= 10` bits per item for 1% FPR.
