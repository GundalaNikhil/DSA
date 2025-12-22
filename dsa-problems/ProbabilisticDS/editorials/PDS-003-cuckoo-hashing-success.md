---
problem_id: PDS_CUCKOO_HASHING_SUCCESS__7392
display_id: PDS-003
slug: cuckoo-hashing-success
title: "Cuckoo Hashing Success Probability"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - Hashing
  - Random Graphs
tags:
  - probabilistic-ds
  - cuckoo-hashing
  - probability
  - medium
premium: true
subscription_tier: basic
---

# PDS-003: Cuckoo Hashing Success Probability

## 📋 Problem Summary

We need to calculate the probability that Cuckoo Hashing succeeds in constructing a valid hash table without entering an infinite loop of evictions.
- Cuckoo Hashing uses 2 hash functions.
- An item can be placed in either $H_1(x)$ or $H_2(x)$.
- If both are full, we kick out an existing item to its alternative location.
- This process can fail if there is a cycle in the "cuckoo graph".
- We are given a formula for the failure probability based on load factor $\alpha$ and table size $m$.

## 🌍 Real-World Scenario

**Scenario Title:** High-Performance Router Lookup

Imagine a network router that needs to look up IP addresses in $O(1)$ worst-case time.
- Standard hash tables have collisions, leading to $O(n)$ worst case.
- **Cuckoo Hashing** guarantees $O(1)$ lookup because an item is always in one of two locations.
- However, insertion can fail if the table gets too full (cycles form).
- Before deploying a router with a specific table size ($m$) and expected traffic ($\alpha$), engineers need to know: "What is the chance this table configuration will fail completely?"

**Why This Problem Matters:**

- **Hardware Implementation:** Cuckoo hashing is popular in hardware (FPGA/ASIC) because it requires only 2 parallel memory lookups.
- **Database Indexing:** Used in high-performance in-memory databases.

![Real-World Application](../images/PDS-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Cuckoo Graph

Nodes are buckets in the hash table. Edges connect $H_1(x)$ and $H_2(x)$ for each item $x$.

```
Item A: H1=1, H2=2
Item B: H1=2, H2=3
Item C: H1=3, H2=1

Graph: 1 --(A)-- 2 --(B)-- 3 --(C)-- 1
```

- This forms a cycle: $1-2-3-1$.
- We have 3 items (edges) and 3 buckets (nodes).
- In Cuckoo Hashing, each connected component with $V$ vertices can hold at most $V+1$ edges (actually just $V$ edges for 2-way cuckoo hashing to be simple, or $V$ edges + 1 cycle).
- If the component has more edges than vertices (density > 1), insertion fails.
- The formula provided approximates the probability of such dense subgraphs appearing.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Inputs:**
  - $m$: Table size (buckets).
  - $\alpha$: Load factor ($n/m$).
- **Output:** Success probability.
- **Formula:**
  - $P_{fail} \approx \exp\left(-\frac{(1-\alpha)^2 m}{2}\right)$ is actually a simplified heuristic for the probability of having *no* complex components. Wait, let's check the problem statement carefully.
  - The problem statement gives: $P_{fail} = \exp(-((1 - \alpha)^2 * m) / 2)$.
  - This looks like a bound related to the size of the largest component or the probability of failure.
  - We just need to implement: $P_{success} = 1 - P_{fail}$.

## Naive Approach

### Intuition

Implement the formula.

### Algorithm

1. Calculate exponent $E = -((1 - \alpha)^2 \times m) / 2$.
2. Calculate $P_{fail} = \exp(E)$.
3. Calculate $P_{success} = 1 - P_{fail}$.

### Limitations

- None, this is $O(1)$.

## Optimal Approach

### Key Insight

Direct implementation.

### Algorithm

1. Read $m, \alpha$.
2. Compute $val = (1.0 - \alpha)$.
3. Compute $exponent = -(val * val * m) / 2.0$.
4. Compute $p\_fail = \exp(exponent)$.
5. Print $1.0 - p\_fail$.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PDS-003/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-003/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public double successProbability(long m, double alpha) {
        double val = 1.0 - alpha;
        double exponent = -(val * val * m) / 2.0;
        double pFail = Math.exp(exponent);
        return 1.0 - pFail;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long m = sc.nextLong();
            double alpha = sc.nextDouble();

            Solution solution = new Solution();
            System.out.println(solution.successProbability(m, alpha));
        }
        sc.close();
    }
}
```

### Python

```python
import math
import sys

def success_probability(m: int, alpha: float) -> float:
    val = 1.0 - alpha
    exponent = -(val * val * m) / 2.0
    p_fail = math.exp(exponent)
    return 1.0 - p_fail

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = int(data[0])
    alpha = float(data[1])
    print(f"{success_probability(m, alpha):.6f}")

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
    double successProbability(long long m, double alpha) {
        double val = 1.0 - alpha;
        double exponent = -(val * val * (double)m) / 2.0;
        double pFail = exp(exponent);
        return 1.0 - pFail;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long m;
    double alpha;
    if (cin >> m >> alpha) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.successProbability(m, alpha) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function successProbability(m, alpha) {
  const val = 1.0 - alpha;
  const exponent = -(val * val * m) / 2.0;
  const pFail = Math.exp(exponent);
  return 1.0 - pFail;
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
  const alpha = parseFloat(data[1]);
  console.log(successProbability(m, alpha).toFixed(6));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `m=50, alpha=0.8`

1. $1 - \alpha = 0.2$.
2. $(0.2)^2 = 0.04$.
3. $0.04 \times 50 = 2.0$.
4. $2.0 / 2 = 1.0$.
5. Exponent = -1.0.
6. $P_{fail} = e^{-1} \approx 0.367879$.
7. $P_{success} = 1 - 0.367879 = 0.632121$.

Matches example.

![Example Visualization](../images/PDS-003/example-1.png)

## ✅ Proof of Correctness

### Invariant
The formula is a given approximation.

### Why the approach is correct
We correctly implement the mathematical expression provided.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** How to handle failure?
  - *Hint:* Rehash everything with new hash functions (Stash can also help).
- **Extension 2:** Load factor limit?
  - *Hint:* For 2 hash functions, theoretical limit is 50% ($\alpha < 0.5$). With 3 hash functions, it goes up to 91%.
- **Extension 3:** Why is lookup $O(1)$?
  - *Hint:* Check $H_1(x)$ and $H_2(x)$. If not there, it's not in the table. 2 checks always.

## Common Mistakes to Avoid

1. **Sign Error**
   - ❌ Wrong: `exp( (1-alpha)... )` (positive exponent).
   - ✅ Correct: `exp( - ... )`.
2. **Order of Operations**
   - ❌ Wrong: `1 - alpha^2`.
   - ✅ Correct: `(1 - alpha)^2`.

## Related Concepts

- **Random Graphs:** Erdős–Rényi model.
- **Bipartite Matching:** Cuckoo hashing is related to matching in bipartite graphs.
