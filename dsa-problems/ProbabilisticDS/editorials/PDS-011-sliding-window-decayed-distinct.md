---
problem_id: PDS_SLIDING_WINDOW_DECAYED_DISTINCT__5072
display_id: PDS-011
slug: sliding-window-decayed-distinct
title: "Sliding Window Distinct with Exponential Decay"
difficulty: Medium
difficulty_score: 56
topics:
  - Probabilistic Data Structures
  - Sliding Window
  - Decay
tags:
  - probabilistic-ds
  - sliding-window
  - decay
  - medium
premium: true
subscription_tier: basic
---

# PDS-011: Sliding Window Distinct with Exponential Decay

## 📋 Problem Summary

We need to compute a "decayed" count of distinct elements.
- Each distinct element $i$ contributes a weight based on how recently it was seen.
- If the last time we saw item $i$ was $t_i$, its contribution at current time $T$ is $e^{-\lambda(T - t_i)}$.
- The total estimate is the sum of these contributions for all distinct items.
- We are given the set of last-seen timestamps for all distinct items.

## 🌍 Real-World Scenario

**Scenario Title:** Trending Topic Detection

Imagine you are Twitter or Reddit.
- You want to know "how many people are talking about this topic *right now*?"
- A simple distinct count over all time is useless (it never decreases).
- A distinct count over the last 24 hours is better, but has a hard cutoff.
- **Exponential Decay** gives a smooth, continuous measure of "current popularity".
- A user who posted 1 minute ago counts as $\approx 1.0$.
- A user who posted 1 hour ago counts as $\approx 0.5$ (depending on $\lambda$).
- This metric reacts instantly to spikes and gradually fades out old activity.

**Why This Problem Matters:**

- **Rate Limiting:** Leaky bucket algorithms often use exponential decay.
- **Cache Eviction:** Least Recently Used (LRU) approximations.
- **Online Learning:** Forgetting old data to adapt to concept drift.

![Real-World Application](../images/PDS-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Decay Function

Time $T=10$. $\lambda=0.1$.

Item A: Last seen $t=10$. Age=0. Weight = $e^0 = 1.0$.
Item B: Last seen $t=8$. Age=2. Weight = $e^{-0.2} \approx 0.818$.
Item C: Last seen $t=0$. Age=10. Weight = $e^{-1.0} \approx 0.368$.

Total Score = $1.0 + 0.818 + 0.368 = 2.186$.

Graph of Weight vs Age:
```
Weight
1.0 | *
    |  *
0.5 |    *
    |       *
0.0 |___________*____
    0   5   10  Age
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:**
  - $T$: Current time.
  - $\lambda$: Decay rate.
  - Times: List of timestamps $t_i$ (one per distinct item).
- **Output:** Sum of weights.
- **Formula:** $\sum e^{-\lambda(T - t_i)}$.

## Naive Approach

### Intuition

Iterate and sum.

### Algorithm

1. `sum = 0`.
2. For each `t` in `times`:
   - `sum += exp(-lambda * (T - t))`.
3. Return `sum`.

### Limitations

- None.

## Optimal Approach

### Key Insight

Direct implementation.

### Algorithm

1. Read inputs.
2. Initialize `total = 0.0`.
3. For each timestamp `t`:
   - `total += exp(-lambda * (T - t))`.
4. Print `total`.

### Time Complexity

- **O(m)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PDS-011/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-011/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public double decayedDistinct(int T, double lambda, int[] times) {
        double sum = 0.0;
        for (int t : times) {
            sum += Math.exp(-lambda * (T - t));
        }
        return sum;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int T = sc.nextInt();
            double lambda = sc.nextDouble();
            int m = sc.nextInt();
            int[] times = new int[m];
            for (int i = 0; i < m; i++) times[i] = sc.nextInt();
    
            Solution solution = new Solution();
            System.out.println(solution.decayedDistinct(T, lambda, times));
        }
        sc.close();
    }
}
```

### Python

```python
import math
import sys

def decayed_distinct(T: int, lam: float, times):
    total = 0.0
    for t in times:
        total += math.exp(-lam * (T - t))
    return total

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        T = int(next(iterator))
        lam = float(next(iterator))
        m = int(next(iterator))
        times = []
        for _ in range(m):
            times.append(int(next(iterator)))
            
        print(f"{decayed_distinct(T, lam, times):.6f}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double decayedDistinct(int T, double lambda, const vector<int>& times) {
        double sum = 0.0;
        for (int t : times) {
            sum += exp(-lambda * (T - t));
        }
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, m;
    double lambda;
    if (cin >> T >> lambda >> m) {
        vector<int> times(m);
        for (int i = 0; i < m; i++) cin >> times[i];
    
        Solution solution;
        cout << fixed << setprecision(6) << solution.decayedDistinct(T, lambda, times) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function decayedDistinct(T, lambda, times) {
  let sum = 0.0;
  for (const t of times) {
    sum += Math.exp(-lambda * (T - t));
  }
  return sum;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const T = parseInt(data[idx++], 10);
  const lambda = parseFloat(data[idx++]);
  const m = parseInt(data[idx++], 10);
  const times = [];
  for (let i = 0; i < m; i++) times.push(parseInt(data[idx++], 10));
  console.log(decayedDistinct(T, lambda, times).toFixed(6));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input:
`10 0.1 3`
`10 8 5`

1. $T=10, \lambda=0.1$.
2. $t=10$: $e^{-0.1(0)} = e^0 = 1.0$.
3. $t=8$: $e^{-0.1(2)} = e^{-0.2} \approx 0.81873$.
4. $t=5$: $e^{-0.1(5)} = e^{-0.5} \approx 0.60653$.
5. Sum: $1.0 + 0.81873 + 0.60653 = 2.42526$.

Output: `2.425261`. Matches example.

![Example Visualization](../images/PDS-011/example-1.png)

## ✅ Proof of Correctness

### Invariant
The sum of exponentials correctly models the decayed cardinality.

### Why the approach is correct
Direct application of the definition.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** How to maintain this online?
  - *Hint:* When time advances by $\Delta t$, multiply the entire sum by $e^{-\lambda \Delta t}$. When a new item arrives, add 1.
- **Extension 2:** What if we don't store all timestamps?
  - *Hint:* Use a sketch (like HLL) combined with decay.

## Common Mistakes to Avoid

1. **Sign Error**
   - ❌ Wrong: `exp(lambda * ...)` (growth instead of decay).
   - ✅ Correct: `exp(-lambda * ...)`.
2. **Order of Subtraction**
   - ❌ Wrong: `t - T` (negative age, positive exponent).
   - ✅ Correct: `T - t` (positive age, negative exponent).

## Related Concepts

- **Exponential Moving Average (EMA):** Similar concept for averages.
- **Time-Decayed HLL:** Advanced probabilistic structure.
