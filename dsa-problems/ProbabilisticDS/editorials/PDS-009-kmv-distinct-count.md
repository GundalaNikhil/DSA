---
problem_id: PDS_KMV_DISTINCT_COUNT__9186
display_id: PDS-009
slug: kmv-distinct-count
title: "k-Minimum Values (KMV) Distinct Count"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - KMV
  - Distinct Count
tags:
  - probabilistic-ds
  - kmv
  - distinct-count
  - medium
premium: true
subscription_tier: basic
---

# PDS-009: k-Minimum Values (KMV) Distinct Count

## 📋 Problem Summary

We are given the $k$ smallest hash values from a set of items, where hash values are uniformly distributed in $(0, 1)$. We need to estimate the total number of distinct elements in the original set using the KMV estimator: $\text{Estimate} = \frac{k-1}{h_k}$, where $h_k$ is the $k$-th smallest hash value.

## 🌍 Real-World Scenario

**Scenario Title:** Distributed Database Query Optimization

Imagine a distributed database like Cassandra or DynamoDB.
- Data is sharded across hundreds of nodes.
- You want to run `SELECT COUNT(DISTINCT user_id) FROM users`.
- Querying every shard and merging full sets of user IDs is extremely slow and network-heavy.
- **KMV Solution:** Each shard maintains just the $k$ smallest hash values of the user IDs it sees.
- The coordinator node collects these small lists, merges them to find the global $k$ smallest hashes, and applies the KMV formula.
- This allows estimating the global distinct count with minimal data transfer.

**Why This Problem Matters:**

- **Set Operations:** KMV sketches allow estimating intersection and union sizes (Jaccard similarity).
- **Data Warehousing:** Pre-computing statistics for query planning.

![Real-World Application](../images/PDS-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Hash Space

Hash values are points on the line $(0, 1)$.
If we have $N$ distinct items, their hashes will be roughly evenly spaced with gap $1/N$.
The $k$-th smallest hash $h_k$ should be roughly at position $k/N$.

```
0.0   h1    h2        h3 (k=3)                                  1.0
|-----|-----|---------|------------------------------------------|
      ^     ^         ^
    Items mapped to (0,1)
```

If $h_k \approx k/N$, then $N \approx k/h_k$.
The unbiased estimator uses $k-1$ instead of $k$: $N \approx (k-1)/h_k$.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:**
  - $k$: Number of smallest hashes provided.
  - Hashes: List of $k$ floats, sorted.
- **Output:** Estimated count.
- **Formula:** $(k-1) / \text{hashes}[k-1]$. (Note: 0-based index of $k$-th item is $k-1$).

## Naive Approach

### Intuition

Implement formula.

### Algorithm

1. Get $h_k$ (last element of input).
2. Compute $(k-1) / h_k$.

### Limitations

- None.

## Optimal Approach

### Key Insight

Direct formula.

### Algorithm

1. Read $k$ and hashes.
2. $h_k = \text{hashes}[k-1]$.
3. Result = $(k-1) / h_k$.
4. Print result.

### Time Complexity

- **O(1)** (after reading input).

### Space Complexity

- **O(1)** (ignoring input storage).

![Algorithm Visualization](../images/PDS-009/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-009/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public double kmvEstimate(double[] hashes) {
        int k = hashes.length;
        if (k == 0) return 0.0;
        double hk = hashes[k-1];
        return (k - 1) / hk;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            double[] hashes = new double[k];
            for (int i = 0; i < k; i++) hashes[i] = sc.nextDouble();
    
            Solution solution = new Solution();
            System.out.println(solution.kmvEstimate(hashes));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def kmv_estimate(hashes):
    k = len(hashes)
    if k == 0:
        return 0.0
    hk = hashes[-1]
    return (k - 1) / hk

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        hashes = []
        for _ in range(k):
            hashes.append(float(next(iterator)))
            
        print(f"{kmv_estimate(hashes):.6f}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

class Solution {
public:
    double kmvEstimate(const vector<double>& hashes) {
        int k = hashes.size();
        if (k == 0) return 0.0;
        double hk = hashes.back();
        return (double)(k - 1) / hk;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (cin >> k) {
        vector<double> hashes(k);
        for (int i = 0; i < k; i++) cin >> hashes[i];
    
        Solution solution;
        cout << fixed << setprecision(6) << solution.kmvEstimate(hashes) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function kmvEstimate(hashes) {
  const k = hashes.length;
  if (k === 0) return 0.0;
  const hk = hashes[k-1];
  return (k - 1) / hk;
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
  const k = parseInt(data[idx++], 10);
  const hashes = [];
  for (let i = 0; i < k; i++) hashes.push(parseFloat(data[idx++]));
  console.log(kmvEstimate(hashes).toFixed(6));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input:
`3`
`0.1 0.2 0.4`

1. $k=3$.
2. $h_k = 0.4$.
3. Estimate = $(3-1) / 0.4 = 2 / 0.4 = 5.0$.

Output: `5.0`. Matches example.

![Example Visualization](../images/PDS-009/example-1.png)

## ✅ Proof of Correctness

### Invariant
The $k$-th order statistic of $N$ uniform random variables on $(0,1)$ follows a Beta distribution with expected value $k/(N+1)$.
So $E[h_k] \approx k/N \implies N \approx k/h_k$.
The bias-corrected version is $(k-1)/h_k$.

### Why the approach is correct
Standard KMV estimator.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Merging KMV sketches?
  - *Hint:* Take the union of the two lists of hashes, sort them, and keep the smallest $k$.
- **Extension 2:** Jaccard Similarity?
  - *Hint:* $|A \cap B| / |A \cup B| \approx \frac{|S_A \cap S_B|}{|S_A \cup S_B|}$ where $S$ are the KMV sets.

## Common Mistakes to Avoid

1. **Index Error**
   - ❌ Wrong: Using `hashes[k]` (out of bounds).
   - ✅ Correct: `hashes[k-1]`.
2. **Formula Error**
   - ❌ Wrong: `k / hk` (biased).
   - ✅ Correct: `(k-1) / hk`.

## Related Concepts

- **HyperLogLog:** Another distinct count estimator (more space efficient).
- **Order Statistics:** Statistical properties of sorted random samples.
