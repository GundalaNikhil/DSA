---
problem_id: BIT_DISTINCT_SUBARRAY_XORS__8412
display_id: BIT-012
slug: distinct-subarray-xors
title: "Distinct Subarray XORs"
difficulty: Medium
difficulty_score: 55
topics:
  - Bitwise Operations
  - XOR
  - Subarray
  - Trie
tags:
  - bitwise
  - xor
  - subarray
  - trie
  - medium
premium: true
subscription_tier: basic
---

# BIT-012: Distinct Subarray XORs

## 📋 Problem Summary

Count the number of **distinct** values obtained by XORing elements of all possible subarrays of `a`.

## 🌍 Real-World Scenario

**Scenario Title:** The Unique Interference Signatures

You are cataloging radio burst patterns.
- **Recording**: A continuous stream of signal samples `a[i]`.
- **Bursts**: A "burst" is any contiguous segment of time (subarray).
- **Signature**: The digital signature of a burst is the XOR sum of its samples.
- **Goal**: You want to build a database of all *unique* signatures seen in the recording. Duplicates don't add new information.
- **Challenge**: The recording is long (10,000 samples), so the number of bursts is huge (50 million). You need an efficient way to catalog them.

**Why This Problem Matters:**

- **Constraints Analysis**: `N=10,000` lies in the tricky zone where $O(N^2)$ is theoretically computation-feasible ($10^8$ ops) but memory-intensive ($10^8$ integers).
- **Memory Management**: Choosing `int[]` vs `HashSet` becomes critical.
- **Sorting vs Hashing**: Understanding tradeoffs for uniqueness checking.

![Real-World Application](../images/BIT-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Brute Force Collection
```
Array: [1, 2, 3]

Subarrays:
[1] -> 1
[2] -> 2
[3] -> 3
[1, 2] -> 1^2 = 3
[2, 3] -> 2^3 = 1
[1, 2, 3] -> 1^2^3 = 0

Results: {1, 2, 3, 3, 1, 0}
Distinct: {0, 1, 2, 3} -> Count 4.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: `a` size `N <= 10,000`.
- **Values**: Up to $10^9$.
- **Output**: Integer count.

Common interpretation mistake:

- ❌ Using Python `set` or Java `HashSet` blindly.
- ✅ realizing that for $N=10,000$, total subarrays $\approx 5 \times 10^7$. Storing this many objects in a Hash Set will cause Memory Limit Exceeded (MLE) or Time Limit Exceeded (TLE) due to overhead.
- ✅ Preferring Primitive Arrays + Sorting.

### Core Concept: Space-Efficient Counting

The total number of subarrays is $N(N+1)/2$.
For $N=10000$, this is $\approx 50,000,000$.
Storing 50 million integers takes $50 \times 10^6 \times 4$ bytes $\approx 200$ MB.
This fits in 256MB memory.
However, a `HashSet` node has overhead (pointers, object headers), easily 3-4x the size.
Thus, **collecting to a primitive array and sorting** is the viable approach.

## Naive Approach (HashSet)

### Intuition

Iterate all subarrays, add XORs to a Set.

### Algorithm

1. `Set<Integer> distinct`.
2. Loop `i` from 0 to `n-1`:
   - `curr = 0`.
   - Loop `j` from `i` to `n-1`:
     - `curr ^= a[j]`.
     - `distinct.add(curr)`.
3. Return `distinct.size()`.

### Time Complexity

- **O(N²)** on average, but overhead is high.

### Space Complexity

- **O(N²)**. High constant factor (MLE risk).

## Optimal Approach (Sorting Primitive Array)

### Key Insight

Use a raw integer array to store all XOR sums, then sort and count unique elements. In C++, `std::unique` is perfect. In Java, `Arrays.sort`. Iterating sorted array takes O(K).

### Algorithm

1. Allocate array `results` of size $N(N+1)/2$.
2. Fill array with XOR sums:
   - `idx = 0`
   - Loop `i` 0..n:
     - `curr = 0`
     - Loop `j` i..n:
       - `curr ^= a[j]`
       - `results[idx++] = curr`
3. Sort `results`.
4. Iterate to count unique elements.
   - `count = 0`
   - If `len > 0`, `count=1`.
   - Loop `k` from 1 to `len-1`:
     - `if results[k] != results[k-1]`: `count++`.
5. Return `count`.

### Time Complexity

- **O(N² log(N²))**. Sorting dominates.
- But sequential access is cache-friendly.

### Space Complexity

- **O(N²)**. Minimized constant factor.

![Algorithm Visualization](../images/BIT-012/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-012/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long distinctSubarrayXors(int[] a) {
        int n = a.length;
        // Total subarrays: n*(n+1)/2
        // Be careful with integer overflow for size index?
        // n=10000 -> size ~ 5*10^7. Fits in int.
        int totalSubarrays = n * (n + 1) / 2;
        int[] results = new int[totalSubarrays];
        
        int idx = 0;
        for (int i = 0; i < n; i++) {
            int currentXor = 0;
            for (int j = i; j < n; j++) {
                currentXor ^= a[j];
                results[idx++] = currentXor;
            }
        }
        
        // Sorting primitive array is memory efficient (Dual-Pivot Quicksort)
        Arrays.sort(results);
        
        if (totalSubarrays == 0) return 0;
        
        long distinctCount = 1;
        for (int i = 1; i < totalSubarrays; i++) {
            if (results[i] != results[i-1]) {
                distinctCount++;
            }
        }
        
        return distinctCount;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.distinctSubarrayXors(a));
        sc.close();
    }
}
```

### Python

```python
import sys

def distinct_subarray_xors(a: list[int]) -> int:
    # Python ints are objects (28 bytes+). N=10000 -> 50M ints -> 1.4GB RAM.
    # Standard Python list will MLE.
    # However, N=10000 is small enough for localized test cases but large for heavy memory.
    # Strategy: Use set logic but beware limit.
    # If standard set fails, we rely on constraints being somewhat loose or inputs usually having fewer distinct values.
    # But strictly, Python struggles here.
    # To optimize: use Set and `add` - Set removes dups on the fly, saving space IF many dups exist.
    
    # Try Set approach first.
    s = set()
    n = len(a)
    for i in range(n):
        curr = 0
        for j in range(i, n):
            curr ^= a[j]
            s.add(curr)
    return len(s)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
        
    result = distinct_subarray_xors(a)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    long long distinctSubarrayXors(vector<int>& a) {
        int n = a.size();
        long long size = (long long)n * (n + 1) / 2;
        vector<int> results;
        results.reserve(size);
        
        for (int i = 0; i < n; i++) {
            int currentXor = 0;
            for (int j = i; j < n; j++) {
                currentXor ^= a[j];
                results.push_back(currentXor);
            }
        }
        
        sort(results.begin(), results.end());
        
        // Count unique
        if (results.empty()) return 0;
        long long count = 1;
        for (size_t i = 1; i < results.size(); i++) {
            if (results[i] != results[i-1]) {
                count++;
            }
        }
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution solution;
    cout << solution.distinctSubarrayXors(a) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  distinctSubarrayXors(a) {
    const n = a.length;
    // Use TypedArray to save memory (Int32Array)
    const size = (n * (n + 1)) / 2;
    const results = new Int32Array(size);
    
    let idx = 0;
    for (let i = 0; i < n; i++) {
      let val = 0;
      for (let j = i; j < n; j++) {
        val ^= a[j];
        results[idx++] = val;
      }
    }
    
    results.sort();
    
    if (size === 0) return 0;
    let count = 1;
    for (let i = 1; i < size; i++) {
      if (results[i] !== results[i - 1]) {
        count++;
      }
    }
    return count;
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
    
    const solution = new Solution();
    console.log(String(solution.distinctSubarrayXors(a)));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `1, 2, 3`.
1. i=0:
   - [1] -> 1
   - [1,2] -> 3
   - [1,2,3] -> 0
2. i=1:
   - [2] -> 2
   - [2,3] -> 1
3. i=2:
   - [3] -> 3
Array: `[1, 3, 0, 2, 1, 3]`.
Sorted: `[0, 1, 1, 2, 3, 3]`.
Unique: `0, 1, 2, 3`. Count 4.

## ✅ Proof of Correctness

### Invariant

We explicitly calculate every possible subarray XOR. The only optimization is using sorting to count distinct elements instead of a Hash Set to respect memory constraints. Correctness of logic is absolute.

## 💡 Interview Extensions (High-Value Add-ons)

- **Large N (10^5)**: Only possible if range of values is small, or number of distinct XORs is provably small (not generally true).
- **Trie**: Could insert into Trie to save space (deduplicates implicitly), but node overhead is also high.

## Common Mistakes to Avoid

1. **Memory Blowup**:
   - ❌ Doing `list.append` in a loop in interpreted languages for N=10000.
2. **Slow Sort**:
   - ❌ Bubble sort ($O(M^2)$) on the results array. M is $N^2$. Complexity $N^4$. Total disaster.
   - ✅ Use built-in Quicksort/Mergesort ($O(M \log M)$).

## Related Concepts

- **Radix Sort**: Could sort integers in linear time $O(M)$.
- **Space-Time Tradeoff**: Using sorting (time) to save map overhead (space).
