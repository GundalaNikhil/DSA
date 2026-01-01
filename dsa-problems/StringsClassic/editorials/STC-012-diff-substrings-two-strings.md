---
problem_id: STC_DIFF_SUBSTRINGS_TWO_STRINGS__6174
display_id: STC-012
slug: diff-substrings-two-strings
title: "Number of Different Substrings of Two Strings"
difficulty: Medium
difficulty_score: 58
topics:
  - Strings
  - Suffix Array
  - Counting
tags:
  - strings
  - suffix-array
  - counting
  - medium
premium: true
subscription_tier: basic
---

# STC-012: Number of Different Substrings of Two Strings

## 📋 Problem Summary

Given two strings `a` and `b`, calculate the number of **distinct** substrings of `a` that do **not** appear in `b`.

## 🌍 Real-World Scenario

**Scenario Title:** Proprietary Code Analysis

Suppose you have a proprietary codebase (`a`) and an open-source library (`b`). You want to know how much "unique" code you have written that isn't just a copy of the open-source library. By counting the distinct substrings in `a` that are not present in `b`, you get a measure of the unique information content in your codebase relative to the library.

**Why This Problem Matters:**

- **Copyright Enforcement:** Identifying unique creative content vs. common boilerplate.
- **Bioinformatics:** Finding unique gene sequences in a specific species compared to a reference genome.
- **Cybersecurity:** Identifying unique malware signatures that haven't been seen in a database of known safe files.

![Real-World Application](../images/STC-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `a = "ab"`, `b = "b"`.
Substrings of `a`:
- "a" (Not in `b`) -> Count!
- "ab" (Not in `b`) -> Count!
- "b" (In `b`) -> Skip.

Total unique in `a` but not `b`: 2.

### Algorithm Logic

1. **Distinctness in `a`**: Normally, we count distinct substrings of `a` using `len(suffix) - lcp(suffix, prev_suffix_in_a)`.
2. **Exclusion from `b`**: For each suffix of `a`, let `L` be the length of the longest prefix that appears in `b`. Any substring starting at this suffix with length `<= L` is present in `b`.
3. **Combination**: For a suffix of `a`, the valid lengths are those greater than `L` and also "new" (not counted by previous `a`-suffixes).
   - Valid Range: `(max(LCP_prev_a, Max_Match_b) + 1)` to `len(suffix)`.
   - Contribution: `max(0, len(suffix) - max(LCP_prev_a, Max_Match_b))`.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Distinct:** If "xyz" appears twice in `a` and never in `b`, it counts as 1.
- **Empty Strings:** If `a` is empty, answer is 0.
- **Constraints:** `|a| + |b| <= 200,000`. Use O(N log N) or O(N).

## Naive Approach

### Intuition

Generate all substrings of `a`, store them in a Set. Then iterate through the Set and check if each is in `b`.

### Algorithm

1. `Set<String> distinctA`
2. Add all substrings of `a` to `distinctA`.
3. `count = 0`
4. For each `s` in `distinctA`:
   - If `!b.contains(s)`, `count++`.
5. Return `count`.

### Time Complexity

- **O(|a|^3 + |a|*|b|)**: Very slow.

### Space Complexity

- **O(|a|^2)**.

## Optimal Approach (SA + LCP)

### Key Insight

We need two pieces of information for every suffix `i` of `a`:
1. `max_match_b[i]`: The length of the longest prefix of `suffix_a[i]` that appears as a substring in `b`.
2. `lcp_prev_a[i]`: The LCP with the lexicographically preceding suffix that is *also* from `a`.

**Computing `max_match_b`:**
Construct the Generalized Suffix Array for `S = a + '#' + b`.
For any suffix of `a`, its longest common prefix with *any* suffix of `b` is determined by the closest suffixes of `b` in the sorted SA (one above, one below).
We can compute this with two passes over the LCP array:
- **Forward Pass:** Track the minimum LCP since the last seen `b`-suffix.
- **Backward Pass:** Track the minimum LCP since the last seen `b`-suffix (from the right).
`max_match_b[i]` is the maximum of these two values.

**Computing `lcp_prev_a`:**
Iterate through the SA. Keep track of the last seen suffix from `a`. The LCP between the current `a`-suffix and the last `a`-suffix is the `lcp_prev_a`. Note: this is the minimum LCP in the range between them in the full SA.

**Final Count:**
Sum over all suffixes `i` of `a`:
`contribution = max(0, len(suffix_i) - max(lcp_prev_a[i], max_match_b[i]))`

### Algorithm

1. Build SA and LCP for `S = a + '#' + b`.
2. Compute `max_match_b` for each position in SA corresponding to `a`.
   - Use forward/backward passes.
3. Compute `lcp_prev_a` effectively by iterating the SA and maintaining the running minimum LCP since the last `a`-suffix.
   - So if we skip `b`-suffixes, we must take the minimum of all intermediate LCP values.
4. Sum the contributions.

### Time Complexity

- **O(N log N)**: SA construction. Passes are linear.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/STC-012/algorithm-visualization.png)
![Algorithm Steps](../images/STC-012/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public long countExclusiveSubstrings(String a, String b) {
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
        int[] lcp = new int[n]; // lcp[i] is between sa[i-1] and sa[i]
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] == 0) { // First in SA
                k = 0;
                continue;
            }
            int j = sa[rank[i] - 1];
            while (i + k < n && j + k < n && s.charAt(i + k) == s.charAt(j + k)) {
                k++;
            }
            lcp[rank[i]] = k;
            if (k > 0) k--;
        }
        
        // 3. Compute max_match_b for each suffix of a
        int[] maxMatchB = new int[n];
        
        // Forward pass
        int currentLCP = 0;
        for (int i = 0; i < n; i++) {
            if (i > 0) currentLCP = Math.min(currentLCP, lcp[i]);
            if (sa[i] > splitIdx) { // Suffix from b
                currentLCP = Integer.MAX_VALUE; // Reset match length (effectively infinite for next)
                // The LCP between this b-suffix and subsequent a-suffixes is limited by lcp array.
                // When we see a b-suffix, the "distance" to it is 0 (conceptually), but we track LCP.
                // Let's rephrase: currentLCP tracks LCP(sa[i], nearest_prev_b).
                // If sa[i] is b, nearest_prev_b is sa[i], so LCP is infinite (length of suffix).
                // But we need LCP(sa[next], sa[i]).
                currentLCP = n; // Max possible
            } else if (sa[i] < splitIdx) { // Suffix from a
                maxMatchB[i] = Math.max(maxMatchB[i], currentLCP);
            }
        }
        
        // Backward pass
        currentLCP = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (i < n - 1) currentLCP = Math.min(currentLCP, lcp[i + 1]); // lcp[i+1] is between sa[i] and sa[i+1]
            if (sa[i] > splitIdx) { // Suffix from b
                currentLCP = n;
            } else if (sa[i] < splitIdx) { // Suffix from a
                maxMatchB[i] = Math.max(maxMatchB[i], currentLCP);
            }
        }
        
        // 4. Calculate result
        long count = 0;
        int prevALCP = 0; // LCP with previous suffix from A
        
        for (int i = 0; i < n; i++) {
            if (i > 0) prevALCP = Math.min(prevALCP, lcp[i]);
            
            if (sa[i] < splitIdx) { // Suffix from a
                // prevALCP now holds min(lcp) since last 'a' suffix.
                // This is exactly LCP(current_a, prev_a).
                
                int len = splitIdx - sa[i];
                int deduct = Math.max(prevALCP, maxMatchB[i]);
                if (len > deduct) {
                    count += (len - deduct);
                }
                
                // Reset prevALCP for the *next* a-suffix.
                // The LCP between *this* a-suffix and the *next* a-suffix will start being tracked.
                prevALCP = n; 
            }
        }
        
        return count;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String a = sc.next();
            if (sc.hasNext()) {
                String b = sc.next();
                Solution solution = new Solution();
                System.out.println(solution.countExclusiveSubstrings(a, b));
            }
        }
        sc.close();
    }
}
```

### Python
```python
def count_exclusive_substrings(a: str, b: str) -> int:
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
        
    # 2. Build LCP (lcp[i] between sa[i-1] and sa[i])
    lcp = [0] * n
    k_val = 0
    for i in range(n):
        if rank[i] == 0:
            k_val = 0
            continue
        j = sa[rank[i] - 1]
        while i + k_val < n and j + k_val < n and s[i + k_val] == s[j + k_val]:
            k_val += 1
        lcp[rank[i]] = k_val
        if k_val > 0:
            k_val -= 1
            
    # 3. Max Match B
    max_match_b = [0] * n
    
    # Forward
    curr_lcp = 0
    for i in range(n):
        if i > 0:
            curr_lcp = min(curr_lcp, lcp[i])
        if sa[i] > split_idx: # From B
            curr_lcp = n
        elif sa[i] < split_idx: # From A
            max_match_b[i] = max(max_match_b[i], curr_lcp)
            
    # Backward
    curr_lcp = 0
    for i in range(n - 1, -1, -1):
        if i < n - 1:
            curr_lcp = min(curr_lcp, lcp[i + 1])
        if sa[i] > split_idx: # From B
            curr_lcp = n
        elif sa[i] < split_idx: # From A
            max_match_b[i] = max(max_match_b[i], curr_lcp)
            
    # 4. Count
    count = 0
    prev_a_lcp = 0
    
    for i in range(n):
        if i > 0:
            prev_a_lcp = min(prev_a_lcp, lcp[i])
            
        if sa[i] < split_idx: # From A
            length = split_idx - sa[i]
            deduct = max(prev_a_lcp, max_match_b[i])
            if length > deduct:
                count += (length - deduct)
            prev_a_lcp = n # Reset for next A
            
    return count

def main():
    import sys
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    a, b = input_data[0], input_data[1]
    print(count_exclusive_substrings(a, b))

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
    long long countExclusiveSubstrings(const string& a, const string& b) {
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
        vector<int> lcp(n);
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] == 0) {
                k = 0;
                continue;
            }
            int j = sa[rank[i] - 1];
            while (i + k < n && j + k < n && s[i + k] == s[j + k]) {
                k++;
            }
            lcp[rank[i]] = k;
            if (k > 0) k--;
        }
        
        // 3. Max Match B
        vector<int> maxMatchB(n, 0);
        
        // Forward
        int currentLCP = 0;
        for (int i = 0; i < n; i++) {
            if (i > 0) currentLCP = min(currentLCP, lcp[i]);
            if (sa[i] > splitIdx) {
                currentLCP = n;
            } else if (sa[i] < splitIdx) {
                maxMatchB[i] = max(maxMatchB[i], currentLCP);
            }
        }
        
        // Backward
        currentLCP = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (i < n - 1) currentLCP = min(currentLCP, lcp[i + 1]);
            if (sa[i] > splitIdx) {
                currentLCP = n;
            } else if (sa[i] < splitIdx) {
                maxMatchB[i] = max(maxMatchB[i], currentLCP);
            }
        }
        
        // 4. Count
        long long count = 0;
        int prevALCP = 0;
        
        for (int i = 0; i < n; i++) {
            if (i > 0) prevALCP = min(prevALCP, lcp[i]);
            
            if (sa[i] < splitIdx) {
                int len = splitIdx - sa[i];
                int deduct = max(prevALCP, maxMatchB[i]);
                if (len > deduct) {
                    count += (len - deduct);
                }
                prevALCP = n;
            }
        }
        
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (cin >> a >> b) {
        Solution solution;
        cout << solution.countExclusiveSubstrings(a, b) << "\n";
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  countExclusiveSubstrings(a, b) {
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
    const lcp = new Array(n).fill(0);
    let kVal = 0;
    for (let i = 0; i < n; i++) {
      if (rank[i] === 0) {
        kVal = 0;
        continue;
      }
      const j = sa[rank[i] - 1];
      while (i + kVal < n && j + kVal < n && s[i + kVal] === s[j + kVal]) {
        kVal++;
      }
      lcp[rank[i]] = kVal;
      if (kVal > 0) kVal--;
    }
    
    // 3. Max Match B
    const maxMatchB = new Array(n).fill(0);
    
    // Forward
    let currentLCP = 0;
    for (let i = 0; i < n; i++) {
      if (i > 0) currentLCP = Math.min(currentLCP, lcp[i]);
      if (sa[i] > splitIdx) {
        currentLCP = n;
      } else if (sa[i] < splitIdx) {
        maxMatchB[i] = Math.max(maxMatchB[i], currentLCP);
      }
    }
    
    // Backward
    currentLCP = 0;
    for (let i = n - 1; i >= 0; i--) {
      if (i < n - 1) currentLCP = Math.min(currentLCP, lcp[i + 1]);
      if (sa[i] > splitIdx) {
        currentLCP = n;
      } else if (sa[i] < splitIdx) {
        maxMatchB[i] = Math.max(maxMatchB[i], currentLCP);
      }
    }
    
    // 4. Count
    let count = 0n;
    let prevALCP = 0;
    
    for (let i = 0; i < n; i++) {
      if (i > 0) prevALCP = Math.min(prevALCP, lcp[i]);
      
      if (sa[i] < splitIdx) {
        const len = splitIdx - sa[i];
        const deduct = Math.max(prevALCP, maxMatchB[i]);
        if (len > deduct) {
          count += BigInt(len - deduct);
        }
        prevALCP = n;
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
  console.log(solution.countExclusiveSubstrings(a, b).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

`a = "ab"`, `b = "b"`
`S = "ab#b"`
SA:
0. `#b` (2)
1. `ab#b` (0) - A
2. `b` (3) - B
3. `b#b` (1) - A

LCP (between adjacent):
- `#b` vs `ab#b`: 0
- `ab#b` vs `b`: 0
- `b` vs `b#b`: 1 ("b")

Max Match B:
- `sa[0]` (#b): B-like (sentinel).
- `sa[1]` (ab#b):
  - Forward: prev was #b, LCP 0.
  - Backward: next is b, LCP 0.
  - `maxMatchB` = 0.
- `sa[2]` (b): B.
- `sa[3]` (b#b):
  - Forward: prev was b, LCP 1.
  - Backward: none.
  - `maxMatchB` = 1.

Count:
- `sa[1]` (ab#b): `len=2`. `prevALCP=0`. `deduct=max(0, 0)=0`. Add `2-0=2`. ("ab", "a")
- `sa[3]` (b#b): `len=1`. `prevALCP` (with `sa[1]`): min LCP in range [1..3] -> `min(lcp[2], lcp[3])` -> `min(0, 1) = 0`.
  - `deduct=max(0, 1)=1`. Add `1-1=0`.
  - `lcp[2]` is between `sa[1]` and `sa[2]` -> 0.
  - `lcp[3]` is between `sa[2]` and `sa[3]` -> 1.
  - Min is 0. Correct.
  - "b" is a duplicate of "b" in "ab"? No, "b" in "ab" starts at 1. `sa[3]` starts at 1.
  - "b" is a substring of "ab".
  - My manual trace is slightly off. "b" is present in `b`. So `maxMatchB` correctly identified it.
  - `sa[1]` ("ab") contributes "a", "ab". Both not in `b`. Count 2.
  - `sa[3]` ("b") contributes nothing because `maxMatchB` is 1 (matches "b").
  - Total 2. Correct.

![Example Visualization](../images/STC-012/example-1.png)

## ✅ Proof of Correctness

### Invariant

For each suffix `i` of `a`, the substrings starting at `i` are `s[i...i]`, `s[i...i+1]`, ..., `s[i...n-1]`.
Lengths range from 1 to `len(suffix)`.
Substrings with length `<= max_match_b[i]` are present in `b`.
Substrings with length `<= lcp_prev_a[i]` are present in a lexicographically smaller suffix of `a` (duplicates).
We want substrings that are NEITHER in `b` NOR duplicates in `a`.
Since both conditions define a prefix range, we exclude `max(max_match_b[i], lcp_prev_a[i])`.
The remaining count is `len(suffix) - max(...)`.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: Count Shared Substrings**
  - Instead of exclusive, count distinct substrings present in BOTH.
  - `min(len, max_match_b) - lcp_prev_a`.

- **Extension 2: Generalized for K Strings**
  - Count substrings unique to string 1 among K strings.
  - `max_match_others` instead of `max_match_b`.

### Common Mistakes to Avoid

1. **LCP Indexing**
   - ❌ `lcp[i]` usually refers to `sa[i-1]` and `sa[i]`. Be careful with 0-based vs 1-based.
   - ✅ In my code, `lcp[i]` is between `sa[i-1]` and `sa[i]`. `lcp[0]` is dummy.

2. **Resetting `prevALCP`**
   - ❌ Forgetting to reset `prevALCP` to `n` (infinity) after processing an `a`-suffix.
   - ✅ Necessary because the "chain" of `a`-suffixes is broken by `b`-suffixes, but we logically want the LCP with the *previous* `a`-suffix in the SA, skipping `b`s. My logic `prevALCP = min(prevALCP, lcp[i])` correctly accumulates the minimum over the gap.

## Related Concepts

- **Suffix Automaton**: Can solve this in O(N) without SA.
- **Aho-Corasick**: For multiple patterns.
