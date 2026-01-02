---
problem_id: HSH_DETECT_PERIOD_STRING__6183
display_id: HSH-007
slug: detect-period-string
title: "Detect Period of String"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - String Algorithms
  - Periodicity
tags:
  - hashing
  - period
  - pattern
  - medium
premium: true
subscription_tier: basic
---

# HSH-007: Detect Period of String

## 📋 Problem Summary

You are given a string `s`. You need to find the smallest length `p` such that `s` is composed of the prefix `s[0..p-1]` repeated multiple times, effectively meaning the string has a period `p`. If no such `p` exists (other than the string itself), return the length of `s`.

## 🌍 Real-World Scenario

**Scenario Title:** The Heartbeat Signal Compressor ❤️

### The Problem
You are designing a storage system for a medical device that records heartbeats.
- **Data:** A continuous stream of digital samples: `10, 20, 10, 20, 10, 20...`
- **Goal:** Instead of storing millions of data points, detect if the signal is periodic.
- **Compression:** If the signal is just `[10, 20]` repeated, you only store the pattern `[10, 20]` and the count. This reduces storage by 99%.

### Why This Matters
- **Data Compression:** Run-Length Encoding and variants rely on finding repeating patterns.
- **Cryptography:** Analyzing periodicities in ciphertexts to break encryption (e.g., Vigenère cipher).
- **Physics:** Finding the fundamental frequency of a wave.

### Constraints in Real World
- **Speed:** The check must be fast ($O(N)$ or near-linear), not quadratic.
- **False Positives:** Must be exact. A single mismatch means it's not periodic.

## Detailed Explanation

### Concept Visualization

A string `S` has period `P` if it consists of blocks of length `P`.
Example: `ababab` (Length 6).
Blocks: `ab`, `ab`, `ab`. Period = 2.

**The "Shift" Trick:**
If `S` has period `P`, then looking at `S` shifted by `P` positions should align perfectly with the original `S`, except for the ends.
Specifically, the prefix of length $N-P$ must equal the suffix of length $N-P$.

```mermaid
graph TD
    S[String: a b a b a b]
    
    subgraph Shift Check (P=2)
    Prefix[Prefix N-2: a b a b]
    Suffix[Suffix N-2: a b a b]
    Match{Prefix == Suffix?}
    Match -- Yes --> Periodic
    end
    
    subgraph Indices
    P1[Ind: 0 1 2 3]
    P2[Ind: 2 3 4 5]
    end
    
    style Match fill:#d4f4dd
```

### Algorithm Flow Diagram

```mermaid
graph TD
    Start[Start] --> Div[Find Divisors of N]
    Div --> Sort[Sort Divisors Ascending]
    Sort --> Init[Compute Rolling Hashes]
    Init --> Loop{For each divisor P}
    
    Loop -- P < N --> Check[Check Hash: S[0..N-P-1] == S[P..N-1]]
    Check -- Equal --> Found[Return P]
    Check -- Not Equal --> Loop
    
    Loop -- No More P --> ReturnN[Return N]
    Found --> End
    ReturnN --> End
    
    style Found fill:#d4f4dd
    style ReturnN fill:#fff0e6
```

## 🎯 Edge Cases to Test

1.  **Single Character**
    -   Input: `"a"`
    -   Output: `1`
2.  **All Same Characters**
    -   Input: `"aaaa"`
    -   Divisors: 1, 2, 4.
    -   Check 1: `S[0..2] == S[1..3]` ("aaa" vs "aaa") -> Match.
    -   Output: `1` (Correct).
3.  **No Repetition**
    -   Input: `"abacaba"`
    -   Output: `7` (Length of string).
4.  **Prime Length String**
    -   Input: `"abc"`
    -   Output: `3`.
5.  **Multiple Periods**
    -   Input: `"abababab"` (Len 8)
    -   Divisors: 1, 2, 4, 8.
    -   1 fails ("abababa" != "bababab").
    -   2 succeeds ("ababab" == "ababab").
    -   Output: `2`.

## ✅ Input/Output Clarifications

-   **Input:** String `s`.
-   **Output:** Smallest period length `P`.
-   **Divisors Only:** A string of length $N$ can only have a period $P$ if $N$ is divisible by $P$.
    -   Counter-example: `aba` (Len 3). Period could be 2 ("ab" + "a" cut off)?
    -   **Problem Definition:** Usually "composed of prefix repeated". This implies $N \% P == 0$.
    -   The solution assumes strict modification where entire string is covered by full repetitions.

## Naive Approach

### Intuition
For every possible length `P` from 1 to `N/2`:
1.  Check if `N % P == 0`.
2.  Construct the string by repeating `s[0..P-1]`.
3.  Compare strictly.

### Algorithm
1.  Iterate `P` from 1 to `N`.
2.  If `N % P == 0`:
    -   Build `Pattern = s[0..P-1]`.
    -   Build `Candidate = Pattern * (N/P)`.
    -   If `Candidate == s`, return `P`.

### Complexity Visualization

| Approach | Time Complexity | Space Complexity | Feasibility for N=200K |
| :--- | :---: | :---: | :---: |
| Naive Build | O(N × Divisors) | O(N) | ✅ Acceptable (Divisors small) |
| **Hashing** | **O(N + Divisors)** | **O(N)** | ✅ Fastest & Cleanest |
| KMP Algo | O(N) | O(N) | ✅ Optimal (Hard to implement) |

### Why This Fails
It doesn't strictly fail, but building strings is standard "wasteful" practice in interviews. Hashing allows in-place checks.

## Optimal Approach (Hashing + Divisors)

### Key Insight
We used the "Shift Trick":
`S` has period `P` if and only if `Prefix(N-P) == Suffix(N-P)`.
This checks $S[i] == S[i+P]$ for all $i$.
Combined with the requirement that $P$ divides $N$, this is sufficient.

### Algorithm
1.  Compute prefix hashes of `s` ($O(N)$).
2.  Find all divisors of `N` up to $\sqrt{N}$ ($O(\sqrt{N})$).
3.  Sort divisors ($O(D \log D)$).
4.  For each divisor `P` in increasing order:
    -   Check if `getHash(0, N-P-1) == getHash(P, N-1)`.
    -   If yes, return `P`.
5.  If no divisor works, return `N`.

### Time Complexity
-   **O(N + D)**: $N$ for hashing, $D$ number of divisors checks ($O(1)$ each). Max divisors for $2 \cdot 10^5$ is 160. Very fast.

### Space Complexity
-   **O(N)**: Rolling hash arrays.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;
    
    public int detectPeriod(String s) {
        int n = s.length();
        long[] h = new long[n + 1];
        long[] p = new long[n + 1];
        p[0] = 1;
        
        for (int i = 0; i < n; i++) {
            h[i + 1] = (h[i] * BASE + s.charAt(i)) % MOD;
            p[i + 1] = (p[i] * BASE) % MOD;
        }
        
        // Find divisors
        List<Integer> divisors = new ArrayList<>();
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                divisors.add(i);
                if (i * i != n) {
                    divisors.add(n / i);
                }
            }
        }
        Collections.sort(divisors);
        
        for (int len : divisors) {
            if (len == n) return n;
            
            // Check if prefix(n-len) == suffix(n-len)
            // S[0...n-len-1] vs S[len...n-1]
            long h1 = getHash(h, p, 0, n - len - 1);
            long h2 = getHash(h, p, len, n - 1);
            
            if (h1 == h2) return len;
        }
        
        return n;
    }
    
    private long getHash(long[] h, long[] p, int l, int r) {
        int len = r - l + 1;
        long val = (h[r + 1] - (h[l] * p[len]) % MOD + MOD) % MOD;
        return val;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            Solution solution = new Solution();
            System.out.println(solution.detectPeriod(s));
        }
        sc.close();
    }
}
```

### Python
```python
import sys

class Solution:
    def detect_period(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        BASE = 313
        
        h = [0] * (n + 1)
        p = [1] * (n + 1)
        
        for i in range(n):
            h[i+1] = (h[i] * BASE + ord(s[i])) % MOD
            p[i+1] = (p[i] * BASE) % MOD
            
        def get_hash(l, r):
            length = r - l + 1
            return (h[r+1] - h[l] * p[length]) % MOD
            
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
        divisors.sort()
        
        for length in divisors:
            if length == n:
                return n
            
            # Check s[0...n-length-1] == s[length...n-1]
            h1 = get_hash(0, n - length - 1)
            h2 = get_hash(length, n - 1)
            
            if h1 == h2:
                return length
                
        return n

def detect_period(s: str) -> int:
    solver = Solution()
    return solver.detect_period(s)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(detect_period(s))

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    int detectPeriod(string s) {
        int n = s.length();
        vector<long long> h(n + 1, 0), p(n + 1, 1);
        
        for (int i = 0; i < n; i++) {
            h[i + 1] = (h[i] * BASE + s[i]) % MOD;
            p[i + 1] = (p[i] * BASE) % MOD;
        }
        
        vector<int> divisors;
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                divisors.push_back(i);
                if (i * i != n) {
                    divisors.push_back(n / i);
                }
            }
        }
        sort(divisors.begin(), divisors.end());
        
        for (int len : divisors) {
            if (len == n) return n;
            
            long long h1 = getHash(h, p, 0, n - len - 1);
            long long h2 = getHash(h, p, len, n - 1);
            
            if (h1 == h2) return len;
        }
        
        return n;
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
        cout << solution.detectPeriod(s) << "\n";
    }
    
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  detectPeriod(s) {
    const n = s.length;
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const h = new BigInt64Array(n + 1);
    const p = new BigInt64Array(n + 1);
    p[0] = 1n;
    
    for (let i = 0; i < n; i++) {
      const code = BigInt(s.charCodeAt(i));
      h[i + 1] = (h[i] * BASE + code) % MOD;
      p[i + 1] = (p[i] * BASE) % MOD;
    }
    
    const getHash = (l, r) => {
      const len = r - l + 1;
      let val = (h[r + 1] - (h[l] * p[len]) % MOD) % MOD;
      if (val < 0n) val += MOD;
      return val;
    };
    
    const divisors = [];
    for (let i = 1; i * i <= n; i++) {
      if (n % i === 0) {
        divisors.push(i);
        if (i * i !== n) divisors.push(n / i);
      }
    }
    divisors.sort((a, b) => a - b);
    
    for (const len of divisors) {
      if (len === n) return n;
      
      const h1 = getHash(0, n - len - 1);
      const h2 = getHash(len, n - 1);
      
      if (h1 === h2) return len;
    }
    
    return n;
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
  console.log(solution.detectPeriod(s));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

### Input
```
ababab
```
`N = 6`. Divisors: 1, 2, 3, 6.

### Execution Table
**Target Comparison:** `S[0...N-P-1]` vs `S[P...N-1]`

| P (Divisor) | Range 1 `S[0...N-P-1]` | Range 2 `S[P...N-1]` | Content R1 | Content R2 | Match? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | `0` to `4` | `1` to `5` | "ababa" | "babab" | ❌ No | Continue |
| **2** | `0` to `3` | `2` to `5` | "abab" | "abab" | ✅ Yes | **Return 2** |

Result: `2`.

## ✅ Proof of Correctness

### Implication Direction
If `S` has period `P`, then $S[i] = S[i+P]$ for all $0 \le i < N-P$.
This is exactly equivalent to equality of the prefix of length $N-P$ and the suffix of same length starting at $P$.
We iterate divisors in increasing order to find the *smallest* valid `P`.

## ⚠️ Common Mistakes to Avoid

1.  **Forgetting to Sort Divisors**
    -   ❌ Wrong: Checking divisors in random order reduces finding the *smallest* period.
    -   ✅ Correct: Sort them.
2.  **Using `int` for Divisors logic**
    -   ❌ Wrong: `i * i <= n` can overflow if `n` is `Integer.MAX_VALUE` (rare but possible).
    -   ✅ Correct: Loop condition usually safe for typical $N \le 2\times 10^5$.
3.  **Boundary Conditions**
    -   ❌ Wrong: Comparing wrong ranges.
    -   ✅ Correct: `0` to `n-p-1` and `p` to `n-1`.

## 💡 Interview Extensions

1.  **Using KMP Failure Function**
    -   *Extension:* How to solve in strictly $O(N)$?
    -   *Answer:* Compute `pi` array. Let `len = pi[N-1]`. If `N % (N - len) == 0` and `len > 0`, period is `N - len`. Else `N`.
2.  **Z-Algorithm**
    -   *Answer:* Check if `N` is divisible by `p` and `Z[p] == N - p`.

## Related Concepts

-   **KMP Algorithm:** Essential for period detection.
-   **String Borders:** A border is a prefix that is also a suffix. Fundamental to this problem.
