---
problem_id: HSH_SUBSTRING_EQUALITY_QUERIES__5917
display_id: HSH-002
slug: substring-equality-queries
title: "Substring Equality Queries"
difficulty: Medium
difficulty_score: 45
topics:
  - Hashing
  - Rolling Hash
  - String Matching
tags:
  - hashing
  - rolling-hash
  - substring
  - queries
  - medium
premium: true
subscription_tier: basic
---

# HSH-002: Substring Equality Queries

## 📋 Problem Summary

You are given a string `s` and multiple queries. Each query provides two pairs of indices `(l1, r1)` and `(l2, r2)`, representing two substrings `s[l1..r1]` and `s[l2..r2]`. Your task is to determine if these two substrings are identical for each query.

## 🌍 Real-World Scenario

**Scenario Title:** DNA Sequence Matching

Imagine you are a geneticist analyzing a massive DNA sequence (millions of base pairs). You want to check if a specific gene segment found at position X is identical to another segment at position Y.
- Comparing them character by character for every query is too slow if the segments are long and queries are frequent.
- Instead, you can "fingerprint" the entire DNA sequence once. Then, checking if two segments match becomes a simple comparison of their fingerprints.

![Real-World Application](../images/HSH-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Substring Hashing

String: "banana"
Query: `s[1..3]` ("ana") vs `s[3..5]` ("ana")

```text
Indices: 0 1 2 3 4 5
String:  b a n a n a

Prefix Hashes (Base 10, Mod 1000 for simplicity):
H[0] = 'b'(98)
H[1] = 98*10 + 97 = 1077 -> 77
H[2] = 77*10 + 110('n') = 880
H[3] = 880*10 + 97 = 8897 -> 897
H[4] = 897*10 + 110 = 9080 -> 80
H[5] = 80*10 + 97 = 897

Hash("ana" at 1..3):
Formula: (H[3] - H[0] * B^3) % M
Wait, length is 3. Formula is (H[r] - H[l-1] * B^len) % M
H[3] = 897
H[0] = 98
B^3 = 1000 -> 0 (mod 1000) -> Wait, mod is 1000. B=10.
Let's use larger mod to avoid 0. Say Mod large.

Hash(1..3) = H[3] - H[0] * B^3
Hash(3..5) = H[5] - H[2] * B^3

If Hash(1..3) == Hash(3..5), substrings are likely equal.
```

### Key Concept: O(1) Substring Hash

Using the prefix hash array $H$ where $H[i]$ is the hash of $s[0 \dots i]$, we can calculate the hash of any substring $s[l \dots r]$ in $O(1)$ time:

$$ \text{Hash}(s[l \dots r]) = (H[r] - H[l-1] \times B^{r-l+1}) \pmod M $$

(If $l=0$, the term $H[l-1]$ is 0).
This works because $H[r]$ contains the polynomial for $s[0 \dots r]$, and $H[l-1] \times B^{\text{len}}$ represents the prefix $s[0 \dots l-1]$ shifted to align with the start of the substring, effectively subtracting it out.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Double Hashing:** Use two sets of (Base, Mod) to minimize collisions. A collision happens when two different strings have the same hash. With two hashes, the probability is negligible ($ \approx 10^{-18}$).
- **Indices:** 0-based inclusive.
- **Constraints:** $N, Q \le 2 \cdot 10^5$. An $O(N \cdot Q)$ solution will TLE. We need $O(N + Q)$.

## Naive Approach

### Intuition

For each query, compare the substrings character by character.

### Algorithm

1. For each query `(l1, r1, l2, r2)`:
   - Check if lengths differ ($r1-l1 \neq r2-l2$). If so, return false.
   - Loop `k` from 0 to length-1.
   - If `s[l1+k] != s[l2+k]`, return false.
   - Return true.

### Time Complexity

- **O(Q * N)**: Worst case (e.g., all queries are for the whole string). Too slow.

## Optimal Approach

### Key Insight

Use **Polynomial Rolling Hash** with **Double Hashing**.
1. Precompute prefix hashes for the entire string.
2. Precompute powers of the base $B$.
3. Answer each query in $O(1)$ by computing the substring hash using the formula.

### Algorithm

1. Choose two pairs of constants: $(B_1, M_1)$ and $(B_2, M_2)$.
   - e.g., $B_1=31, M_1=10^9+7$ and $B_2=37, M_2=10^9+9$.
2. Precompute `powers` arrays for $B_1$ and $B_2$.
3. Precompute `prefix_hashes` arrays for both pairs.
4. For each query:
   - Calculate Hash1 for both substrings.
   - Calculate Hash2 for both substrings.
   - If (Hash1_sub1 == Hash1_sub2) AND (Hash2_sub1 == Hash2_sub2), return true.
   - Else return false.

### Time Complexity

- **O(N + Q)**: $O(N)$ preprocessing, $O(1)$ per query.

### Space Complexity

- **O(N)**: To store hashes and powers.

![Algorithm Visualization](../images/HSH-002/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private static final long MOD1 = 1000000007L;
    private static final long BASE1 = 313L;
    private static final long MOD2 = 1000000009L;
    private static final long BASE2 = 317L;

    public boolean[] checkSubstringEquality(String s, int[][] queries) {
        int n = s.length();
        
        long[] h1 = new long[n + 1];
        long[] p1 = new long[n + 1];
        long[] h2 = new long[n + 1];
        long[] p2 = new long[n + 1];
        
        p1[0] = 1;
        p2[0] = 1;
        
        for (int i = 0; i < n; i++) {
            h1[i + 1] = (h1[i] * BASE1 + s.charAt(i)) % MOD1;
            p1[i + 1] = (p1[i] * BASE1) % MOD1;
            
            h2[i + 1] = (h2[i] * BASE2 + s.charAt(i)) % MOD2;
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
        // h is 1-based prefix hash array
        // substring s[l..r] corresponds to h[r+1] and h[l]
        // Formula: (h[r+1] - h[l] * p[len]) % mod
        int len = r - l + 1;
        long val = (h[r + 1] - (h[l] * p[len]) % mod + mod) % mod;
        return val;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (sc.hasNextInt()) {
                int q = sc.nextInt();
                int[][] queries = new int[q][4];
                for (int i = 0; i < q; i++) {
                    queries[i][0] = sc.nextInt();
                    queries[i][1] = sc.nextInt();
                    queries[i][2] = sc.nextInt();
                    queries[i][3] = sc.nextInt();
                }
                
                Solution solution = new Solution();
                boolean[] result = solution.checkSubstringEquality(s, queries);
                
                for (boolean ans : result) {
                    System.out.println(ans);
                }
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

class Solution:
    def check_substring_equality(self, s: str, queries: list) -> list:
        n = len(s)
        MOD1 = 10**9 + 7
        BASE1 = 313
        MOD2 = 10**9 + 9
        BASE2 = 317
        
        h1 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        h2 = [0] * (n + 1)
        p2 = [1] * (n + 1)
        
        for i in range(n):
            char_code = ord(s[i])
            h1[i+1] = (h1[i] * BASE1 + char_code) % MOD1
            p1[i+1] = (p1[i] * BASE1) % MOD1
            
            h2[i+1] = (h2[i] * BASE2 + char_code) % MOD2
            p2[i+1] = (p2[i] * BASE2) % MOD2
            
        results = []
        
        def get_hash(h, p, l, r, mod):
            length = r - l + 1
            return (h[r+1] - h[l] * p[length]) % mod
            
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

def check_substring_equality(s: str, queries: list) -> list:
    solver = Solution()
    return solver.check_substring_equality(s, queries)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        s = next(iterator)
        q = int(next(iterator))
        queries = []
        for _ in range(q):
            l1 = int(next(iterator))
            r1 = int(next(iterator))
            l2 = int(next(iterator))
            r2 = int(next(iterator))
            queries.append([l1, r1, l2, r2])
            
        result = check_substring_equality(s, queries)
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
#include <string>

using namespace std;

class Solution {
    const long long MOD1 = 1e9 + 7;
    const long long BASE1 = 313;
    const long long MOD2 = 1e9 + 9;
    const long long BASE2 = 317;

public:
    vector<bool> checkSubstringEquality(string s, vector<vector<int>>& queries) {
        int n = s.length();
        
        vector<long long> h1(n + 1, 0), p1(n + 1, 1);
        vector<long long> h2(n + 1, 0), p2(n + 1, 1);
        
        for (int i = 0; i < n; i++) {
            h1[i + 1] = (h1[i] * BASE1 + s[i]) % MOD1;
            p1[i + 1] = (p1[i] * BASE1) % MOD1;
            
            h2[i + 1] = (h2[i] * BASE2 + s[i]) % MOD2;
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
    
    string s;
    if (!(cin >> s)) return 0;
    
    int q;
    if (!(cin >> q)) return 0;
    
    vector<vector<int>> queries(q, vector<int>(4));
    for (int i = 0; i < q; i++) {
        cin >> queries[i][0] >> queries[i][1] >> queries[i][2] >> queries[i][3];
    }
    
    Solution solution;
    vector<bool> result = solution.checkSubstringEquality(s, queries);
    
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
  checkSubstringEquality(s, queries) {
    const n = s.length;
    const MOD1 = 1000000007n;
    const BASE1 = 313n;
    const MOD2 = 1000000009n;
    const BASE2 = 317n;
    
    const h1 = new BigInt64Array(n + 1);
    const p1 = new BigInt64Array(n + 1);
    const h2 = new BigInt64Array(n + 1);
    const p2 = new BigInt64Array(n + 1);
    
    h1[0] = 0n; p1[0] = 1n;
    h2[0] = 0n; p2[0] = 1n;
    
    for (let i = 0; i < n; i++) {
      const charCode = BigInt(s.charCodeAt(i));
      
      h1[i + 1] = (h1[i] * BASE1 + charCode) % MOD1;
      p1[i + 1] = (p1[i] * BASE1) % MOD1;
      
      h2[i + 1] = (h2[i] * BASE2 + charCode) % MOD2;
      p2[i + 1] = (p2[i] * BASE2) % MOD2;
    }
    
    const results = [];
    
    const getHash = (h, p, l, r, mod) => {
      const len = r - l + 1;
      let val = (h[r + 1] - (h[l] * p[len]) % mod) % mod;
      if (val < 0n) val += mod;
      return val;
    };
    
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
  const s = data[ptr++];
  const q = parseInt(data[ptr++]);
  
  const queries = [];
  for (let i = 0; i < q; i++) {
    const parts = data[ptr++].split(" ").map(Number);
    queries.push(parts);
  }
  
  const solution = new Solution();
  const result = solution.checkSubstringEquality(s, queries);
  
  result.forEach((ans) => console.log(ans ? "true" : "false"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
ababa
1
0 2 2 4
```
Query: `s[0..2]` ("aba") vs `s[2..4]` ("aba").

**Preprocessing:**
- Calculate prefixes for "ababa".
- $H[3]$ (hash of "aba") will be computed.
- $H[5]$ (hash of "ababa") will be computed.

**Query Processing:**
- Substring 1 (0..2): $H[3] - H[0] \times B^3$. Since $H[0]=0$, this is just $H[3]$.
- Substring 2 (2..4): $H[5] - H[2] \times B^3$.
- If we do the math (assuming no collisions), these values will be identical because the underlying strings "aba" are identical.
- Result: `true`.

## ✅ Proof of Correctness

### Invariant
The function `getHash(l, r)` correctly returns the polynomial hash of $s[l \dots r]$.
Proof:
$H[r+1] = s[0]B^r + s[1]B^{r-1} + \dots + s[r]B^0$.
$H[l] = s[0]B^{l-1} + \dots + s[l-1]B^0$.
$H[l] \times B^{r-l+1} = s[0]B^r + \dots + s[l-1]B^{r-l+1}$.
Subtracting gives: $s[l]B^{r-l} + \dots + s[r]B^0$, which is exactly the hash of $s[l \dots r]$.

## 💡 Interview Extensions

- **Extension 1:** Find the longest common substring between two strings.
  - *Answer:* Binary search on length + Hashing. $O(N \log N)$.
- **Extension 2:** Check if a string is a palindrome using hashing.
  - *Answer:* Compute forward hash and reverse hash. Check if Hash(Forward) == Hash(Reverse).

## Common Mistakes to Avoid

1. **Single Hash Collision**
   - ❌ Wrong: Using only one modulus (e.g., $10^9+7$).
   - ✅ Correct: Use double hashing to make probability of failure negligible.

2. **Negative Modulo Result**
   - ❌ Wrong: `(a - b) % M` in languages like C++/Java can be negative.
   - ✅ Correct: `(a - b + M) % M`.

3. **1-based vs 0-based Indexing**
   - ❌ Wrong: Mixing up prefix array indices. $H[i]$ usually stores hash of length $i$ (indices $0 \dots i-1$).
   - ✅ Correct: Be consistent. $H[i+1]$ for prefix ending at $i$.

## Related Concepts

- **Rabin-Karp:** Uses this technique for pattern matching.
- **Suffix Structures:** Suffix Array/Tree can also solve this but are harder to implement.
