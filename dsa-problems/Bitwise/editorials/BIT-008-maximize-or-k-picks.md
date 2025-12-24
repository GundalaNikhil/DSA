---
problem_id: BIT_MAXIMIZE_OR_K_PICKS__8408
display_id: BIT-008
slug: maximize-or-k-picks
title: "Maximize OR With K Picks"
difficulty: Medium
difficulty_score: 48
topics:
  - Bitwise Operations
  - OR
  - Greedy
  - Array
tags:
  - bitwise
  - or-operation
  - greedy
  - optimization
  - medium
premium: true
subscription_tier: basic
---

# BIT-008: Maximize OR With K Picks

## 📋 Problem Summary

Select exactly `k` integers from an array such that their bitwise OR sum is maximized.

## 🌍 Real-World Scenario

**Scenario Title:** The Feature Bundle Optimization

You are assembling a software bundle.
- **Modules**: You have a library of `n` modules. Each module enables a specific set of features (represented by bits).
- **License**: Your license allows you to include exactly `k` modules in the standard edition.
- **Goal**: You want to offer the most feature-rich standard edition possible ( maximize the total set of unique features enabled).
- **Logic**: Since features don't conflict (OR logic), you just want to pick the `k` modules that cover the most high-value feature bits.

**Why This Problem Matters:**

- **Set Cover**: A simplified variation where "elements" (bits) have strictly hierarchical weights ($2^i$).
- **Greedy Validity**: Understanding when greedy choices are globally optimal.
- **Dimensionality**: Leveraging the small count of bits (30-60) vs large N.

![Real-World Application](../images/BIT-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Greedy Choice
```
Array: [100, 010, 001] (Binary)
K = 2

Pass 1:
- Current: 000
- Try 100 -> 100 (Gain 4)
- Try 010 -> 010 (Gain 2)
- Try 001 -> 001 (Gain 1)
- Pick 100. New Mask: 100.

Pass 2:
- Current: 100
- Try 010 -> 110 (Gain 2)
- Try 001 -> 101 (Gain 1)
- Pick 010. New Mask: 110.

Result: 110 (6).
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Integer array `a` and `k`.
- **Duplicates**: You can pick duplicates if useful (but `x | x = x`, so usually useless). Distinct indices matter.
- **Constraints**: `a[i]` up to `10^9` (30 bits).

Common interpretation mistake:

- ❌ Trying Dynamic Programming. The state space (index, currentOR) is too large.
- ✅ Using Greedy. Since bit `i` is worth more than the sum of all bits `0` to `i-1`, we always prioritize setting higher bits.

### Core Concept: Hierarchical Greedy

The value of the MSB ($2^{29}$) is greater than the sum of all lower bits ($2^{29}-1$). This simple arithmetic property means we never sacrifice a higher bit to gain lower bits.
Therefore, the strategy "Pick the number that adds the most value to the current OR" is optimal.

### Why K Threshold Matters

Since there are only ~30 bits, we can saturate the max possible OR of the array with at most 30 picks (one per bit). If `k >= 30`, we can just pick the minimal set to get `TotalOR` and fill the rest with garbage. Effectively, if `k >= 30`, answer is `OR(All)`.

## Naive Approach (Backtracking)

### Intuition

Try all combinations of size `k`.

### Algorithm

1. Recursively select element.
2. Maximize result.

### Time Complexity

- **O(C(N, K))**. Exponential.

### Space Complexity

- **O(K)** recursion.

## Optimal Approach (Greedy Scan)

### Key Insight

In each step, pick the element `x` that maximizes `CurrentOR | x`.
Repeat `k` times.

### Algorithm

1. `current_or = 0`.
2. `used = boolean array`.
3. Loop `step` from 0 to `k-1`:
   - `best_val = -1`, `best_idx = -1`.
   - Loop `i` from 0 to `n-1`:
     - If `!used[i]`:
       - `new_or = current_or | a[i]`.
       - If `new_or > best_val`: `best_val = new_or`, `best_idx = i`.
   - If `best_idx` valid:
     - `current_or = best_val`.
     - `used[best_idx] = true`.
   - Else: Break (no more numbers? Not possible if k <= n).
4. Return `current_or`.

Optimization: If `k > 30`, just return `OR` of the whole array array (linear scan), because 30 picks is enough to set all 30 bits.

### Time Complexity

- **O(min(K, 30) * N)**. Since we cap K at 30, it is **O(N)**.

### Space Complexity

- **O(N)** for used flags.

![Algorithm Visualization](../images/BIT-008/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-008/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long maximizeOrWithKPicks(int[] a, int k) {
        int n = a.length;
        // Optimization: 30 bits max. If k >= 30, we can collect all bits.
        if (k >= 30) {
            long totalOr = 0;
            for (int x : a) totalOr |= x;
            return totalOr;
        }

        long currentOr = 0;
        boolean[] used = new boolean[n];

        for (int step = 0; step < k; step++) {
            long bestOr = -1;
            int bestIdx = -1;

            for (int i = 0; i < n; i++) {
                if (!used[i]) {
                    long newOr = currentOr | a[i];
                    if (newOr > bestOr) {
                        bestOr = newOr;
                        bestIdx = i;
                    }
                }
            }

            if (bestIdx != -1) {
                currentOr = bestOr;
                used[bestIdx] = true;
            }
        }
        return currentOr;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int k = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.maximizeOrWithKPicks(a, k));
        sc.close();
    }
}
```

### Python

```python
import sys

def maximize_or_with_k_picks(a: list[int], k: int) -> int:
    n = len(a)
    # Optimization: If K is large enough, we can set all possible bits
    if k >= 30:
        total = 0
        for x in a:
            total |= x
        return total
        
    current_or = 0
    used = [False] * n
    
    for _ in range(k):
        best_or = -1
        best_idx = -1
        
        for i in range(n):
            if not used[i]:
                new_or = current_or | a[i]
                if new_or > best_or:
                    best_or = new_or
                    best_idx = i
                    
        # If we found something (which we always should if k <= n)
        if best_idx != -1:
            current_or = best_or
            used[best_idx] = True
            
    return current_or

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
    
    k = int(data[ptr]); ptr += 1
    
    result = maximize_or_with_k_picks(a, k)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

class Solution {
public:
    long long maximizeOrWithKPicks(vector<int>& a, int k) {
        int n = a.size();
        if (k >= 30) {
            long long total = 0;
            for (int x : a) total |= x;
            return total;
        }
        
        long long currentOr = 0;
        vector<bool> used(n, false);
        
        for (int step = 0; step < k; step++) {
            long long bestOr = -1;
            int bestIdx = -1;
            
            for (int i = 0; i < n; i++) {
                if (!used[i]) {
                    long long newOr = currentOr | a[i];
                    if (newOr > bestOr) {
                        bestOr = newOr;
                        bestIdx = i;
                    }
                }
            }
            
            if (bestIdx != -1) {
                currentOr = bestOr;
                used[bestIdx] = true;
            }
        }
        return currentOr;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int k;
    cin >> k;

    Solution solution;
    cout << solution.maximizeOrWithKPicks(a, k) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maximizeOrWithKPicks(a, k) {
    const n = a.length;
    
    if (k >= 30) {
      let total = 0n;
      for (const x of a) total |= BigInt(x);
      return total.toString();
    }
    
    let currentOr = 0n;
    const used = new Uint8Array(n);
    
    for (let step = 0; step < k; step++) {
      let bestOr = -1n;
      let bestIdx = -1;
      
      for (let i = 0; i < n; i++) {
        if (used[i] === 0) {
          const val = BigInt(a[i]);
          const newOr = currentOr | val;
          if (newOr > bestOr) {
            bestOr = newOr;
            bestIdx = i;
          }
        }
      }
      
      if (bestIdx !== -1) {
        currentOr = bestOr;
        used[bestIdx] = 1;
      }
    }
    
    return currentOr.toString();
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
    if (data.length === 0) return;
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const a = [];
    for (let i = 0; i < n; i++) a.push(Number(tokens[ptr++]));
    const k = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(solution.maximizeOrWithKPicks(a, k));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `a=[1, 2, 4], k=2`.
1. **Pass 1**:
   - `0 | 1 = 1`
   - `0 | 2 = 2`
   - `0 | 4 = 4` -> Max. Pick 4. `current = 4`.
2. **Pass 2**:
   - `4 | 1 = 5`
   - `4 | 2 = 6` -> Max. Pick 2. `current = 6`.
Result: 6.

## ✅ Proof of Correctness

### Invariant

The greedy strategy works because the bitwise OR function with the canonical bit weights ($2^i$) satisfies the matroid property where the lexicographically largest (value-wise largest) element/set is an optimal basis. Specifically, priority to MSB is never wrong.

## 💡 Interview Extensions (High-Value Add-ons)

- **Subset Sum**: Much harder (NP-complete).
- **XOR Sum**: Requires Linear Basis (Gaussian Elimination).

## Common Mistakes to Avoid

1. **Greedy Trap**:
   - ❌ This greedy works for OR. It does NOT work for Sum or XOR generally (though XOR basis is greedy-like).
2. **Sort**:
   - ❌ Sorting array descending helps heuristic but doesn't change complexity O(NK).

## Related Concepts

- **Set Cover Problem**: General case.
- **Maximum AND**: Usually involves iterating bits from MSB.
