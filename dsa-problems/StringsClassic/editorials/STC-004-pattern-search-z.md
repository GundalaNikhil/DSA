---
problem_id: STC_PATTERN_SEARCH_Z__4681
display_id: STC-004
slug: pattern-search-z
title: "Pattern Search With Z-Function"
difficulty: Easy
difficulty_score: 32
topics:
  - Strings
  - Z-Algorithm
  - Pattern Matching
tags:
  - strings
  - z-function
  - pattern-search
  - easy
premium: true
subscription_tier: basic
---

# STC-004: Pattern Search With Z-Function

## 📋 Problem Summary

Given a pattern `p` and a text `t`, you need to find all starting indices in `t` where `p` occurs as a substring. You are required to use the **Z-function** algorithm. The output must be a sorted list of 0-based indices.

## 🌍 Real-World Scenario

**Scenario Title:** Plagiarism Detection

In plagiarism detection systems, we often need to check if specific phrases or sentences from a source document appear in a submitted document. If we treat the "suspicious phrase" as the pattern `p` and the "submitted document" as the text `t`, we need to find all occurrences of `p` in `t`. The Z-algorithm allows us to do this efficiently, even for very long documents, by essentially comparing the pattern against every suffix of the text simultaneously.

**Why This Problem Matters:**

- **Alternative to KMP:** While KMP is popular, the Z-algorithm is often easier to understand and implement for certain types of string problems (like finding the longest common prefix of all suffixes).
- **Bioinformatics:** Used for finding motifs in DNA sequences.
- **Efficiency:** Linear time complexity is essential for processing large datasets.

![Real-World Application](../images/STC-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `p = "aa"` and `t = "aaa"`.
We construct a new string `S = p + '#' + t`.
`S = "aa#aaa"`

```
Index: 0 1 2 3 4 5
Char:  a a # a a a

Z-values for S:
Index 0 ('a'): Z[0] = 6 (length of S)
Index 1 ('a'): Z[1] = 1 ("a" matches "a", but "a#" != "aa")
Index 2 ('#'): Z[2] = 0 (starts with #)
Index 3 ('a'): Z[3] = 2 ("aa" matches prefix "aa") -> Match!
Index 4 ('a'): Z[4] = 2 ("aa" matches prefix "aa") -> Match!
Index 5 ('a'): Z[5] = 1 ("a" matches "a", but end of string)

Matches found at indices corresponding to 3 and 4 in S.
Map back to t:
Index 3 in S corresponds to index 0 in t.
Index 4 in S corresponds to index 1 in t.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Sentinel Character:** You MUST use a character that does not appear in `p` or `t` (e.g., `#`, `$`, `\0`) to separate them. This prevents matches from spanning across the boundary of `p` and `t`.
- **Indices:** The problem asks for indices in `t`. If `S = p + '#' + t`, an index `i` in `S` corresponds to `i - |p| - 1` in `t`.
- **Constraints:** `|p|, |t| <= 200,000`. Total length <= 400,001.

## Naive Approach

### Intuition

Check every position in `t` to see if `p` starts there.

### Algorithm

1. Iterate `i` from `0` to `|t| - |p|`.
2. Compare `t[i...i+|p|-1]` with `p`.
3. If equal, add `i` to result.

### Time Complexity

- **O(|p| * |t|)**: Too slow.

### Space Complexity

- **O(1)**.

## Optimal Approach (Z-Algorithm)

### Key Insight

By concatenating `p`, a sentinel `#`, and `t`, we create a single string `S`. Computing the Z-array for `S` tells us, for every position `i`, the length of the longest substring starting at `i` that matches the prefix of `S`.
Since the prefix of `S` is `p`, `Z[i]` tells us the length of the match between `p` and the suffix of `S` starting at `i`.
If `Z[i] == |p|`, it means `p` fully matches the substring starting at `i`.

### Algorithm

1. Construct `S = p + "#" + t`.
2. Compute the Z-array for `S`.
3. Iterate through the Z-array starting from index `|p| + 1` (the start of `t`).
4. If `Z[i] == |p|` (it can't be greater because of the sentinel), then we found a match.
5. The starting index in `t` is `i - (|p| + 1)`.

### Time Complexity

- **O(|p| + |t|)**: Constructing `S` takes linear time. Computing Z-array takes linear time. Scanning Z-array takes linear time.

### Space Complexity

- **O(|p| + |t|)**: To store `S` and the Z-array.

![Algorithm Visualization](../images/STC-004/algorithm-visualization.png)
![Algorithm Steps](../images/STC-004/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public int[] findOccurrences(String p, String t) {
        String s = p + "#" + t;
        int n = s.length();
        int[] z = new int[n];
        int l = 0, r = 0;
        
        // Compute Z-array
        for (int i = 1; i < n; i++) {
            if (i <= r) {
                z[i] = Math.min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i])) {
                z[i]++;
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        
        // Collect matches
        List<Integer> matches = new ArrayList<>();
        int pLen = p.length();
        for (int i = pLen + 1; i < n; i++) {
            if (z[i] == pLen) {
                matches.add(i - (pLen + 1));
            }
        }
        
        return matches.stream().mapToInt(i -> i).toArray();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String t = sc.next();
            String p = sc.next();

            Solution solution = new Solution();
            int[] result = solution.findOccurrences(p, t);

            if (result.length == 0) {
                System.out.println("-1");
            } else {
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < result.length; i++) {
                    if (i > 0) sb.append(' ');
                    sb.append(result[i]);
                }
                System.out.println(sb.toString());
            }
        }
        sc.close();
    }
}
```

### Python
```python
def find_occurrences(p: str, t: str) -> list[int]:
    s = p + "#" + t
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    
    # Compute Z-array
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
            
    # Collect matches
    matches = []
    p_len = len(p)
    for i in range(p_len + 1, n):
        if z[i] == p_len:
            matches.append(i - (p_len + 1))
            
    return matches

def main():
    import sys
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    t = input_data[0]
    p = input_data[1]
    result = find_occurrences(p, t)
    if not result:
        print("-1")
    else:
        print(*(result))

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> findOccurrences(const string& p, const string& t) {
        string s = p + "#" + t;
        int n = s.length();
        vector<int> z(n);
        int l = 0, r = 0;
        
        // Compute Z-array
        for (int i = 1; i < n; i++) {
            if (i <= r) {
                z[i] = min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
                z[i]++;
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        
        // Collect matches
        vector<int> matches;
        int pLen = p.length();
        for (int i = pLen + 1; i < n; i++) {
            if (z[i] == pLen) {
                matches.push_back(i - (pLen + 1));
            }
        }
        return matches;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string t, p;
    if (cin >> t >> p) {
        Solution solution;
        vector<int> result = solution.findOccurrences(p, t);
        if (result.empty()) {
            cout << "-1\n";
        } else {
            for (int i = 0; i < (int)result.size(); i++) {
                if (i > 0) cout << " ";
                cout << result[i];
            }
            cout << "\n";
        }
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  findOccurrences(p, t) {
    const s = p + "#" + t;
    const n = s.length;
    const z = new Array(n).fill(0);
    let l = 0, r = 0;
    
    // Compute Z-array
    for (let i = 1; i < n; i++) {
      if (i <= r) {
        z[i] = Math.min(r - i + 1, z[i - l]);
      }
      while (i + z[i] < n && s[z[i]] === s[i + z[i]]) {
        z[i]++;
      }
      if (i + z[i] - 1 > r) {
        l = i;
        r = i + z[i] - 1;
      }
    }
    
    // Collect matches
    const matches = [];
    const pLen = p.length;
    for (let i = pLen + 1; i < n; i++) {
      if (z[i] === pLen) {
        matches.push(i - (pLen + 1));
      }
    }
    return matches;
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
  const t = data[0];
  const p = data[1];
  const solution = new Solution();
  const result = solution.findOccurrences(p, t);
  if (result.length === 0) {
    console.log("-1");
  } else {
    console.log(result.join(" "));
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

`p = "aa"`, `t = "aaa"`
`S = "aa#aaa"`
`|p| = 2`

1.  **Z-Array Computation**:
    - `i=0`: `Z[0]=6` (unused)
    - `i=1`: `S[1..]`="a#aaa". Match "a" with "a". `Z[1]=1`.
    - `i=2`: `S[2..]`="#aaa". `Z[2]=0`.
    - `i=3`: `S[3..]`="aaa". Match "aa" with "aa". `Z[3]=2`.
    - `i=4`: `S[4..]`="aa". Match "aa" with "aa". `Z[4]=2`.
    - `i=5`: `S[5..]`="a". Match "a" with "a". `Z[5]=1`.

2.  **Scanning**:
    - Start at `i = |p| + 1 = 3`.
    - `i=3`: `Z[3] == 2`. Match! Index `3 - 3 = 0`.
    - `i=4`: `Z[4] == 2`. Match! Index `4 - 3 = 1`.
    - `i=5`: `Z[5] == 1`. No match.

Result: `0 1`.

![Example Visualization](../images/STC-004/example-1.png)

## ✅ Proof of Correctness

### Invariant

`Z[i]` stores the length of the longest common prefix between `S` and `S[i...]`.
Since `S` starts with `p`, `Z[i]` is the length of the longest common prefix between `p` and `S[i...]`.

### Why the approach is correct

- We are interested in suffixes of `S` that start inside the `t` part (indices `> |p|`).
- A suffix starting at `i` in `S` corresponds to a suffix starting at `i - |p| - 1` in `t`.
- If `Z[i] == |p|`, it means `p` matches the prefix of this suffix.
- The sentinel `#` ensures `Z[i]` cannot be greater than `|p|` (unless `p` itself contains `#`, which is forbidden).

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: Count Occurrences**
  - Trivial modification.

- **Extension 2: Longest Prefix of P in T**
  - Find `max(Z[i])` for `i > |p|`. This tells you the longest prefix of `p` that appears as a substring in `t`.

- **Extension 3: Periodicity of P**
  - You can use the Z-values of `p` (which are computed as part of the Z-array of `S`) to determine the period of `p`.

### Common Mistakes to Avoid

1. **Forgetting the Sentinel**
   - ❌ `S = p + t`. If `p="a"`, `t="aa"`, `S="aaa"`. `Z[1]=2`. `Z[2]=1`. Correct.
   - But if `p="aa"`, `t="a"`, `S="aaa"`. `Z[1]=2`. We might think we found a match of length 2 at index 1, but `t` only has length 1. The sentinel forces the match to stop at the boundary.

2. **Index Mapping Errors**
   - ❌ `matches.add(i)`.
   - ✅ `matches.add(i - |p| - 1)`.

3. **Memory Limit**
   - Creating `S` takes extra space. For extremely large strings, you might need to implement Z-algo without explicit concatenation (simulating it), but usually O(N) space is fine.

## Related Concepts

- **KMP Algorithm**: Uses O(|p|) space instead of O(|p|+|t|).
- **Aho-Corasick**: For multiple patterns.
- **Suffix Automaton**: For more complex queries.
