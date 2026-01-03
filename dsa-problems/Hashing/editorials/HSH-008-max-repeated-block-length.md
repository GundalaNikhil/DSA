---
problem_id: HSH_MAX_REPEATED_BLOCK_LENGTH__5827
display_id: HSH-008
slug: max-repeated-block-length
title: "Longest Non-Overlapping Repeating Substring"
difficulty: Hard
difficulty_score: 65
topics:
  - Hashing
  - Binary Search
  - String Algorithms
tags:
  - hashing
  - binary-search
  - substring
  - hard
premium: true
subscription_tier: basic
---

# HSH-008: Longest Non-Overlapping Repeating Substring

## 📋 Problem Summary

You are given a string `s`. Find the maximum length `K` such that there exists a substring of length `K` that appears at least twice in `s` **without overlapping**.

## 🌍 Real-World Scenario

**Scenario Title:** The Genetic Motif Hunter 🧬

### The Problem
In genomic analysis, detecting repeated motifs (sequences) is crucial, but overlaps can be misleading.
- **Example:** In `AAAAA`, the substring `AA` appears at indices 0, 1, 2, 3. `AA` at 0 overlaps with `AA` at 1.
- **Goal:** Find repeats that are completely distinct, indicating separate functional units or gene duplications separated by other genetic material.
- **Application:** Identifying Transposable Elements (TEs) or Copy Number Variations (CNVs) where a distinct chunk of DNA is copied elsewhere.

### Why This Matters
- **Bioinformatics:** Distinguishing tandem repeats (adjacent, often overlapping) from dispersed repeats (non-overlapping).
- **Data Compression:** Finding non-overlapping blocks allows replacing the second occurrence with a reference to the first (LZ77).

### Constraints in Real World
- **Scale:** Genomes are huge ($10^9$). $O(N^2)$ is impossible. We need $O(N \log N)$ or linear approaches.

## Detailed Explanation

### Concept Visualization

String: `banana`
- Try Length 2: `ba` (at 0), `na` (at 2), `na` (at 4).
  - `na` is at index 2 and 4.
  - End of first `na` is $2+2-1 = 3$. Start of second is $4$.
  - $4 > 3$. No overlap!
  - Valid Length: 2.
- Try Length 3: `ban` (at 0), `ana` (at 1), `nan` (at 2), `ana` (at 3).
  - `ana` at 1 and 3.
  - Overlap? Index 1 ends at $1+3-1=3$. Index 3 starts at 3. Overlap at index 3.
  - Wait, strict non-overlap means $start_2 \ge start_1 + length$.
  - $3 \ge 1+3$? $3 < 4$. Overlap.
  - Invalid Length: 3.

```mermaid
graph TD
    Str[String: a b a b a]
    
    subgraph Overlapping (Len 3)
    Sub1[aba at 0]
    Sub2[aba at 2]
    Overlap[Overlap at index 2!]
    Sub1 -.-> Overlap
    Sub2 -.-> Overlap
    Result1[Invalid]
    end
    
    subgraph Non-Overlapping (Len 2)
    SubA[ab at 0]
    SubB[ab at 2]
    Gap[End 1 = 1, Start 2 = 2]
    SubA -.-> Gap
    SubB -.-> Gap
    Result2[Valid!]
    end
    
    style Result1 fill:#ffcccc
    style Result2 fill:#d4f4dd
```

### Algorithm Flow Diagram

```mermaid
graph TD
    Start[Start] --> BinSearch[Binary Search Len from 0 to N/2]
    BinSearch --> Check{Check Length L}
    
    Check --> HashInit[Compute Rolling Hash for first L chars]
    HashInit --> Map[Map: Hash -> First Index]
    HashInit --> Slide[Slide Window]
    
    Slide --> UpdateH[Update Hash]
    UpdateH --> Exists{Hash in Map?}
    
    Exists -- Yes --> OverlapCheck{CurrIdx >= FirstIdx + L?}
    OverlapCheck -- Yes --> Valid[Found! Return True]
    OverlapCheck -- No --> Slide
    
    Exists -- No --> Store[Map[Hash] = CurrIdx]
    Store --> Slide
    
    Valid --> Increase[Ans = L, Low = Mid + 1]
    Slide -- End of String --> Invalid[Return False]
    Invalid --> Decrease[High = Mid - 1]
    
    style Valid fill:#d4f4dd
    style Invalid fill:#ffcccc
```

## 🎯 Edge Cases to Test

1.  **No Repeats**
    -   Input: `"abcdef"`
    -   Output: `0`
2.  **Full Repeat**
    -   Input: `"abcabc"`
    -   Output: `3` ("abc" and "abc")
3.  **Overlapping Repeats Only**
    -   Input: `"aaaa"`
    -   Max Non-Overlapping: `2` ("aa" at 0, "aa" at 2).
    -   ("aaa" at 0 and 1 overlaps).
4.  **Adjacent Repeats**
    -   Input: `"aabb"`
    -   Output: `1` ("a" or "b").

## ✅ Input/Output Clarifications

-   **Input:** String `s`.
-   **Output:** Integer `K` (Max length).
-   **Overlap Definition:** Two substrings starting at `i` and `j` ($i < j$) do not overlap if `j >= i + K`.
-   **Max Answer:** The max possible answer is `N/2`.

## Naive Approach

### Intuition
Check all possible lengths `L`. For each `L`, exhaustive check.

### Time Complexity
-   $O(N^3)$: Check all lengths ($N$), generate all substrings ($N$), compare all ($N$).

## Optimal Approach (Binary Search + Hashing)

### Key Insight
1.  **Monotonicity:** If a repeating non-overlapping substring of length `L` exists, then one of length `L-1` definitely exists (just take a prefix).
    -   This allows **Binary Search** on the answer.
2.  **Efficient Check:** For a fixed length `L`, we can use **Rolling Hash** to find duplicates in $O(N)$.
    -   Store the **first index** of every hash encountered.
    -   When seeing a hash again at `curr_index`, check `curr_index >= first_index + L`.

### Algorithm
1.  Binary Search `len` from `0` to `N/2`.
2.  `check(len)`:
    -   Use Rolling Hash.
    -   Store `Map<Hash, FirstIndex>`.
    -   Iterate through string.
    -   If hash exists: check non-overlap condition. If satisfied, return `True`.
    -   If hash doesn't exist: store `(Hash, CurrIndex)`.
    -   Return `False`.
3.  Return max valid `len`.

### Time Complexity
-   **O(N log N)**: Binary search takes $O(\log N)$ steps. Each check takes $O(N)$.

### Space Complexity
-   **O(N)**: To store hashes in the map.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;
    
    public int maxRepeatedBlockLength(String s) {
        int n = s.length();
        int low = 0, high = n / 2;
        int ans = 0;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                low = mid + 1;
                continue;
            }
            
            if (check(s, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
    
    private boolean check(String s, int len) {
        int n = s.length();
        Map<Long, Integer> firstOccurrence = new HashMap<>();
        
        long currentHash = 0;
        long power = 1;
        
        // Precompute BASE^(len-1)
        for (int i = 0; i < len - 1; i++) {
            power = (power * BASE) % MOD;
        }
        
        // Initial window
        for (int i = 0; i < len; i++) {
            currentHash = (currentHash * BASE + s.charAt(i)) % MOD;
        }
        firstOccurrence.put(currentHash, 0);
        
        // Slide window
        for (int i = 1; i <= n - len; i++) {
            // Remove char at i-1
            long remove = (s.charAt(i - 1) * power) % MOD;
            currentHash = (currentHash - remove + MOD) % MOD;
            
            // Add char at i+len-1
            currentHash = (currentHash * BASE + s.charAt(i + len - 1)) % MOD;
            
            if (firstOccurrence.containsKey(currentHash)) {
                int firstIdx = firstOccurrence.get(currentHash);
                if (i >= firstIdx + len) {
                    return true;
                }
            } else {
                firstOccurrence.put(currentHash, i);
            }
        }
        
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            Solution solution = new Solution();
            System.out.println(solution.maxRepeatedBlockLength(s));
        }
        sc.close();
    }
}
```

### Python
```python
import sys

class Solution:
    def max_repeated_block_length(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        BASE = 313
        
        def check(length):
            if length == 0: return True
            
            first_occurrence = {}
            current_hash = 0
            power = pow(BASE, length - 1, MOD)
            
            # Initial window
            for i in range(length):
                current_hash = (current_hash * BASE + ord(s[i])) % MOD
            first_occurrence[current_hash] = 0
            
            # Slide window
            for i in range(1, n - length + 1):
                remove = (ord(s[i - 1]) * power) % MOD
                current_hash = (current_hash - remove + MOD) % MOD
                current_hash = (current_hash * BASE + ord(s[i + length - 1])) % MOD
                
                if current_hash in first_occurrence:
                    if i >= first_occurrence[current_hash] + length:
                        return True
                else:
                    first_occurrence[current_hash] = i
            return False

        low, high = 0, n // 2
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if mid == 0:
                low = mid + 1
                continue
            
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans

def max_repeated_block_length(s: str) -> int:
    solver = Solution()
    return solver.max_repeated_block_length(s)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(max_repeated_block_length(s))

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    int maxRepeatedBlockLength(string s) {
        int n = s.length();
        int low = 0, high = n / 2;
        int ans = 0;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                low = mid + 1;
                continue;
            }
            
            if (check(s, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
    
    bool check(const string& s, int len) {
        int n = s.length();
        unordered_map<long long, int> firstOccurrence;
        
        long long currentHash = 0;
        long long power = 1;
        
        for (int i = 0; i < len - 1; i++) {
            power = (power * BASE) % MOD;
        }
        
        for (int i = 0; i < len; i++) {
            currentHash = (currentHash * BASE + s[i]) % MOD;
        }
        firstOccurrence[currentHash] = 0;
        
        for (int i = 1; i <= n - len; i++) {
            long long remove = (s[i - 1] * power) % MOD;
            currentHash = (currentHash - remove + MOD) % MOD;
            currentHash = (currentHash * BASE + s[i + len - 1]) % MOD;
            
            if (firstOccurrence.count(currentHash)) {
                if (i >= firstOccurrence[currentHash] + len) {
                    return true;
                }
            } else {
                firstOccurrence[currentHash] = i;
            }
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (getline(cin, s)) {
        Solution solution;
        cout << solution.maxRepeatedBlockLength(s) << "\n";
    }
    
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  maxRepeatedBlockLength(s) {
    const n = s.length;
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const check = (len) => {
      if (len === 0) return true;
      
      const firstOccurrence = new Map();
      let currentHash = 0n;
      let power = 1n;
      
      for (let i = 0; i < len - 1; i++) {
        power = (power * BASE) % MOD;
      }
      
      for (let i = 0; i < len; i++) {
        const code = BigInt(s.charCodeAt(i));
        currentHash = (currentHash * BASE + code) % MOD;
      }
      firstOccurrence.set(currentHash, 0);
      
      for (let i = 1; i <= n - len; i++) {
        const removeCode = BigInt(s.charCodeAt(i - 1));
        const addCode = BigInt(s.charCodeAt(i + len - 1));
        
        let remove = (removeCode * power) % MOD;
        currentHash = (currentHash - remove + MOD) % MOD;
        currentHash = (currentHash * BASE + addCode) % MOD;
        
        if (firstOccurrence.has(currentHash)) {
          if (i >= firstOccurrence.get(currentHash) + len) {
            return true;
          }
        } else {
          firstOccurrence.set(currentHash, i);
        }
      }
      return false;
    };
    
    let low = 0, high = Math.floor(n / 2);
    let ans = 0;
    
    while (low <= high) {
      const mid = Math.floor((low + high) / 2);
      if (mid === 0) {
        low = mid + 1;
        continue;
      }
      
      if (check(mid)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
    return ans;
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
  console.log(solution.maxRepeatedBlockLength(s));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

### Input
```
banana
```
`N=6`. Range `[0, 3]`.

### Binary Search Steps

1.  **Low=0, High=3. Mid=1.**
    -   `check(1)`:
    -   Hashes: `b`, `a`, `n`, `a`, `n`, `a`.
    -   `a` at index 3 matches `a` at 1. Gap $3 - 1 = 2 \ge 1$. Valid!
    -   **Ans=1, Low=2.**
2.  **Low=2, High=3. Mid=2.**
    -   `check(2)`:
    -   Hashes of `ba`, `an`, `na`, `an`, `na`.
    -   `an` (idx 1) ... `an` (idx 3). Overlap check: $3 \ge 1 + 2$? $3 \ge 3$. True!
    -   Non-overlapping repeat found ("an" at 1 and 3).
    -   **Ans=2, Low=3.**
3.  **Low=3, High=3. Mid=3.**
    -   `check(3)`:
    -   Hashes of `ban`, `ana`, `nan`, `ana`.
    -   `ana` (idx 1) ... `ana` (idx 3).
    -   Overlap check: $3 \ge 1 + 3$? $3 \ge 4$. False!
    -   **High=2.**
4.  End. Return **Ans=2**.

## ✅ Proof of Correctness

### Binary Search Validity
If there are two disjoint substrings of length $L$, say $S[i..i+L-1]$ and $S[j..j+L-1]$ with $j \ge i+L$, then their prefixes of length $L-1$ are also disjoint (indices $i$ to $i+L-2$ vs $j$ to $j+L-2$).
Since $j \ge i+L > i+L-1$, they are definitely disjoint.
Thus, the property is monotonic.

## ⚠️ Common Mistakes to Avoid

1.  **Overlap Logic Error**
    -   ❌ Wrong: `if (i > firstIdx)` (allows overlap).
    -   ✅ Correct: `if (i >= firstIdx + len)` (strict non-overlap).
2.  **Modifying Map**
    -   ❌ Wrong: Updating `firstOccurrence` for every match. We need the *first* occurrence to maximize the gap.
    -   ✅ Correct: Only insert if hash not present.
3.  **Binary Search Boundaries**
    -   ❌ Wrong: High = N.
    -   ✅ Correct: High = N/2 (impossible to have 2 non-overlapping blocks > N/2).

## 💡 Interview Extensions

1.  **Allow Overlaps**
    -   *Extension:* Longest Repeating Substring (overlaps allowed).
    -   *Answer:* Remove the `+ length` check. Or use **Suffix Array** + **LCP Array** (Max LCP value).
2.  **K-th Repeating**
    -   *Extension:* Find substring appearing $K$ times.
    -   *Answer:* Check specific count in hash map.
