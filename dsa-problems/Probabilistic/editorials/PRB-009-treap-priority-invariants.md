---
problem_id: PRB_TREAP_PRIORITY_INVARIANTS__7410
display_id: PRB-009
slug: treap-priority-invariants
title: "Treap Priority Invariants"
difficulty: Medium
difficulty_score: 52
topics:
  - Probability
  - Data Structures
  - Expected Value
tags:
  - probability
  - treap
  - expectation
  - medium
premium: true
subscription_tier: basic
---

# PRB-009: Treap Priority Invariants

## 📋 Problem Summary

Calculate the expected depth of a node and the expected total path length (sum of depths of all nodes) in a Treap with n nodes.

A Treap is a binary tree that is a BST by keys and a Heap by random priorities. The structure is isomorphic to a randomly built BST.

| | |
|---|---|
| **Formulas** | E[depth] = 2Hₙ - 2 <br> E[total path length] = 2(n+1)Hₙ - 4n |
| **Input** | n |
| **Output** | E[depth], E[path] |

## 🌍 Real-World Scenario

**Scenario Title:** The Self-Organizing Archive

You are designing a dynamic archive system where documents are added in random order.
- You use a **Treap** (Tree + Heap) to maintain the index.
- Unlike AVL or Red-Black trees which require complex rotations to balance, a Treap uses random priorities to achieve balance "on average".
- You want to predict the performance:
  - **Expected Depth:** Tells you the average time to find a specific document.
  - **Total Path Length:** Tells you the total cost to access every document once (e.g., for a full backup or audit).
- Knowing these expected values helps you provision the right amount of CPU and I/O throughput.

**Why This Problem Matters:**

- **Randomized Data Structures:** Understanding why randomness yields efficiency.
- **Algorithm Analysis:** Quicksort analysis is identical to Treap depth analysis.
- **System Design:** Predicting average latency vs worst-case latency.

![Real-World Application](../images/PRB-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Treap Structure

Keys: 1, 2, 3. Random Priorities: P(1)=10, P(2)=5, P(3)=20.
Heap Property (Max-Heap): Parent priority > Child priority.

```
      3 (P=20)
     /
    1 (P=10)
     \
      2 (P=5)
```

- Root is max priority (3).
- Left child of 3 is {1, 2}. Max priority in {1, 2} is 1.
- Right child of 1 is {2}.
- Structure is unique given priorities.
- With random priorities, the tree shape is random.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Harmonic Number:** $H_n = \sum_{i=1}^n \frac{1}{i}$.
- **Formulas:**
  - $E[\text{depth}]$ usually refers to the average depth of a node chosen uniformly at random, or the expected depth of the *last* inserted node?
  - The problem statement says "Expected depth of a node: $2H_n - 2$". This matches the expected depth of a specific node (like the root of the equivalent random BST? No, root depth is 0).
  -   - Let's check the example. N = 4$. $H_4 \approx 2.0833$.
  - $E_{depth} = 2(2.0833) - 2 = 4.1666 - 2 = 2.1666$.
  - This matches the example output.
  - $E_{path} = 2(5)(2.0833) - 16 = 20.833 - 16 = 4.8333$.
  - Matches example.
- **Constraints:** n \le 10^6$. O(n) calculation is fine.

### Core Concept: Harmonic Numbers

The Harmonic number $H_n$ grows as $\ln n + \gamma$ (Euler-Mascheroni constant).
It appears in many randomized algorithms (Coupon Collector, Quicksort).
We compute it iteratively.

## Naive Approach

### Intuition

Simulate many Treaps.

### Algorithm

Monte Carlo.

### Time Complexity

- **O(Trials \cdot n \log n)**. Too slow.

## Optimal Approach

### Key Insight

Direct implementation of the formulas.
Compute $H_n$ in a loop.

### Algorithm

1. Initialize `H = 0.0`.
2. Loop `i` from 1 to `n`: `H += 1.0 / i`.
3. `E_depth = 2 * H - 2`.
4. `E_path = 2 * (n + 1) * H - 4 * n`.
5. Print results.

### Time Complexity

- **O(n)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/PRB-009/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-009/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public double[] treapExpectations(int n) {
        double H = 0.0;
        for (int i = 1; i <= n; i++) {
            H += 1.0 / i;
        }
        
        double eDepth = 2 * H - 2;
        // Note: For n=1, H=1, E_depth = 0. Correct.
        //         // If n=0? Loop doesn't run, H=0. E_depth = -2. 
        // Problem constraints n >= 1.
        
        double ePath = 2 * (n + 1) * H - 4 * n;
        
        return new double[]{eDepth, ePath};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Solution solution = new Solution();
            double[] res = solution.treapExpectations(n);
            System.out.printf("%.6f %.6f\n", res[0], res[1]);
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def treap_expectations(n: int):
    H = 0.0
    for i in range(1, n + 1):
        H += 1.0 / i
        
    e_depth = 2 * H - 2
    e_path = 2 * (n + 1) * H - 4 * n
    
    return e_depth, e_path

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    d, p = treap_expectations(n)
    print(f"{d:.6f} {p:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

class Solution {
public:
    pair<double, double> treapExpectations(int n) {
        double H = 0.0;
        for (int i = 1; i <= n; i++) {
            H += 1.0 / i;
        }
        
        double eDepth = 2 * H - 2;
        double ePath = 2 * (n + 1) * H - 4 * n;
        
        return {eDepth, ePath};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        Solution solution;
        auto res = solution.treapExpectations(n);
        cout << fixed << setprecision(6) << res.first << " " << res.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function treapExpectations(n) {
  let H = 0.0;
  for (let i = 1; i <= n; i++) {
    H += 1.0 / i;
  }
  
  const eDepth = 2 * H - 2;
  const ePath = 2 * (n + 1) * H - 4 * n;
  
  return [eDepth, ePath];
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
  const res = treapExpectations(n);
  console.log(res[0].toFixed(6) + " " + res[1].toFixed(6));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `4`.
1. H = 1 + 0.5 + 0.333 + 0.25 = 2.083333$.
2. $E_{depth} = 2(2.083333) - 2 = 2.166667$.
3. $E_{path} = 2(5)(2.083333) - 16 = 20.83333 - 16 = 4.83333$.
Matches example.

## ✅ Proof of Correctness

### Invariant
The formulas are standard results for Random Binary Search Trees (RBST).
A Treap with random priorities is isomorphic to an RBST.

### Why the approach is correct
Direct implementation of derived expectations.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Variance of depth.
  - *Hint:* $Var \approx 2 \ln n$.
- **Extension 2:** Max depth (Height).
  - *Hint:* $E[Height] \approx 4.311 \ln n$.
- **Extension 3:** Split/Merge complexity.
  - *Hint:* O(\log n) expected.

## Common Mistakes to Avoid

1. **Integer Division**
   - ❌ Wrong: `1/i` in C++/Java.
   - ✅ Correct: `1.0/i`.
2. **Formula Application**
   - ❌ Wrong: Mixing up n and $n+1$.
   - ✅ Correct: Follow the problem statement exactly.

## Related Concepts

- **Quicksort:** Comparisons ≈ 2n \ln n$.
- **Cartesian Trees:** Deterministic version of Treap logic.
