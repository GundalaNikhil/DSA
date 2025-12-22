---
problem_id: STC_LCS_TWO_STRINGS_SA__4927
display_id: STC-011
slug: lcs-two-strings-sa
title: "Longest Common Substring of Two Strings (SA)"
difficulty: Medium
difficulty_score: 56
topics:
  - Strings
  - Suffix Array
  - LCP
tags:
  - strings
  - suffix-array
  - lcp
  - medium
premium: true
subscription_tier: basic
---

# STC-011: Longest Common Substring of Two Strings (SA)

## 📋 Problem Summary

Given two strings `a` and `b`, find the length of the **Longest Common Substring**. This is the longest string that appears as a contiguous sequence of characters in both `a` and `b`.

## 🌍 Real-World Scenario

**Scenario Title:** Code Plagiarism Detection

Imagine you are a professor checking student assignments for plagiarism. Students might copy code but rename variables or reorder functions. However, significant chunks of logic often remain identical. By finding the longest common substring between two code submissions (after some normalization), you can detect if one student copied from another. If the longest common substring is unusually long, it's a strong indicator of copying.

**Why This Problem Matters:**

- **Bioinformatics:** Finding homologous regions in DNA or protein sequences.
- **Data Deduplication:** Identifying shared data chunks between files to save storage.
- **Spam Detection:** Finding common phrases in spam emails.

![Real-World Application](../images/STC-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `a = "abcd"`, `b = "bc"`.
Concatenate with sentinel: `S = "abcd#bc"`.

Suffixes of S (sorted):
1. `abcd#bc` (starts in `a`)
2. `bc` (starts in `b`)
3. `bcd#bc` (starts in `a`)
4. `c` (starts in `b`)
5. `cd#bc` (starts in `a`)
6. `d#bc` (starts in `a`)
... (and others starting with #)

Notice `bc` (from `b`) and `bcd#bc` (from `a`) are close in sorted order.
LCP("bc", "bcd#bc") = "bc" (length 2).
This is the longest common substring.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Contiguous:** Must be a substring, not a subsequence. "ace" is a subsequence of "abcde", but "abc" is a substring.
- **Sentinel:** Use a character like `#` or `$` that doesn't appear in `a` or `b`.
- **Constraints:** Total length up to 200,000. O(N^2) DP solution is too slow.

## Naive Approach

### Intuition

Check every substring of `a` to see if it exists in `b`.

### Algorithm

1. Iterate length `len` from `|a|` down to 1.
2. For each substring of `a` with length `len`:
3. Check if it is a substring of `b` (using `b.contains()` or similar).
4. If found, return `len`.

### Time Complexity

- **O(|a| * |b| * min(|a|, |b|))** or **O(|a|^2)** depending on implementation.
- Too slow.

### Space Complexity

- **O(1)**.

## Optimal Approach (SA + LCP)

### Key Insight

If a string `w` is a substring of both `a` and `b`, then `w` is a prefix of some suffix of `a` AND a prefix of some suffix of `b`.
If we construct the Suffix Array for `S = a + '#' + b`, all suffixes are sorted lexicographically.
Suffixes starting with the same prefix `w` will be grouped together.
The longest common substring will correspond to the maximum LCP between a suffix starting in `a` and a suffix starting in `b`.
Since the SA is sorted, we only need to check **adjacent** suffixes in the Suffix Array. If `sa[i]` and `sa[i+1]` belong to different original strings, their LCP is a candidate for the answer.

### Algorithm

1. Construct `S = a + '#' + b`.
2. Build Suffix Array (`sa`) and LCP Array (`lcp`) for `S`.
3. Iterate `i` from `0` to `|S| - 2`.
4. Check if `sa[i]` and `sa[i+1]` belong to different strings:
   - One index should be `< |a|`.
   - The other index should be `> |a|` (i.e., inside `b`).
5. If they are from different strings, update `max_len = max(max_len, lcp[i])`.
6. Return `max_len`.

### Time Complexity

- **O(N log N)**: Where `N = |a| + |b|`. Dominated by SA construction.

### Space Complexity

- **O(N)**: To store SA and LCP.

![Algorithm Visualization](../images/STC-011/algorithm-visualization.png)
![Algorithm Steps](../images/STC-011/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int longestCommonSubstring(String a, String b) {
        String s = a + "#" + b;
        int n = s.length();
        int splitIdx = a.length();
        
        // 1. Build SA
        Integer[] sa = new Integer[n];
        int[] rank = new int[n];
        int[] newRank = new int[n];
        
        for (int i = 0; i < n; i++) {
            sa[i] = i;
            rank[i] = s.charAt(i);
        }
        
        for (int k = 1; k < n; k *= 2) {
            int len = k;
            Arrays.sort(sa, (i, j) -> {
                if (rank[i] != rank[j]) return rank[i] - rank[j];
                int ri = (i + len < n) ? rank[i + len] : -1;
                int rj = (j + len < n) ? rank[j + len] : -1;
                return ri - rj;
            });
            
            newRank[sa[0]] = 0;
            for (int i = 1; i < n; i++) {
                int prev = sa[i - 1];
                int curr = sa[i];
                int r1 = rank[prev];
                int r2 = (prev + len < n) ? rank[prev + len] : -1;
                int r3 = rank[curr];
                int r4 = (curr + len < n) ? rank[curr + len] : -1;
                
                if (r1 == r3 && r2 == r4) newRank[curr] = newRank[prev];
                else newRank[curr] = newRank[prev] + 1;
            }
            System.arraycopy(newRank, 0, rank, 0, n);
            if (rank[sa[n - 1]] == n - 1) break;
        }
        
        // 2. Build LCP
        int[] lcp = new int[n - 1];
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] == n - 1) {
                k = 0;
                continue;
            }
            int j = sa[rank[i] + 1];
            while (i + k < n && j + k < n && s.charAt(i + k) == s.charAt(j + k)) {
                k++;
            }
            lcp[rank[i]] = k;
            if (k > 0) k--;
        }
        
        // 3. Find Max LCP between different strings
        int maxLen = 0;
        for (int i = 0; i < n - 1; i++) {
            // Check if sa[i] and sa[i+1] are from different strings
            boolean fromA = sa[i] < splitIdx;
            boolean fromB = sa[i+1] < splitIdx;
            
            // One from A (index < splitIdx) and one from B (index > splitIdx)
            // Note: index == splitIdx is the sentinel '#'
            if (fromA != fromB) {
                maxLen = Math.max(maxLen, lcp[i]);
            }
        }
        
        return maxLen;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String a = sc.next();
            if (sc.hasNext()) {
                String b = sc.next();
                Solution solution = new Solution();
                System.out.println(solution.longestCommonSubstring(a, b));
            }
        }
        sc.close();
    }
}
```

### Python

```python
def longest_common_substring(a: str, b: str) -> int:
    s = a + "#" + b
    n = len(s)
    split_idx = len(a)
    
    # 1. Build SA
    sa = list(range(n))
    rank = [ord(c) for c in s]
    new_rank = [0] * n
    
    k = 1
    while k < n:
        key_func = lambda i: (rank[i], rank[i + k] if i + k < n else -1)
        sa.sort(key=key_func)
        
        new_rank[sa[0]] = 0
        for i in range(1, n):
            prev = sa[i-1]
            curr = sa[i]
            if key_func(prev) == key_func(curr):
                new_rank[curr] = new_rank[prev]
            else:
                new_rank[curr] = new_rank[prev] + 1
        
        rank = list(new_rank)
        if rank[sa[n-1]] == n - 1:
            break
        k *= 2
        
    # 2. Build LCP
    lcp = [0] * (n - 1)
    k_val = 0
    for i in range(n):
        if rank[i] == n - 1:
            k_val = 0
            continue
        j = sa[rank[i] + 1]
        while i + k_val < n and j + k_val < n and s[i + k_val] == s[j + k_val]:
            k_val += 1
        lcp[rank[i]] = k_val
        if k_val > 0:
            k_val -= 1
            
    # 3. Find Max LCP
    max_len = 0
    for i in range(n - 1):
        idx1 = sa[i]
        idx2 = sa[i+1]
        
        from_a = idx1 < split_idx
        from_b = idx2 < split_idx
        
        if from_a != from_b:
            max_len = max(max_len, lcp[i])
            
    return max_len

def main():
    import sys
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    a, b = input_data[0], input_data[1]
    print(longest_common_substring(a, b))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestCommonSubstring(const string& a, const string& b) {
        string s = a + "#" + b;
        int n = s.length();
        int splitIdx = a.length();
        
        // 1. Build SA
        vector<int> sa(n), rank(n), newRank(n);
        for (int i = 0; i < n; i++) {
            sa[i] = i;
            rank[i] = s[i];
        }
        
        for (int k = 1; k < n; k *= 2) {
            auto cmp = [&](int i, int j) {
                if (rank[i] != rank[j]) return rank[i] < rank[j];
                int ri = (i + k < n) ? rank[i + k] : -1;
                int rj = (j + k < n) ? rank[j + k] : -1;
                return ri < rj;
            };
            sort(sa.begin(), sa.end(), cmp);
            
            newRank[sa[0]] = 0;
            for (int i = 1; i < n; i++) {
                if (cmp(sa[i - 1], sa[i])) newRank[sa[i]] = newRank[sa[i - 1]] + 1;
                else newRank[sa[i]] = newRank[sa[i - 1]];
            }
            rank = newRank;
            if (rank[sa[n - 1]] == n - 1) break;
        }
        
        // 2. Build LCP
        vector<int> lcp(n - 1);
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] == n - 1) {
                k = 0;
                continue;
            }
            int j = sa[rank[i] + 1];
            while (i + k < n && j + k < n && s[i + k] == s[j + k]) {
                k++;
            }
            lcp[rank[i]] = k;
            if (k > 0) k--;
        }
        
        // 3. Find Max
        int maxLen = 0;
        for (int i = 0; i < n - 1; i++) {
            bool fromA = sa[i] < splitIdx;
            bool fromB = sa[i+1] < splitIdx;
            
            if (fromA != fromB) {
                maxLen = max(maxLen, lcp[i]);
            }
        }
        return maxLen;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (cin >> a >> b) {
        Solution solution;
        cout << solution.longestCommonSubstring(a, b) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  longestCommonSubstring(a, b) {
    const s = a + "#" + b;
    const n = s.length;
    const splitIdx = a.length;
    
    // 1. Build SA
    let sa = new Array(n).fill(0).map((_, i) => i);
    let rank = new Array(n).fill(0).map((_, i) => s.charCodeAt(i));
    let newRank = new Array(n).fill(0);
    
    for (let k = 1; k < n; k *= 2) {
      sa.sort((i, j) => {
        if (rank[i] !== rank[j]) return rank[i] - rank[j];
        const ri = (i + k < n) ? rank[i + k] : -1;
        const rj = (j + k < n) ? rank[j + k] : -1;
        return ri - rj;
      });
      
      newRank[sa[0]] = 0;
      for (let i = 1; i < n; i++) {
        const prev = sa[i - 1];
        const curr = sa[i];
        const r1 = rank[prev];
        const r2 = (prev + k < n) ? rank[prev + k] : -1;
        const r3 = rank[curr];
        const r4 = (curr + k < n) ? rank[curr + k] : -1;
        
        if (r1 === r3 && r2 === r4) newRank[curr] = newRank[prev];
        else newRank[curr] = newRank[prev] + 1;
      }
      for (let i = 0; i < n; i++) rank[i] = newRank[i];
      if (rank[sa[n - 1]] === n - 1) break;
    }
    
    // 2. Build LCP
    const lcp = new Array(n - 1).fill(0);
    let kVal = 0;
    for (let i = 0; i < n; i++) {
      if (rank[i] === n - 1) {
        kVal = 0;
        continue;
      }
      const j = sa[rank[i] + 1];
      while (i + kVal < n && j + kVal < n && s[i + kVal] === s[j + kVal]) {
        kVal++;
      }
      lcp[rank[i]] = kVal;
      if (kVal > 0) kVal--;
    }
    
    // 3. Find Max
    let maxLen = 0;
    for (let i = 0; i < n - 1; i++) {
      const idx1 = sa[i];
      const idx2 = sa[i+1];
      
      const fromA = idx1 < splitIdx;
      const fromB = idx2 < splitIdx;
      
      if (fromA !== fromB) {
        maxLen = Math.max(maxLen, lcp[i]);
      }
    }
    return maxLen;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length < 2) return;
  const a = data[0];
  const b = data[1];
  const solution = new Solution();
  console.log(solution.longestCommonSubstring(a, b).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

`a = "abcd"`, `b = "bc"`
`S = "abcd#bc"`
SA:
0. `#bc` (4)
1. `abcd#bc` (0)
2. `bc` (5) - from B
3. `bcd#bc` (1) - from A
4. `c` (6) - from B
5. `cd#bc` (2) - from A
6. `d#bc` (3) - from A

LCP:
- `#` vs `abcd`: 0
- `abcd` vs `bc`: 0
- `bc` vs `bcd`: 2 ("bc") -> `sa[2]=5` (B), `sa[3]=1` (A). Diff strings. `maxLen = 2`.
- `bcd` vs `c`: 0
- `c` vs `cd`: 1 ("c") -> `sa[4]=6` (B), `sa[5]=2` (A). Diff strings. `maxLen` stays 2 (1 < 2).
- `cd` vs `d`: 0

Result: 2.

![Example Visualization](../images/STC-011/example-1.png)

## ✅ Proof of Correctness

### Invariant

The longest common substring corresponds to the maximum LCP between a suffix of `a` and a suffix of `b`.
In the sorted Suffix Array, suffixes starting with the same prefix are grouped together.
The "best" match for any suffix `u` is either its immediate predecessor or immediate successor in the SA.
Thus, we only need to check adjacent pairs `(sa[i], sa[i+1])` in the SA. If they belong to different strings, their LCP is a candidate.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: K Strings**

- **Extension 2: Generalized Suffix Tree**
  - Build a suffix tree for multiple strings. Find the deepest node marked with all string IDs.

### Common Mistakes to Avoid

1. **Sentinel Character**
   - ❌ `a + b`. If `a="ab"`, `b="ba"`, `S="abba"`. Suffix "abba" (from a) and "ba" (from b) might mix.
   - ✅ `a + '#' + b`.

2. **Checking Origin**
   - ❌ `max(lcp)`.
   - ✅ `max(lcp)` only if `sa[i]` and `sa[i+1]` are from different strings. Otherwise, we might find a repeated substring inside `a` itself.

## Related Concepts

- **Suffix Automaton**: Can solve this by building automaton for `a` and streaming `b` through it.
- **DP**: O(|a|*|b|) solution using `dp[i][j]`.
