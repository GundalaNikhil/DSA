---
problem_id: HSH_COUNT_PAIRS_EQUAL_DOUBLE_HASH__9418
display_id: HSH-015
slug: count-pairs-equal-double-hash
title: "Count Pairs with Equal Hash Mod Two Mods"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Combinatorics
  - String Algorithms
tags:
  - hashing
  - double-hash
  - pairs
  - medium
premium: true
subscription_tier: basic
---

# HSH-015: Count Pairs with Equal Hash Mod Two Mods

## 📋 Problem Summary

You are given a string `s` and a length `L`.
Find the number of pairs of indices $(i, j)$ such that $i < j$ and the substring starting at $i$ with length $L$ is "equal" to the substring starting at $j$ with length $L$.
Equality is determined by checking if their **Double Hashes** match.

## 🌍 Real-World Scenario

**Scenario Title:** Duplicate Log Entry Detection

Imagine a system processing millions of log lines.
- You want to find how many times the exact same error message of length $L$ appears.
- If a message appears $K$ times, it contributes $K(K-1)/2$ pairs of duplicates.
- Using double hashing ensures we don't accidentally group different messages together (collisions), providing accurate statistics.

![Real-World Application](../images/HSH-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Grouping by Hash

String: "banana", L=2
Substrings:
1. "ba" -> Hash Pair (H1_a, H2_a)
2. "an" -> Hash Pair (H1_b, H2_b)
3. "na" -> Hash Pair (H1_c, H2_c)
4. "an" -> Hash Pair (H1_b, H2_b)
5. "na" -> Hash Pair (H1_c, H2_c)

Groups:
- (H1_a, H2_a): Count 1 ("ba"). Pairs: 0.
- (H1_b, H2_b): Count 2 ("an"). Pairs: 1.
- (H1_c, H2_c): Count 2 ("na"). Pairs: 1.

Total Pairs: 2.

### Key Concept: Double Hashing

Single hashing with modulo $10^9+7$ has a collision probability of $\approx 1/10^9$.
With $N=10^5$ substrings, we have $\approx 10^{10}$ pairs, so collisions are possible (Birthday Paradox).
**Double Hashing** uses two pairs of $(Base, Mod)$.
Collision probability drops to $\approx 1/10^{18}$, making it virtually impossible to have a false positive.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`, integer `L`.
- **Output:** Long integer (count of pairs).
- **Constraints:** $N \le 10^5$.
- **Note:** The number of pairs can be up to $N(N-1)/2 \approx 5 \cdot 10^9$, so use 64-bit integer (`long` in Java/C++) for the result.

## Naive Approach

### Intuition

Compare every pair of substrings.

### Time Complexity

- **O(N^2 * L)**: String comparison.
- **O(N^2)**: With hashing but checking all pairs. Too slow.

## Optimal Approach

### Key Insight

1. Compute rolling hashes for all substrings of length `L`.
2. Store counts of each hash pair in a Map.
   - Key: `(hash1, hash2)`
   - Value: `count`
3. If a hash pair appears `k` times, it contributes `k * (k - 1) / 2` pairs.
4. Sum up these contributions.

### Algorithm

1. Initialize `Map<Pair<Long, Long>, Integer> counts`.
2. Compute rolling hashes for `s` with two sets of parameters.
3. Iterate `i` from 0 to `N-L`:
   - Get `h1` and `h2` for `s[i..i+L-1]`.
   - Increment count in Map.
4. Iterate Map values: `ans += count * (count - 1) / 2`.
5. Return `ans`.

### Time Complexity

- **O(N)**: Single pass to compute hashes and populate map.

### Space Complexity

- **O(N)**: Map storage.

![Algorithm Visualization](../images/HSH-015/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private static final long MOD1 = 1_000_000_007L;
    private static final long BASE1 = 313L;
    private static final long MOD2 = 1_000_000_009L;
    private static final long BASE2 = 317L;
    
    public long countPairs(String s, int L) {
        int n = s.length();
        if (L > n) return 0;
        
        // Map key: "hash1,hash2" string or a custom object
        // Using String key is easiest in Java but slightly slower. 
        // For competitive programming, use a custom class or combine into one long if possible (but 2 longs don't fit in 1 long).
        // Here we use String for clarity.
        Map<String, Integer> counts = new HashMap<>();
        
        long h1 = 0, h2 = 0;
        long p1 = 1, p2 = 1;
        
        // Precompute powers
        for (int i = 0; i < L - 1; i++) {
            p1 = (p1 * BASE1) % MOD1;
            p2 = (p2 * BASE2) % MOD2;
        }
        
        // Initial window
        for (int i = 0; i < L; i++) {
            h1 = (h1 * BASE1 + s.charAt(i)) % MOD1;
            h2 = (h2 * BASE2 + s.charAt(i)) % MOD2;
        }
        
        String key = h1 + "," + h2;
        counts.put(key, 1);
        
        // Slide
        for (int i = 1; i <= n - L; i++) {
            long remove1 = (s.charAt(i - 1) * p1) % MOD1;
            h1 = (h1 - remove1 + MOD1) % MOD1;
            h1 = (h1 * BASE1 + s.charAt(i + L - 1)) % MOD1;
            
            long remove2 = (s.charAt(i - 1) * p2) % MOD2;
            h2 = (h2 - remove2 + MOD2) % MOD2;
            h2 = (h2 * BASE2 + s.charAt(i + L - 1)) % MOD2;
            
            key = h1 + "," + h2;
            counts.put(key, counts.getOrDefault(key, 0) + 1);
        }
        
        long ans = 0;
        for (int count : counts.values()) {
            ans += (long) count * (count - 1) / 2;
        }
        
        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (sc.hasNextInt()) {
                int L = sc.nextInt();
                Solution solution = new Solution();
                System.out.println(solution.countPairs(s, L));
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def count_pairs(self, s: str, L: int) -> int:
        n = len(s)
        if L > n:
            return 0
            
        MOD1 = 10**9 + 7
        BASE1 = 313
        MOD2 = 10**9 + 9
        BASE2 = 317
        
        counts = {}
        
        h1 = 0
        h2 = 0
        p1 = pow(BASE1, L - 1, MOD1)
        p2 = pow(BASE2, L - 1, MOD2)
        
        # Initial window
        for i in range(L):
            val = ord(s[i])
            h1 = (h1 * BASE1 + val) % MOD1
            h2 = (h2 * BASE2 + val) % MOD2
            
        key = (h1, h2)
        counts[key] = 1
        
        # Slide
        for i in range(1, n - L + 1):
            val_remove = ord(s[i - 1])
            val_add = ord(s[i + L - 1])
            
            remove1 = (val_remove * p1) % MOD1
            h1 = (h1 - remove1 + MOD1) % MOD1
            h1 = (h1 * BASE1 + val_add) % MOD1
            
            remove2 = (val_remove * p2) % MOD2
            h2 = (h2 - remove2 + MOD2) % MOD2
            h2 = (h2 * BASE2 + val_add) % MOD2
            
            key = (h1, h2)
            counts[key] = counts.get(key, 0) + 1
            
        ans = 0
        for count in counts.values():
            ans += count * (count - 1) // 2
            
        return ans

def count_pairs(s: str, L: int) -> int:
    solver = Solution()
    return solver.count_pairs(s, L)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    s = input_data[0]
    if len(input_data) > 1:
        L = int(input_data[1])
        print(count_pairs(s, L))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

class Solution {
    const long long MOD1 = 1e9 + 7;
    const long long BASE1 = 313;
    const long long MOD2 = 1e9 + 9;
    const long long BASE2 = 317;

public:
    long long countPairs(string s, int L) {
        int n = s.length();
        if (L > n) return 0;
        
        map<pair<long long, long long>, int> counts;
        
        long long h1 = 0, h2 = 0;
        long long p1 = 1, p2 = 1;
        
        for (int i = 0; i < L - 1; i++) {
            p1 = (p1 * BASE1) % MOD1;
            p2 = (p2 * BASE2) % MOD2;
        }
        
        for (int i = 0; i < L; i++) {
            h1 = (h1 * BASE1 + s[i]) % MOD1;
            h2 = (h2 * BASE2 + s[i]) % MOD2;
        }
        
        counts[{h1, h2}]++;
        
        for (int i = 1; i <= n - L; i++) {
            long long remove1 = (s[i - 1] * p1) % MOD1;
            h1 = (h1 - remove1 + MOD1) % MOD1;
            h1 = (h1 * BASE1 + s[i + L - 1]) % MOD1;
            
            long long remove2 = (s[i - 1] * p2) % MOD2;
            h2 = (h2 - remove2 + MOD2) % MOD2;
            h2 = (h2 * BASE2 + s[i + L - 1]) % MOD2;
            
            counts[{h1, h2}]++;
        }
        
        long long ans = 0;
        for (auto const& [key, count] : counts) {
            ans += (long long)count * (count - 1) / 2;
        }
        
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    int L;
    if (getline(cin, s) && cin >> L) {
        Solution solution;
        cout << solution.countPairs(s, L) << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countPairs(s, L) {
    const n = s.length;
    if (L > n) return 0;
    
    const MOD1 = 1000000007n;
    const BASE1 = 313n;
    const MOD2 = 1000000009n;
    const BASE2 = 317n;
    
    const counts = new Map();
    
    let h1 = 0n, h2 = 0n;
    let p1 = 1n, p2 = 1n;
    
    for (let i = 0; i < L - 1; i++) {
      p1 = (p1 * BASE1) % MOD1;
      p2 = (p2 * BASE2) % MOD2;
    }
    
    for (let i = 0; i < L; i++) {
      const val = BigInt(s.charCodeAt(i));
      h1 = (h1 * BASE1 + val) % MOD1;
      h2 = (h2 * BASE2 + val) % MOD2;
    }
    
    const getKey = (a, b) => a.toString() + "," + b.toString();
    
    let key = getKey(h1, h2);
    counts.set(key, 1);
    
    for (let i = 1; i <= n - L; i++) {
      const valRemove = BigInt(s.charCodeAt(i - 1));
      const valAdd = BigInt(s.charCodeAt(i + L - 1));
      
      let remove1 = (valRemove * p1) % MOD1;
      h1 = (h1 - remove1 + MOD1) % MOD1;
      h1 = (h1 * BASE1 + valAdd) % MOD1;
      
      let remove2 = (valRemove * p2) % MOD2;
      h2 = (h2 - remove2 + MOD2) % MOD2;
      h2 = (h2 * BASE2 + valAdd) % MOD2;
      
      key = getKey(h1, h2);
      counts.set(key, (counts.get(key) || 0) + 1);
    }
    
    let ans = 0n;
    for (const count of counts.values()) {
      const c = BigInt(count);
      ans += (c * (c - 1n)) / 2n;
    }
    
    return ans.toString();
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length < 2) return;
  const s = data[0];
  const L = parseInt(data[1]);

  const solution = new Solution();
  console.log(solution.countPairs(s, L));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `aaaa`, `L=2`.

**Iter 0 (i=0):**
- Substring "aa". Hash pair (X, Y).
- Map: `{(X,Y): 1}`.

**Iter 1 (i=1):**
- Substring "aa". Hash pair (X, Y).
- Map: `{(X,Y): 2}`.

**Iter 2 (i=2):**
- Substring "aa". Hash pair (X, Y).
- Map: `{(X,Y): 3}`.

**Calc:**
- Count = 3.
- Pairs = $3 \times 2 / 2 = 3$.

## ✅ Proof of Correctness

### Invariant
We iterate through all possible substrings of length `L`.
Double hashing ensures unique identification of substring content.
Grouping counts allows combinatorial calculation of pairs.

## 💡 Interview Extensions

- **Extension 1:** Find the most frequent substring of length `L`.
  - *Answer:* Return max value in Map.
- **Extension 2:** Longest substring that appears at least K times.
  - *Answer:* Binary search on Length + Hashing.

## Common Mistakes to Avoid

1. **Integer Overflow**
   - ❌ Wrong: Using `int` for answer.
   - ✅ Correct: Use `long` (64-bit).
2. **Single Hash**
   - ❌ Wrong: Using one hash.
   - ✅ Correct: Double hash minimizes collision risk significantly.

## Related Concepts

- **Rabin-Karp:** The core hashing mechanism.
- **Suffix Automaton:** Can solve this without hashing in $O(N)$.
