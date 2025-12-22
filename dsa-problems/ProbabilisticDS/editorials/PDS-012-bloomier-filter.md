---
problem_id: PDS_BLOOMIER_FILTER__6841
display_id: PDS-012
slug: bloomier-filter
title: "Bloomier Filter Key-Value"
difficulty: Hard
difficulty_score: 65
topics:
  - Probabilistic Data Structures
  - Bloomier Filter
  - False Positives
tags:
  - probabilistic-ds
  - bloomier
  - key-value
  - hard
premium: true
subscription_tier: basic
---

# PDS-012: Bloomier Filter Key-Value

## 📋 Problem Summary

We need to calculate the memory usage and false positive probability (FPR) of a Bloomier Filter.
- A Bloomier Filter is a generalization of a Bloom Filter that stores a value associated with each key, instead of just a boolean.
- It uses an array of $m$ cells, each of width $r$ bits.
- If we query a key that was inserted, we get the correct value.
- If we query a key that was NOT inserted, we get a random $r$-bit value (false positive).
- The probability that this random value matches a specific target value (or looks like a valid value) is $2^{-r}$.

## 🌍 Real-World Scenario

**Scenario Title:** URL Shortener Cache

Imagine a URL shortener like bit.ly.
- You have billions of mappings: `short_code -> long_url_id`.
- You want to cache these in RAM to avoid DB lookups.
- A HashMap stores the full key (short_code) and value, which is huge.
- A **Bloomier Filter** can store this mapping using very few bits per key.
- If the user asks for a valid short code, it returns the correct ID.
- If the user asks for an invalid short code, it returns a random ID (which the DB will reject as "not found").
- This trades a small chance of a "phantom lookup" for massive memory savings.

**Why This Problem Matters:**

- **Distributed Systems:** Storing metadata about files in a distributed file system.
- **Networking:** Router forwarding tables.

![Real-World Application](../images/PDS-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Bloomier Filter Structure

Table of size $m=4$, width $r=2$ bits.

```
Index: 0   1   2   3
Val:  [01] [11] [00] [10]
```

To insert `Key="A", Val="11"`:
- Hash "A" to get indices $h_1, h_2, h_3$.
- XOR the values at these indices to match "11".
- This requires solving a system of linear equations (usually done via peeling/cuckoo-style ordering).

Query `Key="B"` (not in set):
- Hash "B" to get indices.
- XOR values. Result is random bits, e.g., `01`.
- Probability this equals a specific target is $1/2^r$.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:**
  - $m$: Number of cells.
  - $r$: Bits per cell.
- **Output:**
  - Memory in bits: $m \times r$.
  - FPR: $2^{-r}$.

## Naive Approach

### Intuition

Implement formulas.

### Algorithm

1. `mem = m * r`.
2. `fpr = pow(2, -r)`.

### Limitations

- None.

## Optimal Approach

### Key Insight

Direct calculation.

### Algorithm

1. Read $m, r$.
2. Compute `mem = m * r`.
3. Compute `fpr = pow(2.0, -r)`.
4. Print both.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PDS-012/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-012/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public Object[] bloomierStats(long m, int r) {
        long mem = m * r;
        double fpr = Math.pow(2.0, -r);
        return new Object[]{mem, fpr};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long m = sc.nextLong();
            int r = sc.nextInt();
    
            Solution solution = new Solution();
            Object[] res = solution.bloomierStats(m, r);
            System.out.println(res[0] + " " + String.format("%.6f", (double)res[1]));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def bloomier_stats(m: int, r: int):
    mem = m * r
    fpr = 2.0 ** -r
    return mem, fpr

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = int(data[0])
    r = int(data[1])
    mem, fpr = bloomier_stats(m, r)
    print(f"{mem} {fpr:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

class Solution {
public:
    pair<long long, double> bloomierStats(long long m, int r) {
        long long mem = m * r;
        double fpr = pow(2.0, -r);
        return {mem, fpr};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long m;
    int r;
    if (cin >> m >> r) {
        Solution solution;
        auto res = solution.bloomierStats(m, r);
        cout << res.first << " " << fixed << setprecision(6) << res.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function bloomierStats(m, r) {
  const mem = m * r;
  const fpr = Math.pow(2.0, -r);
  return [mem, fpr];
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
  const r = parseInt(data[1], 10);
  const res = bloomierStats(m, r);
  console.log(res[0] + " " + res[1].toFixed(6));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `6 4`

1. $m=6, r=4$.
2. Memory = $6 \times 4 = 24$ bits.
3. FPR = $2^{-4} = 1/16 = 0.0625$.

Output: `24 0.062500`. Matches example.

![Example Visualization](../images/PDS-012/example-1.png)

## ✅ Proof of Correctness

### Invariant
The FPR is determined solely by the bit-width of the stored values, assuming uniform hashing.

### Why the approach is correct
Standard property of Bloomier Filters.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** How to handle updates?
  - *Hint:* Bloomier filters are static. To support updates, use a dynamic version or rebuild.
- **Extension 2:** What if the graph has cycles?
  - *Hint:* Construction fails. Need to re-hash or use more space (typically $m \approx 1.23n$ ensures success).

## Common Mistakes to Avoid

1. **Precision**
   - ❌ Wrong: Integer division for FPR.
   - ✅ Correct: Floating point.

## Related Concepts

- **XOR Filter:** More modern, space-efficient version.
- **Perfect Hashing:** Similar goal (O(1) lookup), but usually stores keys.
