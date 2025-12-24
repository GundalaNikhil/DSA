---
problem_id: HSH_MINIMAL_ROTATION_HASH__4729
display_id: HSH-006
slug: minimal-rotation-hash
title: "Minimal Rotation via Hash Compare"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - String Algorithms
  - Rotation
tags:
  - hashing
  - rotation
  - lexicographic
  - medium
premium: true
subscription_tier: basic
---

# HSH-006: Minimal Rotation via Hash Compare

## 📋 Problem Summary

You are given a string `s`. You need to find the **lexicographically smallest rotation** of `s`.
A rotation is formed by moving a prefix to the end.
Example: "bba" -> "bab" -> "abb". Smallest is "abb".

## 🌍 Real-World Scenario

**Scenario Title:** Canonical Representation of Cyclic Data

Imagine you are storing cyclic chemical structures (like benzene rings) or circular DNA plasmids in a database.
- "ABCDEF" and "BCDEFA" represent the exact same circular structure.
- To store them uniquely (canonicalization), you need a standard form.
- The "lexicographically smallest rotation" is a common choice for this standard form.
- By converting all cyclic variations to this form, you can easily check if two structures are identical.

![Real-World Application](../images/HSH-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Comparing Rotations

String: "banana"
Rotations:
1. "banana"
2. "ananab"
3. "nanaba"
4. "anaban"
5. "nabana"
6. "abanan"

To find the smallest, we can compare any two rotations.
Compare "ananab" vs "anaban":
- "ana" matches.
- Next char: 'n' vs 'b'.
- 'b' < 'n', so "anaban" is smaller.

### Key Concept: Efficient Comparison

Comparing two strings of length `N` takes `O(N)`. Doing this for all `N` rotations takes `O(N^2)`.
We can speed up the comparison using **Hashing + Binary Search**.
- To compare Rotation A and Rotation B:
  - Find the length of the Longest Common Prefix (LCP) using binary search and hashing.
  - Let LCP length be `L`.
  - Compare the characters at index `L`.
  - This takes `O(log N)` instead of `O(N)`.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`.
- **Output:** The smallest rotation string.
- **Constraints:** `|s| <= 2 * 10^5`. `O(N^2)` is too slow. `O(N log N)` or `O(N)` is required.
- **Note:** Booth's Algorithm solves this in `O(N)`, but the problem specifically asks for Hashing (`O(N log N)`).

## Naive Approach

### Intuition

Generate all rotations and sort them.

### Algorithm

1. Create a list of all rotations.
2. Sort the list.
3. Return the first element.

### Time Complexity

- **O(N^2 \log N)**: Sorting `N` strings of length `N`. Too slow.

## Optimal Approach (Hashing)

### Key Insight

1. Concatenate `s + s` to easily access any rotation as a substring of length `N`.
2. Use **Rolling Hash** to compute hashes of substrings in `O(1)`.
3. Keep track of the `best_start_index` (initially 0).
4. Iterate `current_start` from 1 to `N-1`.
5. Compare rotation at `best_start` vs `current_start`:
   - Use Binary Search to find the first mismatching character.
   - Check hashes of prefixes. If hashes match, LCP is longer.
   - Once mismatch index `k` is found, compare characters `(s+s)[best+k]` and `(s+s)[current+k]`.
   - Update `best_start` if `current` is smaller.

### Algorithm

1. `doubled = s + s`.
2. Compute prefix hashes for `doubled`.
3. `best = 0`.
4. Loop `curr` from 1 to `n-1`:
   - Compare rotation starting at `best` vs `curr`.
   - Binary search `len` in `[0, n]`.
   - `check(len)`: `hash(best, best+len-1) == hash(curr, curr+len-1)`.
   - Find max `len` where hashes match (LCP).
   - If `LCP == n`, strings are equal.
   - Else, compare chars at `best + LCP` and `curr + LCP`.
   - If `doubled[curr + LCP] < doubled[best + LCP]`, `best = curr`.
5. Return `doubled.substring(best, best + n)`.

### Time Complexity

- **O(N \log N)**: `N` comparisons, each takes `O(log N)` with binary search.

### Space Complexity

- **O(N)**: Hash arrays.

![Algorithm Visualization](../images/HSH-006/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;
    
    public String minimalRotation(String s) {
        int n = s.length();
        String doubled = s + s;
        int m = doubled.length();
        
        long[] h = new long[m + 1];
        long[] p = new long[m + 1];
        p[0] = 1;
        
        for (int i = 0; i < m; i++) {
            h[i + 1] = (h[i] * BASE + doubled.charAt(i)) % MOD;
            p[i + 1] = (p[i] * BASE) % MOD;
        }
        
        int best = 0;
        for (int curr = 1; curr < n; curr++) {
            // Compare rotation at 'best' vs 'curr'
            int lcp = getLCP(h, p, best, curr, n);
            if (lcp < n) {
                if (doubled.charAt(curr + lcp) < doubled.charAt(best + lcp)) {
                    best = curr;
                }
            }
        }
        
        return doubled.substring(best, best + n);
    }
    
    private int getLCP(long[] h, long[] p, int i, int j, int maxLen) {
        int low = 0, high = maxLen;
        int ans = 0;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                low = mid + 1;
                continue;
            }
            
            long h1 = getHash(h, p, i, i + mid - 1);
            long h2 = getHash(h, p, j, j + mid - 1);
            
            if (h1 == h2) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
    
    private long getHash(long[] h, long[] p, int l, int r) {
        int len = r - l + 1;
        long val = (h[r + 1] - (h[l] * p[len]) % MOD + MOD) % MOD;
        return val;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            Solution solution = new Solution();
            System.out.println(solution.minimalRotation(s));
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
    def minimal_rotation(self, s: str) -> str:
        n = len(s)
        doubled = s + s
        m = len(doubled)
        
        MOD = 10**9 + 7
        BASE = 313
        
        h = [0] * (m + 1)
        p = [1] * (m + 1)
        
        for i in range(m):
            h[i+1] = (h[i] * BASE + ord(doubled[i])) % MOD
            p[i+1] = (p[i] * BASE) % MOD
            
        def get_hash(l, r):
            length = r - l + 1
            return (h[r+1] - h[l] * p[length]) % MOD
            
        def get_lcp(i, j):
            low, high = 0, n
            ans = 0
            while low <= high:
                mid = (low + high) // 2
                if mid == 0:
                    low = mid + 1
                    continue
                
                h1 = get_hash(i, i + mid - 1)
                h2 = get_hash(j, j + mid - 1)
                
                if h1 == h2:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
            
        best = 0
        for curr in range(1, n):
            lcp = get_lcp(best, curr)
            if lcp < n:
                if doubled[curr + lcp] < doubled[best + lcp]:
                    best = curr
                    
        return doubled[best : best + n]

def minimal_rotation(s: str) -> str:
    solver = Solution()
    return solver.minimal_rotation(s)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(minimal_rotation(s))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    string minimalRotation(string s) {
        int n = s.length();
        string doubled = s + s;
        int m = doubled.length();
        
        vector<long long> h(m + 1, 0), p(m + 1, 1);
        
        for (int i = 0; i < m; i++) {
            h[i + 1] = (h[i] * BASE + doubled[i]) % MOD;
            p[i + 1] = (p[i] * BASE) % MOD;
        }
        
        int best = 0;
        for (int curr = 1; curr < n; curr++) {
            int lcp = getLCP(h, p, best, curr, n);
            if (lcp < n) {
                if (doubled[curr + lcp] < doubled[best + lcp]) {
                    best = curr;
                }
            }
        }
        
        return doubled.substr(best, n);
    }
    
    int getLCP(const vector<long long>& h, const vector<long long>& p, int i, int j, int maxLen) {
        int low = 0, high = maxLen;
        int ans = 0;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                low = mid + 1;
                continue;
            }
            
            long long h1 = getHash(h, p, i, i + mid - 1);
            long long h2 = getHash(h, p, j, j + mid - 1);
            
            if (h1 == h2) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
    
    long long getHash(const vector<long long>& h, const vector<long long>& p, int l, int r) {
        int len = r - l + 1;
        long long val = (h[r + 1] - (h[l] * p[len]) % MOD + MOD) % MOD;
        return val;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (getline(cin, s)) {
        Solution solution;
        cout << solution.minimalRotation(s) << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minimalRotation(s) {
    const n = s.length;
    const doubled = s + s;
    const m = doubled.length;
    
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const h = new BigInt64Array(m + 1);
    const p = new BigInt64Array(m + 1);
    p[0] = 1n;
    
    for (let i = 0; i < m; i++) {
      const code = BigInt(doubled.charCodeAt(i));
      h[i + 1] = (h[i] * BASE + code) % MOD;
      p[i + 1] = (p[i] * BASE) % MOD;
    }
    
    const getHash = (l, r) => {
      const len = r - l + 1;
      let val = (h[r + 1] - (h[l] * p[len]) % MOD) % MOD;
      if (val < 0n) val += MOD;
      return val;
    };
    
    const getLCP = (i, j) => {
      let low = 0, high = n;
      let ans = 0;
      while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if (mid === 0) {
          low = mid + 1;
          continue;
        }
        
        const h1 = getHash(i, i + mid - 1);
        const h2 = getHash(j, j + mid - 1);
        
        if (h1 === h2) {
          ans = mid;
          low = mid + 1;
        } else {
          high = mid - 1;
        }
      }
      return ans;
    };
    
    let best = 0;
    for (let curr = 1; curr < n; curr++) {
      const lcp = getLCP(best, curr);
      if (lcp < n) {
        if (doubled.charCodeAt(curr + lcp) < doubled.charCodeAt(best + lcp)) {
          best = curr;
        }
      }
    }
    
    return doubled.substring(best, best + n);
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
  const s = data[0];

  const solution = new Solution();
  console.log(solution.minimalRotation(s));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
bba
```
`doubled` = "bbabba"

**Iteration 1 (curr=1):**
- Compare "bba..." (best=0) vs "bab..." (curr=1).
- LCP("bba...", "bab...")?
  - Len 1: 'b' vs 'b'. Match.
  - Len 2: 'bb' vs 'ba'. Mismatch.
- LCP = 1.
- Compare char at index 1: `doubled[0+1]`='b', `doubled[1+1]`='a'.
- 'a' < 'b', so `curr` is better. `best = 1`.

**Iteration 2 (curr=2):**
- Compare "bab..." (best=1) vs "abb..." (curr=2).
- LCP("bab...", "abb...")?
  - Len 1: 'b' vs 'a'. Mismatch.
- LCP = 0.
- Compare char at index 0: `doubled[1+0]`='b', `doubled[2+0]`='a'.
- 'a' < 'b', so `curr` is better. `best = 2`.

**End:**
Return `doubled.substring(2, 5)` = "abb".

## ✅ Proof of Correctness

### Invariant
At step `i`, `best` holds the starting index of the lexicographically smallest rotation found among indices `0` to `i`.
Comparing two strings using LCP + next char correctly determines lexicographical order.
Binary search + Hashing finds LCP in `O(log N)`.

## 💡 Interview Extensions

- **Extension 1:** Solve in `O(N)` time.
  - *Answer:* Booth's Algorithm (Least Rotation) or Duval's Algorithm (Lyndon Factorization).
- **Extension 2:** Find *maximal* rotation.
  - *Answer:* Same logic, just flip the comparison condition.

### Common Mistakes to Avoid

1. **Comparing Hashes Directly**
   - ❌ Wrong: `if (hash(rot1) < hash(rot2))` - Hashes are random numbers, not lexicographical.
   - ✅ Correct: Use hashes only for equality check in LCP. Compare actual characters for order.
2. **Modulo Arithmetic**
   - ❌ Wrong: Forgetting negative results in subtraction.
   - ✅ Correct: `(a - b + MOD) % MOD`.

## Related Concepts

- **Booth's Algorithm:** `O(N)` specific algorithm for this problem.
- **Suffix Array:** Can solve this by sorting suffixes of `s+s`.
