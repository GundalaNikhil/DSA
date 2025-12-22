---
problem_id: HSH_SUBARRAY_HASH_EQUALITY__6271
display_id: HSH-012
slug: subarray-hash-equality
title: "Subarray Hash Equality (Integers)"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Arrays
  - Rolling Hash
tags:
  - hashing
  - array
  - subarray
  - medium
premium: true
subscription_tier: basic
---

# HSH-012: Subarray Hash Equality (Integers)

## 📋 Problem Summary

You are given an array of integers `arr` and multiple queries. Each query consists of two ranges `[l1, r1]` and `[l2, r2]`. You need to determine if the subarray `arr[l1..r1]` is identical to `arr[l2..r2]`.
This is essentially "Substring Equality" but for arrays of numbers instead of characters.

## 🌍 Real-World Scenario

**Scenario Title:** Audio Snippet Matching

Digital audio is often represented as an array of integer samples (amplitudes).
- You have a long recording (the array).
- You want to check if a sound effect at timestamp A is the same as the one at timestamp B.
- Comparing sample-by-sample is slow ($O(N)$).
- Hashing allows $O(1)$ comparison after preprocessing.

![Real-World Application](../images/HSH-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Integer Rolling Hash

Array: `[10, 20, 30, 40]`
Base: $B=100$ (Must be larger than max element, or map elements to smaller range)

Prefix Hashes:
- $H[0] = 10$
- $H[1] = 10 \cdot 100 + 20 = 1020$
- $H[2] = 1020 \cdot 100 + 30 = 102030$

Query `[1..2]` (Values 20, 30):
- Formula: $H[2] - H[0] \cdot B^2$
- $102030 - 10 \cdot 10000 = 102030 - 100000 = 2030$.
- Expected Hash for `[20, 30]`: $20 \cdot 100 + 30 = 2030$. Matches!

### Key Concept: Handling Large/Negative Integers

Standard rolling hash works on characters (0-255). Here, integers can be large ($10^9$) or negative.
- **Large Values:** The Base $B$ doesn't strictly need to be larger than the max element if we rely on modulo arithmetic, but collisions are more likely if $B$ is small. A random large prime $B > N$ is usually good.
- **Negative Values:** Add a large offset (e.g., $10^9 + 7$) to make them positive before hashing. Or just use raw values in modulo arithmetic (handling negative results correctly).

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Array of size $N$, $Q$ queries.
- **Output:** Boolean for each query.
- **Constraints:** $N, Q \le 2 \cdot 10^5$.
- **Values:** $-10^9 \dots 10^9$.
- **Strategy:** Use double hashing to avoid collisions.

## Naive Approach

### Intuition

Compare subarrays element by element.

### Time Complexity

- **O(Q * N)**: Too slow.

## Optimal Approach

### Key Insight

Treat the integer array exactly like a string.
- Map each integer `x` to a positive value if necessary (though modulo handles negatives fine if we do `(x % M + M) % M`).
- Compute prefix hashes.
- Answer queries in $O(1)$.

### Algorithm

1. Choose Base $B$ and Modulus $M$.
2. Precompute `powers[]`.
3. Precompute `hashes[]`: $H[i] = (H[i-1] \cdot B + arr[i]) \pmod M$.
4. For query `(l1, r1, l2, r2)`:
   - Check lengths: if `r1-l1 != r2-l2`, return false.
   - Compute hash of first subarray.
   - Compute hash of second subarray.
   - Compare.

### Time Complexity

- **O(N + Q)**.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HSH-012/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private static final long MOD1 = 1_000_000_007L;
    private static final long BASE1 = 100003L; // Larger than typical small constraints, but random is better
    private static final long MOD2 = 1_000_000_009L;
    private static final long BASE2 = 100019L;
    
    public boolean[] checkSubarrayEquality(int[] arr, int[][] queries) {
        int n = arr.length;
        long[] h1 = new long[n + 1];
        long[] p1 = new long[n + 1];
        long[] h2 = new long[n + 1];
        long[] p2 = new long[n + 1];
        
        p1[0] = 1;
        p2[0] = 1;
        
        for (int i = 0; i < n; i++) {
            // Handle negative numbers by adding offset or just standard mod arithmetic
            // (val % MOD + MOD) % MOD ensures positive
            long val = arr[i];
            
            h1[i + 1] = (h1[i] * BASE1 + val) % MOD1;
            if (h1[i + 1] < 0) h1[i + 1] += MOD1;
            
            p1[i + 1] = (p1[i] * BASE1) % MOD1;
            
            h2[i + 1] = (h2[i] * BASE2 + val) % MOD2;
            if (h2[i + 1] < 0) h2[i + 1] += MOD2;
            
            p2[i + 1] = (p2[i] * BASE2) % MOD2;
        }
        
        boolean[] results = new boolean[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int l1 = queries[i][0];
            int r1 = queries[i][1];
            int l2 = queries[i][2];
            int r2 = queries[i][3];
            
            if (r1 - l1 != r2 - l2) {
                results[i] = false;
                continue;
            }
            
            long hash1_sub1 = getHash(h1, p1, l1, r1, MOD1);
            long hash1_sub2 = getHash(h1, p1, l2, r2, MOD1);
            
            long hash2_sub1 = getHash(h2, p2, l1, r1, MOD2);
            long hash2_sub2 = getHash(h2, p2, l2, r2, MOD2);
            
            results[i] = (hash1_sub1 == hash1_sub2) && (hash2_sub1 == hash2_sub2);
        }
        
        return results;
    }
    
    private long getHash(long[] h, long[] p, int l, int r, long mod) {
        int len = r - l + 1;
        long val = (h[r + 1] - (h[l] * p[len]) % mod + mod) % mod;
        return val;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            
            int q = sc.nextInt();
            int[][] queries = new int[q][4];
            for (int i = 0; i < q; i++) {
                queries[i][0] = sc.nextInt();
                queries[i][1] = sc.nextInt();
                queries[i][2] = sc.nextInt();
                queries[i][3] = sc.nextInt();
            }
            
            Solution solution = new Solution();
            boolean[] result = solution.checkSubarrayEquality(arr, queries);
            
            for (boolean ans : result) {
                System.out.println(ans);
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(2000)

class Solution:
    def check_subarray_equality(self, arr: list, queries: list) -> list:
        n = len(arr)
        MOD1 = 10**9 + 7
        BASE1 = 100003
        MOD2 = 10**9 + 9
        BASE2 = 100019
        
        h1 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        h2 = [0] * (n + 1)
        p2 = [1] * (n + 1)
        
        for i in range(n):
            val = arr[i]
            
            h1[i+1] = (h1[i] * BASE1 + val) % MOD1
            p1[i+1] = (p1[i] * BASE1) % MOD1
            
            h2[i+1] = (h2[i] * BASE2 + val) % MOD2
            p2[i+1] = (p2[i] * BASE2) % MOD2
            
        def get_hash(h, p, l, r, mod):
            length = r - l + 1
            return (h[r+1] - h[l] * p[length]) % mod
            
        results = []
        for l1, r1, l2, r2 in queries:
            if r1 - l1 != r2 - l2:
                results.append(False)
                continue
                
            hash1_s1 = get_hash(h1, p1, l1, r1, MOD1)
            hash1_s2 = get_hash(h1, p1, l2, r2, MOD1)
            
            if hash1_s1 != hash1_s2:
                results.append(False)
                continue
                
            hash2_s1 = get_hash(h2, p2, l1, r1, MOD2)
            hash2_s2 = get_hash(h2, p2, l2, r2, MOD2)
            
            results.append(hash2_s1 == hash2_s2)
            
        return results

def check_subarray_equality(arr: list, queries: list) -> list:
    solver = Solution()
    return solver.check_subarray_equality(arr, queries)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        arr = []
        for _ in range(n):
            arr.append(int(next(iterator)))
            
        q = int(next(iterator))
        queries = []
        for _ in range(q):
            l1 = int(next(iterator))
            r1 = int(next(iterator))
            l2 = int(next(iterator))
            r2 = int(next(iterator))
            queries.append([l1, r1, l2, r2])
            
        result = check_subarray_equality(arr, queries)
        for ans in result:
            print("true" if ans else "false")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
    const long long MOD1 = 1e9 + 7;
    const long long BASE1 = 100003;
    const long long MOD2 = 1e9 + 9;
    const long long BASE2 = 100019;

public:
    vector<bool> checkSubarrayEquality(vector<int>& arr, vector<vector<int>>& queries) {
        int n = arr.size();
        
        vector<long long> h1(n + 1, 0), p1(n + 1, 1);
        vector<long long> h2(n + 1, 0), p2(n + 1, 1);
        
        for (int i = 0; i < n; i++) {
            long long val = arr[i];
            
            h1[i + 1] = (h1[i] * BASE1 + val) % MOD1;
            if (h1[i + 1] < 0) h1[i + 1] += MOD1;
            p1[i + 1] = (p1[i] * BASE1) % MOD1;
            
            h2[i + 1] = (h2[i] * BASE2 + val) % MOD2;
            if (h2[i + 1] < 0) h2[i + 1] += MOD2;
            p2[i + 1] = (p2[i] * BASE2) % MOD2;
        }
        
        vector<bool> results;
        results.reserve(queries.size());
        
        for (const auto& q : queries) {
            int l1 = q[0], r1 = q[1], l2 = q[2], r2 = q[3];
            
            if (r1 - l1 != r2 - l2) {
                results.push_back(false);
                continue;
            }
            
            long long hash1_s1 = getHash(h1, p1, l1, r1, MOD1);
            long long hash1_s2 = getHash(h1, p1, l2, r2, MOD1);
            
            if (hash1_s1 != hash1_s2) {
                results.push_back(false);
                continue;
            }
            
            long long hash2_s1 = getHash(h2, p2, l1, r1, MOD2);
            long long hash2_s2 = getHash(h2, p2, l2, r2, MOD2);
            
            results.push_back(hash2_s1 == hash2_s2);
        }
        
        return results;
    }
    
    long long getHash(const vector<long long>& h, const vector<long long>& p, int l, int r, long long mod) {
        int len = r - l + 1;
        long long val = (h[r + 1] - (h[l] * p[len]) % mod + mod) % mod;
        return val;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    int q;
    if (!(cin >> q)) return 0;
    
    vector<vector<int>> queries(q, vector<int>(4));
    for (int i = 0; i < q; i++) {
        cin >> queries[i][0] >> queries[i][1] >> queries[i][2] >> queries[i][3];
    }
    
    Solution solution;
    vector<bool> result = solution.checkSubarrayEquality(arr, queries);
    
    for (bool ans : result) {
        cout << (ans ? "true" : "false") << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  checkSubarrayEquality(arr, queries) {
    const n = arr.length;
    const MOD1 = 1000000007n;
    const BASE1 = 100003n;
    const MOD2 = 1000000009n;
    const BASE2 = 100019n;
    
    const h1 = new BigInt64Array(n + 1);
    const p1 = new BigInt64Array(n + 1);
    const h2 = new BigInt64Array(n + 1);
    const p2 = new BigInt64Array(n + 1);
    
    p1[0] = 1n;
    p2[0] = 1n;
    
    for (let i = 0; i < n; i++) {
      let val = BigInt(arr[i]);
      
      h1[i + 1] = (h1[i] * BASE1 + val) % MOD1;
      if (h1[i + 1] < 0n) h1[i + 1] += MOD1;
      p1[i + 1] = (p1[i] * BASE1) % MOD1;
      
      h2[i + 1] = (h2[i] * BASE2 + val) % MOD2;
      if (h2[i + 1] < 0n) h2[i + 1] += MOD2;
      p2[i + 1] = (p2[i] * BASE2) % MOD2;
    }
    
    const getHash = (h, p, l, r, mod) => {
      const len = r - l + 1;
      let val = (h[r + 1] - (h[l] * p[len]) % mod) % mod;
      if (val < 0n) val += mod;
      return val;
    };
    
    const results = [];
    for (const [l1, r1, l2, r2] of queries) {
      if (r1 - l1 !== r2 - l2) {
        results.push(false);
        continue;
      }
      
      const hash1_s1 = getHash(h1, p1, l1, r1, MOD1);
      const hash1_s2 = getHash(h1, p1, l2, r2, MOD1);
      
      if (hash1_s1 !== hash1_s2) {
        results.push(false);
        continue;
      }
      
      const hash2_s1 = getHash(h2, p2, l1, r1, MOD2);
      const hash2_s2 = getHash(h2, p2, l2, r2, MOD2);
      
      results.push(hash2_s1 === hash2_s2);
    }
    
    return results;
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
  
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  const arr = data[ptr++].split(" ").map(Number);
  const q = parseInt(data[ptr++]);
  
  const queries = [];
  for (let i = 0; i < q; i++) {
    queries.push(data[ptr++].split(" ").map(Number));
  }
  
  const solution = new Solution();
  const result = solution.checkSubarrayEquality(arr, queries);
  
  result.forEach((ans) => console.log(ans ? "true" : "false"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4
1 2 1 2
1
0 1 2 3
```
Array: `[1, 2, 1, 2]`
Query: `[0, 1]` vs `[2, 3]`.

**Hashes:**
- $H[0]=0$.
- $H[1]=1$.
- $H[2]=1 \cdot B + 2$.
- $H[3]=(1 \cdot B + 2) \cdot B + 1 = B^2 + 2B + 1$.
- $H[4]=(B^2 + 2B + 1) \cdot B + 2 = B^3 + 2B^2 + B + 2$.

**Subarray 1 (0..1):**
- $H[2] - H[0] \cdot B^2 = (B+2) - 0 = B+2$.

**Subarray 2 (2..3):**
- $H[4] - H[2] \cdot B^2$.
- $(B^3 + 2B^2 + B + 2) - (B+2) \cdot B^2$.
- $B^3 + 2B^2 + B + 2 - (B^3 + 2B^2) = B + 2$.

**Result:**
- $B+2 == B+2$. True.

## ✅ Proof of Correctness

### Invariant
Polynomial hash works for any sequence of numbers, not just characters.
$Hash([x_1, x_2]) = x_1 \cdot B + x_2$.
As long as $x_i$ are treated consistently, equality holds.

## 💡 Interview Extensions

- **Extension 1:** Longest Common Subarray between two arrays.
  - *Answer:* Binary search on length + Hashing.
- **Extension 2:** Find if array is a palindrome.
  - *Answer:* Check if $Hash(Forward) == Hash(Reverse)$.

## Common Mistakes to Avoid

1. **Negative Numbers**
   - ❌ Wrong: `val % MOD` can be negative in Java/C++.
   - ✅ Correct: `(val % MOD + MOD) % MOD`.
2. **Base Size**
   - ❌ Wrong: Base smaller than max element value (e.g., Base 10 for array `[12, 5]`).
   - ✅ Correct: Base should ideally be larger than max element to avoid simple collisions like `[1, 2]` vs `[12]`, though modulo helps. Random large prime is best.

## Related Concepts

- **Suffix Array:** Can handle this for general comparisons.
- **KMP:** For pattern matching in arrays.
