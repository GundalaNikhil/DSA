---
problem_id: PDS_XOR_FILTERS__7789
display_id: PDS-013
slug: xor-filters
title: "XOR Filters"
difficulty: Medium
difficulty_score: 52
topics:
  - Probabilistic Data Structures
  - XOR Filters
  - False Positives
tags:
  - probabilistic-ds
  - xor-filter
  - false-positives
  - medium
premium: true
subscription_tier: basic
---

# PDS-013: XOR Filters

## 📋 Problem Summary

We need to calculate the memory usage and false positive rate (FPR) for an XOR Filter.
- An XOR Filter is a modern alternative to Bloom Filters.
- It is more space-efficient (usually 1.23 bits per entry overhead vs Bloom's 1.44).
- It stores $b$-bit fingerprints.
- The number of cells required is approximately $1.23 \times n$, where $n$ is the number of keys.
- The FPR is $2^{-b}$.

## 🌍 Real-World Scenario

**Scenario Title:** Browser Malicious Site Blocking

Browsers (Chrome/Firefox) maintain a list of known malicious URLs.
- This list is huge (millions of URLs).
- Checking a remote server for every page load is too slow and leaks privacy.
- The browser downloads a compressed filter of bad URLs.
- **XOR Filters** are perfect here because they are static (read-only) and smaller than Bloom Filters.
- If the filter says "Safe", the browser proceeds.
- If the filter says "Malicious" (might be a false positive), the browser performs a secondary, slower check.
- Saving 20% space over Bloom Filters means faster updates and less bandwidth for billions of users.

**Why This Problem Matters:**

- **Embedded Systems:** Extremely constrained memory environments.
- **Static Sets:** When the set of keys doesn't change often, XOR filters are superior.

![Real-World Application](../images/PDS-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: XOR Filter Logic

Structure: Array `B` of size $m \approx 1.23n$.
Key $x$ maps to 3 positions $h_0(x), h_1(x), h_2(x)$.
Fingerprint $f(x)$ is stored such that:
`B[h0] ^ B[h1] ^ B[h2] = f(x)`

```
Key "A": h=[1, 5, 8], f=101
Key "B": h=[2, 5, 9], f=011

To query "A":
Read B[1], B[5], B[8].
XOR them.
If result == 101, return True.
Else, return False.
```

If we query a key "C" not in the set, the XOR sum will be a random $b$-bit value. The chance it matches $f(C)$ is $1/2^b$.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:**
  - $n$: Number of keys.
  - $b$: Bits per fingerprint.
- **Output:**
  - Memory: $\lceil 1.23 \times n \rceil \times b$.
  - FPR: $2^{-b}$.

## Naive Approach

### Intuition

Implement formulas.

### Algorithm

1. `cells = ceil(1.23 * n)`.
2. `mem = cells * b`.
3. `fpr = pow(2, -b)`.

### Limitations

- None.

## Optimal Approach

### Key Insight

Direct calculation.

### Algorithm

1. Read $n, b$.
2. `cells = ceil(1.23 * n)`.
3. `mem = cells * b`.
4. `fpr = pow(2.0, -b)`.
5. Print both.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PDS-013/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-013/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public Object[] xorFilterStats(long n, int b) {
        long cells = (long) Math.ceil(1.23 * n);
        long mem = cells * b;
        double fpr = Math.pow(2.0, -b);
        return new Object[]{mem, fpr};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            int b = sc.nextInt();
    
            Solution solution = new Solution();
            Object[] res = solution.xorFilterStats(n, b);
            System.out.println(res[0] + " " + String.format("%.6f", (double)res[1]));
        }
        sc.close();
    }
}
```

### Python

```python
import math
import sys

def xor_filter_stats(n: int, b: int):
    cells = math.ceil(1.23 * n)
    mem = int(cells * b)
    fpr = 2.0 ** -b
    return mem, fpr

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    b = int(data[1])
    mem, fpr = xor_filter_stats(n, b)
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
    pair<long long, double> xorFilterStats(long long n, int b) {
        long long cells = (long long) ceil(1.23 * n);
        long long mem = cells * b;
        double fpr = pow(2.0, -b);
        return {mem, fpr};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int b;
    if (cin >> n >> b) {
        Solution solution;
        auto res = solution.xorFilterStats(n, b);
        cout << res.first << " " << fixed << setprecision(6) << res.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function xorFilterStats(n, b) {
  const cells = Math.ceil(1.23 * n);
  const mem = cells * b;
  const fpr = Math.pow(2.0, -b);
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
  const n = parseInt(data[0], 10);
  const b = parseInt(data[1], 10);
  const res = xorFilterStats(n, b);
  console.log(res[0] + " " + res[1].toFixed(6));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `1000 8`

1. $n=1000, b=8$.
2. Cells = $\lceil 1.23 \times 1000 \rceil = \lceil 1230.0 \rceil = 1230$.
3. Memory = $1230 \times 8 = 9840$ bits.
4. FPR = $2^{-8} = 1/256 \approx 0.003906$.

Output: `9840 0.003906`. Matches example.

![Example Visualization](../images/PDS-013/example-1.png)

## ✅ Proof of Correctness

### Invariant
XOR filters require solving a linear system over GF(2). The factor 1.23 is empirically derived (related to the threshold for 2-core of a random hypergraph) to ensure the system is solvable with high probability.

### Why the approach is correct
We implement the standard sizing formula.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Construction time?
  - *Hint:* Construction is slower than Bloom filters because it involves solving a system (though optimized peeling algorithms make it fast, $O(n)$).
- **Extension 2:** Can we add elements?
  - *Hint:* No, XOR filters are immutable. Adding an element changes the solution to the entire system.

### Common Mistakes to Avoid

1. **Ceiling**
   - ❌ Wrong: `(long)(1.23 * n)` (truncates).
   - ✅ Correct: `Math.ceil()`.

## Related Concepts

- **Cuckoo Filter:** Another space-efficient alternative (supports deletions).
- **Ribbon Filter:** Even more space-efficient variant of XOR filters.
