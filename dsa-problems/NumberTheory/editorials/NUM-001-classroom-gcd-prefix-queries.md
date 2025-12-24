---
problem_id: NUM_CLASSROOM_GCD_PREFIX_QUERIES__4821
display_id: NUM-001
slug: classroom-gcd-prefix-queries
title: "Classroom GCD Prefix Queries"
difficulty: Easy
difficulty_score: 25
topics:
  - Number Theory
  - GCD
  - Prefix Computation
tags:
  - number-theory
  - gcd
  - prefix
  - easy
premium: true
subscription_tier: basic
---

# NUM-001: Classroom GCD Prefix Queries

## 📋 Problem Summary

Given an array of numbers, efficiently answer multiple queries asking for the Greatest Common Divisor (GCD) of the prefix ending at index `r`.
- Input: Array `A`, multiple queries `r`.
- Output: `GCD(A[0], A[1], dots, A[r])` for each query.

## 🌍 Real-World Scenario

**Scenario Title:** The Supply Distributor

Imagine you are a logistics manager for a school district. You have a sequence of classrooms, and each classroom needs a certain number of identical supply kits (e.g., 12 notebooks, 18 pencils, 6 erasers).
- You want to package these supplies into standard boxes such that every classroom receives an integer number of boxes.
- The number of items in a box must divide the requirement of every classroom in the group you are serving.
- To maximize efficiency, you want the largest possible box size (GCD).
- As you add more classrooms to your delivery route (extending the prefix), the box size might need to shrink to accommodate the new requirements. You need to quickly know the optimal box size for the first `r` classrooms.

**Why This Problem Matters:**

- **Cryptography:** GCD is fundamental to RSA and other encryption algorithms.
- **Data Compression:** Finding common patterns or periods in data streams.
- **Resource Allocation:** Distributing resources fairly in discrete chunks.

![Real-World Application](../images/NUM-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Prefix GCD

Consider array: `[12, 18, 6, 8]`

```
Index: 0   1   2   3
Value: 12  18  6   8

Prefix GCDs:
P[0] = gcd(12) = 12
P[1] = gcd(12, 18) = 6
P[2] = gcd(6, 6) = 6
P[3] = gcd(6, 8) = 2
```

Notice that the prefix GCD is **non-increasing**. It can only stay the same or decrease as we include more numbers.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** `N, Q <= 200,000`. This means an `O(N * Q)` solution will time out. We need `O(N)` precomputation and `O(1)` per query.
- **Values:** Integers can be negative. GCD is always positive. `gcd(a, b) = gcd(|a|, |b|)`.
- **Zero:** `gcd(x, 0) = |x|`. `gcd(0, 0) = 0`.

### Core Concept: Prefix Array

Just like a prefix sum array allows `O(1)` range sum queries, a prefix GCD array allows `O(1)` prefix GCD queries.
`P[i] = gcd(P[i-1], A[i])`.

## Naive Approach

### Intuition

For each query `r`, iterate from `0` to `r` and compute the GCD.

### Algorithm

```python
for r in queries:
    g = a[0]
    for i in range(1, r + 1):
        g = gcd(g, a[i])
    print(g)
```

### Time Complexity

- **O(Q \cdot N \cdot \log(\text{max\_val}))**.
- With `N, Q = 2 * 10^5`, this is roughly `4 * 10^10` operations, which is way too slow (limit is usually `10^8`).

### Space Complexity

- **O(1)** (excluding input).

## Optimal Approach

### Key Insight

Since the queries are always about prefixes `A[0 dots r]`, we can precompute the answers.
Define `prefix_gcd[i]` as the GCD of all elements from index 0 to `i`.
`prefix_gcd[i] = gcd(prefix_gcd[i-1], A[i])`.

### Algorithm

1. Create an array `pref` of size `N`.
2. Set `pref[0] = abs(A[0])`.
3. Iterate `i` from 1 to `N-1`:
   - `pref[i] = gcd(pref[i-1], abs(A[i]))`.
4. For each query `r`, return `pref[r]`.

### Time Complexity

- **Precomputation:** `O(N * log(max_val))`.
- **Query:** `O(1)`.
- **Total:** `O((N + Q) * log(max_val))`. This fits easily within 2 seconds.

### Space Complexity

- **O(N)** to store the prefix array.

![Algorithm Visualization](../images/NUM-001/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-001/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public int[] prefixGcds(int[] a) {
        int n = a.length;
        if (n == 0) return new int[0];
        
        int[] pref = new int[n];
        pref[0] = Math.abs(a[0]);
        
        for (int i = 1; i < n; i++) {
            pref[i] = gcd(pref[i - 1], Math.abs(a[i]));
        }
        
        return pref;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] pref = solution.prefixGcds(a);
        
        for (int i = 0; i < q; i++) {
            int r = sc.nextInt();
            System.out.println(pref[r]);
        }
        sc.close();
    }
}
```

### Python

```python
import sys
from math import gcd
from typing import List

def prefix_gcds(a: List[int]) -> List[int]:
    if not a:
        return []
    
    n = len(a)
    pref = [0] * n
    pref[0] = abs(a[0])
    
    for i in range(1, n):
        pref[i] = gcd(pref[i-1], abs(a[i]))
        
    return pref

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    try:
        n = int(next(iterator))
        q = int(next(iterator))
        a = [int(next(iterator)) for _ in range(n)]
        
        pref = prefix_gcds(a)
        
        results = []
        for _ in range(q):
            r = int(next(iterator))
            results.append(str(pref[r]))
            
        print('\n'.join(results))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
    int gcd(int a, int b) {
        while (b) {
            a %= b;
            swap(a, b);
        }
        return a;
    }

public:
    vector<int> prefixGcds(const vector<int>& a) {
        int n = a.size();
        if (n == 0) return {};
        
        vector<int> pref(n);
        pref[0] = abs(a[0]);
        
        for (int i = 1; i < n; i++) {
            pref[i] = gcd(pref[i - 1], abs(a[i]));
        }
        
        return pref;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution solution;
    vector<int> pref = solution.prefixGcds(a);
    
    for (int i = 0; i < q; i++) {
        int r;
        cin >> r;
        cout << pref[r] << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function gcd(a, b) {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

function prefixGcds(a) {
  const n = a.length;
  if (n === 0) return [];
  
  const pref = new Int32Array(n);
  pref[0] = Math.abs(a[0]);
  
  for (let i = 1; i < n; i++) {
    pref[i] = gcd(pref[i - 1], Math.abs(a[i]));
  }
  
  return pref;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (let i = 0; i < parts.length; i++) {
    if (parts[i].length > 0) data.push(parts[i]);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const a = [];
  for (let i = 0; i < n; i++) a.push(parseInt(data[idx++], 10));
  
  const pref = prefixGcds(a);
  const out = [];
  for (let i = 0; i < q; i++) {
    const r = parseInt(data[idx++], 10);
    out.push(pref[r].toString());
  }
  console.log(out.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `A = [12, 18, 6]`, Queries: `0, 1, 2`.

1. **Initialization:**
   - `pref` array of size 3.
   - `pref[0] = abs(12) = 12`.

2. **Iteration 1 (i=1):**
   - `pref[1] = gcd(pref[0], abs(18)) = gcd(12, 18)`.
   - Divisors of 12: 1, 2, 3, 4, 6, 12.
   - Divisors of 18: 1, 2, 3, 6, 9, 18.
   - Largest common is 6.
   - `pref[1] = 6`.

3. **Iteration 2 (i=2):**
   - `pref[2] = gcd(pref[1], abs(6)) = gcd(6, 6)`.
   - `pref[2] = 6`.

4. **Queries:**
   - `r=0`: Return `pref[0]` -> **12**.
   - `r=1`: Return `pref[1]` -> **6**.
   - `r=2`: Return `pref[2]` -> **6**.

Matches example output.

## ✅ Proof of Correctness

### Invariant
At index `i`, `pref[i]` stores the GCD of all elements from `A[0]` to `A[i]`.
Base case: `pref[0] = A[0]` holds.
Inductive step: If `pref[i-1] = gcd(A[0]...A[i-1])`, then `pref[i] = gcd(pref[i-1], A[i]) = gcd(gcd(A[0]...A[i-1]), A[i]) = gcd(A[0]...A[i])` by the associative property of GCD.

### Why the approach is correct
The problem asks for prefix GCDs. Since GCD is associative, we can compute them incrementally in a single pass.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Range GCD Queries (Sparse Table / Segment Tree).
  - *Question:* What if queries are for arbitrary ranges `[L, R]`?
  - *Answer:* Use a Sparse Table for `O(1)` queries (since GCD is idempotent) or a Segment Tree for `O(log N)` queries with updates.
- **Extension 2:** Dynamic Updates.
  - *Question:* What if we update `A[i]`?
  - *Answer:* Segment Tree allows point updates and range queries in `O(log N)`.
- **Extension 3:** Number of distinct prefix GCDs.
  - *Question:* How many unique values can the prefix GCD array contain?
  - *Answer:* At most `O(log(max A))`, because each time the GCD changes, it must decrease by a factor of at least 2.

### Common Mistakes to Avoid

1. **Negative Numbers**
   - ❌ Wrong: `gcd(-12, 18)` might return -6 in some languages or be undefined.
   - ✅ Correct: Always use `abs()` before computing GCD.
2. **Zero Handling**
   - ❌ Wrong: `gcd(0, 0)` might crash.
   - ✅ Correct: Ensure your GCD function handles 0 correctly (usually returns 0).
3. **Time Complexity**
   - ❌ Wrong: Recomputing GCD for each query (`O(N * Q)`).
   - ✅ Correct: Precompute in `O(N)`.

## Related Concepts

- **Euclidean Algorithm:** The standard way to compute GCD.
- **Prefix Sums:** Similar concept for summation.
- **Associative Property:** Allows incremental computation.
