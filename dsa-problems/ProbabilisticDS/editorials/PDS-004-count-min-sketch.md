---
problem_id: PDS_COUNT_MIN_SKETCH__4815
display_id: PDS-004
slug: count-min-sketch
title: "Count-Min Sketch Error Bound"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - Sketches
  - Error Bounds
tags:
  - probabilistic-ds
  - sketch
  - error-bound
  - medium
premium: true
subscription_tier: basic
---

# PDS-004: Count-Min Sketch Error Bound

## 📋 Problem Summary

We need to calculate the dimensions of a Count-Min Sketch (width $w$ and depth $d$) to satisfy specific error guarantees.
- **Goal:** Estimate the frequency of items in a stream.
- **Guarantee:** With probability at least $1 - \delta$, the estimated count $\hat{c}_x$ satisfies $c_x \le \hat{c}_x \le c_x + \epsilon N$, where $N$ is the total number of items in the stream.
- **Formulas:**
  - $w = \lceil e / \epsilon \rceil$
  - $d = \lceil \ln(1/\delta) \rceil$

## 🌍 Real-World Scenario

**Scenario Title:** Trending Hashtags on Twitter

Imagine you want to track the most popular hashtags on Twitter in real-time.
- There are millions of unique hashtags (high cardinality).
- You can't store a counter for every single hashtag (too much RAM).
- You are okay with a small error. If a hashtag appears 100 times, you might count it as 105, but never 99.
- You want to be 99% sure that your count is not off by more than 0.1% of the total stream size.
- **Count-Min Sketch** allows you to do this using a fixed-size 2D array of counters, drastically reducing memory usage compared to a HashMap.

**Why This Problem Matters:**

- **Network Traffic Analysis:** Identifying "heavy hitters" (IPs sending too much traffic).
- **Natural Language Processing:** Estimating word frequencies in huge corpora (Google n-grams).
- **Database Query Optimization:** Estimating selectivity of queries.

![Real-World Application](../images/PDS-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Count-Min Sketch Structure

Structure is a 2D array `count[d][w]`.
$d$ rows (hash functions), $w$ columns (buckets).

```
Stream: "A", "B", "A", "C"

Hash functions:
h1("A") = 1, h2("A") = 3
h1("B") = 0, h2("B") = 3
h1("C") = 2, h2("C") = 1

Update "A":
Row 1: [0, 1, 0, 0]  (Inc index 1)
Row 2: [0, 0, 0, 1]  (Inc index 3)

Query "A":
Min(Row1[1], Row2[3])
```

- **Width ($w$):** Controls the magnitude of the error ($\epsilon$). Wider table = less collisions = less error.
- **Depth ($d$):** Controls the confidence ($1-\delta$). More rows = lower chance that *all* hash functions collide with heavy hitters.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Inputs:**
  - $\epsilon$ (epsilon): Error factor (e.g., 0.01).
  - $\delta$ (delta): Failure probability (e.g., 0.01).
- **Outputs:**
  - $w$: Number of columns.
  - $d$: Number of rows.
- **Constants:** $e \approx 2.71828$.

## Naive Approach

### Intuition

Just implement the formulas.

### Algorithm

1. $w = \lceil e / \epsilon \rceil$.
2. $d = \lceil \ln(1 / \delta) \rceil$.

### Limitations

- None.

## Optimal Approach

### Key Insight

Direct formula application.

### Algorithm

1. Read $\epsilon, \delta$.
2. $w = \text{ceil}(\exp(1.0) / \epsilon)$.
3. $d = \text{ceil}(\log(1.0 / \delta))$.
4. Print $w, d$.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PDS-004/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-004/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long[] cmsParams(double epsilon, double delta) {
        long w = (long) Math.ceil(Math.E / epsilon);
        long d = (long) Math.ceil(Math.log(1.0 / delta));
        return new long[]{w, d};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextDouble()) {
            double epsilon = sc.nextDouble();
            double delta = sc.nextDouble();

            Solution solution = new Solution();
            long[] res = solution.cmsParams(epsilon, delta);
            System.out.println(res[0] + " " + res[1]);
        }
        sc.close();
    }
}
```

### Python

```python
import math
import sys

def cms_params(epsilon: float, delta: float):
    w = math.ceil(math.e / epsilon)
    d = math.ceil(math.log(1.0 / delta))
    return w, d

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    epsilon = float(data[0])
    delta = float(data[1])
    w, d = cms_params(epsilon, delta)
    print(f"{w} {d}")

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
    pair<long long, long long> cmsParams(double epsilon, double delta) {
        long long w = (long long) ceil(exp(1.0) / epsilon);
        long long d = (long long) ceil(log(1.0 / delta));
        return {w, d};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double epsilon, delta;
    if (cin >> epsilon >> delta) {
        Solution solution;
        auto res = solution.cmsParams(epsilon, delta);
        cout << res.first << " " << res.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function cmsParams(epsilon, delta) {
  const w = Math.ceil(Math.E / epsilon);
  const d = Math.ceil(Math.log(1.0 / delta));
  return [w, d];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const epsilon = parseFloat(data[0]);
  const delta = parseFloat(data[1]);
  const res = cmsParams(epsilon, delta);
  console.log(res[0] + " " + res[1]);
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `0.01 0.01`

1. $w = \lceil 2.71828 / 0.01 \rceil = \lceil 271.828 \rceil = 272$.
2. $d = \lceil \ln(100) \rceil = \lceil 4.605 \rceil = 5$.

Output: `272 5`. Matches example.

![Example Visualization](../images/PDS-004/example-1.png)

## ✅ Proof of Correctness

### Invariant
The formulas are derived from Markov's Inequality.

### Why the approach is correct
Standard theoretical bounds for Count-Min Sketch.
- Error in one row is $N/w$ with prob $1/e$.
- Probability that *all* $d$ rows have error $> N/w$ is $(1/e)^d \le \delta$.
- Setting $w = e/\epsilon$ ensures error is $\epsilon N$.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Count-Mean-Min Sketch?
  - *Hint:* Subtract estimated noise to reduce bias.
- **Extension 2:** Heavy Hitters?
  - *Hint:* Use a heap alongside the sketch to track top-k elements.
- **Extension 3:** Deletions?
  - *Hint:* CMS supports deletions (decrement counters), but error bounds become trickier if counts go negative (usually assumed non-negative).

## Common Mistakes to Avoid

1. **Log Base**
   - ❌ Wrong: `log10`.
   - ✅ Correct: `ln` (natural log).
2. **Ceiling**
   - ❌ Wrong: Casting to int/long directly (truncates).
   - ✅ Correct: `Math.ceil()`.

## Related Concepts

- **Bloom Filter:** Set membership (binary).
- **HyperLogLog:** Cardinality estimation.
- **Reservoir Sampling:** Random sampling.
