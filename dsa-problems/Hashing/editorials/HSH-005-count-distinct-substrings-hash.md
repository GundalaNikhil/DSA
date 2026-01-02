---
problem_id: HSH_COUNT_DISTINCT_SUBSTRINGS__8741
display_id: HSH-005
slug: count-distinct-substrings-hash
title: "Count Distinct Substrings"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - String Algorithms
  - Set Operations
tags:
  - hashing
  - substring
  - distinct
  - medium
premium: true
subscription_tier: basic
---

# HSH-005: Count Distinct Substrings

## 📋 Problem Summary

You are given a string `s`. Your task is to count the total number of **distinct** substrings, including the empty string.
For example, in "aaa", the substrings are "", "a", "a", "a", "aa", "aa", "aaa".
Distinct ones: "", "a", "aa", "aaa". Count = 4.

## 🌍 Real-World Scenario

**Scenario Title:** The Search Engine Indexer 🔍

### The Problem
You are building the autocomplete feature for a search engine. When a user types a query, you want to suggest completions based on phrases that exist in your database.
- **Goal:** Build an index of all unique phrases (substrings) contained in a set of documents.
- **Challenge:** A document might contain the phrase "data science" 50 times. You only need to store it once.
- **Metric:** Determining the "richness" of a vocabulary (e.g., in a book) by counting unique substrings.

### Why This Matters
- **Compression:** Lempel-Ziv (LZ77) compression works by finding repeated substrings. Counting distinct substrings helps estimate compressibility.
- **Bioinformatics:** Measuring DNA sequence complexity. High distinct substring count = high information entropy.
- **Plagiarism:** Specialized algorithms compare the set of distinct substrings to find finding partial matches.

### Constraints in Real World
- **Scale:** If text size $N = 100,000$, total substrings = $5 \times 10^9$. We can't store them all.
- **Suffix Approach:** For massive scale, we use Suffix Trees ($O(N)$). For this problem context, we explore the **Hashing** approach ($O(N^2)$).

## Detailed Explanation

### Concept Visualization

We need to generate every possible substring and throw them into a "Unique Filter" (Set).

```mermaid
graph LR
    Input[String: aaa] --> Gen[Generate All Substrings]
    Gen --> Sub1["a"]
    Gen --> Sub2["a"]
    Gen --> Sub3["a"]
    Gen --> Sub4["aa"]
    Gen --> Sub5["aa"]
    Gen --> Sub6["aaa"]
    
    Sub1 & Sub2 & Sub3 --> Filter{Unique Set}
    Sub4 & Sub5 --> Filter
    Sub6 --> Filter
    
    Filter --> Result["a", "aa", "aaa"]
    Result --> Count[Count = 3 + 1(empty) = 4]
    
    style Result fill:#d4f4dd
```

### Algorithm Flow Diagram

```mermaid
graph TD
    Start[Start] --> Init[Set<Long> uniqueHashes]
    Init --> LoopI{i from 0 to N-1}
    LoopI -- i < N --> ResetH[currentHash = 0]
    ResetH --> LoopJ{j from i to N-1}
    
    LoopJ -- j < N --> CalcH[currentHash = currentHash * B + s[j]]
    CalcH --> AddH[Add currentHash to Set]
    AddH --> IncJ[j++]
    IncJ --> LoopJ
    
    LoopJ -- j >= N --> IncI[i++]
    IncI --> LoopI
    
    LoopI -- i >= N --> Return[Return Set.size + 1]
    
    style AddH fill:#e6f3ff
```

## 🎯 Edge Cases to Test

1.  **Repeated Characters**
    -   Input: `"aaaa"`
    -   Distinct: `"", "a", "aa", "aaa", "aaaa"` (5)
2.  **All Distinct Characters**
    -   Input: `"abc"`
    -   Distinct: `"", "a", "b", "c", "ab", "bc", "abc"` (7)
    -   Formula: $N(N+1)/2 + 1$
3.  **Empty String**
    -   Input: `""`
    -   Distinct: `""` (1)
4.  **Alternating Characters**
    -   Input: `"abab"`
    -   Distinct: `"", "a", "b", "ab", "ba", "aba", "bab", "abab"` (8)

## ✅ Input/Output Clarifications

-   **Input:** String `s`.
-   **Output:** Integer representing count of distinct substrings.
-   **Constraints:**
    -   Algorithms based on Hashing are typically $O(N^2)$.
    -   If $N=10^5$, this will time out. Hashing solutions are suitable for $N \le 3000$.
    -   For larger $N$, Suffix Structures are required (see Interview Extensions).

## Naive Approach

### Intuition
Generate every substring as a string object and add to a `HashSet<String>`.

### Algorithm
1.  `Set<String> set = new HashSet<>()`
2.  Nested loops `i`, `j` to generate `sub = s.substring(i, j)`.
3.  `set.add(sub)`.

### Complexity Visualization

| Approach | Time Complexity | Space Complexity | Feasibility for N=1000 | Feasibility for N=100K |
| :--- | :---: | :---: | :---: | :---: |
| Naive (String Set) | O(N³) | O(N³) | ⚠️ Slow (10⁹ ops) | ❌ CRASH |
| Rolling Hash Set | O(N²) | O(N²) | ✅ Fast (10⁶ ops) | ❌ TLE (10¹⁰ ops) |
| Suffix Automaton | O(N) | O(N) | ✅ Instant | ✅ Fast |

### Why This Fails
String creation and hashing takes $O(L)$ where $L$ is length. Total time $\sum L \approx O(N^3)$. Memory also explodes storing heavily duplicated string data.

## Optimal Approach (for Hashing context)

### Key Insight
Instead of extracting substrings (expensive), we just need their **fingerprints**.
We can compute the hash of `s[i...j]` based on the hash of `s[i...j-1]` in $O(1)$.
`Hash(s[i...j]) = (Hash(s[i...j-1]) * B + s[j]) % M`
We insert these `long` values into a `HashSet`.

### Algorithm
1.  Initialize `Set<Long> hashes`.
2.  Loop `i` from 0 to `N-1` (start index):
    -   `currentHash = 0`
    -   Loop `j` from `i` to `N-1` (end index):
        -   Update `currentHash`: add `s[j]`.
        -   Add `currentHash` to `hashes`.
3.  Return `hashes.size() + 1` (for empty string).

### Time Complexity
-   **O(N^2)**: Two nested loops, $O(1)$ operations inside.

### Space Complexity
-   **O(N^2)**: In the worst case (all distinct), we store $O(N^2)$ distinct hashes.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;

    public int countDistinctSubstrings(String s) {
        int n = s.length();
        // Use a Set to store unique hashes
        // For competitive programming with N=10^5, this requires Suffix Structures.
        // This Hashing solution works for N <= 3000.
        Set<Long> distinctHashes = new HashSet<>();
        
        for (int i = 0; i < n; i++) {
            long currentHash = 0;
            for (int j = i; j < n; j++) {
                currentHash = (currentHash * BASE + s.charAt(j)) % MOD;
                distinctHashes.add(currentHash);
            }
        }
        
        // +1 for empty string
        return distinctHashes.size() + 1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            Solution solution = new Solution();
            System.out.println(solution.countDistinctSubstrings(s));
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
    def count_distinct_substrings(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        BASE = 313
        
        distinct_hashes = set()
        
        for i in range(n):
            current_hash = 0
            for j in range(i, n):
                current_hash = (current_hash * BASE + ord(s[j])) % MOD
                distinct_hashes.add(current_hash)
                
        return len(distinct_hashes) + 1

def count_distinct_substrings(s: str) -> int:
    solver = Solution()
    return solver.count_distinct_substrings(s)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(count_distinct_substrings(s))

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    int countDistinctSubstrings(string s) {
        int n = s.length();
        unordered_set<long long> distinctHashes;
        // Pre-allocate to avoid resizing overhead if possible
        // distinctHashes.reserve(n * n / 2); 
        
        for (int i = 0; i < n; i++) {
            long long currentHash = 0;
            for (int j = i; j < n; j++) {
                currentHash = (currentHash * BASE + s[j]) % MOD;
                distinctHashes.insert(currentHash);
            }
        }
        
        return distinctHashes.size() + 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (getline(cin, s)) {
        Solution solution;
        cout << solution.countDistinctSubstrings(s) << "\n";
    }
    
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  countDistinctSubstrings(s) {
    const n = s.length;
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const distinctHashes = new Set();
    
    for (let i = 0; i < n; i++) {
      let currentHash = 0n;
      for (let j = i; j < n; j++) {
        const code = BigInt(s.charCodeAt(j));
        currentHash = (currentHash * BASE + code) % MOD;
        distinctHashes.add(currentHash);
      }
    }
    
    return distinctHashes.size + 1;
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
  console.log(solution.countDistinctSubstrings(s));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

### Input
```
aba
```

### Execution Table

| Outer `i` | Inner `j` | Char | Calculation `(H*B + c)%M` | New Hash | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | **0** | a | `(0 * 313 + 97) % M` | **97** | Add {97} |
| 0 | 1 | b | `(97 * 313 + 98) % M` | **30459** | Add {97, 30459} |
| 0 | 2 | a | `(30459 * 313 + 97) % M` | **9533764** | Add {..., 9533764} |
| **1** | **1** | b | `(0 * 313 + 98) % M` | **98** | Add {..., 98} |
| 1 | 2 | a | `(98 * 313 + 97) % M` | **30771** | Add {..., 30771} |
| **2** | **2** | a | `(0 * 313 + 97) % M` | **97** | Present (skip) |

**Distinct Hashes (`distinctHashes`):** {97, 30459, 9533764, 98, 30771}
**Size:** 5
**Result:** 5 + 1 (empty) = **6**.
**Verification:** "", "a", "ab", "aba", "b", "ba". Correct (6).

## ✅ Proof of Correctness

### Invariant
At the end of the loops, `distinctHashes` contains the rolling hash of every valid substring $s[i \dots j]$.
Since the Set data structure filters duplicates, `distinctHashes.size()` equals the number of distinct substring hashes.
Assuming no hash collisions (which is approximately true for small $N$ or with double hashing), this equals the number of distinct substrings.

## ⚠️ Common Mistakes to Avoid

1.  **Forgetting Empty String**
    -   ❌ Wrong: Returning `set.size()`.
    -   ✅ Correct: Returning `set.size() + 1` (Problem statement usually counts empty string, check specific constraints).
2.  **Using String Set**
    -   ❌ Wrong: `Set<String>`. Causes MLE/TLE.
    -   ✅ Correct: `Set<Long>`.
3.  **Hash Collisions**
    -   ❌ Wrong: Using small MOD or single hash for massive datasets.
    -   ✅ Correct: Use Double Hashing or Suffix Structures for robustness.

## 💡 Interview Extensions

1.  **Solve in O(N)**
    -   *Idea:* Build a **Suffix Automaton** (SAM).
    -   *Method:* Each node in SAM represents a set of substrings. Transitions represent adding characters. Count = $\sum (\text{longest}(u) - \text{shortest}(u) + 1)$.
2.  **Solve in O(N log N)**
    -   *Idea:* Build a **Suffix Array** and **LCP Array**.
    -   *Method:* Number of distinct substrings = $\frac{N(N+1)}{2} - \sum LCP[i]$.
    -   *Why:* $N(N+1)/2$ is total substrings. $LCP[i]$ counts duplicates between sorted suffixes.
3.  **K-th Lexicographically Smallest Substring**
    -   *Idea:* Use SAM or Suffix Array. With distinct counts per node, we can navigate to the K-th substring like in a BST.
